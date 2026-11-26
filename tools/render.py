#!/usr/bin/env python3
"""Рендер 3D-роликов LapRadar Studio: tools/video3d/<тема>.py (VIDEO) → media/render/<id>-<lang>.mp4 (без звука) + .json (тайминг сцен).
Заголовки берутся из статьи content/articles/<slug>.json. Звук (озвучка по сценам) накладывает сервер: deploy/media.sh.

  python3 tools/render.py tools/video3d/qatar.py [--lang ru] [--frames 0:60] [--still 45]
"""
import asyncio, base64, functools, http.server, importlib.util, json, os, subprocess, sys, threading, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'media', 'render')
CPS = 17.5
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slides import SPOKEN  # «как читает диктор» → «как пишем в субтитрах»  # символов озвучки в секунду (замерено по Piper/Edge на 4 языках)


def load(path):
    sp = importlib.util.spec_from_file_location('c', path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    v = m.VIDEO; art = {'slug': v['slug'], 'video3d': v, 'videoId': v.get('id', v['slug']), 'titles': v.get('titles'), 'captions': v.get('captions')}
    f = os.path.join(ROOT, 'content', 'articles', v['slug'] + '.json')
    if os.path.exists(f): art['i18n'] = json.load(open(f))['i18n']
    return art


# какие машины двигает каждая анимация (act): камера chase должна смотреть на одну из них, остальные машины в такой сцене скрыты
ACT_CARS = {'duel': {0, 1}, 'follow': {0, 1}, 'boost': {0, 1}, 'wings': {0, 1}, 'speed': {0, 1}, 'heat': {0, 1}, 'cold': {0, 1}, 'manhole': {0, 1},
            'narrow': {0, 1}, 'race2': {0, 1}, 'trace': {0}, 'energy': {0}, 'fade': {0, 1, 2}, 'convoy': {0, 1, 2, 3}, 'restart': set(range(10))}
def lint(v):
    """Проверка сценария до рендера: камера на машине, которой нет в кадре, число сцен и кадров."""
    out = []
    for i, sh in enumerate(v['shots']):
        a = sh.get('act') or {}; t = a.get('type')
        if sh.get('type') != 'chase' or sh.get('follow') or not t: continue
        ctl = ACT_CARS.get(t)
        if t == 'slide': ctl = {0, *a.get('followers', [1, 2])}
        if t == 'pit': ctl = {a.get('car', 0)} | ({a['rival']} if 'rival' in a else set())
        if t == 'pitexit': ctl = {a.get('pitcar', 0), a.get('car', 1)}
        if t == 'duel' and sh.get('car', 0) == 1: out.append(f'сцена {i + 1}: duel с камерой на машине 1 — отстающая машина 0 пролетает сквозь камеру, ставь car 0')
        if ctl is not None and sh.get('car', 0) not in ctl: out.append(f'сцена {i + 1}: камера на машине {sh.get("car", 0)}, а act {t} двигает только {sorted(ctl)}')
    for lang, sc in v['scenes'].items():
        if len(sc) != len(v['shots']): out.append(f'{lang}: сцен {len(sc)}, а камер {len(v["shots"])}')
    return out


def plan(art, lang):
    v = art['video3d']
    scenes = []
    for sc in v['scenes'][lang]:
        say = sc.get('say', '')
        cps = {'zh': 4.6, 'de': 16.0}.get(lang, CPS)  # китайский читается по иероглифам, немецкий чуть медленнее
        dur = max(sc.get('min', 2.6), round(len(say) / cps + 0.55, 2))
        cap = say
        for a, b in SPOKEN: cap = cap.replace(a, b)
        scenes.append({**sc, 'cap': cap, 'dur': dur, 'url': f"lapradar.com/a/{art['slug']}" if art.get('i18n') else 'lapradar.com'})
    # кадры сцен общие для всех языков: камера из shots
    for sc, shot in zip(scenes, v['shots']): sc['shot'] = shot
    out = {'track': v['track'], 'theme': v.get('theme', 'night'), 'city': v.get('city', False), 'style': v.get('style', 'tt'), 'brand3d': v.get('brand3d', True), 'fps': 30, 'scenes': scenes}
    if v.get('hq'): out['hq'] = v['hq']  # HQ-режим студии (свет, тени, bloom, детальные машины): только у роликов, где он задан
    if v.get('look'): out['look'] = v['look']  # look cinema (реалистичный свет, motion blur, DoF, грейдинг): только у роликов, где он задан
    return out


def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
    h.log_message = lambda *a: None
    s = http.server.ThreadingHTTPServer(('127.0.0.1', 0), h)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s.server_address[1]


async def render(art, lang, frames=None, still=None, wide=False):
    from playwright.async_api import async_playwright
    port = serve(); spec = plan(art, lang)
    if wide: spec['w'], spec['h'] = 1920, 1080  # горизонтальная версия для статьи
    spec['q3d'] = float(os.environ.get('Q3D', art['video3d'].get('q3d', '0.667')))  # 3D в ~720p, текст в 1080p: почти вдвое быстрее
    vid = art.get('videoId') or art['slug']; suf = '-wide' if wide else ''
    os.makedirs(OUT, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
        pg = await b.new_page(viewport={'width': 540, 'height': 960})
        logs = []; pg.on('console', lambda m: logs.append(m.text)); pg.on('pageerror', lambda e: logs.append('ERR ' + str(e)))
        await pg.goto(f'http://127.0.0.1:{port}/tools/studio/studio.html')
        await pg.wait_for_function('window.studioReady === true', timeout=30000)
        info = await pg.evaluate('s => window.setupVideo(s)', spec)
        if logs: print('\n'.join(logs[-10:]))
        n = info['frames']
        if still is not None:
            data = await pg.evaluate('i => window.renderFrame(i)', still)
            f = os.path.join('/tmp', f'still-{vid}-{lang}{suf}-{still}.jpg'); open(f, 'wb').write(base64.b64decode(data.split(',', 1)[1])); print(f); await b.close(); return f
        a, z = (0, n) if not frames else map(int, frames.split(':'))
        dst = os.path.join(OUT, f'{vid}-{lang}{suf}.mp4')
        ff = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'image2pipe', '-framerate', '30', '-c:v', 'mjpeg', '-i', '-',
                               '-c:v', 'libx264', '-preset', 'medium', '-crf', '24', '-tune', 'animation', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', dst], stdin=subprocess.PIPE)
        t0 = time.time()
        for i in range(a, z):
            data = await pg.evaluate('i => window.renderFrame(i)', i)
            ff.stdin.write(base64.b64decode(data.split(',', 1)[1]))
            if i % 150 == 0: print(f'  {vid}-{lang}: кадр {i}/{n} · {(time.time() - t0) / max(1, i - a + 1):.2f} с/кадр', flush=True)
        ff.stdin.close(); ff.wait()
        if logs: print('\n'.join(l for l in logs if l.startswith('ERR'))[-2000:])
        await b.close()
    meta = {'id': vid, 'lang': lang, 'variant': 'wide' if wide else 'tall', 'fps': 30, 'scenes': [{'start': s0, 'dur': sc['dur'], 'say': sc.get('say', '')} for s0, sc in zip(info['starts'], spec['scenes'])],
            'title': (art.get('titles') or {}).get(lang) or art.get('i18n', {}).get(lang, {}).get('title', ''),
            'caption': (art.get('captions') or {}).get(lang) or '', 'slug': art.get('slug')}
    json.dump(meta, open(os.path.join(OUT, f'{vid}-{lang}{suf}.json'), 'w'), ensure_ascii=False, indent=1)
    print('готово', dst)
    return dst


async def stills(art):
    """Иллюстрации к статье: VIDEO['images'] → public/img/articles/3d/<slug>-<name>.jpg (без текста)."""
    from playwright.async_api import async_playwright
    v = art['video3d']; port = serve(); outdir = os.path.join(ROOT, 'public', 'img', 'articles', '3d'); os.makedirs(outdir, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
        for im in v.get('images', []):
            pg = await b.new_page(viewport={'width': 600, 'height': 400})
            await pg.goto(f'http://127.0.0.1:{port}/tools/studio/studio.html'); await pg.wait_for_function('window.studioReady === true', timeout=30000)
            w, h = im.get('w', 1200), im.get('h', 750); t = im.get('t', 1.0)
            spec = {'track': im.get('track', v['track']), 'theme': im.get('theme', v.get('theme', 'night')), 'fps': 30, 'w': w, 'h': h, 'plain': True,
                    'scenes': [{'kind': 'plain', 'dur': t / im.get('u', 0.5), 'shot': {**im['shot'], 't0': im['shot'].get('t0', 0)}}]}
            if im.get('hq', v.get('hq')): spec['hq'] = im.get('hq', v.get('hq'))
            await pg.evaluate('s => window.setupVideo(s)', spec)
            data = await pg.evaluate('i => window.renderFrame(i, 0.88)', int(t * 30))
            f = os.path.join(outdir, f"{art['slug']}-{im['name']}.jpg"); open(f, 'wb').write(base64.b64decode(data.split(',', 1)[1])); print(f)
            await pg.close()
        await b.close()


if __name__ == '__main__':
    args = sys.argv[1:]; files = [a for a in args if a.endswith('.py')]
    opt = lambda k: args[args.index(k) + 1] if k in args else None
    for f in files:
        art = load(f)
        for w in lint(art['video3d']): print('ВНИМАНИЕ:', os.path.basename(f), w)
        if '--lint' in args: continue
        if '--stills' in args: asyncio.run(stills(art)); continue
        for lang in ([opt('--lang')] if opt('--lang') else art['video3d']['scenes'].keys()):
            asyncio.run(render(art, lang, opt('--frames'), int(opt('--still')) if opt('--still') else None, '--wide' in args))

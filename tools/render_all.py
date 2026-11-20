#!/usr/bin/env python3
"""Рендерит все 3D-ролики, которых ещё нет или которые устарели, в папку ветки renders.
Запускается в GitHub Actions (.github/workflows/render.yml) или локально:
  python3 tools/render_all.py <папка-с-веткой-renders> [--jobs 3] [--only qatar]
Хэш ролика = файл сценария + студия + трасса + статья. Готовые ролики с тем же хэшем не перерисовываются.
"""
import asyncio, glob, hashlib, json, os, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render as R

ROOT = R.ROOT
# версия студии: увеличь, когда правка studio.js должна перерисовать все ролики (мелкие правки — без пересчёта)
STUDIO_VERSION = 2  # не повышать: иначе перерисуются все старые ролики


def digest(path, art, lang, wide):
    """Хэш ролика на одном языке: его сцены, камера, картинки + студия и трасса. Новые языки не перерисовывают старые."""
    v = art['video3d']; h = hashlib.sha1()
    key = {'scenes': v['scenes'][lang], 'shots': v['shots'], 'track': v['track'], 'theme': v.get('theme'), 'wide': wide,
           'title': (art.get('i18n') or {}).get(lang, {}).get('title') or (art.get('titles') or {}).get(lang)}
    if v.get('hq'): key['hq'] = v['hq']  # HQ-режим входит в хэш, только если задан: хэши старых роликов не меняются
    h.update(json.dumps(key, ensure_ascii=False, sort_keys=True).encode())
    h.update(f'studio-v{STUDIO_VERSION}'.encode())
    for f in [os.path.join(ROOT, 'tools', 'studio', 'tracks', v['track'] + '.json')]:
        if os.path.exists(f): h.update(open(f, 'rb').read())
    return h.hexdigest()[:16]


async def main(dst, jobs, only, lang_only=None, plan_only=False):
    os.makedirs(dst, exist_ok=True)
    todo = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'tools', 'video3d', '*.py'))):
        if only and not any(o.strip() and o.strip() in os.path.basename(f) for o in only.split(',')): continue
        art = R.load(f); art['_file'] = f; vid = art['videoId']
        for lang in art['video3d']['scenes']:
            if lang_only and lang != lang_only: continue
            for wide in ([False, True] if art.get('i18n') and os.environ.get('RENDER_WIDE') == '1' else [False]):  # горизонтальная версия выключена: на сайте показываем вертикальную  # горизонтальная версия — только для роликов при статье
                dg = digest(f, art, lang, wide); meta = os.path.join(dst, f'{vid}-{lang}{"-wide" if wide else ""}.json')
                try: old = json.load(open(meta)).get('digest')
                except Exception: old = None
                if old != dg: todo.append((art, lang, dg, wide))
    if plan_only:  # для GitHub Actions: какие пары тема×язык надо рисовать
        pairs = sorted({(os.path.basename(t[0]['_file'])[:-3], t[1]) for t in todo})
        print(json.dumps([{'topic': a, 'lang': b} for a, b in pairs])); return len(todo)
    print(f'к рендеру: {len(todo)}', flush=True)
    sem = asyncio.Semaphore(jobs)

    async def one(art, lang, dg, wide):
        async with sem:
            await R.render(art, lang, wide=wide)
            name = f"{art['videoId']}-{lang}{'-wide' if wide else ''}"
            for ext in ('mp4', 'json'): shutil.copy(os.path.join(R.OUT, f'{name}.{ext}'), os.path.join(dst, f'{name}.{ext}'))
            m = json.load(open(os.path.join(dst, f'{name}.json'))); m['digest'] = dg; m['studio'] = STUDIO_VERSION
            json.dump(m, open(os.path.join(dst, f'{name}.json'), 'w'), ensure_ascii=False, indent=1)
    await asyncio.gather(*(one(*t) for t in todo))
    return len(todo)


if __name__ == '__main__':
    a = sys.argv[1:]
    jobs = int(a[a.index('--jobs') + 1]) if '--jobs' in a else 2
    only = a[a.index('--only') + 1] if '--only' in a else None
    lang = a[a.index('--lang') + 1] if '--lang' in a else None
    n = asyncio.run(main(a[0], jobs, only, lang, '--plan' in a))
    if '--plan' not in a: print('готово, отрисовано', n)

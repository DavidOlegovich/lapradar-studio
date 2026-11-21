#!/usr/bin/env python3
"""Кадры для вертикальных видео (1080×1920) и обложки статей LapRadar.
Запуск: python3 tools/slides.py  → media/videos/<slug>/<lang>/NN.png + scenes.json, public/img/articles/<slug>.png
Озвучку и сборку видео делает сервер (deploy/media.sh)."""
import json, math, os, re, sys, importlib.util, glob
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1080, 1920
BG, BG2, BLUE, WHITE, MUTED = (5, 7, 13), (14, 20, 36), (52, 120, 246), (240, 244, 255), (140, 152, 180)
RED, YEL, WHT, GRN = (232, 44, 56), (247, 202, 46), (235, 235, 235), (60, 200, 120)
FONT = '/usr/share/fonts/opentype/inter/Inter-{}.otf'
CJK_FONT = '/usr/share/fonts/opentype/noto/NotoSansCJK-{}.ttc'
CUR_LANG = ['en']  # текущий язык сборки: для китайского — шрифт с иероглифами
def F(size, w='Bold'):
    if CUR_LANG[0] == 'zh':
        cw = {'Black': 'Black', 'ExtraBold': 'Bold', 'Bold': 'Bold', 'SemiBold': 'Medium'}.get(w, 'Bold')
        try: return ImageFont.truetype(CJK_FONT.format(cw), size, index=2)  # SC
        except OSError: pass
    return ImageFont.truetype(FONT.format(w), size)

L = {  # подписи на кадрах
  'ru': {'soft': 'МЯГКИЕ', 'med': 'СРЕДНИЕ', 'hard': 'ЖЁСТКИЕ', 'grip': 'Сцепление', 'life': 'Ресурс', 'laps': 'круги', 'laptime': 'темп', 'cliff': 'обрыв', 'illu': 'иллюстрация', 'read': 'Читать разбор', 'live': 'Live-карта, шины, стратегия'},
  'en': {'soft': 'SOFT', 'med': 'MEDIUM', 'hard': 'HARD', 'grip': 'Grip', 'life': 'Tyre life', 'laps': 'laps', 'laptime': 'pace', 'cliff': 'cliff', 'illu': 'illustration', 'read': 'Read the breakdown', 'live': 'Live map, tyres, strategy'},
  'es': {'soft': 'BLANDO', 'med': 'MEDIO', 'hard': 'DURO', 'grip': 'Agarre', 'life': 'Duración', 'laps': 'vueltas', 'laptime': 'ritmo', 'cliff': 'acantilado', 'illu': 'ilustración', 'read': 'Lee el análisis', 'live': 'Mapa en vivo, neumáticos, estrategia'},
  'pt': {'soft': 'MACIO', 'med': 'MÉDIO', 'hard': 'DURO', 'grip': 'Aderência', 'life': 'Durabilidade', 'laps': 'voltas', 'laptime': 'ritmo', 'cliff': 'penhasco', 'illu': 'ilustração', 'read': 'Leia a análise', 'live': 'Mapa ao vivo, pneus, estratégia'},
}
SPOKEN = [('LapRadar Punkt com', 'lapradar.com'), ('LapRadar点com', 'lapradar.com'), ('Formel Eins, Zwei und Drei', 'Formel 1, 2 und 3'), ('Formel-Eins', 'Formel-1'), ('Formel Eins', 'Formel 1'), ('一级方程式', 'F1'),
  ('Zweitausenddreiundzwanzig', '2023'), ('zweitausenddreiundzwanzig', '2023'), ('二零二三年', '2023年'), ('achtzehn Runden', '18 Runden'), ('十八圈', '18圈'),
  ('zwanzig bis fünfundzwanzig', '20–25'), ('二十到二十五', '20–25'), ('zehn bis fünfzehn Grad', '10–15 Grad'), ('十到十五度', '10–15度'), ('Neunzig-Grad', '90-Grad'), ('九十度', '90度'), ('sechs Kilometer', '6 Kilometer'), ('六公里', '6公里'),
  ('ЛапРадар точка ком', 'lapradar.com'), ('LapRadar dot com', 'lapradar.com'), ('LapRadar punto com', 'lapradar.com'), ('LapRadar ponto com', 'lapradar.com'),
  ('МотоДжиПи', 'MotoGP'), ('Мото два', 'Moto2'), ('Мото три', 'Moto3'), ('НАСКАР', 'NASCAR'), ('Формула E', 'Formula E'),
  ('Формула один, два и три', 'Формула 1, 2 и 3'), ('Formula One, Two and Three', 'Formula 1, 2 and 3'), ('Fórmula Uno, Dos y Tres', 'Fórmula 1, 2 y 3'), ('Fórmula Um, Dois e Três', 'Fórmula 1, 2 e 3'),
  ('Формула один', 'Формула 1'), ('Формулу один', 'Формулу 1'), ('Formula One', 'Formula 1'),
  ('двадцать третьего года', '2023 года'), ('двадцать третьем году', '2023 году'), ('twenty twenty-three', '2023'), ('dos mil veintitrés', '2023'), ('dois mil e vinte e três', '2023'),
  ('восемнадцатью кругами', '18 кругами'), ('eighteen laps', '18 laps'), ('dieciocho vueltas', '18 vueltas'), ('dezoito voltas', '18 voltas'),
  ('эм джи ю эйч', 'MGU-H'), ('эм джи ю кей', 'MGU-K'), ('ЛапРадар', 'LapRadar'), ('Формулы один', 'Формулы 1'), ('Формуле один', 'Формуле 1'), ('Formula One', 'Formula 1'), ('Fórmula Uno', 'Fórmula 1'), ('Fórmula Um', 'Fórmula 1')]

def caption_text(s):
    for a, b in SPOKEN: s = s.replace(a, b)
    s = re.sub(r'двадцать[–-]двадцать пять', '20–25', s)
    return s

def wrap(d, text, font, maxw):
    import re
    cjk = bool(re.search(r'[\u3000-\u9fff]', text)); sp = '' if cjk else ' '
    words, lines, cur = (list(text.replace(' ', '')) if cjk else text.split()), [], ''
    for w in words:
        t = (cur + sp + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def shot(src, lang):
    # скриншоты интерфейса: для роликов не на русском — английская версия из tools/shots/en/, если есть
    p = os.path.join(ROOT, src)
    if lang != 'ru':
        alt = os.path.join(os.path.dirname(p), 'en', os.path.basename(p))
        if os.path.exists(alt): return alt
    return p

def base():
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    # мягкий градиент и «радар»
    glow = Image.new('L', (W, H), 0); g = ImageDraw.Draw(glow)
    g.ellipse((-300, -200, 1300, 1100), fill=70); glow = glow.filter(ImageFilter.GaussianBlur(220))
    im.paste(Image.new('RGB', (W, H), (20, 50, 120)), (0, 0), glow)
    d = ImageDraw.Draw(im)
    for r in (260, 420, 580):
        d.arc((W - 120 - r, -120 - r, W - 120 + r, -120 + r), 90, 180, fill=(30, 44, 80), width=2)
    # логотип
    d.rounded_rectangle((70, 90, 150, 170), 18, fill=BLUE)
    d.arc((86, 104, 160, 178), 180, 270, fill=WHITE, width=9)
    d.ellipse((104, 122, 122, 140), fill=WHITE)
    d.text((172, 104), 'LAPRADAR', font=F(52, 'ExtraBold'), fill=WHITE)
    return im, d

def caption(im, d, text):
    text = caption_text(text)
    # безопасная зона TikTok/Reels: снизу ~420 px и справа ~170 px заняты интерфейсом
    f = F(56, 'Bold'); lines = wrap(d, text, f, W - 290)
    if len(lines) > 5: f = F(48, 'Bold'); lines = wrap(d, text, f, W - 290)
    bottom = H - 430; lh = int(f.size * 1.22); y0 = bottom - lh * len(lines)
    pad = 34
    d.rounded_rectangle((50, y0 - pad, W - 170, bottom + pad - 10), 34, fill=(16, 22, 40))
    d.rectangle((50, y0 - pad + 20, 58, bottom + pad - 30), fill=BLUE)
    for i, ln in enumerate(lines):
        d.text((86, y0 + i * lh), ln, font=f, fill=WHITE)

def tyre(d, cx, cy, r, color, label, dim=False):
    c = tuple(int(x * 0.35) for x in color) if dim else color
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(22, 22, 26))
    d.ellipse((cx - r * .78, cy - r * .78, cx + r * .78, cy + r * .78), outline=c, width=int(r * .09))
    d.ellipse((cx - r * .52, cy - r * .52, cx + r * .52, cy + r * .52), fill=(48, 50, 58))
    d.ellipse((cx - r * .16, cy - r * .16, cx + r * .16, cy + r * .16), fill=(120, 124, 134))
    f = F(42, 'ExtraBold'); tw = d.textlength(label, font=f)
    d.text((cx - tw / 2, cy + r + 24), label, font=f, fill=c)

def draw_head(d, text, y=330, size=104):
    f = F(size, 'Black'); lines = wrap(d, text, f, W - 140)
    for i, ln in enumerate(lines): d.text((70, y + i * int(size * 1.08)), ln, font=f, fill=WHITE)
    return y + len(lines) * int(size * 1.08)

def scene(sc, lang, slug):
    im, d = base(); t = L[lang]
    k = sc['kind']
    if k == 'title':
        y = draw_head(d, sc.get('head', ''), 360, 120)
        d.rectangle((70, y + 30, 250, y + 42), fill=BLUE)
        if sc.get('src'):  # заставка со скриншотом вместо шин
            src = Image.open(shot(sc['src'], lang)).convert('RGB'); bw = 760; bh = min(int(src.height * bw / src.width), 640)
            src = src.resize((bw, int(src.height * bw / src.width))).crop((0, 0, bw, bh))
            mask = Image.new('L', (bw, bh), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, bw, bh), 40, fill=255)
            yy = y + 90; d.rounded_rectangle(((W - bw) // 2 - 8, yy - 8, (W + bw) // 2 + 8, yy + bh + 8), 46, fill=(40, 50, 80)); im.paste(src, ((W - bw) // 2, yy), mask)
        elif sc.get('icon') != 'none':
            tyre(d, 300, y + 330, 150, RED, '', False); tyre(d, 640, y + 380, 120, YEL, ''); tyre(d, 900, y + 300, 95, WHT, '')
    elif k == 'tyres':
        hi = sc.get('hi', -1)
        for i, (col, lab) in enumerate([(RED, t['soft']), (YEL, t['med']), (WHT, t['hard'])]):
            tyre(d, 200 + i * 340, 760, 150, col, lab, dim=(hi >= 0 and hi != i))
    elif k == 'bars':
        rows = [(t['soft'], RED, .95, .35), (t['med'], YEL, .8, .65), (t['hard'], WHT, .65, .95)]
        y = 380
        for lab, col, g, l in rows:
            d.text((70, y), lab, font=F(48, 'ExtraBold'), fill=col)
            for j, (name, v) in enumerate([(t['grip'], g), (t['life'], l)]):
                yy = y + 80 + j * 70
                d.text((70, yy), name, font=F(34, 'Medium'), fill=MUTED)
                d.rounded_rectangle((340, yy + 6, 1010, yy + 36), 15, fill=(30, 36, 54))
                d.rounded_rectangle((340, yy + 6, 340 + int(670 * v), yy + 36), 15, fill=col)
            y += 260
    elif k == 'chart':
        x0, y0, x1, y1 = 120, 400, 1000, 1150
        d.line((x0, y1, x1, y1), fill=MUTED, width=3); d.line((x0, y0, x0, y1), fill=MUTED, width=3)
        d.text((x1 - 140, y1 + 16), t['laps'], font=F(34, 'Medium'), fill=MUTED)
        d.text((x0 + 10, y0 - 50), '↑ ' + t['laptime'], font=F(34, 'Medium'), fill=MUTED)
        def curve(col, start, slope, cliff_at=None):
            pts = []
            for i in range(0, 41):
                v = start + slope * i + (0.06 * (i - cliff_at) ** 2 if cliff_at and i > cliff_at else 0)
                pts.append((x0 + (x1 - x0) * i / 40, y1 - 40 - (1 - min(v, 1)) * (y1 - y0 - 60)))
            d.line(pts, fill=col, width=10, joint='curve')
        curve(RED, 0.0, 0.006, 18); curve(YEL, 0.15, 0.004, 30); curve(WHT, 0.28, 0.0025)
        d.text((x0 + (x1 - x0) * 22 / 40, y0 + 330), t['cliff'] + ' ↘', font=F(40, 'ExtraBold'), fill=RED)
        d.text((x0, y1 + 60), t['illu'], font=F(28, 'Medium'), fill=(90, 100, 125))
    elif k == 'big':
        f = F(220, 'Black'); tw = d.textlength(sc.get('big', ''), font=f)
        d.text(((W - tw) / 2, 560), sc.get('big', ''), font=f, fill=WHITE)
        if sc.get('sub'): f2 = F(52, 'SemiBold'); tw = d.textlength(sc['sub'], font=f2); d.text(((W - tw) / 2, 830), sc['sub'], font=f2, fill=BLUE)
    elif k == 'list':
        y = draw_head(d, sc.get('head', ''), 330, 96) + 50
        for it in sc['items']:
            d.rounded_rectangle((70, y, W - 70, y + 120), 26, fill=BG2)
            d.ellipse((105, y + 42, 141, y + 78), fill=BLUE)
            d.text((170, y + 28), it, font=F(60, 'Bold'), fill=WHITE); y += 145
    elif k == 'image':
        src = Image.open(shot(sc['src'], lang)).convert('RGB')
        bw = 860; bh = int(src.height * bw / src.width); bh = min(bh, 900)
        src = src.resize((bw, int(src.height * bw / src.width)))
        src = src.crop((0, 0, bw, bh))
        mask = Image.new('L', (bw, bh), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, bw, bh), 40, fill=255)
        y = 310 + max(0, (900 - bh) // 2)
        d.rounded_rectangle(((W - bw) // 2 - 8, y - 8, (W + bw) // 2 + 8, y + bh + 8), 46, fill=(40, 50, 80))
        im.paste(src, ((W - bw) // 2, y), mask)
        if sc.get('head'): draw_head(d, sc['head'], 210, 64)
    elif k == 'end':
        f = F(130, 'Black'); tw = d.textlength('LapRadar', font=f)
        d.text(((W - tw) / 2, 520), 'LapRadar', font=f, fill=WHITE)
        f2 = F(46, 'SemiBold'); s = t['live']; tw = d.textlength(s, font=f2); d.text(((W - tw) / 2, 690), s, font=f2, fill=MUTED)
        d.rounded_rectangle((140, 800, W - 140, 940), 70, fill=BLUE)
        u = f'lapradar.com/a/{slug}' if slug else 'lapradar.com'
        f3 = F(48 if len(u) < 30 else 38, 'Bold'); tw = d.textlength(u, font=f3); d.text(((W - tw) / 2, 845), u, font=f3, fill=WHITE)
        if slug: s2 = t['read'] + ' →'; tw = d.textlength(s2, font=F(44, 'Bold')); d.text(((W - tw) / 2, 980), s2, font=F(44, 'Bold'), fill=WHITE)
    caption(im, d, sc['say'])
    return im

def cover(art, path, lang='en'):
    CUR_LANG[0] = lang
    im = Image.new('RGB', (1200, 630), BG); d = ImageDraw.Draw(im)
    glow = Image.new('L', (1200, 630), 0); ImageDraw.Draw(glow).ellipse((-200, -300, 900, 600), fill=80)
    im.paste(Image.new('RGB', (1200, 630), (20, 50, 120)), (0, 0), glow.filter(ImageFilter.GaussianBlur(160)))
    d = ImageDraw.Draw(im)
    c = art.get('cover', {})
    if c.get('kind') == 'bg':  # 3D-картинка на весь кадр, слева затемнение под заголовок
        src = Image.open(os.path.join(ROOT, c['src'])).convert('RGB')
        k = max(1200 / src.width, 630 / src.height); src = src.resize((int(src.width * k) + 1, int(src.height * k) + 1))
        im.paste(src.crop((src.width - 1200, (src.height - 630) // 2, src.width, (src.height - 630) // 2 + 630)), (0, 0))
        shade = Image.new('L', (1200, 630), 0); sd = ImageDraw.Draw(shade)
        for x in range(1200): sd.line([(x, 0), (x, 630)], fill=int(235 * max(0, 1 - x / 820) ** 1.3))
        im.paste(Image.new('RGB', (1200, 630), (6, 9, 18)), (0, 0), shade); d = ImageDraw.Draw(im)
    elif c.get('kind') == 'tyres':
        for i, col in enumerate([RED, YEL, WHT]): tyre(d, 820 + i * 150, 330 + (i % 2) * 60, 95 - i * 10, col, '')
    elif c.get('kind') == 'image':
        src = Image.open(shot(c['src'], lang)).convert('RGB'); bw = 440; bh = min(int(src.height * bw / src.width), 520)
        src = src.resize((bw, int(src.height * bw / src.width))).crop((0, 0, bw, bh))
        mask = Image.new('L', (bw, bh), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, bw, bh), 28, fill=255)
        im.paste(src, (720, (630 - bh) // 2), mask); d = ImageDraw.Draw(im)
    d.text((60, 60), 'LAPRADAR', font=F(40, 'ExtraBold'), fill=BLUE)
    t = (art['i18n'].get(lang) or art['i18n'].get('en') or {}).get('title', '')
    f = F(56, 'Black'); lines = wrap(d, t, f, 630)[:5]
    for i, ln in enumerate(lines): d.text((60, 150 + i * 66), ln, font=f, fill=WHITE)
    im.save(path, optimize=True)

def build(mod):
    art = mod.ARTICLE; slug = art['slug']
    os.makedirs(os.path.join(ROOT, 'content', 'articles'), exist_ok=True)
    data = {k: v for k, v in art.items() if k != 'video'}
    if art.get('i18n'):
        json.dump(data, open(os.path.join(ROOT, 'content', 'articles', slug + '.json'), 'w'), ensure_ascii=False, indent=1)
        os.makedirs(os.path.join(ROOT, 'public', 'img', 'articles'), exist_ok=True)
        cover(art, os.path.join(ROOT, 'public', 'img', 'articles', slug + '.png'))
        for lg in art['i18n']: cover(art, os.path.join(ROOT, 'public', 'img', 'articles', f'{slug}-{lg}.png'), lg)
    vid_id = art.get('videoId', slug)
    link_slug = slug if art.get('i18n') else ''
    for lang, scenes in art.get('video', {}).items():
        CUR_LANG[0] = lang
        out = os.path.join(ROOT, 'media', 'videos', vid_id, lang); os.makedirs(out, exist_ok=True)
        for f in glob.glob(os.path.join(out, '*.png')): os.remove(f)
        sj = []
        for i, sc in enumerate(scenes):
            name = f'{i:02d}.png'
            scene(sc, lang, link_slug).quantize(256, dither=Image.Dither.NONE).save(os.path.join(out, name), optimize=True)
            sj.append({'img': name, 'say': sc['say'], **({'pad': sc['pad']} if 'pad' in sc else {})})
        title = (art.get('i18n', {}).get(lang) or {}).get('title') or art.get('titles', {}).get(lang, slug)
        link = f'https://lapradar.com/a/{slug}?l={lang}' if link_slug else 'https://lapradar.com'
        cap = art.get('captions', {}).get(lang) or (title + ' 👉 ' + link)
        json.dump({'title': title, 'caption': cap, 'link': link, 'speed': art.get('speed', {}).get(lang, 0.92), 'scenes': sj}, open(os.path.join(out, 'scenes.json'), 'w'), ensure_ascii=False, indent=1)
    print('ok', slug)

if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, 'tools', 'content', '*.py')))
    for f in files:
        spec = importlib.util.spec_from_file_location('m', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); build(m)

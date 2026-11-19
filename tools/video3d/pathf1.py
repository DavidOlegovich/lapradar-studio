# Путь в Формулу 1: картинг, F4, F3, F2, суперлицензия и деньги. Камера (shots) общая для всех языков.
VIDEO = {
 "slug": "path-to-f1",
 "track": "monza",
 "theme": "day",
 "shots": [
  {"type": "chase", "car": 1, "dist": 13, "dist2": 12, "h": 6.5, "h2": 6, "side": 0, "side2": 0, "look": 25, "drop": 9, "noCut": True, "act": {"type": "follow", "at": 0.3}},
  {"type": "stage", "items": [{"o": "f1", "c": "#facc15"}], "bg": "blue", "r": 10, "r2": 9, "h": 2.4, "h2": 3.2, "a0": 0.9, "a1": -0.2, "spin": 0.3, "ly": 0.8,
   "hud": {"type": "bars", "rows": [{"label": "KRT", "v": 4, "c": "#9fb4ff"}, {"label": "F4", "v": 12, "c": "#5b9bff"}, {"label": "F3", "v": 30, "c": "#3b82f6"}, {"label": "F2", "v": 40, "c": "#facc15"}], "min": 0, "max": 40, "hi": 3}},
  {"type": "chase", "car": 3, "dist": 14, "dist2": 12, "h": 6, "h2": 5, "side": 1.5, "side2": -1.5, "look": 25, "drop": 9, "noCut": True, "act": {"type": "convoy", "at": "straight", "t0": 6}},
  {"type": "chase", "car": 1, "dist": 13, "dist2": 11, "h": 6, "h2": 5, "side": 0.5, "side2": -0.5, "look": 25, "drop": 9, "noCut": True, "act": {"type": "follow", "at": 0.55}},
  {"type": "chase", "car": 1, "dist": 16, "dist2": 13, "h": 6, "h2": 5.5, "side": 0, "side2": 2.5, "look": 25, "drop": 9, "noCut": True, "act": {"type": "boost"}},
  {"type": "stage", "items": [{"o": "f1", "c": "#e10600", "x": -1.6, "ry": 0.3}, {"o": "trophy", "x": 2.4, "s": 0.8}], "bg": "red", "r": 12, "r2": 10, "h": 3, "h2": 3.6, "a0": -0.4, "a1": 0.3, "spin": 0, "ly": 1.2},
  {"type": "fly", "from": 0.05, "to": 0.13, "h": 60, "h2": 140, "side": 40, "ahead": 260}
 ],
 "coverShot": {"type": "chase", "car": 1, "dist": 12, "h": 4.5, "side": 0, "look": 25, "drop": 1, "noCut": True, "act": {"type": "follow", "at": 0.3}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 1, "dist": 9, "h": 3.4, "side": -3.5, "look": 18, "drop": 2, "fov": 44, "act": {"type": "follow", "at": 0.3}}},
  {"name": "duel", "w": 1200, "h": 800, "t": 1.0, "u": 0.5,
   "shot": {"type": "chase", "car": 1, "dist": 9, "h": 3.6, "side": -2.2, "look": 14, "drop": 2, "fov": 40, "act": {"type": "boost"}}},
  {"name": "licence", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "f1", "c": "#e10600", "x": -1.6, "ry": 0.3}, {"o": "trophy", "x": 2.4, "s": 0.8}], "bg": "red", "r": 11, "h": 3, "a0": -0.2, "spin": 0, "ly": 1.2}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "ПУТЬ В F1", "chip": "≈ £8 000 000",
    "say": "Восемь миллионов фунтов. Столько, по словам Култхарда, стоит дорога от картинга до Формулы один.",
    "hl": ["восьми миллионов"]},
   {"kind": "list", "head": "Очки суперлицензии", "items": ["F4 12", "F3 30", "F2 40"],
    "say": "Для Формулы один нужна суперлицензия, а для неё сорок очков. Их дают за места в младших сериях.",
    "hl": ["сорок очков"]},
   {"kind": "big", "big": "8", "chip": "картинг · с 8 лет",
    "say": "Всё начинается с картинга лет в восемь. Уже он обходится в сотни тысяч.",
    "hl": ["картинга", "сотни тысяч"]},
   {"kind": "big", "big": "15", "chip": "F4 · с 15 лет · 12 очков",
    "say": "С пятнадцати можно в Формулу четыре. Чемпиону дают всего двенадцать очков.",
    "hl": ["пятнадцати", "двенадцать"]},
   {"kind": "big", "big": "40", "chip": "F3 ≈ £1,5 млн · F2 > £2 млн",
    "say": "Сезон Формулы три около полутора миллионов фунтов, Формулы два больше двух. Зато тройка лучших в F2 получает все сорок очков.",
    "hl": ["полутора миллионов", "все сорок"]},
   {"kind": "big", "big": "18", "chip": "18 лет · 40 очков за 3 года",
    "say": "И возраст: с шестнадцатого года нужно восемнадцать лет. Правило ввели после дебюта Ферстаппена в семнадцать.",
    "hl": ["восемнадцать", "Ферстаппен"]},
   {"kind": "end", "tag": "F2 и F3 тоже здесь",
    "say": "Таблицы Формулы два и Формулы три смотрите на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "THE ROAD TO F1", "chip": "≈ £8,000,000",
    "say": "Eight million pounds. That's what Coulthard says the road from karting to Formula One costs.",
    "hl": ["eight million"]},
   {"kind": "list", "head": "Super licence points", "items": ["F4 12", "F3 30", "F2 40"],
    "say": "Formula One needs a super licence, and that takes forty points, earned with results in junior series.",
    "hl": ["forty points"]},
   {"kind": "big", "big": "8", "chip": "karting · from age 8",
    "say": "It starts with karting at around eight. That alone costs hundreds of thousands.",
    "hl": ["karting", "hundreds of thousands"]},
   {"kind": "big", "big": "15", "chip": "F4 · age 15+ · 12 pts",
    "say": "At fifteen you can race Formula Four. The champion gets just twelve points.",
    "hl": ["fifteen", "twelve"]},
   {"kind": "big", "big": "40", "chip": "F3 ≈ £1.5m · F2 > £2m",
    "say": "Formula Three costs about one and a half million pounds a season, Formula Two over two. But the F2 top three get all forty points.",
    "hl": ["million", "all forty"]},
   {"kind": "big", "big": "18", "chip": "age 18 · 40 pts in 3 years",
    "say": "And age: since twenty sixteen you must be eighteen. The rule came after Verstappen debuted at seventeen.",
    "hl": ["eighteen", "Verstappen"]},
   {"kind": "end", "tag": "F2 and F3 are here too",
    "say": "Formula Two and Formula Three standings are on LapRadar."}
  ]
 }
}

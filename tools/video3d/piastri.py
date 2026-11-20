# Оскар Пиастри расстался с менеджером Марком Уэббером: 7 лет, объявили 9.11.2026 после Сан-Паулу, по обоюдному согласию.
# Таймлайн чипами: 2019 → F3 2020 → F2 2021 → 2022 спор контрактов (CRB за McLaren) → 2026 расставание.
# Оранжевая машина 1 из палитры студии (без логотипов McLaren), шлем нарисован (оранжевый с синим), фото нет. Камера (shots) общая для всех языков.
_HELMET = {"c": ["#ff8000", "#1e3a8a", "#ffffff"], "p": "stripes"}

VIDEO = {
 "slug": "piastri-webber-split",
 "track": "monza",
 "theme": "day",
 "shots": [
  {"type": "chase", "car": 1, "dist": 13, "dist2": 12, "h": 6, "h2": 5.5, "side": 0, "side2": 0, "look": 22, "drop": 6, "noCut": True,
   "act": {"type": "follow", "at": 0.3}},
  {"type": "chase", "car": 1, "dist": 14, "dist2": 12, "h": 5.5, "h2": 5, "side": 1.5, "side2": -1.5, "look": 25, "drop": 3, "noCut": True,
   "act": {"type": "follow", "at": 0.45}, "helmet": _HELMET},
  {"type": "stage", "items": [{"o": "podium"}, {"o": "trophy", "y": 2.2, "s": 0.6}], "confetti": True, "bg": "gold", "r": 14, "r2": 11, "h": 4, "h2": 4.5, "a0": -0.3, "a1": 0.3, "spin": 0, "ly": 2.2},
  {"type": "stage", "items": [{"o": "f1", "c": "#1d4ed8", "x": -2.3, "ry": 0.25}, {"o": "f1", "c": "#f97316", "x": 2.3, "ry": -0.25}], "bg": "blue", "beams": True, "r": 13, "r2": 11, "h": 3, "h2": 4, "a0": -0.4, "a1": 0.3, "spin": 0.1, "ly": 0.6},
  {"type": "stage", "items": [{"o": "f1", "c": "#f97316"}], "bg": "blue", "r": 10.5, "r2": 9.5, "h": 2.4, "h2": 3.2, "a0": 0.9, "a1": -0.2, "spin": 0.3, "ly": 0.8},
  {"type": "chase", "car": 1, "dist": 14, "dist2": 11, "h": 5.5, "h2": 4.5, "side": 3, "side2": -2.5, "look": 25, "drop": 3, "noCut": True, "act": {"type": "follow", "at": 0.6}},
  {"type": "fly", "from": 0.3, "to": 0.38, "h": 60, "h2": 140, "side": 40, "ahead": 260}
 ],
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 1, "dist": 8.5, "h": 3.2, "side": -2.6, "look": 14, "drop": 2, "fov": 40, "act": {"type": "follow", "at": 0.3}}},
  {"name": "podium", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "podium"}, {"o": "trophy", "y": 2.2, "s": 0.6}], "confetti": True, "bg": "gold", "r": 12, "h": 4, "a0": 0.2, "spin": 0, "ly": 2.2}},
  {"name": "duel", "w": 1200, "h": 800, "t": 1.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 9, "h": 3.6, "side": -2.4, "look": 12, "drop": 2, "fov": 40, "act": {"type": "duel"}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "ПИАСТРИ БЕЗ УЭББЕРА", "chip": "Пиастри × Уэббер · 7 лет",
    "say": "Семь лет вместе, и всё. Оскар Пиастри расстался со своим менеджером Марком Уэббером.",
    "hl": ["Семь", "Уэббером"]},
   {"kind": "big", "big": "9.11", "chip": "9 ноября · по согласию",
    "say": "Об этом объявили в понедельник после Гран-при Сан-Паулу. Решение обоюдное.",
    "hl": ["Сан-Паулу", "обоюдное"]},
   {"kind": "big", "big": "2019", "chip": "2019 → F3 2020 → F2 2021",
    "say": "Уэббер и его жена Энн вели Оскара с девятнадцатого года. Потом два титула подряд: Формула три и Формула два.",
    "hl": ["два", "титула"]},
   {"kind": "big", "big": "2022", "chip": "2022 · CRB за McLaren",
    "say": "В двадцать втором Alpine объявила его своим пилотом. Оскар сказал нет, и FIA признала контракт с McLaren.",
    "hl": ["нет", "McLaren"]},
   {"kind": "big", "big": "3", "chip": "контракты · спонсоры · имидж",
    "say": "Менеджер пилота ведёт переговоры о контрактах, ищет спонсоров и следит за его имиджем.",
    "hl": ["контрактах", "спонсоров"]},
   {"kind": "big", "big": "P7", "chip": "2026 · P7 · 152 очка",
    "say": "С начала сезона Уэббер работал за кулисами и почти не ездил на гонки. Пиастри сейчас седьмой.",
    "hl": ["за", "кулисами", "седьмой"]},
   {"kind": "end", "tag": "Пиастри · новый менеджмент",
    "say": "Кто теперь ведёт Пиастри, пока не объявили. Таблица пилотов на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "PIASTRI WITHOUT WEBBER", "chip": "Piastri × Webber · 7 years",
    "say": "Seven years together, and that's it. Oscar Piastri has split with his manager Mark Webber.",
    "hl": ["Seven", "Webber"]},
   {"kind": "big", "big": "9.11", "chip": "9 November · mutual",
    "say": "It was announced on the Monday after the São Paulo Grand Prix. Both sides agreed.",
    "hl": ["São", "Paulo", "agreed"]},
   {"kind": "big", "big": "2019", "chip": "2019 → F3 2020 → F2 2021",
    "say": "Webber and his wife Ann managed him from twenty nineteen. Then two titles in a row, Formula Three and Formula Two.",
    "hl": ["two", "titles"]},
   {"kind": "big", "big": "2022", "chip": "2022 · CRB backs McLaren",
    "say": "In twenty twenty-two Alpine announced him. Oscar said no, and the FIA backed his McLaren contract.",
    "hl": ["no", "McLaren"]},
   {"kind": "big", "big": "3", "chip": "contracts · sponsors · image",
    "say": "A driver's manager negotiates contracts, finds sponsors and looks after the driver's image.",
    "hl": ["contracts", "sponsors"]},
   {"kind": "big", "big": "P7", "chip": "2026 · P7 · 152 pts",
    "say": "This season Webber worked behind the scenes and rarely came to races. Piastri is seventh right now.",
    "hl": ["behind", "scenes", "seventh"]},
   {"kind": "end", "tag": "Piastri · new management",
    "say": "Who manages Piastri next hasn't been announced. The driver standings are on LapRadar."}
  ]
 }
}

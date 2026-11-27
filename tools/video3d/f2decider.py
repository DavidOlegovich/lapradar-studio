# Формула 2: титул решается в Катаре и Абу-Даби (28.11.2026). Лидер Камара (207) не гоняет: он в Haas, в Invicta вместо него Слейтер.
# Цолов 200, Данн 189; максимум 39 за уикенд, 78 за два этапа. Спринт в субботу, основная гонка в воскресенье, Абу-Даби 5-6.12.
# Время сессий не называем. Источники: tools/topics.md («Источники 28.11: F2, решающие этапы»).
# Без look cinema (правило с 30.11). Машины условные, без ливрей; ровно 9 камер на 9 сцен.
_BLUE = ["#1e40af", "#f8fafc", "stripe"]
_ORG = ["#f97316", "#111827", "band"]
_TEAL = ["#0f766e", "#e5e7eb", "split"]
_CV = {"type": "convoy", "at": 0.02, "v": 30, "n": 3}

VIDEO = {
 "slug": "f2-title-fight-qatar-abu-dhabi-2026",
 "track": "lusail",
 "theme": "night",
 "hq": {"cars": [_BLUE, _ORG, _TEAL], "lampFade": True},
 "coverText": {"ru": {"head": "ТИТУЛ F2", "sub": "Катар и Абу-Даби"},
               "en": {"head": "F2 TITLE", "sub": "Qatar and Abu Dhabi"}},
 "shots": [
  # 1 крючок
  {"type": "chase", "car": 1, "dist": 10, "dist2": 9.5, "h": 4.2, "h2": 4.0, "side": 0, "side2": 0, "look": 18, "drop": 3, "noCut": True, "act": {"type": "follow", "at": 0.01}},
  # 2 таблица
  {"type": "stage", "items": [{"o": "f1", "c": _BLUE[0], "a": _BLUE[1], "p": _BLUE[2], "x": -2.3, "ry": 0.25}, {"o": "f1", "c": _ORG[0], "a": _ORG[1], "p": _ORG[2], "x": 2.3, "ry": -0.25}],
   "bg": "blue", "r": 13, "r2": 11.5, "h": 3.0, "h2": 3.6, "a0": -0.35, "a1": 0.3, "spin": 0.06, "ly": 0.6,
   "hud": {"type": "bars", "rows": [{"label": "CAM", "v": 207, "c": "#9fb4ff"}, {"label": "TSO", "v": 200, "c": "#ef4444"}, {"label": "DUN", "v": 189, "c": "#f97316"}], "min": 120, "max": 215, "hi": 1}},
  # 3 Камара в Haas, Слейтер в Invicta
  {"type": "carorbit", "car": 0, "r": 10.5, "r2": 9.5, "h": 1.5, "h2": 2.0, "a0": 0.5, "a1": 1.15, "fov": 46, "ly": 0.8, "act": {**_CV, "at": 0.03, "v": 22, "n": 1}},
  # 4 39 очков
  {"type": "chase", "car": 0, "dist": 11, "dist2": 10, "h": 4.4, "h2": 4.0, "side": -1.5, "side2": 1.5, "look": 14, "drop": 3, "noCut": True, "act": {"type": "duel"}},
  # 5 Цолову нужно 8
  {"type": "chase", "car": 1, "dist": 12, "dist2": 10.5, "h": 5, "h2": 4.6, "side": 1.5, "side2": -1.2, "look": 20, "drop": 3, "noCut": True, "act": {"type": "follow", "at": 0.26}},
  # 6 Данн
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10, "h": 4.6, "h2": 4.2, "side": -2.6, "side2": -1.6, "look": 14, "drop": 3, "noCut": True, "act": {"type": "duel"}},
  # 7 клинч в Катаре
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 5.5, "h2": 5, "side": -1.5, "side2": 0, "look": 20, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 58, "n": 3}},
  # 8 даты
  {"type": "chase", "car": 0, "dist": 11, "dist2": 10, "h": 4, "h2": 3.8, "side": 1.8, "side2": 1.2, "look": 10, "drop": 1.5, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 62, "n": 3}},
  # 9 конец
  {"type": "chase", "car": 0, "dist": 26, "dist2": 28, "h": 10, "h2": 11, "side": -2, "side2": 0, "look": 30, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 55, "n": 3}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 9.5, "h": 1.4, "a0": 1.85, "a1": 1.85, "fov": 44, "act": {**_CV, "at": 0.02, "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 7.5, "h": 1.2, "a0": 2.1, "a1": 2.1, "fov": 40, "ly": 0.6, "act": {**_CV, "at": 0.02, "v": 1, "n": 2}}},
  {"name": "duel", "w": 1200, "h": 800, "t": 3.2, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 10, "h": 3.8, "side": -2.4, "look": 12, "drop": 2, "fov": 42, "act": {"type": "duel"}}},
  {"name": "straight", "w": 1200, "h": 800, "t": 1.8, "u": 0.4,
   "shot": {"type": "chase", "car": 0, "dist": 26, "h": 10, "side": 0, "look": 30, "drop": 3, "fov": 44, "act": {"type": "convoy", "at": "straight", "v": 62, "n": 3}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "big": "207", "chip": "Камара 207 · в F2 не гоняет",
    "say": "Лидер Формулы два не выйдет на старт в Катаре. Так кто решит титул?",
    "hl": ["не выйдет", "титул"]},
   {"kind": "big", "big": "11", "chip": "Камара 207 · Цолов 200 · Данн 189",
    "say": "У Камары двести семь, у Цолова двести, у Данна сто восемьдесят девять. Но Камара очков уже не добавит.",
    "hl": ["двести", "семь"]},
   {"kind": "big", "chip": "Камара в Haas · Слейтер в Invicta",
    "say": "Камара гоняет за Haas в Формуле один, а в его машине в Invicta дебютирует Фредди Слейтер.",
    "hl": ["Haas", "Слейтер"]},
   {"kind": "big", "big": "39", "chip": "до 39 за уикенд · до 78 за два",
    "say": "За уикенд можно взять тридцать девять очков, за два этапа семьдесят восемь.",
    "hl": ["тридцать", "девять"]},
   {"kind": "big", "big": "8", "chip": "Цолову нужно 8 очков",
    "say": "Цолову нужно восемь очков, чтобы выйти вперёд. Второе место в спринте даёт ровно столько.",
    "hl": ["восемь", "спринте"]},
   {"kind": "big", "big": "19", "chip": "Данн: 11 до Цолова · 19 до лидера",
    "say": "Данн позади Цолова на одиннадцать очков. До Камары девятнадцать: второе место в основной гонке и быстрый круг.",
    "hl": ["одиннадцать", "девятнадцать"]},
   {"kind": "big", "big": "39", "chip": "Отрыв >39 от всех · иначе Абу-Даби",
    "say": "Закрыть титул в Катаре Цолов может, только если оторвётся больше чем на тридцать девять от всех ближайших соперников.",
    "hl": ["тридцать", "девять"]},
   {"kind": "big", "chip": "Лусаил 28–29.11 · Абу-Даби 5–6.12",
    "say": "Спринт в субботу, основная гонка в воскресенье. Финал в Абу-Даби пятого и шестого декабря.",
    "hl": ["субботу", "воскресенье"]},
   {"kind": "end", "tag": "F2 · решающие этапы",
    "say": "Во сколько гонки по вашему времени, смотрите на ЛапРадар.",
    "hl": ["вашему", "времени"]}
  ],
  "en": [
   {"kind": "big", "big": "207", "chip": "Câmara 207 · not racing F2",
    "say": "The Formula Two leader won't start in Qatar. So who decides the title?",
    "hl": ["won't start", "title"]},
   {"kind": "big", "big": "11", "chip": "Câmara 207 · Tsolov 200 · Dunne 189",
    "say": "Câmara has two oh seven, Tsolov two hundred, Dunne one eighty-nine. Câmara can't add more.",
    "hl": ["two", "hundred"]},
   {"kind": "big", "chip": "Câmara at Haas · Slater at Invicta",
    "say": "Câmara races for Haas in Formula One, and Freddie Slater makes his debut in the Invicta car.",
    "hl": ["Haas", "Slater"]},
   {"kind": "big", "big": "39", "chip": "up to 39 a weekend · 78 in two",
    "say": "A driver can take thirty-nine points in a weekend, seventy-eight across the two rounds.",
    "hl": ["thirty-nine", "seventy-eight"]},
   {"kind": "big", "big": "8", "chip": "Tsolov needs 8 points",
    "say": "Tsolov needs eight points to lead. Second in the sprint pays exactly that.",
    "hl": ["eight", "sprint"]},
   {"kind": "big", "big": "19", "chip": "Dunne: 11 to Tsolov · 19 to the lead",
    "say": "Dunne is eleven behind Tsolov. Nineteen would pass Câmara: second in the feature plus fastest lap.",
    "hl": ["eleven", "nineteen"]},
   {"kind": "big", "big": "39", "chip": "Gap over 39 to all · or Abu Dhabi",
    "say": "Tsolov can only seal it in Qatar by getting more than thirty-nine points clear of every close rival.",
    "hl": ["thirty-nine", "every"]},
   {"kind": "big", "chip": "Lusail 28–29 Nov · Abu Dhabi 5–6 Dec",
    "say": "Sprint Saturday, feature race Sunday. Abu Dhabi closes it on the fifth and sixth of December.",
    "hl": ["Saturday", "Sunday"]},
   {"kind": "end", "tag": "F2 · the final rounds",
    "say": "Check what time the races start in your own time zone on LapRadar.",
    "hl": ["your", "own", "time", "zone"]}
  ]
 }
}

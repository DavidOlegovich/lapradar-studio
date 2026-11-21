# Итоги квалификации Гран-при Лас-Вегаса 2026 (20.11 по Вегасу, 21.11 утром по Тбилиси): Антонелли быстрее всех, но штраф 5 мест,
# с поула стартует Ферстаппен; Пиастри −10 (5-й ДВС), Сайнс, Стролл и Берман в хвосте; обе Ferrari вылетели в Q2 (не в Q1).
# HQ-режим, ночной Вегас со Sphere и неоном. Таблицы позиций: hud "grid" (строки с условными цветами команд, без логотипов).
# Машины (VIDEO.hq.cars, условные цвета, без ливрей): 0 серебро с бирюзой, 1 тёмно-синяя с красным, 2 оранжевая, 3 красная.
# Стартовая решётка в ролике и статье предварительная (до официального документа FIA). Камера (shots) общая для всех языков.
_SIL = ["#c3c8d0", "#14b8a6", "stripe"]
_NAVY = ["#1b2a6b", "#d61f3c", "stripe"]
_PAP = ["#ff8a1f", "#111827", "band"]
_RED = ["#d81e1e", "#f8fafc", "fade"]
_CV = {"type": "convoy", "at": 0.355, "v": 30, "n": 4}
_N = {"neon": True}

# условные цвета-полоски команд в таблицах
_C = {"MER": "#2dd4bf", "RBR": "#3b5bdb", "MCL": "#ff8a1f", "FER": "#ef4444", "RB": "#93c5fd", "ALP": "#f472b6", "AUD": "#a3a3a3",
      "WIL": "#2563eb", "HAA": "#e5e7eb", "CAD": "#facc15", "AMR": "#16a34a"}
_Q = [("ANT", "MER"), ("VER", "RBR"), ("RUS", "MER"), ("NOR", "MCL"), ("HAD", "RBR"), ("LIN", "RB"), ("PIA", "MCL"), ("LAW", "RB"), ("GAS", "ALP"), ("COL", "ALP"),
      ("LEC", "FER"), ("HAM", "FER"), ("HUL", "AUD"), ("SAI", "WIL"), ("BOR", "AUD"), ("ALB", "WIL"),
      ("CAM", "HAA"), ("PER", "CAD"), ("ALO", "AMR"), ("STR", "AMR"), ("BOT", "CAD"), ("BEA", "HAA")]
_GAP = {"ANT": "1:33.893", "VER": "+0.258", "RUS": "+0.331", "NOR": "+0.351", "HAD": "+0.699", "LIN": "+0.775"}
# позиция на старте (предварительно): Антонелли +5 → 6, Пиастри +10 → 17, Сайнс/Стролл/Берман в конец (20–22)
_GRID = {"VER": 1, "RUS": 2, "NOR": 3, "HAD": 4, "LIN": 5, "ANT": 6, "LAW": 7, "GAS": 8, "COL": 9, "LEC": 10, "HAM": 11, "HUL": 12, "BOR": 13, "ALB": 14,
         "CAM": 15, "PER": 16, "PIA": 17, "ALO": 18, "BOT": 19, "SAI": 20, "STR": 21, "BEA": 22}
_TAG = {"ANT": "+5", "PIA": "+10"}
def _rows(a, b, **kw):
    return [{"t": t, "c": _C[tm], **({k: v(t) for k, v in kw.items() if v(t)})} for t, tm in _Q[a:b]]

_Q3 = {"type": "grid", "start": 1, "rows": _rows(0, 10, v=lambda t: _GAP.get(t)), "hi": ["ANT"]}
_SHUF = {"type": "grid", "start": 1, "n": 10, "move": 0.3, "hi": ["VER", "ANT"],
         "rows": [{"t": t, "c": _C[tm], "p": i + 1, "to": _GRID[t], **({"tag": _TAG[t]} if t in _TAG else {})} for i, (t, tm) in enumerate(_Q[:11])]}
_Q1 = {"type": "grid", "start": 17, "out": True, "rows": _rows(16, 22)}
_Q2 = {"type": "grid", "start": 11, "out": True, "rows": _rows(10, 16), "hi": ["LEC", "HAM"]}

VIDEO = {
 "slug": "las-vegas-gp-2026-qualifying",
 "track": "las-vegas",
 "theme": "vegas",
 "hq": {"cars": [_SIL, _NAVY, _PAP, _RED], "lampFade": True},
 "shots": [
  {"type": "side", "car": 0, "side": 8.6, "side2": 8.0, "h": 1.1, "h2": 1.3, "fw": 2.5, "fw2": -1.5, "look": 0.5, "ly": 1.1, "fov": 56, **_N,
   "sphere": {"show": "number", "n": "P1", "t": "?", "s": 0.4, "y": 0.55}, "act": {**_CV, "at": 0.374, "v": 22}},
  {"type": "orbit", "at": 0.372, "tside": -110, "ly": 42, "r": 300, "r2": 270, "h": 26, "h2": 36, "a0": 0.15, "a1": 0.4, "fov": 50, **_N,
   "sphere": {"show": "lights", "s": 0.55}, "act": {**_CV, "at": 0.36}, "hud": _Q3},
  {"type": "orbit", "at": 0.38, "tside": -110, "ly": 22, "r": 230, "r2": 210, "h": 40, "h2": 34, "a0": -1.95, "a1": -1.75, "fov": 56, **_N,
   "sphere": {"show": "chequer"}, "act": {**_CV, "at": 0.366, "v": 30}, "hud": _SHUF},
  {"type": "carorbit", "car": 1, "r": 11, "r2": 10, "h": 1.5, "h2": 2.0, "a0": 0.6, "a1": 1.2, "fov": 48, "ly": 0.9, **_N,
   "sphere": {"show": "number", "n": "1", "t": "POLE", "s": 0.3, "y": 0.56}, "act": {**_CV, "at": 0.37, "v": 22, "n": 2}},
  {"type": "side", "car": 2, "side": 8.4, "side2": 7.8, "h": 1.2, "h2": 1.4, "fw": 2.0, "fw2": -3.0, "look": 0.5, "ly": 1.0, "fov": 54, **_N,
   "sphere": {"show": "number", "n": "17", "t": "PIA", "s": 0.32, "y": 0.56}, "act": {**_CV, "at": 0.372, "v": 24, "n": 3}},
  {"type": "side", "car": 0, "side": -8.4, "side2": -7.8, "h": 1.2, "h2": 1.5, "fw": 3.0, "fw2": -2.0, "look": 0.5, "ly": 1.0, "fov": 56, **_N,
   "sphere": {"show": "swirl"}, "act": {**_CV, "at": 0.378, "v": 26}},
  {"type": "orbit", "at": 0.362, "tside": -70, "ly": 0, "r": 320, "r2": 280, "h": 220, "h2": 190, "a0": 0.1, "a1": 0.4, "fov": 50, **_N,
   "sphere": {"show": "lights"}, "act": {**_CV, "at": 0.335, "v": 40}, "hud": _Q1},
  {"type": "orbit", "at": 0.372, "tside": -110, "ly": 55, "r": 340, "r2": 310, "h": 70, "h2": 50, "a0": 0.55, "a1": 0.3, "fov": 50, **_N,
   "sphere": {"show": "number", "n": "Q2", "t": "OUT", "c": ["#ef4444", "#ffffff"]}, "act": {**_CV, "at": 0.362}, "hud": _Q2},
  {"type": "carorbit", "car": 3, "r": 11.5, "r2": 10.5, "h": 1.5, "h2": 2.1, "a0": -0.5, "a1": 0.2, "fov": 48, "ly": 0.9, **_N,
   "sphere": {"show": "number", "n": "11 · 12", "t": "Q2", "s": 0.3, "y": 0.56}, "act": {**_CV, "at": 0.37, "v": 22}},
  {"type": "orbit", "at": 0.372, "tside": -110, "ly": 40, "r": 420, "r2": 400, "h": 120, "h2": 105, "a0": 0.3, "a1": 0.45, "fov": 50, **_N,
   "sphere": {"show": "lights"}, "act": {**_CV, "at": 0.362}},
  {"type": "orbit", "at": 0.372, "tside": -110, "ly": 40, "r": 430, "r2": 410, "h": 125, "h2": 115, "a0": 0.45, "a1": 0.55, "fov": 50, **_N, "sphere": {"show": "helmet"}}
 ],
 "coverShot": {"type": "carorbit", "car": 1, "r": 9.5, "h": 1.4, "a0": 1.75, "a1": 1.75, "fov": 44, **_N, "sphere": {"show": "number", "n": "1", "t": "POLE"}, "act": {**_CV, "at": 0.366, "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 1, "r": 9, "h": 1.3, "a0": 1.7, "a1": 1.7, "fov": 40, **_N, "sphere": {"show": "number", "n": "1", "t": "POLE"}, "act": {**_CV, "at": 0.368, "v": 1, "n": 2}}},
  {"name": "sphere", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "orbit", "at": 0.372, "tside": -110, "ly": 30, "r": 260, "h": 45, "a0": 0.35, "a1": 0.35, "fov": 50, **_N, "sphere": {"show": "chequer"}, "act": {**_CV, "at": 0.364}}},
  {"name": "red", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "side", "car": 3, "side": 6, "h": 1.2, "fw": 1, "look": 0.5, "ly": 1.0, "fov": 50, **_N, "sphere": {"show": "lights"}, "act": {**_CV, "at": 0.368, "v": 30}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "head": "Квалификация в Вегасе", "sub": "быстрее всех ≠ поул", "chip": "Быстрее всех ≠ поул",
    "say": "Самый быстрый круг в Вегасе проехал Антонелли. Но с поула стартует не он.",
    "hl": ["не", "он"]},
   {"kind": "big", "gh": "Квалификация · Q3", "min": 5.2,
    "say": "Антонелли опередил Ферстаппена на четверть секунды, Расселл и Норрис совсем рядом.",
    "hl": ["четверть"]},
   {"kind": "big", "gh": "Стартовая решётка · топ-10", "min": 7.2,
    "say": "Но у Антонелли шестой двигатель за сезон при лимите четыре. Штраф пять мест, он стартует шестым.",
    "hl": ["шестым"]},
   {"kind": "big", "chip": "P1 · Ферстаппен",
    "say": "Поул достаётся Ферстаппену, рядом Расселл. Второй ряд: Норрис и Хаджар.",
    "hl": ["Ферстаппену"]},
   {"kind": "big", "chip": "Пиастри: P7 → P17",
    "say": "Пиастри получил пятый двигатель: минус десять мест, старт с семнадцатого.",
    "hl": ["семнадцатого"]},
   {"kind": "big", "chip": "Сайнс · Стролл · Берман → хвост",
    "say": "Сайнс, Стролл и Берман тоже меняли детали мотора и уходят в хвост решётки.",
    "hl": ["хвост"]},
   {"kind": "big", "gh": "Вылетели в Q1", "min": 4.6,
    "say": "В первом сегменте вылетели Камара, Перес, Алонсо, Стролл, Боттас и Берман.",
    "hl": ["первом"]},
   {"kind": "big", "gh": "Вылетели в Q2", "min": 4.8,
    "say": "А во втором сегменте вылетели обе Ferrari: Леклер одиннадцатый, Хэмилтон двенадцатый.",
    "hl": ["обе", "Ferrari"]},
   {"kind": "big", "chip": "Старт: Леклер P10 · Хэмилтон P11",
    "say": "Леклер ошибся на лучшем круге и не успел на новую попытку. Хэмилтону не хватало сцепления.",
    "hl": ["ошибся", "сцепления"]},
   {"kind": "big", "chip": "22.11 · 08:00 по Тбилиси",
    "say": "Гонка в субботу в восемь вечера по Вегасу. В Тбилиси это воскресенье, восемь утра.",
    "hl": ["восемь"]},
   {"kind": "end", "tag": "Гран-при Лас-Вегаса · решётка",
    "say": "Гонку смотрите на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "big", "head": "Vegas qualifying", "sub": "fastest ≠ pole", "chip": "Fastest ≠ pole sitter",
    "say": "Antonelli was fastest in Vegas qualifying. But he won't start from pole.",
    "hl": ["won't"]},
   {"kind": "big", "gh": "Qualifying · Q3", "min": 5.2,
    "say": "Antonelli beat Verstappen by a quarter of a second. Russell and Norris were close.",
    "hl": ["quarter"]},
   {"kind": "big", "gh": "Starting grid · top 10", "min": 7.2,
    "say": "But it's his sixth engine of the season, against a limit of four. A five-place penalty drops him to sixth.",
    "hl": ["sixth"]},
   {"kind": "big", "chip": "P1 · Verstappen",
    "say": "So Verstappen gets pole, Russell joins him. Norris and Hadjar make row two.",
    "hl": ["Verstappen"]},
   {"kind": "big", "chip": "Piastri: P7 → P17",
    "say": "Piastri took a fifth engine: a ten-place drop, so he starts seventeenth.",
    "hl": ["seventeenth"]},
   {"kind": "big", "chip": "Sainz · Stroll · Bearman → back",
    "say": "Sainz, Stroll and Bearman also changed engine parts and go to the back.",
    "hl": ["back"]},
   {"kind": "big", "gh": "Out in Q1", "min": 4.6,
    "say": "Out in Q1: Camara, Perez, Alonso, Stroll, Bottas and Bearman.",
    "hl": ["Q1"]},
   {"kind": "big", "gh": "Out in Q2", "min": 4.8,
    "say": "And in Q2 both Ferraris went out: Leclerc eleventh, Hamilton twelfth.",
    "hl": ["both", "Ferraris"]},
   {"kind": "big", "chip": "Grid: Leclerc P10 · Hamilton P11",
    "say": "Leclerc made a mistake on his best lap and ran out of time. Hamilton was short of grip.",
    "hl": ["mistake", "grip"]},
   {"kind": "big", "chip": "Sat 8pm Vegas · Sun 04:00 UTC",
    "say": "The race starts Saturday at eight pm in Vegas. That's four am Sunday UTC.",
    "hl": ["eight"]},
   {"kind": "end", "tag": "Las Vegas GP · starting grid",
    "say": "Follow the race on the LapRadar live map."}
  ]
 }
}

# Итоги гонки Гран-при Лас-Вегаса 2026 (сб 21.11 по местному времени): Ферстаппен выиграл с поула, Норрис и Пиастри (с P17) на подиуме;
# столкновение Ferrari (Леклер +10 с), крыло Хаджара на рестарте, Расселл в барьере за три круга до конца (P3 → P9), Антонелли без энергии на последнем круге (P2 → P4),
# обе Aston Martin финишировали. HQ-режим, ночной Вегас со Sphere и неоном, таблицы позиций hud "grid" (условные цвета, без логотипов).
# Машины (VIDEO.hq.cars, условные цвета, без ливрей), как в vegasquali.py: 0 серебро с бирюзой, 1 тёмно-синяя с красным, 2 оранжевая, 3 красная.
# Камера (shots) общая для всех языков. Время старта по городам не называем: «смотрите по своему времени на LapRadar».
_SIL = ["#c3c8d0", "#14b8a6", "stripe"]
_NAVY = ["#1b2a6b", "#d61f3c", "stripe"]
_PAP = ["#ff8a1f", "#111827", "band"]
_RED = ["#d81e1e", "#f8fafc", "fade"]
_CV = {"type": "convoy", "at": 0.355, "v": 30, "n": 4}
_N = {"neon": True}
_REDP = {"c": "#d81e1e", "a": "#f8fafc", "p": "fade"}
_SILP = {"c": "#c3c8d0", "a": "#14b8a6", "p": "stripe"}
_GRN = {"c": "#0f5c3a", "a": "#c6f24e", "p": "stripe"}

# условные цвета-полоски команд в таблицах
_C = {"MER": "#2dd4bf", "RBR": "#3b5bdb", "MCL": "#ff8a1f", "FER": "#ef4444", "RB": "#93c5fd", "ALP": "#f472b6", "AUD": "#a3a3a3",
      "WIL": "#2563eb", "HAA": "#e5e7eb", "CAD": "#facc15", "AMR": "#16a34a"}
_TOP = [("VER", "RBR"), ("NOR", "MCL"), ("PIA", "MCL"), ("ANT", "MER"), ("GAS", "ALP"), ("COL", "ALP"), ("HAM", "FER"), ("SAI", "WIL"), ("RUS", "MER"), ("LEC", "FER")]
_PTS = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
_FIN = {"type": "grid", "start": 1, "hi": ["VER", "PIA"],
        "rows": [{"t": t, "c": _C[tm], "v": f"+{_PTS[i]}", **({"tag": "P17"} if t == "PIA" else {})} for i, (t, tm) in enumerate(_TOP)]}
# личный зачёт после Вегаса (gpblog, сверено с очками до гонки + очки за места)
_STD = {"type": "grid", "start": 1, "hi": ["VER"],
        "rows": [{"t": "ANT", "c": _C["MER"], "v": "402"}, {"t": "VER", "c": _C["RBR"], "v": "304"}, {"t": "HAM", "c": _C["FER"], "v": "267"},
                 {"t": "RUS", "c": _C["MER"], "v": "264"}, {"t": "NOR", "c": _C["MCL"], "v": "264"}]}

VIDEO = {
 "slug": "las-vegas-gp-2026-race",
 "track": "las-vegas",
 "theme": "vegas",
 "hq": {"cars": [_SIL, _NAVY, _PAP, _RED], "lampFade": True},
 "shots": [
  # 1 крючок: Ферстаппен (тёмно-синяя, машина 1) ведёт колонну
  {"type": "side", "car": 1, "side": 8.6, "side2": 8.0, "h": 1.1, "h2": 1.3, "fw": 2.5, "fw2": -1.5, "look": 0.5, "ly": 1.1, "fov": 56, **_N,
   "sphere": {"show": "number", "n": "1", "t": "WIN", "s": 0.4, "y": 0.55}, "act": {**_CV, "at": 0.374, "v": 22}},
  # 2 финиш, топ-10 с очками; подиум и Пиастри с P17
  {"type": "orbit", "at": 0.38, "tside": -110, "ly": 22, "r": 230, "r2": 210, "h": 40, "h2": 34, "a0": -1.95, "a1": -1.75, "fov": 56, **_N,
   "sphere": {"show": "chequer"}, "act": {**_CV, "at": 0.366, "v": 30}, "hud": _FIN},
  # 3 столкновение Ferrari: красная машина 0 крутится в повороте 7, красная 1 рядом
  {"type": "chase", "car": 0, "noCut": True, "dist": 14, "dist2": 12, "h": 6, "h2": 5, "side": 0, "look": 20, "fov": 52, **_N,
   "paint": {"0": _REDP, "1": _REDP}, "sphere": {"show": "number", "n": "38", "t": "LAP", "s": 0.3, "y": 0.56},
   "act": {"type": "slide", "corner": 6, "tc": 0.55, "v": 34, "followers": [1, 2]}},
  # 4 рестарт после машины безопасности: крыло Хаджара (машина 1)
  {"type": "side", "car": 1, "side": 8.4, "side2": 7.8, "h": 1.2, "h2": 1.5, "fw": 3.0, "fw2": -2.0, "look": 0.5, "ly": 1.0, "fov": 56, **_N,
   "sphere": {"show": "sc", "y": 0.6}, "act": {"type": "restart", "at": 0.36, "release": 0.3}},
  # 5 Расселл (серебро, машина 0) блокирует колёса в 5-м повороте
  {"type": "chase", "car": 0, "noCut": True, "dist": 14, "dist2": 12, "h": 6, "h2": 5, "side": 0, "look": 20, "fov": 52, **_N,
   "paint": {"0": _SILP, "1": _SILP}, "sphere": {"show": "number", "n": "3→9", "t": "RUS", "s": 0.3, "y": 0.56},
   "act": {"type": "slide", "corner": 4, "tc": 0.55, "v": 34, "followers": [1, 2]}},
  # 6 Антонелли без энергии, McLaren (оранжевая 2) рядом
  {"type": "side", "car": 0, "side": 8.4, "side2": 7.8, "h": 1.2, "h2": 1.5, "fw": 3.0, "fw2": -2.0, "look": 0.5, "ly": 1.0, "fov": 56, **_N,
   "sphere": {"show": "number", "n": "2→4", "t": "ANT", "s": 0.3, "y": 0.56}, "act": {**_CV, "at": 0.378, "v": 26, "n": 3}},
  # 7 обе Aston Martin на финише (условный зелёный)
  {"type": "carorbit", "car": 0, "r": 11, "r2": 10, "h": 1.5, "h2": 2.0, "a0": 0.6, "a1": 1.2, "fov": 48, "ly": 0.9, **_N,
   "paint": {"0": _GRN, "1": _GRN}, "sphere": {"show": "number", "n": "2/2", "t": "FINISH", "s": 0.3, "y": 0.56},
   "act": {**_CV, "at": 0.37, "v": 22, "n": 2}},
  # 8 личный зачёт
  {"type": "orbit", "at": 0.372, "tside": -110, "ly": 55, "r": 340, "r2": 310, "h": 70, "h2": 50, "a0": 0.55, "a1": 0.3, "fov": 50, **_N,
   "sphere": {"show": "helmet"}, "act": {**_CV, "at": 0.362}, "hud": _STD},
  # 9 призыв: время Катара по своему поясу
  {"type": "orbit", "at": 0.372, "tside": -110, "ly": 40, "r": 420, "r2": 400, "h": 120, "h2": 105, "a0": 0.3, "a1": 0.45, "fov": 50, **_N,
   "sphere": {"show": "lights"}, "act": {**_CV, "at": 0.362}},
  # 10 конец
  {"type": "orbit", "at": 0.372, "tside": -110, "ly": 40, "r": 430, "r2": 410, "h": 125, "h2": 115, "a0": 0.45, "a1": 0.55, "fov": 50, **_N, "sphere": {"show": "chequer"}}
 ],
 "coverShot": {"type": "carorbit", "car": 1, "r": 9.5, "h": 1.4, "a0": 1.75, "a1": 1.75, "fov": 44, **_N, "sphere": {"show": "number", "n": "1", "t": "WIN"}, "act": {**_CV, "at": 0.366, "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 1, "r": 9, "h": 1.3, "a0": 1.7, "a1": 1.7, "fov": 40, **_N, "sphere": {"show": "number", "n": "1", "t": "WIN"}, "act": {**_CV, "at": 0.368, "v": 1, "n": 2}}},
  {"name": "sphere", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "orbit", "at": 0.372, "tside": -110, "ly": 30, "r": 260, "h": 45, "a0": 0.35, "a1": 0.35, "fov": 50, **_N, "sphere": {"show": "chequer"}, "act": {**_CV, "at": 0.364}}},
  {"name": "red", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "side", "car": 3, "side": 6, "h": 1.2, "fw": 1, "look": 0.5, "ly": 1.0, "fov": 50, **_N, "sphere": {"show": "lights"}, "act": {**_CV, "at": 0.368, "v": 30}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "head": "Гонка в Вегасе", "sub": "с поула к победе", "chip": "Ферстаппен: P1 → P1",
    "say": "Ферстаппен выиграл Вегас с поула. А позади творилось безумие.",
    "hl": ["выиграл", "безумие"]},
   {"kind": "big", "gh": "Финиш · топ-10 · очки", "min": 5.4,
    "say": "Норрис второй, Пиастри третий, хотя стартовал семнадцатым.",
    "hl": ["семнадцатым"]},
   {"kind": "big", "chip": "Круг 38 · Леклер × Хэмилтон",
    "say": "Круг тридцать восемь: Леклер задевает напарника, Хэмилтон крутится. Леклеру десять секунд штрафа.",
    "hl": ["напарника", "десять"]},
   {"kind": "big", "chip": "Хаджар: сломано крыло · P14",
    "say": "После машины безопасности у Хаджара сломалось переднее крыло. Итог: четырнадцатый.",
    "hl": ["крыло"]},
   {"kind": "big", "chip": "Расселл: P3 → P9",
    "say": "За три круга до конца Расселл шёл третьим. Блокировка, барьер, финиш девятым.",
    "hl": ["барьер", "девятым"]},
   {"kind": "big", "chip": "Антонелли: P2 → P4",
    "say": "На последнем круге Антонелли остался без энергии, и обе McLaren прошли его.",
    "hl": ["энергии"]},
   {"kind": "big", "chip": "Aston Martin: 2 из 2 на финише",
    "say": "Обе Aston Martin доехали до финиша. В этом сезоне это редкость.",
    "hl": ["Обе", "редкость"]},
   {"kind": "big", "gh": "Личный зачёт", "min": 4.8,
    "say": "Ферстаппен укрепился на втором месте в чемпионате.",
    "hl": ["втором"]},
   {"kind": "big", "chip": "Дальше Катар · lapradar.com",
    "say": "Дальше Катар. Во сколько гонка по вашему времени, смотрите на ЛапРадар.",
    "hl": ["вашему времени"]},
   {"kind": "end", "tag": "Гран-при Лас-Вегаса · итоги",
    "say": "Гонки на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "big", "head": "Vegas race", "sub": "pole to win", "chip": "Verstappen: P1 → P1",
    "say": "Verstappen won Vegas from pole. Behind him, pure chaos.",
    "hl": ["won", "chaos"]},
   {"kind": "big", "gh": "Result · top 10 · points", "min": 5.4,
    "say": "Norris second, Piastri third, after starting seventeenth.",
    "hl": ["seventeenth"]},
   {"kind": "big", "chip": "Lap 38 · Leclerc × Hamilton",
    "say": "Lap thirty-eight: Leclerc hits his teammate and Hamilton spins. Ten seconds for Leclerc.",
    "hl": ["teammate", "Ten"]},
   {"kind": "big", "chip": "Hadjar: broken wing · P14",
    "say": "After the safety car, Hadjar's front wing broke. He finished fourteenth.",
    "hl": ["wing"]},
   {"kind": "big", "chip": "Russell: P3 → P9",
    "say": "Three laps from the end Russell was third. A lock-up, the barrier, and ninth place.",
    "hl": ["barrier", "ninth"]},
   {"kind": "big", "chip": "Antonelli: P2 → P4",
    "say": "On the last lap Antonelli ran out of energy, and both McLarens went past.",
    "hl": ["energy"]},
   {"kind": "big", "chip": "Aston Martin: 2 of 2 finish",
    "say": "Both Aston Martins reached the flag. This season, that's rare.",
    "hl": ["Both", "rare"]},
   {"kind": "big", "gh": "Drivers' standings", "min": 4.8,
    "say": "Verstappen tightened his grip on second in the championship.",
    "hl": ["second"]},
   {"kind": "big", "chip": "Next: Qatar · lapradar.com",
    "say": "Qatar is next. Check the race start in your own time zone on LapRadar.",
    "hl": ["your own time zone"]},
   {"kind": "end", "tag": "Las Vegas GP · race result",
    "say": "Follow every race on the LapRadar live map."}
  ]
 }
}

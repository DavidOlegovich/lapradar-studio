# Палоу, пятый титул IndyCar: клинч 30.08.2026 на Milwaukee Mile за гонку до финала (Лагуна-Сека), титулы 2021, 2023, 2024, 2025, 2026,
# четыре подряд = рекорд Бурде 2004-07, третье место за все годы (Фойт 7, Диксон 6), 6 побед и 8 поулов, Индианаполис-500 2025.
# Нейтрально, цитат нет. Источники: tools/topics.md («Источники 27.11: Палоу, пятый титул»). HQ, овал. Машины условные, без ливрей.
_B = {"c": "#1d4ed8", "a": "#e5e7eb", "p": "stripe"}
_R = {"c": "#c2272d", "a": "#e5e7eb", "p": "stripe"}
_PAINT = {"0": _B, "1": _R, "2": _B, "3": _R}
_CV = {"type": "convoy", "at": "straight", "n": 2, "v": 62}

VIDEO = {
 "slug": "palou-fifth-indycar-title-2026",
 "track": "oval",
 "theme": "day",
 "hq": True,
 "coverText": {"ru": {"head": "ПАЛОУ: ПЯТЬ ТИТУЛОВ", "sub": "IndyCar 2026"},
               "en": {"head": "PALOU: FIVE TITLES", "sub": "IndyCar 2026"}},
 "shots": [
  # 1 крючок
  {"type": "chase", "car": 0, "dist": 9, "dist2": 8, "h": 3.2, "h2": 3, "side": 0, "side2": 1.2, "look": 14, "drop": 3, "noCut": True, "paint": _PAINT, "act": {**_CV, "n": 1}},
  # 2 Милуоки, 30 августа
  {"type": "chase", "car": 3, "dist": 14, "dist2": 12, "h": 5, "h2": 4.5, "side": 2, "look": 18, "drop": 3, "fov": 50, "noCut": True, "paint": _PAINT, "act": {**_CV, "n": 4, "v": 50}},
  # 3 четыре подряд
  {"type": "carorbit", "car": 0, "r": 11, "r2": 10, "h": 2.2, "h2": 1.7, "a0": 0.7, "a1": 1.4, "fov": 48, "ly": 0.8, "paint": _PAINT, "act": {**_CV, "v": 22, "n": 1}},
  # 4 третье место: Фойт, Диксон
  {"type": "stage", "items": [{"o": "podium"}, {"o": "trophy", "y": 2.2, "s": 0.6}], "bg": "gold", "r": 14, "r2": 12, "h": 4, "h2": 4.5, "a0": -0.3, "a1": 0.3, "spin": 0, "ly": 2.2},
  # 5 шесть побед, восемь поулов
  {"type": "side", "car": 0, "side": 6.5, "side2": 6, "h": 1.0, "h2": 1.3, "fw": 2.5, "fw2": -1.5, "look": 0.5, "ly": 0.9, "fov": 52, "paint": _PAINT, "act": {**_CV, "v": 40, "n": 1}},
  # 6 путь: Япония, Coyne, Ganassi
  {"type": "chase", "car": 0, "dist": 8, "dist2": 7.5, "h": 3, "h2": 2.8, "side": -1.2, "side2": 1.2, "look": 14, "drop": 3, "noCut": True, "paint": _PAINT, "act": {**_CV, "n": 2, "t0": 2}},
  # 7 Индианаполис-500 2025
  {"type": "chase", "car": 3, "dist": 13, "dist2": 12, "h": 5, "h2": 4.5, "side": 0, "side2": 1.5, "look": 20, "drop": 3, "fov": 48, "noCut": True, "paint": _PAINT, "act": {**_CV, "n": 4, "v": 56}},
  # 8 конец
  {"type": "chase", "car": 3, "dist": 22, "dist2": 20, "h": 8, "h2": 7.5, "side": -2, "side2": 0, "look": 22, "drop": 3, "fov": 50, "noCut": True, "paint": _PAINT, "act": {**_CV, "n": 4, "v": 50}}
 ],
 "coverShot": {"type": "chase", "car": 0, "dist": 11, "h": 3.4, "side": 0, "look": 20, "drop": 2, "fov": 46, "paint": _PAINT, "act": {**_CV, "n": 1, "v": 8}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 8.5, "h": 1.8, "a0": 2.4, "a1": 2.4, "fov": 42, "ly": 0.6, "paint": _PAINT, "act": {**_CV, "n": 1, "v": 1}}},
  {"name": "pack", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 3, "dist": 17, "h": 6.5, "side": 2.5, "look": 20, "drop": 3, "fov": 48, "paint": _PAINT, "act": {**_CV, "n": 4, "v": 50}}},
  {"name": "side", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "side", "car": 0, "side": 6, "h": 1.1, "fw": 0.5, "look": 0.5, "ly": 0.9, "fov": 46, "paint": _PAINT, "act": {**_CV, "n": 1, "v": 40}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "big": "5", "chip": "Палоу · пятый титул IndyCar",
    "say": "Пять титулов IndyCar, и ему всего двадцать девять. Алекс Палоу снова чемпион.",
    "hl": ["Пять", "двадцать девять"]},
   {"kind": "big", "big": "30.08", "chip": "Милуоки · за гонку до финала",
    "say": "Титул решился тридцатого августа в Милуоки, за одну гонку до финала сезона.",
    "hl": ["тридцатого августа", "Милуоки"]},
   {"kind": "big", "big": "4", "chip": "Четыре титула подряд · 2023–2026",
    "say": "Четвёртый титул подряд. Столько же выиграл Себастьен Бурде в Чамп Кар, в две тысячи четвёртом–седьмом.",
    "hl": ["Четвёртый", "Бурде"]},
   {"kind": "big", "chip": "Фойт 7 · Диксон 6 · Палоу 5",
    "say": "По числу титулов он теперь третий за всю историю. Впереди только Эй Джей Фойт и Скотт Диксон.",
    "hl": ["третий", "Фойт", "Диксон"]},
   {"kind": "big", "big": "6", "chip": "6 побед · 8 поулов в 2026",
    "say": "В этом сезоне у Палоу шесть побед и восемь поулов, больше, чем у остальных.",
    "hl": ["шесть побед", "восемь поулов"]},
   {"kind": "big", "big": "2021", "chip": "Super Formula 2019 · Coyne 2020 · Ganassi 2021",
    "say": "Японская Супер Формула в девятнадцатом, IndyCar у Дейла Койна в двадцатом, титул с Ганасси в двадцать первом.",
    "hl": ["Супер", "Ганасси"]},
   {"kind": "big", "big": "2025", "chip": "Индианаполис 500 · 2025",
    "say": "А в две тысячи двадцать пятом он выиграл «Индианаполис пятьсот» и стал первым испанцем в списке победителей.",
    "hl": ["Индианаполис", "испанцем"]},
   {"kind": "end", "tag": "IndyCar · Палоу",
    "say": "Календарь и таблицу IndyCar смотрите на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "big", "big": "5", "chip": "Palou · fifth IndyCar title",
    "say": "Five IndyCar titles, and he is only twenty-nine. Alex Palou is champion again.",
    "hl": ["Five", "twenty-nine"]},
   {"kind": "big", "big": "30.08", "chip": "Milwaukee · one race to spare",
    "say": "It was settled on the thirtieth of August at Milwaukee, one race before the season finale.",
    "hl": ["thirtieth of August", "Milwaukee"]},
   {"kind": "big", "big": "4", "chip": "Four straight titles · 2023–2026",
    "say": "Fourth title in a row. Sebastien Bourdais won four straight in Champ Car, two thousand four to seven.",
    "hl": ["Fourth", "Bourdais"]},
   {"kind": "big", "chip": "Foyt 7 · Dixon 6 · Palou 5",
    "say": "He is now third on the all-time list. Only A.J. Foyt and Scott Dixon have more titles.",
    "hl": ["third", "Foyt", "Dixon"]},
   {"kind": "big", "big": "6", "chip": "6 wins · 8 poles in 2026",
    "say": "This season Palou has six wins and eight poles, more than anyone else.",
    "hl": ["six wins", "eight poles"]},
   {"kind": "big", "big": "2021", "chip": "Super Formula 2019 · Coyne 2020 · Ganassi 2021",
    "say": "Japanese Super Formula in twenty nineteen, IndyCar with Dale Coyne in twenty twenty, Ganassi title in twenty twenty-one.",
    "hl": ["Super Formula", "Ganassi"]},
   {"kind": "big", "big": "2025", "chip": "Indianapolis 500 · 2025",
    "say": "And in twenty twenty-five he won the Indianapolis five hundred, the first Spaniard to do it.",
    "hl": ["Indianapolis", "Spaniard"]},
   {"kind": "end", "tag": "IndyCar · Palou",
    "say": "Follow the IndyCar calendar and standings on the LapRadar live map."}
  ]
 }
}

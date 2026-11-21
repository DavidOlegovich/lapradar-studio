# Формула E, сезон 2026/27 (эра Gen4): этап в Джидде 18–19.12.2026 перенесён на 16–17.04.2027 из-за конфликта на Ближнем Востоке
# (объявлено 12.11.2026). Сезон открывает Мехико 16.01.2027, Санья сдвинута с 17.04 на 3.04, гонок по-прежнему 21.
# Контраст: F1 едет в Катар (конец ноября) и Абу-Даби (начало декабря). Не повторяет разбор о тестах Gen4 (formula-e-gen4-first-test).
# HQ-режим, трасса Мехико днём. Машины: условные цвета без ливрей. Календарь: hud "grid" (строки: этапы, дата справа или в плашке).
_CYAN = ["#0e7490", "#f8fafc", "stripe"]
_LIME = ["#65a30d", "#111827", "band"]
_PINK = ["#be185d", "#f8fafc", "split"]
_CV = {"type": "convoy", "at": 0.03, "v": 30, "n": 3}

_FE = "#22d3ee"
_CAL = {"type": "grid", "start": 1, "n": 7, "move": 0.42, "hi": ["JEDDAH", "MEXICO"], "rows": [
  {"t": "JEDDAH", "c": "#f59e0b", "p": 1, "to": 6, "tag0": "18–19.12", "tag": "16–17.04", "tc": "#d97706"},
  {"t": "MEXICO", "c": _FE, "p": 2, "to": 1, "v": "16.01"},
  {"t": "AUSTIN", "c": _FE, "p": 3, "to": 2, "v": "6.02"},
  {"t": "MIAMI", "c": _FE, "p": 4, "to": 3, "v": "20.02"},
  {"t": "SAO PAULO", "c": _FE, "p": 5, "to": 4, "v": "13.03"},
  {"t": "SANYA", "c": "#a78bfa", "p": 6, "to": 5, "tag0": "17.04", "tag": "3.04", "tc": "#7c3aed"},
  {"t": "MONACO", "c": _FE, "p": 7, "to": 7, "v": "1–2.05"}]}

VIDEO = {
 "slug": "formula-e-2027-calendar-jeddah-postponed",
 "track": "mexico-city",
 "theme": "day",
 "hq": {"cars": [_CYAN, _LIME, _PINK], "lampFade": True},
 "shots": [
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 5.5, "h2": 5, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 55, "n": 3}},
  {"type": "orbit", "at": 0.02, "r": 320, "r2": 290, "h": 110, "h2": 90, "a0": 0.3, "a1": 0.6, "fov": 50, "act": {**_CV, "at": 0.0, "v": 40}, "hud": _CAL},
  {"type": "carorbit", "car": 0, "r": 10, "r2": 9, "h": 1.4, "h2": 1.9, "a0": 0.5, "a1": 1.15, "fov": 46, "ly": 0.8, "act": {**_CV, "at": 0.05, "v": 22, "n": 1}},
  {"type": "side", "car": 0, "side": 8.4, "side2": 7.8, "h": 1.1, "h2": 1.3, "fw": 2.5, "fw2": -2.5, "look": 0.5, "ly": 0.9, "fov": 54, "act": {**_CV, "at": 0.06, "v": 28}},
  {"type": "carorbit", "car": 1, "r": 10.5, "r2": 9.5, "h": 1.5, "h2": 2.0, "a0": -0.5, "a1": 0.2, "fov": 48, "ly": 0.8, "act": {**_CV, "at": 0.42, "v": 22}},
  {"type": "chase", "car": 2, "dist": 16, "dist2": 14, "h": 6.5, "h2": 6, "side": 0, "side2": 0, "look": 25, "drop": 4, "noCut": True, "act": {"type": "convoy", "at": 0.04, "v": 55, "n": 3}},
  {"type": "chase", "car": 0, "dist": 14, "dist2": 12.5, "h": 6, "h2": 5.5, "side": 1.5, "side2": -1.5, "look": 22, "drop": 3, "noCut": True, "act": {"type": "follow", "at": 0.02}},
  {"type": "orbit", "at": 0.02, "r": 430, "r2": 410, "h": 130, "h2": 120, "a0": 1.2, "a1": 1.3, "fov": 50, "act": {**_CV, "at": 0.0, "v": 45}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 9.5, "h": 1.4, "a0": 1.85, "a1": 1.85, "fov": 44, "act": {**_CV, "at": 0.05, "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 7.5, "h": 1.2, "a0": 2.1, "a1": 2.1, "fov": 40, "ly": 0.6, "act": {**_CV, "at": 0.05, "v": 1, "n": 2}}},
  {"name": "mexico", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "side", "car": 0, "side": 6.5, "h": 1.2, "fw": 1, "look": 0.5, "ly": 1.0, "fov": 50, "act": {**_CV, "at": 0.06, "v": 30}}},
  {"name": "pack", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 2, "dist": 14, "h": 4.5, "side": -1.5, "look": 25, "drop": 3, "fov": 44, "act": {"type": "convoy", "at": "straight", "v": 55, "n": 3}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "head": "Формула E начнёт позже", "sub": "Джидда переехала в апрель", "chip": "Gen4 стартует в Мехико",
    "say": "Новая эра Формулы E начнётся на месяц позже. Первую гонку машин Gen4 примет не Джидда, а Мехико.",
    "hl": ["Мехико"]},
   {"kind": "big", "gh": "Формула E · новый календарь", "min": 6.2,
    "say": "Двойной этап в Джидде восемнадцатого и девятнадцатого декабря перенесли на шестнадцатое и семнадцатое апреля.",
    "hl": ["апреля"]},
   {"kind": "big", "chip": "Причина: конфликт в регионе",
    "say": "Причина в конфликте на Ближнем Востоке. Чемпионат сослался на обстановку в регионе и логистику.",
    "hl": ["Ближнем", "Востоке"]},
   {"kind": "big", "chip": "Мехико · 16 января",
    "say": "Теперь сезон откроет Мехико шестнадцатого января. Раньше этот этап стоял в календаре третьим.",
    "hl": ["шестнадцатого", "января"]},
   {"kind": "big", "chip": "Санья: 17.04 → 3.04",
    "say": "Джидда заняла апрельские выходные Саньи, а китайский этап сдвинули на две недели раньше, на третье апреля.",
    "hl": ["третье", "апреля"]},
   {"kind": "big", "chip": "Всё равно 21 гонка",
    "say": "Гонок по-прежнему двадцать одна: восемь двойных этапов и пять одиночных.",
    "hl": ["двадцать", "одна"]},
   {"kind": "big", "chip": "F1: Катар и Абу-Даби в силе",
    "say": "А Формула один на Ближний Восток едет: Катар в конце ноября, Абу-Даби в начале декабря.",
    "hl": ["Катар", "Абу-Даби"]},
   {"kind": "end", "tag": "Формула E · сезон 2026/27",
    "say": "Во сколько гонки по вашему времени, смотрите на ЛапРадар.", "hl": ["вашему", "времени"]}
  ],
  "en": [
   {"kind": "big", "head": "Formula E starts later", "sub": "Jeddah moves to April", "chip": "Gen4 starts in Mexico",
    "say": "Formula E's new era starts a month later. The first Gen4 race goes to Mexico City, not Jeddah.",
    "hl": ["Mexico", "City"]},
   {"kind": "big", "gh": "Formula E · new calendar", "min": 6.2,
    "say": "The Jeddah double-header on December eighteenth and nineteenth moves to April sixteenth and seventeenth.",
    "hl": ["April"]},
   {"kind": "big", "chip": "Reason: conflict in the region",
    "say": "The reason is the conflict in the Middle East. The series pointed to the situation in the region and logistics.",
    "hl": ["Middle", "East"]},
   {"kind": "big", "chip": "Mexico City · January 16",
    "say": "Mexico City now opens the season on January sixteenth. It was originally round three.",
    "hl": ["January", "sixteenth"]},
   {"kind": "big", "chip": "Sanya: 17.04 → 3.04",
    "say": "Jeddah takes Sanya's April weekend, and the China race moves two weeks earlier, to April third.",
    "hl": ["April", "third"]},
   {"kind": "big", "chip": "Still 21 races",
    "say": "It's still twenty-one races: eight double-headers and five single races.",
    "hl": ["twenty-one"]},
   {"kind": "big", "chip": "F1: Qatar and Abu Dhabi still on",
    "say": "Formula One, meanwhile, is still heading to the Middle East: Qatar at the end of November, Abu Dhabi in early December.",
    "hl": ["Qatar", "Abu", "Dhabi"]},
   {"kind": "end", "tag": "Formula E · 2026/27 season",
    "say": "Check race times in your own time zone on LapRadar.", "hl": ["your", "own", "time", "zone"]}
  ]
 }
}

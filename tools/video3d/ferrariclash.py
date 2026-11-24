# Ferrari 2026: Хэмилтон и Леклер, три эпизода за месяц. Мехико (1.11): первый круг, поворот 4, оба за трассой без контакта,
# Ферстаппен проходит Хэмилтона и побеждает, Леклеру +5 с (база 10 с, смягчили: Хэмилтон тоже вылетел), итог HAM P2, LEC P4;
# Вассёр: неуважение к команде. Сан-Паулу: разговор втроём перед гонкой. Лас-Вегас: круг 38, поворот 7, Леклер изнутри разворачивает
# Хэмилтона, стюарды: Леклер полностью виноват, +10 с, P10; Хэмилтон P7. Вассёр: «неприемлемо», тот же разговор, что после Мексики.
# Кубок конструкторов после Вегаса: Mercedes 666 (чемпион), Ferrari 517, Red Bull 440, McLaren 431, осталось 2 гонки.
# Нейтрально: без оценок, кроме решений стюардов; цитаты только короткие и подтверждённые. Источники: tools/topics.md («Источники 25.11»).
# HQ-режим, ночной Вегас. Машины условные: две красные (без ливрей и логотипов, разные акценты), синяя (Red Bull). Номера на Sphere.
# Камера (shots) общая для всех языков. Время по городам не называем.
_R44 = {"c": "#d81e1e", "a": "#f8fafc", "p": "stripe"}   # Хэмилтон: красная с белой полосой
_R16 = {"c": "#b3121b", "a": "#111827", "p": "band"}     # Леклер: красная с тёмным поясом
_BLU = {"c": "#1e3a8a", "a": "#e5e7eb", "p": "stripe"}   # Ферстаппен: условная синяя
_GRY = {"c": "#6b7280", "a": "#f8fafc", "p": "fade"}
_HQC = lambda d: [d["c"], d["a"], d["p"]]
_N = {"neon": True}
_CV = {"type": "convoy", "at": 0.374, "v": 22, "n": 2}
_TWO = [{"o": "f1", "c": _R44["c"], "a": _R44["a"], "p": _R44["p"], "x": -2.3, "ry": 0.25},
        {"o": "f1", "c": _R16["c"], "a": _R16["a"], "p": _R16["p"], "x": 2.3, "ry": -0.25}]
# условные цвета-полоски команд в таблицах
_C = {"MER": "#2dd4bf", "RBR": "#3b5bdb", "MCL": "#ff8a1f", "FER": "#ef4444"}
_MEX = {"type": "grid", "start": 1, "hi": ["HAM", "LEC"],
        "rows": [{"t": "VER", "c": _C["RBR"]}, {"t": "HAM", "c": _C["FER"]}, {"t": "ANT", "c": _C["MER"]}, {"t": "LEC", "c": _C["FER"], "tag": "+5"}]}
_WCC = {"type": "grid", "start": 1, "hi": ["FER"],
        "rows": [{"t": "MER", "c": _C["MER"], "v": "666"}, {"t": "FER", "c": _C["FER"], "v": "517", "tag": "+7"},
                 {"t": "RBR", "c": _C["RBR"], "v": "440"}, {"t": "MCL", "c": _C["MCL"], "v": "431"}]}

VIDEO = {
 "slug": "ferrari-hamilton-leclerc-2026",
 "track": "las-vegas",
 "theme": "vegas",
 "hq": {"cars": [_HQC(_R44), _HQC(_R16), _HQC(_BLU), _HQC(_GRY)], "lampFade": True},
 "coverText": {"ru": {"head": "ХЭМИЛТОН И ЛЕКЛЕР", "sub": "три эпизода за месяц"},
               "en": {"head": "HAMILTON AND LECLERC", "sub": "three flashpoints in a month"}},
 "shots": [
  # 1 крючок: две красные на прямой, камера за задней
  {"type": "chase", "car": 1, "dist": 13, "dist2": 12, "h": 5.5, "h2": 5, "side": 0, "side2": 0, "look": 24, "drop": 3, "noCut": True, **_N,
   "act": {"type": "convoy", "at": "straight", "v": 62, "n": 2}},
  # 2 Мехико, круг 1: колесо в колесо, красная 16 выходит вперёд
  {"type": "chase", "car": 0, "dist": 19, "dist2": 15, "h": 7, "h2": 6, "side": 2.5, "side2": 2.5, "look": 34, "drop": 3, "noCut": True, **_N,
   "act": {"type": "duel"}},
  # 3 Ферстаппен (синяя, машина 1) проходит красную 44
  {"type": "chase", "car": 0, "dist": 18, "dist2": 14, "h": 6.5, "h2": 5.5, "side": -2.5, "side2": -2.5, "look": 34, "drop": 3, "noCut": True, **_N,
   "paint": {"0": _R44, "1": _BLU}, "act": {"type": "duel"}},
  # 4 итог Мехико и штраф Леклера
  {"type": "orbit", "at": 0.38, "tside": -110, "ly": 22, "r": 230, "r2": 210, "h": 40, "h2": 34, "a0": -1.95, "a1": -1.75, "fov": 56, **_N,
   "sphere": {"show": "number", "n": "+5", "t": "SEC", "s": 0.4, "y": 0.56}, "act": {**_CV, "at": 0.366, "v": 30}, "hud": _MEX},
  # 5 Хэмилтон просит разговора, Вассёр: неуважение к команде (студия, две красные)
  {"type": "stage", "items": _TWO, "bg": "red", "r": 13, "r2": 11.5, "h": 3, "h2": 3.6, "a0": -0.35, "a1": 0.3, "spin": 0.05, "ly": 0.6},
  # 6 Сан-Паулу: разговор втроём (машины развёрнуты друг к другу)
  {"type": "stage", "items": [{**_TWO[0], "x": -2.0, "ry": 0.9}, {**_TWO[1], "x": 2.0, "ry": -0.9}], "bg": "blue",
   "r": 12.5, "r2": 11, "h": 2.8, "h2": 3.4, "a0": 0.3, "a1": -0.3, "spin": 0.04, "ly": 0.6},
  # 7 Лас-Вегас, круг 38, поворот 7: красная 44 разворачивается, красная 16 рядом
  {"type": "chase", "car": 0, "noCut": True, "dist": 14, "dist2": 12, "h": 6, "h2": 5, "side": 0, "look": 20, "fov": 52, **_N,
   "sphere": {"show": "number", "n": "38", "t": "LAP", "s": 0.3, "y": 0.56},
   "act": {"type": "slide", "corner": 6, "tc": 0.55, "v": 34, "followers": [1]}},
  # 8 решение стюардов: +10 с Леклеру
  {"type": "carorbit", "car": 1, "r": 11, "r2": 10, "h": 1.5, "h2": 2.0, "a0": 0.6, "a1": 1.2, "fov": 48, "ly": 0.9, **_N,
   "sphere": {"show": "number", "n": "+10", "t": "SEC", "s": 0.3, "y": 0.56}, "act": {**_CV, "at": 0.37}},
  # 9 Вассёр: «неприемлемо»; Леклер признал ошибку (студия)
  {"type": "stage", "items": [{**_TWO[0], "x": -2.6, "ry": -0.4}, {**_TWO[1], "x": 2.6, "ry": 0.4}], "bg": "red",
   "r": 12, "r2": 10.5, "h": 3.2, "h2": 3.8, "a0": -0.6, "a1": 0.2, "spin": 0.05, "ly": 0.6},
  # 10 Кубок конструкторов
  {"type": "orbit", "at": 0.372, "tside": -110, "ly": 55, "r": 340, "r2": 310, "h": 70, "h2": 50, "a0": 0.55, "a1": 0.3, "fov": 50, **_N,
   "sphere": {"show": "number", "n": "517", "t": "PTS", "s": 0.4, "y": 0.56}, "act": {**_CV, "at": 0.362}, "hud": _WCC},
  # 11 конец
  {"type": "orbit", "at": 0.372, "tside": -110, "ly": 40, "r": 430, "r2": 410, "h": 125, "h2": 115, "a0": 0.45, "a1": 0.55, "fov": 50, **_N, "sphere": {"show": "chequer"}}
 ],
 "coverShot": {"type": "chase", "car": 1, "dist": 7.5, "h": 2.2, "side": 2.6, "look": 12, "drop": 1, "fov": 48, **_N,
               "sphere": {"show": "number", "n": "44 16", "s": 0.4}, "act": {**_CV, "at": 0.366, "v": 1}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 1, "dist": 7.5, "h": 2.2, "side": 2.6, "look": 12, "drop": 1, "fov": 44, **_N,
            "sphere": {"show": "number", "n": "44 16", "s": 0.4}, "act": {**_CV, "at": 0.368, "v": 1}}},
  {"name": "mexico", "w": 1200, "h": 800, "t": 1.6, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 8, "h": 2.4, "side": 1.2, "look": 10, "drop": 1, "fov": 46, **_N, "act": {"type": "duel"}}},
  {"name": "vegas", "w": 1200, "h": 800, "t": 2.4, "u": 0.55,
   "shot": {"type": "chase", "car": 0, "dist": 12, "h": 5, "side": 1.5, "look": 20, "fov": 46, **_N,
            "act": {"type": "slide", "corner": 6, "tc": 0.55, "v": 34, "followers": [1]}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "chip": "Мехико · Сан-Паулу · Лас-Вегас",
    "say": "Второй конфликт за три недели. Что происходит между Хэмилтоном и Леклером?",
    "hl": ["Второй", "конфликт"]},
   {"kind": "big", "chip": "Мехико · круг 1 · поворот 4",
    "say": "Мехико, первый круг. Хэмилтон и Леклер идут колесо в колесо, и обе Феррари вылетают за трассу.",
    "hl": ["вылетают"]},
   {"kind": "big", "chip": "Ферстаппен проходит Хэмилтона",
    "say": "Контакта нет, но Ферстаппен проходит Хэмилтона и побеждает.",
    "hl": ["побеждает"]},
   {"kind": "big", "gh": "Мехико · итог", "min": 4.2,
    "say": "Леклеру пять секунд штрафа. Хэмилтон второй, Леклер четвёртый.",
    "hl": ["пять", "секунд"]},
   {"kind": "big", "chip": "Вассёр: неуважение к команде",
    "say": "Хэмилтон просит разговора. Вассёр: это неуважение к команде.",
    "hl": ["неуважение"]},
   {"kind": "big", "chip": "Сан-Паулу · разговор втроём",
    "say": "Перед Бразилией Вассёр собрал обоих. Вышли, по его словам, шутя.",
    "hl": ["шутя"]},
   {"kind": "big", "chip": "Лас-Вегас · круг 38 · поворот 7",
    "say": "Вегас, круг тридцать восемь. Атака изнутри, и Хэмилтона разворачивает.",
    "hl": ["разворачивает"]},
   {"kind": "big", "chip": "Леклер +10 с · P10 · Хэмилтон P7",
    "say": "Стюарды винят Леклера: плюс десять секунд. Хэмилтон седьмой.",
    "hl": ["десять", "секунд"]},
   {"kind": "big", "chip": "Вассёр: «неприемлемо»",
    "say": "Леклер извинился. Вассёр: неприемлемо, как и после Мексики.",
    "hl": ["неприемлемо"]},
   {"kind": "big", "gh": "Кубок конструкторов", "min": 4.2,
    "say": "Феррари вторая в Кубке конструкторов, в Вегасе всего семь очков.",
    "hl": ["вторая", "семь"]},
   {"kind": "end", "tag": "Хэмилтон и Леклер · хронология",
    "say": "Все дуэли напарников на живой карте ЛапРадар.", "hl": ["ЛапРадар"]}
  ],
  "en": [
   {"kind": "big", "chip": "Mexico · São Paulo · Las Vegas",
    "say": "A second clash in three weeks. What's up with Hamilton and Leclerc?",
    "hl": ["second", "clash"]},
   {"kind": "big", "chip": "Mexico · lap 1 · Turn 4",
    "say": "Mexico, lap one. Hamilton and Leclerc go wheel to wheel, and both Ferraris run off the track.",
    "hl": ["off"]},
   {"kind": "big", "chip": "Verstappen passes Hamilton",
    "say": "No contact, but Verstappen gets past Hamilton and wins.",
    "hl": ["wins"]},
   {"kind": "big", "gh": "Mexico · result", "min": 4.2,
    "say": "Leclerc gets five seconds. Hamilton finishes second, Leclerc fourth.",
    "hl": ["five", "seconds"]},
   {"kind": "big", "chip": "Vasseur: a lack of respect",
    "say": "Hamilton wants serious talks. Vasseur calls it a lack of respect.",
    "hl": ["respect"]},
   {"kind": "big", "chip": "São Paulo · a three-way talk",
    "say": "Before Brazil, Vasseur sits them down. He says they left joking.",
    "hl": ["joking"]},
   {"kind": "big", "chip": "Las Vegas · lap 38 · Turn 7",
    "say": "Vegas, lap thirty-eight. A dive up the inside, and Hamilton is spun.",
    "hl": ["spun"]},
   {"kind": "big", "chip": "Leclerc +10 s · P10 · Hamilton P7",
    "say": "The stewards blame Leclerc: ten seconds. Hamilton finishes seventh.",
    "hl": ["ten", "seconds"]},
   {"kind": "big", "chip": "Vasseur: \"unacceptable\"",
    "say": "Leclerc apologises. Vasseur: unacceptable, same message as Mexico.",
    "hl": ["unacceptable"]},
   {"kind": "big", "gh": "Constructors' championship", "min": 4.2,
    "say": "Ferrari are second in the constructors', with only seven points from Vegas.",
    "hl": ["second", "seven"]},
   {"kind": "end", "tag": "Hamilton and Leclerc · the timeline",
    "say": "Every race and team-mate duel on the LapRadar live map.", "hl": ["LapRadar"]}
  ]
 }
}

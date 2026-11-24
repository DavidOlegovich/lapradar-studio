# Ферстаппен может закрыть второе место в личном зачёте F1 2026 уже в Катаре (27–29.11.2026). Только условия, без прогнозов.
# После Вегаса (офиц. таблица formula1.com): ANT 402, VER 304, HAM 267, RUS 264, NOR 264, LEC 250. Осталось Катар и Абу-Даби, спринтов нет,
# очка за быстрый круг нет (с 2025): максимум 25 за гонку. Тай-брейк: больше побед (VER 4, RUS 3, NOR 3, HAM 1).
# Расчёт (перебор всех исходов Катара): VER в тройке → P2 его при любом раскладе; P4 → если Катар не выиграл HAM;
# без очков → если никто из HAM, RUS, NOR не на подиуме. В очках: HAM не больше чем +12 к VER, RUS и NOR не больше чем +14.
# Источники: tools/topics.md («Источники 25.11: Ферстаппен и P2»). HQ-режим, Лусаил ночью, условные цвета без ливрей.
# Машины (VIDEO.hq.cars): 0 тёмно-синяя (VER), 1 красная (HAM), 2 серебристая (RUS), 3 оранжевая (NOR). Время старта не называем.
_NAVY = ["#1b2a6b", "#d61f3c", "stripe"]
_RED = ["#d81e1e", "#f8fafc", "fade"]
_SIL = ["#c3c8d0", "#14b8a6", "stripe"]
_PAP = ["#ff8a1f", "#111827", "band"]
_CV = {"type": "convoy", "at": 0.02, "v": 30, "n": 4}

# условные цвета-полоски в таблице (без логотипов)
_C = {"MER": "#2dd4bf", "RBR": "#3b5bdb", "MCL": "#ff8a1f", "FER": "#ef4444"}
_STD = {"type": "grid", "start": 1, "hi": ["VER"],
        "rows": [{"t": "ANT", "c": _C["MER"], "v": "402"}, {"t": "VER", "c": _C["RBR"], "v": "304"}, {"t": "HAM", "c": _C["FER"], "v": "267"},
                 {"t": "RUS", "c": _C["MER"], "v": "264"}, {"t": "NOR", "c": _C["MCL"], "v": "264"}, {"t": "LEC", "c": _C["FER"], "v": "250"}]}
_WINS = {"type": "bars", "rows": [{"label": "VER", "v": 4, "c": "#3b5bdb"}, {"label": "RUS", "v": 3, "c": "#9ca3af"},
                                  {"label": "NOR", "v": 3, "c": "#ff8a1f"}, {"label": "HAM", "v": 1, "c": "#ef4444"}], "min": 0, "max": 4, "hi": 0}

VIDEO = {
 "slug": "verstappen-p2-qatar-scenarios",
 "track": "lusail",
 "theme": "night",
 "hq": {"cars": [_NAVY, _RED, _SIL, _PAP], "lampFade": True},
 "shots": [
  # 1 крючок: тёмно-синяя машина ведёт колонну на прямой
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 5.5, "h2": 5, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 62, "n": 4}},
  # 2 таблица после Вегаса поверх облёта старта
  {"type": "orbit", "at": 0.02, "r": 430, "r2": 410, "h": 130, "h2": 120, "a0": 1.2, "a1": 1.3, "fov": 50, "act": {**_CV, "at": 0.0, "v": 45}, "hud": _STD},
  # 3 максимум 25 за гонку: низкий проезд рядом с машиной
  {"type": "side", "car": 0, "side": 8.4, "side2": 7.8, "h": 1.1, "h2": 1.3, "fw": 2.5, "fw2": -2.5, "look": 0.5, "ly": 0.9, "fov": 54, "act": {**_CV, "at": 0.62, "v": 28}},
  # 4 Леклер выбыл, в борьбе трое: камера за последней машиной, впереди вся группа
  {"type": "chase", "car": 3, "dist": 12, "dist2": 10.5, "h": 5, "h2": 4.6, "side": 1.5, "side2": 1.5, "look": 26, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 55, "n": 4}},
  # 5 подиум: студия с пьедесталом и кубком
  {"type": "stage", "items": [{"o": "podium"}, {"o": "trophy", "y": 2.2, "s": 0.6}], "bg": "gold", "r": 14, "r2": 12, "h": 4, "h2": 4.5, "a0": -0.3, "a1": 0.3, "spin": 0, "ly": 2.2},
  # 6 P4, если Катар не выиграет Хэмилтон: тёмно-синяя против красной
  {"type": "chase", "car": 0, "dist": 13, "dist2": 11, "h": 5, "h2": 4.5, "side": -2.5, "side2": 2, "look": 20, "drop": 3, "noCut": True, "act": {"type": "duel"}},
  # 7 без очков: облёт машины
  {"type": "carorbit", "car": 0, "r": 9.5, "r2": 8.5, "h": 1.3, "h2": 1.7, "a0": 0.4, "a1": 1.05, "fov": 46, "ly": 0.7, "act": {**_CV, "at": 0.7, "v": 30}},
  # 8 тай-брейк: победы
  {"type": "stage", "items": [{"o": "f1", "c": _NAVY[0], "a": _NAVY[1], "p": _NAVY[2]}], "bg": "blue", "r": 11, "r2": 9.5, "h": 2.6, "h2": 3.2, "a0": 0.9, "a1": -0.2, "spin": 0.2, "ly": 0.8, "hud": _WINS},
  # 9 финал
  {"type": "orbit", "at": 0.05, "r": 330, "r2": 300, "h": 90, "h2": 70, "a0": 0.4, "a1": 0.8, "fov": 50, "act": {**_CV, "at": 0.04, "v": 45}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 9.5, "h": 1.4, "a0": 1.85, "a1": 1.85, "fov": 44, "act": {**_CV, "at": 0.02, "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 7.5, "h": 1.2, "a0": 2.6, "a1": 2.6, "fov": 40, "ly": 0.6, "act": {**_CV, "at": 0.04, "v": 1, "n": 2}}},
  {"name": "pack", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 3, "dist": 9, "h": 4.2, "side": 2.2, "look": 26, "drop": 3, "fov": 46, "act": {"type": "convoy", "at": "straight", "v": 55, "n": 4}}},
  {"name": "duel", "w": 1200, "h": 800, "t": 1.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 10, "h": 3.8, "side": -2.4, "look": 12, "drop": 2, "fov": 42, "act": {"type": "duel"}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "head": "P2 уже в Катаре?", "sub": "Ферстаппен и второе место", "chip": "Ферстаппен · P2 в Катаре?",
    "say": "Ферстаппен может закрыть второе место уже в Катаре. Что для этого нужно?",
    "hl": ["в", "Катаре"]},
   {"kind": "big", "gh": "Личный зачёт после Вегаса", "min": 5,
    "say": "У Ферстаппена триста четыре. Хэмилтон отстаёт на тридцать семь, Расселл и Норрис на сорок.",
    "hl": ["тридцать", "семь", "сорок"]},
   {"kind": "big", "big": "25", "chip": "Катар 25 · Абу-Даби 25",
    "say": "Спринтов и очка за быстрый круг не будет. За гонку максимум двадцать пять.",
    "hl": ["двадцать", "пять"]},
   {"kind": "big", "chip": "Леклер −54 · уже не догонит",
    "say": "Леклер отстаёт на пятьдесят четыре и уже не догонит. В борьбе трое.",
    "hl": ["трое"]},
   {"kind": "big", "big": "ТОП-3", "chip": "Ферстаппен на подиуме → P2",
    "say": "Если он в Катаре на подиуме, второе место его при любом раскладе.",
    "hl": ["на", "подиуме"]},
   {"kind": "big", "big": "P4", "chip": "P4 · если Хэмилтон не победит",
    "say": "Четвёртого места хватит, если гонку не выиграет Хэмилтон.",
    "hl": ["Хэмилтон"]},
   {"kind": "big", "big": "0", "chip": "0 очков · трое без подиума",
    "say": "Даже без очков хватит, если никто из троих не будет на подиуме.",
    "hl": ["без", "очков"]},
   {"kind": "big",
    "say": "При равенстве очков выше тот, у кого больше побед. У Ферстаппена их четыре.",
    "hl": ["побед", "четыре"]},
   {"kind": "end", "tag": "Катар · 27–29 ноября",
    "say": "Во сколько гонка по вашему времени, смотрите на ЛапРадар.",
    "hl": ["вашему", "времени"]}
  ],
  "en": [
   {"kind": "big", "head": "P2 in Qatar?", "sub": "Verstappen and second place", "chip": "Verstappen · P2 in Qatar?",
    "say": "Verstappen could lock up second place in Qatar. What does he need?",
    "hl": ["in", "Qatar"]},
   {"kind": "big", "gh": "Standings after Vegas", "min": 5,
    "say": "Verstappen has three hundred four. Hamilton is thirty-seven back, Russell and Norris forty.",
    "hl": ["thirty-seven", "forty"]},
   {"kind": "big", "big": "25", "chip": "Qatar 25 · Abu Dhabi 25",
    "say": "No sprints left, no fastest lap point. Twenty-five per race, tops.",
    "hl": ["Twenty-five"]},
   {"kind": "big", "chip": "Leclerc −54 · out of reach",
    "say": "Leclerc is fifty-four back and out of reach. It's a three-way fight.",
    "hl": ["three-way"]},
   {"kind": "big", "big": "TOP 3", "chip": "Verstappen on the podium → P2",
    "say": "With a podium in Qatar, second is his whatever the others do.",
    "hl": ["podium"]},
   {"kind": "big", "big": "P4", "chip": "P4 · unless Hamilton wins",
    "say": "Fourth place is enough, as long as Hamilton doesn't win the race.",
    "hl": ["Hamilton"]},
   {"kind": "big", "big": "0", "chip": "0 points · none of the three on the podium",
    "say": "Even zero points is enough, if none of the three reaches the podium.",
    "hl": ["zero", "points"]},
   {"kind": "big",
    "say": "If points are tied, more wins decide it. Verstappen has four.",
    "hl": ["wins", "four"]},
   {"kind": "end", "tag": "Qatar · November 27–29",
    "say": "Check the race start in your own time zone on LapRadar.",
    "hl": ["your", "own", "time", "zone"]}
  ]
 }
}

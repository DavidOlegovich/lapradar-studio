# Финал F2 2026: Камара (207) против Цолова (200) перед Катаром и Абу-Даби. Очки за уикенд, вопрос «F1 или F2» у Камары, расклады.
# HQ-режим, Лусаил ночью. Машина 0 синяя (Камара), машина 1 красная (Цолов): свои схемы без ливрей команд (VIDEO.hq.cars).
# В follow машина 0 впереди, в duel машина 1 обходит машину 0. Камера (shots) общая для всех языков.
_BLUE = ["#1d4ed8", "#f8fafc", "stripe"]
_RED = ["#dc2626", "#f8fafc", "band"]
_CV = {"type": "convoy", "at": 0.02, "v": 30, "n": 2}

VIDEO = {
 "slug": "f2-title-qatar-2026",
 "track": "lusail",
 "theme": "night",
 "hq": {"cars": [_BLUE, _RED], "lampFade": True},
 "shots": [
  {"type": "chase", "car": 1, "dist": 13, "dist2": 12, "h": 5.5, "h2": 5, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "act": {"type": "follow", "at": 0.01}},
  {"type": "stage", "items": [{"o": "f1", "c": _BLUE[0], "a": _BLUE[1], "p": _BLUE[2], "x": -2.3, "ry": 0.25}, {"o": "f1", "c": _RED[0], "a": _RED[1], "p": _RED[2], "x": 2.3, "ry": -0.25}],
   "bg": "blue", "r": 14, "r2": 12, "h": 3.2, "h2": 4, "a0": -0.35, "a1": 0.3, "spin": 0.08, "ly": 0.6,
   "hud": {"type": "bars", "rows": [{"label": "CAM", "v": 207, "c": "#3b82f6"}, {"label": "TSO", "v": 200, "c": "#ef4444"}, {"label": "DUN", "v": 189, "c": "#9fb4ff"}], "min": 120, "max": 215, "hi": 0}},
  {"type": "carorbit", "car": 0, "r": 10.5, "r2": 9.5, "h": 1.5, "h2": 2.0, "a0": 0.5, "a1": 1.15, "fov": 46, "ly": 0.8, "act": {**_CV, "at": 0.03, "v": 22, "n": 1}},
  {"type": "side", "car": 0, "side": 8.5, "side2": 7.8, "h": 1.2, "h2": 1.4, "fw": 2.0, "fw2": -3.5, "look": 0.5, "ly": 0.9, "fov": 54, "act": {**_CV, "at": 0.85}},
  {"type": "chase", "car": 1, "dist": 14, "dist2": 12.5, "h": 6, "h2": 5.5, "side": 1.5, "side2": -1.5, "look": 22, "drop": 3, "noCut": True, "act": {"type": "follow", "at": 0.26}},
  {"type": "stage", "items": [{"o": "f1", "c": _BLUE[0], "a": _BLUE[1], "p": _BLUE[2]}], "bg": "blue", "beams": True, "r": 10.5, "r2": 9.5, "h": 2.4, "h2": 3.0, "a0": -0.6, "a1": 0.4, "spin": 0.15, "ly": 0.8},
  {"type": "chase", "car": 0, "dist": 15, "dist2": 13, "h": 6, "h2": 5.5, "side": -3.5, "side2": -1, "look": 28, "drop": 3, "noCut": True, "act": {"type": "duel"}},
  {"type": "orbit", "at": 0.05, "r": 330, "r2": 300, "h": 90, "h2": 70, "a0": 0.4, "a1": 0.8, "fov": 50, "act": {**_CV, "at": 0.04, "v": 45}},
  {"type": "orbit", "at": 0.06, "r": 420, "r2": 400, "h": 140, "h2": 120, "a0": 0.9, "a1": 1.1, "fov": 50, "act": {**_CV, "at": 0.05, "v": 45}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 11, "h": 1.5, "a0": 1.9, "a1": 1.9, "fov": 44, "act": {**_CV, "at": 0.05, "v": 1}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 7.5, "h": 1.2, "a0": 2.1, "a1": 2.1, "fov": 40, "ly": 0.6, "act": {**_CV, "at": 0.05, "v": 1}}},
  {"name": "duel", "w": 1200, "h": 800, "t": 3.2, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 10, "h": 3.8, "side": -2.4, "look": 12, "drop": 2, "fov": 42, "act": {"type": "duel"}}},
  {"name": "onboard", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "onboard", "car": 1, "fov": 60, "act": {**_CV, "at": 0.03, "v": 30}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "big": "7", "head": "Финал F2", "sub": "Камара против Цолова", "chip": "Камара 207 · Цолов 200",
    "say": "Семь очков между лидерами Формулы два, а лидер может даже не выйти на старт в Катаре.",
    "hl": ["Семь", "очков"]},
   {"kind": "big", "big": "207", "chip": "Таблица F2 после Баку",
    "say": "У Камары двести семь, у Цолова двести. Третий Данн отстаёт от лидера на восемнадцать.",
    "hl": ["двести", "семь"]},
   {"kind": "big", "big": "39", "chip": "Спринт 10 · гонка 25 · поул 2 · БК 1+1",
    "say": "За уикенд можно взять тридцать девять: спринт десять, основная гонка двадцать пять, поул и быстрые круги.",
    "hl": ["тридцать", "девять"]},
   {"kind": "big", "big": "78", "chip": "Катар + Абу-Даби · до 78 очков",
    "say": "Два этапа, значит на кону до семидесяти восьми очков.",
    "hl": ["семидесяти", "восьми"]},
   {"kind": "big", "big": "F1?", "chip": "Камара · Haas · F1 или F2?",
    "say": "Но Камара уже выступает за Haas в Формуле один, а ехать в двух сериях в один уикенд нельзя.",
    "hl": ["Haas"]},
   {"kind": "big", "big": "?", "chip": "Решение после Вегаса",
    "say": "Haas решит после Вегаса, кто едет в Катаре и Абу-Даби: Камара или Хиракава.",
    "hl": ["Вегаса"]},
   {"kind": "big", "big": "8", "chip": "Без Камары Цолову хватит 8 очков",
    "say": "Если Камара пропустит Катар, Цолову хватит восьми очков, чтобы выйти вперёд.",
    "hl": ["восьми"]},
   {"kind": "big", "big": "28.11", "chip": "Лусаил 28–29.11 · Абу-Даби 5–6.12",
    "say": "Весной F2 потеряла Бахрейн и Джидду, но Катар и Абу-Даби в силе. Гонки двадцать восьмого и двадцать девятого.",
    "hl": ["Катар"]},
   {"kind": "end", "tag": "F2 · финал сезона",
    "say": "Таблицу Формулы два после каждой гонки смотрите на ЛапРадар."}
  ],
  "en": [
   {"kind": "big", "big": "7", "head": "F2 title decider", "sub": "Câmara vs Tsolov", "chip": "Câmara 207 · Tsolov 200",
    "say": "Seven points split the Formula Two leaders, and the leader might not even start in Qatar.",
    "hl": ["Seven", "points"]},
   {"kind": "big", "big": "207", "chip": "F2 standings after Baku",
    "say": "Câmara has two hundred and seven, Tsolov two hundred. Dunne is third, eighteen behind the leader.",
    "hl": ["seven"]},
   {"kind": "big", "big": "39", "chip": "Sprint 10 · feature 25 · pole 2 · FL 1+1",
    "say": "A weekend is worth up to thirty-nine: ten in the sprint, twenty-five in the feature, plus pole and fastest laps.",
    "hl": ["thirty-nine"]},
   {"kind": "big", "big": "78", "chip": "Qatar + Abu Dhabi · up to 78",
    "say": "Two rounds left, so up to seventy-eight points are on the table.",
    "hl": ["seventy-eight"]},
   {"kind": "big", "big": "F1?", "chip": "Câmara · Haas · F1 or F2?",
    "say": "But Câmara is already racing for Haas in Formula One, and you can't do both series on one weekend.",
    "hl": ["Haas"]},
   {"kind": "big", "big": "?", "chip": "Decision after Vegas",
    "say": "Haas will decide after Vegas who races in Qatar and Abu Dhabi: Câmara or Hirakawa.",
    "hl": ["Vegas"]},
   {"kind": "big", "big": "8", "chip": "Without Câmara, Tsolov needs 8",
    "say": "If Câmara skips Qatar, eight points are enough for Tsolov to take the lead.",
    "hl": ["eight"]},
   {"kind": "big", "big": "28.11", "chip": "Lusail Nov 28–29 · Abu Dhabi Dec 5–6",
    "say": "F2 lost Bahrain and Jeddah in spring, but Qatar and Abu Dhabi are on. Racing on November twenty-eighth and twenty-ninth.",
    "hl": ["Qatar"]},
   {"kind": "end", "tag": "F2 · season finale",
    "say": "Check the Formula Two standings after every race on LapRadar."}
  ]
 }
}

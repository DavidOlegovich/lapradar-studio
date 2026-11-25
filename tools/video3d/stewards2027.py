# Штатные стюарды F1 с 2027: ФИА объявила 19.11.2026 (уикенд Лас-Вегаса). Небольшая первая группа в 2027, расширение 2028+, цель отдел 12-15;
# нынешние стюарды и стюард-бывший пилот остаются; цели: единообразие и преемственность; между этапами тренды и уточнение регламента;
# обучение будущих судей (High Performance Programme); позже поддержка других одноместных серий ФИА.
# Удалённый центр ФИА в Биггин-Хилле: работает с лета, официально открыт в октябре 2026, решения остаются за стюардами.
# Нейтрально, без оценок. Цитат нет. Источники: tools/topics.md («Источники 26.11: штатные стюарды»).
# HQ-режим, Сильверстоун днём (широкая открытая трасса). Машины условные, без ливрей. Время по городам не называем.
_WHT = ["#e5e7eb", "#dc2626", "stripe"]
_BLU = ["#1d4ed8", "#facc15", "band"]
_GRN = ["#15803d", "#f8fafc", "split"]
_CV = {"type": "convoy", "at": 0.2, "v": 30, "n": 3}
_TWO = [{"o": "f1", "c": _WHT[0], "a": _WHT[1], "p": _WHT[2], "x": -2.3, "ry": 0.25},
        {"o": "f1", "c": _BLU[0], "a": _BLU[1], "p": _BLU[2], "x": 2.3, "ry": -0.25}]

VIDEO = {
 "slug": "f1-full-time-stewards-2027",
 "track": "silverstone",
 "theme": "day",
 "hq": {"cars": [_WHT, _BLU, _GRN], "lampFade": True},
 "coverText": {"ru": {"head": "ШТАТНЫЕ СТЮАРДЫ", "sub": "в F1 с 2027 года"},
               "en": {"head": "FULL-TIME STEWARDS", "sub": "in F1 from 2027"}},
 "shots": [
  # 1 крючок: колесо в колесо
  {"type": "chase", "car": 0, "dist": 14, "dist2": 12, "h": 5.5, "h2": 5, "side": -2.5, "side2": -1.5, "look": 22, "drop": 3, "noCut": True, "act": {"type": "duel"}},
  # 2 сейчас: ротация добровольцев
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 5.5, "h2": 5, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 60, "n": 3}},
  # 3 объявление 19.11
  {"type": "carorbit", "car": 0, "r": 10, "r2": 9, "h": 1.4, "h2": 1.9, "a0": 0.5, "a1": 1.1, "fov": 46, "ly": 0.8, "act": {**_CV, "at": 0.25, "v": 22, "n": 1}},
  # 4 небольшая первая группа 2027
  {"type": "side", "car": 0, "side": 8.4, "side2": 7.8, "h": 1.1, "h2": 1.3, "fw": 2.5, "fw2": -2.5, "look": 0.5, "ly": 0.9, "fov": 54, "act": {**_CV, "at": 0.3, "v": 28}},
  # 5 цель 12-15
  {"type": "chase", "car": 0, "dist": 27, "dist2": 25, "h": 11, "h2": 10, "side": 0, "side2": 0, "look": 30, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 60, "n": 3}},
  # 6 остаются нынешние стюарды и стюард-пилот
  {"type": "stage", "items": _TWO, "bg": "blue", "r": 12.5, "r2": 11, "h": 2.8, "h2": 3.4, "a0": 0.3, "a1": -0.3, "spin": 0.04, "ly": 0.6},
  # 7 между этапами
  {"type": "carorbit", "car": 1, "r": 10.5, "r2": 9.5, "h": 1.5, "h2": 2.0, "a0": -0.5, "a1": 0.2, "fov": 48, "ly": 0.8, "act": {**_CV, "at": 0.4, "v": 22, "n": 2}},
  # 8 обучение и другие серии
  {"type": "chase", "car": 0, "dist": 10.5, "dist2": 10, "h": 4, "h2": 4, "side": -2.4, "side2": -1.5, "look": 14, "drop": 3, "noCut": True, "act": {"type": "duel"}},
  # 9 Биггин-Хилл
  {"type": "chase", "car": 0, "dist": 29, "dist2": 27, "h": 12, "h2": 11, "side": 2, "side2": 1, "look": 30, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 60, "n": 3}},
  # 10 конец
  {"type": "chase", "car": 0, "dist": 26, "dist2": 28, "h": 10, "h2": 11, "side": -2, "side2": 0, "look": 30, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 55, "n": 3}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 9.5, "h": 1.4, "a0": 1.85, "a1": 1.85, "fov": 44, "act": {**_CV, "at": 0.25, "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 7.5, "h": 1.2, "a0": 2.1, "a1": 2.1, "fov": 40, "ly": 0.6, "act": {**_CV, "at": 0.25, "v": 1, "n": 2}}},
  {"name": "duel", "w": 1200, "h": 800, "t": 3.2, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 10, "h": 3.8, "side": -2.4, "look": 12, "drop": 2, "fov": 42, "act": {"type": "duel"}}},
  {"name": "pack", "w": 1200, "h": 800, "t": 1.8, "u": 0.4,
   "shot": {"type": "chase", "car": 0, "dist": 28, "h": 12, "side": 0, "look": 30, "drop": 3, "fov": 44, "act": {"type": "convoy", "at": "straight", "v": 60, "n": 3}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "chip": "С 2027 · штатные стюарды",
    "say": "Похожие эпизоды, а штрафы разные? С двадцать седьмого года в Формуле один появятся стюарды на постоянной ставке.",
    "hl": ["разные", "постоянной", "ставке"]},
   {"kind": "big", "chip": "Сейчас: стюарды по очереди",
    "say": "Сейчас стюарды приезжают на этапы по ротации и работают в основном как добровольцы.",
    "hl": ["ротации", "добровольцы"]},
   {"kind": "big", "chip": "ФИА · 19 ноября · Лас-Вегас",
    "say": "ФИА объявила об этом девятнадцатого ноября, в уикенд Гран-при Лас-Вегаса.",
    "hl": ["ФИА", "девятнадцатого"]},
   {"kind": "big", "chip": "2027: небольшая группа · 2028+: больше",
    "say": "В двадцать седьмом наберут небольшую первую группу, а с двадцать восьмого программу расширят.",
    "hl": ["небольшую", "расширят"]},
   {"kind": "big", "big": "15", "chip": "Цель: отдел из 12–15 стюардов",
    "say": "Цель на будущее: отдел от двенадцати до пятнадцати штатных стюардов.",
    "hl": ["двенадцати", "пятнадцати"]},
   {"kind": "big", "chip": "Остаются: нынешние стюарды и стюард-пилот",
    "say": "Нынешние стюарды останутся. Бывший гонщик в составе на каждом этапе тоже.",
    "hl": ["останутся", "гонщик"]},
   {"kind": "big", "chip": "Между этапами: тренды и регламент",
    "say": "Между гонками штатные стюарды будут искать тенденции и места, где регламент нужно уточнить.",
    "hl": ["тенденции", "регламент"]},
   {"kind": "big", "chip": "Обучение судей · другие серии ФИА",
    "say": "Ещё они будут учить будущих судей и со временем смогут помогать другим сериям ФИА.",
    "hl": ["учить", "судей"]},
   {"kind": "big", "chip": "Центр ФИА в Биггин-Хилле · октябрь",
    "say": "В октябре ФИА открыла удалённый центр в Биггин-Хилле. Решения по-прежнему принимают стюарды.",
    "hl": ["Биггин-Хилле", "стюарды"]},
   {"kind": "end", "tag": "Штатные стюарды F1 · коротко",
    "say": "Сообщения race control и гонки вживую смотрите на карте ЛапРадар."}
  ],
  "en": [
   {"kind": "big", "chip": "From 2027 · full-time stewards",
    "say": "Similar incidents, different penalties? From twenty twenty-seven, Formula One gets full-time stewards.",
    "hl": ["different", "full-time", "stewards"]},
   {"kind": "big", "chip": "Today: stewards in rotation",
    "say": "Today stewards rotate through the races and work mostly as volunteers.",
    "hl": ["rotate", "volunteers"]},
   {"kind": "big", "chip": "FIA · 19 November · Las Vegas",
    "say": "The FIA announced it on the nineteenth of November, during Las Vegas Grand Prix weekend.",
    "hl": ["FIA", "nineteenth"]},
   {"kind": "big", "chip": "2027: small group · 2028+: more",
    "say": "A small first group is recruited in twenty twenty-seven, and the programme grows from twenty twenty-eight.",
    "hl": ["small", "grows"]},
   {"kind": "big", "big": "15", "chip": "Goal: a department of 12–15",
    "say": "The long-term goal is a department of twelve to fifteen full-time stewards.",
    "hl": ["twelve", "fifteen"]},
   {"kind": "big", "chip": "Staying: current stewards and the driver steward",
    "say": "Current stewards stay. So does the former racing driver on each panel.",
    "hl": ["stay", "driver"]},
   {"kind": "big", "chip": "Between races: trends and rules",
    "say": "Between races, the full-time stewards will spot trends and rules that need clarifying.",
    "hl": ["trends", "clarifying"]},
   {"kind": "big", "chip": "Training officials · other FIA series",
    "say": "They will also train future officials and may later support other FIA series.",
    "hl": ["train", "officials"]},
   {"kind": "big", "chip": "FIA centre at Biggin Hill · October",
    "say": "In October the FIA opened a remote centre at Biggin Hill. The stewards still make the decisions.",
    "hl": ["Biggin", "Hill"]},
   {"kind": "end", "tag": "Full-time F1 stewards · in short",
    "say": "Follow race control messages and live races on the LapRadar map."}
  ]
 }
}

# Боттас остаётся в Cadillac на 2027 (объявлено 18.11.2026 перед домашним этапом команды). HQ-режим, трасса Остин (COTA, домашний этап Cadillac в США) в вечернем свете (theme dusk, hq.street).
# Машина Боттаса: условная чёрная с серебром (shot "paint"), без логотипов и настоящей ливреи Cadillac. Цифры: Перес впереди в гонках 14:4 (Sky Sports, roundtable),
# 9 сходов, больше только у Стролла с 13 (formula1.com). Камера (shots) общая для всех языков.
_BLK = {"c": "#15171c", "a": "#c3c8d0", "p": "stripe"}          # условная чёрно-серебряная окраска
_PAINT = {"0": _BLK, "1": _BLK}
_CV = {"type": "convoy", "at": "straight", "n": 2, "v": 60}

VIDEO = {
 "slug": "bottas-cadillac-2027",
 "track": "austin",
 "theme": "dusk",
 "hq": {"street": True},
 "shots": [
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10.5, "h": 4.2, "h2": 3.6, "side": 0, "side2": 1.2, "look": 20, "drop": 3, "noCut": True, "paint": _PAINT, "act": {**_CV, "n": 1}},
  {"type": "stage", "items": [{"o": "f1", "c": _BLK["c"], "a": _BLK["a"], "p": _BLK["p"], "x": -1.6, "ry": 0.35}, {"o": "trophy", "x": 2.4, "y": 0, "s": 0.55}], "bg": "gold", "r": 12, "r2": 10.5, "h": 3, "h2": 3.6, "a0": -0.4, "a1": 0.3, "spin": 0, "ly": 1.0},
  {"type": "side", "car": 0, "side": 6.5, "side2": 6, "h": 1.0, "h2": 1.3, "fw": 2.5, "fw2": -1.5, "look": 0.5, "ly": 0.9, "fov": 52, "paint": _PAINT, "act": {**_CV, "v": 40}},
  {"type": "stage", "items": [{"o": "f1", "c": _BLK["c"], "a": _BLK["a"], "p": _BLK["p"], "x": -2.3, "ry": 0.25}, {"o": "f1", "c": _BLK["c"], "a": _BLK["a"], "p": _BLK["p"], "x": 2.3, "ry": -0.25}], "bg": "blue", "beams": True, "r": 13, "r2": 11, "h": 3, "h2": 4, "a0": -0.4, "a1": 0.3, "spin": 0.1, "ly": 0.6},
  {"type": "chase", "car": 0, "dist": 11, "dist2": 9.5, "h": 4.2, "h2": 3.6, "side": -1.2, "side2": 1.2, "look": 20, "drop": 3, "noCut": True, "paint": _PAINT,
   "hud": {"type": "bars", "rows": [{"label": "PER", "v": 14, "c": "#c3c8d0"}, {"label": "BOT", "v": 4, "c": "#5b9bff"}], "min": 0, "max": 15, "hi": 1}, "act": {**_CV, "n": 1, "t0": 3}},
  {"type": "carorbit", "car": 0, "r": 11, "r2": 10, "h": 1.6, "h2": 2.2, "a0": 0.7, "a1": 1.3, "fov": 48, "ly": 0.9, "paint": _PAINT,
   "hud": {"type": "bars", "rows": [{"label": "STR", "v": 13, "c": "#22c55e"}, {"label": "BOT", "v": 9, "c": "#c3c8d0"}], "min": 0, "max": 14, "hi": 1}, "act": {**_CV, "v": 26, "n": 1}},
  {"type": "onboard", "car": 0, "fov": 70, "eh": 1.3, "ez": 0.05, "ty": 1.6, "paint": _PAINT, "act": {**_CV, "v": 50}},
  {"type": "carorbit", "car": 0, "r": 10.5, "r2": 9.5, "h": 2.4, "h2": 1.7, "a0": -1.0, "a1": -0.35, "fov": 48, "ly": 0.8, "paint": _PAINT, "act": {**_CV, "v": 24, "n": 1, "t0": 2}},
  {"type": "fly", "from": 0.02, "to": 0.08, "h": 70, "h2": 150, "side": 40, "ahead": 260}
 ],
 "coverShot": {"type": "chase", "car": 0, "dist": 11, "h": 3.4, "side": 0, "look": 20, "drop": 2, "fov": 46, "paint": _PAINT, "act": {**_CV, "v": 8}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 8.5, "h": 1.8, "a0": 2.4, "a1": 2.4, "fov": 42, "ly": 0.6, "paint": _PAINT, "act": {**_CV, "n": 1, "v": 1}}},
  {"name": "duo", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "f1", "c": _BLK["c"], "a": _BLK["a"], "p": _BLK["p"], "x": -2.3, "ry": 0.25}, {"o": "f1", "c": _BLK["c"], "a": _BLK["a"], "p": _BLK["p"], "x": 2.3, "ry": -0.25}], "bg": "blue", "beams": True, "r": 12, "h": 3.2, "a0": 0.1, "spin": 0, "ly": 0.6}},
  {"name": "side", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "side", "car": 0, "side": 6, "h": 1.1, "fw": 0.5, "look": 0.5, "ly": 0.9, "fov": 46, "paint": _PAINT, "act": {**_CV, "v": 40}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "БОТТАС ОСТАЁТСЯ", "chip": "Боттас · Cadillac · 2027",
    "say": "«Всем, кого это касается: я остаюсь!» Так Валттери Боттас объявил, что едет за Cadillac и в следующем году.",
    "hl": ["остаюсь"]},
   {"kind": "big", "big": "2019", "chip": "Мельбурн 2019 → 2027",
    "say": "Это отсылка к его радио после победы в Австралии в девятнадцатом. Тогда концовка была куда грубее.",
    "hl": ["Австралии"]},
   {"kind": "big", "big": "+1", "chip": "Опция · второй год",
    "say": "В его контракте была опция на второй сезон, и команда её использовала.",
    "hl": ["опция"]},
   {"kind": "big", "big": "2029", "chip": "Перес · до 2029",
    "say": "Напарник прежний: Серхио Перес в октябре продлил контракт до двадцать девятого года.",
    "hl": ["девятого"]},
   {"kind": "big", "big": "14:4", "chip": "Гонки: Перес 14, Боттас 4",
    "say": "Внутри команды счёт не в его пользу: в гонках Перес был впереди четырнадцать раз, Боттас четыре.",
    "hl": ["четырнадцать"]},
   {"kind": "big", "big": "9", "chip": "9 сходов · у Стролла 13",
    "say": "Девять сходов за сезон, больше только у Стролла. Новичков часто подводили тормоза.",
    "hl": ["Девять", "тормоза"]},
   {"kind": "big", "big": "0", "chip": "0 очков · лучший P13",
    "say": "Очков у Cadillac пока нет. Лучший финиш: тринадцатый Боттас в Китае.",
    "hl": ["тринадцатый"]},
   {"kind": "big", "big": "40", "chip": "Херта · суперлицензия",
    "say": "Колтон Херта набрал очки на суперлицензию в тренировках, но гоночного места пока не получит.",
    "hl": ["суперлицензию"]},
   {"kind": "end", "tag": "Боттас и Перес · 2027",
    "say": "Гонки Боттаса и Переса смотрите на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "BOTTAS STAYS", "chip": "Bottas · Cadillac · 2027",
    "say": "\"To whom it may concern, I'm staying!\" That's how Valtteri Bottas confirmed another year at Cadillac.",
    "hl": ["staying"]},
   {"kind": "big", "big": "2019", "chip": "Melbourne 2019 → 2027",
    "say": "A nod to his radio call after winning in Australia in twenty nineteen. That one had a much ruder ending.",
    "hl": ["Australia"]},
   {"kind": "big", "big": "+1", "chip": "Option · year two",
    "say": "His deal had an option for a second season, and the team has taken it.",
    "hl": ["option"]},
   {"kind": "big", "big": "2029", "chip": "Perez · to 2029",
    "say": "Same team-mate too: Sergio Perez extended in October, through twenty twenty-nine.",
    "hl": ["twenty-nine"]},
   {"kind": "big", "big": "14:4", "chip": "Races: Perez 14, Bottas 4",
    "say": "The team-mate fight hasn't gone his way: Perez finished ahead fourteen times, Bottas four.",
    "hl": ["fourteen"]},
   {"kind": "big", "big": "9", "chip": "9 DNFs · Stroll 13",
    "say": "Nine retirements this year, only Stroll has more. Brakes kept failing the new team.",
    "hl": ["Nine", "Brakes"]},
   {"kind": "big", "big": "0", "chip": "0 points · best P13",
    "say": "Cadillac is still on zero points. Best finish: Bottas, thirteenth in China.",
    "hl": ["thirteenth"]},
   {"kind": "big", "big": "40", "chip": "Herta · superlicence",
    "say": "Colton Herta earned superlicence points in practice, but there's no race seat for him yet.",
    "hl": ["superlicence"]},
   {"kind": "end", "tag": "Bottas and Perez · 2027",
    "say": "Follow Bottas and Perez on the LapRadar live map."}
  ]
 }
}

# История Лусаила и Гран-при Катара + 2026: лимит 27 кругов, минимум два пит-стопа, F2 в тот же уикенд (Камара остаётся в Haas).
# Источники фактов: tools/topics.md («Источники 24.11: история Лусаила»).
# HQ-режим, Лусаил ночью. Машины: условные цвета без ливрей (VIDEO.hq.cars). Время старта не называем.
_BLUE = ["#1d4ed8", "#f8fafc", "stripe"]
_RED = ["#dc2626", "#f8fafc", "band"]
_TEAL = ["#0f766e", "#e5e7eb", "split"]
_CV = {"type": "convoy", "at": 0.02, "v": 30, "n": 3}

VIDEO = {
 "slug": "lusail-history-qatar-gp-2026",
 "track": "lusail",
 "theme": "night",
 "hq": {"cars": [_BLUE, _RED, _TEAL], "lampFade": True},
 "shots": [
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 5.5, "h2": 5, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 62, "n": 3}},
  {"type": "orbit", "at": 0.02, "r": 430, "r2": 410, "h": 130, "h2": 120, "a0": 1.2, "a1": 1.3, "fov": 50, "act": {**_CV, "at": 0.0, "v": 45}},
  {"type": "chase", "car": 0, "dist": 26, "dist2": 22, "h": 11, "h2": 9, "side": 0, "side2": 0, "look": 20, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 55, "n": 3}},
  {"type": "side", "car": 0, "side": 8.4, "side2": 7.8, "h": 1.1, "h2": 1.3, "fw": 2.5, "fw2": -2.5, "look": 0.5, "ly": 0.9, "fov": 54, "act": {**_CV, "at": 0.62, "v": 28}},
  {"type": "carorbit", "car": 0, "r": 9.5, "r2": 8.5, "h": 1.3, "h2": 1.7, "a0": 0.4, "a1": 1.05, "fov": 46, "ly": 0.7, "act": {"type": "heat", "at": 0.7}},
  {"type": "onboard", "car": 0, "fov": 66, "eh": 1.3, "ez": 0.05, "ty": 1.6, "act": {**_CV, "at": 0.5, "v": 34}},
  {"type": "tyre", "hi": 0, "wear": True, "hud": {"type": "laps", "n": 27}},
  {"type": "stage", "items": [{"o": "f1", "c": _BLUE[0], "a": _BLUE[1], "p": _BLUE[2], "x": -2.3, "ry": 0.25}, {"o": "f1", "c": _RED[0], "a": _RED[1], "p": _RED[2], "x": 2.3, "ry": -0.25}],
   "bg": "blue", "r": 14, "r2": 12, "h": 3.2, "h2": 4, "a0": -0.35, "a1": 0.3, "spin": 0.08, "ly": 0.6,
   "hud": {"type": "bars", "rows": [{"label": "CAM", "v": 207, "c": "#3b82f6"}, {"label": "TSO", "v": 200, "c": "#ef4444"}, {"label": "DUN", "v": 189, "c": "#9fb4ff"}], "min": 120, "max": 215, "hi": 1}},
  {"type": "orbit", "at": 0.05, "r": 330, "r2": 300, "h": 90, "h2": 70, "a0": 0.4, "a1": 0.8, "fov": 50, "act": {**_CV, "at": 0.04, "v": 45}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 9.5, "h": 1.4, "a0": 1.85, "a1": 1.85, "fov": 44, "act": {**_CV, "at": 0.02, "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 7.5, "h": 1.2, "a0": 2.6, "a1": 2.6, "fov": 40, "ly": 0.6, "act": {**_CV, "at": 0.04, "v": 1, "n": 2}}},
  {"name": "night", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 28, "h": 12, "side": 0, "look": 20, "drop": 3, "fov": 46, "act": {"type": "convoy", "at": "straight", "v": 55, "n": 3}}},
  {"name": "pair", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 11, "h": 4.2, "side": 2.2, "look": 14, "drop": 2, "fov": 44, "act": {"type": "follow", "at": 0.3}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "head": "Лусаил", "sub": "трасса для мотоциклов", "chip": "Построена для мотоциклов",
    "say": "Для кого построили трассу в Катаре? Не для Формулы один, а для мотоциклов.",
    "hl": ["мотоциклов"]},
   {"kind": "big", "chip": "2004 MotoGP · 2008 ночью",
    "say": "MotoGP приехала сюда в две тысячи четвёртом, а в две тысячи восьмом провела первую ночную гонку.",
    "hl": ["ночью"]},
   {"kind": "big", "chip": "2021 · Хэмилтон · 2022 пропуск",
    "say": "В двадцать первом дебют Формулы один, выиграл Хэмилтон. В двадцать втором гонки не было из-за чемпионата мира по футболу.",
    "hl": ["Хэмилтон", "футболу"]},
   {"kind": "big", "chip": "С 2023 · контракт до 2032",
    "say": "В двадцать третьем гонка вернулась по десятилетнему контракту, до две тысячи тридцать второго.",
    "hl": ["тридцать", "второго"]},
   {"kind": "big", "chip": "2023 · жара · Сарджент и Окон",
    "say": "Жара двадцать третьего: Сарджент сошёл, Окона стошнило в кокпите, а лимит шин был восемнадцать кругов.",
    "hl": ["жара", "восемнадцать"]},
   {"kind": "big", "chip": "2023, 2024, 2025 · Ферстаппен",
    "say": "Все три гонки с возвращения выиграл Ферстаппен.",
    "hl": ["Ферстаппен"]},
   {"kind": "tyre", "head": "27", "laps": 27, "chip": "2026 · 27 кругов · 57 в гонке",
    "say": "Сейчас лимит двадцать семь кругов на комплект, гонка пятьдесят семь. Значит, минимум два пит-стопа.",
    "hl": ["минимум", "два"]},
   {"kind": "big", "big": "F2", "chip": "F2 · Камара 207 · Цолов 200",
    "say": "В этот уикенд тут и Формула два. Лидер Камара едет за Haas, Цолов отстаёт на семь очков.",
    "hl": ["Камара", "Haas"]},
   {"kind": "end", "tag": "Лусаил · 27–29 ноября",
    "say": "Во сколько гонка по вашему времени, смотрите на ЛапРадар.",
    "hl": ["вашему", "времени"]}
  ],
  "en": [
   {"kind": "big", "head": "Lusail", "sub": "a track built for bikes", "chip": "Built for motorcycles",
    "say": "Who was the Qatar circuit built for? Not Formula One. Motorbikes.",
    "hl": ["motorbikes"]},
   {"kind": "big", "chip": "2004 MotoGP · 2008 at night",
    "say": "MotoGP arrived in two thousand four, and held its first night race in two thousand eight.",
    "hl": ["night"]},
   {"kind": "big", "chip": "2021 · Hamilton · 2022 skipped",
    "say": "F1 debuted in twenty twenty-one, Hamilton won. No race in twenty twenty-two because of the football World Cup.",
    "hl": ["Hamilton", "World", "Cup"]},
   {"kind": "big", "chip": "From 2023 · contract to 2032",
    "say": "It returned in twenty twenty-three on a ten-year deal, through twenty thirty-two.",
    "hl": ["ten-year"]},
   {"kind": "big", "chip": "2023 · heat · Sargeant and Ocon",
    "say": "Twenty twenty-three was brutal: Sargeant retired, Ocon was sick in his cockpit, tyres capped at eighteen laps.",
    "hl": ["brutal", "eighteen"]},
   {"kind": "big", "chip": "2023, 2024, 2025 · Verstappen",
    "say": "Verstappen has won all three races since the return.",
    "hl": ["Verstappen"]},
   {"kind": "tyre", "head": "27", "laps": 27, "chip": "2026 · 27 laps · 57-lap race",
    "say": "Now it's twenty-seven laps per set in a fifty-seven-lap race. So at least two pit stops.",
    "hl": ["two", "stops"]},
   {"kind": "big", "big": "F2", "chip": "F2 · Câmara 207 · Tsolov 200",
    "say": "Formula Two races here too. Leader Câmara drives for Haas, Tsolov is seven points back.",
    "hl": ["Haas", "seven"]},
   {"kind": "end", "tag": "Lusail · November 27–29",
    "say": "Check the race start in your own time zone on LapRadar.",
    "hl": ["your", "own", "time", "zone"]}
  ]
 }
}

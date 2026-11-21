# Катар-2026: Pirelli ограничила комплект шин 27 кругами (объявлено 20.11.2026), 57 кругов гонки → минимум два пит-стопа.
# История лимита: 2023: 18 кругов (поребрики, боковины), 2024: без лимита, 2025: 25 кругов. Жара 2023: Сарджент сошёл, Окона стошнило.
# HQ-режим, Лусаил ночью, фонари с плавным светом (hq.lampFade). Машины: условные цвета без ливрей (VIDEO.hq.cars).
# Время старта не называем: «по вашему времени: на LapRadar». Камера (shots) общая для всех языков.
_BLUE = ["#1e40af", "#f8fafc", "stripe"]
_ORG = ["#f97316", "#111827", "band"]
_TEAL = ["#0f766e", "#e5e7eb", "split"]
_CV = {"type": "convoy", "at": 0.02, "v": 30, "n": 3}

VIDEO = {
 "slug": "qatar-gp-2026-tyre-limit",
 "track": "lusail",
 "theme": "night",
 "hq": {"cars": [_BLUE, _ORG, _TEAL], "lampFade": True},
 "shots": [
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 5.5, "h2": 5, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 62, "n": 3}},
  {"type": "tyre", "hi": 0, "wear": True, "hud": {"type": "laps", "n": 27}},
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10, "h": 4.5, "h2": 4, "side": -2.5, "side2": -1.5, "look": 14, "drop": 3, "noCut": True, "act": {"type": "pit", "car": 0, "box": 0.45}},
  {"type": "fly", "from": 0.68, "to": 0.78, "h": 70, "h2": 120, "side": -45, "ahead": 200},
  {"type": "carorbit", "car": 0, "r": 9.5, "r2": 8.5, "h": 1.3, "h2": 1.7, "a0": 0.4, "a1": 1.05, "fov": 46, "ly": 0.7, "act": {"type": "heat", "at": 0.7}},
  {"type": "side", "car": 0, "side": 8.4, "side2": 7.8, "h": 1.1, "h2": 1.3, "fw": 2.5, "fw2": -2.5, "look": 0.5, "ly": 0.9, "fov": 54, "act": {**_CV, "at": 0.62, "v": 28}},
  {"type": "onboard", "car": 0, "fov": 66, "eh": 1.3, "ez": 0.05, "ty": 1.6, "act": {**_CV, "at": 0.5, "v": 34}},
  {"type": "chase", "car": 0, "dist": 14, "dist2": 12.5, "h": 6, "h2": 5.5, "side": 1.5, "side2": -1.5, "look": 22, "drop": 3, "noCut": True, "act": {"type": "restart", "at": 0.93}},
  {"type": "orbit", "at": 0.02, "r": 430, "r2": 410, "h": 130, "h2": 120, "a0": 1.2, "a1": 1.3, "fov": 50, "act": {**_CV, "at": 0.0, "v": 45}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 9.5, "h": 1.4, "a0": 1.85, "a1": 1.85, "fov": 44, "act": {**_CV, "at": 0.02, "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 7.5, "h": 1.2, "a0": 2.1, "a1": 2.1, "fov": 40, "ly": 0.6, "act": {**_CV, "at": 0.02, "v": 1, "n": 2}}},
  {"name": "pit", "w": 1200, "h": 800, "t": 2.6, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 8.5, "h": 2.6, "a0": 2.4, "a1": 2.4, "fov": 46, "ly": 0.6, "act": {"type": "pit", "car": 0, "box": 0.4}}},
  {"name": "corners", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "side", "car": 0, "side": 6.5, "h": 1.2, "fw": 1, "look": 0.5, "ly": 1.0, "fov": 50, "act": {**_CV, "at": 0.7, "v": 30}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "head": "Катар: 27 кругов", "sub": "и шины в боксы", "chip": "27 кругов на комплект",
    "say": "Комплект шин в Катаре живёт максимум двадцать семь кругов. Дальше на нём ехать нельзя.",
    "hl": ["двадцать", "семь"]},
   {"kind": "tyre", "head": "27", "laps": 27, "chip": "Лимит 2026 · весь уикенд",
    "say": "Лимит объявили двадцатого ноября. Круги считают за весь уикенд, вместе с тренировками.",
    "hl": ["весь", "уикенд"]},
   {"kind": "big", "big": "57", "chip": "57 кругов → 2 пит-стопа",
    "say": "Гонка длится пятьдесят семь кругов, значит у каждого минимум два пит-стопа.",
    "hl": ["два"]},
   {"kind": "big", "chip": "Повороты 12–14 · почти в пол",
    "say": "Виноваты быстрые правые повороты с двенадцатого по четырнадцатый, их проходят почти в пол.",
    "hl": ["почти", "в", "пол"]},
   {"kind": "big", "chip": "Передние шины · ≈25 кругов",
    "say": "Больше всех страдает левая передняя: она изнашивается до предела примерно за двадцать пять кругов.",
    "hl": ["левая", "передняя"]},
   {"kind": "big", "chip": "2023 · 18 кругов",
    "say": "В двадцать третьем лимит был восемнадцать кругов: боковины шин страдали на высоких поребриках.",
    "hl": ["восемнадцать"]},
   {"kind": "big", "chip": "2023 · жара и влажность",
    "say": "Ночь была душной. Сарджент сошёл из-за обезвоживания, Окона стошнило прямо в машине.",
    "hl": ["обезвоживания"]},
   {"kind": "big", "chip": "2025 · 25 кругов",
    "say": "В прошлом году лимит был двадцать пять. Макларен не заехал под машину безопасности, и победил Ферстаппен.",
    "hl": ["Ферстаппен"]},
   {"kind": "end", "tag": "Катар · 29 ноября",
    "say": "Гонка двадцать девятого ноября. Во сколько по вашему времени, смотрите на ЛапРадар.", "hl": ["вашему", "времени"]}
  ],
  "en": [
   {"kind": "big", "head": "Qatar: 27 laps", "sub": "then the tyres must go", "chip": "27 laps per set",
    "say": "In Qatar a set of tyres can do twenty-seven laps at most. After that it has to come off.",
    "hl": ["twenty-seven"]},
   {"kind": "tyre", "head": "27", "laps": 27, "chip": "2026 limit · whole weekend",
    "say": "The limit was announced on November twentieth. Laps count across the whole weekend, practice included.",
    "hl": ["whole", "weekend"]},
   {"kind": "big", "big": "57", "chip": "57 laps → 2 stops",
    "say": "The race is fifty-seven laps, so every driver has to stop at least twice.",
    "hl": ["twice"]},
   {"kind": "big", "chip": "Turns 12–14 · nearly flat out",
    "say": "Blame the fast right-handers from Turn twelve to fourteen. Drivers take them almost flat out.",
    "hl": ["flat", "out"]},
   {"kind": "big", "chip": "Front tyres · ≈25 laps",
    "say": "The left front takes the worst of it. It hits the wear limit after roughly twenty-five laps.",
    "hl": ["left", "front"]},
   {"kind": "big", "chip": "2023 · 18 laps",
    "say": "In twenty twenty-three it was eighteen laps, after the sidewalls suffered on the high kerbs.",
    "hl": ["eighteen"]},
   {"kind": "big", "chip": "2023 · heat and humidity",
    "say": "It was a brutal night: Sargeant retired with dehydration, and Ocon was sick in the car.",
    "hl": ["dehydration"]},
   {"kind": "big", "chip": "2025 · 25 laps",
    "say": "Last year the limit was twenty-five. McLaren didn't pit under the safety car, and Verstappen won.",
    "hl": ["Verstappen"]},
   {"kind": "end", "tag": "Qatar · November 29",
    "say": "The race is on November twenty-ninth. Check the start in your own time zone on LapRadar.", "hl": ["your", "own", "time", "zone"]}
  ]
 }
}

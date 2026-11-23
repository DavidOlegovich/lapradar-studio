# Новая машина IndyCar IR-28: дебют 2028, мотор 2,4 л V6 до 760 л.с., батарейный гибрид, первые тесты на овале IMS 9-10.09.2026, Себринг в октябре. HQ, овал.
# Машины условные (синяя и красная), без логотипов и настоящих ливрей. Камера (shots) общая для всех языков.
_B = {"c": "#1d4ed8", "a": "#e5e7eb", "p": "stripe"}
_R = {"c": "#c2272d", "a": "#e5e7eb", "p": "stripe"}
_PAINT = {"0": _B, "1": _R, "2": _B, "3": _R}
_CV = {"type": "convoy", "at": "straight", "n": 2, "v": 62}

VIDEO = {
 "slug": "ir28-indycar-new-car",
 "track": "oval",
 "theme": "day",
 "hq": True,
 "shots": [
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10.5, "h": 4.5, "h2": 4, "side": 0, "side2": 1.2, "look": 24, "drop": 3, "noCut": True, "paint": _PAINT, "act": {**_CV, "n": 1}},
  {"type": "carorbit", "car": 0, "r": 11, "r2": 10, "h": 2.2, "h2": 1.7, "a0": 0.7, "a1": 1.4, "fov": 48, "ly": 0.8, "paint": _PAINT, "act": {**_CV, "v": 22, "n": 1}},
  {"type": "side", "car": 0, "side": 6.5, "side2": 6, "h": 1.0, "h2": 1.3, "fw": 2.5, "fw2": -1.5, "look": 0.5, "ly": 0.9, "fov": 52, "paint": _PAINT, "act": {**_CV, "v": 40, "n": 1}},
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10.5, "h": 4.5, "h2": 4, "side": -1.2, "side2": 1.2, "look": 24, "drop": 3, "noCut": True, "paint": _PAINT, "act": {**_CV, "n": 2, "t0": 2}},
  {"type": "chase", "car": 3, "dist": 20, "dist2": 17, "h": 7.5, "h2": 6.5, "side": 2.5, "look": 22, "drop": 3, "fov": 50, "noCut": True, "paint": _PAINT, "act": {**_CV, "n": 4, "v": 50}},
  {"type": "onboard", "car": 0, "fov": 70, "eh": 1.3, "ez": 0.05, "ty": 1.6, "paint": _PAINT, "act": {**_CV, "n": 1, "v": 50}},
  {"type": "fly", "from": 0.02, "to": 0.08, "h": 70, "h2": 150, "side": 40, "ahead": 260}
 ],
 "coverShot": {"type": "chase", "car": 0, "dist": 11, "h": 3.4, "side": 0, "look": 20, "drop": 2, "fov": 46, "paint": _PAINT, "act": {**_CV, "n": 1, "v": 8}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 8.5, "h": 1.8, "a0": 2.4, "a1": 2.4, "fov": 42, "ly": 0.6, "paint": _PAINT, "act": {**_CV, "n": 1, "v": 1}}},
  {"name": "oval", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 3, "dist": 17, "h": 6.5, "side": 2.5, "look": 20, "drop": 3, "fov": 48, "paint": _PAINT, "act": {**_CV, "n": 4, "v": 50}}},
  {"name": "side", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "side", "car": 0, "side": 6, "h": 1.1, "fw": 0.5, "look": 0.5, "ly": 0.9, "fov": 46, "paint": _PAINT, "act": {**_CV, "n": 1, "v": 40}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "IR-28", "chip": "IR-28 · новая машина IndyCar",
    "say": "Эта машина заменит нынешнюю в IndyCar. Она уже выезжала на овал Индианаполиса. Что в ней нового?",
    "hl": ["IndyCar", "нового"]},
   {"kind": "big", "big": "760", "chip": "V6 2,4 л · до 760 л.с.",
    "say": "Мотор вырос с двух целых двух до двух целых четырёх литров. Два турбонаддува, до семисот шестидесяти сил.",
    "hl": ["двух целых четырёх", "семисот шестидесяти"]},
   {"kind": "big", "big": "×14", "chip": "Батарея вместо суперконденсатора",
    "say": "Гибрид теперь с батареей, первой в истории серии. Запас энергии в четырнадцать раз больше, чем у суперконденсатора.",
    "hl": ["батареей", "четырнадцать"]},
   {"kind": "big", "big": "9.09", "chip": "Овал IMS · Росси и Палоу",
    "say": "Девятого сентября Александр Росси первым проехал на ней по овалу. На следующий день за руль сел Алекс Палоу.",
    "hl": ["Росси", "Палоу"]},
   {"kind": "big", "big": "237,498", "chip": "Рекорд 1996 · 237,498 миль/ч",
    "say": "В IndyCar считают, что машина может побить рекорды Индианаполиса девяносто шестого года. В сентябре за ними не гнались: скорости держали умеренными.",
    "hl": ["рекорды", "не гнались"]},
   {"kind": "big", "big": "43", "chip": "Себринг · Палоу · 43 круга",
    "say": "В октябре Палоу проехал сорок три круга на Себринге: тест на прочность. Гонки на ней начнутся в двадцать восьмом.",
    "hl": ["сорок три", "двадцать восьмом"]},
   {"kind": "end", "tag": "IndyCar · IR-28",
    "say": "Календарь и таблицу IndyCar смотрите на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "IR-28", "chip": "IR-28 · IndyCar's new car",
    "say": "This car will replace the current one in IndyCar. It has already run on the Indianapolis oval. What's new?",
    "hl": ["IndyCar", "new"]},
   {"kind": "big", "big": "760", "chip": "2.4 L V6 · up to 760 hp",
    "say": "The engine grows from two point two to two point four litres. Twin turbos, up to seven hundred and sixty horsepower.",
    "hl": ["two point four", "seven hundred and sixty"]},
   {"kind": "big", "big": "×14", "chip": "Battery, not supercapacitor",
    "say": "The hybrid now uses a battery, a first for the series. It stores fourteen times more energy than the supercapacitor.",
    "hl": ["battery", "fourteen"]},
   {"kind": "big", "big": "9.09", "chip": "IMS oval · Rossi and Palou",
    "say": "On September ninth, Alexander Rossi was first to drive it on the oval. The next day, Alex Palou took over.",
    "hl": ["Rossi", "Palou"]},
   {"kind": "big", "big": "237.498", "chip": "1996 record · 237.498 mph",
    "say": "IndyCar says the car can beat Indianapolis records from nineteen ninety-six. In September they weren't chasing them: speeds were kept moderate.",
    "hl": ["records", "weren't chasing"]},
   {"kind": "big", "big": "43", "chip": "Sebring · Palou · 43 laps",
    "say": "In October Palou ran forty-three laps at Sebring, a durability test. Racing with it starts in twenty twenty-eight.",
    "hl": ["forty-three", "twenty-eight"]},
   {"kind": "end", "tag": "IndyCar · IR-28",
    "say": "Follow IndyCar on the LapRadar live map."}
  ]
 }
}

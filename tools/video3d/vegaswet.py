# Мокрый четверг в Вегасе по данным LapRadar (OpenF1 через наш API, сессии 11413 и 11414): FP1 без единого круга со временем,
# FP2 на промежуточных, лучший круг Расселла 1:47.272 против сухого 1:33.602 Норриса в FP2-2025, 33 удалённых круга.
# Дождь: эффект студии (shot "rain"), цвет шин: shot "band" (синий: полные дождевые, зелёный: промежуточные). Камера (shots) общая для всех языков.
_WET = "#3b82f6"
_INTER = "#22c55e"

VIDEO = {
 "slug": "las-vegas-wet-thursday-2026",
 "track": "las-vegas",
 "theme": "vegas",
 "shots": [
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 5.5, "h2": 5, "side": 0, "side2": 0, "look": 22, "drop": 8, "noCut": True,
   "rain": True, "band": _WET, "neon": True, "act": {"type": "convoy", "at": "straight", "n": 2, "v": 38}},
  {"type": "chase", "car": 1, "dist": 12, "dist2": 10.5, "h": 4.5, "h2": 4, "side": 2.2, "side2": -1.2, "look": 22, "drop": 6, "noCut": True,
   "rain": True, "band": _WET, "neon": True, "act": {"type": "convoy", "at": "straight", "n": 2, "v": 38, "t0": 6}},
  {"type": "chase", "car": 1, "dist": 13, "dist2": 11, "h": 6, "h2": 5, "side": 1.5, "side2": -1.5, "look": 25, "drop": 9, "noCut": True,
   "rain": {"k": 0.25}, "band": _INTER, "neon": True, "act": {"type": "follow", "at": 0.6}},
  {"type": "chase", "car": 0, "dist": 14, "dist2": 12, "h": 6, "h2": 5.5, "side": 0, "side2": 0, "look": 22, "drop": 9, "noCut": True,
   "rain": {"k": 0.15}, "band": _INTER, "neon": True, "sphere": True, "act": {"type": "convoy", "at": "straight", "v": 62},
   "hud": {"type": "gap", "ref": 93.602, "lap": 107.272}},
  {"type": "chase", "car": 3, "dist": 15, "dist2": 13, "h": 8, "h2": 7, "side": 0.5, "side2": -0.5, "look": 30, "drop": 9, "noCut": True,
   "rain": {"k": 0.15}, "band": _INTER, "neon": True, "act": {"type": "convoy", "at": "straight", "v": 62, "t0": 6}},
  {"type": "top", "reveal": True, "badges": True, "k": 1.1, "tilt": 0.15, "rot0": 0, "rot1": 0.12},
  {"type": "fly", "from": 0.36, "to": 0.4, "h": 70, "h2": 120, "side": -60, "ahead": 300, "rain": {"k": 0.3}, "sphere": True, "neon": True}
 ],
 "coverShot": {"type": "chase", "car": 0, "dist": 11, "h": 4, "side": 0, "look": 22, "drop": 1.5, "noCut": True, "rain": True, "band": _INTER, "neon": True,
   "act": {"type": "convoy", "at": "straight", "n": 2, "v": 38}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 10, "h": 3.4, "side": -3, "look": 16, "drop": 2, "fov": 42, "rain": True, "band": _INTER, "neon": True,
            "act": {"type": "convoy", "at": "straight", "n": 2, "v": 38}}},
  {"name": "spray", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 3, "dist": 12, "h": 4.5, "side": -2.6, "look": 26, "drop": 3, "fov": 44, "rain": True, "band": _WET, "neon": True,
            "act": {"type": "convoy", "at": "straight", "v": 40}}},
  {"name": "inters", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 1, "dist": 9, "h": 3, "side": 3, "look": 14, "drop": 1.8, "fov": 42, "rain": {"k": 0.25}, "band": _INTER, "neon": True,
            "act": {"type": "follow", "at": 0.6}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "МОКРЫЙ ВЕГАС", "chip": "FP1 · 0 кругов со временем",
    "say": "Первая тренировка в Вегасе: час под дождём, и ни одного круга со временем.",
    "hl": ["ни", "одного"]},
   {"kind": "big", "big": "WET", "chip": "FP1 · только WET",
    "say": "Все выезжали на полных дождевых шинах. На прямой ловушка скорости поймала максимум сто девяносто.",
    "hl": ["дождевых", "сто девяносто"]},
   {"kind": "big", "big": "INTER", "chip": "FP2 · промежуточные",
    "say": "К вечеру дождь кончился, но асфальт остался мокрым. Норрис первым перешёл на промежуточные.",
    "hl": ["Норрис", "промежуточные"]},
   {"kind": "big", "big": "1:47", "chip": "Расселл · 1:47.272", "gl": ["2025 · сухо · Норрис", "2026 · мокро · Расселл"], "gd": "+13,670 с",
    "say": "Лучший круг у Расселла. Это почти на четырнадцать секунд медленнее сухой тренировки год назад.",
    "hl": ["Расселла", "четырнадцать"]},
   {"kind": "big", "big": "0,071", "chip": "Гасли +0,071 · Леклер +0,333",
    "say": "Гасли проиграл ему семь сотых, Леклер треть секунды. Ферстаппен только тринадцатый.",
    "hl": ["семь сотых", "Ферстаппен"]},
   {"kind": "big", "big": "33", "chip": "33 круга удалено · T8 × 13",
    "say": "Тридцать три круга аннулировали. Чаще всего за вылет за лимиты в восьмом повороте.",
    "hl": ["Тридцать три", "восьмом"]},
   {"kind": "end", "tag": "Вегас-2026 · квалификация в пятницу",
    "say": "Все эти круги и шины есть на нашей живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "WET VEGAS", "chip": "FP1 · 0 timed laps",
    "say": "First practice in Vegas: an hour of rain and not a single timed lap.",
    "hl": ["single"]},
   {"kind": "big", "big": "WET", "chip": "FP1 · full wets only",
    "say": "Everyone ran full wet tyres. The fastest car through the speed trap managed just one hundred and ninety.",
    "hl": ["wet", "ninety"]},
   {"kind": "big", "big": "INTER", "chip": "FP2 · intermediates",
    "say": "By the evening the rain had stopped, but the track was still wet. Norris was the first onto intermediates.",
    "hl": ["Norris", "intermediates"]},
   {"kind": "big", "big": "1:47", "chip": "Russell · 1:47.272", "gl": ["2025 · dry · Norris", "2026 · wet · Russell"], "gd": "+13.670 s",
    "say": "Russell set the best lap, almost fourteen seconds slower than dry practice a year ago.",
    "hl": ["Russell", "fourteen"]},
   {"kind": "big", "big": "0.071", "chip": "Gasly +0.071 · Leclerc +0.333",
    "say": "Gasly was seven hundredths behind, Leclerc a third of a second. Verstappen was only thirteenth.",
    "hl": ["seven hundredths", "Verstappen"]},
   {"kind": "big", "big": "33", "chip": "33 laps deleted · T8 × 13",
    "say": "Thirty-three laps were deleted, most of them for track limits at Turn Eight.",
    "hl": ["Thirty-three", "Eight"]},
   {"kind": "end", "tag": "Vegas 2026 · qualifying on Friday",
    "say": "All of these laps and tyres are on our LapRadar live map."}
  ]
 }
}

# Штрафы F1 простыми словами: +5/+10 с, проезд по пит-лейну, стоп-энд-гоу 10 с, штраф на старте, дисквалификация;
# штрафные очки суперлицензии (12 за 12 месяцев = пропуск гонки, Магнуссен: Баку 2024 после Монцы), 2026: очки дают редко.
# HQ-режим, Монца днём (там Магнуссен получил 12-е очко). Лестница наказаний: hud "ladder" (подписи ступеней из сцены, sc.lad).
# Машины: условные цвета без ливрей. Камера (shots) общая для всех языков.
_WHT = ["#e5e7eb", "#dc2626", "stripe"]
_BLU = ["#1d4ed8", "#facc15", "band"]
_GRN = ["#15803d", "#f8fafc", "split"]
_CV = {"type": "convoy", "at": 0.2, "v": 30, "n": 3}
_LAD = lambda hi, upto=6: {"type": "ladder", "hi": hi, "upto": upto}

VIDEO = {
 "slug": "f1-penalties-explained",
 "track": "monza",
 "theme": "day",
 "hq": {"cars": [_WHT, _BLU, _GRN], "lampFade": True},
 "shots": [
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 5.5, "h2": 5, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 60, "n": 3}},
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10, "h": 4.5, "h2": 4, "side": -2.5, "side2": -1.5, "look": 14, "drop": 3, "noCut": True, "act": {"type": "pit", "car": 0, "box": 0.35, "stop": 3.2}, "hud": _LAD(0, 2)},
  {"type": "carorbit", "car": 0, "r": 10, "r2": 9, "h": 1.4, "h2": 1.9, "a0": 0.5, "a1": 1.1, "fov": 46, "ly": 0.8, "act": {**_CV, "at": 0.25, "v": 22, "n": 1}, "hud": _LAD(2, 4)},
  {"type": "side", "car": 0, "side": 8.4, "side2": 7.8, "h": 1.1, "h2": 1.3, "fw": 2.5, "fw2": -2.5, "look": 0.5, "ly": 0.9, "fov": 54, "act": {**_CV, "at": 0.3, "v": 28}, "hud": _LAD(3, 4)},
  {"type": "orbit", "at": 0.97, "r": 320, "r2": 290, "h": 100, "h2": 85, "a0": 0.7, "a1": 1.0, "fov": 50, "act": {**_CV, "at": 0.95, "v": 40}, "hud": _LAD(4)},
  {"type": "carorbit", "car": 1, "r": 10.5, "r2": 9.5, "h": 1.5, "h2": 2.0, "a0": -0.5, "a1": 0.2, "fov": 48, "ly": 0.8, "act": {**_CV, "at": 0.4, "v": 22, "n": 2}, "hud": _LAD(5)},
  {"type": "stage", "items": [{"o": "f1", "c": _WHT[0], "a": _WHT[1], "p": _WHT[2]}], "bg": "red", "beams": True, "r": 10.5, "r2": 9.5, "h": 2.4, "h2": 3.0, "a0": -0.6, "a1": 0.4, "spin": 0.15, "ly": 0.8},
  {"type": "chase", "car": 0, "dist": 15, "dist2": 13, "h": 6, "h2": 5.5, "side": -3.5, "side2": -1, "look": 28, "drop": 3, "noCut": True, "act": {"type": "duel"}},
  {"type": "carorbit", "car": 2, "r": 10.5, "r2": 9.5, "h": 1.6, "h2": 2.1, "a0": 0.3, "a1": 0.95, "fov": 48, "ly": 0.8, "act": {**_CV, "at": 0.45, "v": 22}},
  {"type": "orbit", "at": 0.97, "r": 430, "r2": 410, "h": 130, "h2": 120, "a0": 1.2, "a1": 1.3, "fov": 50, "act": {**_CV, "at": 0.95, "v": 45}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 9.5, "h": 1.4, "a0": 1.85, "a1": 1.85, "fov": 44, "act": {**_CV, "at": 0.25, "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 7.5, "h": 1.2, "a0": 2.1, "a1": 2.1, "fov": 40, "ly": 0.6, "act": {**_CV, "at": 0.25, "v": 1, "n": 2}}},
  {"name": "pit", "w": 1200, "h": 800, "t": 1.8, "u": 0.4,
   "shot": {"type": "chase", "car": 0, "dist": 10, "h": 3.8, "side": -2.4, "look": 12, "drop": 2, "fov": 44, "act": {"type": "pit", "car": 0, "box": 0.35, "stop": 3.2}}},
  {"name": "duel", "w": 1200, "h": 800, "t": 3.2, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 10, "h": 3.8, "side": -2.4, "look": 12, "drop": 2, "fov": 42, "act": {"type": "duel"}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "head": "Штрафы F1", "sub": "от 5 секунд до пропуска гонки", "chip": "Штрафы F1: от мягких к строгим",
    "say": "За что пилот теряет пять секунд, а за что целую гонку? Вот лестница штрафов Формулы один.",
    "hl": ["пять", "секунд", "гонку"]},
   {"kind": "big", "gh": "Лестница штрафов", "lad": ["+5 секунд", "+10 секунд", "Проезд по пит-лейну", "Стоп-энд-гоу 10 с", "Штраф на старте", "Дисквалификация"],
    "say": "Самые мягкие: плюс пять или десять секунд. На пит-стопе машина стоит, механики ждут.",
    "hl": ["пять", "десять"]},
   {"kind": "big", "gh": "Лестница штрафов", "lad": ["+5 секунд", "+10 секунд", "Проезд по пит-лейну", "Стоп-энд-гоу 10 с", "Штраф на старте", "Дисквалификация"],
    "say": "Строже проезд по пит-лейну: заехал, проехал с ограничением скорости и вернулся на трассу.",
    "hl": ["пит-лейну"]},
   {"kind": "big", "gh": "Лестница штрафов", "lad": ["+5 секунд", "+10 секунд", "Проезд по пит-лейну", "Стоп-энд-гоу 10 с", "Штраф на старте", "Дисквалификация"],
    "say": "Ещё строже стоп-энд-гоу: десять секунд стоять в боксе, и машину никто не трогает.",
    "hl": ["десять", "секунд"]},
   {"kind": "big", "gh": "Лестница штрафов", "lad": ["+5 секунд", "+10 секунд", "Проезд по пит-лейну", "Стоп-энд-гоу 10 с", "Штраф на старте", "Дисквалификация"],
    "say": "Штраф на старте: назад на пять или десять мест. Чаще всего за лишние детали мотора.",
    "hl": ["мотора"]},
   {"kind": "big", "gh": "Лестница штрафов", "lad": ["+5 секунд", "+10 секунд", "Проезд по пит-лейну", "Стоп-энд-гоу 10 с", "Штраф на старте", "Дисквалификация"],
    "say": "Дисквалификация вычёркивает пилота из результатов. Чаще всего за технические нарушения.",
    "hl": ["Дисквалификация"]},
   {"kind": "big", "big": "12", "chip": "12 очков за 12 месяцев = пропуск гонки",
    "say": "Есть и штрафные очки в суперлицензии. Двенадцать за двенадцать месяцев, и пилот пропускает гонку.",
    "hl": ["Двенадцать"]},
   {"kind": "big", "chip": "Магнуссен · Монца 2024 → без Баку",
    "say": "Первым так пропустил гонку Магнуссен в двадцать четвёртом. Двенадцатое очко он получил в Монце.",
    "hl": ["Магнуссен"]},
   {"kind": "big", "chip": "2026: очки дают редко",
    "say": "В этом сезоне очки дают редко: только за опасную или безрассудную езду и намеренные столкновения.",
    "hl": ["редко"]},
   {"kind": "end", "tag": "Штрафы F1 · коротко",
    "say": "Гонки вживую смотрите на карте ЛапРадар."}
  ],
  "en": [
   {"kind": "big", "head": "F1 penalties", "sub": "from 5 seconds to a race ban", "chip": "F1 penalties: mild to severe",
    "say": "What costs a driver five seconds, and what costs a whole race? Here's the Formula One penalty ladder.",
    "hl": ["five", "seconds", "race"]},
   {"kind": "big", "gh": "The penalty ladder", "lad": ["+5 seconds", "+10 seconds", "Drive-through", "10 s stop-go", "Grid penalty", "Disqualification"],
    "say": "The mildest: plus five or ten seconds. At the pit stop the car sits still and the crew waits.",
    "hl": ["five", "ten"]},
   {"kind": "big", "gh": "The penalty ladder", "lad": ["+5 seconds", "+10 seconds", "Drive-through", "10 s stop-go", "Grid penalty", "Disqualification"],
    "say": "Next up, the drive-through: in, down the pit lane at the speed limit, and back out.",
    "hl": ["drive-through"]},
   {"kind": "big", "gh": "The penalty ladder", "lad": ["+5 seconds", "+10 seconds", "Drive-through", "10 s stop-go", "Grid penalty", "Disqualification"],
    "say": "Harsher still, the stop-go: ten seconds in the box, and nobody touches the car.",
    "hl": ["ten", "seconds"]},
   {"kind": "big", "gh": "The penalty ladder", "lad": ["+5 seconds", "+10 seconds", "Drive-through", "10 s stop-go", "Grid penalty", "Disqualification"],
    "say": "A grid penalty: five or ten places back at the start, most often for extra engine parts.",
    "hl": ["engine"]},
   {"kind": "big", "gh": "The penalty ladder", "lad": ["+5 seconds", "+10 seconds", "Drive-through", "10 s stop-go", "Grid penalty", "Disqualification"],
    "say": "Disqualification wipes a driver from the results, most often for a technical breach.",
    "hl": ["Disqualification"]},
   {"kind": "big", "big": "12", "chip": "12 points in 12 months = race ban",
    "say": "Then there are super licence penalty points. Twelve in twelve months, and you sit out a race.",
    "hl": ["Twelve"]},
   {"kind": "big", "chip": "Magnussen · Monza 2024 → no Baku",
    "say": "Magnussen was the first to be banned this way, in twenty twenty-four. His twelfth point came at Monza.",
    "hl": ["Magnussen"]},
   {"kind": "big", "chip": "2026: points are rare",
    "say": "This season points are rare: only for dangerous or reckless driving, or deliberate collisions.",
    "hl": ["rare"]},
   {"kind": "end", "tag": "F1 penalties · in short",
    "say": "Watch the races live on the LapRadar map."}
  ]
 }
}

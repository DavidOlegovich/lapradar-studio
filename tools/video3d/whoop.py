# WHOOP и F1: контракт на 4 года, пульс пилотов в трансляциях с 2027, браслет на плече под огнеупорным рукавом, Ферстаппен отказался.
# Пульс рисуем своей графикой (hud "pulse": сердце, кардиограмма, число), без логотипа WHOOP. Камера (shots) общая для всех языков.
VIDEO = {
 "slug": "whoop-f1-heart-rate",
 "track": "las-vegas",
 "theme": "vegas",
 "shots": [
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 6, "h2": 5.5, "side": 0, "side2": 0, "look": 22, "drop": 9, "noCut": True, "neon": True,
   "act": {"type": "convoy", "at": "straight"}, "hud": {"type": "pulse", "from": 96, "to": 168}},
  {"type": "stage", "items": [{"o": "f1", "c": "#1e3a8a"}], "bg": "blue", "beams": True, "r": 10.5, "r2": 9.5, "h": 2.4, "h2": 3.2, "a0": 0.9, "a1": -0.2, "spin": 0.3, "ly": 0.8},
  {"type": "chase", "car": 1, "dist": 13, "dist2": 11, "h": 5.5, "h2": 4.5, "side": 1.5, "side2": -1.5, "look": 25, "drop": 9, "noCut": True, "neon": True,
   "act": {"type": "follow", "at": 0.6}},
  {"type": "chase", "car": 3, "dist": 14, "dist2": 12, "h": 6, "h2": 5, "side": 0.5, "side2": -0.5, "look": 25, "drop": 9, "noCut": True, "neon": True,
   "act": {"type": "convoy", "at": "straight", "t0": 6}, "hud": {"type": "pulse", "from": 150, "to": 178}},
  {"type": "stage", "items": [{"o": "f1", "c": "#111827"}], "bg": "red", "r": 10.5, "r2": 9.5, "h": 2.6, "h2": 3.2, "a0": -0.6, "a1": 0.4, "spin": 0.2, "ly": 0.8},
  {"type": "stage", "items": [{"o": "f1", "c": "#e10600", "x": -1.4, "ry": 0.3}, {"o": "f1", "c": "#e10600", "x": 2.2, "z": -1.6, "ry": 0.3}], "bg": "red", "beams": True, "r": 12, "r2": 10.5, "h": 3, "h2": 3.6, "a0": -0.4, "a1": 0.3, "spin": 0, "ly": 1.0},
  {"type": "fly", "from": 0.42, "to": 0.5, "h": 60, "h2": 140, "side": 40, "ahead": 260, "neon": True}
 ],
 "coverShot": {"type": "chase", "car": 0, "dist": 12, "h": 4.5, "side": 0, "look": 22, "drop": 1, "noCut": True, "neon": True, "act": {"type": "convoy", "at": "straight"}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 1.0, "u": 0.5,
   "shot": {"type": "chase", "car": 1, "dist": 10, "h": 3.6, "side": -3.5, "look": 14, "drop": 2, "fov": 40, "neon": True, "act": {"type": "boost"}}},
  {"name": "strip", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 3, "dist": 10, "h": 4.2, "side": -2.4, "look": 30, "drop": 3, "fov": 44, "neon": True, "act": {"type": "convoy", "at": "straight"}}},
  {"name": "car", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "f1", "c": "#1e3a8a"}], "bg": "blue", "beams": True, "r": 11, "h": 2.8, "a0": 0.6, "spin": 0, "ly": 0.8}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "ПУЛЬС В ЭФИРЕ", "chip": "пульс пилота · 2027", "unit": "уд/мин",
    "say": "С двадцать седьмого в трансляциях Формулы один покажут пульс пилотов прямо в гонке.",
    "hl": ["пульс"]},
   {"kind": "big", "big": "4", "chip": "WHOOP × F1 · 4 года",
    "say": "Формула один подписала с WHOOP контракт на четыре года. Его объявили в Вегасе.",
    "hl": ["четыре", "Вегасе"]},
   {"kind": "big", "big": "FIA", "chip": "одобрено FIA",
    "say": "Это первый потребительский трекер, одобренный FIA для гонок. Его носят на плече под огнеупорным рукавом.",
    "hl": ["FIA", "плече"]},
   {"kind": "big", "big": "170", "chip": "в среднем > 170 уд/мин", "unit": "уд/мин",
    "say": "В гонке сердце пилота в среднем бьётся чаще ста семидесяти раз в минуту.",
    "hl": ["ста", "семидесяти"]},
   {"kind": "big", "big": "NO", "chip": "Ферстаппен · отказался",
    "say": "Но не все согласны. Ферстаппен отказался: людям не нужно знать его пульс.",
    "hl": ["Ферстаппен", "отказался"]},
   {"kind": "big", "big": "2026", "chip": "Ferrari · с января 2026",
    "say": "Леклер уже носит браслет, ему нечего скрывать. А WHOOP с января партнёр Ferrari.",
    "hl": ["Леклер", "Ferrari"]},
   {"kind": "end", "tag": "Пульс пилотов · с 2027",
    "say": "Если Формула один откроет эти данные, добавим их на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "HEART RATE ON AIR", "chip": "driver heart rate · 2027", "unit": "BPM",
    "say": "From twenty twenty-seven, Formula One broadcasts will show drivers' heart rates live in the race.",
    "hl": ["heart"]},
   {"kind": "big", "big": "4", "chip": "WHOOP × F1 · 4 years",
    "say": "Formula One has signed a four-year deal with WHOOP. It was announced in Vegas.",
    "hl": ["four-year", "Vegas"]},
   {"kind": "big", "big": "FIA", "chip": "FIA-approved",
    "say": "It's the first consumer wearable the FIA has approved for racing. It sits on the upper arm, under a fireproof sleeve.",
    "hl": ["FIA", "arm"]},
   {"kind": "big", "big": "170", "chip": "average > 170 BPM", "unit": "BPM",
    "say": "In a race a driver's heart averages more than one hundred and seventy beats a minute.",
    "hl": ["seventy"]},
   {"kind": "big", "big": "NO", "chip": "Verstappen · opted out",
    "say": "Not everyone is in. Verstappen said no: people don't need to know his heart rate.",
    "hl": ["Verstappen", "no"]},
   {"kind": "big", "big": "2026", "chip": "Ferrari · since January 2026",
    "say": "Leclerc already wears the strap and has nothing to hide. And WHOOP has partnered Ferrari since January.",
    "hl": ["Leclerc", "Ferrari"]},
   {"kind": "end", "tag": "Driver heart rate · from 2027",
    "say": "If Formula One opens up this data, we'll add it to LapRadar."}
  ]
 }
}

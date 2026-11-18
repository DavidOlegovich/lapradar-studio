# Возвращение V8 в Формулу 1: что предлагает FIA. Камера (shots) общая для всех языков.
VIDEO = {
 "slug": "f1-v8-return-2031",
 "track": "monza",
 "theme": "day",
 "shots": [
  {"type": "chase", "car": 0, "dist": 11, "dist2": 9, "h": 4, "h2": 3.5, "side": -2.4, "side2": 2, "look": 20, "drop": 3, "act": {"type": "speed"}},
  {"type": "stage", "items": [{"o": "f1", "c": "#e10600"}], "bg": "red", "r": 10, "r2": 9.5, "h": 2.4, "h2": 3.2, "a0": 0.9, "a1": -0.2, "spin": 0.3, "ly": 0.8},
  {"type": "chase", "car": 0, "dist": 11, "dist2": 10, "h": 4.5, "h2": 4.2, "side": 1.5, "side2": 1, "look": 10, "drop": 3, "act": {"type": "energy"}, "hud": {"type": "bars", "rows": [{"label": "2026", "v": 350, "c": "#9fb4ff"}, {"label": "V8", "v": 200, "c": "#facc15"}], "min": 0, "max": 380, "hi": 1}},
  {"type": "chase", "car": 1, "dist": 16, "dist2": 12, "h": 6, "h2": 5, "side": -3, "side2": -2, "look": 35, "drop": 2, "noCut": True, "act": {"type": "boost"}},
  {"type": "stage", "items": [{"o": "f1", "c": "#f3f4f6", "x": -2.3, "ry": 0.25}, {"o": "f1", "c": "#e10600", "x": 2.3, "ry": -0.25}], "bg": "blue", "r": 13, "r2": 11, "h": 3, "h2": 4, "a0": -0.4, "a1": 0.3, "spin": 0.1, "ly": 0.6},
  {"type": "chase", "car": 0, "dist": 14, "dist2": 12, "h": 6, "h2": 5, "side": 1.5, "side2": -1.5, "look": 25, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": 0.4}},
  {"type": "fly", "from": 0.05, "to": 0.13, "h": 60, "h2": 140, "side": 40, "ahead": 260}
 ],
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 11, "h": 4, "side": -2.4, "look": 18, "drop": 3, "fov": 44, "act": {"type": "speed"}}},
  {"name": "boost", "w": 1200, "h": 800, "t": 1.2, "u": 0.5,
   "shot": {"type": "chase", "car": 1, "dist": 9, "h": 3.6, "side": -2.2, "look": 14, "drop": 2, "fov": 40, "act": {"type": "boost"}}},
  {"name": "pack", "w": 1200, "h": 800, "t": 2.4, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 17, "h": 6.5, "side": -4, "look": 14, "drop": 3, "fov": 44, "act": {"type": "convoy", "at": 0.15}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "V8 ВОЗВРАЩАЮТСЯ?", "sub": "новые моторы Формулы 1",
    "say": "Формула один хочет вернуть моторы V8. Только это будут совсем не те V8, что ревели до тринадцатого года.",
    "hl": ["V8"]},
   {"kind": "big", "big": "2,1", "chip": "V6 1,6 л → V8 2,1 л",
    "say": "Идея простая и дешёвая: взять нынешний турбомотор V6 и добавить к нему два цилиндра. Получится около двух литров.",
    "hl": ["два цилиндра"]},
   {"kind": "big", "big": "200", "barTexts": ["350 кВт", "200 кВт"],
    "say": "Электрики станет меньше. Вместо трёхсот пятидесяти киловатт двести.",
    "hl": ["двести"]},
   {"kind": "big", "big": "+100", "chip": "+100 кВт на обгон",
    "say": "Сто киловатт доступны всегда, ещё сто только для обгона, как кнопка пуш-ту-пасс в ИндиКаре.",
    "hl": ["для обгона"]},
   {"kind": "big", "big": "−80", "chip": "−80 кг",
    "say": "Машины хотят облегчить на восемьдесят килограммов. Цель FIA меньше семисот.",
    "hl": ["восемьдесят"]},
   {"kind": "big", "big": "2031", "chip": "2031? · решение в декабре",
    "say": "Нынешние правила действуют до конца тридцатого года, так что ждать V8 стоит в тридцать первом. Решение пока не принято.",
    "hl": ["тридцать первом", "не принято"]},
   {"kind": "end", "tag": "Новости правил F1",
    "say": "Что решат в FIA, расскажем на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "V8s ARE BACK?", "sub": "F1's next engines",
    "say": "Formula One wants V8 engines back. Just not the screaming V8s that raced until twenty thirteen.",
    "hl": ["V8"]},
   {"kind": "big", "big": "2.1", "chip": "1.6L V6 → 2.1L V8",
    "say": "The cheap idea: take today's turbo V6 and bolt on two more cylinders. That gets you roughly two litres.",
    "hl": ["two more cylinders"]},
   {"kind": "big", "big": "200", "barTexts": ["350 kW", "200 kW"],
    "say": "Less electric power. Two hundred kilowatts instead of three hundred fifty.",
    "hl": ["Two hundred"]},
   {"kind": "big", "big": "+100", "chip": "+100 kW to overtake",
    "say": "A hundred kilowatts all the time, another hundred only for overtaking, like push to pass in IndyCar.",
    "hl": ["overtaking"]},
   {"kind": "big", "big": "−80", "chip": "−80 kg",
    "say": "The cars should lose eighty kilos. The FIA wants them under seven hundred.",
    "hl": ["eighty kilos"]},
   {"kind": "big", "big": "2031", "chip": "2031? · decision in December",
    "say": "Current rules run to the end of twenty thirty, so think twenty thirty-one. Nothing is signed yet.",
    "hl": ["twenty thirty-one", "Nothing is signed"]},
   {"kind": "end", "tag": "F1 rules news",
    "say": "What the FIA decides, you'll find on LapRadar."}
  ]
 }
}

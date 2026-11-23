# Расселл запускает академию GR63 (объявлено 12.11.2026). HQ-режим, Сильверстоун днём (theme day).
# Мини-болиды в студии (stage, s 0.4-0.5) дают ощущение детских картов, настоящих картов в студии нет.
# Цвета условные (синий), без логотипов и ливрей. Факты: см. tools/topics.md, раздел «Источники 23.11: GR63».
_BLU = {"c": "#1d4ed8", "a": "#e8ecf4", "p": "stripe"}
_ORG = {"c": "#f97316", "a": "#111827", "p": "band"}
_PAINT = {"0": _BLU, "1": _ORG}
_CV = {"type": "convoy", "at": 0.73, "n": 2, "v": 28}


def _grid(n, cols, s=0.42, gx=2.1, gz=2.6):
    out = []
    for i in range(n):
        r, c = divmod(i, cols)
        col = _BLU if i % 3 else _ORG
        out.append({"o": "f1", "c": col["c"], "a": col["a"], "p": col["p"], "x": round((c - (cols - 1) / 2) * gx, 2), "z": round((r - 0.5) * gz, 2), "ry": 0.3, "s": s})
    return out


VIDEO = {
 "slug": "gr63-karting-academy",
 "track": "silverstone",
 "coverText": {"ru": {"head": "Академия Расселла GR63", "sub": "Оплаченный картинг для детей 8–9 лет"}, "en": {"head": "Russell's GR63 Academy", "sub": "Funded karting for kids aged 8–9"}},
 "theme": "day",
 "hq": {"cars": [[_BLU["c"], _BLU["a"], _BLU["p"]], [_ORG["c"], _ORG["a"], _ORG["p"]]], "lampFade": True},
 "shots": [
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10.5, "h": 4.6, "h2": 4.0, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "act": {"type": "follow", "at": 0.3}},
  {"type": "carorbit", "car": 0, "r": 11, "r2": 10, "h": 2.2, "h2": 2.6, "a0": 0.4, "a1": 1.0, "fov": 48, "ly": 0.8, "act": {**_CV, "n": 1, "v": 22}},
  {"type": "side", "car": 0, "side": 7.5, "side2": 7, "h": 1.0, "h2": 1.3, "fw": 4, "fw2": -1, "look": 0.5, "ly": 0.9, "fov": 54, "act": {**_CV, "v": 26}},
  {"type": "stage", "items": _grid(6, 3, 0.42, 2.0, 2.6), "bg": "blue", "beams": True, "r": 6, "r2": 5.2, "h": 2.4, "h2": 2.8, "a0": -0.5, "a1": 0.3, "spin": 0.1, "ly": 0.5, "fov": 44, "pk": 1.0},
  {"type": "chase", "car": 0, "dist": 11, "dist2": 9.5, "h": 4.0, "h2": 3.4, "side": -1.2, "side2": 1.2, "look": 20, "drop": 3, "noCut": True, "act": {**_CV, "n": 1, "at": 0.6, "v": 30}},
  {"type": "chase", "car": 1, "dist": 13, "dist2": 11, "h": 5.5, "h2": 5, "side": 1.5, "side2": -1.5, "look": 22, "drop": 3, "noCut": True, "act": {"type": "follow", "at": 0.6}},
  {"type": "stage", "items": _grid(10, 5, 0.3, 1.4, 1.9), "bg": "gold", "beams": True, "r": 6.5, "r2": 5.5, "h": 2.4, "h2": 2.8, "a0": -0.4, "a1": 0.4, "spin": 0.1, "ly": 0.5, "fov": 46, "pk": 1.0},
  {"type": "stage", "items": [{"o": "f1", "c": _BLU["c"], "a": _BLU["a"], "p": _BLU["p"], "x": -1.3, "ry": 0.35, "s": 0.5}, {"o": "trophy", "x": 1.1, "y": 0, "s": 0.55}], "bg": "gold", "confetti": True, "r": 7, "r2": 6, "h": 2.2, "h2": 2.6, "a0": -0.4, "a1": 0.3, "spin": 0.05, "ly": 0.8},
  {"type": "orbit", "at": 0.75, "r": 430, "r2": 400, "h": 130, "h2": 110, "a0": 1.2, "a1": 1.35, "fov": 50, "act": {**_CV, "at": 0.72, "v": 40}}
 ],
 "coverShot": {"type": "chase", "car": 0, "dist": 10, "h": 3.6, "side": 1.5, "look": 18, "drop": 2.5, "fov": 46, "act": {"type": "follow", "at": 0.3}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 10, "h": 3.6, "side": 1.5, "look": 18, "drop": 2.5, "fov": 44, "act": {"type": "follow", "at": 0.3}}},
  {"name": "grid", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": _grid(10, 5, 0.4, 2.0, 2.4), "bg": "gold", "beams": True, "r": 8, "h": 2.8, "a0": 0.05, "spin": 0, "ly": 0.5, "fov": 46}},
  {"name": "side", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "side", "car": 0, "side": 6.5, "h": 1.1, "fw": 0.5, "look": 0.5, "ly": 0.9, "fov": 46, "act": {**_CV, "v": 30}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "chip": "≈ £1,5 млн · вернул отцу",
    "say": "Путь в Формулу стоит дорого: отец Расселла потратил около полутора миллионов фунтов, и Джордж всё вернул.",
    "hl": ["полутора", "миллионов"]},
   {"kind": "big", "chip": "GR63 · 12 ноября",
    "say": "Двенадцатого ноября Расселл запустил академию Джи-Ар шестьдесят три с Сильверстоуном и Британским клубом гонщиков.",
    "hl": ["академию", "Сильверстоуном"]},
   {"kind": "big", "chip": "Расселл · карт с 7 лет",
    "say": "Сам Расселл сел в карт в семь лет. Теперь ищет тех, кому не хватает денег на старт.",
    "hl": ["семь", "денег"]},
   {"kind": "big", "big": "8–9", "chip": "8–9 лет",
    "say": "Участвовать могут мальчики и девочки восьми и девяти лет, чьим семьям может не хватать бюджета на картинг.",
    "hl": ["восьми", "девяти"]},
   {"kind": "big", "big": "£25", "chip": "£25 · 6–31 декабря",
    "say": "Заезды на трассе Сильверстоуна с шестого по тридцать первое декабря, двадцать пять фунтов за заезд.",
    "hl": ["двадцать", "пять", "фунтов"]},
   {"kind": "big", "big": "80", "chip": "80 лучших → шоу-аут",
    "say": "Лучшие восемьдесят по итогам заездов выходят в шоу-аут в конце января.",
    "hl": ["восемьдесят", "шоу-аут"]},
   {"kind": "big", "big": "25", "chip": "25 мест · 2027",
    "say": "Двадцать пять мест в чемпионате две тысячи двадцать седьмого. Всё оплачено, вплоть до комбинезона и шлема.",
    "hl": ["Двадцать", "пять", "оплачено"]},
   {"kind": "big", "big": "2028", "chip": "Приз · сезон 2028",
    "say": "А победитель получит полностью оплаченный сезон в картинге на две тысячи двадцать восьмой год.",
    "hl": ["победитель", "оплаченный"]},
   {"kind": "end", "tag": "GR63 · 2027",
    "say": "Новости гонок и живая карта: ЛапРадар."}
  ],
  "en": [
   {"kind": "big", "chip": "≈ £1.5m · paid back",
    "say": "The road to Formula One is expensive: Russell's father spent about one and a half million pounds, and George paid it back.",
    "hl": ["one", "half", "million"]},
   {"kind": "big", "chip": "GR63 · 12 Nov",
    "say": "On the twelfth of November Russell launched the G R sixty-three academy with Silverstone and the BRDC.",
    "hl": ["academy", "Silverstone"]},
   {"kind": "big", "chip": "Russell · karting at 7",
    "say": "Russell himself got in a kart at seven. Now he's looking for kids whose families can't fund a start.",
    "hl": ["seven", "fund"]},
   {"kind": "big", "big": "8–9", "chip": "Ages 8–9",
    "say": "Boys and girls aged eight and nine can take part, if their family may lack the budget for karting.",
    "hl": ["eight", "nine"]},
   {"kind": "big", "big": "£25", "chip": "£25 · 6–31 Dec",
    "say": "Qualifiers at Silverstone run from the sixth to the thirty-first of December, twenty-five pounds a session.",
    "hl": ["twenty-five", "pounds"]},
   {"kind": "big", "big": "80", "chip": "Best 80 → shoot-out",
    "say": "The best eighty from the qualifiers go to a shoot-out at the end of January.",
    "hl": ["eighty", "shoot-out"]},
   {"kind": "big", "big": "25", "chip": "25 places · 2027",
    "say": "Twenty-five get places in the twenty twenty-seven championship. Everything is paid for, even the overalls and helmet.",
    "hl": ["Twenty-five", "paid"]},
   {"kind": "big", "big": "2028", "chip": "Prize · 2028 season",
    "say": "And the winner gets a fully funded karting season in twenty twenty-eight.",
    "hl": ["winner", "funded"]},
   {"kind": "end", "tag": "GR63 · 2027",
    "say": "Race news and the live map: LapRadar."}
  ]
 }
}

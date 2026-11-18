# Рё Хиракава: очко в дебютной гонке F1 и через неделю третий титул WEC. Камера (shots) общая для всех языков.
VIDEO = {
 "slug": "hirakawa-f1-point-wec-title",
 "track": "mexico-city",
 "theme": "day",
 "shots": [
  {"type": "chase", "car": 0, "dist": 13, "dist2": 10, "h": 5, "h2": 4.2, "side": -2.4, "side2": 2, "look": 20, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight"}},
  {"type": "chase", "car": 3, "dist": 14, "dist2": 11, "h": 5.5, "h2": 4.5, "side": 3, "side2": -2.5, "look": 30, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "t0": 7.1}},
  {"type": "chase", "car": 0, "dist": 14, "dist2": 11, "h": 5.5, "h2": 4.5, "side": -3, "side2": 2.5, "look": 20, "drop": 3, "noCut": True, "act": {"type": "duel"}},
  {"type": "stage", "items": [{"o": "f1", "c": "#f3f4f6"}], "bg": "blue", "r": 10, "r2": 9, "h": 2.4, "h2": 3.2, "a0": 0.9, "a1": -0.2, "spin": 0.3, "ly": 0.8},
  {"type": "stage", "items": [{"o": "podium"}, {"o": "trophy", "y": 2.2, "s": 0.6}], "confetti": True, "bg": "gold", "r": 14, "r2": 11, "h": 4, "h2": 4.5, "a0": -0.3, "a1": 0.3, "spin": 0, "ly": 2.2},
  {"type": "chase", "car": 1, "dist": 13, "dist2": 11, "h": 5, "h2": 4.5, "side": 2.5, "side2": -2, "look": 22, "drop": 3, "noCut": True, "act": {"type": "follow", "at": 0.5}},
  {"type": "fly", "from": 0.3, "to": 0.38, "h": 60, "h2": 140, "side": 40, "ahead": 260}
 ],
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 12, "h": 4.5, "side": -2.4, "look": 18, "drop": 3, "fov": 44, "act": {"type": "speed"}}},
  {"name": "duel", "w": 1200, "h": 800, "t": 1.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 9, "h": 3.6, "side": -2.4, "look": 12, "drop": 2, "fov": 40, "act": {"type": "duel"}}},
  {"name": "trophy", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "podium"}, {"o": "trophy", "y": 2.2, "s": 0.6}], "confetti": True, "bg": "gold", "r": 12, "h": 4, "ly": 2.2, "spin": 0}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "ОДНА НЕДЕЛЯ ХИРАКАВЫ", "sub": "очко в F1 и титул WEC",
    "say": "В воскресенье он набрал очко в первой же гонке Формулы один. Через неделю стал чемпионом мира. В другом чемпионате.",
    "hl": ["очко", "чемпионом мира"]},
   {"kind": "big", "big": "P19", "chip": "Мехико · старт P19",
    "say": "Рё Хиракаву позвали в Haas вместо Эстебана Окона прямо по ходу уик-энда в Мехико. Он стартовал девятнадцатым.",
    "hl": ["девятнадцатым"]},
   {"kind": "big", "big": "P13", "chip": "финиш P13",
    "say": "После последнего рестарта он прошёл обе машины Williams и доехал тринадцатым.",
    "hl": ["обе машины Williams"]},
   {"kind": "big", "big": "P10", "chip": "P13 → P10 · 1 очко",
    "say": "Потом стюарды наказали Пиастри, Гасли и Колапинто. Хиракава поднялся на десятое место, это очко в дебюте.",
    "hl": ["десятое место"]},
   {"kind": "big", "big": "3", "chip": "WEC · третий титул",
    "say": "Через неделю в Монце его Toyota номер восемь спокойно доехала до финиша, и это третий титул в WEC.",
    "hl": ["третьего титула"]},
   {"kind": "big", "big": "FP1", "chip": "Вегас · FP1",
    "say": "В Лас-Вегасе Хиракава снова сядет в Haas, в первой тренировке вместо Олли Бермана.",
    "hl": ["первой тренировке"]},
   {"kind": "end", "tag": "Результаты всех гонок",
    "say": "Протоколы гонок и все очки смотрите на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "HIRAKAWA'S WEEK", "sub": "an F1 point and a WEC title",
    "say": "On Sunday he scored a point in his first ever F1 race. A week later he was world champion. In another series.",
    "hl": ["a point", "world champion"]},
   {"kind": "big", "big": "P19", "chip": "Mexico · grid P19",
    "say": "Haas called Ryo Hirakawa up to replace Esteban Ocon in the middle of the Mexico weekend. He started nineteenth.",
    "hl": ["nineteenth"]},
   {"kind": "big", "big": "P13", "chip": "crossed the line P13",
    "say": "After the final restart he passed both Williams cars and crossed the line thirteenth.",
    "hl": ["both Williams"]},
   {"kind": "big", "big": "P10", "chip": "P13 → P10 · 1 point",
    "say": "Then the stewards penalised Piastri, Gasly and Colapinto. Hirakawa moved up to tenth, a point on debut.",
    "hl": ["tenth"]},
   {"kind": "big", "big": "3", "chip": "WEC · title no. 3",
    "say": "A week later at Monza his number eight Toyota just brought it home. That's a third WEC title.",
    "hl": ["third WEC title"]},
   {"kind": "big", "big": "FP1", "chip": "Vegas · FP1",
    "say": "In Las Vegas he's back in the Haas, in first practice instead of Ollie Bearman.",
    "hl": ["first practice"]},
   {"kind": "end", "tag": "Every race result",
    "say": "Full results and points are on LapRadar."}
  ]
 }
}

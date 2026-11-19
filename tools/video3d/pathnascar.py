# Путь в NASCAR: картинг и грунт, лейт-модели, ARCA, Truck Series, O'Reilly (бывшая Xfinity), Кубок. Камера (shots) общая для всех языков.
VIDEO = {
 "slug": "path-to-nascar",
 "track": "oval",
 "theme": "day",
 "shots": [
  {"type": "chase", "follow": "stock", "fi": 7, "dist": 13, "dist2": 11, "h": 5, "h2": 4.5, "side": 0, "side2": 0, "look": 30, "drop": 10, "noCut": True, "act": {"type": "stockpack", "at": 0.02}},
  {"type": "stage", "items": [{"o": "stock", "c": "#facc15", "n": 24, "s": 1.0}], "bg": "blue", "r": 12.5, "r2": 11, "h": 2.6, "h2": 3.4, "a0": -0.9, "a1": 0.3, "spin": 0.3, "ly": 0.9,
   "hud": {"type": "bars", "rows": [{"label": "ARC", "v": 15, "c": "#9fb4ff"}, {"label": "TRK", "v": 16, "c": "#5b9bff"}, {"label": "OAP", "v": 17, "c": "#3b82f6"}, {"label": "CUP", "v": 18, "c": "#facc15"}], "min": 12, "max": 18, "hi": 3}},
  {"type": "chase", "follow": "stock", "fi": 7, "dist": 14, "dist2": 11, "h": 6, "h2": 5, "side": 2, "side2": -1.5, "look": 40, "drop": 10, "noCut": True, "act": {"type": "stockpack", "at": 0.3, "pass": 1}},
  {"type": "chase", "follow": "stock", "fi": 7, "dist": 13, "dist2": 11, "h": 6, "h2": 5, "side": -1.5, "side2": 1.5, "look": 35, "drop": 10, "noCut": True, "act": {"type": "stockpack", "at": 0.15, "pass": 3}},
  {"type": "chase", "follow": "stock", "fi": 7, "dist": 12, "dist2": 14, "h": 6, "h2": 5, "side": -2, "side2": 2, "look": 45, "drop": 10, "noCut": True, "act": {"type": "stockpack", "at": 0.55, "pass": 6}},
  {"type": "stage", "items": [{"o": "stock", "c": "#3b82f6", "n": 24, "s": 1.0}], "confetti": True, "bg": "gold", "r": 12.5, "r2": 11, "h": 2.6, "h2": 3.4, "a0": 0.8, "a1": -0.3, "spin": 0.3, "ly": 0.9},
  {"type": "fly", "from": 0.0, "to": 0.08, "h": 60, "h2": 140, "side": -40, "ahead": 260}
 ],
 "coverShot": {"type": "chase", "follow": "stock", "fi": 7, "dist": 9, "h": 4, "side": 0, "look": 30, "drop": 0, "noCut": True, "act": {"type": "stockpack", "at": 0.02}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "stock", "fi": 7, "dist": 9, "h": 3.5, "side": -6.5, "look": 25, "drop": 2, "fov": 40, "act": {"type": "stockpack", "at": 0.02}}},
  {"name": "pack", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "stock", "fi": 7, "dist": 10, "h": 6, "side": 4, "look": 50, "drop": 3, "fov": 46, "act": {"type": "stockpack", "at": 0.25}}},
  {"name": "car", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "stock", "c": "#3b82f6", "n": 24, "s": 1.3}], "bg": "gold", "r": 12.5, "h": 2.6, "a0": 0.9, "spin": 0, "ly": 0.9, "beams": False}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "ПУТЬ В NASCAR", "chip": "симулятор → Daytona 500",
    "say": "Уильям Байрон до пятнадцати лет гонялся только в симуляторе. А потом выиграл Дайтону пятьсот.",
    "hl": ["в симуляторе", "Дайтону"]},
   {"kind": "list", "head": "Минимальный возраст", "items": ["ARCA 15", "Trucks 16", "Cup 18"],
    "say": "Ступеней в НАСКАР несколько, и на каждой свой возраст. АРКА с пятнадцати, Кубок только с восемнадцати.",
    "hl": ["пятнадцати", "восемнадцати"]},
   {"kind": "big", "big": "1", "chip": "картинг · грунт · Legends",
    "say": "Начинают с картинга, грунтовых овалов и маленьких машин Легендс. Кайл Ларсон вырос как раз на грунте.",
    "hl": ["грунтовых овалов", "Ларсон"]},
   {"kind": "big", "big": "2", "chip": "Late Models · шорт-треки",
    "say": "Дальше лейт-модели на местных шорт-треках. Многие там и остаются на всю карьеру.",
    "hl": ["лейт-модели"]},
   {"kind": "big", "big": "3", "chip": "ARCA 15 · Trucks 16",
    "say": "АРКА для многих первый суперспидвей. Потом грузовики, туда пускают с шестнадцати на коротких трассах.",
    "hl": ["суперспидвей", "шестнадцати"]},
   {"kind": "big", "big": "4", "chip": "O'Reilly · бывшая Xfinity",
    "say": "Вторая серия с этого года называется О'Райли. Байрон выиграл её новичком в семнадцатом и ушёл в Кубок.",
    "hl": ["О'Райли", "новичком"]},
   {"kind": "end", "tag": "NASCAR тоже здесь",
    "say": "Календарь и таблицу НАСКАР смотрите на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "THE ROAD TO NASCAR", "chip": "sim racing → Daytona 500",
    "say": "Until fifteen, William Byron raced only on a simulator. Later he won the Daytona five hundred.",
    "hl": ["simulator", "Daytona"]},
   {"kind": "list", "head": "Minimum age", "items": ["ARCA 15", "Trucks 16", "Cup 18"],
    "say": "NASCAR has several rungs, each with its own minimum age. ARCA from fifteen, the Cup only from eighteen.",
    "hl": ["fifteen", "eighteen"]},
   {"kind": "big", "big": "1", "chip": "karts · dirt · Legends",
    "say": "It starts with karts, dirt ovals and little Legends cars. Kyle Larson came straight off the dirt.",
    "hl": ["dirt ovals", "Larson"]},
   {"kind": "big", "big": "2", "chip": "Late Models · short tracks",
    "say": "Next come Late Models at local short tracks. Plenty of drivers stay there for their whole career.",
    "hl": ["Late Models"]},
   {"kind": "big", "big": "3", "chip": "ARCA 15 · Trucks 16",
    "say": "ARCA is where many first race on a superspeedway. Then the Trucks, open from sixteen on short tracks.",
    "hl": ["superspeedway", "sixteen"]},
   {"kind": "big", "big": "4", "chip": "O'Reilly · formerly Xfinity",
    "say": "The second tier is now the O'Reilly series. Byron won it as a rookie in twenty seventeen, then went Cup racing.",
    "hl": ["O'Reilly", "rookie"]},
   {"kind": "end", "tag": "NASCAR is here too",
    "say": "NASCAR calendar and standings are on LapRadar."}
  ]
 }
}

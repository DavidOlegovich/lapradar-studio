# Абу-Даби-2026: что решится в финале сезона. Данные «до Катара» (после Лас-Вегаса), чтобы текст оставался верным при любом итоге Катара.
# Антонелли чемпион с Мехико, 402; ВЕР 304, ХЭМ 267, РАС 264, НОР 264, ЛЕК 250 (макс. 50 очков: 25+25, спринтов нет, очка за быстрый круг нет с 2025).
# Кубок: Mercedes 666 (чемпион с Сан-Паулу), Ferrari 517, Red Bull 440, McLaren 431, Haas 31, Audi 28, Cadillac 0 (макс. 43 за гонку, 86 за два этапа).
# Окон уходит из Haas, Камара (дебют в Бразилии) и Берман (подтверждён 26.11) на 2027; сетка 2027 собрана. Гонка 6.12, уикенд 4-6.12, 58 кругов.
# Время сессий и время по городам НЕ называем. Источники: tools/topics.md («Источники 29.11: Абу-Даби, финал сезона»).
# Машины условные (синяя, оранжевая, бирюзовая), без ливрей и логотипов.
_BLUE = ["#1e40af", "#f8fafc", "stripe"]
_ORG = ["#f97316", "#111827", "band"]
_TEAL = ["#0f766e", "#e5e7eb", "split"]
_CV = {"type": "convoy", "at": "straight", "v": 62, "n": 3}
_TWO = [{"o": "f1", "c": _BLUE[0], "a": _BLUE[1], "p": _BLUE[2], "x": -2.3, "ry": 0.25},
        {"o": "f1", "c": _ORG[0], "a": _ORG[1], "p": _ORG[2], "x": 2.3, "ry": -0.25}]

VIDEO = {
 "slug": "abu-dhabi-2026-season-finale-stakes",
 "track": "yas-island",
 "theme": "dusk",
 "hq": {"cars": [_BLUE, _ORG, _TEAL]},
 "coverText": {"ru": {"head": "АБУ-ДАБИ: ФИНАЛ", "sub": "что ещё не решено"},
               "en": {"head": "ABU DHABI FINALE", "sub": "what is still open"}},
 "shots": [
  # 1 крючок
  {"type": "chase", "car": 0, "dist": 11, "dist2": 10, "h": 4.4, "h2": 4.2, "side": 0, "side2": 0, "look": 14, "drop": 2, "noCut": True, "act": {**_CV}},
  # 2 чемпион известен
  {"type": "carorbit", "car": 0, "r": 8.5, "r2": 7.5, "h": 1.4, "h2": 1.8, "a0": 0.5, "a1": 1.1, "fov": 46, "ly": 0.8, "act": {**_CV, "v": 30, "n": 2}},
  # 3 до 50 очков
  {"type": "chase", "car": 0, "dist": 11, "dist2": 9.5, "h": 4.2, "h2": 3.8, "side": -2.4, "side2": -1.6, "look": 12, "drop": 2, "noCut": True, "act": {"type": "duel"}},
  # 4 второе место
  {"type": "stage", "items": _TWO, "bg": "gold", "r": 12.5, "r2": 11, "h": 2.8, "h2": 3.4, "a0": 0.3, "a1": -0.3, "spin": 0.04, "ly": 0.6,
   "hud": {"type": "bars", "rows": [{"label": "VER", "v": 304, "c": "#3b5bdb"}, {"label": "HAM", "v": 267, "c": "#f97316"}, {"label": "RUS", "v": 264, "c": "#14b8a6"}], "min": 200, "max": 310}},
  # 5 места 3-6
  {"type": "chase", "car": 0, "dist": 10, "dist2": 9, "h": 3.8, "h2": 3.6, "side": 2.4, "side2": 1.6, "look": 11, "drop": 2, "noCut": True, "act": {"type": "duel"}},
  # 6 кубок конструкторов
  {"type": "chase", "car": 2, "dist": 14, "dist2": 13, "h": 5, "h2": 4.8, "side": 0, "side2": 0, "look": 20, "drop": 2, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 40, "n": 3}},
  # 7 состав на 2027
  {"type": "chase", "car": 0, "dist": 10, "dist2": 9, "h": 4.2, "h2": 3.9, "side": 1.8, "side2": 1.2, "look": 12, "drop": 2, "noCut": True, "act": {"type": "follow", "at": 0.3}},
  # 8 конец
  {"type": "chase", "car": 0, "dist": 26, "dist2": 28, "h": 10, "h2": 11, "side": -2, "side2": 0, "look": 30, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 55, "n": 3}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 9.5, "h": 1.4, "a0": 1.85, "a1": 1.85, "fov": 44, "act": {"type": "convoy", "at": "straight", "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 7.5, "h": 1.2, "a0": 2.1, "a1": 2.1, "fov": 40, "ly": 0.6, "act": {"type": "convoy", "at": "straight", "v": 1, "n": 2}}},
  {"name": "pack", "w": 1200, "h": 800, "t": 2.6, "u": 0.4,
   "shot": {"type": "carorbit", "car": 0, "r": 13, "h": 2.8, "a0": 0.55, "a1": 0.55, "fov": 48, "ly": 0.9, "act": {"type": "convoy", "at": "straight", "v": 40, "n": 3}}},
  {"name": "duel", "w": 1200, "h": 800, "t": 3.2, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 11, "h": 3.6, "side": 2.5, "look": 18, "drop": 2, "fov": 42, "act": {"type": "duel"}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "chip": "Абу-Даби · финал сезона",
    "say": "Чемпион уже известен. Так что же решится в Абу-Даби?",
    "hl": ["Чемпион", "решится"]},
   {"kind": "big", "chip": "Антонелли · 402 очка",
    "say": "Антонелли чемпион с Мехико, у него четыреста два очка. Остаются Катар и финал в Абу-Даби шестого декабря.",
    "hl": ["Антонелли", "четыреста"]},
   {"kind": "big", "big": "50", "chip": "Максимум 50 очков · без спринтов",
    "say": "Спринтов нет, очка за быстрый круг тоже. Значит, пилот может взять ещё максимум пятьдесят очков.",
    "hl": ["пятьдесят", "очков"]},
   {"kind": "big", "chip": "Второе место · после Лас-Вегаса",
    "say": "Второе место: у Ферстаппена триста четыре, у Хэмилтона двести шестьдесят семь, у Расселла и Норриса по двести шестьдесят четыре.",
    "hl": ["Ферстаппена", "Хэмилтона"]},
   {"kind": "big", "chip": "Места 2–6 · пятеро",
    "say": "Места со второго по шестое делят пятеро: Ферстаппен, Хэмилтон, Расселл, Норрис и Леклер. Пиастри уже не вмешается.",
    "hl": ["пятеро", "Пиастри"]},
   {"kind": "big", "chip": "Кубок конструкторов · +77 и +9",
    "say": "В Кубке конструкторов Феррари опережает Ред Булл на семьдесят семь очков, а за третье место Ред Булл и Макларен делят девять.",
    "hl": ["Феррари", "семьдесят", "девять"]},
   {"kind": "big", "chip": "Камара и Берман · Haas 2027",
    "say": "Окон уходит из Хаас. В следующем году там поедут Камара и Берман, сетка двадцать седьмого уже собрана.",
    "hl": ["Окон", "Камара", "Берман"]},
   {"kind": "end", "tag": "Абу-Даби · финал сезона",
    "say": "Во сколько гонка по вашему времени, смотрите на ЛапРадар.", "hl": ["вашему", "времени"]}
  ],
  "en": [
   {"kind": "big", "chip": "Abu Dhabi · season finale",
    "say": "The champion is already known. So what is left to decide in Abu Dhabi?",
    "hl": ["champion", "decide"]},
   {"kind": "big", "chip": "Antonelli · 402 points",
    "say": "Antonelli clinched in Mexico City and has four hundred and two points. Qatar and the Abu Dhabi finale on the sixth of December remain.",
    "hl": ["Antonelli", "four", "hundred"]},
   {"kind": "big", "big": "50", "chip": "50 points at most · no sprints",
    "say": "No sprints and no fastest lap point. So a driver can take fifty more points at most.",
    "hl": ["fifty", "points"]},
   {"kind": "big", "chip": "Second place · after Las Vegas",
    "say": "For second: Verstappen has three hundred and four, Hamilton two sixty-seven, Russell and Norris two sixty-four each.",
    "hl": ["Verstappen", "Hamilton"]},
   {"kind": "big", "chip": "P2 to P6 · five drivers",
    "say": "Places two to six go to five drivers: Verstappen, Hamilton, Russell, Norris and Leclerc. Piastri is out of the fight.",
    "hl": ["five", "Piastri"]},
   {"kind": "big", "chip": "Constructors · +77 and +9",
    "say": "In the constructors' table Ferrari lead Red Bull by seventy-seven points, and nine separate Red Bull and McLaren for third.",
    "hl": ["Ferrari", "seventy-seven", "nine"]},
   {"kind": "big", "chip": "Camara and Bearman · Haas 2027",
    "say": "Ocon leaves Haas. Next year Camara and Bearman drive there, and the twenty twenty-seven grid is complete.",
    "hl": ["Ocon", "Camara", "Bearman"]},
   {"kind": "end", "tag": "Abu Dhabi · season finale",
    "say": "Check what time the race starts in your own time zone on LapRadar.", "hl": ["your", "own", "time", "zone"]}
  ]
 }
}

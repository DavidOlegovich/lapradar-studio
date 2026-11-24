# NASCAR 2027: Уоткинс-Глен возвращается в Chase. Трассы Глена в студии нет, поэтому овал и сток-кары без привязки к конкретной трассе.
# Камера (shots) общая для всех языков.
VIDEO = {
 "slug": "watkins-glen-chase-2027",
 "track": "oval",
 "theme": "day",
 "hq": True,
 "shots": [
  {"type": "chase", "follow": "stock", "fi": 7, "dist": 13, "dist2": 11, "h": 5, "h2": 4.5, "side": 0, "side2": 0, "look": 30, "drop": 10, "noCut": True, "act": {"type": "stockpack", "at": 0.02}},
  {"type": "stage", "items": [{"o": "stock", "c": "#facc15", "n": 16, "s": 1.0}], "bg": "blue", "r": 12.5, "r2": 11, "h": 2.6, "h2": 3.4, "a0": -0.9, "a1": 0.3, "spin": 0.3, "ly": 0.9},
  {"type": "chase", "follow": "stock", "fi": 7, "dist": 14, "dist2": 11, "h": 6, "h2": 5, "side": 2, "side2": -1.5, "look": 40, "drop": 10, "noCut": True, "act": {"type": "stockpack", "at": 0.3, "pass": 1}},
  {"type": "chase", "follow": "stock", "fi": 7, "dist": 13, "dist2": 11, "h": 6, "h2": 5, "side": -1.5, "side2": 1.5, "look": 35, "drop": 10, "noCut": True, "act": {"type": "stockpack", "at": 0.15, "pass": 3}},
  {"type": "chase", "follow": "stock", "fi": 7, "dist": 12, "dist2": 14, "h": 6, "h2": 5, "side": -2, "side2": 2, "look": 45, "drop": 10, "noCut": True, "act": {"type": "stockpack", "at": 0.55, "pass": 6}},
  {"type": "stage", "items": [{"o": "stock", "c": "#3b82f6", "n": 19, "s": 1.0}], "bg": "gold", "r": 12.5, "r2": 11, "h": 2.6, "h2": 3.4, "a0": 0.8, "a1": -0.3, "spin": 0.3, "ly": 0.9},
  {"type": "fly", "from": 0.0, "to": 0.08, "h": 60, "h2": 140, "side": -40, "ahead": 260}
 ],
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "stock", "fi": 7, "dist": 9, "h": 3.5, "side": -6.5, "look": 25, "drop": 2, "fov": 40, "act": {"type": "stockpack", "at": 0.02}}},
  {"name": "pack", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "stock", "fi": 7, "dist": 10, "h": 6, "side": 4, "look": 50, "drop": 3, "fov": 46, "act": {"type": "stockpack", "at": 0.25}}},
  {"name": "car", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "stock", "c": "#3b82f6", "n": 19, "s": 1.3}], "bg": "gold", "r": 12.5, "h": 2.6, "a0": 0.9, "spin": 0, "ly": 0.9, "beams": False}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "ШОССЕЙНАЯ ГОНКА ВЕРНЁТСЯ В CHASE", "chip": "Уоткинс-Глен · 2027",
    "say": "В плей-офф НАСКАР почти одни овалы. Но в две тысячи двадцать седьмом в нём снова будет шоссейная трасса.",
    "hl": ["овалы", "шоссейная"]},
   {"kind": "big", "big": "16", "chip": "Chase · 10 гонок · 16 пилотов",
    "say": "Чейз это последние десять гонок сезона. В нём шестнадцать лучших по очкам и никто не выбывает.",
    "hl": ["десять", "шестнадцать"]},
   {"kind": "list", "head": "Chase 2027", "items": ["Ричмонд 11 сент.", "Глен 19 сент.", "Хомстед 14 нояб."],
    "say": "Откроет Чейз Ричмонд. Вторым этапом Уоткинс-Глен, девятнадцатого сентября, а финал снова в Хомстеде.",
    "hl": ["Ричмонд", "девятнадцатого сентября", "Хомстеде"]},
   {"kind": "big", "big": "0", "chip": "Chase 2026 · 0 шоссейных",
    "say": "В Чейзе этого года шоссейных трасс не было. Шарлотт в октябре вернулся с Ровала на овал.",
    "hl": ["не было", "овал"]},
   {"kind": "big", "big": "1", "chip": "Глен · шоссейная в Chase",
    "say": "В расписании двадцать седьмого года в плей-офф есть Уоткинс-Глен, шоссейная гонка. Раскладка Шарлотта пока не названа.",
    "hl": ["шоссейная гонка", "не названа"]},
   {"kind": "big", "big": "2024", "chip": "в плей-офф · 2024",
    "say": "Последний раз Глен был в плей-офф в две тысячи двадцать четвёртом. Теперь он возвращается.",
    "hl": ["две тысячи двадцать четвёртом", "возвращается"]},
   {"kind": "end", "tag": "NASCAR тоже здесь",
    "say": "Календарь и таблицу НАСКАР смотрите на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "A ROAD COURSE RETURNS TO THE CHASE", "chip": "Watkins Glen · 2027",
    "say": "NASCAR's playoff is almost all ovals. But in twenty twenty seven it gets a road course again.",
    "hl": ["ovals", "road course"]},
   {"kind": "big", "big": "16", "chip": "Chase · 10 races · 16 drivers",
    "say": "The Chase is the last ten races of the season. Sixteen drivers qualify on points and nobody gets eliminated.",
    "hl": ["ten", "Sixteen"]},
   {"kind": "list", "head": "Chase 2027", "items": ["Richmond Sep 11", "The Glen Sep 19", "Homestead Nov 14"],
    "say": "Richmond opens the Chase. Watkins Glen is the second race, on September nineteenth, and the finale is back at Homestead.",
    "hl": ["Richmond", "September nineteenth", "Homestead"]},
   {"kind": "big", "big": "0", "chip": "Chase 2026 · 0 road courses",
    "say": "This year's Chase had no road courses. Charlotte went back from the Roval to the oval in October.",
    "hl": ["no road courses", "oval"]},
   {"kind": "big", "big": "1", "chip": "The Glen · road course in the Chase",
    "say": "On the twenty twenty seven schedule, the playoff includes Watkins Glen, a road course race. Charlotte's layout hasn't been named yet.",
    "hl": ["road course", "hasn't been named"]},
   {"kind": "big", "big": "2024", "chip": "last in the Chase · 2024",
    "say": "The Glen was last in the playoff in twenty twenty four. Now it's coming back.",
    "hl": ["twenty twenty four", "coming back"]},
   {"kind": "end", "tag": "NASCAR is here too",
    "say": "NASCAR calendar and standings are on LapRadar."}
  ]
 }
}

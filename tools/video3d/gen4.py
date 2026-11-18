# Формула E Gen4: тесты в Хараме и самая быстрая машина серии. Камера (shots) общая для всех языков.
VIDEO = {
 "slug": "formula-e-gen4-first-test",
 "track": "mexico-city",
 "theme": "day",
 "shots": [
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 6, "h2": 5.5, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight"}},
  {"type": "stage", "items": [{"o": "f1", "c": "#06b6d4"}], "bg": "blue", "r": 10, "r2": 9, "h": 2.4, "h2": 3.2, "a0": 0.9, "a1": -0.2, "spin": 0.3, "ly": 0.8,
   "hud": {"type": "bars", "rows": [{"label": "RACE", "v": 450, "c": "#9fb4ff"}, {"label": "MAX", "v": 600, "c": "#facc15"}, {"label": "REC", "v": 700, "c": "#22c55e"}], "min": 0, "max": 720, "hi": 1}},
  {"type": "chase", "car": 0, "dist": 11, "dist2": 10, "h": 4.5, "h2": 4.2, "side": 1.5, "side2": 1, "look": 10, "drop": 3, "noCut": True, "act": {"type": "energy"}, "hud": {"type": "battery"}},
  {"type": "chase", "car": 0, "dist": 14, "dist2": 11, "h": 5.5, "h2": 4.5, "side": -3, "side2": 2.5, "look": 20, "drop": 3, "noCut": True, "act": {"type": "duel"}},
  {"type": "stage", "items": [{"o": "f1", "c": "#06b6d4", "x": -2.3, "ry": 0.25}, {"o": "f1", "c": "#f3f4f6", "x": 2.3, "ry": -0.25}], "bg": "blue", "r": 13, "r2": 11, "h": 3, "h2": 4, "a0": -0.4, "a1": 0.3, "spin": 0.1, "ly": 0.6},
  {"type": "chase", "car": 1, "dist": 14, "dist2": 12, "h": 6, "h2": 5, "side": 1.5, "side2": -1.5, "look": 25, "drop": 3, "noCut": True, "act": {"type": "follow", "at": 0.5}},
  {"type": "fly", "from": 0.3, "to": 0.38, "h": 60, "h2": 140, "side": 40, "ahead": 260}
 ],
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 3, "dist": 10, "h": 4.2, "side": -2.4, "look": 30, "drop": 3, "fov": 44, "act": {"type": "convoy", "at": "straight"}}},
  {"name": "studio", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "f1", "c": "#06b6d4", "x": -2.3, "ry": 0.25}, {"o": "f1", "c": "#f3f4f6", "x": 2.3, "ry": -0.25}], "bg": "blue", "r": 12, "h": 3, "a0": -0.2, "spin": 0, "ly": 0.6}},
  {"name": "duel", "w": 1200, "h": 800, "t": 1.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 9, "h": 3.6, "side": -2.4, "look": 12, "drop": 2, "fov": 40, "act": {"type": "duel"}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "GEN4 ВЫЕХАЛА", "sub": "новая Формула E",
    "say": "Формула E на этой неделе впервые выпустила на трассу Gen4. Это самая мощная машина в её истории.",
    "hl": ["Gen4", "самая мощная"]},
   {"kind": "big", "big": "600", "chip": "600 кВт · больше 800 л.с.",
    "say": "В гонке четыреста пятьдесят киловатт, в режиме атаки и в квалификации шестьсот. Это больше восьмисот сил.",
    "hl": ["шестьсот"]},
   {"kind": "big", "big": "700", "chip": "рекуперация до 700 кВт",
    "say": "А при торможении она возвращает в батарею до семисот киловатт. Тормоза работают как генератор.",
    "hl": ["семисот"]},
   {"kind": "big", "big": "4×4", "chip": "постоянный полный привод",
    "say": "Впервые в серии постоянный полный привод. Ведут все четыре колеса, всю гонку.",
    "hl": ["полный привод"]},
   {"kind": "big", "big": "4,4", "chip": "0–200 км/ч · 4,4 с",
    "say": "До двухсот километров в час Gen4 разгоняется за четыре и четыре десятых секунды.",
    "hl": ["четыре и четыре"]},
   {"kind": "big", "big": "21", "chip": "Мехико · 16 января",
    "say": "Первая гонка шестнадцатого января в Мехико. В сезоне двадцать одна гонка и двенадцать команд.",
    "hl": ["Мехико", "двадцать одна"]},
   {"kind": "end", "tag": "Формула E тоже здесь",
    "say": "Календарь Формулы E смотрите на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "GEN4 IS OUT", "sub": "the new Formula E",
    "say": "This week Formula E put its Gen4 car on track for official testing. It's the most powerful car the series has ever had.",
    "hl": ["Gen4", "most powerful"]},
   {"kind": "big", "big": "600", "chip": "600 kW · 800+ hp",
    "say": "Four hundred fifty kilowatts in the race, six hundred in attack mode and qualifying. That's over eight hundred horsepower.",
    "hl": ["six hundred"]},
   {"kind": "big", "big": "700", "chip": "up to 700 kW regen",
    "say": "Under braking it puts up to seven hundred kilowatts back into the battery. The brakes work as a generator.",
    "hl": ["seven hundred"]},
   {"kind": "big", "big": "4×4", "chip": "permanent all-wheel drive",
    "say": "For the first time the series has permanent all-wheel drive. All four wheels drive, all race long.",
    "hl": ["all-wheel drive"]},
   {"kind": "big", "big": "4.4", "chip": "0–200 km/h · 4.4 s",
    "say": "Gen4 gets from zero to two hundred kilometres an hour in four point four seconds.",
    "hl": ["four point four"]},
   {"kind": "big", "big": "21", "chip": "Mexico City · Jan 16",
    "say": "The first race is in Mexico City on January sixteenth. Twenty-one races and twelve teams this season.",
    "hl": ["Mexico City", "Twenty-one"]},
   {"kind": "end", "tag": "Formula E is here too",
    "say": "The Formula E calendar is on LapRadar."}
  ]
 }
}

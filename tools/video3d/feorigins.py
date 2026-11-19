# Как создавалась Формула E: салфетка 2011 года, Пекин 2014, смена машин в Gen1, Gen2, Gen3 и Gen4 на тестах. Камера (shots) общая для всех языков.
VIDEO = {
 "slug": "formula-e-origins",
 "track": "shanghai",
 "theme": "day",
 "shots": [
  {"type": "chase", "car": 1, "dist": 13, "dist2": 12, "h": 6.5, "h2": 6, "side": 0, "side2": 0, "look": 25, "drop": 6.5, "noCut": True, "act": {"type": "follow", "at": 0.3}},
  {"type": "stage", "items": [{"o": "f1", "c": "#06b6d4"}], "bg": "blue", "r": 10, "r2": 9, "h": 2.4, "h2": 3.2, "a0": 0.9, "a1": -0.2, "spin": 0.3, "ly": 0.8},
  {"type": "chase", "car": 0, "dist": 13, "dist2": 11, "h": 5.5, "h2": 5, "side": 0, "side2": 1.5, "look": 20, "drop": 6.5, "noCut": True, "act": {"type": "duel"}},
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10, "h": 4.5, "h2": 4, "side": 2.5, "side2": -2, "look": 20, "drop": 5, "noCut": True, "act": {"type": "pit", "car": 0, "box": 0.4, "stop": 2.0, "band": "#06b6d4"}},
  {"type": "stage", "items": [{"o": "f1", "c": "#06b6d4", "x": -2.3, "ry": 0.25}, {"o": "f1", "c": "#f3f4f6", "x": 2.3, "ry": -0.25}], "bg": "blue", "r": 14.5, "r2": 12.5, "h": 3, "h2": 4, "a0": -0.4, "a1": 0.3, "spin": 0.1, "ly": 0.6,
   "hud": {"type": "bars", "rows": [{"label": "G2", "v": 250, "c": "#9fb4ff"}, {"label": "G3", "v": 350, "c": "#5b9bff"}, {"label": "G4", "v": 600, "c": "#facc15"}], "min": 0, "max": 620, "hi": 2}},
  {"type": "chase", "car": 1, "dist": 14, "dist2": 12, "h": 6, "h2": 5, "side": 0.5, "side2": -0.5, "look": 25, "drop": 6.5, "noCut": True, "act": {"type": "convoy", "at": "straight", "t0": 6}},
  {"type": "fly", "from": 0.02, "to": 0.1, "h": 60, "h2": 140, "side": 40, "ahead": 260}
 ],
 "coverShot": {"type": "stage", "items": [{"o": "f1", "c": "#06b6d4", "x": -2.3, "ry": 0.25}, {"o": "f1", "c": "#f3f4f6", "x": 2.3, "ry": -0.25}], "bg": "blue", "r": 9, "h": 4, "a0": 0.2, "spin": 0, "ly": 3.2},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 10, "h": 4, "side": -3.5, "look": 12, "drop": 3, "fov": 44, "act": {"type": "energy"}}},
  {"name": "duel", "w": 1200, "h": 800, "t": 1.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 9, "h": 3.6, "side": -2.4, "look": 12, "drop": 2, "fov": 40, "act": {"type": "duel"}}},
  {"name": "gens", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "f1", "c": "#06b6d4", "x": -2.3, "ry": 0.25}, {"o": "f1", "c": "#f3f4f6", "x": 2.3, "ry": -0.25}], "bg": "blue", "r": 12, "h": 3, "a0": -0.2, "spin": 0, "ly": 0.6}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "КАК РОДИЛАСЬ ФОРМУЛА E", "chip": "Gen1 · две машины на гонку",
    "say": "В первых гонках Формулы E пилот посреди заезда выпрыгивал из машины и пересаживался в другую.",
    "hl": ["пересаживался"]},
   {"kind": "big", "big": "2011", "chip": "Париж · 3 марта 2011",
    "say": "Началось всё с салфетки: в марте одиннадцатого года в Париже серию набросали Жан Тодт и Алехандро Агаг.",
    "hl": ["салфетки", "Жан Тодт"]},
   {"kind": "big", "big": "2014", "chip": "Пекин · 13.09.2014",
    "say": "Первая гонка в Пекине, сентябрь четырнадцатого. Прост и Хайдфельд бьются в последнем повороте, побеждает ди Грасси.",
    "hl": ["Пекине", "ди Грасси"]},
   {"kind": "big", "big": "4", "chip": "сезоны 1–4 · смена машин",
    "say": "Батареи на гонку не хватало, и в середине пилоты меняли машину. Так прошли четыре сезона.",
    "hl": ["меняли машину", "четыре сезона"]},
   {"kind": "big", "big": "600", "chip": "Gen2 2018 · Gen3 2023",
    "barTexts": ["250 кВт", "350 кВт", "600 кВт"],
    "say": "Gen2 проехала всю гонку на одной батарее. Gen3 получила передний мотор и обошлась без задних гидравлических тормозов.",
    "hl": ["одной батарее", "гидравлических тормозов"]},
   {"kind": "big", "big": "1:24", "chip": "Gen4 · Мехико 16.01.2027",
    "say": "Gen4 уже на тестах: Мортара проехал круг за минуту двадцать четыре. Первая гонка шестнадцатого января в Мехико.",
    "hl": ["Мортара", "Мехико"]},
   {"kind": "end", "tag": "Формула E тоже здесь",
    "say": "Смотрите календарь Формулы E на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "HOW FORMULA E WAS BORN", "chip": "Gen1 · two cars per race",
    "say": "In early Formula E, drivers jumped out of their car mid-race and climbed into a second one.",
    "hl": ["second one"]},
   {"kind": "big", "big": "2011", "chip": "Paris · 3 March 2011",
    "say": "It started on a napkin: in Paris, March twenty eleven, Jean Todt and Alejandro Agag sketched the series.",
    "hl": ["napkin", "Jean Todt"]},
   {"kind": "big", "big": "2014", "chip": "Beijing · 13 Sep 2014",
    "say": "First race: Beijing, September twenty fourteen. Prost and Heidfeld crash at the last corner, di Grassi wins.",
    "hl": ["Beijing", "di Grassi"]},
   {"kind": "big", "big": "4", "chip": "seasons 1–4 · car swaps",
    "say": "One battery couldn't last a race, so drivers swapped cars halfway. That went on for four seasons.",
    "hl": ["swapped cars", "four seasons"]},
   {"kind": "big", "big": "600", "chip": "Gen2 2018 · Gen3 2023",
    "barTexts": ["250 kW", "350 kW", "600 kW"],
    "say": "Gen2 went the full distance on one battery. Gen3 added a front motor and dropped rear hydraulic brakes.",
    "hl": ["one battery", "hydraulic brakes"]},
   {"kind": "big", "big": "1:24", "chip": "Gen4 · Mexico City · Jan 16",
    "say": "Gen4 is testing now, Mortara lapped in one twenty-four. It races first in Mexico City on January sixteenth.",
    "hl": ["Mortara", "Mexico City"]},
   {"kind": "end", "tag": "Formula E is here too",
    "say": "The Formula E calendar is on LapRadar."}
  ]
 }
}

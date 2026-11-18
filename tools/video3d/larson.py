# Кайл Ларсон: третий титул NASCAR и первый дубль с 2010 года. Камера (shots) общая для всех языков.
# Сток-кары: act bikes + follow bike с отрицательной dist (камера впереди мотоциклов, в кадре только сток-кары).
VIDEO = {
 "slug": "larson-third-nascar-title",
 "track": "oval",
 "theme": "day",
 "shots": [{"type": "chase", "follow": "stock", "fi": 7, "dist": 12, "dist2": 9, "h": 4, "h2": 3.5, "side": -3, "side2": 2, "look": 30, "drop": 2, "act": {"type": "stockpack", "at": 0.02}}, {"type": "chase", "follow": "stock", "fi": 7, "dist": 14, "dist2": 10, "h": 6, "h2": 4, "side": 3, "side2": -2, "look": 40, "drop": 2, "act": {"type": "stockpack", "at": 0.3, "pass": 1}}, {"type": "stage", "items": [{"o": "trophy", "x": -2.6, "s": 0.8}, {"o": "trophy", "x": 0, "s": 0.8}, {"o": "trophy", "x": 2.6, "s": 0.8}], "confetti": True, "bg": "gold", "r": 12, "r2": 10, "h": 3, "h2": 3.6, "a0": -0.3, "a1": 0.3, "spin": 0, "ly": 2.6, "hud": {"type": "bars", "rows": [{"label": "JOH", "v": 7, "c": "#9fb4ff"}, {"label": "GOR", "v": 4, "c": "#9fb4ff"}, {"label": "LAR", "v": 3, "c": "#facc15"}], "min": 0, "max": 8, "hi": 2}}, {"type": "orbit", "r": 420, "r2": 340, "h": 170, "h2": 130, "a0": 1.0, "a1": 1.5, "at": 0.0, "act": {"type": "stockpack", "at": 0.0}}, {"type": "chase", "follow": "stock", "fi": 7, "dist": 10, "dist2": 14, "h": 7, "h2": 5, "side": 4, "side2": -3, "look": 50, "drop": 3, "act": {"type": "stockpack", "at": 0.55, "pass": 6}}, {"type": "stage", "items": [{"o": "stock", "c": "#3b82f6", "n": 5, "s": 1.3}], "confetti": True, "bg": "blue", "r": 11, "r2": 9, "h": 2.6, "h2": 3.4, "a0": -0.9, "a1": 0.3, "spin": 0.3, "ly": 0.9}, {"type": "fly", "from": 0.0, "to": 0.08, "h": 60, "h2": 140, "side": -40, "ahead": 260}],
 "images": [{"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5, "shot": {"type": "chase", "follow": "stock", "fi": 7, "dist": 12, "h": 4, "side": -3, "look": 30, "drop": 2, "fov": 44, "act": {"type": "stockpack", "at": 0.02}}}, {"name": "pack", "w": 1200, "h": 800, "t": 2.0, "u": 0.5, "shot": {"type": "chase", "follow": "stock", "fi": 7, "dist": 10, "h": 6, "side": 4, "look": 50, "drop": 3, "fov": 46, "act": {"type": "stockpack", "at": 0.25}}}, {"name": "close", "w": 1200, "h": 800, "t": 2.0, "u": 0.5, "shot": {"type": "stage", "items": [{"o": "trophy", "x": -2.6, "s": 0.8}, {"o": "trophy", "x": 0, "s": 0.8}, {"o": "trophy", "x": 2.6, "s": 0.8}], "confetti": True, "bg": "gold", "r": 11, "h": 3, "ly": 2.6, "spin": 0}}],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "ТРЕТИЙ ТИТУЛ ЛАРСОНА", "sub": "чемпион NASCAR два года подряд",
    "say": "Двенадцатое место в финальной гонке, и он всё равно чемпион НАСКАР. Уже третий раз.",
    "hl": ["Двенадцатое", "третий"]},
   {"kind": "big", "big": "2", "chip": "2025 + 2026",
    "say": "Кайл Ларсон взял титул второй год подряд. Такого в НАСКАР не было с две тысячи десятого, со времён Джимми Джонсона.",
    "hl": ["второй год подряд", "Джимми Джонсона"]},
   {"kind": "big", "big": "3", "barTexts": ["7", "4", "3"],
    "say": "У него три титула. Больше только у Петти, Эрнхардта, Джонсона и Гордона.",
    "hl": ["три титула"]},
   {"kind": "big", "big": "67", "chip": "+67 очков до финала",
    "say": "В Хомстед он приехал с запасом в шестьдесят семь очков, и ему хватило очков за первый сегмент.",
    "hl": ["шестьдесят семь"]},
   {"kind": "big", "big": "10", "chip": "Чейз · 10 гонок",
    "say": "В плей-офф из десяти гонок он выиграл три и восемь раз финишировал в десятке.",
    "hl": ["три", "восемь"]},
   {"kind": "big", "big": "34", "chip": "34 года · Hendrick",
    "say": "Ему тридцать четыре. Для Hendrick Motorsports это шестнадцатый титул в Кубке.",
    "hl": ["шестнадцатый"]},
   {"kind": "end", "tag": "NASCAR тоже здесь",
    "say": "Календарь и таблицу НАСКАР смотрите на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "LARSON'S THIRD TITLE", "sub": "back-to-back NASCAR champion",
    "say": "Twelfth in the final race, and he's still the NASCAR champion. For the third time.",
    "hl": ["Twelfth", "third time"]},
   {"kind": "big", "big": "2", "chip": "2025 + 2026",
    "say": "Kyle Larson won it two years in a row. NASCAR hadn't seen that since Jimmie Johnson in twenty ten.",
    "hl": ["two years in a row", "Jimmie Johnson"]},
   {"kind": "big", "big": "3", "barTexts": ["7", "4", "3"],
    "say": "That's three titles. Only Petty, Earnhardt, Johnson and Gordon have more.",
    "hl": ["three titles"]},
   {"kind": "big", "big": "67", "chip": "+67 pts before the finale",
    "say": "He arrived at Homestead sixty-seven points clear, and the first stage was enough to seal it.",
    "hl": ["sixty-seven"]},
   {"kind": "big", "big": "10", "chip": "Chase · 10 races",
    "say": "In the ten-race Chase he won three times and finished in the top ten eight times.",
    "hl": ["three", "eight"]},
   {"kind": "big", "big": "34", "chip": "age 34 · Hendrick",
    "say": "He's thirty-four. For Hendrick Motorsports it's a sixteenth Cup title.",
    "hl": ["sixteenth"]},
   {"kind": "end", "tag": "NASCAR is here too",
    "say": "NASCAR calendar and standings are on LapRadar."}
  ]
 }
}

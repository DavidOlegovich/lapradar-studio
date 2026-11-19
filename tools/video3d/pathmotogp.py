# Путь в MotoGP: минибайки и Talent Cup, Red Bull Rookies Cup и JuniorGP, Moto3, Moto2, MotoGP. Камера (shots) общая для всех языков.
VIDEO = {
 "slug": "path-to-motogp",
 "track": "spielberg",
 "theme": "day",
 "shots": [
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 8, "dist2": 6.5, "h": 3, "h2": 2.8, "side": 0, "side2": 0, "look": 20, "drop": 6, "noCut": True, "act": {"type": "motogp", "at": 0.12}},
  {"type": "stage", "items": [{"o": "bike", "c": "#f97316", "lean": 0.3, "s": 1.1}], "bg": "blue", "r": 10, "r2": 9, "h": 2.4, "h2": 3, "a0": 0.9, "a1": -0.2, "spin": 0.3, "ly": 0.9,
   "hud": {"type": "bars", "rows": [{"label": "TC", "v": 14, "c": "#9fb4ff"}, {"label": "RBR", "v": 15, "c": "#5b9bff"}, {"label": "JGP", "v": 16, "c": "#3b82f6"}, {"label": "GP", "v": 18, "c": "#facc15"}], "min": 11, "max": 18, "hi": 3}},
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 14, "dist2": 10, "h": 6, "h2": 4.5, "side": 2.5, "side2": -2, "look": 30, "drop": 6, "noCut": True, "act": {"type": "motogp", "at": 0.4}},
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 7, "dist2": 8, "h": 2.8, "h2": 3.2, "side": 2, "side2": -1.5, "look": 18, "drop": 6, "noCut": True, "act": {"type": "motogp", "at": 0.55, "pass": 1}},
  {"type": "stage", "items": [{"o": "bike", "c": "#3b82f6", "x": -1.8, "lean": 0.3, "s": 0.9}, {"o": "bike", "c": "#e10600", "x": 1.8, "lean": -0.3, "s": 1.1}], "bg": "red", "r": 9.5, "r2": 8.5, "h": 2.6, "h2": 3, "a0": -0.4, "a1": 0.3, "spin": 0.1, "ly": 0.9},
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 11, "dist2": 9, "h": 4.2, "h2": 3.8, "side": -2, "side2": 1.8, "look": 22, "drop": 6, "noCut": True, "act": {"type": "motogp", "at": 0.8}},
  {"type": "stage", "items": [{"o": "bike", "c": "#f97316", "x": -1.6, "lean": 0.35, "s": 1.0}, {"o": "trophy", "x": 1.8, "s": 0.8}], "confetti": True, "bg": "gold", "r": 11, "r2": 9.5, "h": 2.6, "h2": 3, "a0": 0.5, "a1": -0.3, "spin": 0, "ly": 1.4}
 ],
 "coverShot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 8, "h": 2.6, "side": 0, "look": 30, "drop": -5, "noCut": True, "act": {"type": "motogp", "at": 0.12}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 6, "h": 2.4, "side": -3, "look": 16, "drop": 1.5, "fov": 42, "act": {"type": "motogp", "at": 0.12}}},
  {"name": "pack", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 8, "h": 3.4, "side": 2.5, "look": 20, "drop": 2, "fov": 42, "act": {"type": "motogp", "at": 0.4}}},
  {"name": "bikes", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "bike", "c": "#3b82f6", "x": -1.8, "lean": 0.3, "s": 0.9}, {"o": "bike", "c": "#e10600", "x": 1.8, "lean": -0.3, "s": 1.1}], "bg": "red", "r": 6.5, "h": 1.8, "a0": -0.2, "spin": 0, "ly": 0.8}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "ПУТЬ В MOTOGP", "chip": "Акоста · чемпион в 17",
    "say": "Педро Акоста выиграл Мото три в семнадцать, в первом же сезоне. Вот его лестница.",
    "hl": ["семнадцать", "первом же сезоне"]},
   {"kind": "list", "head": "Минимальный возраст", "items": ["Talent Cup 14", "Rookies 15", "Moto3 18"],
    "say": "Талент Кап с четырнадцати лет, Рукис с пятнадцати, чемпионат мира только с восемнадцати.",
    "hl": ["четырнадцати", "восемнадцати"]},
   {"kind": "big", "big": "14", "chip": "минибайки → Talent Cup",
    "say": "Начинают на минибайках, потом национальные Талент Капы. Туда берут с четырнадцати.",
    "hl": ["минибайках", "Талент Капы"]},
   {"kind": "big", "big": "17", "chip": "Rookies · JuniorGP · топ-3 → Moto3",
    "say": "Дальше Рукис Кап Ред Булла или ДжуниорДжиПи. Тройку лучших пускают в Мото три уже в семнадцать.",
    "hl": ["Тройку лучших", "в семнадцать"]},
   {"kind": "big", "big": "60", "chip": "Moto3 60 л.с. · Moto2 138",
    "say": "В Мото три один цилиндр и шестьдесят сил. В Мото два мотор Триумф на сто тридцать восемь.",
    "hl": ["шестьдесят", "сто тридцать восемь"]},
   {"kind": "big", "big": "250", "chip": "MotoGP · больше 250 л.с.",
    "say": "А в МотоДжиПи больше двухсот пятидесяти сил. Акоста дошёл сюда в двадцать четвёртом, через титул в Мото два.",
    "hl": ["двухсот пятидесяти", "Мото два"]},
   {"kind": "end", "tag": "MotoGP тоже здесь",
    "say": "Все три класса МотоДжиПи смотрите на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "THE ROAD TO MOTOGP", "chip": "Acosta · champion at 17",
    "say": "Pedro Acosta won Moto3 at seventeen, in his very first season. Here's the ladder he climbed.",
    "hl": ["seventeen", "first season"]},
   {"kind": "list", "head": "Minimum age", "items": ["Talent Cup 14", "Rookies 15", "Moto3 18"],
    "say": "Talent Cup from age fourteen, Rookies from fifteen, the world championship only from eighteen.",
    "hl": ["fourteen", "eighteen"]},
   {"kind": "big", "big": "14", "chip": "minibikes → Talent Cup",
    "say": "It starts on minibikes, then the national Talent Cups. You can join those at fourteen.",
    "hl": ["minibikes", "Talent Cups"]},
   {"kind": "big", "big": "17", "chip": "Rookies · JuniorGP · top 3 → Moto3",
    "say": "Next is the Red Bull Rookies Cup or JuniorGP. The top three can step up to Moto3 at seventeen.",
    "hl": ["top three", "seventeen"]},
   {"kind": "big", "big": "60", "chip": "Moto3 60 hp · Moto2 138",
    "say": "Moto3 has one cylinder and sixty horsepower. Moto2 runs a Triumph triple with a hundred thirty-eight.",
    "hl": ["sixty", "a hundred thirty-eight"]},
   {"kind": "big", "big": "250", "chip": "MotoGP · 250+ hp",
    "say": "MotoGP bikes make over two hundred fifty. Acosta got there in twenty twenty-four, after winning Moto2.",
    "hl": ["two hundred fifty", "Moto2"]},
   {"kind": "end", "tag": "MotoGP is here too",
    "say": "All three MotoGP classes are on LapRadar."}
  ]
 }
}

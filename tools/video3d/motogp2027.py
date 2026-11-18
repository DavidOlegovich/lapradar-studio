# MotoGP 2027: 850 кубов, без «приседа» и с шинами Pirelli. Камера (shots) общая для всех языков.
VIDEO = {
 "slug": "motogp-2027-850cc-rules",
 "track": "lusail",
 "theme": "night",
 "shots": [
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 7, "dist2": 5, "h": 2.8, "h2": 2.4, "side": -2.2, "side2": 1.8, "look": 20, "drop": 2, "act": {"type": "motogp", "at": 0.12}},
  {"type": "stage", "items": [{"o": "bike", "c": "#e10600", "lean": 0.0, "s": 1.2}], "bg": "red", "r": 9.5, "r2": 9, "h": 2.2, "h2": 2.8, "a0": 0.9, "a1": -0.3, "spin": 0.3, "ly": 0.9,
   "hud": {"type": "bars", "rows": [{"label": "2026", "v": 1000, "c": "#9fb4ff"}, {"label": "2027", "v": 850, "c": "#facc15"}], "min": 0, "max": 1050, "hi": 1}},
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 6, "dist2": 8, "h": 2.6, "h2": 3.2, "side": 2.2, "side2": -1.6, "look": 18, "drop": 2, "act": {"type": "motogp", "at": 0.02}},
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 8, "dist2": 6.5, "h": 3.2, "h2": 2.8, "side": 2.4, "side2": -2, "look": 22, "drop": 2, "noCut": True, "act": {"type": "motogp", "at": 0.12}},
  {"type": "stage", "items": [{"o": "bike", "c": "#f97316", "x": -1.6, "lean": 0.35, "s": 1.0}, {"o": "bike", "c": "#3b82f6", "x": 1.6, "lean": -0.35, "s": 1.0}], "bg": "blue", "r": 10, "r2": 8.5, "h": 2.6, "h2": 3, "a0": 0.5, "a1": -0.3, "spin": 0, "ly": 1.0},
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 8, "dist2": 6, "h": 3, "h2": 2.6, "side": -2, "side2": 2, "look": 22, "drop": 2, "act": {"type": "motogp", "at": 0.6, "pass": 1}},
  {"type": "fly", "from": 0.0, "to": 0.08, "h": 60, "h2": 140, "side": -40, "ahead": 260}
 ],
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 7, "h": 2.8, "side": -2.2, "look": 20, "drop": 2, "fov": 42, "act": {"type": "motogp", "at": 0.12}}},
  {"name": "start", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 14, "h": 6, "side": 3, "look": 30, "drop": 3, "fov": 44, "act": {"type": "motogp", "at": 0.02}}},
  {"name": "lean", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 6, "h": 2.6, "side": 2.2, "look": 18, "drop": 2, "fov": 42, "act": {"type": "motogp", "at": 0.55}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "MotoGP 2027", "sub": "меньше мотор, меньше крыльев",
    "say": "Через год мотоциклы МотоДжиПи станут медленнее. И это сделано нарочно.",
    "hl": ["медленнее", "нарочно"]},
   {"kind": "big", "big": "850", "barTexts": ["1000 см³", "850 см³"],
    "say": "Объём мотора уменьшат с тысячи до восьмисот пятидесяти кубов. Цилиндров по-прежнему четыре.",
    "hl": ["восьмисот пятидесяти"]},
   {"kind": "big", "big": "0", "chip": "без «приседа» на старте",
    "say": "Устройства, которые опускают мотоцикл на старте и на выходе из поворота, запретят полностью.",
    "hl": ["запретят полностью"]},
   {"kind": "big", "big": "−50", "chip": "обтекатель −50 мм",
    "say": "Аэродинамику урежут: передний обтекатель станет уже на пять сантиметров, нос сдвинут назад.",
    "hl": ["пять сантиметров"]},
   {"kind": "big", "big": "20", "chip": "бак 22 → 20 л",
    "say": "Бак уменьшат до двадцати литров, а топливо будет полностью экологичным. Моторов на сезон шесть вместо семи.",
    "hl": ["двадцати литров", "шесть"]},
   {"kind": "big", "big": "P", "chip": "Michelin → Pirelli",
    "say": "И шины другие: вместо Michelin единым поставщиком станет Pirelli.",
    "hl": ["Pirelli"]},
   {"kind": "end", "tag": "MotoGP тоже здесь",
    "say": "Календарь и таблицу МотоДжиПи смотрите на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "MotoGP 2027", "sub": "smaller engines, less aero",
    "say": "In a year, MotoGP bikes will get slower. And that's the whole point.",
    "hl": ["slower", "whole point"]},
   {"kind": "big", "big": "850", "barTexts": ["1000 cc", "850 cc"],
    "say": "Engines shrink from a thousand to eight hundred fifty cc. Still four cylinders.",
    "hl": ["eight hundred fifty"]},
   {"kind": "big", "big": "0", "chip": "no ride-height devices",
    "say": "The devices that drop the bike at the start and out of corners are banned completely.",
    "hl": ["banned completely"]},
   {"kind": "big", "big": "−50", "chip": "fairing −50 mm",
    "say": "Less aero too: the front fairing gets five centimetres narrower and the nose moves back.",
    "hl": ["five centimetres"]},
   {"kind": "big", "big": "20", "chip": "tank 22 → 20 L",
    "say": "The tank drops to twenty litres and the fuel goes fully sustainable. Six engines a season instead of seven.",
    "hl": ["twenty litres", "Six"]},
   {"kind": "big", "big": "P", "chip": "Michelin → Pirelli",
    "say": "New tyres as well: Pirelli replaces Michelin as the single supplier.",
    "hl": ["Pirelli"]},
   {"kind": "end", "tag": "MotoGP is here too",
    "say": "MotoGP calendar and standings are on LapRadar."}
  ]
 }
}

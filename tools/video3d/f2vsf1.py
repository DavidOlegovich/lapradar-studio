# Чем Формула 2 отличается от Формулы 1. Камера (shots) общая для всех языков.
VIDEO = {
 "slug": "f2-vs-f1-differences",
 "track": "yas-island",
 "theme": "dusk",
 "shots": [
  {"type": "chase", "car": 1, "dist": 13, "dist2": 12, "h": 6.5, "h2": 6, "side": 0, "side2": 0, "look": 25, "drop": 3, "noCut": True, "act": {"type": "follow", "at": 0.3}},
  {"type": "stage", "items": [{"o": "f1", "c": "#f3f4f6", "x": -2.3, "ry": 0.25}, {"o": "f1", "c": "#f3f4f6", "x": 2.3, "ry": -0.25}], "bg": "blue", "r": 13, "r2": 11, "h": 3, "h2": 4, "a0": -0.4, "a1": 0.3, "spin": 0.1, "ly": 0.6},
  {"type": "stage", "items": [{"o": "f1", "c": "#1e3a8a"}], "bg": "red", "r": 10, "r2": 9, "h": 2.4, "h2": 3.2, "a0": 0.9, "a1": -0.2, "spin": 0.3, "ly": 0.8,
   "hud": {"type": "bars", "rows": [{"label": "F1", "v": 1000, "c": "#e10600"}, {"label": "F2", "v": 620, "c": "#5b9bff"}], "min": 0, "max": 1050, "hi": 1}},
  {"type": "chase", "car": 0, "dist": 13, "dist2": 11, "h": 5.5, "h2": 5, "side": 0, "side2": 1.5, "look": 20, "drop": 3, "noCut": True, "act": {"type": "duel"}},
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10, "h": 4.5, "h2": 4, "side": 2.5, "side2": -2, "look": 20, "drop": 3, "noCut": True, "act": {"type": "pit", "car": 0, "box": 0.4, "stop": 2.0, "band": "#f3f4f6"}},
  {"type": "stage", "items": [{"o": "podium"}, {"o": "trophy", "y": 2.2, "s": 0.6}], "confetti": True, "bg": "gold", "r": 14, "r2": 11, "h": 4, "h2": 4.5, "a0": -0.3, "a1": 0.3, "spin": 0, "ly": 2.2},
  {"type": "fly", "from": 0.6, "to": 0.68, "h": 60, "h2": 140, "side": 40, "ahead": 260}
 ],
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 3, "dist": 10, "h": 4.2, "side": -2.4, "look": 30, "drop": 3, "fov": 44, "act": {"type": "convoy", "at": "straight"}}},
  {"name": "duel", "w": 1200, "h": 800, "t": 1.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 9, "h": 3.6, "side": -2.4, "look": 12, "drop": 2, "fov": 40, "act": {"type": "duel"}}},
  {"name": "same", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "f1", "c": "#f3f4f6", "x": -2.3, "ry": 0.25}, {"o": "f1", "c": "#1e3a8a", "x": 2.3, "ry": -0.25}], "bg": "blue", "r": 12, "h": 3, "a0": -0.2, "spin": 0, "ly": 0.6}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "F2 ИЛИ F1?", "sub": "в чём разница",
    "say": "Формула два едет в те же выходные и на тех же трассах, что Формула один. Но это совсем другие гонки.",
    "hl": ["совсем другие"]},
   {"kind": "big", "big": "1", "chip": "одна машина на всех · Dallara",
    "say": "Машина у всех одна и та же, от Даллары. Побеждает пилот, а не завод.",
    "hl": ["одна и та же"]},
   {"kind": "big", "big": "620", "chip": "F2 ≈620 л.с. · F1 ≈1000",
    "say": "Мотор три и четыре литра, V6 с турбиной, около шестисот двадцати сил. У Формулы один около тысячи.",
    "hl": ["шестисот двадцати", "тысячи"]},
   {"kind": "big", "big": "10", "chip": "спринт · реверс топ-10",
    "say": "В субботу спринт, и первая десятка квалификации стартует наоборот. Быстрейший уходит десятым.",
    "hl": ["наоборот", "десятым"]},
   {"kind": "big", "big": "1", "chip": "главная гонка · 1 пит-стоп",
    "say": "В воскресенье главная гонка. Хотя бы один пит-стоп и оба состава шин обязательны.",
    "hl": ["один пит-стоп"]},
   {"kind": "big", "big": "25", "chip": "главная 25 · спринт 10",
    "say": "За главную гонку дают двадцать пять очков, за спринт десять. Титул решат Катар и Абу-Даби.",
    "hl": ["двадцать пять", "Абу-Даби"]},
   {"kind": "end", "tag": "F2 тоже здесь",
    "say": "Таблицу Формулы два смотрите на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "F2 OR F1?", "sub": "what's the difference",
    "say": "Formula Two races on the same weekends and the same tracks as Formula One. But it's a very different game.",
    "hl": ["very different"]},
   {"kind": "big", "big": "1", "chip": "one car for all · Dallara",
    "say": "Everyone drives the same Dallara chassis. The driver makes the difference, not the factory.",
    "hl": ["same Dallara"]},
   {"kind": "big", "big": "620", "chip": "F2 ≈620 hp · F1 ≈1000",
    "say": "A three point four litre turbo V6 with about six hundred twenty horsepower. Formula One has around a thousand.",
    "hl": ["six hundred twenty", "a thousand"]},
   {"kind": "big", "big": "10", "chip": "sprint · top 10 reversed",
    "say": "Saturday is the sprint, and the top ten from qualifying start in reverse. The fastest starts tenth.",
    "hl": ["reverse", "tenth"]},
   {"kind": "big", "big": "1", "chip": "feature race · 1 pit stop",
    "say": "Sunday is the feature race. At least one pit stop and both tyre compounds are mandatory.",
    "hl": ["one pit stop"]},
   {"kind": "big", "big": "25", "chip": "feature 25 · sprint 10",
    "say": "A feature win pays twenty-five points, a sprint win ten. Qatar and Abu Dhabi will decide the title.",
    "hl": ["twenty-five", "Abu Dhabi"]},
   {"kind": "end", "tag": "F2 is here too",
    "say": "Formula Two standings are on LapRadar."}
  ]
 }
}

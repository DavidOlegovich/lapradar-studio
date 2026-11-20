# Сетка F1 2027: 21 место из 22 занято, свободно одно, в Haas рядом с Рафаэлом Камарой (на 20.11.2026; Cadillac подтвердил Боттаса 18.11).
# «Все команды за 40 секунд»: HQ, Монца вечером, стартовая прямая и пит-лейн. Машины в условных цветах команд (shot "paint"), без логотипов и настоящих ливрей.
# Плашки HUD bars: по 2–3 команды на сцену, у каждой два кода пилотов; место в Haas подсвечено и помечено «?». Камера (shots) общая для всех языков.
_T = {
 "MCL": {"c": "#ff8000", "a": "#111827", "p": "band"},
 "MER": {"c": "#c7ccd4", "a": "#14b8a6", "p": "fade"},
 "RBR": {"c": "#1e2a5a", "a": "#ef4444", "p": "split"},
 "FER": {"c": "#d61f1f", "a": "#f8fafc", "p": "stripe"},
 "AMR": {"c": "#0e5a43", "a": "#b5e61d", "p": "band"},
 "WIL": {"c": "#1f4fd6", "a": "#f8fafc", "p": "fade"},
 "ALP": {"c": "#1d6fe0", "a": "#ff5fb0", "p": "split"},
 "AUD": {"c": "#6b7280", "a": "#e11d48", "p": "band"},
 "RB":  {"c": "#e8ecf2", "a": "#2563eb", "p": "split"},
 "CAD": {"c": "#15171c", "a": "#c3c8d0", "p": "stripe"},
 "HAA": {"c": "#f3f4f6", "a": "#111827", "p": "band"},
}
def _paint(*teams): return {str(k): _T[t] for k, t in enumerate(teams)}
def _bars(*teams, hi=None, half=None):   # half: строка, где бар заполнен наполовину (одно место из двух свободно)
    h = {"type": "bars", "rows": [{"label": t, "v": 0.5 if k == half else 1, "c": _T[t]["c"] if t != "CAD" else "#9aa3ad"} for k, t in enumerate(teams)], "min": 0, "max": 1}
    if hi is not None: h["hi"] = hi
    return h
_CV = {"type": "convoy", "at": "straight", "n": 4, "v": 60}

VIDEO = {
 "slug": "f1-2027-grid-one-seat-left",
 "track": "monza",
 "theme": "dusk",
 "hq": {"street": True},
 "shots": [
  {"type": "chase", "car": 3, "dist": 13, "dist2": 11, "h": 5, "h2": 4.2, "side": 0, "side2": 1.2, "look": 30, "drop": 3, "noCut": True, "paint": _paint("MCL", "FER", "RBR", "MER"), "act": {**_CV}},
  {"type": "side", "car": 0, "side": 6.5, "side2": 6, "h": 1.0, "h2": 1.3, "fw": 2.5, "fw2": -1.5, "look": 0.5, "ly": 0.9, "fov": 52, "paint": _paint("MCL", "MER", "RBR"),
   "hud": _bars("MCL", "MER", "RBR"), "act": {**_CV, "v": 40, "n": 3}},
  {"type": "carorbit", "car": 0, "r": 10.5, "r2": 9.5, "h": 2.4, "h2": 1.7, "a0": 0.7, "a1": 1.3, "fov": 48, "ly": 0.8, "paint": _paint("FER", "AMR", "WIL"),
   "hud": _bars("FER", "AMR", "WIL"), "act": {**_CV, "v": 24, "n": 1, "t0": 2}},
  {"type": "chase", "car": 0, "dist": 11, "dist2": 9.5, "h": 4.2, "h2": 3.6, "side": -1.2, "side2": 1.2, "look": 20, "drop": 3, "noCut": True, "paint": _paint("ALP", "AUD", "RB", "WIL"),
   "hud": _bars("ALP", "AUD", "RB"), "act": {**_CV, "t0": 3}},
  {"type": "side", "car": 0, "side": -6.5, "side2": -6, "h": 1.0, "h2": 1.3, "fw": 0.5, "fw2": 2.5, "look": 0.5, "ly": 0.9, "fov": 52, "paint": _paint("CAD", "HAA"),
   "hud": _bars("CAD", "HAA", hi=1, half=1), "act": {**_CV, "v": 40, "n": 2}},
  {"type": "carorbit", "car": 0, "r": 9.5, "r2": 8.5, "h": 1.6, "h2": 2.2, "a0": -0.9, "a1": -0.2, "fov": 46, "ly": 0.8, "paint": _paint("HAA"), "act": {**_CV, "v": 18, "n": 1, "t0": 1}},
  {"type": "stage", "items": [{"o": "f1", "c": _T["HAA"]["c"], "a": _T["HAA"]["a"], "p": _T["HAA"]["p"]}], "bg": "red", "r": 10.5, "r2": 9.5, "h": 2.4, "h2": 3.2, "a0": 0.9, "a1": -0.2, "spin": 0.3, "ly": 0.8},
  {"type": "fly", "from": 0.0, "to": 0.06, "h": 70, "h2": 150, "side": 40, "ahead": 260}
 ],
 "coverShot": {"type": "chase", "car": 3, "dist": 12, "h": 3.4, "side": 1.5, "look": 24, "drop": 2, "fov": 44, "paint": _paint("MCL", "FER", "RBR", "HAA"), "act": {**_CV, "v": 6}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 3, "dist": 12, "h": 3.2, "side": 1.6, "look": 24, "drop": 2, "fov": 42, "paint": _paint("MCL", "FER", "RBR", "HAA"), "act": {**_CV, "v": 6}}},
  {"name": "pack", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 3, "dist": 30, "h": 12, "side": 3, "look": 30, "drop": 3, "fov": 46, "paint": _paint("MER", "ALP", "AMR", "WIL"), "act": {**_CV, "v": 30}}},
  {"name": "haas", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 9, "h": 1.5, "a0": -0.5, "a1": -0.5, "fov": 42, "ly": 0.8, "paint": _paint("HAA"), "act": {**_CV, "v": 1, "n": 1}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "СЕТКА F1 2027", "chip": "2027 · занято 21 из 22",
    "say": "Сетка Формулы один на двадцать седьмой почти собрана: свободно одно кресло из двадцати двух.",
    "hl": ["одно"]},
   {"kind": "big", "big": "MCL", "chip": "Ферстаппен · до 2030",
    "barTexts": ["NOR · PIA", "RUS · ANT", "VER · HAD"],
    "say": "Макларен: Норрис и Пиастри. Мерседес: Расселл и Антонелли. Ред Булл: Ферстаппен до тридцатого года и Аджар.",
    "hl": ["тридцатого"]},
   {"kind": "big", "big": "FER", "chip": "Алонсо · ещё сезон",
    "barTexts": ["LEC · HAM", "ALO · STR", "SAI · ALB"],
    "say": "Феррари: Леклер и Хэмилтон. Астон Мартин: Алонсо остаётся, рядом Стролл. Уильямс: Сайнс и Албон.",
    "hl": ["Алонсо"]},
   {"kind": "big", "big": "ALP", "chip": "Без перемен",
    "barTexts": ["GAS · COL", "HUL · BOR", "LAW · LIN"],
    "say": "Альпин: Гасли и Колапинто. Ауди: Хюлькенберг и Бортолето. Рейсинг Буллз оставили Лоусона и Линдблада.",
    "hl": ["Лоусона", "Линдблада"]},
   {"kind": "big", "big": "HAA", "chip": "Haas: CAM + ?",
    "barTexts": ["PER · BOT", "CAM · ?"],
    "say": "Кадиллак только что оставил Боттаса рядом с Пересом. В Хаасе есть Камара, второе место свободно.",
    "hl": ["свободно"]},
   {"kind": "big", "big": "?", "chip": "Фаворит: Берман?",
    "say": "По данным прессы, фаворит Оливер Берман: у Хааса есть опция на его контракт.",
    "hl": ["Берман"]},
   {"kind": "big", "big": "1", "chip": "Камара вместо Окона",
    "say": "Если Бермана оставят, новичок будет один: Рафаэл Камара вместо Эстебана Окона.",
    "hl": ["один"]},
   {"kind": "end", "tag": "Сетка F1 2027",
    "say": "Пилотов и команды сезона смотрите в таблицах на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "F1 GRID 2027", "chip": "2027 · 21 of 22 filled",
    "say": "The twenty twenty-seven F1 grid is almost done. Just one seat out of twenty-two is still open.",
    "hl": ["one"]},
   {"kind": "big", "big": "MCL", "chip": "Verstappen · to 2030",
    "barTexts": ["NOR · PIA", "RUS · ANT", "VER · HAD"],
    "say": "McLaren: Norris and Piastri. Mercedes: Russell and Antonelli. Red Bull: Verstappen, signed to twenty thirty, with Hadjar.",
    "hl": ["thirty"]},
   {"kind": "big", "big": "FER", "chip": "Alonso · one more year",
    "barTexts": ["LEC · HAM", "ALO · STR", "SAI · ALB"],
    "say": "Ferrari: Leclerc and Hamilton. Aston Martin: Alonso stays on with Stroll. Williams: Sainz and Albon.",
    "hl": ["Alonso"]},
   {"kind": "big", "big": "ALP", "chip": "No changes",
    "barTexts": ["GAS · COL", "HUL · BOR", "LAW · LIN"],
    "say": "Alpine: Gasly and Colapinto. Audi: Hulkenberg and Bortoleto. Racing Bulls kept Lawson and Lindblad.",
    "hl": ["Lawson", "Lindblad"]},
   {"kind": "big", "big": "HAA", "chip": "Haas: CAM + ?",
    "barTexts": ["PER · BOT", "CAM · ?"],
    "say": "Cadillac has just kept Bottas alongside Perez. Haas has Camara, and the other seat is open.",
    "hl": ["open"]},
   {"kind": "big", "big": "?", "chip": "Favourite: Bearman?",
    "say": "Reports name Oliver Bearman as favourite: Haas holds an option on his deal.",
    "hl": ["Bearman"]},
   {"kind": "big", "big": "1", "chip": "Camara replaces Ocon",
    "say": "If Bearman stays, there's only one new face: Rafael Camara in for Esteban Ocon.",
    "hl": ["one"]},
   {"kind": "end", "tag": "F1 grid 2027",
    "say": "Find every driver and team in the LapRadar standings."}
  ]
 }
}

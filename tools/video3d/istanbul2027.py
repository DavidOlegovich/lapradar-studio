# Турция возвращается в F1: Истанбул Парк в календаре 2027–2031 (контракт объявлен 24.04.2026, дата 3 октября 2027; календарь 16.09.2026).
# HQ, трасса istanbul (контур из bacinger/f1-circuits, MIT; собрана tools/geojson_track.py, высот и зданий нет), дневной свет.
# Поворот 8 (≈0,43–0,52 круга): пролёт сверху и проезд за машиной. 2020: дождь и промежуточные шины (зелёная полоса), 2021: влажно.
# Машины в условных цветах, без логотипов и ливрей команд. Камера (shots) общая для всех языков.
_RED = {"c": "#d61f1f", "a": "#f8fafc", "p": "band"}      # условная красная (Турция в цветах флага, без символов)
_SIL = {"c": "#c7ccd4", "a": "#14b8a6", "p": "fade"}      # условная серебряная (Mercedes 2020–2021, без логотипов)
_CV = {"type": "convoy", "at": "straight", "n": 2, "v": 60}

VIDEO = {
 "slug": "turkish-gp-istanbul-returns-2027",
 "track": "istanbul",
 "theme": "day",
 "hq": True,
 "shots": [
  {"type": "chase", "car": 0, "dist": 13, "dist2": 11, "h": 5, "h2": 4.2, "side": 0, "side2": 1.2, "look": 30, "drop": 3, "noCut": True, "paint": {"0": _RED, "1": _SIL}, "act": {**_CV}},
  {"type": "side", "car": 0, "side": 6.5, "side2": 6, "h": 1.0, "h2": 1.3, "fw": 2.5, "fw2": -1.5, "look": 0.5, "ly": 0.9, "fov": 52, "paint": {"0": _RED}, "act": {**_CV, "v": 40, "n": 1}},
  {"type": "flyby", "car": 0, "side": 8, "h": 1.4, "mid": 0.55, "fov": 40, "fov2": 30, "ly": 0.8, "paint": {"0": _RED, "1": _SIL}, "act": {**_CV, "v": 55}},
  {"type": "orbit", "at": 0.467, "r": 430, "r2": 360, "h": 330, "h2": 260, "a0": 0.4, "a1": 1.0, "fov": 55},
  {"type": "carorbit", "car": 0, "r": 11, "r2": 10, "h": 1.8, "h2": 2.4, "a0": 0.7, "a1": 1.3, "fov": 48, "ly": 0.9, "paint": {"0": _RED}, "act": {"type": "convoy", "at": 0.44, "n": 1, "v": 30}},
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10.5, "h": 4.5, "h2": 4, "side": 0, "look": 24, "drop": 3, "noCut": True, "rain": True, "band": "#22c55e", "paint": {"0": _SIL, "1": _RED}, "act": {**_CV}},
  {"type": "side", "car": 0, "side": -6.5, "side2": -6, "h": 1.0, "h2": 1.3, "fw": 0.5, "fw2": 2.5, "look": 0.5, "ly": 0.9, "fov": 52, "rain": {"k": 0.15, "spray": False}, "paint": {"0": _SIL}, "act": {**_CV, "v": 40, "n": 1}},
  {"type": "stage", "items": [{"o": "f1", "c": "#d61f1f", "a": "#f8fafc", "p": "stripe"}, {"o": "trophy", "x": 2.4, "y": 0, "s": 0.55}], "bg": "red", "r": 11, "r2": 9.5, "h": 2.6, "h2": 3.4, "a0": 0.9, "a1": -0.1, "spin": 0.2, "ly": 0.9},
  {"type": "fly", "from": 0.02, "to": 0.08, "h": 70, "h2": 150, "side": 40, "ahead": 260}
 ],
 "coverShot": {"type": "chase", "car": 0, "dist": 11, "h": 3.4, "side": 0, "look": 20, "drop": 2, "fov": 46, "paint": {"0": _RED, "1": _SIL}, "act": {**_CV, "v": 8}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 8.5, "h": 1.8, "a0": 2.4, "a1": 2.4, "fov": 42, "ly": 0.6, "paint": {"0": _RED}, "act": {**_CV, "n": 1, "v": 1}}},
  {"name": "turn8", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 34, "h": 16, "side": 6, "look": 40, "drop": 4, "fov": 48, "paint": {"0": _RED, "1": _SIL}, "act": {"type": "convoy", "at": 0.455, "n": 2, "v": 2}}},
  {"name": "wet", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "side", "car": 0, "side": 6, "h": 1.1, "fw": 0.5, "look": 0.5, "ly": 0.9, "fov": 46, "rain": True, "band": "#22c55e", "paint": {"0": _SIL}, "act": {**_CV, "v": 40, "n": 1}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "СТАМБУЛ ВОЗВРАЩАЕТСЯ", "chip": "Турция · F1 · 2027",
    "say": "Турция возвращается в Формулу один! Истанбул Парк снова в календаре с двадцать седьмого года.",
    "hl": ["возвращается"]},
   {"kind": "big", "big": "5", "chip": "Контракт · 2027–2031",
    "say": "Контракт на пять сезонов, до тридцать первого года. Первая гонка пройдёт третьего октября.",
    "hl": ["пять", "октября"]},
   {"kind": "big", "big": "3", "chip": "Баку → Стамбул → Сингапур",
    "say": "Стамбул встанет в середину тройки гонок подряд: Баку, Стамбул и Сингапур.",
    "hl": ["Стамбул"]},
   {"kind": "big", "big": "8", "chip": "Поворот 8 · 4 апекса",
    "say": "Главная легенда трассы: восьмой поворот. Длинная скоростная левая дуга с четырьмя апексами.",
    "hl": ["восьмой", "четырьмя"]},
   {"kind": "big", "big": "14", "chip": "5,338 км · 14 поворотов",
    "say": "Круг пять и три десятых километра, четырнадцать поворотов, и едут против часовой стрелки.",
    "hl": ["против"]},
   {"kind": "big", "big": "7", "chip": "2020 · Хэмилтон · 7-й титул",
    "say": "В двадцатом году на мокрой скользкой трассе Хэмилтон стартовал шестым, выиграл и взял седьмой титул.",
    "hl": ["седьмой"]},
   {"kind": "big", "big": "2021", "chip": "2021 · Боттас P1",
    "say": "Последнюю гонку здесь, в двадцать первом, выиграл с поула Валттери Боттас. Трасса снова была влажной.",
    "hl": ["Боттас"]},
   {"kind": "big", "big": "3", "chip": "Масса · 2006–2008",
    "say": "А рекордсмен Стамбула Фелипе Масса: три победы подряд за Феррари.",
    "hl": ["три"]},
   {"kind": "end", "tag": "Стамбул · 3 октября 2027",
    "say": "Турецкий этап смотрите на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "ISTANBUL IS BACK", "chip": "Turkey · F1 · 2027",
    "say": "Turkey is coming back to Formula One! Istanbul Park returns to the calendar in twenty twenty-seven.",
    "hl": ["back", "returns"]},
   {"kind": "big", "big": "5", "chip": "Deal · 2027–2031",
    "say": "A five-season deal, through twenty thirty-one. The first race is on the third of October.",
    "hl": ["five-season", "October"]},
   {"kind": "big", "big": "3", "chip": "Baku → Istanbul → Singapore",
    "say": "Istanbul sits in the middle of a triple header: Baku, Istanbul, then Singapore.",
    "hl": ["Istanbul"]},
   {"kind": "big", "big": "8", "chip": "Turn 8 · 4 apexes",
    "say": "The star of the lap is Turn Eight. A long, fast left-hander with four apexes.",
    "hl": ["Eight", "four"]},
   {"kind": "big", "big": "14", "chip": "5.338 km · 14 turns",
    "say": "The lap is five point three kilometres with fourteen corners, and it runs anti-clockwise.",
    "hl": ["anti-clockwise"]},
   {"kind": "big", "big": "7", "chip": "2020 · Hamilton · title 7",
    "say": "In twenty twenty, on a wet and slippery track, Hamilton started sixth, won, and took his seventh title.",
    "hl": ["seventh"]},
   {"kind": "big", "big": "2021", "chip": "2021 · Bottas P1",
    "say": "The last race here, in twenty twenty-one, went to Valtteri Bottas from pole. The track was damp again.",
    "hl": ["Bottas"]},
   {"kind": "big", "big": "3", "chip": "Massa · 2006–2008",
    "say": "And Istanbul's record man is Felipe Massa: three wins in a row for Ferrari.",
    "hl": ["three"]},
   {"kind": "end", "tag": "Istanbul · 3 October 2027",
    "say": "Follow the Turkish round on the LapRadar live map."}
  ]
 }
}

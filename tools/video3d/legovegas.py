# LEGO и Лас-Вегас: розовый кабриолет из кубиков на подиуме 2025, кирпичные болиды перед гонкой 2026, команда в F1 Academy.
# Кинематографичный ролик: ночной Вегас, светящаяся Sphere, огни на фасадах, машины в кирпичном стиле студии (shot "brick").
# Логотипов и фигурок LEGO нет: только кубики как форма. Камера (shots) общая для всех языков.
_PINK = "#ff7ac6"
_CLASSIC = {"classic": [0], "c": [_PINK]}
_GRID = {"c": ["#3b82f6", "#ef4444", "#facc15", "#22c55e"]}

VIDEO = {
 "slug": "lego-las-vegas",
 "track": "las-vegas",
 "theme": "vegas",
 "shots": [
  {"type": "chase", "car": 0, "dist": 10, "dist2": 9, "h": 4.2, "h2": 3.8, "side": -1, "side2": -1.2, "look": 40, "drop": 15, "fov": 56, "noCut": True,
   "brick": _CLASSIC, "sphere": True, "neon": True, "act": {"type": "convoy", "at": 0.358, "n": 1, "v": 9}},
  {"type": "orbit", "at": 0.381, "r": 360, "r2": 300, "h": 60, "h2": 42, "a0": 2.15, "a1": 2.7, "fov": 50,
   "brick": _CLASSIC, "sphere": True, "neon": True, "act": {"type": "convoy", "at": 0.376, "n": 1, "v": 9}},
  {"type": "stage", "items": [{"o": "brick", "kind": "classic", "c": _PINK}], "bg": "red", "r": 8, "r2": 7, "h": 2.4, "h2": 3.0, "a0": 0.9, "a1": -0.3, "spin": 0.25, "ly": 0.9},
  {"type": "chase", "car": 3, "dist": 15, "dist2": 13, "h": 8, "h2": 7, "side": 0, "side2": 0, "look": 30, "drop": 9, "noCut": True,
   "brick": _GRID, "neon": True, "act": {"type": "convoy", "at": "straight", "v": 34}},
  {"type": "chase", "car": 3, "dist": 12, "dist2": 10, "h": 4.5, "h2": 4, "side": 2.5, "side2": -1.5, "look": 22, "drop": 6, "noCut": True,
   "brick": _GRID, "neon": True, "act": {"type": "convoy", "at": "straight", "v": 34, "t0": 7}},
  {"type": "stage", "items": [{"o": "brick", "kind": "f1", "c": "#facc15", "x": -1.5, "ry": 0.4}, {"o": "brick", "kind": "f1", "c": "#ef4444", "x": 2, "z": -1.5, "ry": 0.4}], "bg": "gold", "beams": True, "r": 9.5, "r2": 8.5, "h": 3, "h2": 3.6, "a0": -0.5, "a1": 0.3, "spin": 0.15, "ly": 0.9},
  {"type": "fly", "from": 0.36, "to": 0.4, "h": 70, "h2": 120, "side": -60, "ahead": 300, "sphere": True, "neon": True}
 ],
 "coverShot": {"type": "chase", "car": 0, "dist": 8.5, "h": 3.4, "side": 0, "look": 30, "drop": 2.5, "fov": 50, "noCut": True,
   "brick": _CLASSIC, "sphere": True, "neon": True, "act": {"type": "convoy", "at": 0.372, "n": 1, "v": 9}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 7, "h": 2.4, "side": -3, "look": 14, "drop": 1.8, "fov": 44,
            "brick": _CLASSIC, "sphere": True, "neon": True, "act": {"type": "convoy", "at": 0.372, "n": 1, "v": 9}}},
  {"name": "cadillac", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "brick", "kind": "classic", "c": _PINK}], "bg": "red", "r": 10, "h": 2.8, "a0": 0.7, "spin": 0, "ly": 0.8}},
  {"name": "grid", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 3, "dist": 10, "h": 3.6, "side": -2.6, "look": 26, "drop": 3, "fov": 44,
            "brick": _GRID, "neon": True, "act": {"type": "convoy", "at": "straight", "v": 34}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "LEGO В ВЕГАСЕ", "chip": "418 000 деталей",
    "say": "Четыреста восемнадцать тысяч деталей. Из них собрали машину для подиума Вегаса.",
    "hl": ["подиум"]},
   {"kind": "big", "big": "2025", "chip": "Ферстаппен · Норрис · Расселл",
    "say": "В двадцать пятом Ферстаппена, Норриса и Расселла к подиуму вёз розовый кабриолет. За рулём сидел Терри Крюс.",
    "hl": ["розового", "Терри Крюс"]},
   {"kind": "big", "big": "17", "chip": "2 т · 5 м · до 25 км/ч",
    "say": "Его собрали по мотивам Кадиллака пятидесятых. Семнадцать мастеров, почти четыре тысячи часов, больше двух тонн.",
    "hl": ["Кадиллак", "четыре тысячи"]},
   {"kind": "big", "big": "11", "chip": "11 болидов · 28 000+ деталей",
    "say": "В субботу перед гонкой на трассу выедут одиннадцать болидов из кубиков, по одному на команду.",
    "hl": ["субботу", "одиннадцать"]},
   {"kind": "big", "big": "25", "chip": "до 25 км/ч · один круг",
    "say": "Один круг, до двадцати пяти километров в час. Кто за рулём, пока секрет.",
    "hl": ["секрет"]},
   {"kind": "big", "big": "F1 ACADEMY", "chip": "LEGO Racing · Эсме Костерман",
    "say": "А в F1 Academy за команду LEGO в этом сезоне гоняется нидерландка Эсме Костерман.",
    "hl": ["Эсме Костерман"]},
   {"kind": "end", "tag": "Вегас-2026 в субботу",
    "say": "Субботнюю гонку смотрите на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "LEGO IN VEGAS", "chip": "418,000 pieces",
    "say": "Four hundred and eighteen thousand pieces. That's the car built for the Vegas podium.",
    "hl": ["podium"]},
   {"kind": "big", "big": "2025", "chip": "Verstappen · Norris · Russell",
    "say": "In twenty twenty-five a pink convertible drove Verstappen, Norris and Russell to the podium. Terry Crews was at the wheel.",
    "hl": ["pink", "Terry Crews"]},
   {"kind": "big", "big": "17", "chip": "2 t · 5 m · up to 25 km/h",
    "say": "It was inspired by a nineteen fifties Cadillac. Seventeen builders, nearly four thousand hours, over two tonnes.",
    "hl": ["Cadillac", "four thousand"]},
   {"kind": "big", "big": "11", "chip": "11 cars · 28,000+ pieces",
    "say": "On Saturday, before the race, eleven brick-built F1 cars hit the track, one per team.",
    "hl": ["Saturday", "eleven"]},
   {"kind": "big", "big": "25", "chip": "up to 25 km/h · one lap",
    "say": "One lap, up to twenty-five kilometres an hour. Who's driving is still a secret.",
    "hl": ["secret"]},
   {"kind": "big", "big": "F1 ACADEMY", "chip": "LEGO Racing · Esmee Kosterman",
    "say": "And in F1 Academy, Dutch driver Esmee Kosterman races for the LEGO team this season.",
    "hl": ["Esmee Kosterman"]},
   {"kind": "end", "tag": "Vegas 2026 on Saturday",
    "say": "Follow Saturday night's race on the LapRadar live map."}
  ]
 }
}

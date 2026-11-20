# Sphere и F1: светящийся шар у трассы Гран-при Лас-Вегаса. Первый ролик в HQ-режиме студии (VIDEO["hq"]):
# свет и тени, отражения, bloom, детальные болиды-2026 и машина безопасности, бетонные блоки и сетка на городской трассе.
# На экране Sphere только своя графика (шлем в цветах LapRadar, цифры, цвета, клетчатый флаг), без логотипов. Камера общая для всех языков.
_AT = 0.372                      # прямая вдоль Sphere после 9-го поворота (Sphere слева, центр в ~110 м от оси трассы)
_SPH = -110                      # tside: центр Sphere от оси трассы
_CV = {"type": "convoy", "at": 0.355, "v": 34, "n": 4}

VIDEO = {
 "slug": "sphere-and-f1",
 "track": "las-vegas",
 "theme": "vegas",
 "hq": True,
 "shots": [
  {"type": "side", "car": 0, "side": 8.8, "side2": 8.2, "h": 1.1, "h2": 1.3, "fw": 2.5, "fw2": -1.5, "look": 0.5, "ly": 1.1, "fov": 56, "neon": True, "sphere": {"show": "helmet", "s": 0.3, "y": 0.58}, "act": {**_CV, "at": 0.374, "v": 22}},
  {"type": "orbit", "at": _AT, "tside": _SPH, "ly": 42, "r": 270, "r2": 235, "h": 18, "h2": 30, "a0": 0.15, "a1": 0.45, "fov": 50, "neon": True, "sphere": {"show": "lights", "t0": 3.9, "s": 0.55}, "act": {**_CV, "at": 0.36}},
  {"type": "orbit", "at": 0.38, "tside": -110, "ly": 22, "r": 215, "r2": 195, "h": 42, "h2": 34, "a0": -1.95, "a1": -1.7, "fov": 56, "neon": True, "sphere": {"show": "number", "n": "1 200 000", "t": "LED", "y": 0.5, "s": 0.42}, "act": {**_CV, "at": 0.366, "v": 30}},
  {"type": "orbit", "at": 0.362, "tside": -70, "ly": 0, "r": 300, "r2": 260, "h": 230, "h2": 190, "a0": 0.1, "a1": 0.5, "fov": 50, "neon": True, "sphere": {"show": "helmet", "s": 0.7}, "act": {**_CV, "at": 0.335, "v": 40}},
  {"type": "onboard", "car": 0, "fov": 70, "eh": 1.3, "ez": 0.05, "ty": 1.6, "lx": 6, "neon": True, "sphere": {"show": "swirl"}, "act": {**_CV, "at": 0.321, "v": 24}},
  {"type": "carorbit", "car": 0, "r": 11.5, "r2": 10.5, "h": 1.5, "h2": 2.1, "a0": 0.6, "a1": 1.2, "fov": 48, "ly": 0.9, "neon": True, "sphere": {"show": "helmet", "s": 0.28, "y": 0.56}, "act": {**_CV, "at": 0.37, "v": 22, "n": 1}},
  {"type": "side", "follow": "sc", "side": 10, "side2": 9, "h": 1.5, "h2": 1.9, "fw": 2, "fw2": -4, "look": 0, "ly": 1.3, "fov": 54, "neon": True, "sphere": {"show": "sc", "y": 0.6}, "act": {"type": "restart", "at": 0.355, "release": 0.95}},
  {"type": "orbit", "at": _AT, "tside": _SPH, "ly": 55, "r": 330, "r2": 300, "h": 70, "h2": 45, "a0": 0.55, "a1": 0.25, "fov": 50, "neon": True, "sphere": {"show": "chequer"}, "act": {**_CV, "at": 0.362}},
  {"type": "orbit", "at": _AT, "tside": _SPH, "ly": 40, "r": 420, "r2": 400, "h": 120, "h2": 110, "a0": 0.3, "a1": 0.4, "fov": 50, "neon": True, "sphere": {"show": "helmet"}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 9.5, "h": 1.4, "a0": 1.75, "a1": 1.75, "fov": 44, "neon": True, "sphere": {"show": "helmet"}, "act": {**_CV, "at": 0.366, "v": 1}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 9, "h": 1.3, "a0": 1.7, "a1": 1.7, "fov": 40, "neon": True, "sphere": {"show": "helmet"}, "act": {**_CV, "at": 0.368, "v": 1}}},
  {"name": "track", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "orbit", "at": _AT, "tside": _SPH, "ly": 30, "r": 260, "h": 45, "a0": 0.35, "a1": 0.35, "fov": 50, "neon": True, "sphere": {"show": "number", "n": "112", "t": "M"}, "act": {**_CV, "at": 0.364}}},
  {"name": "onboard", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "onboard", "car": 0, "fov": 62, "neon": True, "sphere": {"show": "swirl"}, "act": {**_CV, "at": 0.364, "v": 30}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "big": "112", "head": "Сфера и F1", "sub": "112 метров у трассы", "chip": "112 м",
    "say": "Шар высотой сто двенадцать метров, и болиды F1 летят прямо у его подножия.",
    "hl": ["шар"]},
   {"kind": "big", "big": "2023", "chip": "29.09.2023",
    "say": "Сферу открыли в сентябре двадцать третьего, за семь недель до первой гонки в Вегасе.",
    "hl": ["семь"]},
   {"kind": "big", "big": "1,2M", "chip": "1,2 млн светодиодных шайб",
    "say": "Снаружи миллион двести тысяч светодиодных шайб. Это самый большой экран в мире.",
    "hl": ["экран"]},
   {"kind": "big", "big": "9", "chip": "Сектор 2 · поворот 9",
    "say": "Трасса огибает Сферу во втором секторе, а после девятого поворота идёт вдоль неё.",
    "hl": ["девятого"]},
   {"kind": "big", "big": "3", "chip": "Нельзя: красный, жёлтый, синий",
    "say": "На время заездов F1 запретила там красный, жёлтый и синий: их легко спутать с флагами.",
    "hl": ["красный", "жёлтый", "синий"]},
   {"kind": "big", "big": "20", "chip": "Поул · 20 пилотов · подиум",
    "say": "Зато показывали поул в реальном времени, карточки двадцати пилотов и подиум.",
    "hl": ["поул"]},
   {"kind": "big", "big": "SC", "chip": "Флаги и SC",
    "say": "Флаги и машину безопасности Сфера включала вместе с гоночной дирекцией.",
    "hl": ["машину", "безопасности"]},
   {"kind": "big", "big": "2030", "chip": "До 2030 · 21 ноября",
    "say": "Контракт продлили до двадцать тридцатого, а в субботу в Сфере пройдёт первое официальное афтерпати F1.",
    "hl": ["субботу"]},
   {"kind": "end", "tag": "Вегас-2026 · гонка в субботу",
    "say": "Гонку в субботу смотрите на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "big", "big": "112", "head": "The Sphere and F1", "sub": "112 metres by the track", "chip": "112 m",
    "say": "A glowing ball a hundred and twelve metres tall, and F1 cars race right past it.",
    "hl": ["ball"]},
   {"kind": "big", "big": "2023", "chip": "Sept 29, 2023",
    "say": "The Sphere opened in September twenty twenty-three, seven weeks before the first Vegas race.",
    "hl": ["seven"]},
   {"kind": "big", "big": "1,2M", "chip": "1.2M LED pucks",
    "say": "Its outside has one point two million LED pucks. The largest screen in the world.",
    "hl": ["screen"]},
   {"kind": "big", "big": "9", "chip": "Sector 2 · Turn 9",
    "say": "The track wraps around it in sector two and runs alongside after Turn nine.",
    "hl": ["nine"]},
   {"kind": "big", "big": "3", "chip": "Banned: red, yellow, blue",
    "say": "During sessions F1 banned red, yellow and blue on it. Drivers could mistake them for flags.",
    "hl": ["red", "yellow", "blue"]},
   {"kind": "big", "big": "20", "chip": "Pole · 20 drivers · podium",
    "say": "Instead it showed pole position live, cards of all twenty drivers and the podium.",
    "hl": ["pole"]},
   {"kind": "big", "big": "SC", "chip": "Flags and SC",
    "say": "Flags and the safety car came up on the Sphere in sync with race control.",
    "hl": ["safety", "car"]},
   {"kind": "big", "big": "2030", "chip": "To 2030 · Nov 21",
    "say": "The deal now runs to twenty thirty, and on Saturday the Sphere hosts the first F1 afterparty.",
    "hl": ["Saturday"]},
   {"kind": "end", "tag": "Vegas 2026 · race on Saturday",
    "say": "Follow Saturday's race on the LapRadar live map."}
  ]
 }
}

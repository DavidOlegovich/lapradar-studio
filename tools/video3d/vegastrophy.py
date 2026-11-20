# Новый кубок Гран-при Лас-Вегаса 2026: V-силуэт по мотивам неоновых вывесок и старых афиш Фримонт-стрит, 122 лампы, красный контур.
# Кубок: своя модель студии (stage "vtrophy", на трассе shot "trophy"): форма и свет по описанию, без логотипов и надписей настоящего кубка.
# Ночной Стрип, светящаяся Sphere, неон на фасадах, медленный облёт. Камера (shots) общая для всех языков.
_T = {"at": 0.38, "side": 40, "s": 7, "spin": 0.06}
_NIGHT = {"sphere": True, "neon": True}

VIDEO = {
 "slug": "las-vegas-neon-trophy",
 "track": "las-vegas",
 "theme": "vegas",
 "shots": [
  {"type": "orbit", "at": 0.38, "tside": 40, "ly": 15, "r": 95, "r2": 80, "h": 14, "h2": 18, "a0": -1.25, "a1": -1.75, "fov": 52,
   "trophy": _T, **_NIGHT, "act": {"type": "convoy", "at": 0.37, "v": 34}},
  {"type": "stage", "items": [{"o": "vtrophy"}], "bg": "red", "beams": True, "r": 9, "r2": 7.8, "h": 2.2, "h2": 2.8, "a0": 0.55, "a1": -0.35, "spin": 0.04, "ly": 2.3},
  {"type": "stage", "items": [{"o": "vtrophy"}], "bg": "blue", "beams": False, "r": 5.2, "r2": 4.6, "h": 3.4, "h2": 3.8, "a0": -0.35, "a1": 0.2, "spin": 0.05, "ly": 3.2, "pk": 1.5},
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 6, "h2": 5.5, "side": 0, "side2": 0, "look": 22, "drop": 9, "noCut": True,
   **_NIGHT, "act": {"type": "convoy", "at": "straight", "v": 48}},
  {"type": "orbit", "at": 0.38, "r": 330, "r2": 280, "h": 70, "h2": 50, "a0": -2.2, "a1": -1.6, "fov": 50,
   "trophy": _T, **_NIGHT, "act": {"type": "convoy", "at": 0.372, "v": 30}},
  {"type": "stage", "items": [{"o": "vtrophy", "x": -2.1, "ry": 0.3}, {"o": "vtrophy", "x": 2.1, "z": -1.2, "ry": -0.3, "s": 0.8}], "bg": "gold", "beams": True, "r": 11, "r2": 10, "h": 2.6, "h2": 3.2, "a0": -0.4, "a1": 0.3, "spin": 0, "ly": 2.2},
  {"type": "orbit", "at": 0.38, "tside": 40, "ly": 20, "r": 150, "r2": 125, "h": 30, "h2": 42, "a0": -1.9, "a1": -1.45, "fov": 50, "trophy": _T, **_NIGHT, "act": {"type": "convoy", "at": 0.372, "v": 30}}
 ],
 "coverShot": {"type": "stage", "items": [{"o": "vtrophy"}], "bg": "red", "beams": True, "r": 7.5, "h": 3.2, "a0": 0.4, "a1": 0.4, "spin": 0, "ly": 4.6, "pk": 1.5},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "vtrophy"}], "bg": "red", "beams": True, "r": 6.2, "h": 2.4, "a0": 0.5, "a1": 0.5, "spin": 0, "ly": 2.4}},
  {"name": "strip", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "orbit", "at": 0.38, "tside": 40, "ly": 13, "r": 75, "h": 22, "a0": -1.35, "a1": -1.35, "fov": 50, "trophy": _T, **_NIGHT, "act": {"type": "convoy", "at": 0.372, "v": 30}}},
  {"name": "lights", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "vtrophy"}], "bg": "blue", "beams": False, "r": 4.6, "h": 3.6, "a0": -0.2, "a1": -0.2, "spin": 0, "ly": 3.3}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "НЕОНОВЫЙ КУБОК", "chip": "Вегас-2026 · новый кубок",
    "say": "Победитель Вегаса в этом году увезёт домой собственную неоновую вывеску.",
    "hl": ["неоновую", "вывеску"]},
   {"kind": "big", "big": "V", "chip": "V · Vegas · victory",
    "say": "Кубок в форме буквы V: Вегас и победа. В сети сразу пошутили, что V значит Verstappen.",
    "hl": ["V", "Verstappen"]},
   {"kind": "big", "big": "122", "chip": "122 лампы · красный контур",
    "say": "Сто двадцать две лампы и красный контур. Так светились старые афиши на Фримонт-стрит.",
    "hl": ["Сто двадцать две", "Фримонт-стрит"]},
   {"kind": "big", "big": "56", "chip": "56 см · 3,6 кг",
    "say": "Высота пятьдесят шесть сантиметров, вес три и шесть десятых килограмма. Поднять его после гонки легко.",
    "hl": ["пятьдесят шесть"]},
   {"kind": "big", "big": "2023", "chip": "2023–2025 · пустыня и хром",
    "say": "Прошлый кубок три года напоминал скалы пустыни: бронза под песчаник и хромированный верх с подсветкой.",
    "hl": ["бронза", "песчаник"]},
   {"kind": "big", "big": "6", "chip": "≈6 месяцев работы",
    "say": "Новый кубок делали около полугода. Это вторая версия за всю историю гонки.",
    "hl": ["полугода", "вторая"]},
   {"kind": "end", "tag": "Вегас-2026 · гонка в субботу",
    "say": "Кто поднимет его в субботу, смотрите на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "NEON TROPHY", "chip": "Vegas 2026 · new trophy",
    "say": "This year's Vegas winner takes home their very own neon sign.",
    "hl": ["neon", "sign"]},
   {"kind": "big", "big": "V", "chip": "V · Vegas · victory",
    "say": "The trophy is shaped like a V, for Vegas and victory. Fans instantly joked that V stands for Verstappen.",
    "hl": ["V", "Verstappen"]},
   {"kind": "big", "big": "122", "chip": "122 lights · red outline",
    "say": "One hundred and twenty-two lights and a red outline, like the old marquees on Fremont Street.",
    "hl": ["twenty-two", "Fremont"]},
   {"kind": "big", "big": "56", "chip": "56 cm · 3.6 kg",
    "say": "Fifty-six centimetres tall and three point six kilos. Easy to lift after the race.",
    "hl": ["Fifty-six"]},
   {"kind": "big", "big": "2023", "chip": "2023–2025 · desert and chrome",
    "say": "The old trophy echoed the desert rock: a bronze base made to look like sandstone and a lit chrome top.",
    "hl": ["bronze", "sandstone"]},
   {"kind": "big", "big": "6", "chip": "≈6 months of work",
    "say": "The new one took about six months to make. It's only the second design in the race's history.",
    "hl": ["six months", "second"]},
   {"kind": "end", "tag": "Vegas 2026 · race on Saturday",
    "say": "See who lifts it on Saturday on the LapRadar live map."}
  ]
 }
}

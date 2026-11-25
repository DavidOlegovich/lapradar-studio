# Формула E, сезон 2026/27: двойные этапы с двумя разными гонками, классический E-Prix и короткий E-Prix Unleashed.
# Факты (источники в tools/topics.md, «Источники 26.11: E-Prix Unleashed»): на двойном этапе один E-Prix и один Unleashed;
# Unleashed около 25–30 мин (FIA в обновлённом описании 25, в июне 30), классика около 40–45 мин; высокий прижим против низкого;
# Attack Mode 6 мин в Unleashed; Pit Boost обязателен только в классической гонке; очки за гонку прежние (25 победителю, топ-10);
# 8 двойных этапов из 21 гонки в 13 городах; сезон открывает Мехико 16.01.2027, Джидда 16–17.04.2027; новые трассы Брэндс-Хэтч, Зандфорт, COTA.
# Не повторяет gen4 (машина), fecalendar (календарь и перенос Джидды), feorigins (история). Цитат нет.
# HQ-режим, трасса Зандфорт днём (новая в календаре Формулы E). Машины условные: цвета без ливрей и логотипов. Время по городам не называем.
_CYAN = ["#0e7490", "#f8fafc", "stripe"]
_LIME = ["#65a30d", "#111827", "band"]
_PINK = ["#be185d", "#f8fafc", "split"]
_CV = {"type": "convoy", "at": 0.03, "v": 30, "n": 3}
_TWO = [{"o": "f1", "c": "#0e7490", "a": "#f8fafc", "p": "stripe", "x": -2.3, "ry": 0.25},
        {"o": "f1", "c": "#65a30d", "a": "#111827", "p": "band", "x": 2.3, "ry": -0.25}]

VIDEO = {
 "slug": "formula-e-eprix-unleashed",
 "track": "zandvoort",
 "theme": "day",
 "hq": {"cars": [_CYAN, _LIME, _PINK], "lampFade": True},
 "coverText": {"ru": {"head": "E-PRIX UNLEASHED", "sub": "новая короткая гонка Формулы E"},
               "en": {"head": "E-PRIX UNLEASHED", "sub": "Formula E's new short race"}},
 "shots": [
  # 1 крючок: колонна на прямой
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 5.5, "h2": 5, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 55, "n": 3}},
  # 2 длительность: дуэль
  {"type": "chase", "car": 0, "dist": 14, "dist2": 12, "h": 5.5, "h2": 5, "side": -2.5, "side2": 2, "look": 22, "drop": 3, "noCut": True, "act": {"type": "duel"}},
  # 3 аэродинамика: две машины в студии
  {"type": "stage", "items": _TWO, "bg": "blue", "r": 12, "r2": 10.5, "h": 2.6, "h2": 3.4, "a0": -0.3, "a1": 0.4, "spin": 0.05, "ly": 0.6},
  # 4 Attack Mode
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10, "h": 4.8, "h2": 4.4, "side": 1.5, "side2": -1, "look": 18, "drop": 3, "noCut": True, "act": {"type": "boost"}},
  # 5 Pit Boost
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 5, "h2": 4.8, "side": 2, "side2": 2, "look": 14, "drop": 3, "noCut": True, "act": {"type": "pit", "car": 0, "box": 0.4, "stop": 3.2}},
  # 6 восемь двойных этапов
  {"type": "chase", "car": 2, "dist": 27, "dist2": 25, "h": 11, "h2": 10, "side": 0, "side2": 0, "look": 24, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 50, "n": 3}},
  # 7 календарь: 21 гонка, Мехико, Джидда
  {"type": "chase", "car": 2, "dist": 30, "dist2": 26, "h": 12, "h2": 10, "side": 1.5, "side2": -1.5, "look": 26, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 55, "n": 3}},
  # 8 очки те же
  {"type": "carorbit", "car": 0, "r": 10, "r2": 9, "h": 1.4, "h2": 1.9, "a0": 0.5, "a1": 1.2, "fov": 46, "ly": 0.8, "act": {**_CV, "at": 0.05, "v": 22, "n": 1}},
  # 9 конец
  {"type": "orbit", "at": 0.05, "r": 430, "r2": 410, "h": 130, "h2": 120, "a0": 1.2, "a1": 1.3, "fov": 50, "act": {**_CV, "at": 0.0, "v": 45}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 9.5, "h": 1.4, "a0": 1.85, "a1": 1.85, "fov": 44, "act": {**_CV, "at": 0.05, "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 7.5, "h": 1.2, "a0": 2.1, "a1": 2.1, "fov": 40, "ly": 0.6, "act": {**_CV, "at": 0.05, "v": 1, "n": 2}}},
  {"name": "sprint", "w": 1200, "h": 800, "t": 1.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 9, "h": 3.6, "side": -2.4, "look": 12, "drop": 2, "fov": 40, "act": {"type": "duel"}}},
  {"name": "pitboost", "w": 1200, "h": 800, "t": 2.4, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 11, "h": 4, "side": 2.2, "look": 10, "drop": 2, "fov": 44, "act": {"type": "pit", "car": 0, "box": 0.4, "stop": 3.2}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "chip": "Две гонки за уикенд",
    "say": "Один уикенд, две гонки, и они совсем разные. Знакомьтесь: E-Prix Unleashed.",
    "hl": ["разные", "Unleashed"]},
   {"kind": "big", "chip": "25 мин против 40",
    "say": "По описанию FIA новая гонка идёт около двадцати пяти минут. Классическая Формула E около сорока.",
    "hl": ["двадцати", "сорока"]},
   {"kind": "big", "chip": "Прижим: высокий и низкий",
    "say": "В короткой гонке высокий прижим, в классической низкий: меньше сопротивления, проще беречь энергию.",
    "hl": ["высокий", "низкий"]},
   {"kind": "big", "chip": "Attack Mode · 6 минут",
    "say": "Режим атаки в Unleashed длится шесть минут. Борьба идёт колесо в колесо.",
    "hl": ["шесть", "минут"]},
   {"kind": "big", "chip": "Pit Boost только в классике",
    "say": "Обязательный пит-буст остался только в классической гонке. В короткой его нет.",
    "hl": ["пит-буст", "нет"]},
   {"kind": "big", "chip": "8 двойных этапов",
    "say": "Короткие гонки будут только на двойных этапах, а их в сезоне восемь.",
    "hl": ["восемь"]},
   {"kind": "big", "chip": "21 гонка · 13 городов",
    "say": "В календаре двадцать одна гонка в тринадцати городах. Сезон откроет Мехико шестнадцатого января, а Джидда сдвинулась на апрель.",
    "hl": ["двадцать", "Мехико"]},
   {"kind": "big", "chip": "Очки прежние: 25 за победу",
    "say": "Очки за гонку не изменились: двадцать пять победителю и очки первой десятке.",
    "hl": ["двадцать", "пять"]},
   {"kind": "end", "tag": "Какая гонка вам ближе?",
    "say": "Календарь Формулы E смотрите на ЛапРадар.", "hl": ["ЛапРадар"]}
  ],
  "en": [
   {"kind": "big", "chip": "Two races, one weekend",
    "say": "One weekend, two races, and they're nothing alike. Meet E-Prix Unleashed.",
    "hl": ["two", "Unleashed"]},
   {"kind": "big", "chip": "25 min vs 40",
    "say": "Per the FIA description, the new race runs about twenty-five minutes. A classic Formula E race takes about forty.",
    "hl": ["twenty-five", "forty"]},
   {"kind": "big", "chip": "Downforce: high vs low",
    "say": "The short race uses high downforce. The classic uses low, less drag and easier energy saving.",
    "hl": ["high", "low"]},
   {"kind": "big", "chip": "Attack Mode · 6 minutes",
    "say": "In Unleashed, Attack Mode lasts six minutes. Expect wheel-to-wheel fights.",
    "hl": ["six", "minutes"]},
   {"kind": "big", "chip": "Pit Boost: classic only",
    "say": "The mandatory Pit Boost stop stays in the classic race. The short one has none.",
    "hl": ["Pit Boost", "none"]},
   {"kind": "big", "chip": "8 double-headers",
    "say": "Short races only run at double-headers, and there are eight of them this season.",
    "hl": ["eight"]},
   {"kind": "big", "chip": "21 races · 13 cities",
    "say": "Twenty-one races in thirteen cities. Mexico City opens it on January sixteenth, and Jeddah moved to April.",
    "hl": ["Twenty-one", "Mexico City"]},
   {"kind": "big", "chip": "Same points: 25 for a win",
    "say": "Race points haven't changed: twenty-five for the winner, and points for the top ten.",
    "hl": ["twenty-five"]},
   {"kind": "end", "tag": "Which race is for you?",
    "say": "The Formula E calendar is on LapRadar.", "hl": ["LapRadar"]}
  ]
 }
}

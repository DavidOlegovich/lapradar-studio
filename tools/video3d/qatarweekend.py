# Катар-2026: гид по уикенду. Формат без спринта (Пт: 2 тренировки, Сб: 3-я тренировка и квалификация, Вс: гонка), F2 в тот же уикенд.
# Круг 5,419 км, 57 кругов, около 309 км; рекорд круга в гонке 1:22,384 (Норрис, 2024); 16 поворотов, повороты 12-14 быстрые, главная прямая > 1 км, T1 место обгона.
# Шины: Pirelli привезла C1, C2, C3 (самое жёсткое трио); лимит 27 кругов на комплект (подробно в qatar-gp-2026-tyre-limit, тут одна строка).
# Зачёт после Вегаса: Антонелли 402 (чемпион с Мехико, 1.11), Ферстаппен 304, Хэмилтон 267, Расселл 264, Норрис 264, Леклер 250.
# Время сессий и время по городам НЕ называем. Источники: tools/topics.md («Источники 27.11: Катар, гид по уикенду»).
_BLUE = ["#1e40af", "#f8fafc", "stripe"]
_ORG = ["#f97316", "#111827", "band"]
_TEAL = ["#0f766e", "#e5e7eb", "split"]
_CV = {"type": "convoy", "at": 0.02, "v": 30, "n": 3}
_TWO = [{"o": "f1", "c": _BLUE[0], "a": _BLUE[1], "p": _BLUE[2], "x": -2.3, "ry": 0.25},
        {"o": "f1", "c": _ORG[0], "a": _ORG[1], "p": _ORG[2], "x": 2.3, "ry": -0.25}]

VIDEO = {
 "slug": "qatar-gp-2026-weekend-guide",
 "track": "lusail",
 "theme": "night",
 "hq": {"cars": [_BLUE, _ORG, _TEAL], "lampFade": True},
 "coverText": {"ru": {"head": "КАТАР: ГИД", "sub": "как пройдёт уикенд"},
               "en": {"head": "QATAR: A GUIDE", "sub": "how the weekend works"}},
 "shots": [
  # 1 крючок
  {"type": "chase", "car": 0, "dist": 9, "dist2": 8.5, "h": 3.4, "h2": 3.2, "side": -1.8, "side2": -1.2, "look": 9, "drop": 1.5, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 62, "n": 3}},
  # 2 формат
  {"type": "carorbit", "car": 0, "r": 8.5, "r2": 7.5, "h": 1.4, "h2": 1.8, "a0": 0.5, "a1": 1.1, "fov": 46, "ly": 0.8, "act": {**_CV, "at": 0.62, "v": 28}},
  # 3 цифры
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10, "h": 4.5, "h2": 4, "side": -2.5, "side2": -1.5, "look": 14, "drop": 3, "noCut": True, "act": {"type": "duel"}},
  # 4 рекорд
  {"type": "chase", "car": 0, "dist": 10, "dist2": 9, "h": 3.8, "h2": 3.6, "side": 2.4, "side2": 1.6, "look": 11, "drop": 2, "noCut": True, "act": {"type": "duel"}},
  # 5 быстрые повороты
  {"type": "carorbit", "car": 0, "r": 9.5, "r2": 8.5, "h": 1.3, "h2": 1.7, "a0": 0.4, "a1": 1.05, "fov": 46, "ly": 0.7, "act": {"type": "heat", "at": 0.7}},
  # 6 прямая и первый поворот
  {"type": "chase", "car": 0, "dist": 10, "dist2": 9, "h": 3.8, "h2": 3.6, "side": 1.8, "side2": 1.2, "look": 10, "drop": 1.5, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 62, "n": 3}},
  # 7 шины
  {"type": "tyres", "hi": -1},
  # 8 зачёт
  {"type": "stage", "items": _TWO, "bg": "gold", "r": 12.5, "r2": 11, "h": 2.8, "h2": 3.4, "a0": 0.3, "a1": -0.3, "spin": 0.04, "ly": 0.6},
  # 9 F2
  {"type": "chase", "car": 0, "dist": 11, "dist2": 10, "h": 4.2, "h2": 4, "side": -2.4, "side2": -1.6, "look": 12, "drop": 2, "noCut": True, "act": {"type": "duel"}},
  # 10 конец
  {"type": "chase", "car": 0, "dist": 26, "dist2": 28, "h": 10, "h2": 11, "side": -2, "side2": 0, "look": 30, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 55, "n": 3}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 9.5, "h": 1.4, "a0": 1.85, "a1": 1.85, "fov": 44, "act": {**_CV, "at": 0.02, "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 7.5, "h": 1.2, "a0": 2.1, "a1": 2.1, "fov": 40, "ly": 0.6, "act": {**_CV, "at": 0.02, "v": 1, "n": 2}}},
  {"name": "straight", "w": 1200, "h": 800, "t": 1.8, "u": 0.4,
   "shot": {"type": "chase", "car": 0, "dist": 28, "h": 12, "side": 0, "look": 30, "drop": 3, "fov": 44, "act": {"type": "convoy", "at": "straight", "v": 62, "n": 3}}},
  {"name": "corners", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "side", "car": 0, "side": 6.5, "h": 1.2, "fw": 1, "look": 0.5, "ly": 1.0, "fov": 50, "act": {**_CV, "at": 0.7, "v": 30}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "chip": "Катар · гид по уикенду",
    "say": "Что ждать от Катара? Чемпион уже известен, зато остальное ещё не решено.",
    "hl": ["Катара", "чемпион"]},
   {"kind": "big", "chip": "Без спринта · Пт, Сб, Вс",
    "say": "Спринта нет. В пятницу две тренировки, в субботу третья и квалификация, в воскресенье гонка.",
    "hl": ["Спринта", "нет"]},
   {"kind": "big", "big": "57", "chip": "57 кругов · 5,419 км · ≈ 309 км",
    "say": "Пятьдесят семь кругов по пять целых четыреста девятнадцать километра, около трёхсот девяти километров всей гонки.",
    "hl": ["пятьдесят", "семь"]},
   {"kind": "big", "chip": "Рекорд круга в гонке · 1:22,384",
    "say": "Рекорд круга в гонке принадлежит Норрису: одна двадцать две триста восемьдесят четыре, двадцать четвёртый год.",
    "hl": ["Норрису"]},
   {"kind": "big", "chip": "Повороты 12–14 · быстрые правые",
    "say": "Круг состоит из быстрых дуг. Самые тяжёлые для шин правые повороты с двенадцатого по четырнадцатый.",
    "hl": ["быстрых", "двенадцатого"]},
   {"kind": "big", "chip": "Прямая > 1 км · обгон в повороте 1",
    "say": "Главная прямая длиннее километра, и первый поворот в конце неё лучшее место для обгона.",
    "hl": ["прямая", "первый", "поворот"]},
   {"kind": "tyres", "names": ["C1", "C2", "C3"], "hi": -1, "chip": "C1, C2, C3 · лимит 27 кругов",
    "say": "Pirelli привезла три самых жёстких состава, плюс лимит: комплект живёт до двадцати семи кругов.",
    "hl": ["жёстких", "двадцати", "семи"]},
   {"kind": "big", "chip": "Антонелли 402 · Ферстаппен 304",
    "say": "Антонелли чемпион, четыреста два очка. Второе место: у Ферстаппена триста четыре, у Хэмилтона двести шестьдесят семь.",
    "hl": ["Антонелли", "Ферстаппена"]},
   {"kind": "big", "chip": "Тот же уикенд · Формула 2",
    "say": "В те же дни в Лусаиле гоняется и Формула два.",
    "hl": ["Формула", "два"]},
   {"kind": "end", "tag": "Катар · гид по уикенду",
    "say": "Во сколько гонка по вашему времени, смотрите на ЛапРадар.", "hl": ["вашему", "времени"]}
  ],
  "en": [
   {"kind": "big", "chip": "Qatar · weekend guide",
    "say": "What to expect in Qatar? The champion is already known, but plenty is still to be decided.",
    "hl": ["Qatar", "champion"]},
   {"kind": "big", "chip": "No sprint · Fri, Sat, Sun",
    "say": "No sprint. Two practice sessions on Friday, third practice and qualifying on Saturday, the race on Sunday.",
    "hl": ["no", "sprint"]},
   {"kind": "big", "big": "57", "chip": "57 laps · 5.419 km · ≈ 309 km",
    "say": "Fifty-seven laps of five point four one nine kilometres, about three hundred and nine kilometres in all.",
    "hl": ["Fifty-seven"]},
   {"kind": "big", "chip": "Race lap record · 1:22.384",
    "say": "The race lap record belongs to Norris: one twenty-two three eighty-four, set in twenty twenty-four.",
    "hl": ["Norris"]},
   {"kind": "big", "chip": "Turns 12–14 · fast right-handers",
    "say": "Fast bends all lap. Hardest on tyres: the right-handers from Turn twelve to fourteen.",
    "hl": ["fast", "twelve"]},
   {"kind": "big", "chip": "Straight > 1 km · pass into Turn 1",
    "say": "The main straight is over a kilometre long, and Turn one at the end of it is the best place to pass.",
    "hl": ["straight", "Turn", "one"]},
   {"kind": "tyres", "names": ["C1", "C2", "C3"], "hi": -1, "chip": "C1, C2, C3 · 27-lap limit",
    "say": "Pirelli brought its three hardest compounds, plus a limit: a set lasts at most twenty-seven laps.",
    "hl": ["hardest", "twenty-seven"]},
   {"kind": "big", "chip": "Antonelli 402 · Verstappen 304",
    "say": "Antonelli is champion with four hundred and two points. Verstappen has three hundred and four in second, Hamilton two sixty-seven.",
    "hl": ["Antonelli", "Verstappen"]},
   {"kind": "big", "chip": "Same weekend · Formula 2",
    "say": "Formula Two races at Lusail the same weekend.",
    "hl": ["Formula", "Two"]},
   {"kind": "end", "tag": "Qatar · weekend guide",
    "say": "Check what time the race starts in your own time zone on LapRadar.", "hl": ["your", "own", "time", "zone"]}
  ]
 }
}

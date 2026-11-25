# Маркес, восьмой титул MotoGP: как он отыграл 102 очка. Камера (shots) общая для всех языков.
# Факты и источники: tools/topics.md («Источники 26.11: Маркес, восьмой титул»). Байки условные: без логотипов и настоящих ливрей.
# Время по городам не называем. Трасса: Шпильберг, день, HQ-режим.
_BIKE = lambda at, dist=8, dist2=6.5, h=3.2, h2=2.8, side=-2.2, side2=1.8, **k: {
    "type": "chase", "follow": "bike", "fi": 5, "dist": dist, "dist2": dist2, "h": h, "h2": h2, "side": side, "side2": side2,
    "look": 22, "drop": 2, "noCut": True, "act": {"type": "motogp", "at": at, **k}}
_RED = "#e10600"
VIDEO = {
 "slug": "marquez-eighth-motogp-title-2026",
 "track": "spielberg",
 "theme": "day",
 "hq": True,
 "coverText": {"ru": {"head": "МАРКЕС: ВОСЬМОЙ ТИТУЛ", "sub": "минус 102 очка"},
               "en": {"head": "MÁRQUEZ: TITLE NO. 8", "sub": "from 102 points down"}},
 "shots": [
  # 1 крючок: байки на трассе
  _BIKE(0.12, 7, 5, 2.8, 2.4),
  # 2 Муджелло: минус 102 и рекорд Баньайи
  {"type": "stage", "items": [{"o": "bike", "c": _RED, "lean": 0.0, "s": 1.3, "y": 0.4}], "bg": "red", "r": 7.2, "r2": 6.8, "h": 1.4, "h2": 1.8,
   "a0": 0.9, "a1": -0.3, "spin": 0.3, "ly": 2.4,
   "hud": {"type": "bars", "rows": [{"label": "2022", "v": 91, "c": "#9fb4ff"}, {"label": "2026", "v": 102, "c": _RED}], "min": 0, "max": 110, "hi": 1}},
  # 3 Венгрия: спринт и гонка
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 7, "dist2": 8, "h": 2.8, "h2": 3.2, "side": 2, "side2": -1.5, "look": 18, "drop": 2, "noCut": True, "act": {"type": "motogp", "at": 0.55, "pass": 1}},
  # 4 368 очков
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 14, "dist2": 10, "h": 6, "h2": 4.5, "side": 2.5, "side2": -2, "look": 30, "drop": 3, "noCut": True, "act": {"type": "motogp", "at": 0.4}},
  # 5 Портиман, спринт: падение
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 6, "dist2": 8, "h": 2.6, "h2": 3.2, "side": -2, "side2": 2, "look": 18, "drop": 2, "noCut": True, "act": {"type": "motogp", "at": 0.02}},
  # 6 запас 55 очков, нужно девятое место
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 14, "dist2": 11, "h": 6, "h2": 5, "side": -2.5, "side2": 2, "look": 30, "drop": 3, "noCut": True, "act": {"type": "motogp", "at": 0.3}},
  # 7 воскресная гонка
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 8, "dist2": 6, "h": 3, "h2": 2.6, "side": -2, "side2": 2, "look": 22, "drop": 2, "noCut": True, "act": {"type": "motogp", "at": 0.85}},
  # 8 восьмой титул, рекорд Агостини, шлем
  {"type": "stage", "items": [{"o": "bike", "c": _RED, "x": -1.6, "lean": 0.35, "s": 1.1}, {"o": "trophy", "x": 1.8, "s": 0.9}], "confetti": True, "bg": "gold",
   "r": 10, "r2": 8.5, "h": 2.6, "h2": 3, "a0": 0.5, "a1": -0.3, "spin": 0, "ly": 1.6},
  # 9 Валенсия
  {"type": "fly", "from": 0.0, "to": 0.08, "h": 60, "h2": 140, "side": -40, "ahead": 260}
 ],
 "coverShot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 7, "h": 2.8, "side": -2.2, "look": 20, "drop": 2, "act": {"type": "motogp", "at": 0.12}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 7, "h": 2.8, "side": -2.2, "look": 20, "drop": 2, "fov": 42, "act": {"type": "motogp", "at": 0.12}}},
  {"name": "sprint", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 6, "h": 2.6, "side": -2, "look": 18, "drop": 2, "fov": 42, "act": {"type": "motogp", "at": 0.02}}},
  {"name": "title", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "bike", "c": _RED, "x": -1.6, "lean": 0.35, "s": 1.1}, {"o": "trophy", "x": 1.8, "s": 0.9}], "confetti": True, "bg": "gold",
            "r": 9, "h": 2.4, "a0": 0.3, "spin": 0, "ly": 1.5}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "chip": "Минус 102 → чемпион",
    "say": "Сто два очка отставания, и всё равно чемпион. Как Маркес это сделал?",
    "hl": ["Сто два", "чемпион"]},
   {"kind": "big", "chip": "Муджелло · рекорд камбэка", "min": 4.6,
    "say": "После Муджелло минус сто два очка. Прежний рекорд камбэка чемпиона: девяносто одно, Баньайя, две тысячи двадцать второй.",
    "hl": ["сто два", "девяносто одно"]},
   {"kind": "big", "chip": "Венгрия · спринт и гонка",
    "say": "В Венгрии Маркес выиграл спринт и гонку, свою первую победу в гонке за сезон.",
    "hl": ["спринт", "гонку"]},
   {"kind": "big", "big": "368", "chip": "368 очков с Венгрии",
    "say": "С Венгрии он набрал триста шестьдесят восемь очков. Отрыв Беццекки растаял.",
    "hl": ["триста шестьдесят восемь"]},
   {"kind": "big", "chip": "Портиман · спринт · падение",
    "say": "Спринт. Маркес идёт третьим, титул рядом, но на предпоследнем круге падает в седьмом повороте.",
    "hl": ["падает"]},
   {"kind": "big", "chip": "Запас 55 очков · нужно P9", "min": 4.2,
    "say": "Титул откладывается. Запас над Мартином пятьдесят пять очков, в воскресенье хватит девятого места.",
    "hl": ["пятьдесят пять", "девятого"]},
   {"kind": "big", "chip": "Беццекки P1 · Мартин P2 · Маркес P8",
    "say": "Выиграл Беццекки, вторым Мартин, а Маркес приехал восьмым. И этого хватило.",
    "hl": ["восьмым", "хватило"]},
   {"kind": "big", "chip": "8 титулов · как у Агостини",
    "say": "Восьмой титул в королевском классе, как у Агостини. Сам Агостини вручил ему золотой шлем.",
    "hl": ["Восьмой", "золотой шлем"]},
   {"kind": "end", "tag": "Валенсия · 27–29 ноября",
    "say": "Дальше Валенсия, двадцать седьмого по двадцать девятое ноября, последняя гонка эры тысячи кубов. Смотрите на ЛапРадар.",
    "hl": ["Валенсия", "ЛапРадар"]}
  ],
  "en": [
   {"kind": "big", "chip": "−102 → champion",
    "say": "A hundred and two points down, and still champion. How did Márquez do it?",
    "hl": ["hundred and two", "champion"]},
   {"kind": "big", "chip": "Mugello · comeback record", "min": 4.6,
    "say": "After Mugello he is a hundred and two down. The old comeback record: ninety-one, Bagnaia, twenty twenty-two.",
    "hl": ["hundred and two", "ninety-one"]},
   {"kind": "big", "chip": "Hungary · sprint and race",
    "say": "In Hungary Márquez won the sprint and the race, his first grand prix win of the year.",
    "hl": ["sprint", "race"]},
   {"kind": "big", "big": "368", "chip": "368 points since Hungary",
    "say": "Since Hungary he has scored three hundred sixty-eight points. Bezzecchi's gap melted away.",
    "hl": ["three hundred sixty-eight"]},
   {"kind": "big", "chip": "Portimão · sprint · crash",
    "say": "The sprint. Márquez runs third, title within reach, but on the penultimate lap he crashes at Turn seven.",
    "hl": ["crashes"]},
   {"kind": "big", "chip": "55-point lead · P9 needed", "min": 4.2,
    "say": "The title waits. His lead over Martín is fifty-five points, and ninth place on Sunday will do.",
    "hl": ["fifty-five", "ninth"]},
   {"kind": "big", "chip": "Bezzecchi P1 · Martín P2 · Márquez P8",
    "say": "Bezzecchi wins, Martín is second, and Márquez comes home eighth. That is enough.",
    "hl": ["eighth", "enough"]},
   {"kind": "big", "chip": "8 titles · level with Agostini",
    "say": "An eighth premier-class title, level with Agostini. Agostini himself handed him a golden helmet.",
    "hl": ["eighth", "golden helmet"]},
   {"kind": "end", "tag": "Valencia · 27–29 Nov",
    "say": "Next, Valencia, November twenty-seventh to twenty-ninth, the last race of the thousand cc era. Follow it on LapRadar.",
    "hl": ["Valencia", "LapRadar"]}
  ]
 }
}

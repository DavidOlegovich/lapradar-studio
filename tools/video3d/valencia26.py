# Валенсия 2026: последняя гонка эпохи 1000 кубов MotoGP, превью финала. Камера (shots) общая для всех языков.
# Факты и источники: tools/topics.md («Источники 27.11: Валенсия, финал MotoGP»). Байки условные: без логотипов и настоящих ливрей.
# Время сессий и городов не называем. Карты Валенсии в студии нет: трасса Имола (день), в кадре не выдаём её за Валенсию.
_BIKE = lambda at, dist=8, dist2=6.5, h=3.2, h2=2.8, side=-2.2, side2=1.8, **k: {
    "type": "chase", "follow": "bike", "fi": 5, "dist": dist, "dist2": dist2, "h": h, "h2": h2, "side": side, "side2": side2,
    "look": 22, "drop": 2, "noCut": True, "act": {"type": "motogp", "at": at, **k}}
_RED = "#e10600"
_BLUE = "#2f6bff"
VIDEO = {
 "slug": "motogp-valencia-2026-finale-preview",
 "track": "imola",
 "theme": "day",
 "hq": True,
 "coverText": {"ru": {"head": "ВАЛЕНСИЯ: ФИНАЛ ЭПОХИ 1000 КУБОВ", "sub": "что ещё не решено"},
               "en": {"head": "VALENCIA: LAST 1000cc RACE", "sub": "what is still undecided"}},
 "shots": [
  # 1 крючок
  _BIKE(0.12, 6, 5, 2.4, 2.2),
  # 2 зачёт производителей
  {"type": "stage", "items": [{"o": "bike", "c": _RED, "x": -1.2, "lean": 0.2, "s": 1.2, "y": 0.4}, {"o": "bike", "c": _BLUE, "x": 1.4, "lean": -0.2, "s": 1.2, "y": 0.4}], "bg": "red",
   "r": 7.5, "r2": 7.0, "h": 1.5, "h2": 1.9, "a0": 0.7, "a1": -0.3, "spin": 0.3, "ly": 2.2,
   "hud": {"type": "bars", "rows": [{"label": "APR", "v": 598, "c": _BLUE}, {"label": "DUC", "v": 589, "c": _RED}], "min": 560, "max": 600, "hi": 0}},
  # 4 второе место
  {"type": "stage", "items": [{"o": "bike", "c": _BLUE, "x": -1.4, "lean": 0.3, "s": 1.15, "y": 0.4}, {"o": "bike", "c": "#8ea0ff", "x": 1.5, "lean": -0.3, "s": 1.15, "y": 0.4}], "bg": "blue",
   "r": 8, "r2": 7, "h": 1.6, "h2": 1.9, "a0": -0.6, "a1": 0.4, "spin": 0.3, "ly": 2.2,
   "hud": {"type": "bars", "rows": [{"label": "MAR", "v": 396, "c": "#8ea0ff"}, {"label": "BEZ", "v": 394, "c": _BLUE}], "min": 380, "max": 400, "hi": 0}},
  # 5 Moto2
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 6, "dist2": 5.5, "h": 2.4, "h2": 2.2, "side": 2, "side2": -1.6, "look": 22, "drop": 2, "noCut": True, "act": {"type": "motogp", "at": 0.62, "pass": 1}},
  # 6 Moto2 очки
  {"type": "stage", "items": [{"o": "bike", "c": "#ffb020", "x": -1.4, "lean": 0.3, "s": 1.1, "y": 0.4}, {"o": "bike", "c": "#26c281", "x": 1.5, "lean": -0.3, "s": 1.1, "y": 0.4}], "bg": "gold",
   "r": 8, "r2": 7, "h": 1.6, "h2": 1.9, "a0": 0.5, "a1": -0.5, "spin": 0.3, "ly": 2.2},
  # 7 прощания
  {"type": "chase", "follow": "bike", "fi": 5, "dist": 8, "dist2": 7, "h": 3.2, "h2": 3, "side": -2.0, "side2": 2, "look": 30, "drop": 3, "noCut": True, "act": {"type": "motogp", "at": 0.3}},
  # 9 конец эпохи 1000 кубов
  {"type": "stage", "items": [{"o": "bike", "c": _RED, "x": 0, "lean": 0.25, "s": 1.3, "y": 0.4}], "bg": "gold", "beams": True,
   "r": 8, "r2": 7.2, "h": 1.8, "h2": 1.6, "a0": 0.5, "a1": -0.4, "spin": 0.2, "ly": 1.8},
  # 10 финал
  {"type": "fly", "from": 0.0, "to": 0.08, "h": 60, "h2": 140, "side": -40, "ahead": 260}
 ],
 "coverShot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 7, "h": 2.8, "side": -2.2, "look": 20, "drop": 2, "act": {"type": "motogp", "at": 0.12}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 7, "h": 2.8, "side": -2.2, "look": 20, "drop": 2, "fov": 42, "act": {"type": "motogp", "at": 0.12}}},
  {"name": "pack", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 9, "h": 3.6, "side": 1.6, "look": 22, "drop": 3, "fov": 44, "act": {"type": "motogp", "at": 0.4}}},
  {"name": "duel", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "bike", "c": _BLUE, "x": -1.4, "lean": 0.3, "s": 1.15, "y": 0.4}, {"o": "bike", "c": "#8ea0ff", "x": 1.5, "lean": -0.3, "s": 1.15, "y": 0.4}], "bg": "blue",
            "r": 8, "h": 1.7, "a0": -0.3, "spin": 0, "ly": 2.0}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "chip": "Последняя гонка эпохи 1000 кубов",
    "say": "Чемпион уже известен, но Валенсия решит ещё три вопроса. Это последняя гонка эпохи тысячи кубов.",
    "hl": ["три вопроса", "тысячи кубов"]},
   {"kind": "big", "chip": "Aprilia 598 · Ducati 589", "min": 5.6,
    "say": "Первый вопрос: зачёт производителей. Априлия впереди на девять очков, Дукати нужно набрать минимум на десять больше.",
    "hl": ["девять очков", "десять"]},
   {"kind": "big", "chip": "Мартин 396 · Беццекки 394",
    "say": "Второй вопрос: второе место среди пилотов. Мартин опережает Беццекки на два очка, оба на Априлии.",
    "hl": ["Мартин", "два очка"]},
   {"kind": "big", "chip": "Moto2 · третий вопрос",
    "say": "Третий вопрос: титул в Мото два. Он решится в последней гонке.",
    "hl": ["Мото два", "последней гонке"]},
   {"kind": "big", "chip": "Гонсалес 286,5 · Гевара 282", "min": 4.6,
    "say": "Гонсалес впереди на четыре с половиной очка. Если Гевара выиграет, он чемпион, даже при втором месте Гонсалеса.",
    "hl": ["четыре с половиной", "выиграет"]},
   {"kind": "big", "chip": "Прощания и замены", "min": 5.4,
    "say": "Для многих это прощание: Мартин уходит в Ямаху, Миллер и Биндер в супербайк. Баньяя и Виньялес финал пропустят.",
    "hl": ["Мартин", "супербайк"]},
   {"kind": "big", "chip": "С 2027 года моторы 850 кубов",
    "say": "С две тысячи двадцать седьмого Мотоджипи переходит на восемьсот пятьдесят кубов. Тысячи кубов больше не будет.",
    "hl": ["восемьсот пятьдесят", "не будет"]},
   {"kind": "end", "tag": "Валенсия · 27–29 ноября",
    "say": "Во сколько гонка по вашему времени, смотрите на ЛапРадар.",
    "hl": ["ЛапРадар"]}
  ],
  "en": [
   {"kind": "big", "chip": "Last race of the 1000cc era",
    "say": "The champion is known, but Valencia still settles three questions. It is the last thousand cc race.",
    "hl": ["three questions", "thousand cc"]},
   {"kind": "big", "chip": "Aprilia 598 · Ducati 589", "min": 5.6,
    "say": "Question one: constructors. Aprilia lead by nine points, and Ducati need at least ten more than them.",
    "hl": ["nine points", "ten"]},
   {"kind": "big", "chip": "Martín 396 · Bezzecchi 394",
    "say": "Question two: second place among the riders. Martín leads Bezzecchi by two points, both on Aprilia.",
    "hl": ["Martín", "two points"]},
   {"kind": "big", "chip": "Moto2 · question three",
    "say": "Question three: the Moto2 title. It goes down to the last race.",
    "hl": ["Moto2", "last race"]},
   {"kind": "big", "chip": "González 286.5 · Guevara 282", "min": 4.6,
    "say": "González leads by four and a half points. If Guevara wins, he is champion, even with González second.",
    "hl": ["four and a half", "wins"]},
   {"kind": "big", "chip": "Farewells and stand-ins", "min": 5.4,
    "say": "A farewell for many: Martín heads to Yamaha, Miller and Binder to WorldSBK. Bagnaia and Viñales miss out.",
    "hl": ["Martín", "WorldSBK"]},
   {"kind": "big", "chip": "850cc engines from 2027",
    "say": "From twenty twenty-seven MotoGP moves to eight hundred fifty cc. The thousand is history.",
    "hl": ["eight hundred fifty", "history"]},
   {"kind": "end", "tag": "Valencia · 27–29 Nov",
    "say": "Check the race start in your own time zone on LapRadar.",
    "hl": ["LapRadar"]}
  ]
 }
}

# Викторина «Какой ты фанат F1? Средний уровень», выпуск 1 (одобрено Давидом: только ролик ru+en, на сайт не добавляем, 2 ролика в неделю).
# Формат как у quiz_easy1.py: карточка-крючок «Вы просили, мы делаем сложнее» (диктор говорит её в самом начале), 6 вопросов (kind "quiz"),
# 3 секунды отсчёта, ответ (quiz.reveal) с пояснением, «Считай очки», финал. Вопросы чуть сложнее лёгкого уровня, но популярные;
# вопрос 5 технический «с подвохом» (диктор так его и объявляет): MGU-H убрали в 2026, турбина осталась.
# Ответы сверены по двум источникам на 21.11.2026 (ссылки в tools/topics.md); вопросов, ответ на которые может поменять гонка в Вегасе, нет.
# HQ, Монца днём (вопрос 3 как раз про неё), машины в условных цветах без логотипов.
_CPS, _CD = 17.5, 3


def _ask(tag, q, opts, ans, say, abc):
    return {"kind": "quiz", "say": say, "min": round(len(say) / _CPS + 0.55 + _CD + 0.3, 2),
            "quiz": {"tag": tag, "q": q, "opts": opts, "ans": ans, "abc": abc, "cd": _CD}}


def _rev(ask, say, hl=None):
    return {"kind": "quiz", "say": say, "min": 3.4, "hl": hl or [], "quiz": {**ask["quiz"], "reveal": True, "cd": 0}}


def _qs(items, abc, tag):
    out = []
    for k, (q, opts, ans, s_ask, s_rev, hl) in enumerate(items):
        a = _ask(tag.format(k + 1), q, opts, ans, s_ask, abc); out += [a, _rev(a, s_rev, hl)]
    return out


_P = {"0": {"c": "#b91c1c", "a": "#f8fafc", "p": "stripe"}, "1": {"c": "#0f766e", "a": "#fbbf24", "p": "band"},
      "2": {"c": "#1e293b", "a": "#38bdf8", "p": "split"}, "3": {"c": "#e5e7eb", "a": "#7c3aed", "p": "fade"}}
_CV = {"type": "convoy", "at": "straight", "n": 4, "v": 60}
_ORB = lambda a0, a1, t0=0: {"type": "carorbit", "car": 0, "r": 11, "r2": 10, "h": 2.2, "h2": 1.7, "a0": a0, "a1": a1, "fov": 48, "ly": 0.8, "paint": _P, "act": {**_CV, "v": 16, "n": 1, "t0": t0}}
_CAR = lambda c, a, p, bg, a0=-0.4, a1=0.3: {"type": "stage", "items": [{"o": "f1", "c": c, "a": a, "p": p, "x": -1.6, "ry": 0.35}, {"o": "trophy", "x": 2.4, "y": 0, "s": 0.55}], "bg": bg, "confetti": True, "r": 12, "r2": 10.5, "h": 3, "h2": 3.6, "a0": a0, "a1": a1, "spin": 0, "ly": 1.0}

_RU = [
 ("В каком году прошёл первый чемпионат мира F1?", ["1946", "1950", "1958"], 1,
  "Вопрос первый. Когда прошёл первый чемпионат мира? В сорок шестом, пятидесятом или пятьдесят восьмом?",
  "В пятидесятом! Первую гонку выиграл Джузеппе Фарина, он же стал первым чемпионом.", ["пятидесятом!"]),
 ("У кого больше всего побед в Гран-при?", ["Льюис Хэмилтон", "Михаэль Шумахер", "Макс Ферстаппен"], 0,
  "Вопрос второй. У кого больше всего побед в Гран-при? Хэмилтон, Шумахер или Ферстаппен?",
  "Льюис Хэмилтон, больше ста побед! У Шумахера девяносто одна.", ["Хэмилтон,", "ста"]),
 ("Какую трассу называют «храмом скорости»?", ["Монако", "Сильверстоун", "Монца"], 2,
  "Вопрос третий. Какую трассу называют храмом скорости? Монако, Сильверстоун или Монца?",
  "Монца! Длинные прямые, почти весь круг газ в пол. Её вы сейчас и видите.", ["Монца!"]),
 ("У какой команды больше всего Кубков конструкторов?", ["McLaren", "Ferrari", "Mercedes"], 1,
  "Вопрос четвёртый. У кого больше всего Кубков конструкторов? Макларен, Феррари или Мерседес?",
  "Феррари, шестнадцать титулов! У Макларена десять, у Мерседеса девять.", ["шестнадцать"]),
 ("Чего больше нет в моторе F1 с 2026 года?", ["Турбины", "MGU-H", "MGU-K"], 1,
  "А теперь вопрос с подвохом! Чего нет в моторе Формулы один с двадцать шестого года? Турбины, эм джи ю эйч или эм джи ю кей?",
  "Эм джи ю эйч! Его убрали: турбина осталась, а эм джи ю кей стал почти втрое мощнее.", ["убрали:"]),
 ("Кто самый молодой чемпион мира в истории F1?", ["Себастьян Феттель", "Макс Ферстаппен", "Кими Антонелли"], 2,
  "Последний вопрос. Кто самый молодой чемпион мира в истории? Феттель, Ферстаппен или Антонелли?",
  "Кими Антонелли! В этом году он взял титул в двадцать лет и побил рекорд Феттеля.", ["Антонелли!"]),
]
_EN = [
 ("When was the first F1 world championship held?", ["1946", "1950", "1958"], 1,
  "Question one. When was the first world championship? Nineteen forty-six, fifty, or fifty-eight?",
  "Nineteen fifty! Giuseppe Farina won the first race and became the first champion.", ["fifty!"]),
 ("Who has the most Grand Prix wins?", ["Lewis Hamilton", "Michael Schumacher", "Max Verstappen"], 0,
  "Question two. Who has the most Grand Prix wins? Hamilton, Schumacher, or Verstappen?",
  "Lewis Hamilton, with more than a hundred! Schumacher has ninety-one.", ["Hamilton,", "hundred!"]),
 ("Which track is called the Temple of Speed?", ["Monaco", "Silverstone", "Monza"], 2,
  "Question three. Which track is called the Temple of Speed? Monaco, Silverstone, or Monza?",
  "Monza! Long straights and flat out for almost the whole lap. That's the track you're looking at.", ["Monza!"]),
 ("Which team has the most Constructors' titles?", ["McLaren", "Ferrari", "Mercedes"], 1,
  "Question four. Which team has the most Constructors' titles? McLaren, Ferrari, or Mercedes?",
  "Ferrari, with sixteen! McLaren has ten, Mercedes nine.", ["sixteen!"]),
 ("What's no longer in an F1 power unit since 2026?", ["The turbo", "The MGU-H", "The MGU-K"], 1,
  "Now a trick question! What's gone from the Formula One power unit since twenty twenty-six? The turbo, the MGU-H, or the MGU-K?",
  "The MGU-H! The turbo stayed, and the MGU-K got almost three times more powerful.", ["MGU-H"]),
 ("Who is the youngest world champion in F1 history?", ["Sebastian Vettel", "Max Verstappen", "Kimi Antonelli"], 2,
  "Last one. Who is the youngest world champion in history? Vettel, Verstappen, or Antonelli?",
  "Kimi Antonelli! He won the title this year at twenty, beating Vettel's record.", ["Antonelli!"]),
]

VIDEO = {
 "slug": "f1-fan-quiz-medium-1",
 "id": "f1-fan-quiz-medium-1",
 "track": "monza",
 "theme": "day",
 "hq": True,
 "titles": {"ru": "Какой ты фанат F1? Средний уровень", "en": "How big an F1 fan are you? Medium level"},
 "captions": {
  "ru": "Вы просили, мы делаем сложнее! Какой ты фанат F1? 6 вопросов, средний уровень, 3 секунды на ответ. Пиши свой счёт в комментариях! Живая карта гонок: lapradar.com",
  "en": "You asked, we're making it harder! How big an F1 fan are you? 6 questions, medium level, 3 seconds each. Drop your score in the comments! Live race map: lapradar.com",
 },
 "coverText": {"ru": {"head": "Какой ты фанат F1?", "sub": "Средний уровень"}, "en": {"head": "How big an F1 fan are you?", "sub": "Medium level"}},
 "shots": [
  # крючок: «Вы просили, мы делаем сложнее»
  {"type": "chase", "car": 0, "dist": 13, "dist2": 11, "h": 5, "h2": 4.2, "side": 0, "side2": 1.2, "look": 30, "drop": 3, "noCut": True, "paint": _P, "act": {**_CV}},
  # 1: первый чемпионат
  _ORB(0.7, 1.4),
  {"type": "side", "car": 0, "side": 6.5, "side2": 6, "h": 1.0, "h2": 1.3, "fw": 2.5, "fw2": -1.5, "look": 0.5, "ly": 0.9, "fov": 52, "paint": _P, "act": {**_CV, "v": 40, "n": 1}},
  # 2: больше всех побед
  {"type": "chase", "car": 3, "dist": 30, "dist2": 26, "h": 12, "h2": 10, "side": 3, "look": 30, "drop": 3, "fov": 50, "noCut": True, "paint": _P, "act": {**_CV, "v": 50}},
  _CAR("#1e293b", "#38bdf8", "split", "blue"),
  # 3: храм скорости (пролёт над Монцей)
  {"type": "fly", "from": 0.12, "to": 0.2, "h": 90, "h2": 70, "side": 40, "ahead": 240},
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10.5, "h": 4.5, "h2": 4, "side": -1.2, "side2": 1.2, "look": 24, "drop": 3, "noCut": True, "paint": _P, "act": {**_CV, "n": 2, "t0": 2}},
  # 4: Кубки конструкторов
  _ORB(-1.2, -0.5, 2),
  _CAR("#b91c1c", "#f8fafc", "stripe", "red", 0.4, -0.3),
  # 5: вопрос с подвохом: MGU-H убрали в 2026
  {"type": "side", "car": 0, "side": -6.5, "side2": -6, "h": 1.0, "h2": 1.3, "fw": 0.5, "fw2": 2.5, "look": 0.5, "ly": 0.9, "fov": 52, "paint": _P, "act": {**_CV, "v": 40, "n": 1}},
  _ORB(-0.4, 0.3, 6),
  # 6: самый молодой чемпион
  _ORB(0.4, 1.1, 4),
  _CAR("#e5e7eb", "#7c3aed", "fade", "gold"),
  # итог и финал
  {"type": "stage", "items": [{"o": "podium"}, {"o": "trophy", "x": 0, "y": 1.2, "s": 0.6}], "bg": "gold", "confetti": True, "beams": True, "r": 12, "r2": 10, "h": 3.2, "h2": 3.8, "a0": -0.5, "a1": 0.4, "spin": 0.2, "ly": 1.2},
  {"type": "fly", "from": 0.02, "to": 0.08, "h": 70, "h2": 150, "side": 40, "ahead": 260}
 ],
 "coverShot": {"type": "chase", "car": 3, "dist": 12, "h": 3.4, "side": 1.5, "look": 24, "drop": 2, "fov": 44, "paint": _P, "act": {**_CV, "v": 6}},
 "scenes": {
  "ru": [
   {"kind": "quizend", "head": "Вы просили, мы делаем сложнее", "rows": ["Какой ты фанат F1?", "Средний уровень", "6 вопросов · 3 секунды"],
    "say": "Вы просили, мы делаем сложнее! Какой ты фанат Формулы один? Средний уровень!", "hl": ["сложнее!", "Средний"]},
   *_qs(_RU, ["А", "Б", "В"], "Вопрос {} из 6"),
   {"kind": "quizend", "head": "Считай очки", "rows": ["6/6 · настоящий знаток", "4–5 · крепкий фанат", "0–3 · начни с лёгкого уровня"],
    "say": "Шесть из шести: ты настоящий знаток! Четыре или пять: крепкий фанат. Меньше: начни с лёгкого уровня.", "hl": ["знаток!"]},
   {"kind": "end", "tag": "Викторина · средний уровень",
    "say": "Пиши свой счёт в комментариях, а гонки смотри на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "quizend", "head": "You asked, we're making it harder", "rows": ["How big an F1 fan are you?", "Medium level", "6 questions · 3 seconds"],
    "say": "You asked, we're making it harder! How big a Formula One fan are you? Medium level!", "hl": ["harder!", "Medium"]},
   *_qs(_EN, ["A", "B", "C"], "Question {} of 6"),
   {"kind": "quizend", "head": "Count your points", "rows": ["6/6 · Real expert", "4–5 · Solid fan", "0–3 · Try the easy level first"],
    "say": "Six out of six: you're a real expert! Four or five: a solid fan. Fewer: try the easy level first.", "hl": ["expert!"]},
   {"kind": "end", "tag": "F1 quiz · medium level",
    "say": "Drop your score in the comments, and follow the races on the LapRadar live map."}
  ]
 }
}

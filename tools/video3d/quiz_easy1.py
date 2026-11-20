# Викторина «Какой ты фанат F1? Лёгкий уровень», выпуск 1 (одобрено Давидом: только ролик ru+en, на сайт не добавляем, 2 ролика в неделю).
# Формат: вопрос и 3 варианта (kind "quiz"), в последние 3 секунды сцены обратный отсчёт без озвучки, затем ответ (quiz.reveal) с пояснением.
# Ответы сверены по двум источникам с учётом правил 2026 года (ссылки в tools/topics.md). HQ, Сильверстоун днём, машины в условных цветах без логотипов.
# Длительность сцены вопроса: оценка озвучки (как в render.py: символы / 17,5 + 0,55 с) плюс 3,3 с на отсчёт.
_CPS, _CD = 17.5, 3


def _ask(tag, q, opts, ans, say, abc):
    return {"kind": "quiz", "say": say, "min": round(len(say) / _CPS + 0.55 + _CD + 0.3, 2),
            "quiz": {"tag": tag, "q": q, "opts": opts, "ans": ans, "abc": abc, "cd": _CD}}


def _rev(ask, say, hl=None):
    return {"kind": "quiz", "say": say, "min": 3.4, "hl": hl or [], "quiz": {**ask["quiz"], "reveal": True, "cd": 0}}


def _qs(lang, items, abc, tag):
    out = []
    for k, (q, opts, ans, s_ask, s_rev, hl) in enumerate(items):
        a = _ask(tag.format(k + 1), q, opts, ans, s_ask, abc); out += [a, _rev(a, s_rev, hl)]
    return out


_P = {"0": {"c": "#ff8000", "a": "#111827", "p": "band"}, "1": {"c": "#d61f1f", "a": "#f8fafc", "p": "stripe"},
      "2": {"c": "#1e2a5a", "a": "#ef4444", "p": "split"}, "3": {"c": "#c7ccd4", "a": "#14b8a6", "p": "fade"}}
_CV = {"type": "convoy", "at": "straight", "n": 4, "v": 60}
_ORB = lambda a0, a1, t0=0: {"type": "carorbit", "car": 0, "r": 11, "r2": 10, "h": 2.2, "h2": 1.7, "a0": a0, "a1": a1, "fov": 48, "ly": 0.8, "paint": _P, "act": {**_CV, "v": 16, "n": 1, "t0": t0}}

_RU = [
 ("Сколько очков получает победитель гонки?", ["10 очков", "18 очков", "25 очков"], 2,
  "Вопрос первый. Сколько очков получает победитель гонки? Десять, восемнадцать или двадцать пять?",
  "Правильно: двадцать пять! А за десятое место дают всего одно очко.", ["двадцать", "пять!"]),
 ("Кто стал чемпионом мира F1 в 2025 году?", ["Ландо Норрис", "Макс Ферстаппен", "Оскар Пиастри"], 0,
  "Вопрос второй. Кто стал чемпионом мира в двадцать пятом году? Норрис, Ферстаппен или Пиастри?",
  "Ландо Норрис! Он обошёл Ферстаппена всего на два очка.", ["Норрис!"]),
 ("Сколько машин выходит на старт гонки в 2026 году?", ["20 машин", "22 машины", "24 машины"], 1,
  "Вопрос третий. Сколько машин выходит на старт в двадцать шестом году? Двадцать, двадцать две или двадцать четыре?",
  "Двадцать две! С приходом Cadillac команд стало одиннадцать, по две машины в каждой.", ["две!"]),
 ("Что значит синий флаг?", ["Опасность, обгоны запрещены", "Гонка остановлена", "Тебя догоняют на круг: пропусти"], 2,
  "Вопрос четвёртый. Что значит синий флаг? Опасность, остановка гонки или тебя догоняют на круг?",
  "Тебя догоняют на круг, пропусти быструю машину. За три пропущенных синих флага могут наказать.", ["пропусти"]),
 ("Сколько титулов чемпиона мира у Льюиса Хэмилтона?", ["7 титулов", "6 титулов", "5 титулов"], 0,
  "Вопрос пятый. Сколько титулов чемпиона мира у Льюиса Хэмилтона? Семь, шесть или пять?",
  "Семь! Столько же у Михаэля Шумахера, это общий рекорд.", ["Семь!"]),
 ("Сколько составов сухих шин Pirelli привозит на этап?", ["2 состава", "3 состава", "5 составов"], 1,
  "Последний вопрос. Сколько составов сухих шин Пирелли привозит на этап? Два, три или пять?",
  "Три: мягкие, средние и жёсткие. Их выбирают из пяти составов сезона.", ["Три:"]),
]
_EN = [
 ("How many points does the race winner get?", ["10 points", "18 points", "25 points"], 2,
  "Question one. How many points does the race winner get? Ten, eighteen, or twenty-five?",
  "Twenty-five! Tenth place gets just one point.", ["Twenty-five!"]),
 ("Who won the 2025 F1 world title?", ["Lando Norris", "Max Verstappen", "Oscar Piastri"], 0,
  "Question two. Who won the twenty twenty-five world title? Norris, Verstappen, or Piastri?",
  "Lando Norris! He beat Verstappen by just two points.", ["Norris!"]),
 ("How many cars start a race in 2026?", ["20 cars", "22 cars", "24 cars"], 1,
  "Question three. How many cars start a race in twenty twenty-six? Twenty, twenty-two, or twenty-four?",
  "Twenty-two! Cadillac made it eleven teams, with two cars each.", ["Twenty-two!"]),
 ("What does the blue flag mean?", ["Danger, no overtaking", "The race is stopped", "You're being lapped: let them by"], 2,
  "Question four. What does the blue flag mean? Danger, race stopped, or you're about to be lapped?",
  "You're about to be lapped, so let the faster car through. Ignore three blue flags and you can get a penalty.", ["lapped,"]),
 ("How many world titles does Lewis Hamilton have?", ["7 titles", "6 titles", "5 titles"], 0,
  "Question five. How many world titles does Lewis Hamilton have? Seven, six, or five?",
  "Seven! The same as Michael Schumacher, a shared record.", ["Seven!"]),
 ("How many dry tyre compounds does Pirelli bring to a race weekend?", ["2 compounds", "3 compounds", "5 compounds"], 1,
  "Last one. How many dry tyre compounds does Pirelli bring to a race weekend? Two, three, or five?",
  "Three: soft, medium and hard, picked from this season's five compounds.", ["Three:"]),
]

VIDEO = {
 "slug": "f1-fan-quiz-easy-1",
 "id": "f1-fan-quiz-easy-1",
 "track": "silverstone",
 "theme": "day",
 "hq": True,
 "titles": {"ru": "Какой ты фанат F1? Лёгкий уровень", "en": "How big an F1 fan are you? Easy level"},
 "captions": {
  "ru": "Какой ты фанат F1? 6 вопросов, лёгкий уровень, 3 секунды на ответ. Пиши свой счёт в комментариях! Живая карта гонок: lapradar.com",
  "en": "How big an F1 fan are you? 6 questions, easy level, 3 seconds each. Drop your score in the comments! Live race map: lapradar.com",
 },
 "shots": [
  {"type": "chase", "car": 0, "dist": 13, "dist2": 11, "h": 5, "h2": 4.2, "side": 0, "side2": 1.2, "look": 30, "drop": 3, "noCut": True, "paint": _P, "act": {**_CV}},
  # 1: очки за победу
  _ORB(0.7, 1.4),
  {"type": "side", "car": 0, "side": 6.5, "side2": 6, "h": 1.0, "h2": 1.3, "fw": 2.5, "fw2": -1.5, "look": 0.5, "ly": 0.9, "fov": 52, "paint": _P, "act": {**_CV, "v": 40, "n": 1}},
  # 2: чемпион 2025
  {"type": "fly", "from": 0.12, "to": 0.2, "h": 90, "h2": 70, "side": 40, "ahead": 240},
  {"type": "stage", "items": [{"o": "f1", "c": "#ff8000", "a": "#111827", "p": "band", "x": -1.6, "ry": 0.35}, {"o": "trophy", "x": 2.4, "y": 0, "s": 0.55}], "bg": "gold", "confetti": True, "r": 12, "r2": 10.5, "h": 3, "h2": 3.6, "a0": -0.4, "a1": 0.3, "spin": 0, "ly": 1.0},
  # 3: сколько машин
  {"type": "chase", "car": 3, "dist": 30, "dist2": 26, "h": 12, "h2": 10, "side": 3, "look": 30, "drop": 3, "fov": 50, "noCut": True, "paint": _P, "act": {**_CV, "v": 50}},
  {"type": "flyby", "car": 0, "side": 8, "h": 1.4, "mid": 0.5, "fov": 40, "fov2": 32, "ly": 0.8, "paint": _P, "act": {**_CV, "v": 55}},
  # 4: синий флаг
  _ORB(-1.2, -0.5, 2),
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10.5, "h": 4.5, "h2": 4, "side": -1.2, "side2": 1.2, "look": 24, "drop": 3, "noCut": True, "paint": _P, "act": {**_CV, "n": 2, "t0": 2}},
  # 5: титулы Хэмилтона
  {"type": "fly", "from": 0.55, "to": 0.63, "h": 90, "h2": 70, "side": -40, "ahead": 240},
  {"type": "stage", "items": [{"o": "trophy", "x": 0, "y": 0, "s": 0.8}], "bg": "gold", "beams": True, "r": 9, "r2": 8, "h": 2.2, "h2": 2.8, "a0": -0.3, "a1": 0.4, "spin": 0.4, "ly": 1.2},
  # 6: шины
  _ORB(0.4, 1.1, 4),
  {"type": "side", "car": 0, "side": -6.5, "side2": -6, "h": 1.0, "h2": 1.3, "fw": 0.5, "fw2": 2.5, "look": 0.5, "ly": 0.9, "fov": 52, "paint": _P, "act": {**_CV, "v": 40, "n": 1}},
  # итог и финал
  {"type": "stage", "items": [{"o": "podium"}, {"o": "trophy", "x": 0, "y": 1.2, "s": 0.6}], "bg": "blue", "confetti": True, "beams": True, "r": 12, "r2": 10, "h": 3.2, "h2": 3.8, "a0": -0.5, "a1": 0.4, "spin": 0.2, "ly": 1.2},
  {"type": "fly", "from": 0.02, "to": 0.08, "h": 70, "h2": 150, "side": 40, "ahead": 260}
 ],
 "coverShot": {"type": "chase", "car": 3, "dist": 12, "h": 3.4, "side": 1.5, "look": 24, "drop": 2, "fov": 44, "paint": _P, "act": {**_CV, "v": 6}},
 "scenes": {
  "ru": [
   {"kind": "title", "head": "КАКОЙ ТЫ ФАНАТ F1?", "sub": "Лёгкий уровень", "chip": "Какой ты фанат F1?",
    "say": "Какой ты фанат Формулы один? Шесть простых вопросов, на каждый три секунды. Считай свои очки!", "hl": ["фанат", "очки!"]},
   *_qs("ru", _RU, ["А", "Б", "В"], "Вопрос {} из 6"),
   {"kind": "quizend", "head": "Считай очки", "rows": ["6/6 · настоящий фанат", "4–5 · крепкий болельщик", "0–3 · пора смотреть гонки"],
    "say": "Шесть из шести: ты настоящий фанат! Четыре или пять: крепкий болельщик. Меньше: самое время смотреть гонки.", "hl": ["фанат!"]},
   {"kind": "end", "tag": "Викторина · лёгкий уровень",
    "say": "Пиши свой счёт в комментариях, а гонки смотри на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "HOW BIG AN F1 FAN ARE YOU?", "sub": "Easy level", "chip": "How big an F1 fan are you?",
    "say": "How big a Formula One fan are you? Six easy questions, three seconds each. Keep score!", "hl": ["fan", "score!"]},
   *_qs("en", _EN, ["A", "B", "C"], "Question {} of 6"),
   {"kind": "quizend", "head": "Count your points", "rows": ["6/6 · True fan", "4–5 · Solid fan", "0–3 · Time to watch more races"],
    "say": "Six out of six: you're a true fan! Four or five: a solid fan. Fewer: time to watch more races.", "hl": ["true"]},
   {"kind": "end", "tag": "F1 quiz · easy level",
    "say": "Drop your score in the comments, and follow the races on the LapRadar live map."}
  ]
 }
}

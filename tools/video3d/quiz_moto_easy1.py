# Викторина «Угадаешь? Автоспорт за пределами F1. Лёгкий уровень», выпуск 1 (только ролик ru+en, на сайт не добавляем).
# Формат как у quiz_easy1.py: 6 вопросов по одному на серию (Ле-Ман, MotoGP, Формула E, NASCAR, IndyCar, WRC), 3 секунды отсчёта, ответ с пояснением, «Считай очки», финал.
# Ответы сверены по двум источникам на 21.11.2026 (ссылки в tools/topics.md). HQ, овал днём; машины, мотоциклы и сток-кары в условных цветах без логотипов.
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


_P = {"0": {"c": "#2563eb", "a": "#facc15", "p": "band"}, "1": {"c": "#f97316", "a": "#111827", "p": "stripe"},
      "2": {"c": "#16a34a", "a": "#f8fafc", "p": "split"}, "3": {"c": "#e5e7eb", "a": "#dc2626", "p": "fade"}}
_CV = {"type": "convoy", "at": "straight", "n": 4, "v": 60}
_STOCK = lambda at, side=0, side2=0, p=0: {"type": "chase", "follow": "stock", "fi": 7, "dist": 13, "dist2": 11, "h": 5.5, "h2": 4.8, "side": side, "side2": side2, "look": 32, "drop": 10, "noCut": True, "act": {"type": "stockpack", "at": at, "pass": p}}
_BIKE = lambda at, side=-2.2, side2=1.8: {"type": "chase", "follow": "bike", "fi": 5, "dist": 8, "dist2": 6.5, "h": 3.2, "h2": 2.8, "side": side, "side2": side2, "look": 22, "drop": 2, "noCut": True, "act": {"type": "motogp", "at": at}}

_RU = [
 ("Сколько длится главная гонка в Ле-Мане?", ["6 часов", "12 часов", "Целые сутки"], 2,
  "Вопрос первый. Сколько длится главная гонка в Ле-Мане? Шесть часов, двенадцать или сутки?",
  "Целые сутки, двадцать четыре часа! Пилоты по очереди сменяют друг друга за рулём.", ["сутки,"]),
 ("Под каким номером гонялся Валентино Росси?", ["№ 93", "№ 46", "№ 99"], 1,
  "Вопрос второй. Какой номер был у Валентино Росси? Девяносто три, сорок шесть или девяносто девять?",
  "Сорок шесть! С двадцать второго года этот номер в МотоДжиПи навсегда закреплён за Росси.", ["Сорок", "шесть!"]),
 ("На чём едут машины Формулы E?", ["На бензине", "На электричестве", "На водороде"], 1,
  "Вопрос третий. На чём едут машины Формулы E? На бензине, электричестве или водороде?",
  "Только на электричестве! Так было с самой первой гонки в Пекине в четырнадцатом году.", ["электричестве!"]),
 ("Куда поворачивают машины NASCAR на овалах?", ["Только налево", "Только направо", "То налево, то направо"], 0,
  "Вопрос четвёртый. Куда поворачивают машины НАСКАР на овалах? Налево, направо или по очереди?",
  "Только налево: на овалах едут против часовой стрелки. Направо поворачивают только на шоссейных трассах.", ["налево:"]),
 ("Где проходит гонка Indy 500?", ["На улицах Монако", "На овале в Индианаполисе", "На трассе в Дайтоне"], 1,
  "Вопрос пятый. Где проходит гонка Инди пятьсот? В Монако, Индианаполисе или Дайтоне?",
  "В Индианаполисе! Двести кругов по овалу, ровно пятьсот миль.", ["Индианаполисе!"]),
 ("У кого рекорд WRC: 9 титулов чемпиона мира по ралли?", ["Себастьен Лёб", "Себастьен Ожье", "У обоих"], 2,
  "Последний вопрос. У кого рекорд ралли, девять титулов чемпиона мира? У Лёба, у Ожье или у обоих?",
  "У обоих! Ожье догнал Лёба в двадцать пятом году, у каждого по девять титулов.", ["обоих!"]),
]
_EN = [
 ("How long is the big race at Le Mans?", ["6 hours", "12 hours", "A full day"], 2,
  "Question one. How long is the big race at Le Mans? Six hours, twelve, or a full day?",
  "A full day, twenty-four hours! Drivers take turns behind the wheel.", ["full", "day,"]),
 ("What number did Valentino Rossi race with?", ["#93", "#46", "#99"], 1,
  "Question two. What number did Valentino Rossi race with? Ninety-three, forty-six, or ninety-nine?",
  "Forty-six! In twenty twenty-two MotoGP retired it for good in his honour.", ["Forty-six!"]),
 ("What powers a Formula E car?", ["Petrol", "Electricity", "Hydrogen"], 1,
  "Question three. What powers a Formula E car? Petrol, electricity, or hydrogen?",
  "Electricity only! That's how it's been since the very first race in Beijing in twenty fourteen.", ["Electricity"]),
 ("Which way do NASCAR cars turn on ovals?", ["Left only", "Right only", "Both ways"], 0,
  "Question four. Which way do NASCAR cars turn on ovals? Left only, right only, or both ways?",
  "Left only: ovals run counterclockwise. They turn right only on road courses.", ["Left"]),
 ("Where is the Indy 500 held?", ["Streets of Monaco", "Oval in Indianapolis", "Track in Daytona"], 1,
  "Question five. Where is the famous Indy five hundred held? Monaco, Indianapolis, or Daytona?",
  "Indianapolis! Two hundred laps of the oval, five hundred miles exactly.", ["Indianapolis!"]),
 ("Who holds the WRC record of 9 world rally titles?", ["Sébastien Loeb", "Sébastien Ogier", "Both of them"], 2,
  "Last one. Who holds the rally record of nine world titles? Loeb, Ogier, or both?",
  "Both! Ogier matched Loeb in twenty twenty-five, nine titles each.", ["Both!"]),
]

VIDEO = {
 "slug": "motorsport-quiz-easy-1",
 "id": "motorsport-quiz-easy-1",
 "track": "oval",
 "theme": "day",
 "hq": True,
 "titles": {"ru": "Угадаешь? Автоспорт за пределами F1. Лёгкий уровень", "en": "Motorsport beyond F1: easy level"},
 "captions": {
  "ru": "Угадаешь? Автоспорт за пределами F1: Ле-Ман, MotoGP, Формула E, NASCAR, IndyCar и ралли. 6 вопросов, 3 секунды на ответ. Пиши свой счёт в комментариях! Живая карта гонок: lapradar.com",
  "en": "Motorsport beyond F1: Le Mans, MotoGP, Formula E, NASCAR, IndyCar and rally. 6 questions, 3 seconds each. Drop your score in the comments! Live race map: lapradar.com",
 },
 "coverText": {"ru": {"head": "Автоспорт за пределами F1", "sub": "Лёгкий уровень"}, "en": {"head": "Motorsport beyond F1", "sub": "Easy level"}},
 "shots": [
  _STOCK(0.02),
  # 1: Ле-Ман
  {"type": "chase", "car": 0, "dist": 13, "dist2": 11, "h": 5, "h2": 4.2, "side": 0, "side2": 1.2, "look": 30, "drop": 3, "noCut": True, "paint": _P, "act": {**_CV}},
  {"type": "stage", "items": [{"o": "f1", "c": "#2563eb", "a": "#facc15", "p": "band", "x": -1.6, "ry": 0.35}, {"o": "trophy", "x": 2.4, "y": 0, "s": 0.55}], "bg": "blue", "confetti": True, "r": 12, "r2": 10.5, "h": 3, "h2": 3.6, "a0": -0.4, "a1": 0.3, "spin": 0, "ly": 1.0},
  # 2: номер Росси
  {"type": "stage", "items": [{"o": "bike", "c": "#facc15", "lean": 0.0, "s": 1.2}], "bg": "red", "r": 9, "r2": 8.5, "h": 1.6, "h2": 1.9, "a0": 0.9, "a1": -0.3, "spin": 0.3, "ly": 2.6},
  {"type": "stage", "items": [{"o": "bike", "c": "#facc15", "x": -1.6, "lean": 0.35, "s": 1.1}, {"o": "trophy", "x": 1.8, "s": 0.9}], "bg": "blue", "confetti": True, "r": 11, "r2": 10, "h": 2.0, "h2": 2.4, "a0": 0.5, "a1": -0.3, "spin": 0, "ly": 2.6},
  # 3: Формула E
  {"type": "carorbit", "car": 0, "r": 11, "r2": 10, "h": 2.2, "h2": 1.7, "a0": 0.7, "a1": 1.4, "fov": 48, "ly": 0.8, "paint": _P, "act": {**_CV, "v": 16, "n": 1}},
  {"type": "side", "car": 0, "side": 6.5, "side2": 6, "h": 1.0, "h2": 1.3, "fw": 2.5, "fw2": -1.5, "look": 0.5, "ly": 0.9, "fov": 52, "paint": _P, "act": {**_CV, "v": 40, "n": 1}},
  # 4: NASCAR
  _STOCK(0.3, 2, -1.5, 1),
  _STOCK(0.55, -2, 2, 3),
  # 5: Indy 500
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10.5, "h": 4.5, "h2": 4, "side": -1.2, "side2": 1.2, "look": 24, "drop": 3, "noCut": True, "paint": _P, "act": {**_CV, "n": 2, "t0": 2}},
  {"type": "chase", "car": 3, "dist": 30, "dist2": 26, "h": 12, "h2": 10, "side": 3, "look": 30, "drop": 3, "fov": 50, "noCut": True, "paint": _P, "act": {**_CV, "v": 50}},
  # 6: рекорд WRC
  {"type": "stage", "items": [{"o": "trophy", "x": -1.2, "y": 0, "s": 0.7}, {"o": "trophy", "x": 1.2, "y": 0, "s": 0.7}], "bg": "blue", "beams": True, "r": 9, "r2": 8, "h": 2.2, "h2": 2.8, "a0": -0.3, "a1": 0.4, "spin": 0.4, "ly": 1.2},
  {"type": "stage", "items": [{"o": "trophy", "x": -1.2, "y": 0, "s": 0.7}, {"o": "trophy", "x": 1.2, "y": 0, "s": 0.7}], "bg": "gold", "confetti": True, "r": 9, "r2": 8, "h": 2.4, "h2": 3.0, "a0": 0.4, "a1": -0.2, "spin": 0.2, "ly": 1.2},
  # итог и финал
  {"type": "stage", "items": [{"o": "podium"}, {"o": "trophy", "x": 0, "y": 1.2, "s": 0.6}], "bg": "blue", "confetti": True, "beams": True, "r": 12, "r2": 10, "h": 3.2, "h2": 3.8, "a0": -0.5, "a1": 0.4, "spin": 0.2, "ly": 1.2},
  {"type": "fly", "from": 0.02, "to": 0.08, "h": 70, "h2": 150, "side": 40, "ahead": 260}
 ],
 "coverShot": {"type": "chase", "follow": "stock", "fi": 7, "dist": 9, "h": 4, "side": 0, "look": 30, "drop": 0, "noCut": True, "act": {"type": "stockpack", "at": 0.02}},
 "scenes": {
  "ru": [
   {"kind": "title", "head": "УГАДАЕШЬ?", "sub": "Автоспорт за пределами F1", "chip": "Автоспорт за пределами F1",
    "say": "Угадаешь? Шесть простых вопросов про гонки без Формулы один. Три секунды на ответ!", "hl": ["Угадаешь?", "Три"]},
   *_qs(_RU, ["А", "Б", "В"], "Вопрос {} из 6"),
   {"kind": "quizend", "head": "Считай очки", "rows": ["6/6 · знаток автоспорта", "4–5 · крепкий болельщик", "0–3 · смотри не только F1"],
    "say": "Шесть из шести: ты знаток автоспорта! Четыре или пять: крепкий болельщик. Меньше: пора смотреть не только Формулу один.", "hl": ["знаток"]},
   {"kind": "end", "tag": "Викторина · лёгкий уровень",
    "say": "Пиши свой счёт в комментариях, а гонки смотри на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "CAN YOU GUESS?", "sub": "Motorsport beyond F1", "chip": "Motorsport beyond F1",
    "say": "Can you guess? Six easy questions about motorsport beyond Formula One. Three seconds each!", "hl": ["guess?", "Three"]},
   *_qs(_EN, ["A", "B", "C"], "Question {} of 6"),
   {"kind": "quizend", "head": "Count your points", "rows": ["6/6 · Motorsport expert", "4–5 · Solid fan", "0–3 · Time to watch beyond F1"],
    "say": "Six out of six: you're a motorsport expert! Four or five: a solid fan. Fewer: time to look beyond Formula One.", "hl": ["expert!"]},
   {"kind": "end", "tag": "Motorsport quiz · easy level",
    "say": "Drop your score in the comments, and follow the races on the LapRadar live map."}
  ]
 }
}

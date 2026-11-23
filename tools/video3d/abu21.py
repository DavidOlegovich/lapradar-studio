# Абу-Даби 2021: финал сезона F1, 369,5 : 369,5 перед гонкой, круг 53 машина безопасности, круг 57 пропустили только пятерых отстающих,
# обгон на последнем круге, протесты, отстранение Мази, отчёт FIA «человеческая ошибка», правило «any» → «all»; потом пять гонок сезона,
# где обе стороны теряли очки (Сильверстоун, Венгрия, Баку, Монца, Джидда), итог 395,5 : 387,5. Текст утверждён Давидом (статья tools/content/abu21.py).
# Нейтрально: без оценок «украли/заслужил», без цитат. HQ-режим, Яс-Марина на закате. Длинный ролик (Давид: «он будет длинным»).
# Машины условные, без ливрей и логотипов: синяя (Red Bull), серебристая (Mercedes), остальные (отстающие) разных цветов.
# Камера (shots) общая для всех языков. Время по городам не называем.
_SIL = {"c": "#c3c8d0", "a": "#1f2937", "p": "stripe"}
_BLU = {"c": "#1e40af", "a": "#e5e7eb", "p": "stripe"}
_LAP = [{"c": "#f97316", "a": "#111827", "p": "band"}, {"c": "#15803d", "a": "#e5e7eb", "p": "split"}, {"c": "#dc2626", "a": "#f8fafc", "p": "fade"},
        {"c": "#f3f4f6", "a": "#2563eb", "p": "band"}, {"c": "#7c3aed", "a": "#facc15", "p": "split"}, {"c": "#0e7490", "a": "#f8fafc", "p": "stripe"},
        {"c": "#facc15", "a": "#111827", "p": "band"}, {"c": "#6b7280", "a": "#f8fafc", "p": "fade"}]
_HQC = lambda d: [d["c"], d["a"], d["p"]]
# по умолчанию: 0 серебристая лидирует, 1 синяя за ней, дальше отстающие
_DEF = {"0": _SIL, "1": _BLU, "2": _LAP[5], "3": _LAP[6], "4": _LAP[7]}
_VS = {"0": _BLU, "1": _SIL}                     # 0 синяя, 1 серебристая
_SV = {"0": _SIL, "1": _BLU}                     # 0 серебристая, 1 синяя
# очередь за машиной безопасности на 53–56 кругах: серебристая, пять отстающих, синяя, за ней отстающий (в студии 8 машин)
_Q = {"0": _SIL, "1": _LAP[0], "2": _LAP[1], "3": _LAP[2], "4": _LAP[3], "5": _LAP[4], "6": _BLU, "7": _LAP[5]}
_CV = {"type": "convoy", "at": "straight", "v": 62, "n": 2}
_TWO = [{"o": "f1", "c": _BLU["c"], "a": _BLU["a"], "p": _BLU["p"], "x": -2.3, "ry": 0.25}, {"o": "f1", "c": _SIL["c"], "a": _SIL["a"], "p": _SIL["p"], "x": 2.3, "ry": -0.25}]

VIDEO = {
 "slug": "abu-dhabi-2021-final",
 "track": "yas-island",
 "theme": "dusk",
 "hq": {"cars": [_HQC(_SIL), _HQC(_BLU)] + [_HQC(x) for x in _LAP[5:]] + [_HQC(x) for x in _LAP[:3]]},
 "coverText": {"ru": {"head": "АБУ-ДАБИ 2021", "sub": "один круг и весь сезон"},
               "en": {"head": "ABU DHABI 2021", "sub": "one lap and a whole season"}},
 "shots": [
  # 1 крючок: серебристая впереди, синяя в 11 м за ней, главная прямая
  {"type": "chase", "car": 1, "dist": 12.5, "dist2": 11.5, "h": 5, "h2": 4.6, "side": 0, "side2": 0, "look": 24, "drop": 3, "noCut": True, "paint": _SV, "act": {**_CV}},
  # 2 равенство очков
  {"type": "stage", "items": _TWO, "bg": "blue", "r": 13, "r2": 11.5, "h": 3, "h2": 3.6, "a0": -0.35, "a1": 0.3, "spin": 0.05, "ly": 0.6,
   "hud": {"type": "bars", "rows": [{"label": "VER", "v": 369.5, "c": "#3b5bdb"}, {"label": "HAM", "v": 369.5, "c": "#c3c8d0"}], "min": 300, "max": 400}},
  # 3 старт: синяя с поула, серебристая проходит
  {"type": "chase", "car": 0, "dist": 19, "dist2": 15, "h": 7, "h2": 6, "side": 2.5, "side2": 2.5, "look": 34, "drop": 3, "noCut": True, "paint": _VS, "act": {"type": "duel"}},
  # 4 круг 1, шестой поворот в конце длинной прямой: серебристая впереди, синяя атакует
  {"type": "chase", "car": 1, "dist": 13, "dist2": 11, "h": 5.5, "h2": 5, "side": 1.5, "side2": -1, "look": 22, "drop": 3, "noCut": True, "paint": _SV, "act": {"type": "convoy", "at": 0.455, "v": 52, "n": 2}},
  # 5 Хэмилтон уезжает: серебристая одна
  {"type": "side", "car": 0, "side": 8.6, "side2": 8.2, "h": 1.2, "h2": 1.5, "fw": 3, "fw2": -1, "look": 0.5, "ly": 0.9, "fov": 58, "paint": _SV, "act": {**_CV, "v": 40, "n": 1}},
  # 6 круг 53: машина безопасности ведёт колонну
  {"type": "chase", "car": 0, "dist": 7, "dist2": 6.8, "h": 3.6, "h2": 3.3, "side": 0, "side2": 0, "look": 30, "drop": 2, "noCut": True, "paint": _DEF, "act": {"type": "restart", "release": 0.99}},
  # 7 шины: свежие мягкие у Ферстаппена (пит-стоп в студии на этой трассе не виден, поэтому три шины крупно)
  {"type": "tyres", "hi": 0},
  # 8 пять отстающих между лидерами: вся очередь за машиной безопасности
  {"type": "chase", "car": 7, "dist": 20, "dist2": 17, "h": 10, "h2": 9, "side": 1.5, "side2": -1, "look": 45, "drop": 4, "noCut": True, "paint": _Q, "act": {"type": "restart", "release": 0.99}},
  # 9 круг 57: решение изменили, пропустили пятерых (синяя теперь сразу за серебристой)
  {"type": "side", "follow": "sc", "side": 7.5, "side2": 7, "h": 1.5, "h2": 1.9, "fw": 2, "fw2": -4, "look": 0, "ly": 1.2, "fov": 54, "paint": _DEF, "act": {"type": "restart", "at": 0.1, "release": 0.99}},
  # 10 машина безопасности уходит, последний круг: синяя за серебристой, сзади трое отстающих
  {"type": "chase", "car": 1, "dist": 14, "dist2": 12, "h": 5.5, "h2": 5, "side": 0, "side2": 1.5, "look": 30, "drop": 3, "noCut": True, "paint": _DEF, "act": {"type": "restart", "at": 0.12, "release": 0.5}},
  # 11 обгон: синяя (машина 1) проходит серебристую (машина 0)
  {"type": "chase", "car": 0, "dist": 19, "dist2": 15, "h": 7, "h2": 6, "side": 2.5, "side2": 2.5, "look": 34, "drop": 3, "noCut": True, "paint": _SV, "act": {"type": "duel"}},
  # 12 протесты и Мази: студия, две машины
  {"type": "stage", "items": _TWO, "bg": "blue", "r": 12.5, "r2": 11, "h": 2.8, "h2": 3.4, "a0": 0.3, "a1": -0.35, "spin": 0.05, "ly": 0.6},
  # 13 отчёт FIA и новое правило: машина безопасности крупно
  {"type": "side", "follow": "sc", "side": -7, "side2": -6.5, "h": 1.2, "h2": 1.6, "fw": 3, "fw2": -3, "look": 0, "ly": 1.1, "fov": 52, "paint": _DEF, "act": {"type": "restart", "at": 0.5, "release": 0.99}},
  # 14 «титул решает не одна гонка»: облёт трассы
  {"type": "orbit", "at": 0.02, "r": 430, "r2": 400, "h": 150, "h2": 120, "a0": 1.0, "a1": 1.35, "fov": 50, "act": {**_CV, "at": 0.0, "v": 45, "n": 2}},
  # 15 Сильверстоун: синяя уходит в занос с дымом, серебристая следом
  {"type": "chase", "car": 0, "dist": 16, "dist2": 13, "h": 6.5, "h2": 5.5, "side": 2, "side2": 0, "look": 20, "drop": 3, "noCut": True, "paint": _VS, "act": {"type": "slide", "followers": [1], "tc": 0.45}},
  # 16 Венгрия: мокрый старт, повреждённая синяя теряет места
  {"type": "chase", "car": 0, "dist": 14, "dist2": 12, "h": 6, "h2": 5.5, "side": 1.5, "side2": -1, "look": 20, "drop": 3, "noCut": True, "rain": True, "band": "#22c55e",
   "paint": {"0": _BLU, "1": _LAP[0], "2": _LAP[1]}, "act": {"type": "fade"}},
  # 17 Баку: лопнувшая шина у синей
  {"type": "chase", "car": 0, "dist": 13, "dist2": 11, "h": 5.5, "h2": 5, "side": -2, "side2": 0, "look": 20, "drop": 3, "noCut": True, "paint": {"0": _BLU}, "act": {"type": "slide", "followers": [], "corner": 4, "tc": 0.5}},
  # 18 Монца: две машины в студии
  {"type": "stage", "items": [{"o": "f1", "c": _BLU["c"], "a": _BLU["a"], "p": _BLU["p"], "x": -1.4, "ry": 0.5}, {"o": "f1", "c": _SIL["c"], "a": _SIL["a"], "p": _SIL["p"], "x": 1.4, "ry": -0.3}],
   "bg": "red", "r": 12, "r2": 10.5, "h": 3.2, "h2": 3.8, "a0": -0.6, "a1": 0.2, "spin": 0.05, "ly": 0.6},
  # 19 Джидда: синяя впереди, серебристая вплотную
  {"type": "chase", "car": 1, "dist": 11, "dist2": 10, "h": 4.5, "h2": 4.2, "side": 0, "side2": 0, "look": 20, "drop": 3, "noCut": True, "paint": _VS, "act": {"type": "follow", "at": 0.3}},
  # 20 итог: кубок и очки
  {"type": "stage", "items": [{"o": "podium"}, {"o": "trophy", "y": 2.2, "s": 0.6}], "bg": "gold", "r": 14, "r2": 12, "h": 4, "h2": 4.5, "a0": -0.3, "a1": 0.3, "spin": 0, "ly": 2.2,
   "hud": {"type": "bars", "rows": [{"label": "VER", "v": 395.5, "c": "#3b5bdb"}, {"label": "HAM", "v": 387.5, "c": "#c3c8d0"}], "min": 300, "max": 400}},
  # 21 финал: облёт старта на закате
  {"type": "orbit", "at": 0.015, "r": 420, "r2": 340, "h": 170, "h2": 130, "a0": 1.0, "a1": 1.5, "fov": 50, "act": {**_CV, "at": 0.0, "v": 45, "n": 2}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 10, "h": 1.5, "a0": 1.9, "a1": 1.9, "fov": 46, "paint": _SV, "act": {**_CV, "v": 1, "n": 2}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 9, "h": 1.4, "a0": 2.3, "a1": 2.3, "fov": 42, "ly": 0.6, "paint": _SV, "act": {**_CV, "v": 1, "n": 2}}},
  {"name": "sc", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 4, "dist": 20, "h": 8, "side": 2, "look": 40, "drop": 4, "fov": 46, "paint": _Q, "act": {"type": "restart", "release": 0.99}}},
  {"name": "duel", "w": 1200, "h": 800, "t": 3.2, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 11, "h": 3.6, "side": 2.5, "look": 18, "drop": 2, "fov": 40, "paint": _SV, "act": {"type": "duel"}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "chip": "Абу-Даби · 12 декабря 2021",
    "say": "Финал сезона, у двух пилотов поровну очков. Как один круг решил титул?",
    "hl": ["поровну", "один", "круг"]},
   {"kind": "big", "chip": "369,5 : 369,5", "barTexts": ["369,5", "369,5"],
    "say": "У обоих по триста шестьдесят девять с половиной. Впервые с семьдесят четвёртого.",
    "hl": ["семьдесят", "четвёртого"]},
   {"kind": "big", "chip": "Старт · поул у Ферстаппена",
    "say": "Ферстаппен стартует с поула, но Хэмилтон обходит его на старте.",
    "hl": ["обходит"]},
   {"kind": "big", "chip": "Круг 1 · поворот 6",
    "say": "Атака Макса в шестом повороте. Хэмилтон срезает шикану, остаётся впереди. Расследования нет.",
    "hl": ["срезает", "шикану"]},
   {"kind": "big", "chip": "Круг 51 из 58 · +11 с",
    "say": "Хэмилтон уезжает. К пятьдесят первому кругу отрыв больше одиннадцати секунд.",
    "hl": ["одиннадцать", "секунд"]},
   {"kind": "big", "chip": "Круг 53 · машина безопасности",
    "say": "Круг пятьдесят три. Латифи разбивает машину, выезжает машина безопасности.",
    "hl": ["машина", "безопасности"]},
   {"kind": "tyres", "head": "", "names": [], "hi": 0, "chip": "Свежие мягкие ↔ старые шины",
    "say": "Ферстаппену ставят свежие мягкие. Хэмилтон на старых, иначе потеряет лидерство.",
    "hl": ["свежие", "мягкие"]},
   {"kind": "big", "chip": "5 отстающих между лидерами",
    "say": "Между лидерами пять отстающих на круг. Сначала сообщают: обгонять им нельзя.",
    "hl": ["пять", "нельзя"]},
   {"kind": "big", "chip": "Круг 57 · директор гонки Мази",
    "say": "Круг пятьдесят семь. Мази меняет решение: обогнать разрешают только пятерым.",
    "hl": ["только", "пятерым"]},
   {"kind": "big", "chip": "Круг 58 · последний",
    "say": "Трое остаются на местах. На последний круг Ферстаппен выходит прямо за Хэмилтоном.",
    "hl": ["последний", "круг"]},
   {"kind": "big", "chip": "Поворот 5 · обгон",
    "say": "Обгон в пятом повороте, и Ферстаппен удерживается до финиша. Он чемпион.",
    "hl": ["чемпион"]},
   {"kind": "big", "chip": "2 протеста · Мази отстранён",
    "say": "Протесты Мерседес отклонены, апелляцию отозвали. В феврале FIA отстранила Мази.",
    "hl": ["отклонены", "отстранила"]},
   {"kind": "big", "chip": "Отчёт FIA · человеческая ошибка",
    "say": "Отчёт FIA: человеческая ошибка, итоги окончательные. Теперь пропускают всех отстающих.",
    "hl": ["человеческая", "ошибка", "всех"]},
   {"kind": "big", "big": "22", "chip": "22 гонки сезона",
    "say": "Но титул решает не одна гонка. До Абу-Даби очки теряли обе стороны.",
    "hl": ["не", "одна", "гонка"]},
   {"kind": "big", "chip": "Сильверстоун · HAM 25 · VER 0",
    "say": "Сильверстоун: столкновение, удар в пятьдесят одно же. Хэмилтон со штрафом побеждает.",
    "hl": ["пятьдесят", "одно", "же"]},
   {"kind": "big", "chip": "Венгрия · HAM 18 · VER 2",
    "say": "Венгрия: завал на мокром старте. У Ферстаппена два очка, у Хэмилтона восемнадцать.",
    "hl": ["два", "восемнадцать"]},
   {"kind": "big", "chip": "Баку · 0 : 0",
    "say": "Баку: у Ферстаппена лопается шина, Хэмилтон ошибается на рестарте. Ноль у обоих.",
    "hl": ["Ноль", "у", "обоих"]},
   {"kind": "big", "chip": "Монца · штраф Ферстаппену",
    "say": "Монца: виноватым признают Ферстаппена. Машины сцепились, сошли оба.",
    "hl": ["сошли", "оба"]},
   {"kind": "big", "chip": "Джидда · +10 с Ферстаппену",
    "say": "Джидда: штраф Ферстаппену за резкое торможение. Хэмилтон побеждает, очки равны.",
    "hl": ["очки", "равны"]},
   {"kind": "big", "chip": "395,5 : 387,5", "barTexts": ["395,5", "387,5"],
    "say": "Итог: восемь очков за двадцать две гонки. Титул складывается из всего сезона.",
    "hl": ["всего", "сезона"]},
   {"kind": "end", "tag": "Абу-Даби 2021 · разбор",
    "say": "Весь разбор читайте на сайте ЛапРадар.", "hl": ["ЛапРадар"]}
  ],
  "en": [
   {"kind": "big", "chip": "Abu Dhabi · 12 December 2021",
    "say": "Season finale, two drivers level on points. How did one lap decide the title?",
    "hl": ["level", "one", "lap"]},
   {"kind": "big", "chip": "369.5 : 369.5", "barTexts": ["369.5", "369.5"],
    "say": "Both on three sixty-nine and a half. The first time since nineteen seventy-four.",
    "hl": ["nineteen", "seventy-four"]},
   {"kind": "big", "chip": "Start · Verstappen on pole",
    "say": "Verstappen starts from pole, but Hamilton passes him at the start.",
    "hl": ["passes"]},
   {"kind": "big", "chip": "Lap 1 · Turn 6",
    "say": "Max attacks into Turn six. Hamilton cuts the chicane, stays ahead. No investigation.",
    "hl": ["cuts", "the", "chicane"]},
   {"kind": "big", "chip": "Lap 51 of 58 · +11 s",
    "say": "Hamilton pulls away. By lap fifty-one he is over eleven seconds clear.",
    "hl": ["eleven", "seconds"]},
   {"kind": "big", "chip": "Lap 53 · safety car",
    "say": "Lap fifty-three. Latifi crashes, and the safety car comes out.",
    "hl": ["safety", "car"]},
   {"kind": "tyres", "head": "", "names": [], "hi": 0, "chip": "Fresh softs ↔ old tyres",
    "say": "Verstappen gets fresh softs. Hamilton stays out on old tyres to keep the lead.",
    "hl": ["fresh", "softs"]},
   {"kind": "big", "chip": "5 lapped cars between them",
    "say": "Five lapped cars sit between the leaders. First message: they may not overtake.",
    "hl": ["Five", "not", "overtake"]},
   {"kind": "big", "chip": "Lap 57 · race director Masi",
    "say": "Lap fifty-seven. Masi changes the decision: only those five may overtake.",
    "hl": ["only", "those", "five"]},
   {"kind": "big", "chip": "Lap 58 · the last lap",
    "say": "Three stay put. Verstappen starts the last lap right behind Hamilton.",
    "hl": ["last", "lap"]},
   {"kind": "big", "chip": "Turn 5 · the pass",
    "say": "He passes Hamilton at Turn five, holds on to the flag and becomes champion.",
    "hl": ["champion"]},
   {"kind": "big", "chip": "2 protests · Masi removed",
    "say": "Mercedes' protests rejected, appeal withdrawn. In February the FIA removed Masi.",
    "hl": ["rejected", "removed"]},
   {"kind": "big", "chip": "FIA report · human error",
    "say": "The FIA report: human error, results final. Now all lapped cars are let past.",
    "hl": ["human", "error", "all"]},
   {"kind": "big", "big": "22", "chip": "22 races in the season",
    "say": "But one race doesn't decide a title. Before Abu Dhabi, both sides lost points.",
    "hl": ["one", "race"]},
   {"kind": "big", "chip": "Silverstone · HAM 25 · VER 0",
    "say": "Silverstone: a collision, a fifty-one g impact. Hamilton wins despite a penalty.",
    "hl": ["fifty-one", "g"]},
   {"kind": "big", "chip": "Hungary · HAM 18 · VER 2",
    "say": "Hungary: a wet-start pile-up. Verstappen two points, Hamilton eighteen.",
    "hl": ["Two", "eighteen"]},
   {"kind": "big", "chip": "Baku · 0 : 0",
    "say": "Baku: Verstappen's tyre fails, Hamilton goes off at the restart. Zero for both.",
    "hl": ["Zero", "for", "both"]},
   {"kind": "big", "chip": "Monza · penalty for Verstappen",
    "say": "Monza: Verstappen is found responsible. The cars tangle, and both retire.",
    "hl": ["both", "retire"]},
   {"kind": "big", "chip": "Jeddah · +10 s for Verstappen",
    "say": "Jeddah: a penalty for Verstappen's erratic braking. Hamilton wins, they're level.",
    "hl": ["level"]},
   {"kind": "big", "chip": "395.5 : 387.5", "barTexts": ["395.5", "387.5"],
    "say": "In the end, eight points over twenty-two races. A title is built over the whole season.",
    "hl": ["whole", "season"]},
   {"kind": "end", "tag": "Abu Dhabi 2021 · the story",
    "say": "Read the full story on LapRadar.", "hl": ["LapRadar"]}
  ]
 }
}

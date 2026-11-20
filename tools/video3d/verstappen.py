# Ферстаппен в 2026: угрозы уйти (март–май), спор о правилах 2027 и контракт до 2030 (20.08.2026). Хронология по месяцам в chip.
# HQ-режим, Судзука (там в марте прозвучали его слова про «анти-вождение»). Машина 0: своя тёмно-синяя схема без логотипов (VIDEO.hq.cars).
# Камера (shots) общая для всех языков.
_NAVY = ["#1b2a6b", "#d61f3c", "stripe"]          # тёмно-синий с красным акцентом, без ливреи команды
_CV = {"type": "convoy", "at": 0.425, "v": 30, "n": 3}

VIDEO = {
 "slug": "verstappen-quit-threat-2026",
 "track": "suzuka",
 "theme": "dusk",
 "hq": {"cars": [_NAVY, ["#0f766e", "#f8fafc", "split"]], "lampFade": True},
 "shots": [
  {"type": "chase", "car": 0, "dist": 12, "dist2": 11, "h": 5, "h2": 4.5, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "v": 50, "n": 3}},
  {"type": "carorbit", "car": 0, "r": 10.5, "r2": 9.5, "h": 1.5, "h2": 2.0, "a0": 0.5, "a1": 1.15, "fov": 46, "ly": 0.8, "act": {**_CV, "at": 0.44, "v": 22, "n": 1}},
  {"type": "onboard", "car": 0, "fov": 68, "eh": 1.3, "ez": 0.05, "ty": 1.6, "act": {**_CV, "at": 0.76, "v": 26}},
  {"type": "stage", "items": [{"o": "f1", "c": _NAVY[0], "a": _NAVY[1], "p": _NAVY[2]}], "bg": "blue", "r": 10.5, "r2": 9.5, "h": 2.4, "h2": 3.0, "a0": -0.9, "a1": 0.1, "spin": 0.25, "ly": 0.8},
  {"type": "chase", "car": 0, "dist": 9.5, "dist2": 9, "h": 4.2, "h2": 4, "side": 0, "side2": 0, "look": 20, "drop": 3, "noCut": True, "act": {"type": "follow", "at": 0.3}},
  {"type": "stage", "items": [{"o": "f1", "c": _NAVY[0], "a": _NAVY[1], "p": _NAVY[2]}], "bg": "blue", "r": 11, "r2": 10, "h": 2.8, "h2": 3.2, "a0": -0.7, "a1": 0.2, "spin": 0.15, "ly": 0.8,
   "hud": {"type": "bars", "rows": [{"label": "2026", "v": 50, "c": "#9fb4ff"}, {"label": "2027", "v": 58, "c": "#5b9bff"}, {"label": "2028", "v": 60, "c": "#facc15"}], "min": 0, "max": 64, "hi": 1}},
  {"type": "stage", "items": [{"o": "f1", "c": _NAVY[0], "a": _NAVY[1], "p": _NAVY[2]}], "bg": "gold", "beams": True, "r": 10.5, "r2": 9.5, "h": 2.6, "h2": 3.2, "a0": -0.5, "a1": 0.5, "spin": 0.1, "ly": 0.8},
  {"type": "carorbit", "car": 0, "r": 11.5, "r2": 10, "h": 1.8, "h2": 2.4, "a0": -0.7, "a1": 0.35, "fov": 48, "ly": 0.8, "act": {**_CV, "at": 0.755, "v": 40, "n": 1}},
  {"type": "orbit", "at": 0.06, "r": 330, "r2": 300, "h": 90, "h2": 70, "a0": 0.4, "a1": 0.8, "fov": 50, "act": {**_CV, "at": 0.04, "v": 45}}
 ],
 "coverShot": {"type": "carorbit", "car": 0, "r": 9.5, "h": 1.4, "a0": 1.75, "a1": 1.75, "fov": 44, "act": {**_CV, "at": 0.44, "v": 1, "n": 1}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "carorbit", "car": 0, "r": 7, "h": 1.1, "a0": 2.0, "a1": 2.0, "fov": 40, "ly": 0.6, "act": {**_CV, "at": 0.44, "v": 1, "n": 1}}},
  {"name": "onboard", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "onboard", "car": 1, "fov": 58, "act": {**_CV, "at": 0.77, "v": 30, "n": 2}}},
  {"name": "side", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "side", "car": 0, "side": 6, "h": 1.2, "fw": 1, "look": 0.5, "ly": 1.0, "fov": 50, "act": {**_CV, "at": 0.44, "v": 30}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "big": "2030", "head": "Ферстаппен грозил уйти", "sub": "а подписал до 2030", "chip": "«Уйду» → контракт до 2030",
    "say": "Весной Ферстаппен грозил уйти из Формулы один, а летом подписал контракт до тридцатого года.",
    "hl": ["уйти", "тридцатого"]},
   {"kind": "big", "big": "11.2025", "chip": "Ноябрь 2025 · Катар",
    "say": "Год назад в Катаре: если новые машины не будут в радость, он уйдёт.",
    "hl": ["радость"]},
   {"kind": "big", "big": "P8", "chip": "Март 2026 · Судзука · P8",
    "say": "В марте в Судзуке он восьмой и называет такие гонки анти-вождением. Пишут, что думает уйти в конце года.",
    "hl": ["анти-вождением"]},
   {"kind": "big", "big": "2028", "chip": "Контракт до 2028 · пункты о результатах",
    "say": "Контракт был до двадцать восьмого, но с пунктами о результатах: можно уйти раньше.",
    "hl": ["раньше"]},
   {"kind": "big", "big": "05.2026", "chip": "Май 2026 · Канада",
    "say": "В мае в Канаде: оставаться так психологически невозможно. Без правок к двадцать седьмому он готов уйти.",
    "hl": ["невозможно"]},
   {"kind": "big", "big": "58/42", "chip": "Июнь 2026 · ДВС 58 / батарея 42",
    "say": "В июне FIA утвердила правки: в двадцать седьмом больше мощности от двигателя, меньше от батареи.",
    "hl": ["двигатель"]},
   {"kind": "big", "big": "2030", "chip": "20 августа 2026 · до конца 2030",
    "say": "Двадцатого августа, перед Зандвортом, Red Bull продлила контракт до конца тридцатого года.",
    "hl": ["тридцатого"]},
   {"kind": "big", "big": "3", "chip": "3 победы · P2 · 279 очков",
    "say": "Первая победа только в шестнадцатой гонке, потом Сингапур и Мексика. Перед Вегасом он второй.",
    "hl": ["второй"]},
   {"kind": "end", "tag": "Ферстаппен · сезон 2026",
    "say": "Как Макс закончит сезон, смотрите на ЛапРадар."}
  ],
  "en": [
   {"kind": "big", "big": "2030", "head": "Verstappen threatened to quit", "sub": "then signed to 2030", "chip": "\"I'll quit\" → signed to 2030",
    "say": "In spring Verstappen was threatening to quit Formula One. By summer he'd signed to twenty thirty.",
    "hl": ["quit", "thirty"]},
   {"kind": "big", "big": "11.2025", "chip": "Nov 2025 · Qatar",
    "say": "A year ago in Qatar: if the new cars weren't fun, he'd leave.",
    "hl": ["fun"]},
   {"kind": "big", "big": "P8", "chip": "Mar 2026 · Suzuka · P8",
    "say": "In March at Suzuka he was eighth and called the racing anti-driving. Reports said he might quit at year end.",
    "hl": ["anti-driving"]},
   {"kind": "big", "big": "2028", "chip": "Deal to 2028 · performance clauses",
    "say": "His deal ran to twenty twenty-eight, but with performance clauses that let him leave early.",
    "hl": ["early"]},
   {"kind": "big", "big": "05.2026", "chip": "May 2026 · Canada",
    "say": "In May in Canada: staying like this was mentally not doable. No changes for twenty twenty-seven, and he could go.",
    "hl": ["mentally"]},
   {"kind": "big", "big": "58/42", "chip": "June 2026 · engine 58 / battery 42",
    "say": "In June the FIA approved the tweaks: for twenty twenty-seven, more engine power and less from the battery.",
    "hl": ["engine"]},
   {"kind": "big", "big": "2030", "chip": "Aug 20, 2026 · to end of 2030",
    "say": "On August twentieth, before Zandvoort, Red Bull extended his deal to the end of twenty thirty.",
    "hl": ["thirty"]},
   {"kind": "big", "big": "3", "chip": "3 wins · P2 · 279 pts",
    "say": "First win only in race sixteen, then Singapore and Mexico. He's second going into Vegas.",
    "hl": ["second"]},
   {"kind": "end", "tag": "Verstappen · 2026 season",
    "say": "Follow how Max ends the season on LapRadar."}
  ]
 }
}

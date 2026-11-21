# «Грязный воздух»: почему трудно ехать вплотную. Вихревой след за машиной (shot.wake, новая опция студии, по умолчанию выключена),
# потеря прижимной силы, скольжение и перегрев шин; 2022: граунд-эффект (≈47% → ≈18% потерь на расстоянии корпуса по данным F1),
# лазейки команд снова усилили след; 2026: активная аэродинамика (прямой/поворотный режим крыльев) и режим обгона вместо DRS.
# HQ-режим, Сильверстоун днём. Машина 0 (впереди) серебристая, машина 1 (догоняет) оранжевая: условные цвета без ливрей.
_SIL = ["#c3c8d0", "#0f172a", "stripe"]
_ORG = ["#f97316", "#111827", "band"]
_CV = {"type": "convoy", "at": 0.6, "v": 30, "n": 2}
_WK = {"cars": [0], "len": 30}

VIDEO = {
 "slug": "f1-dirty-air-explained",
 "track": "silverstone",
 "theme": "day",
 "hq": {"cars": [_SIL, _ORG], "lampFade": True},
 "shots": [
  {"type": "chase", "car": 1, "dist": 12, "dist2": 11, "h": 4.5, "h2": 4.2, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "wake": _WK, "act": {"type": "follow", "at": 0.3}},
  {"type": "chase", "car": 0, "dist": 17, "dist2": 15, "h": 9, "h2": 8, "side": -5, "side2": -3, "look": 8, "drop": 4, "noCut": True, "wake": _WK, "act": {**_CV, "at": 0.73, "v": 24, "n": 1}},
  {"type": "carorbit", "car": 1, "r": 11, "r2": 10, "h": 2.2, "h2": 2.6, "a0": 0.4, "a1": 1.0, "fov": 48, "ly": 0.8, "wake": {**_WK, "heat": [1]}, "act": {**_CV, "at": 0.74, "v": 22}},
  {"type": "side", "car": 1, "side": 8.4, "side2": 7.8, "h": 1.3, "h2": 1.5, "fw": 6, "fw2": 2, "look": 0.5, "ly": 0.9, "fov": 58, "wake": _WK, "act": {**_CV, "at": 0.73, "v": 26},
   "hud": {"type": "bars", "rows": [{"label": "2021", "v": 47, "c": "#ef4444"}, {"label": "2022", "v": 18, "c": "#22c55e"}], "min": 0, "max": 50, "hi": 1}},
  {"type": "carorbit", "car": 0, "r": 8.5, "r2": 8, "h": 0.6, "h2": 0.8, "a0": 1.2, "a1": 1.8, "fov": 50, "ly": 0.4, "act": {**_CV, "at": 0.74, "v": 20, "n": 1}},
  {"type": "chase", "car": 1, "dist": 14, "dist2": 12.5, "h": 6, "h2": 5.5, "side": 1.5, "side2": -1.5, "look": 22, "drop": 3, "noCut": True, "wake": {**_WK, "len": 38, "op": 0.7}, "act": {"type": "follow", "at": 0.6}},
  {"type": "chase", "car": 0, "dist": 10, "dist2": 9, "h": 3.6, "h2": 3.2, "side": -2.2, "side2": 2.2, "look": 10, "drop": 2.8, "noCut": True, "act": {"type": "wings"}},
  {"type": "chase", "car": 1, "dist": 16, "dist2": 13, "h": 6, "h2": 5.5, "side": 0, "side2": 2, "look": 25, "drop": 9, "noCut": True, "act": {"type": "boost"}},
  {"type": "orbit", "at": 0.75, "r": 430, "r2": 410, "h": 130, "h2": 120, "a0": 1.2, "a1": 1.3, "fov": 50, "act": {**_CV, "at": 0.72, "v": 45}}
 ],
 "coverShot": {"type": "chase", "car": 1, "dist": 11, "h": 4.2, "side": -1.5, "look": 22, "drop": 3, "fov": 46, "wake": _WK, "act": {"type": "follow", "at": 0.3}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 1, "dist": 10, "h": 3.6, "side": -1.5, "look": 18, "drop": 2.5, "fov": 44, "wake": _WK, "act": {"type": "follow", "at": 0.3}}},
  {"name": "wake", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 13, "h": 6.5, "side": -3.5, "look": 8, "drop": 3.5, "fov": 46, "wake": _WK, "act": {**_CV, "at": 0.73, "v": 24, "n": 1}}},
  {"name": "wings", "w": 1200, "h": 800, "t": 1.6, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 9, "h": 3.2, "side": -2.2, "look": 10, "drop": 2.8, "fov": 44, "act": {"type": "wings"}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "head": "Грязный воздух", "sub": "почему трудно ехать вплотную", "chip": "Грязный воздух",
    "say": "Почему в Формуле один так трудно ехать вплотную за соперником? Виноват грязный воздух.",
    "hl": ["грязный", "воздух"]},
   {"kind": "big", "chip": "Вихревой след",
    "say": "Болид рвёт воздух, и за ним тянется вихревой след. Догоняющая машина въезжает прямо в него.",
    "hl": ["вихревой", "след"]},
   {"kind": "big", "chip": "Меньше прижима → скольжение",
    "say": "Крылья и днище получают рваный поток и теряют прижимную силу. Машина скользит, шины перегреваются.",
    "hl": ["прижимную", "силу"]},
   {"kind": "big", "barTexts": ["почти ½", "< ⅕"],
    "say": "Машины до двадцать второго года в корпусе от соперника теряли почти половину прижима. Новым обещали меньше пятой части.",
    "hl": ["половину"]},
   {"kind": "big", "chip": "2022: прижим под днищем",
    "say": "Для этого прижим перенесли под днище, в туннели, а след за машиной сделали уже.",
    "hl": ["днище"]},
   {"kind": "big", "chip": "Лазейки → след сильнее",
    "say": "Но команды нашли лазейки в крыльях и тормозных воздуховодах, и след снова стал сильнее.",
    "hl": ["лазейки"]},
   {"kind": "big", "chip": "2026: подвижные крылья",
    "say": "Теперь крылья подвижные: на прямых закрылки открываются у всех, не только у догоняющего.",
    "hl": ["у", "всех"]},
   {"kind": "big", "chip": "Вместо DRS: режим обгона",
    "say": "А вместо DRS режим обгона: в секунде от соперника пилот получает лишнюю энергию на следующий круг.",
    "hl": ["режим", "обгона"]},
   {"kind": "end", "tag": "Грязный воздух · коротко",
    "say": "Кто кого догоняет и какой разрыв, смотрите на живой карте ЛапРадар."}
  ],
  "en": [
   {"kind": "big", "head": "Dirty air", "sub": "why following is so hard", "chip": "Dirty air",
    "say": "Why is it so hard to follow another car closely in Formula One? Blame the dirty air.",
    "hl": ["dirty", "air"]},
   {"kind": "big", "chip": "A turbulent wake",
    "say": "A car punches through the air and leaves a swirling wake. The chasing car drives right into it.",
    "hl": ["wake"]},
   {"kind": "big", "chip": "Less downforce → sliding",
    "say": "The wings and floor get messy airflow and lose downforce. The car slides and the tyres overheat.",
    "hl": ["downforce"]},
   {"kind": "big", "barTexts": ["almost ½", "< ⅕"],
    "say": "Older cars lost almost half their downforce one car length back. The twenty twenty-two cars were meant to lose under a fifth.",
    "hl": ["half"]},
   {"kind": "big", "chip": "2022: downforce from the floor",
    "say": "So downforce moved under the floor, into tunnels, and the wake behind the car was made narrower.",
    "hl": ["floor"]},
   {"kind": "big", "chip": "Loopholes → bigger wake",
    "say": "But teams found loopholes in the wings and brake ducts, and the wake got worse again.",
    "hl": ["loopholes"]},
   {"kind": "big", "chip": "2026: moving wings",
    "say": "Now the wings move: on the straights the flaps open for everyone, not just the chasing car.",
    "hl": ["everyone"]},
   {"kind": "big", "chip": "Instead of DRS: Overtake Mode",
    "say": "And DRS is gone. Within a second of the car ahead, Overtake Mode gives extra energy for the next lap.",
    "hl": ["Overtake", "Mode"]},
   {"kind": "end", "tag": "Dirty air · in short",
    "say": "See who's closing in, and by how much, on the LapRadar live map."}
  ]
 }
}

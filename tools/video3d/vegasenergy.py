# Лас-Вегас-2026: прямая по Стрипу и батарея новых машин. Камера (shots) общая для всех языков.
VIDEO = {
 "slug": "las-vegas-2026-strip-energy",
 "track": "las-vegas",
 "theme": "vegas",
 "shots": [
  {"type": "chase", "car": 0, "dist": 13, "dist2": 12, "h": 6, "h2": 5.5, "side": 0, "side2": 0, "look": 22, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight"}},
  {"type": "stage", "items": [{"o": "f1", "c": "#f3f4f6"}], "bg": "blue", "r": 10, "r2": 9, "h": 2.4, "h2": 3.2, "a0": 0.9, "a1": -0.2, "spin": 0.3, "ly": 0.8,
   "hud": {"type": "bars", "rows": [{"label": "ICE", "v": 400, "c": "#9fb4ff"}, {"label": "ERS", "v": 350, "c": "#facc15"}], "min": 0, "max": 420, "hi": 1}},
  {"type": "chase", "car": 0, "dist": 11, "dist2": 10, "h": 4.5, "h2": 4.2, "side": 1.5, "side2": 1, "look": 10, "drop": 3, "noCut": True, "act": {"type": "energy"}, "hud": {"type": "battery"}},
  {"type": "chase", "car": 1, "dist": 14, "dist2": 12, "h": 6, "h2": 5, "side": 1.5, "side2": -1.5, "look": 25, "drop": 3, "noCut": True, "act": {"type": "convoy", "at": "straight", "t0": 6}},
  {"type": "chase", "car": 0, "dist": 12, "dist2": 10, "h": 4.5, "h2": 4, "side": -1.5, "side2": 1.5, "look": 25, "drop": 2.5, "noCut": True, "act": {"type": "cold", "at": 0.45}, "hud": {"type": "thermo", "from": 25, "to": 14}},
  {"type": "chase", "car": 1, "dist": 16, "dist2": 13, "h": 6, "h2": 5.5, "side": 0, "side2": 2.5, "look": 35, "drop": 2, "noCut": True, "act": {"type": "boost"}},
  {"type": "fly", "from": 0.42, "to": 0.5, "h": 60, "h2": 140, "side": 40, "ahead": 260}
 ],
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 10, "h": 3.6, "side": -2.2, "look": 16, "drop": 3, "fov": 42, "act": {"type": "speed"}}},
  {"name": "energy", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "car": 0, "dist": 10, "h": 4, "side": 2.2, "look": 12, "drop": 3, "fov": 44, "act": {"type": "energy"}}},
  {"name": "boost", "w": 1200, "h": 800, "t": 1.2, "u": 0.5,
   "shot": {"type": "chase", "car": 1, "dist": 9, "h": 3.6, "side": -2.2, "look": 14, "drop": 2, "fov": 40, "act": {"type": "boost"}}}
 ],
 "scenes": {
  "ru": [
   {"kind": "title", "head": "БАТАРЕЯ НЕ ДОЕЗЖАЕТ", "sub": "Вегас-2026",
    "say": "Почти два километра газ в пол. На такой прямой у новых машин Формулы один кончается батарея.",
    "hl": ["два километра", "батарея"]},
   {"kind": "big", "big": "50/50", "chip": "ДВС ≈400 кВт · ERS 350 кВт",
    "say": "С этого года мощность делится примерно поровну между мотором и электрикой.",
    "hl": ["поровну"]},
   {"kind": "big", "big": "kW", "chip": "заряд на торможении",
    "say": "Батарея заряжается на торможении. А в Вегасе медленных поворотов мало, длинных прямых много.",
    "hl": ["на торможении"]},
   {"kind": "big", "big": "−км/ч", "chip": "суперклиппинг до 350 кВт",
    "say": "Поэтому в конце прямой машина подзаряжается прямо на полном газу. Это суперклиппинг, и скорость падает.",
    "hl": ["суперклиппинг"]},
   {"kind": "big", "big": "C3–C5", "chip": "самые мягкие шины",
    "say": "Ещё и холод. Пирелли везёт три самых мягких состава, чтобы шины вообще прогрелись.",
    "hl": ["три самых мягких"]},
   {"kind": "big", "big": "50", "chip": "50 кругов · 6,2 км",
    "say": "Пятьдесят кругов по шесть километров. Кто лучше распределит энергию, тот и обгонит на Стрипе.",
    "hl": ["энергию"]},
   {"kind": "end", "tag": "Вегас в прямом эфире",
    "say": "Скорости и отрывы по ходу гонки смотрите на ЛапРадар."}
  ],
  "en": [
   {"kind": "title", "head": "OUT OF BATTERY", "sub": "Vegas 2026",
    "say": "Nearly two kilometres flat out. On a straight that long, the new Formula One cars run out of battery.",
    "hl": ["two kilometres", "battery"]},
   {"kind": "big", "big": "50/50", "chip": "ICE ≈400 kW · ERS 350 kW",
    "say": "Since this year the power is split roughly half and half between engine and electrics.",
    "hl": ["half and half"]},
   {"kind": "big", "big": "kW", "chip": "charging under braking",
    "say": "The battery charges under braking. Vegas has few slow corners and a lot of long straights.",
    "hl": ["under braking"]},
   {"kind": "big", "big": "−km/h", "chip": "super clipping up to 350 kW",
    "say": "So at the end of the straight the car recharges while still flat out. That's super clipping, and top speed drops.",
    "hl": ["super clipping"]},
   {"kind": "big", "big": "C3–C5", "chip": "the softest tyres",
    "say": "Then there's the cold. Pirelli brings its three softest compounds just so the tyres warm up.",
    "hl": ["three softest"]},
   {"kind": "big", "big": "50", "chip": "50 laps · 6.2 km",
    "say": "Fifty laps of six kilometres. Whoever manages energy best will be the one passing on the Strip.",
    "hl": ["energy"]},
   {"kind": "end", "tag": "Vegas, live",
    "say": "Follow speeds and gaps during the race on LapRadar."}
  ]
 }
}

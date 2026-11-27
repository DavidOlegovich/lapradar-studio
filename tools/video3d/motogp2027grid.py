# MotoGP 2027: кто куда переходит (рынок пилотов). Камера (shots) общая для всех языков.
# Факты и источники: tools/topics.md («Источники 28.11: MotoGP 2027, переходы»). Байки условные: без логотипов и настоящих ливрей.
# Время сессий и городов не называем. Трасса Сильверстоун (день) просто фон, в кадре её не выдаём ни за какую гонку.
_BIKE = lambda at, dist=8, dist2=6.5, h=3.2, h2=2.8, side=-2.2, side2=1.8, fov=50, **k: {
    "type": "chase", "follow": "bike", "fi": 5, "dist": dist, "dist2": dist2, "h": h, "h2": h2, "side": side, "side2": side2,
    "look": 22, "drop": 2, "fov": fov, "noCut": True, "act": {"type": "motogp", "at": at, **k}}
_RED = "#e10600"
_BLUE = "#2f6bff"
_PURPLE = "#8e5bff"
_ORANGE = "#ff7a00"
_WHITE = "#e8ecf2"
_GREEN = "#26c281"
def _stage(cols, bg, a0, a1, **k):
    xs = {1: [0], 2: [-1.4, 1.5], 3: [-2.6, 0, 2.6]}[len(cols)]
    items = [{"o": "bike", "c": c, "x": x, "lean": 0.3 if i == 0 else -0.3, "s": 1.15, "y": 0.4} for i, (c, x) in enumerate(zip(cols, xs))]
    return {"type": "stage", "items": items, "bg": bg, "r": 8, "r2": 7.2, "h": 1.6, "h2": 1.9, "a0": a0, "a1": a1, "spin": 0.3, "ly": 2.1, **k}
VIDEO = {
 "slug": "motogp-2027-rider-market",
 "track": "silverstone",
 "theme": "day",
 "hq": True,
 "coverText": {"ru": {"head": "MOTOGP 2027: КТО КУДА", "sub": "новая решётка эры 850 кубов"},
               "en": {"head": "MOTOGP 2027: WHO GOES WHERE", "sub": "the new grid for the 850cc era"}},
 "shots": [
  # 1 крючок
  _BIKE(0.12, 4.5, 4, 1.9, 1.8, fov=38),
  # 2 Акоста в Ducati
  _stage([_RED, _ORANGE], "red", 0.7, -0.3),
  # 3 Баньяя в Aprilia
  _stage([_PURPLE, _BLUE], "blue", -0.6, 0.4),
  # 4 Мартин в Yamaha
  _BIKE(0.4, 4.5, 4, 1.9, 1.8, side=1.6, side2=-1.3, fov=38),
  # 5 Куартараро в Honda
  _stage([_WHITE, _BLUE], "gold", 0.5, -0.5),
  # 6 KTM
  _stage([_ORANGE, "#ffb020"], "gold", -0.5, 0.5, beams=True),
  # 7 новички
  _BIKE(0.62, 5.5, 5, 2.1, 2.0, side=-1.5, side2=1.3, fov=38, **{"pass": 1}),
  # 8 уходят в WorldSBK
  _stage(["#26c281", "#ffb020", _PURPLE], "blue", 0.15, -0.15, r=11, r2=10, spin=0),
  # 9 финал
  {"type": "fly", "from": 0.0, "to": 0.08, "h": 60, "h2": 140, "side": -40, "ahead": 260}
 ],
 "coverShot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 7, "h": 2.8, "side": -2.2, "look": 20, "drop": 2, "act": {"type": "motogp", "at": 0.12}},
 "images": [
  {"name": "cover", "w": 1200, "h": 630, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 7, "h": 2.8, "side": -2.2, "look": 20, "drop": 2, "fov": 42, "act": {"type": "motogp", "at": 0.12}}},
  {"name": "grid", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "chase", "follow": "bike", "fi": 5, "dist": 9, "h": 3.6, "side": 1.6, "look": 22, "drop": 3, "fov": 44, "act": {"type": "motogp", "at": 0.4}}},
  {"name": "swap", "w": 1200, "h": 800, "t": 2.0, "u": 0.5,
   "shot": {"type": "stage", "items": [{"o": "bike", "c": _PURPLE, "x": -1.4, "lean": 0.3, "s": 1.15, "y": 0.4}, {"o": "bike", "c": _RED, "x": 1.5, "lean": -0.3, "s": 1.15, "y": 0.4}], "bg": "red",
            "r": 8, "h": 1.7, "a0": -0.3, "spin": 0, "ly": 2.0}}
 ],
 "scenes": {
  "ru": [
   {"kind": "big", "chip": "22 пилота · 5 дебютантов",
    "say": "Двадцать два пилота и пять дебютантов. Кто куда переходит в Мотоджипи две тысячи двадцать седьмого?",
    "hl": ["двадцать два", "пять дебютантов"]},
   {"kind": "big", "chip": "Акоста: KTM → Ducati", "min": 4.6,
    "say": "Педро Акоста уходит из КТМ в Дукати и встаёт рядом с Маркесом. Контракт до конца две тысячи двадцать восьмого.",
    "hl": ["Акоста", "Дукати"]},
   {"kind": "big", "chip": "Баньяя: Ducati → Aprilia", "min": 4.6,
    "say": "Баньяя покидает Дукати и подписывает с Априлией четыре года. Напарник у него Беццекки.",
    "hl": ["Баньяя", "четыре года"]},
   {"kind": "big", "chip": "Мартин: Aprilia → Yamaha", "min": 4.4,
    "say": "Хорхе Мартин из Априлии переходит в заводскую Ямаху. Напарник у него Ай Огура.",
    "hl": ["Мартин", "Ямаху"]},
   {"kind": "big", "chip": "Куартараро: Yamaha → Honda", "min": 4.6,
    "say": "Куартараро меняет Ямаху на Хонду. Два года, до конца две тысячи двадцать восьмого.",
    "hl": ["Куартараро", "Хонду"]},
   {"kind": "big", "chip": "KTM: новый состав", "min": 4.6,
    "say": "В КТМ полностью новая пара: Алекс Маркес и Фабио Ди Джаннантонио.",
    "hl": ["новая пара", "Алекс Маркес"]},
   {"kind": "big", "chip": "Пять новичков", "min": 5.2,
    "say": "Дебютируют Холгадо, Алонсо, Гевара, Агиус и Булега, который приходит из супербайка.",
    "hl": ["Холгадо", "Булега"]},
   {"kind": "big", "chip": "Миллер, Биндер, Морбиделли → WorldSBK", "min": 5.2,
    "say": "Миллер, Биндер и Морбиделли уходят в супербайк: Ямаха, БМВ и заводская Дукати.",
    "hl": ["Миллер", "супербайк"]},
   {"kind": "end", "tag": "MotoGP 2027 · кто куда",
    "say": "Весь календарь и составы смотрите на ЛапРадар.",
    "hl": ["ЛапРадар"]}
  ],
  "en": [
   {"kind": "big", "chip": "22 riders · 5 rookies",
    "say": "Twenty-two riders and five rookies. Who is going where in MotoGP twenty twenty-seven?",
    "hl": ["twenty-two", "five rookies"]},
   {"kind": "big", "chip": "Acosta: KTM → Ducati", "min": 4.6,
    "say": "Pedro Acosta leaves KTM for Ducati and lines up next to Márquez. His deal runs to the end of twenty twenty-eight.",
    "hl": ["Acosta", "Ducati"]},
   {"kind": "big", "chip": "Bagnaia: Ducati → Aprilia", "min": 4.6,
    "say": "Bagnaia leaves Ducati and signs a four-year deal with Aprilia. His teammate is Bezzecchi.",
    "hl": ["Bagnaia", "four-year"]},
   {"kind": "big", "chip": "Martín: Aprilia → Yamaha", "min": 4.4,
    "say": "Jorge Martín moves from Aprilia to the factory Yamaha team. His teammate is Ai Ogura.",
    "hl": ["Martín", "Yamaha"]},
   {"kind": "big", "chip": "Quartararo: Yamaha → Honda", "min": 4.6,
    "say": "Quartararo swaps Yamaha for Honda on a two-year deal, to the end of twenty twenty-eight.",
    "hl": ["Quartararo", "Honda"]},
   {"kind": "big", "chip": "KTM: new line-up", "min": 4.6,
    "say": "KTM have a brand new pair: Álex Márquez and Fabio Di Giannantonio.",
    "hl": ["brand new", "Álex Márquez"]},
   {"kind": "big", "chip": "Five newcomers", "min": 5.2,
    "say": "Holgado, Alonso, Guevara, Agius and Bulega, who arrives from WorldSBK, all make their MotoGP debut.",
    "hl": ["Holgado", "Bulega"]},
   {"kind": "big", "chip": "Miller, Binder, Morbidelli → WorldSBK", "min": 5.2,
    "say": "Miller, Binder and Morbidelli head to WorldSBK: Yamaha, BMW and factory Ducati.",
    "hl": ["Miller", "WorldSBK"]},
   {"kind": "end", "tag": "MotoGP 2027 · who goes where",
    "say": "The full calendar and line-ups are on LapRadar.",
    "hl": ["LapRadar"]}
  ]
 }
}

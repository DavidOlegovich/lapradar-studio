# 3D-ролик к разбору «Катар: ночная гонка, которая съедает шины». Камера (shots) общая для всех языков.
VIDEO = {
  "slug": "night-races-qatar",
  "track": "lusail", "theme": "night",
  "shots": [
    {"type": "orbit", "r": 1500, "r2": 1050, "h": 700, "h2": 420, "a0": 0.4, "a1": 1.2},
    {"type": "top", "reveal": True, "badges": True, "k": 1.15, "tilt": 0.25, "rot0": 0, "rot1": 0.25, "act": {"type": "trace", "at": 0.02}},
    {"type": "chase", "car": 0, "dist": 11, "dist2": 8.5, "h": 3.6, "h2": 2.8, "side": -2, "side2": 2, "look": 14, "drop": 3, "act": {"type": "heat", "at": 0.3}},
    {"type": "tyre", "hi": 0, "wear": True, "hud": {"type": "laps", "n": 18}},
    {"type": "chase", "car": 0, "dist": 15, "dist2": 13, "h": 6.5, "h2": 6, "side": 3, "side2": 1, "look": 14, "drop": 3, "act": {"type": "fade", "t1": 0.45}},
    {"type": "fly", "from": 0.05, "to": 0.12, "h": 60, "h2": 160, "side": -40, "ahead": 220},
  ],
  # иллюстрации к статье (без текста): обложка и картинки между блоками
  "images": [
    {"name": "cover", "w": 1200, "h": 630, "t": 3, "u": 0.5, "shot": {"type": "chase", "car": 2, "dist": 11, "h": 3.6, "side": -3, "look": 30, "drop": 2.5, "t0": 40, "fov": 46}},
    {"name": "map", "w": 1200, "h": 800, "t": 3, "u": 1, "shot": {"type": "top", "reveal": True, "badges": True, "k": 1.18, "tilt": 0.2}},
    {"name": "night", "w": 1200, "h": 800, "t": 2, "u": 0.5, "shot": {"type": "orbit", "at": 0.015, "r": 240, "h": 110, "a0": 2.2, "a1": 2.3, "t0": 0}},
  ],
  "scenes": {
    "ru": [
      {"kind": "title", "head": "КАТАР", "sub": "ночная гонка, которая съедает шины", "say": "Почему ночная гонка в Катаре одна из самых тяжёлых в сезоне?"},
      {"kind": "big", "big": "≈5,4 км", "sub": "почти без медленных поворотов", "say": "Лусаил строили для мотоциклов. Быстрые повороты идут один за другим, медленных почти нет."},
      {"kind": "list", "head": "Нагрузка", "items": ["Машина всё время в повороте", "Шины на пределе", "Жарко даже ночью"], "say": "Машина почти всё время в повороте, шины работают на пределе, а ночью всё равно жарко и влажно."},
      {"kind": "tyre", "head": "18 кругов", "laps": 18, "say": "В двадцать третьем году один комплект шин разрешили гонять максимум восемнадцать кругов. Всем пришлось делать три пит-стопа."},
      {"kind": "tyres", "head": "Решает износ", "names": [], "hi": 2, "say": "Так что в Катаре гонку выигрывает не только скорость, но и тот, кто бережёт резину."},
      {"kind": "end", "tag": "Шины и пит-стопы вживую", "say": "Возраст шин и пит-стопы всех пилотов смотрите вживую на ЛапРадар."},
    ],
    "en": [
      {"kind": "title", "head": "QATAR", "sub": "the night race that eats tyres", "say": "Why is the Qatar night race one of the toughest of the season?"},
      {"kind": "big", "big": "≈5.4 km", "sub": "almost no slow corners", "say": "Lusail was built for motorbikes. Fast corners come one after another, and there are hardly any slow ones."},
      {"kind": "list", "head": "The load", "items": ["Always cornering", "Tyres at the limit", "Hot even at night"], "say": "The car is cornering almost all the time, the tyres are on the limit, and even at night it's hot and humid."},
      {"kind": "tyre", "head": "18 laps", "laps": 18, "say": "In twenty twenty-three each set of tyres was capped at eighteen laps. Every team had to stop at least three times."},
      {"kind": "tyres", "head": "Wear decides", "names": [], "hi": 2, "say": "So in Qatar raw speed isn't enough. The race goes to whoever looks after the tyres."},
      {"kind": "end", "tag": "Tyres and pit stops, live", "say": "Follow every driver's tyre age and pit stops live on LapRadar."},
    ],
    "es": [
      {"kind": "title", "head": "CATAR", "sub": "la carrera nocturna que se come los neumáticos", "say": "¿Por qué la carrera nocturna de Catar es una de las más duras del año?"},
      {"kind": "big", "big": "≈5,4 km", "sub": "casi sin curvas lentas", "say": "Lusail se construyó para las motos. Las curvas rápidas llegan una tras otra y casi no hay lentas."},
      {"kind": "list", "head": "La carga", "items": ["Siempre en curva", "Neumáticos al límite", "Calor incluso de noche"], "say": "El coche va casi siempre en curva, los neumáticos trabajan al límite y, aunque sea de noche, hace calor y humedad."},
      {"kind": "tyre", "head": "18 vueltas", "laps": 18, "say": "En dos mil veintitrés cada juego de neumáticos se limitó a dieciocho vueltas. Todos tuvieron que parar al menos tres veces."},
      {"kind": "tyres", "head": "Manda el desgaste", "names": [], "hi": 2, "say": "En Catar la velocidad no basta: gana quien mejor cuida los neumáticos."},
      {"kind": "end", "tag": "Neumáticos y paradas en directo", "say": "Sigue en directo la edad de los neumáticos y las paradas de cada piloto en LapRadar."},
    ],
    "pt": [
      {"kind": "title", "head": "CATAR", "sub": "a corrida noturna que devora pneus", "say": "Por que a corrida noturna do Catar é uma das mais duras do ano?"},
      {"kind": "big", "big": "≈5,4 km", "sub": "quase sem curvas lentas", "say": "Lusail foi construída para as motos. As curvas rápidas vêm uma atrás da outra e quase não há curvas lentas."},
      {"kind": "list", "head": "A carga", "items": ["Sempre em curva", "Pneus no limite", "Calor mesmo à noite"], "say": "O carro passa quase o tempo todo em curva, os pneus trabalham no limite e, mesmo à noite, faz calor e umidade."},
      {"kind": "tyre", "head": "18 voltas", "laps": 18, "say": "Em dois mil e vinte e três cada jogo de pneus foi limitado a dezoito voltas. Todas as equipes tiveram que parar pelo menos três vezes."},
      {"kind": "tyres", "head": "O desgaste manda", "names": [], "hi": 2, "say": "No Catar, velocidade não basta: vence quem cuida melhor dos pneus."},
      {"kind": "end", "tag": "Pneus e paradas ao vivo", "say": "Acompanhe ao vivo a idade dos pneus e as paradas de cada piloto no LapRadar."},
    ],
    "de": [
      {"kind": "title", "head": "KATAR", "sub": "das Nachtrennen, das Reifen frisst", "say": "Warum ist das Nachtrennen in Katar eines der härtesten der Saison?"},
      {"kind": "big", "big": "≈5,4 km", "sub": "kaum langsame Kurven", "say": "Lusail wurde für Motorräder gebaut. Schnelle Kurven folgen dicht aufeinander, langsame gibt es kaum."},
      {"kind": "list", "head": "Die Belastung", "items": ["Fast immer in der Kurve", "Reifen am Limit", "Heiß, auch nachts"], "say": "Das Auto ist fast ständig in Kurvenfahrt, die Reifen sind am Limit, und selbst nachts ist es heiß und schwül."},
      {"kind": "tyre", "head": "18 Runden", "laps": 18, "say": "Zweitausenddreiundzwanzig durfte jeder Reifensatz höchstens achtzehn Runden fahren. Jedes Team musste mindestens dreimal an die Box."},
      {"kind": "tyres", "head": "Verschleiß zählt", "names": [], "hi": 2, "say": "In Katar reicht reiner Speed also nicht. Das Rennen gewinnt, wer seine Reifen schont."},
      {"kind": "end", "tag": "Reifen und Stopps live", "say": "Reifenalter und Boxenstopps jedes Fahrers verfolgst du live auf LapRadar."},
    ],
    "zh": [
      {"kind": "title", "head": "卡塔尔", "sub": "吞噬轮胎的夜赛", "say": "为什么卡塔尔夜赛是本赛季最艰难的比赛之一？"},
      {"kind": "big", "big": "≈5.4公里", "sub": "几乎没有低速弯", "say": "卢赛尔是为摩托车修建的。高速弯一个接一个，低速弯几乎没有。"},
      {"kind": "list", "head": "负荷", "items": ["几乎一直在过弯", "轮胎处于极限", "夜里依然炎热"], "say": "赛车几乎一直在过弯，轮胎处于极限，即使在夜里也又热又潮。"},
      {"kind": "tyre", "head": "18圈", "laps": 18, "say": "二零二三年，每套轮胎最多只能跑十八圈，每支车队都至少进站三次。"},
      {"kind": "tyres", "head": "磨损决胜", "names": [], "hi": 2, "say": "所以在卡塔尔，光有速度还不够。谁更会照顾轮胎，谁就能赢下比赛。"},
      {"kind": "end", "tag": "胎龄与进站实时看", "say": "在LapRadar上实时查看每位车手的胎龄和进站情况。"},
    ],
  },
}

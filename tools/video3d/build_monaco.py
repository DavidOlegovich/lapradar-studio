# Как построить трассу Формулы 1 в Монако. Ролик без статьи, камера (shots) общая для всех языков.
VIDEO = {
 "slug": "build-monaco",
 "id": "build-monaco",
 "track": "monaco",
 "theme": "day",
 "titles": {
  "ru": "Как построить трассу Формулы 1 в Монако",
  "en": "How to build an F1 track in Monaco",
  "es": "Cómo construir un circuito de F1 en Mónaco",
  "pt": "Como construir uma pista de F1 em Mônaco",
  "de": "So baust du eine F1-Strecke in Monaco",
  "zh": "如何在摩纳哥建一条F1赛道"
 },
 "captions": {
  "ru": "6 недель стройки по ночам, 21 км ограждений и улицы, которые открывают каждый вечер. Все трассы в 3D: lapradar.com",
  "en": "Six weeks of night work, 21 km of barriers and streets that reopen every evening. Every track in 3D: lapradar.com",
  "es": "Seis semanas de obras nocturnas, 21 km de barreras y calles que reabren cada tarde. Todos los circuitos en 3D: lapradar.com",
  "pt": "Seis semanas de obras noturnas, 21 km de barreiras e ruas que reabrem toda noite. Todas as pistas em 3D: lapradar.com",
  "de": "Sechs Wochen Nachtarbeit, 21 km Leitplanken und Straßen, die jeden Abend wieder öffnen. Alle Strecken in 3D: lapradar.com",
  "zh": "六周夜间施工、21公里护栏、每晚重新通车的街道。所有赛道3D呈现：lapradar.com"
 },
 "shots": [
  {
   "type": "orbit",
   "r": 1100,
   "r2": 900,
   "h": 500,
   "h2": 380,
   "a0": 0.3,
   "a1": 0.8,
   "build": {
    "walls": "on"
   }
  },
  {
   "type": "chase",
   "follow": "taxi",
   "dist": 15,
   "dist2": 19,
   "h": 6,
   "h2": 9,
   "side": -3,
   "side2": 4,
   "look": 20,
   "drop": 3,
   "act": {
    "type": "traffic",
    "at": 0.3
   },
   "build": {
    "walls": "grow",
    "focus": "taxi",
    "R": 90
   },
   "hud": {
    "type": "clock",
    "from": "21:00",
    "to": "04:00"
   }
  },
  {
   "type": "chase",
   "follow": "taxi",
   "dist": 60,
   "dist2": 110,
   "h": 40,
   "h2": 90,
   "side": -20,
   "side2": -40,
   "look": 40,
   "drop": 10,
   "act": {
    "type": "traffic",
    "at": 0.3
   },
   "build": {
    "walls": "grow",
    "focus": "taxi",
    "R0": 60,
    "R": 1700
   }
  },
  {
   "type": "chase",
   "follow": "taxi",
   "dist": 14,
   "dist2": 17,
   "h": 5,
   "h2": 7,
   "side": 3,
   "side2": -3,
   "look": 20,
   "drop": 3,
   "act": {
    "type": "reopen",
    "at": 0.55
   },
   "build": {
    "walls": "on"
   },
   "hud": {
    "type": "clock",
    "from": "17:30",
    "to": "19:00"
   }
  },
  {
   "type": "chase",
   "car": 0,
   "dist": 14,
   "dist2": 11,
   "h": 5,
   "h2": 4.2,
   "side": 3,
   "side2": 1.5,
   "look": 22,
   "drop": 2.6,
   "build": {
    "walls": "on"
   },
   "hud": {
    "type": "clock",
    "from": "05:30",
    "to": "06:00"
   }
  },
  {
   "type": "chase",
   "car": 1,
   "dist": 18,
   "dist2": 15,
   "h": 7,
   "h2": 6,
   "side": -2,
   "side2": 2,
   "look": 40,
   "drop": 2,
   "act": {
    "type": "follow",
    "at": 0.1
   },
   "build": {
    "walls": "on"
   }
  },
  {
   "type": "top",
   "reveal": True,
   "badges": True,
   "k": 1.12,
   "tilt": 0.22,
   "rot0": 0.05,
   "rot1": 0.22,
   "act": {
    "type": "trace",
    "at": 0.02
   },
   "build": {
    "walls": "on"
   }
  },
  {
   "type": "orbit",
   "r": 1300,
   "r2": 1000,
   "h": 600,
   "h2": 450,
   "a0": 2.2,
   "a1": 2.8,
   "build": {
    "walls": "on"
   }
  }
 ],
 "images": [],
 "scenes": {
  "ru": [
   {
    "kind": "title",
    "say": "А как построить трассу в Монако, где все эти улицы нужны людям каждый день?",
    "head": "ПОСТРОЙ ТРАССУ",
    "sub": "в Монако"
   },
   {
    "kind": "big",
    "say": "Начинаешь за шесть недель до гонки, и почти всё ставишь по ночам, чтобы днём город ездил.",
    "chip": "6 недель"
   },
   {
    "kind": "big",
    "say": "Всего больше двадцати одного километра ограждений и двадцать тысяч квадратных метров сеток.",
    "chip": "21 км"
   },
   {
    "kind": "big",
    "say": "Но город не закрываешь: вечером, около семи, улицы снова открывают для обычных машин."
   },
   {
    "kind": "big",
    "say": "А в шесть утра дороги опять перекрывают, и на них выезжают болиды."
   },
   {
    "kind": "big",
    "say": "Трасса узкая, обгонять почти негде, поэтому здесь всё решает квалификация."
   },
   {
    "kind": "big",
    "say": "Итог: три километра триста метров, девятнадцать поворотов, и гонка здесь с тысяча девятьсот двадцать девятого года.",
    "chip": "3,3 км · с 1929"
   },
   {
    "kind": "end",
    "say": "Все трассы сезона в 3D смотри на ЛапРадар.",
    "tag": "Все трассы в 3D"
   }
  ],
  "en": [
   {
    "kind": "title",
    "say": "So how do you build a track in Monaco, where people need these streets every single day?",
    "head": "BUILD A TRACK",
    "sub": "in Monaco"
   },
   {
    "kind": "big",
    "say": "You start six weeks before the race and do almost everything at night, so the city can drive by day.",
    "chip": "6 weeks"
   },
   {
    "kind": "big",
    "say": "In total that's more than twenty-one kilometres of barriers and twenty thousand square metres of fencing.",
    "chip": "21 km"
   },
   {
    "kind": "big",
    "say": "But the city never closes: around seven in the evening the streets reopen to normal traffic."
   },
   {
    "kind": "big",
    "say": "At six in the morning the roads close again and the race cars come out."
   },
   {
    "kind": "big",
    "say": "The track is narrow and there's almost nowhere to overtake, so qualifying decides everything."
   },
   {
    "kind": "big",
    "say": "The result: three point three kilometres, nineteen corners, and a race here since nineteen twenty-nine.",
    "chip": "3.3 km · since 1929"
   },
   {
    "kind": "end",
    "say": "See every track of the season in 3D on LapRadar.",
    "tag": "Every track in 3D"
   }
  ],
  "es": [
   {
    "kind": "title",
    "say": "¿Y cómo construyes un circuito en Mónaco, donde la gente usa estas calles todos los días?",
    "head": "CONSTRUYE UN CIRCUITO",
    "sub": "en Mónaco"
   },
   {
    "kind": "big",
    "say": "Empiezas seis semanas antes y montas casi todo de noche, para que de día la ciudad circule.",
    "chip": "6 semanas"
   },
   {
    "kind": "big",
    "say": "En total, más de veintiún kilómetros de barreras y veinte mil metros cuadrados de vallas.",
    "chip": "21 km"
   },
   {
    "kind": "big",
    "say": "Pero la ciudad no cierra: hacia las siete de la tarde las calles se abren de nuevo al tráfico."
   },
   {
    "kind": "big",
    "say": "A las seis de la mañana se vuelven a cerrar y salen los monoplazas."
   },
   {
    "kind": "big",
    "say": "La pista es estrecha y casi no se puede adelantar, así que la clasificación lo decide todo."
   },
   {
    "kind": "big",
    "say": "Resultado: tres coma tres kilómetros, diecinueve curvas y carreras aquí desde mil novecientos veintinueve.",
    "chip": "3,3 km · desde 1929"
   },
   {
    "kind": "end",
    "say": "Mira todos los circuitos de la temporada en 3D en LapRadar.",
    "tag": "Todos los circuitos en 3D"
   }
  ],
  "pt": [
   {
    "kind": "title",
    "say": "E como construir uma pista em Mônaco, onde as pessoas usam essas ruas todos os dias?",
    "head": "CONSTRUA UMA PISTA",
    "sub": "em Mônaco"
   },
   {
    "kind": "big",
    "say": "Você começa seis semanas antes e monta quase tudo à noite, para a cidade rodar de dia.",
    "chip": "6 semanas"
   },
   {
    "kind": "big",
    "say": "No total são mais de vinte e um quilômetros de barreiras e vinte mil metros quadrados de telas.",
    "chip": "21 km"
   },
   {
    "kind": "big",
    "say": "Mas a cidade não fecha: por volta das sete da noite as ruas reabrem para o trânsito."
   },
   {
    "kind": "big",
    "say": "Às seis da manhã as ruas fecham de novo e os carros de corrida entram."
   },
   {
    "kind": "big",
    "say": "A pista é estreita e quase não dá para ultrapassar, então a classificação decide tudo."
   },
   {
    "kind": "big",
    "say": "Resultado: três vírgula três quilômetros, dezenove curvas e corrida aqui desde mil novecentos e vinte e nove.",
    "chip": "3,3 km · desde 1929"
   },
   {
    "kind": "end",
    "say": "Veja todas as pistas da temporada em 3D no LapRadar.",
    "tag": "Todas as pistas em 3D"
   }
  ],
  "de": [
   {
    "kind": "title",
    "say": "Und wie baut man eine Strecke in Monaco, wo die Menschen diese Straßen jeden Tag brauchen?",
    "head": "BAU DIR EINE STRECKE",
    "sub": "in Monaco"
   },
   {
    "kind": "big",
    "say": "Du fängst sechs Wochen vorher an und baust fast alles nachts, damit tagsüber Verkehr fließt.",
    "chip": "6 Wochen"
   },
   {
    "kind": "big",
    "say": "Insgesamt über einundzwanzig Kilometer Leitplanken und zwanzigtausend Quadratmeter Zaun.",
    "chip": "21 km"
   },
   {
    "kind": "big",
    "say": "Aber die Stadt schließt nicht: gegen sieben Uhr abends werden die Straßen wieder für den Verkehr geöffnet."
   },
   {
    "kind": "big",
    "say": "Um sechs Uhr morgens wird wieder gesperrt, und die Rennwagen fahren raus."
   },
   {
    "kind": "big",
    "say": "Die Strecke ist eng, überholen fast unmöglich, deshalb entscheidet hier das Qualifying."
   },
   {
    "kind": "big",
    "say": "Ergebnis: drei Komma drei Kilometer, neunzehn Kurven und Rennen hier seit neunzehnhundertneunundzwanzig.",
    "chip": "3,3 km · seit 1929"
   },
   {
    "kind": "end",
    "say": "Alle Strecken der Saison in 3D gibt es auf LapRadar.",
    "tag": "Alle Strecken in 3D"
   }
  ],
  "zh": [
   {
    "kind": "title",
    "say": "摩纳哥的街道居民每天都要用，那赛道要怎么建？",
    "head": "建一条赛道",
    "sub": "摩纳哥"
   },
   {
    "kind": "big",
    "say": "比赛前六周开工，几乎都在夜里施工，白天照常通车。",
    "chip": "6 周"
   },
   {
    "kind": "big",
    "say": "一共要装超过二十一公里护栏和两万平方米防护网。",
    "chip": "21 公里"
   },
   {
    "kind": "big",
    "say": "但城市不封闭：晚上七点左右，街道重新对普通车辆开放。"
   },
   {
    "kind": "big",
    "say": "早上六点再次封路，赛车开上街道。"
   },
   {
    "kind": "big",
    "say": "赛道很窄，几乎没地方超车，所以排位赛决定一切。"
   },
   {
    "kind": "big",
    "say": "结果：三点三公里，十九个弯，这里从一九二九年就开始比赛。",
    "chip": "3.3 公里 · 始于 1929"
   },
   {
    "kind": "end",
    "say": "本赛季所有赛道的 3D 画面，都在 LapRadar。",
    "tag": "所有赛道 3D 呈现"
   }
  ]
 }
}

# Как построить трассу Формулы 1 в Баку. Ролик без статьи, камера (shots) общая для всех языков.
VIDEO = {
 "slug": "build-baku",
 "id": "build-baku",
 "track": "baku",
 "theme": "dusk",
 "titles": {
  "ru": "Как построить трассу Формулы 1 в Баку",
  "en": "How to build an F1 track in Baku",
  "es": "Cómo construir un circuito de F1 en Bakú",
  "pt": "Como construir uma pista de F1 em Baku",
  "de": "So baust du eine F1-Strecke in Baku",
  "zh": "如何在巴库建一条F1赛道"
 },
 "captions": {
  "ru": "Крепость XII века, 7,6 метра между стенами и 2,2 км в пол. Все трассы в 3D: lapradar.com",
  "en": "A 12th-century fortress, 7.6 metres between walls and 2.2 km flat out. Every track in 3D: lapradar.com",
  "es": "Una fortaleza del siglo XII, 7,6 metros entre muros y 2,2 km a fondo. Todos los circuitos en 3D: lapradar.com",
  "pt": "Uma fortaleza do século XII, 7,6 metros entre muros e 2,2 km de pé embaixo. Todas as pistas em 3D: lapradar.com",
  "de": "Eine Festung aus dem 12. Jahrhundert, 7,6 Meter zwischen den Mauern und 2,2 km Vollgas. Alle Strecken in 3D: lapradar.com",
  "zh": "十二世纪古城墙、墙间7.6米、2.2公里全油门。所有赛道3D呈现：lapradar.com"
 },
 "shots": [
  {
   "type": "orbit",
   "r": 1500,
   "r2": 1200,
   "h": 600,
   "h2": 420,
   "a0": 0.5,
   "a1": 0.9,
   "build": {
    "walls": "on"
   }
  },
  {
   "type": "chase",
   "follow": "taxi",
   "dist": 15,
   "dist2": 20,
   "h": 6,
   "h2": 10,
   "side": 3,
   "side2": -4,
   "look": 20,
   "drop": 3,
   "act": {
    "type": "traffic",
    "at": 0.2
   },
   "build": {
    "walls": "grow",
    "focus": "taxi",
    "R": 240
   }
  },
  {
   "type": "chase",
   "car": 0,
   "dist": 34,
   "dist2": 26,
   "h": 24,
   "h2": 18,
   "side": 12,
   "side2": 8,
   "look": 8,
   "drop": 6,
   "act": {
    "type": "narrow",
    "corner": 8,
    "tc": 0.7
   },
   "build": {
    "walls": "on"
   }
  },
  {
   "type": "chase",
   "car": 0,
   "dist": 8.5,
   "dist2": 8,
   "h": 3,
   "h2": 2.8,
   "side": 0,
   "side2": 0,
   "look": 12,
   "drop": 2.6,
   "act": {
    "type": "narrow",
    "corner": 8,
    "tc": 0.4
   },
   "build": {
    "walls": "on"
   }
  },
  {
   "type": "chase",
   "car": 0,
   "dist": 9,
   "dist2": 8,
   "h": 3,
   "h2": 2.6,
   "side": -2.5,
   "side2": 2,
   "look": 20,
   "drop": 2.4,
   "act": {
    "type": "speed"
   },
   "build": {
    "walls": "on"
   }
  },
  {
   "type": "chase",
   "car": 0,
   "dist": 11,
   "dist2": 10,
   "h": 4.5,
   "h2": 4.2,
   "side": 1.5,
   "side2": 1,
   "look": 10,
   "drop": 3,
   "act": {
    "type": "energy"
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
   "rot0": 0.1,
   "rot1": 0.28,
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
   "r": 1700,
   "r2": 1300,
   "h": 700,
   "h2": 500,
   "a0": 2.0,
   "a1": 2.6,
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
    "say": "Теперь строим трассу в Баку, самую быструю городскую трассу календаря.",
    "head": "ПОСТРОЙ ТРАССУ",
    "sub": "в Баку"
   },
   {
    "kind": "big",
    "say": "Улицы перекрываешь стенами на весь гоночный уикенд, а не только на день."
   },
   {
    "kind": "big",
    "say": "Часть круга идёт вдоль стен старой крепости двенадцатого века, под охраной ЮНЕСКО."
   },
   {
    "kind": "big",
    "say": "Там между стенами всего семь и шесть десятых метра, а болид почти два метра в ширину.",
    "chip": "7,6 м"
   },
   {
    "kind": "big",
    "say": "Потом выезжаешь на набережную и едешь в пол больше двух километров.",
    "chip": "2,2 км"
   },
   {
    "kind": "big",
    "say": "В конце прямой скорость за триста пятьдесят и поворот под прямым углом.",
    "chip": "350+ км/ч"
   },
   {
    "kind": "big",
    "say": "Итог: шесть километров и двадцать поворотов. Ошибся, и ты уже в стене.",
    "chip": "6 км · 20 поворотов"
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
    "say": "Now we build a track in Baku, the fastest street circuit on the calendar.",
    "head": "BUILD A TRACK",
    "sub": "in Baku"
   },
   {
    "kind": "big",
    "say": "You close the streets with walls for the whole race weekend, not just one day."
   },
   {
    "kind": "big",
    "say": "Part of the lap runs along the walls of a twelfth-century fortress, protected by UNESCO."
   },
   {
    "kind": "big",
    "say": "Between those walls the track is just seven point six metres wide, and the car is almost two metres wide.",
    "chip": "7.6 m"
   },
   {
    "kind": "big",
    "say": "Then you hit the seafront and stay flat out for more than two kilometres.",
    "chip": "2.2 km"
   },
   {
    "kind": "big",
    "say": "At the end of the straight you're doing over three hundred and fifty, into a ninety-degree corner.",
    "chip": "350+ km/h"
   },
   {
    "kind": "big",
    "say": "The result: six kilometres and twenty corners. One mistake and you're in the wall.",
    "chip": "6 km · 20 turns"
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
    "say": "Ahora construimos un circuito en Bakú, el urbano más rápido del calendario.",
    "head": "CONSTRUYE UN CIRCUITO",
    "sub": "en Bakú"
   },
   {
    "kind": "big",
    "say": "Cierras las calles con muros durante todo el fin de semana, no solo un día."
   },
   {
    "kind": "big",
    "say": "Parte de la vuelta pasa junto a las murallas de una fortaleza del siglo doce, protegida por la UNESCO."
   },
   {
    "kind": "big",
    "say": "Ahí la pista mide solo siete coma seis metros, y el coche tiene casi dos de ancho.",
    "chip": "7,6 m"
   },
   {
    "kind": "big",
    "say": "Luego sales al paseo marítimo y vas a fondo más de dos kilómetros.",
    "chip": "2,2 km"
   },
   {
    "kind": "big",
    "say": "Al final de la recta vas a más de trescientos cincuenta y entras en una curva de noventa grados.",
    "chip": "350+ km/h"
   },
   {
    "kind": "big",
    "say": "Resultado: seis kilómetros y veinte curvas. Un error y estás en el muro.",
    "chip": "6 km · 20 curvas"
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
    "say": "Agora vamos construir uma pista em Baku, a pista de rua mais rápida do calendário.",
    "head": "CONSTRUA UMA PISTA",
    "sub": "em Baku"
   },
   {
    "kind": "big",
    "say": "Você fecha as ruas com muros durante todo o fim de semana, não só por um dia."
   },
   {
    "kind": "big",
    "say": "Parte da volta passa pelas muralhas de uma fortaleza do século doze, protegida pela UNESCO."
   },
   {
    "kind": "big",
    "say": "Ali a pista tem só sete vírgula seis metros, e o carro tem quase dois de largura.",
    "chip": "7,6 m"
   },
   {
    "kind": "big",
    "say": "Depois você sai na orla e anda de pé embaixo por mais de dois quilômetros.",
    "chip": "2,2 km"
   },
   {
    "kind": "big",
    "say": "No fim da reta você passa dos trezentos e cinquenta e entra numa curva de noventa graus.",
    "chip": "350+ km/h"
   },
   {
    "kind": "big",
    "say": "Resultado: seis quilômetros e vinte curvas. Errou, e você está no muro.",
    "chip": "6 km · 20 curvas"
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
    "say": "Jetzt bauen wir eine Strecke in Baku, den schnellsten Stadtkurs im Kalender.",
    "head": "BAU DIR EINE STRECKE",
    "sub": "in Baku"
   },
   {
    "kind": "big",
    "say": "Die Straßen sperrst du mit Mauern für das ganze Rennwochenende, nicht nur für einen Tag."
   },
   {
    "kind": "big",
    "say": "Ein Teil der Runde führt an den Mauern einer Festung aus dem zwölften Jahrhundert vorbei, UNESCO-Welterbe."
   },
   {
    "kind": "big",
    "say": "Dort ist die Strecke nur sieben Komma sechs Meter breit, das Auto fast zwei Meter.",
    "chip": "7,6 m"
   },
   {
    "kind": "big",
    "say": "Dann geht es an die Uferstraße, über zwei Kilometer Vollgas.",
    "chip": "2,2 km"
   },
   {
    "kind": "big",
    "say": "Am Ende der Geraden bist du schneller als dreihundertfünfzig und bremst in eine Neunzig-Grad-Kurve.",
    "chip": "350+ km/h"
   },
   {
    "kind": "big",
    "say": "Ergebnis: sechs Kilometer und zwanzig Kurven. Ein Fehler, und du bist in der Mauer.",
    "chip": "6 km · 20 Kurven"
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
    "say": "现在我们在巴库建赛道，这是赛历上最快的街道赛道。",
    "head": "建一条赛道",
    "sub": "巴库"
   },
   {
    "kind": "big",
    "say": "整个比赛周末都要用墙封闭街道，不只是一天。"
   },
   {
    "kind": "big",
    "say": "一段赛道紧贴十二世纪古城墙，那里是联合国教科文组织世界遗产。"
   },
   {
    "kind": "big",
    "say": "城墙之间只有七点六米宽，而赛车将近两米宽。",
    "chip": "7.6 米"
   },
   {
    "kind": "big",
    "say": "接着开上海滨大道，全油门超过两公里。",
    "chip": "2.2 公里"
   },
   {
    "kind": "big",
    "say": "直道尽头时速超过三百五十公里，然后是一个九十度弯。",
    "chip": "350+ 公里/时"
   },
   {
    "kind": "big",
    "say": "结果：六公里，二十个弯。一失误就撞墙。",
    "chip": "6 公里 · 20 个弯"
   },
   {
    "kind": "end",
    "say": "本赛季所有赛道的 3D 画面，都在 LapRadar。",
    "tag": "所有赛道 3D 呈现"
   }
  ]
 }
}

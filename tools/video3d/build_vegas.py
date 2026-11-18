# Как построить трассу Формулы 1 в Лас-Вегасе. Ролик без статьи, камера (shots) общая для всех языков.
VIDEO = {
 "slug": "build-vegas",
 "id": "build-vegas",
 "track": "las-vegas",
 "theme": "vegas",
 "city": True,
 "titles": {
  "ru": "Как построить трассу Формулы 1 в Лас-Вегасе",
  "en": "How to build an F1 track in Las Vegas",
  "es": "Cómo construir un circuito de F1 en Las Vegas",
  "pt": "Como construir uma pista de F1 em Las Vegas",
  "de": "So baust du eine F1-Strecke in Las Vegas",
  "zh": "如何在拉斯维加斯建一条F1赛道"
 },
 "captions": {
  "ru": "Бетонные блоки, люки, прожекторы и 1,9 км по Стрипу. Все трассы в 3D: lapradar.com",
  "en": "Concrete blocks, manholes, floodlights and 1.9 km down the Strip. Every track in 3D: lapradar.com",
  "es": "Bloques de hormigón, alcantarillas, focos y 1,9 km por el Strip. Todos los circuitos en 3D: lapradar.com",
  "pt": "Blocos de concreto, bueiros, holofotes e 1,9 km pela Strip. Todas as pistas em 3D: lapradar.com",
  "de": "Betonblöcke, Gullydeckel, Flutlicht und 1,9 km über den Strip. Alle Strecken in 3D: lapradar.com",
  "zh": "混凝土护墙、井盖、照明灯和1.9公里的大道直道。所有赛道3D呈现：lapradar.com"
 },
 "shots": [
  {
   "type": "fly",
   "from": 0.42,
   "to": 0.5,
   "h": 110, "h2": 170,
   "side": 0,
   "ahead": 250,
   "build": {
    "walls": "on",
    "lights": "on"
   }
  },
  {
   "type": "chase",
   "follow": "taxi",
   "dist": 15,
   "dist2": 20,
   "h": 6,
   "h2": 10,
   "side": -3,
   "side2": 4,
   "look": 20,
   "drop": 3,
   "act": {
    "type": "traffic",
    "at": 0.45
   },
   "build": {
    "walls": "grow",
    "lights": "off",
    "focus": "taxi",
    "R": 240
   }
  },
  {
   "type": "chase",
   "car": 0,
   "dist": 11,
   "dist2": 9,
   "h": 3.4,
   "h2": 3.8,
   "side": 3.5,
   "side2": 2.5,
   "look": 14,
   "drop": 2.8,
   "act": {
    "type": "manhole"
   },
   "build": {
    "walls": "on",
    "lights": "on"
   }
  },
  {
   "type": "chase",
   "follow": "focus",
   "dist": 11,
   "dist2": 8,
   "h": 4.5,
   "h2": 3.2,
   "side": 6,
   "side2": 4,
   "look": 4,
   "drop": 3,
   "act": {
    "type": "weld"
   },
   "build": {
    "walls": "on",
    "lights": "on"
   }
  },
  {
   "type": "chase",
   "car": 0,
   "dist": 40,
   "dist2": 70,
   "h": 18,
   "h2": 38,
   "side": -10,
   "side2": -22,
   "look": 60,
   "drop": 6,
   "build": {
    "walls": "on",
    "lights": "grow",
    "RL": 1400
   }
  },
  {
   "type": "chase",
   "car": 0,
   "dist": 9,
   "dist2": 8,
   "h": 3,
   "h2": 2.6,
   "side": 2.5,
   "side2": -2,
   "look": 20,
   "drop": 2.4,
   "act": {
    "type": "speed"
   },
   "build": {
    "walls": "on",
    "lights": "on"
   }
  },
  {
   "type": "top",
   "reveal": True,
   "badges": True,
   "k": 1.12,
   "tilt": 0.22,
   "rot0": 0.12,
   "rot1": 0.3,
   "act": {
    "type": "trace",
    "at": 0.05
   },
   "build": {
    "walls": "on",
    "lights": "on"
   }
  },
  {
   "type": "fly",
   "from": 0.7,
   "to": 0.78,
   "h": 120,
   "h2": 200,
   "side": -60,
   "ahead": 300,
   "build": {
    "walls": "on",
    "lights": "on"
   }
  }
 ],
 "images": [],
 "scenes": {
  "ru": [
   {
    "kind": "title",
    "say": "Давай построим трассу Формулы один прямо в центре Лас-Вегаса.",
    "head": "ПОСТРОЙ ТРАССУ",
    "sub": "в Лас-Вегасе"
   },
   {
    "kind": "big",
    "say": "Сначала перекрываешь улицы и ставишь вдоль них бетонные блоки."
   },
   {
    "kind": "big",
    "say": "Асфальт городской, с люками. На первой же тренировке в две тысячи двадцать третьем крышку люка вырвало прямо под Ferrari.",
    "chip": "2023"
   },
   {
    "kind": "big",
    "say": "Вторую тренировку задержали на два с половиной часа, пока проверяли и крепили люки по всей трассе."
   },
   {
    "kind": "big",
    "say": "Гонка ночная, поэтому вдоль всего круга ставишь прожекторы."
   },
   {
    "kind": "big",
    "say": "А главное блюдо здесь прямая по бульвару Стрип: почти два километра в пол.",
    "chip": "1,9 км"
   },
   {
    "kind": "big",
    "say": "Итог: шесть и две десятых километра и семнадцать поворотов прямо между казино.",
    "chip": "6,2 км · 17 поворотов"
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
    "say": "Let's build a Formula One track right in the middle of Las Vegas.",
    "head": "BUILD A TRACK",
    "sub": "in Las Vegas"
   },
   {
    "kind": "big",
    "say": "First you close the streets and line them with concrete blocks."
   },
   {
    "kind": "big",
    "say": "It's normal city asphalt with manholes. In the very first practice in twenty twenty-three, a manhole cover was ripped out under a Ferrari.",
    "chip": "2023"
   },
   {
    "kind": "big",
    "say": "Second practice was delayed two and a half hours while every manhole on the lap was checked and secured."
   },
   {
    "kind": "big",
    "say": "The race runs at night, so you put floodlights all the way around the lap."
   },
   {
    "kind": "big",
    "say": "The main course is the run down the Strip: almost two kilometres flat out.",
    "chip": "1.9 km"
   },
   {
    "kind": "big",
    "say": "The result: six point two kilometres and seventeen corners, right between the casinos.",
    "chip": "6.2 km · 17 turns"
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
    "say": "Vamos a construir un circuito de Fórmula uno en pleno centro de Las Vegas.",
    "head": "CONSTRUYE UN CIRCUITO",
    "sub": "en Las Vegas"
   },
   {
    "kind": "big",
    "say": "Primero cierras las calles y colocas bloques de hormigón a lo largo."
   },
   {
    "kind": "big",
    "say": "El asfalto es de ciudad, con alcantarillas. En el primer libre de dos mil veintitrés, una tapa salió volando bajo un Ferrari.",
    "chip": "2023"
   },
   {
    "kind": "big",
    "say": "El segundo libre se retrasó dos horas y media mientras revisaban y fijaban todas las tapas del circuito."
   },
   {
    "kind": "big",
    "say": "La carrera es de noche, así que pones focos alrededor de toda la vuelta."
   },
   {
    "kind": "big",
    "say": "Y el plato fuerte es la recta del Strip: casi dos kilómetros a fondo.",
    "chip": "1,9 km"
   },
   {
    "kind": "big",
    "say": "Resultado: seis coma dos kilómetros y diecisiete curvas, entre casinos.",
    "chip": "6,2 km · 17 curvas"
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
    "say": "Vamos construir uma pista de Fórmula um bem no centro de Las Vegas.",
    "head": "CONSTRUA UMA PISTA",
    "sub": "em Las Vegas"
   },
   {
    "kind": "big",
    "say": "Primeiro você fecha as ruas e coloca blocos de concreto ao longo delas."
   },
   {
    "kind": "big",
    "say": "O asfalto é de cidade, com bueiros. No primeiro treino de dois mil e vinte e três, uma tampa foi arrancada debaixo de uma Ferrari.",
    "chip": "2023"
   },
   {
    "kind": "big",
    "say": "O segundo treino atrasou duas horas e meia enquanto checavam e fixavam todas as tampas da pista."
   },
   {
    "kind": "big",
    "say": "A corrida é à noite, então você instala holofotes em toda a volta."
   },
   {
    "kind": "big",
    "say": "E o prato principal é a reta da Strip: quase dois quilômetros de pé embaixo.",
    "chip": "1,9 km"
   },
   {
    "kind": "big",
    "say": "Resultado: seis vírgula dois quilômetros e dezessete curvas, no meio dos cassinos.",
    "chip": "6,2 km · 17 curvas"
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
    "say": "Wir bauen eine Formel-1-Strecke mitten in Las Vegas.",
    "head": "BAU DIR EINE STRECKE",
    "sub": "in Las Vegas"
   },
   {
    "kind": "big",
    "say": "Zuerst sperrst du die Straßen und stellst Betonblöcke an den Rand."
   },
   {
    "kind": "big",
    "say": "Der Asphalt ist ganz normal, mit Gullys. Schon im ersten Training zweitausenddreiundzwanzig riss ein Gullydeckel unter einem Ferrari heraus.",
    "chip": "2023"
   },
   {
    "kind": "big",
    "say": "Das zweite Training begann zweieinhalb Stunden später, weil alle Deckel auf der Runde geprüft und gesichert wurden."
   },
   {
    "kind": "big",
    "say": "Das Rennen läuft nachts, also stellst du rund um die Runde Flutlicht auf."
   },
   {
    "kind": "big",
    "say": "Das Highlight ist die Gerade über den Strip: fast zwei Kilometer Vollgas.",
    "chip": "1,9 km"
   },
   {
    "kind": "big",
    "say": "Ergebnis: sechs Komma zwei Kilometer und siebzehn Kurven zwischen den Casinos.",
    "chip": "6,2 km · 17 Kurven"
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
    "say": "我们来在拉斯维加斯市中心建一条F1赛道。",
    "head": "建一条赛道",
    "sub": "拉斯维加斯"
   },
   {
    "kind": "big",
    "say": "先封闭街道，沿路摆上混凝土护墙。"
   },
   {
    "kind": "big",
    "say": "路面是普通城市道路，还有井盖。二零二三年第一次练习赛，一块井盖在法拉利车底被掀飞。",
    "chip": "2023"
   },
   {
    "kind": "big",
    "say": "第二次练习赛推迟了两个半小时，全场井盖逐个检查加固。"
   },
   {
    "kind": "big",
    "say": "比赛在夜间进行，所以整圈都要装上照明灯。"
   },
   {
    "kind": "big",
    "say": "最精彩的是拉斯维加斯大道上的直道：将近两公里全油门。",
    "chip": "1.9 公里"
   },
   {
    "kind": "big",
    "say": "结果：六点二公里，十七个弯，就在赌场之间。",
    "chip": "6.2 公里 · 17 个弯"
   },
   {
    "kind": "end",
    "say": "本赛季所有赛道的 3D 画面，都在 LapRadar。",
    "tag": "所有赛道 3D 呈现"
   }
  ]
 }
}

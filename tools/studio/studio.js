// LapRadar Studio: мультяшные 3D-ролики 1080×1920 из собственной геометрии трасс.
// Никаких чужих картинок и ливрей: трасса — из наших данных, машинки, трибуны, пальмы — нарисованы кодом.
// Управляется из tools/render.py: window.setupVideo(spec) → window.renderFrame(i) → JPEG dataURL.
import * as THREE from 'three';

let W = 1080, H = 1920;
let R, gl, ctx, out, spec, world, stage, fps = 30, sceneStarts = [];

// ---------- утилиты ----------
const rng = seed => () => ((seed = (seed * 1664525 + 1013904223) >>> 0) / 4294967296);
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const ease = t => t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
const easeOut = t => 1 - Math.pow(1 - clamp(t), 3);
const back = t => { t = clamp(t); const c = 1.9; return 1 + (c + 1) * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2); };
const lerp = (a, b, t) => a + (b - a) * t;
const glowTex = (inner = 'rgba(255,240,200,1)', outer = 'rgba(255,200,120,0)') => {
  const c = document.createElement('canvas'); c.width = c.height = 128; const g = c.getContext('2d');
  const r = g.createRadialGradient(64, 64, 0, 64, 64, 64); r.addColorStop(0, inner); r.addColorStop(0.25, inner.replace(/[\d.]+\)$/, '0.55)')); r.addColorStop(1, outer);
  g.fillStyle = r; g.fillRect(0, 0, 128, 128); return new THREE.CanvasTexture(c);
};
const gradTex = stops => {
  const c = document.createElement('canvas'); c.width = 4; c.height = 512; const g = c.getContext('2d');
  const gr = g.createLinearGradient(0, 0, 0, 512); stops.forEach(([o, col]) => gr.addColorStop(o, col)); g.fillStyle = gr; g.fillRect(0, 0, 4, 512);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
};

const THEMES = {
  night: { sky: [[0, '#070a1c'], [0.55, '#18265a'], [0.8, '#4a2c66'], [1, '#8a4a5a']], ground: '#b89a6a', runoff: '#d2bd92', asphalt: '#33373f', fog: '#2a2448', fogN: 1500, fogF: 7000, hemi: [0xaab8ff, 0x6a5030, 1.25], sun: [0xd0dcff, 0.9], lights: true, stars: true, palms: true, bld: ['#c9b48f', '#b9a27c', '#d8c7a3', '#a8916c'] },
  vegas: { sky: [[0, '#06061a'], [0.6, '#1c1c55'], [0.85, '#5b2470'], [1, '#c03a80']], ground: '#5a5866', runoff: '#76747e', asphalt: '#2d3038', fog: '#2a1848', fogN: 1500, fogF: 7000, hemi: [0xa898ff, 0x302040, 1.15], sun: [0xd0c0ff, 0.8], lights: true, stars: true, palms: false, neon: true, bld: ['#2e2a48', '#3a2f5a', '#463565', '#2a3a5c'] },
  dusk: { sky: [[0, '#1b2a5c'], [0.55, '#4a5fa0'], [0.8, '#d98a6a'], [1, '#f5c27a']], ground: '#c2a878', runoff: '#d8c9a3', asphalt: '#373a42', fog: '#c89a8a', fogN: 2000, fogF: 8000, hemi: [0xffd8c0, 0x5a4a3a, 1.1], sun: [0xffc890, 0.9], lights: true, stars: false, palms: true, bld: ['#e8d8c0', '#d8c4a8', '#f0e2cc', '#c9b394'] },
  day: { sky: [[0, '#2f7fd8'], [0.7, '#8fc3f2'], [1, '#e9f3ff']], ground: '#7fb25a', runoff: '#c9c2a8', asphalt: '#3a3d44', fog: '#cfe3f5', fogN: 2000, fogF: 8000, hemi: [0xffffff, 0x557744, 0.75], sun: [0xfff2dd, 1.1], lights: false, stars: false, palms: false, bld: ['#e8e2d6', '#d9d2c4', '#f1ece2', '#cfc6b5'] },
};
const CAR_COLORS = ['#3b82f6', '#f97316', '#f3f4f6', '#22c55e', '#a855f7', '#facc15', '#ef4444', '#06b6d4', '#ec4899', '#84cc16'];
const TYRE = { soft: '#ef3b3b', medium: '#ffd23f', hard: '#f2f2f2' };

// ---------- мир трассы ----------
async function buildWorld(trackName, themeName) {
  const T = THEMES[themeName] || THEMES.night;
  const tr = await (await fetch(`tracks/${trackName}.json`)).json();
  const map = tr.map ? await (await fetch(`../../seed/maps/${tr.map}.json`)).json().catch(() => null) : null;
  const zmin = Math.min(...tr.pts.map(p => p[2])), zrng = Math.max(...tr.pts.map(p => p[2])) - zmin;
  const elevK = tr.elev ?? Math.min(1.5, 30 / Math.max(1, zrng)); // перепад трассы не больше ~3 м: земля плоская, иначе лента «висит» в воздухе
  const cx = tr.pts.reduce((a, p) => a + p[0], 0) / tr.pts.length / 10, cy = tr.pts.reduce((a, p) => a + p[1], 0) / tr.pts.length / 10;
  const toV = (x, y, z) => new THREE.Vector3(x / 10 - cx, z == null ? 0 : (z - zmin) / 10 * elevK, -(y / 10 - cy));
  /* замкнутая кривая: убираем точки-дубли (особенно последнюю = первую), иначе у линии старта получается петля и машины едут назад */
  const cp = []; for (const p of tr.pts) { const v = toV(p[0], p[1], p[2]); if (!cp.length || v.distanceTo(cp[cp.length - 1]) > 0.5) cp.push(v); }
  { const d0 = cp[1].clone().sub(cp[0]).setY(0).normalize(); /* хвост данных заходит за линию старта — отрезаем, чтобы не было петли */
    while (cp.length > 3 && cp[cp.length - 1].distanceTo(cp[0]) < 80 && cp[cp.length - 1].clone().sub(cp[0]).setY(0).dot(d0) > -1) cp.pop(); }
  const curve = new THREE.CatmullRomCurve3(cp, true, 'centripetal');
  curve.arcLengthDivisions = Math.max(2000, tr.pts.length * 20); /* иначе точки идут неравномерно и машины то ускоряются, то тормозят */
  const L = curve.getLength(), N = Math.round(L / 3);
  const P = curve.getSpacedPoints(N).slice(0, N), TG = P.map((_, i) => P[(i + 1) % N].clone().sub(P[(i - 1 + N) % N]).setY(0).normalize());
  const NR = TG.map(t => new THREE.Vector3(-t.z, 0, t.x)); // нормаль вправо
  const scene = new THREE.Scene();
  scene.background = gradTex(T.sky); scene.fog = new THREE.Fog(T.fog, T.fogN, T.fogF);
  scene.add(new THREE.HemisphereLight(...T.hemi));
  const sun = new THREE.DirectionalLight(...T.sun); sun.position.set(-600, 900, 400); scene.add(sun);

  const ribbon = (w0, w1, y, colorFn, step = 1) => { // полоса от смещения w0 до w1 вдоль трассы
    const pos = [], col = [], idx = [], c = new THREE.Color();
    for (let i = 0; i <= N; i += step) {
      const k = i % N, p = P[k], n = NR[k];
      pos.push(p.x + n.x * w0, p.y + y, p.z + n.z * w0, p.x + n.x * w1, p.y + y, p.z + n.z * w1);
      c.set(colorFn(k)); col.push(c.r, c.g, c.b, c.r, c.g, c.b);
    }
    for (let i = 0; i < pos.length / 6 - 1; i++) { const a = i * 2; idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
    const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setAttribute('color', new THREE.Float32BufferAttribute(col, 3)); g.setIndex(idx); g.computeVertexNormals();
    if (HQ) { const uv = []; for (let i = 0; i <= N; i += step) { const v = i * L / N / Math.max(1, Math.abs(w1 - w0)); uv.push(0, v, 1, v); } g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2)); }   /* HQ: текстура асфальта */
    return new THREE.Mesh(g, new THREE.MeshLambertMaterial({ vertexColors: true, side: THREE.DoubleSide }));
  };
  // земля, зона безопасности, асфальт, линии, поребрики
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(30000, 30000), new THREE.MeshLambertMaterial({ color: T.ground })); ground.rotation.x = -Math.PI / 2; ground.position.y = -2.2; scene.add(ground);
  const runoff = ribbon(-24, 24, -0.25, () => T.runoff, 2); scene.add(runoff);
  const asphalt = ribbon(-7, 7, 0.02, () => T.asphalt); scene.add(asphalt);
  const lines = [ribbon(6.4, 6.8, 0.05, () => '#f4f4f4'), ribbon(-6.8, -6.4, 0.05, () => '#f4f4f4')]; scene.add(...lines);
  const kerbs = [], hqStreetOn = HQ && (HQO.street ?? (themeName === 'vegas' || !!spec.city || !!tr.street));
  const cornerIdx = (tr.corners || []).map(([n, x, y]) => { const v = toV(x, y); let bi = 0, bd = 1e18; P.forEach((p, i) => { const d = (p.x - v.x) ** 2 + (p.z - v.z) ** 2; if (d < bd) { bd = d; bi = i; } }); return { n, i: bi }; });
  const nearCorner = k => cornerIdx.some(c => Math.min(Math.abs(c.i - k), N - Math.abs(c.i - k)) < 14);
  const kerb = side => { const m = ribbon(side * 7, side * 8.6, 0.06, k => (Math.floor(k / 1) % 2 ? '#e8332e' : '#f6f6f6')); m.geometry.setDrawRange(0, 0); return m; };
  // поребрики — только у поворотов: собираем отдельные куски
  for (const c of cornerIdx) for (const side of [-1, 1]) {
    const pos = [], col = [], idx = [], cl = new THREE.Color();
    for (let j = -14; j <= 14; j++) { const k = (c.i + j + N) % N, p = P[k], n = NR[k];
      pos.push(p.x + n.x * side * 7, p.y + 0.08, p.z + n.z * side * 7, p.x + n.x * side * 8.6, p.y + 0.08, p.z + n.z * side * 8.6);
      cl.set(((j + 100) >> 1) & 1 ? '#e8332e' : '#f6f6f6'); /* полосы по 6 м: меньше стробоскопа в движении */ col.push(cl.r, cl.g, cl.b, cl.r, cl.g, cl.b); }
    for (let i = 0; i < pos.length / 6 - 1; i++) { const a = i * 2; idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
    const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setAttribute('color', new THREE.Float32BufferAttribute(col, 3)); g.setIndex(idx);
    const km = new THREE.Mesh(g, new THREE.MeshBasicMaterial({ vertexColors: true, side: THREE.DoubleSide })); scene.add(km); kerbs.push(km);
  }
  // старт: шахматная линия
  { const c = document.createElement('canvas'); c.width = 64; c.height = 8; const g = c.getContext('2d'); for (let i = 0; i < 16; i++) for (let j = 0; j < 2; j++) { g.fillStyle = (i + j) % 2 ? '#111' : '#fff'; g.fillRect(i * 4, j * 4, 4, 4); }
    const t = new THREE.CanvasTexture(c); t.magFilter = THREE.NearestFilter; const m = new THREE.Mesh(new THREE.PlaneGeometry(14, 1.8), new THREE.MeshBasicMaterial({ map: t }));
    m.rotation.x = -Math.PI / 2; m.rotation.z = Math.atan2(TG[0].x, TG[0].z) + Math.PI / 2; m.position.copy(P[0]).setY(P[0].y + 0.07); scene.add(m); }

  // нативный брендинг на трассе: арка LapRadar над стартовой прямой и щиты вдоль трассы (как реклама спонсора)
  if (spec?.brand3d !== false) {
    const k0 = Math.round(18 / (L / N)) % N, p0 = P[k0], ang = Math.atan2(TG[k0].x, TG[k0].z), dark = new THREE.MeshLambertMaterial({ color: '#1b2030' });
    const arch = new THREE.Group(); arch.position.copy(p0); arch.rotation.y = ang;
    for (const sx of [-1, 1]) { const post = new THREE.Mesh(new THREE.BoxGeometry(0.7, 7.5, 0.7), dark); post.position.set(sx * 10.5, 3.75, 0); arch.add(post); }
    const beam = new THREE.Mesh(new THREE.BoxGeometry(21.7, 1.9, 0.8), dark); beam.position.set(0, 7.2, 0); arch.add(beam);
    for (const sz of [-1, 1]) { const b = new THREE.Mesh(new THREE.PlaneGeometry(8.4, 2.1), new THREE.MeshBasicMaterial({ map: brandTex('board') })); b.position.set(0, 7.2, sz * 0.41); if (sz < 0) b.rotation.y = Math.PI; arch.add(b); }
    scene.add(arch);
    const boardM = new THREE.MeshBasicMaterial({ map: brandTex('board') }), step = Math.max(40, Math.floor(N / 9));
    for (let i = step >> 1, n = 0; n < 9 && !hqStreetOn; i = (i + step) % N, n++) {   /* HQ на городской трассе: щиты на бетонных блоках */ const p = P[i], nr = NR[i], side = n % 2 ? 1 : -1;
      const b = new THREE.Mesh(new THREE.PlaneGeometry(6, 1.5), boardM); b.position.set(p.x + nr.x * side * 10.2, p.y + 0.9, p.z + nr.z * side * 10.2);
      b.lookAt(p.x, p.y + 0.9, p.z); scene.add(b); }
  }
  const R0 = rng(7);
  const distToTrack = (x, z) => { let bd = 1e9; for (let i = 0; i < N; i += 3) { const d = Math.hypot(P[i].x - x, P[i].z - z); if (d < bd) bd = d; } return bd; };
  // здания из OSM — мультяшные коробки
  let bldMesh = null, bldRanges = [];
  if (map?.buildings?.length) {
    const geos = []; let vtx = 0;
    for (const b of map.buildings) {
      const pts = []; for (let i = 0; i < b.p.length; i += 2) { const v = toV(b.p[i], b.p[i + 1]); pts.push(new THREE.Vector2(v.x, -v.z)); }
      if (pts.length < 3) continue;
      const h = Math.max(4, (b.h || 80) / 10) * (tr.bScale ?? 1);
      const g = new THREE.ExtrudeGeometry(new THREE.Shape(pts), { depth: h, bevelEnabled: false }); g.rotateX(-Math.PI / 2);
      const col = new THREE.Color(T.bld[Math.floor(R0() * T.bld.length)]); const cs = []; for (let i = 0; i < g.attributes.position.count; i++) cs.push(col.r, col.g, col.b);
      g.setAttribute('color', new THREE.Float32BufferAttribute(cs, 3)); geos.push(g);
      const cnt = g.index ? g.index.count : g.attributes.position.count; bldRanges.push({ b, pts, h, start: vtx, count: cnt }); vtx += cnt; /* для сцен с огнями Стрипа и Sphere (только чтение) */
    }
    if (geos.length) { const merged = HQ ? mergeGeosUV(geos) : mergeGeos(geos); const m = new THREE.Mesh(merged, new THREE.MeshLambertMaterial({ vertexColors: true, emissive: themeName === 'day' ? 0x000000 : 0x1a1410 })); m.position.y = -0.3; scene.add(m); bldMesh = m; }
  }
  // газоны
  if (map?.green?.length) for (const [gi, gr] of map.green.slice(0, 400).entries()) {
    const pts = []; for (let i = 0; i < gr.p.length; i += 2) { const v = toV(gr.p[i], gr.p[i + 1]); pts.push(new THREE.Vector2(v.x, -v.z)); }
    if (pts.length < 3) continue; const g = new THREE.ShapeGeometry(new THREE.Shape(pts)); g.rotateX(-Math.PI / 2);
    const m = new THREE.Mesh(g, new THREE.MeshLambertMaterial({ color: gr.k === 'wood' ? '#3f6b35' : '#5f8f45' })); m.position.y = -1.2 - (gr.k === 'wood' ? 0.15 : 0) - (gi % 7) * 0.03; scene.add(m); // разная высота, чтобы перекрывающиеся газоны не мерцали
  }
  // пальмы (Катар, Абу-Даби, Бахрейн)
  if (T.palms) {
    const n = 260, trunk = new THREE.InstancedMesh(new THREE.CylinderGeometry(0.35, 0.55, 9, 6), new THREE.MeshLambertMaterial({ color: '#7a5532' }), n);
    const leafG = new THREE.ConeGeometry(4.2, 2.2, 7); leafG.translate(0, 1, 0);
    const leaf = new THREE.InstancedMesh(leafG, new THREE.MeshLambertMaterial({ color: '#2f8a3c', emissive: 0x0a2010 }), n);
    const m4 = new THREE.Matrix4(); let k = 0;
    for (let tries = 0; tries < 6000 && k < n; tries++) {
      const i = Math.floor(R0() * N), side = R0() < 0.5 ? -1 : 1, off = 30 + R0() * 90, p = P[i], q = NR[i];
      const x = p.x + q.x * off * side, z = p.z + q.z * off * side; if (distToTrack(x, z) < 26) continue;
      const s = 0.8 + R0() * 0.5;
      m4.makeScale(s, s, s).setPosition(x, 4.5 * s, z); trunk.setMatrixAt(k, m4);
      m4.makeRotationY(R0() * 6).scale(new THREE.Vector3(s, s, s)).setPosition(x, 9 * s, z); leaf.setMatrixAt(k, m4); k++;
    }
    trunk.count = leaf.count = k; scene.add(trunk, leaf);
  }
  // трибуны у старта
  { const g = new THREE.Group(), i0 = 8;
    for (let j = 0; j < 5; j++) { const k = (i0 + j * 14) % N, p = P[k], n = NR[k], ang = Math.atan2(TG[k].x, TG[k].z);
      const st = new THREE.Group();
      for (let r = 0; r < 6; r++) { const step = new THREE.Mesh(new THREE.BoxGeometry(40, 1.6, 3), new THREE.MeshLambertMaterial({ color: r % 2 ? '#d9dde5' : '#c3c9d4' })); step.position.set(0, r * 1.6 + 0.8, r * 3); st.add(step); }
      const crowd = new THREE.InstancedMesh(new THREE.BoxGeometry(0.7, 0.9, 0.7), new THREE.MeshBasicMaterial(), 6 * 40); const m4 = new THREE.Matrix4(), cc = new THREE.Color(); let c = 0;
      for (let r = 0; r < 6; r++) for (let s = 0; s < 40; s++) { if (R0() < 0.15) continue; m4.makeTranslation(-19.5 + s, r * 1.6 + 2.1, r * 3); crowd.setMatrixAt(c, m4); crowd.setColorAt(c, cc.set(CAR_COLORS[Math.floor(R0() * CAR_COLORS.length)])); c++; }
      crowd.count = c; st.add(crowd);
      const roof = new THREE.Mesh(new THREE.BoxGeometry(42, 0.6, 20), new THREE.MeshLambertMaterial({ color: '#f2f2f2' })); roof.position.set(0, 14, 7); st.add(roof);
      st.position.set(p.x + n.x * 30, p.y, p.z + n.z * 30); st.rotation.y = ang + Math.PI / 2; st.lookAt(p.x, p.y, p.z); st.rotateY(Math.PI); g.add(st); }
    scene.add(g); }
  // прожекторы и световые пятна на асфальте (ночные гонки)
  const lightObjs = [];
  if (T.lights && !HQ) {   /* HQ: свои фонари (hqLamps) */
    const glow = new THREE.SpriteMaterial({ map: glowTex(), color: 0xffffff, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false });
    const poolMat = new THREE.MeshBasicMaterial({ map: glowTex('rgba(255,236,190,0.55)', 'rgba(255,236,190,0)'), transparent: true, depthWrite: false, blending: THREE.AdditiveBlending });
    const poleG = new THREE.CylinderGeometry(0.4, 0.6, 32, 6), poleM = new THREE.MeshLambertMaterial({ color: '#8a8f99' });
    for (let i = 0; i < N; i += 28) { const side = (i / 28) % 2 ? 1 : -1, p = P[i], n = NR[i];
      const x = p.x + n.x * side * 20, z = p.z + n.z * side * 20;
      const pole = new THREE.Mesh(poleG, poleM); pole.position.set(x, p.y + 16, z); scene.add(pole);
      const head = new THREE.Mesh(new THREE.BoxGeometry(4, 2, 1), new THREE.MeshBasicMaterial({ color: '#fff7dd' })); head.position.set(x, p.y + 32, z); head.lookAt(p.x, p.y, p.z); scene.add(head);
      const s = new THREE.Sprite(glow); s.scale.set(26, 26, 1); s.position.set(x, p.y + 32, z); scene.add(s);
      const pool = new THREE.Mesh(new THREE.PlaneGeometry(55, 55), poolMat); pool.rotation.x = -Math.PI / 2; pool.position.set(p.x + n.x * side * 4, p.y + 0.12, p.z + n.z * side * 4); scene.add(pool);
      lightObjs.push({ s: i / N * L, objs: [pole, head, s, pool] }); }
  }
  // звёзды
  if (T.stars) { const v = []; const r = rng(3); for (let i = 0; i < 1500; i++) { const a = r() * Math.PI * 2, e = 0.12 + r() * 1.3, d = 3800; v.push(Math.cos(a) * Math.cos(e) * d, Math.sin(e) * d, Math.sin(a) * Math.cos(e) * d); }
    const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(v, 3)); scene.add(new THREE.Points(g, new THREE.PointsMaterial({ color: 0xffffff, size: 2.2, sizeAttenuation: false, fog: false }))); }

  // светящаяся линия трассы для вида сверху (раскрывается по ходу сцены)
  const glowLine = ribbon(-9, 9, 1.5, () => '#4f8cff'); glowLine.material = new THREE.MeshBasicMaterial({ color: '#5b9bff', transparent: true, opacity: 0.85, side: THREE.DoubleSide, depthWrite: false, fog: false }); glowLine.visible = false; scene.add(glowLine);
  // номера поворотов
  const badges = cornerIdx.map(c => { const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: badgeTex(String(c.n)), depthTest: false, transparent: true, fog: false })); s.position.copy(P[c.i]).setY(P[c.i].y + 25); s.scale.set(70, 70, 1); s.visible = false; scene.add(s); return { s, i: c.i }; });

  // машины
  const cars = [];
  const nCars = tr.cars ?? 8;
  for (let k = 0; k < nCars; k++) { const m = (HQ ? makeCarHQ : makeCar)(CAR_COLORS[k % CAR_COLORS.length], k === 0 ? TYRE.soft : k % 3 === 1 ? TYRE.medium : TYRE.hard); scene.add(m.group); cars.push({ ...m, s0: L - k * 22 - (k > 3 ? 40 : 0), v: 72 - k * 0.7, lane: ((k % 3) - 1) * 2.2 }); }

  const at = s => { s = ((s % L) + L) % L; const f = s / L * N, i = Math.floor(f) % N, j = (i + 1) % N, u = f - Math.floor(f); return { p: P[i].clone().lerp(P[j], u), t: TG[i].clone().lerp(TG[j], u).normalize(), n: NR[i].clone().lerp(NR[j], u).normalize(), i }; };
  const box = new THREE.Box3().setFromPoints(P); const size = box.getSize(new THREE.Vector3());
  // поворот трассы для вертикального кадра: длинная сторона — вдоль экрана
  let best = { cost: 1e18, a: 0, ex: 0, ez: 0 };
  for (let d = 0; d < 180; d += 3) { const a = d * Math.PI / 180, c = Math.cos(a), s2 = Math.sin(a); let x0 = 1e9, x1 = -1e9, z0 = 1e9, z1 = -1e9;
    for (const p of P) { const x = p.x * c - p.z * s2, z = p.x * s2 + p.z * c; x0 = Math.min(x0, x); x1 = Math.max(x1, x); z0 = Math.min(z0, z); z1 = Math.max(z1, z); }
    const cost = Math.max((x1 - x0) / (W / H), z1 - z0); if (cost < best.cost) best = { cost, a, ex: x1 - x0, ez: z1 - z0, cx: (x0 + x1) / 2, cz: (z0 + z1) / 2 }; }
  const wd = { scene, P, N, L, at, cars, glowLine, badges, size, fit: best, theme: T, cornerIdx, TG, NR, lightObjs, bldMesh, bldRanges };
  extendWorld(wd, tr, toV);
  if (HQ) hqWorld(wd, { sun, asphalt, runoff, ground, lines, kerbs }, tr);
  return wd;
}

function mergeGeos(geos) { // простое слияние BufferGeometry без индекса
  let total = 0; const parts = geos.map(g => { const ng = g.index ? g.toNonIndexed() : g; total += ng.attributes.position.count; return ng; });
  const pos = new Float32Array(total * 3), col = new Float32Array(total * 3); let o = 0;
  for (const g of parts) { pos.set(g.attributes.position.array, o * 3); col.set(g.attributes.color.array, o * 3); o += g.attributes.position.count; }
  const m = new THREE.BufferGeometry(); m.setAttribute('position', new THREE.BufferAttribute(pos, 3)); m.setAttribute('color', new THREE.BufferAttribute(col, 3)); m.computeVertexNormals(); return m;
}
function mergeGeosUV(geos) { // HQ: как mergeGeos, плюс uv (окна на стенах; крыши уходят в тёмный угол текстуры)
  let total = 0; const parts = geos.map(g => { const ng = g.index ? g.toNonIndexed() : g; total += ng.attributes.position.count; return ng; });
  const pos = new Float32Array(total * 3), col = new Float32Array(total * 3), uv = new Float32Array(total * 2); let o = 0;
  for (const g of parts) { pos.set(g.attributes.position.array, o * 3); col.set(g.attributes.color.array, o * 3); if (g.attributes.uv) uv.set(g.attributes.uv.array, o * 2); o += g.attributes.position.count; }
  const m = new THREE.BufferGeometry(); m.setAttribute('position', new THREE.BufferAttribute(pos, 3)); m.setAttribute('color', new THREE.BufferAttribute(col, 3)); m.computeVertexNormals();
  const nr = m.attributes.normal; for (let i = 0; i < total; i++) if (Math.abs(nr.getY(i)) > 0.6) { uv[i * 2] = 0.15; uv[i * 2 + 1] = 0.15; }
  m.setAttribute('uv', new THREE.BufferAttribute(uv, 2)); return m;
}

function badgeTex(text) {
  const c = document.createElement('canvas'); c.width = c.height = 128; const g = c.getContext('2d');
  g.fillStyle = '#0b0e14'; g.beginPath(); g.arc(64, 64, 56, 0, 7); g.fill(); g.lineWidth = 8; g.strokeStyle = '#ffffff'; g.stroke();
  g.fillStyle = '#fff'; g.font = '900 64px Inter'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(text, 64, 68);
  return new THREE.CanvasTexture(c);
}

// ---------- машинка (своя, без ливрей): обтекаемый корпус из капсул и профилей ----------
const ACCENT = { '#3b82f6': '#f8fafc', '#f97316': '#1f2937', '#f3f4f6': '#ef4444', '#22c55e': '#0f172a', '#a855f7': '#facc15', '#facc15': '#111827', '#ef4444': '#f8fafc', '#06b6d4': '#1e293b', '#ec4899': '#f8fafc', '#84cc16': '#1f2937' };
/* нативный брендинг LapRadar в 3D: логотип + надпись, как наклейка спонсора (на машинах, мотоциклах, щитах, арке) */
const _brandTex = {};
function brandTex(kind = 'light') {
  if (_brandTex[kind]) return _brandTex[kind];
  const c = document.createElement('canvas'); c.width = 512; c.height = 128; const g = c.getContext('2d');
  if (kind === 'board') { g.fillStyle = '#0b1020'; g.fillRect(0, 0, 512, 128); g.fillStyle = '#3478f6'; g.fillRect(0, 118, 512, 10); }
  g.save(); g.translate(18, 16); g.scale(3, 3); const R = new Path2D(); R.roundRect(0, 0, 32, 32, 7); g.fillStyle = '#3478f6'; g.fill(R);
  g.strokeStyle = '#fff'; g.lineWidth = 3.4; g.lineCap = 'round'; g.stroke(new Path2D('M7 25C7 15 13 9 25 7')); g.beginPath(); g.arc(15.6, 16.6, 2.5, 0, 7); g.fillStyle = '#fff'; g.fill(); g.restore();
  g.textBaseline = 'middle'; g.fillStyle = kind === 'dark' ? '#0b1020' : '#ffffff';
  let fs = 80; do { g.font = `italic 900 ${fs}px "Barlow Condensed", Inter, sans-serif`; fs -= 2; } while (g.measureText('LAPRADAR').width > 360 && fs > 30);
  g.fillText('LAPRADAR', 136, 68);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; return (_brandTex[kind] = t);
}
const brandMat = kind => new THREE.MeshBasicMaterial({ map: brandTex(kind), transparent: true, depthWrite: false, polygonOffset: true, polygonOffsetFactor: -2 });
function makeCar(color, tyreColor) {
  const g = new THREE.Group();
  const paint = new THREE.MeshStandardMaterial({ color, roughness: 0.35, metalness: 0.15 });
  const accent = new THREE.MeshStandardMaterial({ color: ACCENT[color] || '#f8fafc', roughness: 0.4, metalness: 0.1 });
  const carbon = new THREE.MeshStandardMaterial({ color: '#15171c', roughness: 0.55, metalness: 0.2 });
  const add = (geo, m, x, y, z, rx = 0, ry = 0, rz = 0, sx = 1, sy = 1, sz = 1) => { const o = new THREE.Mesh(geo, m); o.position.set(x, y, z); o.rotation.set(rx, ry, rz); o.scale.set(sx, sy, sz); g.add(o); return o; };
  // монокок и нос
  add(new THREE.CapsuleGeometry(0.42, 2.2, 6, 14), paint, 0, 0.5, 0.15, Math.PI / 2, 0, 0, 1, 1, 0.72);
  const nose = new THREE.CylinderGeometry(0.12, 0.38, 1.9, 14); add(nose, paint, 0, 0.42, 2.35, Math.PI / 2, 0, 0, 1, 1, 0.62);
  add(new THREE.CylinderGeometry(0.12, 0.13, 0.9, 10), accent, 0, 0.41, 2.9, Math.PI / 2, 0, 0, 1, 1, 0.6); // полоса на носу
  // понтоны и кожух двигателя
  for (const sx of [-1, 1]) add(new THREE.CapsuleGeometry(0.3, 1.35, 6, 12), paint, sx * 0.66, 0.42, -0.35, Math.PI / 2, 0, 0, 1.25, 1, 0.75);
  add(new THREE.CapsuleGeometry(0.34, 1.5, 6, 12), paint, 0, 0.72, -0.95, Math.PI / 2, 0, 0, 0.9, 1, 1.05);
  add(new THREE.BoxGeometry(0.05, 0.42, 1.5), accent, 0, 1.0, -1.3); // киль на кожухе
  add(new THREE.CylinderGeometry(0.2, 0.26, 0.42, 12), carbon, 0, 1.05, -0.35, 0, 0, 0, 1, 1, 1.2); // воздухозаборник
  add(new THREE.BoxGeometry(1.7, 0.06, 3.6), carbon, 0, 0.12, -0.2); // днище
  // кокпит, шлем, halo
  add(new THREE.SphereGeometry(0.25, 14, 10), new THREE.MeshStandardMaterial({ color: '#f8fafc', roughness: 0.3 }), 0, 0.98, 0.35);
  add(new THREE.BoxGeometry(0.4, 0.06, 0.12), carbon, 0, 1.0, 0.56); // визор
  /* halo: дуга перед шлемом (а не вокруг головы), две опоры сзади и центральная стойка к носу */
  add(new THREE.TorusGeometry(0.42, 0.04, 8, 24, Math.PI), carbon, 0, 1.18, 0.0, Math.PI / 2, 0, 0, 1, 1.9, 1); // дуга вытянута вперёд: опоры за шлемом, перед лицом — стойка
  for (const sx of [-1, 1]) add(new THREE.CylinderGeometry(0.04, 0.05, 0.4, 6), carbon, sx * 0.42, 0.98, 0.0);
  add(new THREE.CylinderGeometry(0.035, 0.045, 0.46, 6), carbon, 0, 0.99, 0.925, -0.58);
  // переднее крыло: два элемента и щитки
  add(new THREE.BoxGeometry(2.05, 0.05, 0.5), accent, 0, 0.18, 3.25, 0.12); const frontFlap = add(new THREE.BoxGeometry(1.9, 0.04, 0.32), paint, 0, 0.27, 3.05, 0.35);
  for (const sx of [-1, 1]) add(new THREE.BoxGeometry(0.04, 0.32, 0.62), carbon, sx * 1.03, 0.27, 3.2);
  // заднее крыло: основной элемент, закрылок, щитки
  add(new THREE.BoxGeometry(1.5, 0.05, 0.45), carbon, 0, 1.12, -2.25, -0.1); const rearFlap = add(new THREE.BoxGeometry(1.5, 0.05, 0.3), accent, 0, 1.3, -2.38, -0.5);
  for (const sx of [-1, 1]) add(new THREE.BoxGeometry(0.05, 0.75, 0.8), paint, sx * 0.77, 1.0, -2.3);
  add(new THREE.BoxGeometry(0.08, 0.5, 0.12), carbon, 0, 0.85, -2.15);
  // колёса: шина с скруглённым профилем, диск, цветная полоса состава
  const prof = []; for (let i = 0; i <= 8; i++) { const a = -Math.PI / 2 + i / 8 * Math.PI; prof.push(new THREE.Vector2(1 - 0.18 + Math.cos(a) * 0.18, Math.sin(a) * 0.5)); }
  prof.unshift(new THREE.Vector2(0.6, -0.5)); prof.push(new THREE.Vector2(0.6, 0.5));
  const tyreG = new THREE.LatheGeometry(prof, 22), rubber = new THREE.MeshStandardMaterial({ color: '#18191d', roughness: 0.85 }), band = new THREE.MeshBasicMaterial({ color: tyreColor }), rimM = new THREE.MeshStandardMaterial({ color: '#b7bdc7', metalness: 0.7, roughness: 0.3 });
  const wheels = [];
  for (const [x, z, r, w] of [[1.02, 1.85, 0.36, 0.38], [-1.02, 1.85, 0.36, 0.38], [1.02, -1.55, 0.4, 0.5], [-1.02, -1.55, 0.4, 0.5]]) {
    const wg = new THREE.Group();
    const t = new THREE.Mesh(tyreG, rubber); t.scale.set(r, w, r); t.rotation.z = Math.PI / 2; wg.add(t);
    const rim = new THREE.Mesh(new THREE.CylinderGeometry(r * 0.58, r * 0.58, w * 0.92, 16), rimM); rim.rotation.z = Math.PI / 2; wg.add(rim);
    const b2 = new THREE.Mesh(new THREE.TorusGeometry(r * 0.76, 0.03, 5, 22), band); b2.rotation.y = Math.PI / 2; b2.position.x = Math.sign(x) * (w / 2 + 0.004); wg.add(b2);
    wg.position.set(x, r, z); g.add(wg); wheels.push(wg);
    // подвеска
    add(new THREE.CylinderGeometry(0.025, 0.025, Math.abs(x) - 0.35, 5), carbon, x / 2, r + 0.05, z, 0, 0, Math.PI / 2);
  }
  // наклейки LapRadar: бока понтонов и внешние стороны щитков заднего крыла
  { const m = brandMat(['#f8fafc', '#ffffff', '#fde047', '#facc15'].includes(String(color).toLowerCase()) ? 'dark' : 'light');
    for (const sx of [-1, 1]) {
      const d = add(new THREE.PlaneGeometry(1.15, 0.29), m, sx * 1.04, 0.45, -0.35, 0, sx * Math.PI / 2); d.renderOrder = 2;
      const e = add(new THREE.PlaneGeometry(0.72, 0.18), m, sx * 0.80, 1.05, -2.3, 0, sx * Math.PI / 2); e.renderOrder = 2;
    }
    const rw = add(new THREE.PlaneGeometry(1.3, 0.32), brandMat('light'), 0, 1.0, -2.71, 0, Math.PI); rw.renderOrder = 2; /* сзади на заднем крыле: видно в камере «за машиной» */
  }
  g.scale.setScalar(1.15);
  return { group: g, wheels, rubber, band, frontFlap, rearFlap };
}

/* ================= КИРПИЧНЫЙ СТИЛЬ: машины из блоков со шпильками =================
   Включается только явно: shot.brick = true (все машины сцены — кирпичные болиды) или
   shot.brick = { classic: [0], c: ['#f472b6'] } (машина 0 — открытый кабриолет 1950-х, c — свои цвета по номерам машин).
   В студии stage: предмет { o: 'brick', kind: 'f1' | 'classic', c }. Только форма кубиков: никаких логотипов и фигурок.
   Модель — список блоков [x0, x1, y0, y1, z0, z1, цвет]: x и z в шпильках (0,24 м), y в пластинах (кирпич = 3 пластины). */
const BU = 0.24, BP = 0.096;
const BRICK_MODELS = {
  f1: (c, a) => [
    [-3, 3, 0, 1, -9, 12, '#1b1d22'],                                   // днище
    [-3, 3, 1, 4, -6, 3, c], [-1, 1, 1, 4, 3, 13, c], [-1, 1, 1, 2, 13, 14, a],   // понтоны, монокок, нос
    [-2, -1, 4, 6, -1, 3, c], [1, 2, 4, 6, -1, 3, c],                    // борта кокпита
    [-2, 2, 4, 5, -8, -1, c], [-1, 1, 4, 7, -9, 0, c], [-1, 1, 7, 9, -3, 0, '#1b1d22'],   // кожух двигателя, воздухозаборник
    [-5, 5, 0, 1, 12, 14, a], [-5, -4, 0, 3, 11, 14, '#1b1d22'], [4, 5, 0, 3, 11, 14, '#1b1d22'],   // переднее крыло
    [-1, 1, 4, 9, -10, -9, '#1b1d22'], [-4, 4, 9, 10, -11, -9, a], [-4, -3, 4, 10, -12, -8, c], [3, 4, 4, 10, -12, -8, c],   // заднее крыло
  ],
  classic: (c, a) => [
    [-4, 4, 0, 3, -11, 11, c], [-4, 4, 0, 2, 11, 12, '#d9dde3'], [-4, 4, 0, 2, -12, -11, '#d9dde3'],   // кузов и хромированные бамперы
    [-4, 4, 3, 6, 4, 11, c], [-4, 4, 3, 6, -11, -4, c], [-4, -3, 3, 6, -4, 4, c], [3, 4, 3, 6, -4, 4, c],   // капот, багажник, двери
    [-3, 3, 3, 4, -4, 4, '#f8fafc'], [-3, 3, 4, 7, 0, 2, '#f8fafc'], [-3, 3, 4, 8, -4, -2, '#f8fafc'],   // салон: пол и два дивана
    [-4, -3, 6, 9, -11, -6, c], [3, 4, 6, 9, -11, -6, c],                // плавники 50-х
    [-4, 4, 6, 7, 4, 5, '#d9dde3'],                                     // рамка лобового стекла
  ],
};
function brickGeometry(boxes) {
  const occ = new Set(), key = (x, y, z) => x + ',' + y + ',' + z, geos = [], col = new THREE.Color();
  for (const [x0, x1, y0, y1, z0, z1] of boxes) for (let x = x0; x < x1; x++) for (let y = y0; y < y1; y++) for (let z = z0; z < z1; z++) occ.add(key(x, y, z));
  const colored = (g, c) => { g = g.index ? g.toNonIndexed() : g; col.set(c); const a = []; for (let i = 0; i < g.attributes.position.count; i++) a.push(col.r, col.g, col.b); g.setAttribute('color', new THREE.Float32BufferAttribute(a, 3)); return g; };
  const gap = 0.012;
  boxes.forEach(([x0, x1, y0, y1, z0, z1, c], bi) => {
    for (let y = y0, course = 0; y < y1; course++) { const hh = Math.min(3, y1 - y), off = (course + bi) % 2 ? 2 : 0;   /* кирпичи 2×4 вразбежку по рядам */
      for (let z = z0 - off; z < z1; z += 4) for (let x = x0; x < x1; x += 2) {
        const za = Math.max(z, z0), zb = Math.min(z + 4, z1), xa = x, xb = Math.min(x + 2, x1); if (zb <= za) continue;
        const g = new THREE.BoxGeometry((xb - xa) * BU - gap, hh * BP - gap * 0.6, (zb - za) * BU - gap); g.translate((xa + xb) / 2 * BU, (y + hh / 2) * BP, (za + zb) / 2 * BU); geos.push(colored(g, c)); }
      y += hh; }
    for (let x = x0; x < x1; x++) for (let z = z0; z < z1; z++) if (!occ.has(key(x, y1, z))) {   /* шпилька там, где сверху пусто */
      const g = new THREE.CylinderGeometry(BU * 0.3, BU * 0.3, BU * 0.21, 10); g.translate((x + 0.5) * BU, y1 * BP + BU * 0.1, (z + 0.5) * BU); geos.push(colored(g, c)); }
  });
  return mergeGeos(geos);
}
const _brickGeo = {};
function makeBrickCar(kind = 'f1', color = '#3b82f6') {
  const g = new THREE.Group(), body = new THREE.Group(), classic = kind === 'classic'; g.add(body);
  const k = kind + color, acc = classic ? '#d9dde3' : (ACCENT[color] || '#f8fafc');
  const geo = _brickGeo[k] || (_brickGeo[k] = brickGeometry(BRICK_MODELS[classic ? 'classic' : 'f1'](color, acc)));
  body.add(new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.3, metalness: 0.02, emissive: new THREE.Color(color).multiplyScalar(0.2) })));
  body.position.y = classic ? 0.26 : 0.1;
  const dark = new THREE.MeshStandardMaterial({ color: '#141518', roughness: 0.8 }), hub = new THREE.MeshStandardMaterial({ color: classic ? '#e5e7eb' : '#9aa1ad', metalness: 0.6, roughness: 0.3 });
  const wheels = [], spots = classic ? [[0.9, 1.75, 0.36, 0.3], [-0.9, 1.75, 0.36, 0.3], [0.9, -1.6, 0.36, 0.3], [-0.9, -1.6, 0.36, 0.3]] : [[1.1, 1.85, 0.37, 0.4], [-1.1, 1.85, 0.37, 0.4], [1.1, -1.55, 0.41, 0.5], [-1.1, -1.55, 0.41, 0.5]];
  for (const [x, z, r, w] of spots) { const wg = new THREE.Group();
    const t = new THREE.Mesh(new THREE.CylinderGeometry(r, r, w, 20), dark); t.rotation.z = Math.PI / 2; wg.add(t);
    const h = new THREE.Mesh(new THREE.CylinderGeometry(r * 0.55, r * 0.55, w + 0.02, 12), hub); h.rotation.z = Math.PI / 2; wg.add(h);
    if (classic) { const ww = new THREE.Mesh(new THREE.TorusGeometry(r * 0.78, r * 0.09, 6, 22), new THREE.MeshStandardMaterial({ color: '#f8fafc', roughness: 0.5 })); ww.rotation.y = Math.PI / 2; ww.position.x = Math.sign(x) * (w / 2 + 0.005); wg.add(ww); }
    for (let s = 0; s < 4; s++) { const st = new THREE.Mesh(new THREE.BoxGeometry(w + 0.04, r * 0.18, r * 0.18), dark); st.rotation.x = s * Math.PI / 4; wg.add(st); }   /* «кубики» на диске: видно, что колесо крутится */
    wg.position.set(x, r, z); g.add(wg); wheels.push(wg); }
  if (classic) {
    const glass = new THREE.Mesh(new THREE.BoxGeometry(8 * BU - 0.1, 4 * BP * 1.6, 0.05), new THREE.MeshStandardMaterial({ color: '#bfe3ff', transparent: true, opacity: 0.35, roughness: 0.05 }));
    glass.position.set(0, 0.26 + 7 * BP + 3.2 * BP, 4.5 * BU); glass.rotation.x = -0.25; g.add(glass);
    const wheel = new THREE.Mesh(new THREE.TorusGeometry(0.17, 0.025, 6, 18), dark); wheel.position.set(-1.6 * BU, 0.26 + 7.6 * BP, 2.6 * BU); wheel.rotation.x = -0.9; g.add(wheel);
    for (const sx of [-1, 1]) { const hl = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.16, 0.04), new THREE.MeshBasicMaterial({ color: '#fff6d8' })); hl.position.set(sx * 2.8 * BU, 0.26 + 4.5 * BP, 12 * BU + 0.02); g.add(hl);
      const tl = new THREE.Mesh(new THREE.BoxGeometry(0.14, 0.2, 0.04), new THREE.MeshBasicMaterial({ color: '#ff2a3d' })); tl.position.set(sx * 3.5 * BU, 0.26 + 7.5 * BP, -11 * BU - 0.02); g.add(tl); }
  } else {
    const hm = new THREE.Mesh(new THREE.CylinderGeometry(BU * 0.95, BU * 0.95, 3 * BP, 16), new THREE.MeshStandardMaterial({ color: acc, roughness: 0.3 })); hm.position.set(0, 0.1 + 5.5 * BP, 1.2 * BU); g.add(hm);   /* круглый кубик 2×2 вместо шлема */
    const st = new THREE.Mesh(new THREE.CylinderGeometry(BU * 0.3, BU * 0.3, BU * 0.21, 10), hm.material); st.position.set(0, 0.1 + 7 * BP + BU * 0.1, 1.2 * BU); g.add(st);
  }
  g.scale.setScalar(classic ? 1.0 : 1.15);
  return { group: g, wheels, kind };
}
/* своя окраска машин сцены (по умолчанию выключено): shot.paint = { 0: '#16181d' } или { 0: { c: '#16181d', a: '#c0c6cf', p: 'stripe' } }
   (p: stripe | fade | split | band). Только цвета и простой узор: без логотипов и настоящих ливрей. Машина-двойник создаётся один раз и кешируется. */
const paintOf = (shot, k) => { const v = shot?.paint?.[k]; if (!v) return null; const o = typeof v === 'string' ? { c: v } : v; return { ...o, id: [o.c, o.a, o.p].join('|') }; };
const CAR_KEYS = ['group', 'wheels', 'rubber', 'band', 'frontFlap', 'rearFlap', 'helmet', 'rain', 'hq'];
function applyPaint(w, shot, c, k) {
  const pt = paintOf(shot, k), id = pt ? pt.id : '';
  if ((c.paintId || '') === id) return;
  if (!c.base) { c.base = {}; CAR_KEYS.forEach(f => { c.base[f] = c[f]; }); }
  c.alts = c.alts || {};
  let src = c.base;
  if (pt) { src = c.alts[id]; if (!src) { const m = (HQ ? makeCarHQ : makeCar)(pt.c, '#' + c.base.band.color.getHexString(), k, pt); w.scene.add(m.group); src = c.alts[id] = {}; CAR_KEYS.forEach(f => { src[f] = m[f]; }); } }
  c.group.visible = false; CAR_KEYS.forEach(f => { c[f] = src[f]; }); c.paintId = id;
}
const brickOf = (shot, k) => { const b = shot?.brick; if (!b) return null; return { kind: (b.classic || []).includes(k) ? 'classic' : 'f1', c: b.c?.[k] }; };

/* ================= НОЧНОЙ ВЕГАС: светящаяся Sphere и огни на фасадах (shot.sphere, shot.neon; по умолчанию выключено) ================= */
function sphereTex() {
  const c = document.createElement('canvas'); c.width = 1024; c.height = 512; const g = c.getContext('2d');
  const gr = g.createLinearGradient(0, 0, 0, 512); gr.addColorStop(0, '#1d1b6b'); gr.addColorStop(0.35, '#7b2ff7'); gr.addColorStop(0.55, '#ff3d9a'); gr.addColorStop(0.75, '#ffb03a'); gr.addColorStop(1, '#2a1250');
  g.fillStyle = gr; g.fillRect(0, 0, 1024, 512);
  for (let i = 0; i < 9; i++) { g.globalAlpha = 0.18; g.fillStyle = i % 2 ? '#4de1ff' : '#ffffff'; g.beginPath(); g.ellipse(i * 120 + 40, 180 + 60 * Math.sin(i), 160, 40, 0.3 * Math.sin(i * 2), 0, 7); g.fill(); }
  g.globalAlpha = 1; g.fillStyle = 'rgba(0,0,0,0.16)'; for (let y = 0; y < 512; y += 4) g.fillRect(0, y + 3, 1024, 1); for (let x = 0; x < 1024; x += 4) g.fillRect(x + 3, 0, 1, 512);   /* мелкая сетка светодиодов */
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.wrapS = THREE.RepeatWrapping; t.anisotropy = 4; return t;
}
function vegasExtras(w, shot, lt) {
  const want = !!shot.sphere || !!shot.neon;
  if (want && !w.vx) {
    const vx = w.vx = { sphere: null, neon: null };
    /* Sphere: самое большое круглое высокое здание из карты */
    let best = null; for (const r of w.bldRanges || []) { if (r.h < 70 || r.pts.length < 12) continue; const cx = r.pts.reduce((a, p) => a + p.x, 0) / r.pts.length, cy = r.pts.reduce((a, p) => a + p.y, 0) / r.pts.length;
      const ds = r.pts.map(p => Math.hypot(p.x - cx, p.y - cy)), m = ds.reduce((a, b) => a + b, 0) / ds.length; if (m > 50 && (Math.max(...ds) - Math.min(...ds)) / m < 0.15 && (!best || m > best.m)) best = { r, cx, cy, m }; }
    if (best) { const R = Math.min(best.m * 0.92, best.r.h * 0.7), mat = new THREE.MeshBasicMaterial({ map: sphereTex(), fog: false });
      const s = new THREE.Mesh(new THREE.SphereGeometry(R, 64, 40), mat); s.position.set(best.cx, best.r.h - R - 0.3, -best.cy); w.scene.add(s);
      const halo = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowTex('rgba(255,90,190,0.9)', 'rgba(120,60,255,0)'), transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false })); halo.scale.set(R * 4.2, R * 4.2, 1); halo.position.copy(s.position); w.scene.add(halo);
      vx.sphere = { s, halo, r: best.r, R }; }
    /* огни на фасадах: вертикальные неоновые полосы и точки на углах высоких зданий рядом с трассой */
    const R6 = rng(41), bars = [], cols = ['#ff3d9a', '#4de1ff', '#ffd23f', '#a855f7', '#ff7a1a', '#f8fafc'];
    for (const r of w.bldRanges || []) { if (r.h < 25 || r === best?.r) continue; const p0 = r.pts[0]; let near = 1e9; for (let i = 0; i < w.N; i += 6) near = Math.min(near, Math.hypot(w.P[i].x - p0.x, w.P[i].z + p0.y)); if (near > 450) continue;
      const n = Math.min(4, 1 + Math.floor(r.h / 40)); for (let j = 0; j < n; j++) { const p = r.pts[Math.floor(R6() * r.pts.length)]; bars.push({ x: p.x, z: -p.y, h: r.h * (0.55 + R6() * 0.4), c: cols[Math.floor(R6() * cols.length)] }); } }
    if (bars.length) { const im = new THREE.InstancedMesh(new THREE.BoxGeometry(1.6, 1, 1.6), new THREE.MeshBasicMaterial({ fog: false }), bars.length), m4 = new THREE.Matrix4(), cc = new THREE.Color();
      bars.forEach((b, k) => { m4.makeScale(1, b.h, 1).setPosition(b.x, b.h / 2 - 0.3, b.z); im.setMatrixAt(k, m4); im.setColorAt(k, cc.set(b.c)); });
      const pos = [], pc = []; bars.forEach(b => { for (let y = 8; y < b.h; y += 14) { pos.push(b.x, y, b.z); cc.set(b.c); pc.push(cc.r, cc.g, cc.b); } });
      const pg = new THREE.BufferGeometry(); pg.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); pg.setAttribute('color', new THREE.Float32BufferAttribute(pc, 3));
      const pts = new THREE.Points(pg, new THREE.PointsMaterial({ size: 22, map: glowTex(), vertexColors: true, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false }));
      w.scene.add(im, pts); vx.neon = [im, pts]; }
  }
  const vx = w.vx; if (!vx) return;
  if (vx.sphere) { const on = !!shot.sphere; vx.sphere.s.visible = vx.sphere.halo.visible = on; if (on) { vx.sphere.s.material.map.offset.x = lt * 0.012; vx.sphere.halo.material.opacity = 0.55 + 0.1 * Math.sin(lt * 1.3); }
    /* здание-цилиндр из карты на месте Sphere прячем, пока она светится */
    const pa = w.bldMesh.geometry.attributes.position, r = vx.sphere.r; if (vx.sphere.hidden !== on) { if (!vx.sphere.y0) { vx.sphere.y0 = new Float32Array(r.count); for (let i = 0; i < r.count; i++) vx.sphere.y0[i] = pa.getY(r.start + i); }
      for (let i = 0; i < r.count; i++) pa.setY(r.start + i, on ? -40 : vx.sphere.y0[i]); pa.needsUpdate = true; vx.sphere.hidden = on; } }
  if (vx.neon) vx.neon.forEach(o => o.visible = !!shot.neon);
}

/* ================= НЕОНОВЫЙ КУБОК-«V» (stage: { o: 'vtrophy' }; трасса: shot.trophy; по умолчанию выключено) =================
   Своя модель по описанию кубка Гран-при Лас-Вегаса 2026: V-силуэт, хромированная рамка, красные диагональные полосы сверху,
   ряды тёплых ламп снизу и красный светящийся контур. Без логотипов и надписей настоящего кубка. */
function makeNeonTrophy(o = {}) {
  const root = new THREE.Group(), g = new THREE.Group(); root.add(g);
  const chrome = new THREE.MeshStandardMaterial({ color: '#d7dce4', roughness: 0.12, metalness: 1.0, emissive: '#1a1d24' });
  const dark = new THREE.MeshStandardMaterial({ color: '#0c0e14', roughness: 0.5, metalness: 0.4 });
  const red = o.c || '#ff2a3d', warm = o.bulb || '#ffd9a0';
  const tube = new THREE.MeshBasicMaterial({ color: red }), bulbM = new THREE.MeshBasicMaterial({ color: warm }), stripeM = new THREE.MeshBasicMaterial({ color: red, transparent: true, opacity: 0.92 });
  const H = 3.2, ang = 0.36, aw = 0.62, ad = 0.34, glowS = [], bulbs = [];
  /* основание: тёмный блок с хромированной кромкой */
  const base = new THREE.Mesh(new THREE.BoxGeometry(1.5, 0.5, 1.0), dark); base.position.y = 0.25; g.add(base);
  const lip = new THREE.Mesh(new THREE.BoxGeometry(1.56, 0.06, 1.06), chrome); lip.position.y = 0.5; g.add(lip);
  const foot = new THREE.Mesh(new THREE.BoxGeometry(0.42, 0.3, 0.42), chrome); foot.position.y = 0.66; g.add(foot);
  const gT = glowTex('rgba(255,60,80,0.9)', 'rgba(255,40,60,0)'), gW = glowTex('rgba(255,225,170,1)', 'rgba(255,200,120,0)');
  for (const sd of [-1, 1]) {
    const arm = new THREE.Group(); arm.position.set(0, 0.78, 0); arm.rotation.z = -sd * ang; g.add(arm);
    /* рамка плеча: хромированные края, тёмная лицевая панель */
    const panel = new THREE.Mesh(new THREE.BoxGeometry(aw, H, ad * 0.6), dark); panel.position.set(0, H / 2, 0); arm.add(panel);
    for (const ex of [-1, 1]) { const rail = new THREE.Mesh(new THREE.BoxGeometry(0.06, H, ad), chrome); rail.position.set(ex * aw / 2, H / 2, 0); arm.add(rail); }
    const cap = new THREE.Mesh(new THREE.BoxGeometry(aw + 0.06, 0.07, ad), chrome); cap.position.set(0, H, 0); arm.add(cap);
    /* красный контур по периметру плеча (неоновая трубка) */
    for (const zf of [1, -1]) {
      for (const ex of [-1, 1]) { const t = new THREE.Mesh(new THREE.CylinderGeometry(0.022, 0.022, H, 6), tube); t.position.set(ex * (aw / 2 - 0.05), H / 2, zf * ad * 0.31); arm.add(t); }
      const tt = new THREE.Mesh(new THREE.CylinderGeometry(0.022, 0.022, aw - 0.1, 6), tube); tt.rotation.z = Math.PI / 2; tt.position.set(0, H - 0.06, zf * ad * 0.31); arm.add(tt);
      /* верхняя половина: диагональные красные полосы */
      for (let k = 0; k < 6; k++) { const s = new THREE.Mesh(new THREE.PlaneGeometry(0.075, aw * 1.25), stripeM); s.rotation.z = 0.75 * sd; s.position.set(0, H * 0.56 + k * H * 0.072, zf * (ad * 0.31 + 0.004)); if (zf < 0) s.rotation.y = Math.PI;
        s.scale.y = 0.62; arm.add(s); }
      /* нижняя половина: ряды тёплых ламп, сходятся к острию V */
      for (let r = 0; r < 6; r++) for (const bx of [-0.15, 0, 0.15]) { const b = new THREE.Mesh(new THREE.SphereGeometry(0.045, 8, 6), bulbM); b.position.set(bx, 0.22 + r * H * 0.075, zf * (ad * 0.31 + 0.02)); arm.add(b); bulbs.push(b); }
    }
    for (let k = 0; k < 7; k++) { const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: k < 4 ? gT : gW, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false }));
      sp.position.set(0, k < 4 ? H * (0.6 + k * 0.12) : 0.3 + (k - 4) * 0.38, ad * 0.4); sp.scale.setScalar(k < 4 ? 1.1 : 0.8); arm.add(sp); glowS.push(sp); }
  }
  const halo = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowTex('rgba(255,70,110,0.55)', 'rgba(140,40,255,0)'), transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false }));
  halo.position.set(0, 2.4, -0.2); halo.scale.setScalar(6.5); g.add(halo); glowS.push(halo);
  root.userData.vt = { glowS, bulbs, bulbM, halo };
  return root;
}
/* мерцание ламп как у старой вывески: бегущая волна вверх по рядам */
function animNeonTrophy(obj, lt) { const v = obj?.userData?.vt; if (!v) return;
  v.bulbs.forEach((b, i) => { const r = Math.floor((i % 18) / 3), on = 0.55 + 0.45 * Math.max(0, Math.sin(lt * 5 - r * 0.9)); b.scale.setScalar(0.8 + 0.35 * on); });
  v.glowS.forEach((s, k) => { s.material.opacity = 0.75 + 0.25 * Math.sin(lt * 3.1 + k); }); v.halo.material.opacity = 0.55 + 0.12 * Math.sin(lt * 1.7); }
/* кубок на трассе: shot.trophy = { at (доля круга), side (м от оси трассы), s (масштаб), y, spin } */
function trackTrophy(w, shot, lt) {
  const o = shot.trophy; if (!o && !w.vtr) return;
  if (o && !w.vtr) { w.vtr = makeNeonTrophy(o); w.scene.add(w.vtr); }
  w.vtr.visible = !!o; if (!o) return;
  const a = w.at((o.at ?? 0.38) * w.L); w.vtr.position.copy(a.p).addScaledVector(a.n, o.side ?? 34).setY(a.p.y + (o.y ?? 0));
  w.vtr.scale.setScalar(o.s ?? 8); w.vtr.rotation.y = Math.atan2(a.n.x, a.n.z) + Math.PI + (o.ry ?? 0) + (o.spin ?? 0) * lt; animNeonTrophy(w.vtr, lt);
}

/* ================= ДОЖДЬ (shot.rain: true | { k: сила 0–1, spray: false }; по умолчанию выключено) =================
   Струи дождя вокруг камеры, мокрый блеск асфальта, водяной шлейф за машинами, туман ближе. Всё — функция времени кадра. */
function rainFx(w, shot, lt, cam) {
  const on = !!shot.rain, o = typeof shot.rain === 'object' ? shot.rain : {}, k = o.k ?? 1;
  if (on && !w.rain) {
    const n = 2600, pos = new Float32Array(n * 6), g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    const lines = new THREE.LineSegments(g, new THREE.LineBasicMaterial({ color: '#b9cdf5', transparent: true, opacity: 0.38, depthWrite: false, blending: THREE.AdditiveBlending, fog: false }));
    lines.frustumCulled = false; w.scene.add(lines);
    const sp = [], ix = []; for (let i = 0; i <= w.N; i++) { const q = w.P[i % w.N], nn = w.NR[i % w.N]; sp.push(q.x - nn.x * 6.6, q.y + 0.045, q.z - nn.z * 6.6, q.x + nn.x * 6.6, q.y + 0.045, q.z + nn.z * 6.6); }
    for (let i = 0; i < w.N; i++) { const a = i * 2; ix.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
    const wg = new THREE.BufferGeometry(); wg.setAttribute('position', new THREE.Float32BufferAttribute(sp, 3)); wg.setIndex(ix);
    const sheen = new THREE.Mesh(wg, new THREE.MeshBasicMaterial({ color: '#6f86c8', transparent: true, opacity: 0.16, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide }));
    w.scene.add(sheen); w.rain = { lines, n, sheen };
  }
  const R = w.rain; if (!R) return; R.lines.visible = R.sheen.visible = on; if (!on) return;
  /* капли: коробка 70×40×70 м вокруг камеры, каждая падает со своей фазой; координаты привязаны к сетке, чтобы при движении камеры не «плыли» */
  const pa = R.lines.geometry.attributes.position.array, BX = 70, BY = 40, cx = cam.position.x, cy = cam.position.y, cz = cam.position.z, len = 1.6, vy = 22, slant = 0.18, m = Math.floor(R.n * k);
  for (let i = 0; i < R.n; i++) { const j = i * 6; if (i >= m) { pa.fill(0, j, j + 6); continue; }
    const hx = hashK(i), hz = hashK(i + 7001), hy = hashK(i + 3301);
    const x = cx + (((hx * BX - cx) % BX) + BX) % BX - BX / 2, z = cz + (((hz * BX - cz) % BX) + BX) % BX - BX / 2;
    const y = cy - BY / 2 + ((((hy * BY - lt * vy) % BY) + BY) % BY);
    pa[j] = x; pa[j + 1] = y; pa[j + 2] = z; pa[j + 3] = x + slant * len; pa[j + 4] = y - len; pa[j + 5] = z; }
  R.lines.geometry.attributes.position.needsUpdate = true;
  R.sheen.material.opacity = 0.12 + 0.05 * Math.sin(lt * 0.7);
}
/* водяная пыль за машинами: до fxEnd, из того же пула, что дым */
function rainSpray(w, shot, lt) {
  const o = typeof shot.rain === 'object' ? shot.rain : {}, k = o.k ?? 1; if (!shot.rain || o.spray === false) return;
  for (const c of w.cars) { const st = c.st; if (!st?.vis) continue; const hd = st.dir.clone().addScaledVector(st.n, st.yaw || 0).normalize(), right = new THREE.Vector3(-hd.z, 0, hd.x);
    for (let q = 0; q < 9; q++) { const u = ((lt * 2.4 + q / 9) % 1); for (const sd of [0.85, -0.85]) puff(st.pos.clone().addScaledVector(hd, -2.2 - u * 11).addScaledVector(right, sd * (1 + u * 0.9)).setY(st.pos.y + 0.35 + u * 1.5), 0.9 + u * 3.2, 0.42 * (1 - u) * k); } }
}

// ---------- студия шин ----------
function makeTyre(color, r = 1) {
  const g = new THREE.Group();
  const prof = []; const R = 1 * r, w = 0.62 * r, rr = 0.2 * r;
  for (let i = 0; i <= 10; i++) { const a = -Math.PI / 2 + i / 10 * Math.PI; prof.push(new THREE.Vector2(R - rr + Math.cos(a) * rr, Math.sin(a) * (w / 2))); }
  prof.unshift(new THREE.Vector2(0.62 * r, -w / 2)); prof.push(new THREE.Vector2(0.62 * r, w / 2));
  const rub = new THREE.Mesh(new THREE.LatheGeometry(prof, 48), new THREE.MeshStandardMaterial({ color: '#1b1c20', roughness: 0.75 })); rub.rotation.x = Math.PI / 2; g.add(rub);
  for (const s of [-1, 1]) { const b = new THREE.Mesh(new THREE.TorusGeometry(0.8 * r, 0.04 * r, 8, 64), new THREE.MeshBasicMaterial({ color })); b.position.z = s * (w / 2 + 0.005); g.add(b); }
  const rim = new THREE.Mesh(new THREE.CylinderGeometry(0.62 * r, 0.62 * r, w * 0.9, 32), new THREE.MeshStandardMaterial({ color: '#9aa1ad', metalness: 0.6, roughness: 0.35 })); rim.rotation.x = Math.PI / 2; g.add(rim);
  for (let i = 0; i < 5; i++) { const sp = new THREE.Mesh(new THREE.BoxGeometry(0.1 * r, 0.6 * r, 0.05), new THREE.MeshStandardMaterial({ color: '#2a2d33' })); sp.rotation.z = i / 5 * Math.PI * 2; sp.position.z = w * 0.46; sp.translateY(0.25 * r); g.add(sp); }
  return g;
}
function buildStage() {
  const scene = new THREE.Scene(); scene.background = gradTex([[0, '#0b1020'], [0.6, '#141c34'], [1, '#05060c']]);
  scene.add(new THREE.HemisphereLight(0x9fb4ff, 0x101018, 0.9));
  const key = new THREE.DirectionalLight(0xffffff, 2.2); key.position.set(3, 5, 6); scene.add(key);
  const rim = new THREE.DirectionalLight(0x5b8cff, 1.8); rim.position.set(-5, 2, -4); scene.add(rim);
  const floor = new THREE.Mesh(new THREE.CircleGeometry(9, 48), new THREE.MeshStandardMaterial({ color: '#0e1322', roughness: 0.4, metalness: 0.2 })); floor.rotation.x = -Math.PI / 2; floor.position.y = -1.05; scene.add(floor);
  const tyres = [makeTyre(TYRE.soft), makeTyre(TYRE.medium), makeTyre(TYRE.hard)]; tyres.forEach(t => scene.add(t));
  const cam = new THREE.PerspectiveCamera(35, W / H, 0.1, 100); cam.aspect = W / H;
  const bits = Array.from({ length: 30 }, () => { const m = new THREE.Mesh(new THREE.SphereGeometry(0.035, 6, 5), new THREE.MeshStandardMaterial({ color: '#111216', roughness: 0.9 })); m.visible = false; scene.add(m); return m; });
  return { scene, tyres, cam, bits };
}


/* ================= СЦЕНЫ ВНЕ ТРАССЫ: студия с машинами, кубком, пьедесталом, конфетти =================
   shot = { type: 'stage', items: [{ o: 'f1'|'stock'|'bike'|'trophy'|'podium', c: цвет, n: номер, x, z, ry, s }], bg: 'blue'|'gold'|'red',
            r, r2, h, h2, a0, a1, ly (высота взгляда), fov, spin (вращение подиума), confetti: true, beams: true } */
let STG = null;
function buildStage2() {
  const scene = new THREE.Scene(); scene.fog = new THREE.Fog('#05070f', 30, 70);
  scene.add(new THREE.HemisphereLight(0xb8c6ff, 0x141018, 1.0));
  const key = new THREE.DirectionalLight(0xffffff, 2.4); key.position.set(6, 10, 8); scene.add(key);
  const rim = new THREE.DirectionalLight(0x6f9bff, 2.0); rim.position.set(-8, 4, -6); scene.add(rim);
  const floor = new THREE.Mesh(new THREE.CircleGeometry(60, 64), new THREE.MeshStandardMaterial({ color: '#0d1120', roughness: 0.35, metalness: 0.3 })); floor.rotation.x = -Math.PI / 2; scene.add(floor);
  const turn = new THREE.Group(); scene.add(turn);
  const disc = new THREE.Mesh(new THREE.CylinderGeometry(7.5, 7.8, 0.3, 64), new THREE.MeshStandardMaterial({ color: '#1a2140', roughness: 0.3, metalness: 0.5 })); disc.position.y = 0.15; turn.add(disc);
  const ring = new THREE.Mesh(new THREE.TorusGeometry(7.65, 0.07, 6, 96), new THREE.MeshBasicMaterial({ color: '#5b9bff' })); ring.rotation.x = Math.PI / 2; ring.position.y = 0.31; turn.add(ring);
  const beams = [-1, 0, 1].map(k => { const m = new THREE.Mesh(new THREE.ConeGeometry(3.2, 26, 32, 1, true), new THREE.MeshBasicMaterial({ color: '#9fc0ff', transparent: true, opacity: 0.07, side: THREE.DoubleSide, depthWrite: false, blending: THREE.AdditiveBlending }));
    m.position.set(k * 5, 13, -3 + Math.abs(k) * 2); m.rotation.z = -k * 0.18; scene.add(m); return m; });
  const conf = []; const cols = ['#facc15', '#ef4444', '#3b82f6', '#22c55e', '#f3f4f6', '#f97316', '#ec4899'];
  for (let i = 0; i < 220; i++) { const m = new THREE.Mesh(new THREE.PlaneGeometry(0.16, 0.26), new THREE.MeshBasicMaterial({ color: cols[i % cols.length], side: THREE.DoubleSide })); m.visible = false; scene.add(m); conf.push(m); }
  const cam = new THREE.PerspectiveCamera(40, W / H, 0.1, 400);
  return { scene, turn, beams, conf, cam, cache: {}, cur: null };
}
function makeTrophy(color = '#f5c542') {
  const g = new THREE.Group(), gold = new THREE.MeshStandardMaterial({ color, roughness: 0.18, metalness: 0.95, emissive: '#3a2a05' });
  const prof = [[0, 0], [0.9, 0], [0.9, 0.25], [0.55, 0.35], [0.5, 0.75], [0.18, 0.95], [0.16, 1.5], [0.35, 1.7], [0.95, 2.1], [1.15, 2.9], [1.2, 3.35], [1.1, 3.4], [0.95, 2.95], [0.75, 2.3], [0, 2.15]].map(([x, y]) => new THREE.Vector2(x, y));
  g.add(new THREE.Mesh(new THREE.LatheGeometry(prof, 48), gold));
  for (const sd of [-1, 1]) { const h = new THREE.Mesh(new THREE.TorusGeometry(0.45, 0.07, 8, 24, Math.PI * 1.2), gold); h.position.set(sd * 1.2, 2.75, 0); h.rotation.z = sd > 0 ? -Math.PI / 2 - 0.6 : Math.PI / 2 + 0.6 - Math.PI * 1.2 + Math.PI; g.add(h); }
  const base = new THREE.Mesh(new THREE.CylinderGeometry(1.0, 1.15, 0.6, 32), new THREE.MeshStandardMaterial({ color: '#15171c', roughness: 0.4 })); base.position.y = -0.3; g.add(base);
  g.position.y = 0.6; const root = new THREE.Group(); root.add(g); return root;
}
function makePodium() {
  const g = new THREE.Group(), m = new THREE.MeshStandardMaterial({ color: '#e8ecf4', roughness: 0.5 });
  [[0, 2.2, '1'], [-3.1, 1.5, '2'], [3.1, 1.0, '3']].forEach(([x, h, t]) => { const b = new THREE.Mesh(new THREE.BoxGeometry(3, h, 2.6), m); b.position.set(x, h / 2, 0); g.add(b);
    const f = new THREE.Mesh(new THREE.PlaneGeometry(1.4, 1.4), new THREE.MeshBasicMaterial({ map: numTex(t, '#ffffff', '#1d4ed8'), transparent: true })); f.position.set(x, h / 2, 1.31); g.add(f); });
  return g;
}
function stageItem(it) {
  if (it.o === 'f1') { const c = HQ ? makeCarHQ(it.c || '#3b82f6', TYRE.soft, 0, { a: it.a, p: it.p }) : makeCar(it.c || '#3b82f6'); return c.group; }
  if (it.o === 'stock') { const c = makeStock(it.c || '#facc15', it.n); c.group.visible = true; return c.group; }
  if (it.o === 'bike') { const c = makeBike(it.c || '#ef4444'); c.group.visible = true; c.lean.rotation.z = it.lean ?? 0; return c.group; }
  if (it.o === 'brick') return makeBrickCar(it.kind || 'f1', it.c || '#3b82f6').group;
  if (it.o === 'trophy') return makeTrophy(it.c);
  if (it.o === 'vtrophy') return makeNeonTrophy(it);
  if (it.o === 'podium') return makePodium();
  return new THREE.Group();
}
const STAGE_BG = { blue: [[0, '#070b1a'], [0.6, '#122046'], [1, '#04050b']], gold: [[0, '#140d02'], [0.6, '#3a2a0a'], [1, '#050402']], red: [[0, '#160406'], [0.6, '#40101a'], [1, '#060203']] };
function renderStage(shot, u, lt, T) {
  if (!STG) STG = buildStage2(); const s = STG, key = JSON.stringify(shot.items || []);
  if (!s.cache[key]) { const g = new THREE.Group(); (shot.items || []).forEach(it => { const o = stageItem(it); o.position.set(it.x ?? 0, (it.y ?? 0) + 0.3, it.z ?? 0); o.rotation.y = it.ry ?? 0; o.scale.multiplyScalar(it.s ?? 1); o.userData.s0 = o.scale.x; g.add(o); }); s.cache[key] = g; }
  if (s.cur !== s.cache[key]) { if (s.cur) s.turn.remove(s.cur); s.cur = s.cache[key]; s.turn.add(s.cur); }
  const bgk = shot.bg || 'blue'; if (s.bg !== bgk) { s.scene.background = gradTex(STAGE_BG[bgk] || STAGE_BG.blue); s.bg = bgk; }
  s.cur.children.forEach(o => animNeonTrophy(o, lt));
  s.cur.children.forEach((o, k) => { const p = back((lt - 0.15 - k * 0.22) / 0.55); o.scale.setScalar(Math.max(0.001, o.userData.s0 * p)); });
  s.turn.rotation.y = (shot.rot0 ?? 0) + (shot.spin ?? 0.25) * lt;
  s.beams.forEach((b, k) => { b.visible = shot.beams !== false; b.material.opacity = 0.05 + 0.03 * Math.sin(lt * 2 + k * 2); });
  s.conf.forEach((m, i) => { m.visible = !!shot.confetti; if (!m.visible) return; const h1 = hashK(i), h2 = hashK(i + 50), h3 = hashK(i + 99), t = lt * (0.8 + h3 * 0.5) + h2 * 6;
    m.position.set((h1 - 0.5) * 18 + Math.sin(t * 1.3 + i) * 0.6, 14 - (t * 2.6 % 15), (h2 - 0.5) * 12 + Math.cos(t + i) * 0.5); m.rotation.set(t * 3 + i, t * 2.2, t * 1.7); });
  const a = lerp(shot.a0 ?? -0.5, shot.a1 ?? 0.3, ease(u)), r = lerp(shot.r ?? 11, shot.r2 ?? shot.r ?? 11, ease(u)) * (W < H ? (shot.pk ?? 1.8) : 1), h = lerp(shot.h ?? 2.6, shot.h2 ?? shot.h ?? 2.6, ease(u));
  s.cam.aspect = W / H; s.cam.fov = shot.fov ?? 40; s.cam.position.set(Math.sin(a) * r, h, Math.cos(a) * r); s.cam.lookAt(0, shot.ly ?? 1.2, 0); s.cam.updateProjectionMatrix();
  if (HQ && !s.scene.environment) { s.scene.environment = hqEnv('night'); s.scene.environmentIntensity = 0.35; s.hq = true; }
  draw(s.scene, s.cam);
}

/* ================= ОВАЛ (NASCAR): трава внутри, стена SAFER, трибуны по всей внешней стороне ================= */
function ovalScenery(w) {
  const { P, N, NR, scene } = w, c = P.reduce((a, p) => a.add(p), new THREE.Vector3()).multiplyScalar(1 / N);
  const inS = Math.sign(NR[0].clone().dot(c.clone().sub(P[0]))) || 1; /* где внутренняя сторона */
  const inner = P.filter((_, i) => i % 3 === 0).map((p, j) => { const i = j * 3; return new THREE.Vector2(p.x + NR[i].x * inS * 26, -(p.z + NR[i].z * inS * 26)); });
  const gg = new THREE.ShapeGeometry(new THREE.Shape(inner)); gg.rotateX(-Math.PI / 2);
  const grass = new THREE.Mesh(gg, new THREE.MeshLambertMaterial({ color: '#5f9a45' })); grass.position.y = -0.6; scene.add(grass);
  /* полосы скошенной травы */
  for (let k = 1; k < 6; k++) { const sh = inner.map(v => new THREE.Vector2(c.x + (v.x - c.x) * (1 - k * 0.14), -c.z + (v.y + c.z) * (1 - k * 0.14))); const g2 = new THREE.ShapeGeometry(new THREE.Shape(sh)); g2.rotateX(-Math.PI / 2);
    const m = new THREE.Mesh(g2, new THREE.MeshLambertMaterial({ color: k % 2 ? '#6aa74e' : '#5f9a45' })); m.position.y = -0.58 + k * 0.01; scene.add(m); }
  const wall = (off, hgt, color, step = 2) => { const pos = [], idx = []; for (let i = 0; i <= N; i += step) { const k = i % N, p = P[k], n = NR[k], x = p.x + n.x * off, z = p.z + n.z * off; pos.push(x, p.y - 0.3, z, x, p.y + hgt, z); }
    for (let i = 0; i < pos.length / 6 - 1; i++) { const a = i * 2; idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
    const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setIndex(idx); g.computeVertexNormals();
    scene.add(new THREE.Mesh(g, new THREE.MeshLambertMaterial({ color, side: THREE.DoubleSide }))); };
  wall(-inS * 11, 1.3, '#f4f4f4'); wall(-inS * 11.05, 0.25, '#1d4ed8'); wall(-inS * 13, 5.5, '#9aa3b2'); /* SAFER и забор */
  /* трибуны по всей внешней стороне овала */
  const cv = document.createElement('canvas'); cv.width = 256; cv.height = 64; const g = cv.getContext('2d'), R5 = rng(19), cols = ['#ef4444', '#f97316', '#facc15', '#22c55e', '#3b82f6', '#e5e7eb', '#a855f7', '#111827'];
  g.fillStyle = '#1f2433'; g.fillRect(0, 0, 256, 64); for (let y = 2; y < 64; y += 6) for (let x = 1 + (y % 4); x < 256; x += 4) { g.fillStyle = cols[Math.floor(R5() * cols.length)]; g.fillRect(x, y, 3, 4); }
  const tex = new THREE.CanvasTexture(cv); tex.colorSpace = THREE.SRGBColorSpace; tex.wrapS = THREE.RepeatWrapping; tex.repeat.set(3, 1);
  const crowd = new THREE.MeshLambertMaterial({ map: tex, emissive: '#ffffff', emissiveMap: tex, emissiveIntensity: w.theme.lights ? 0.45 : 0.06 });
  for (let i = 0; i < N; i += 11) { const p = P[i], n = NR[i], st = new THREE.Group();
    for (let r = 0; r < 7; r++) { const b = new THREE.Mesh(new THREE.BoxGeometry(34, 2.2, 3.4), crowd); b.position.set(0, 1.1 + r * 2.2, r * 3.4); st.add(b); }
    st.position.set(p.x - n.x * inS * 22, p.y, p.z - n.z * inS * 22); st.lookAt(p.x, p.y, p.z); st.rotateY(Math.PI); scene.add(st); }
}

/* ================= АНИМАЦИИ СЦЕН: пит-лейн, машина безопасности, мотоциклы, эффекты ================= */
function strip(pts, w0, w1, y, color) {
  const pos = [], idx = [];
  for (let i = 0; i < pts.length; i++) { const a = pts[Math.max(0, i - 1)], b = pts[Math.min(pts.length - 1, i + 1)], t = b.clone().sub(a).setY(0).normalize(), n = new THREE.Vector3(-t.z, 0, t.x), p = pts[i];
    pos.push(p.x + n.x * w0, p.y + y, p.z + n.z * w0, p.x + n.x * w1, p.y + y, p.z + n.z * w1); }
  for (let i = 0; i < pts.length - 1; i++) { const a = i * 2; idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
  const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setIndex(idx); g.computeVertexNormals();
  return new THREE.Mesh(g, new THREE.MeshLambertMaterial({ color, side: THREE.DoubleSide }));
}
function makeSC() {
  const g = new THREE.Group(), body = new THREE.MeshStandardMaterial({ color: '#d9dde3', roughness: 0.3, metalness: 0.4 }), dark = new THREE.MeshStandardMaterial({ color: '#1a1d24', roughness: 0.4 });
  const add = (geo, m, x, y, z) => { const o = new THREE.Mesh(geo, m); o.position.set(x, y, z); g.add(o); return o; };
  add(new THREE.BoxGeometry(1.95, 0.6, 4.6), body, 0, 0.55, 0); add(new THREE.BoxGeometry(1.6, 0.5, 2.1), dark, 0, 1.1, -0.3);
  add(new THREE.BoxGeometry(1.96, 0.12, 4.62), new THREE.MeshBasicMaterial({ color: '#f59e0b' }), 0, 0.62, 0);
  for (const [x, z] of [[0.9, 1.5], [-0.9, 1.5], [0.9, -1.5], [-0.9, -1.5]]) { const wh = add(new THREE.CylinderGeometry(0.36, 0.36, 0.3, 14), dark, x, 0.36, z); wh.rotation.z = Math.PI / 2; }
  add(new THREE.BoxGeometry(1.2, 0.12, 0.25), dark, 0, 1.42, -0.2);
  const lights = [-0.4, 0.4].map(x => { const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowTex('rgba(255,190,60,1)', 'rgba(255,150,0,0)'), transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false })); sp.position.set(x, 1.55, -0.2); sp.scale.set(2.2, 2.2, 1); g.add(sp); return sp; });
  g.scale.setScalar(1.15); g.visible = false; return { group: g, lights };
}
function makeBike(color) {
  const g = new THREE.Group(), paint = new THREE.MeshStandardMaterial({ color, roughness: 0.35 }), dark = new THREE.MeshStandardMaterial({ color: '#16181d', roughness: 0.6 });
  const add = (geo, m, x, y, z, rx = 0) => { const o = new THREE.Mesh(geo, m); o.position.set(x, y, z); o.rotation.x = rx; g.add(o); return o; };
  const wheels = [0.75, -0.75].map(z => { const o = add(new THREE.TorusGeometry(0.3, 0.09, 8, 18), dark, 0, 0.36, z); o.rotation.y = Math.PI / 2; return o; });
  add(new THREE.CapsuleGeometry(0.22, 1.1, 6, 10), paint, 0, 0.7, 0.05, Math.PI / 2 - 0.15);
  add(new THREE.CapsuleGeometry(0.2, 0.5, 6, 10), paint, 0, 1.12, -0.1, 0.9);
  add(new THREE.SphereGeometry(0.2, 12, 10), new THREE.MeshStandardMaterial({ color: '#f8fafc', roughness: 0.3 }), 0, 1.42, 0.25);
  for (const sx of [-1, 1]) { const d = new THREE.Mesh(new THREE.PlaneGeometry(0.9, 0.22), brandMat('light')); d.position.set(sx * 0.235, 0.74, 0.1); d.rotation.set(0, sx * Math.PI / 2, -0.15 * sx); g.add(d); }
  const lean = new THREE.Group(); lean.add(g); g.scale.setScalar(1.3); const root = new THREE.Group(); root.add(lean); root.visible = false;
  return { group: root, lean, wheels };
}
function numTex(num, fg = '#111827', bg = '#ffffff') { const c = document.createElement('canvas'); c.width = c.height = 128; const g = c.getContext('2d');
  g.fillStyle = bg; g.beginPath(); g.arc(64, 64, 62, 0, 7); g.fill(); g.fillStyle = fg; g.font = '900 78px Inter, sans-serif'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(String(num), 64, 70);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t; }
function makeStock(color, num) {
  const g = new THREE.Group(), paint = new THREE.MeshStandardMaterial({ color, roughness: 0.35, metalness: 0.2 }), dark = new THREE.MeshStandardMaterial({ color: '#16181d', roughness: 0.5 });
  const add = (geo, m, x, y, z) => { const o = new THREE.Mesh(geo, m); o.position.set(x, y, z); g.add(o); return o; };
  add(new THREE.BoxGeometry(2.0, 0.7, 5.0), paint, 0, 0.6, 0); add(new THREE.BoxGeometry(1.7, 0.55, 2.0), dark, 0, 1.2, -0.4); add(new THREE.BoxGeometry(1.9, 0.08, 0.4), dark, 0, 1.15, -2.4);
  if (num == null) add(new THREE.CylinderGeometry(0.45, 0.45, 0.05, 20), new THREE.MeshBasicMaterial({ color: '#ffffff' }), 1.01, 0.7, 0.2).rotation.z = Math.PI / 2;
  else { const m = new THREE.MeshBasicMaterial({ map: numTex(num), transparent: true }); /* номер на дверях и на крыше */
    for (const sd of [-1, 1]) { const d = add(new THREE.PlaneGeometry(1.0, 1.0), m, sd * 1.012, 0.62, 0.2); d.rotation.y = sd * Math.PI / 2; }
    const r = add(new THREE.PlaneGeometry(1.1, 1.1), m, 0, 1.48, -0.4); r.rotation.set(-Math.PI / 2, 0, Math.PI);
    add(new THREE.BoxGeometry(2.02, 0.16, 5.02), new THREE.MeshStandardMaterial({ color: '#f8fafc', roughness: 0.4 }), 0, 0.42, 0); }
  const wheels = []; for (const [x, z] of [[0.95, 1.6], [-0.95, 1.6], [0.95, -1.6], [-0.95, -1.6]]) { const wh = add(new THREE.CylinderGeometry(0.38, 0.38, 0.32, 14), dark, x, 0.38, z); wh.rotation.z = Math.PI / 2; wheels.push(wh); }
  g.scale.setScalar(1.1); g.visible = false; return { group: g, wheels };
}
function makeCrew() {
  const g = new THREE.Group(), suit = new THREE.MeshStandardMaterial({ color: '#f97316', roughness: 0.6 }), helm = new THREE.MeshStandardMaterial({ color: '#f8fafc', roughness: 0.3 });
  const spots = [[2.0, 1.85], [-2.0, 1.85], [2.0, -1.55], [-2.0, -1.55], [0, 4.3], [0, -3.7], [2.6, 0.2]];
  const men = spots.map(([x, z]) => { const m = new THREE.Group(); const b = new THREE.Mesh(new THREE.CapsuleGeometry(0.3, 0.7, 4, 8), suit); b.position.y = 0.75; m.add(b); const h = new THREE.Mesh(new THREE.SphereGeometry(0.24, 10, 8), helm); h.position.y = 1.5; m.add(h); m.position.set(x, 0, z); g.add(m); return m; });
  g.visible = false; return { group: g, men, spots };
}
function extendWorld(w, tr, toV) {
  const { P, N, L, TG, NR, scene } = w;
  /* кривизна: + поворот вправо (центр справа), − влево */
  w.curv = P.map((_, i) => { const a = TG[(i - 4 + N) % N], b = TG[(i + 4) % N]; return b.clone().sub(a).dot(NR[i]); });
  /* самая длинная прямая */
  let best = { len: 0, i0: 0 }, run = 0, start = 0;
  for (let j = 0; j < N * 2; j++) { const i = j % N; if (Math.abs(w.curv[i]) < 0.05) { if (!run) start = j; run++; if (run > best.len && run < N) best = { len: run, i0: start % N }; } else run = 0; }
  w.straight = { s0: best.i0 / N * L, s1: (best.i0 + best.len) / N * L };
  w.corners = w.cornerIdx.map(c => ({ ...c, s: c.i / N * L, k: Math.abs(w.curv[c.i]), inSign: Math.sign(w.curv[c.i]) || 1 }));
  w.sharpest = w.corners.reduce((b, c, k) => (c.k > (w.corners[b]?.k ?? -1) ? k : b), 0);
  w.cornerAfter = s => { const sn = ((s % L) + L) % L; let bc = null, bd = 1e9; for (const c of w.corners) { const d = (c.s - sn + L) % L; if (d > 40 && d < bd) { bd = d; bc = c; } } return bc && { ...c0(bc), s: s + bd }; };
  const c0 = c => c;
  /* пит-лейн из данных трассы */
  if (tr.pit?.length > 4) {
    let PP = tr.pit.map(p => toV(p[0], p[1], p[2]));
    const near = v => { let bi = 0, bd = 1e18; P.forEach((p, i) => { const d = (p.x - v.x) ** 2 + (p.z - v.z) ** 2; if (d < bd) { bd = d; bi = i; } }); return bi; };
    let iA = near(PP[0]), iB = near(PP[PP.length - 1]);
    if ((iB - iA + N) % N > N / 2) { PP = PP.reverse(); [iA, iB] = [iB, iA]; }
    const smooth = new THREE.CatmullRomCurve3(PP, false, 'centripetal'), PL = smooth.getLength(), M = Math.max(20, Math.round(PL / 2));
    PP = smooth.getSpacedPoints(M); PP.forEach((p, i) => { const k = near(p); p.y = Math.min(p.y, P[k].y) - 0.06; });
    w.pit = { PP, PL, sEntry: iA / N * L, sExit: iB / N * L, M };
    w.pitAt = d => { d = clamp(d, 0, PL); const f = d / PL * M, i = Math.min(M - 1, Math.floor(f)), u = f - i; const p = PP[i].clone().lerp(PP[i + 1], u), t = PP[i + 1].clone().sub(PP[i]).setY(0).normalize(); return { p, t, n: new THREE.Vector3(-t.z, 0, t.x) }; };
    scene.add(strip(PP, -6, 6, 0, w.theme.asphalt));
    /* боксы команд: со стороны от трассы */
    const mid = w.pitAt(PL * 0.5), tk = P[near(mid.p)], away = Math.sign(mid.p.clone().sub(tk).dot(mid.n)) || 1; w.pit.away = away;
    const R0 = rng(11);
    for (let d = PL * 0.22; d < PL * 0.8; d += 13) { const a = w.pitAt(d), b = new THREE.Group();
      const box = new THREE.Mesh(new THREE.BoxGeometry(12, 7, 11), new THREE.MeshLambertMaterial({ color: '#e7e9ee' })); box.position.y = 3.5; b.add(box);
      const door = new THREE.Mesh(new THREE.PlaneGeometry(10, 5), new THREE.MeshBasicMaterial({ color: '#1d2230' })); door.position.set(0, 2.6, -5.52); door.rotation.y = Math.PI; b.add(door);
      const stripe = new THREE.Mesh(new THREE.BoxGeometry(12.05, 1.1, 11.05), new THREE.MeshLambertMaterial({ color: CAR_COLORS[Math.floor(R0() * CAR_COLORS.length)] })); stripe.position.y = 6.2; b.add(stripe);
      b.position.copy(a.p).addScaledVector(a.n, away * 13).setY(a.p.y); b.lookAt(a.p.x, a.p.y, a.p.z); b.rotateY(Math.PI); scene.add(b); }
  }
  /* машина безопасности, мотоциклы, стоковые машины, механики */
  w.sc = HQ ? makeSCHQ() : makeSC(); scene.add(w.sc.group);
  w.bikes = ['#ef4444', '#3b82f6', '#facc15', '#f3f4f6', '#22c55e', '#f97316', '#a855f7'].map(c => { const b = makeBike(c); scene.add(b.group); return b; });
  w.stock = ['#22c55e', '#f97316', '#a855f7'].map(c => { const b = makeStock(c); scene.add(b.group); return b; });
  /* пелетон NASCAR для act stockpack: свои машины с номерами */
  w.pack = [['#facc15', 5], ['#3b82f6', 20], ['#ef4444', 12], ['#f3f4f6', 24], ['#22c55e', 11], ['#f97316', 9], ['#a855f7', 45], ['#06b6d4', 8], ['#ec4899', 1], ['#111827', 3]]
    .map(([c, n]) => { const b = makeStock(c, n); scene.add(b.group); return b; });
  if (tr.oval) ovalScenery(w);
  w.crew = makeCrew(); scene.add(w.crew.group);
  w.cars.forEach(c => { c.band0 = '#' + c.band.color.getHexString(); });
  /* процедурный город вдоль трассы (ролики про городские трассы): дома с окнами */
  if (spec?.city) { const c = document.createElement('canvas'); c.width = 64; c.height = 128; const g = c.getContext('2d'), R2 = rng(77);
    g.fillStyle = '#2b2f3d'; g.fillRect(0, 0, 64, 128); for (let y = 4; y < 128; y += 10) for (let x = 4; x < 64; x += 10) { g.fillStyle = R2() < 0.55 ? (R2() < 0.5 ? '#ffd98a' : '#fff1c9') : '#3a4052'; g.fillRect(x, y, 6, 6); }
    const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace; tex.magFilter = THREE.NearestFilter;
    const mat = new THREE.MeshLambertMaterial({ map: tex, emissive: '#ffffff', emissiveMap: tex, emissiveIntensity: w.theme.lights ? 0.9 : 0.15 });
    const R3 = rng(5), spots = [];
    for (let s = 0; s < L; s += 16) for (const side of [-1, 1]) { const a = w.at(s), off = side * (24 + R3() * 16), x = a.p.x + a.n.x * off, z = a.p.z + a.n.z * off;
      let ok = true; for (let i = 0; i < N; i += 3) { const d = (P[i].x - x) ** 2 + (P[i].z - z) ** 2; if (d < 18 * 18) { ok = false; break; } } if (ok) spots.push({ x, y: a.p.y, z, yaw: Math.atan2(a.t.x, a.t.z), h: 18 + R3() * 55, wd: 12 + R3() * 8 }); }
    const im = new THREE.InstancedMesh(new THREE.BoxGeometry(1, 1, 1), mat, spots.length), m4 = new THREE.Matrix4(), q = new THREE.Quaternion(), e = new THREE.Euler();
    spots.forEach((b, k) => { q.setFromEuler(e.set(0, b.yaw, 0)); m4.compose(new THREE.Vector3(b.x, b.y + b.h / 2, b.z), q, new THREE.Vector3(b.wd, b.h, 12)); im.setMatrixAt(k, m4); });
    scene.add(im); }
  /* трибуны со зрителями вдоль стартовой прямой (со стороны, противоположной боксам) */
  { const c = document.createElement('canvas'); c.width = 256; c.height = 64; const g = c.getContext('2d'), R4 = rng(31), cols = ['#ef4444', '#f97316', '#facc15', '#22c55e', '#3b82f6', '#e5e7eb', '#a855f7', '#111827'];
    g.fillStyle = '#1f2433'; g.fillRect(0, 0, 256, 64); for (let y = 2; y < 64; y += 6) for (let x = 1 + (y % 4); x < 256; x += 4) { g.fillStyle = cols[Math.floor(R4() * cols.length)]; g.fillRect(x, y, 3, 4); }
    const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace; tex.wrapS = THREE.RepeatWrapping; tex.repeat.set(4, 1);
    const crowd = new THREE.MeshLambertMaterial({ map: tex, emissive: '#ffffff', emissiveMap: tex, emissiveIntensity: w.theme.lights ? 0.45 : 0.05 }), steel = new THREE.MeshLambertMaterial({ color: '#c9ced8' });
    const sides = tr.oval ? [] : w.pit ? [-w.pit.away] : [-1, 1];
    for (let s = -140; s < 240; s += 38) for (const side of sides) { const a = w.at(((s % L) + L) % L), g2 = new THREE.Group();
      for (let r = 0; r < 4; r++) { const step = new THREE.Mesh(new THREE.BoxGeometry(36, 2.2, 3.2), crowd); step.position.set(0, 1.1 + r * 2.2, r * 3.2); g2.add(step); }
      const roof = new THREE.Mesh(new THREE.BoxGeometry(37, 0.5, 15), steel); roof.position.set(0, 12, 5); g2.add(roof);
      g2.position.copy(a.p).addScaledVector(a.n, side * 17).setY(a.p.y); g2.lookAt(a.p.x - a.n.x * side * 100, a.p.y, a.p.z - a.n.z * side * 100); g2.rotateY(Math.PI);
      let ok = true; for (let i = 0; i < N; i += 2) { const d = (P[i].x - g2.position.x) ** 2 + (P[i].z - g2.position.z) ** 2; if (d < 12 * 12) { ok = false; break; } } if (ok) scene.add(g2); } }
  /* ролики «построй трассу»: бетонные блоки, такси, люки, сварщики, стены крепости */
  const BL = 2.5, nb = Math.floor(L / BL), bm = new THREE.InstancedMesh(new THREE.BoxGeometry(0.75, 1.05, 2.35), new THREE.MeshLambertMaterial({ color: '#ffffff' }), nb * 2);
  bm.instanceMatrix.setUsage(THREE.DynamicDrawUsage); bm.frustumCulled = false; bm.visible = false; scene.add(bm);
  const base = [], bc = new THREE.Color();
  for (let k = 0; k < nb; k++) for (const side of [-1, 1]) { const a = w.at(k * BL); base.push({ s: k * BL, x: a.p.x + a.n.x * side * 9.3, y: a.p.y, z: a.p.z + a.n.z * side * 9.3, yaw: Math.atan2(a.t.x, a.t.z) });
    bm.setColorAt(base.length - 1, bc.set(k % 6 < 1 ? '#c8352e' : k % 2 ? '#e6e3dc' : '#d4d0c7')); }
  w.blocks = { mesh: bm, base, mode: null };
  w.taxis = [0, 1, 2, 3, 4].map(k => { const t = makeStock(k % 2 ? '#f5c518' : '#ffd23f'); const sign = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.3, 0.4), new THREE.MeshBasicMaterial({ color: '#fff7c2' })); sign.position.set(0, 1.62, -0.3); t.group.add(sign); scene.add(t.group); return t; });
  w.manhole = new THREE.Mesh(new THREE.CylinderGeometry(0.62, 0.62, 0.08, 20), new THREE.MeshStandardMaterial({ color: '#4a4d55', metalness: 0.6, roughness: 0.5 })); w.manhole.visible = false; scene.add(w.manhole);
  w.holes = [0, 1, 2].map(() => { const m = new THREE.Mesh(new THREE.CircleGeometry(0.62, 20), new THREE.MeshBasicMaterial({ color: '#0b0c10' })); m.rotation.x = -Math.PI / 2; m.visible = false; scene.add(m); return m; });
  w.workers = [0, 1, 2].map(() => { const g = new THREE.Group(); const b = new THREE.Mesh(new THREE.CapsuleGeometry(0.3, 0.6, 4, 8), new THREE.MeshStandardMaterial({ color: '#f97316' })); b.position.y = 0.6; b.rotation.x = 0.5; g.add(b); const h = new THREE.Mesh(new THREE.SphereGeometry(0.24, 10, 8), new THREE.MeshStandardMaterial({ color: '#ffd23f' })); h.position.set(0, 1.15, 0.3); g.add(h); g.visible = false; scene.add(g); return g; });
  w.castle = null;
  /* линия замера отрыва для режима обгона */
  w.det = new THREE.Mesh(new THREE.PlaneGeometry(15, 1.6), new THREE.MeshBasicMaterial({ color: '#22d3ee', transparent: true, opacity: 0.9, blending: THREE.AdditiveBlending, depthWrite: false, fog: false })); w.det.rotation.x = -Math.PI / 2; w.det.visible = false; scene.add(w.det);
  /* пул эффектов: дым, свечения, штрихи потока */
  const mk = (n, f) => Array.from({ length: n }, () => { const o = f(); o.visible = false; scene.add(o); return o; });
  const smokeT = glowTex('rgba(235,235,240,0.9)', 'rgba(220,220,230,0)'), glowT = glowTex('rgba(255,255,255,1)', 'rgba(255,255,255,0)');
  w.fx = {
    smoke: mk(160, () => new THREE.Sprite(new THREE.SpriteMaterial({ map: smokeT, transparent: true, depthWrite: false, fog: false }))), si: 0,
    glow: mk(140, () => new THREE.Sprite(new THREE.SpriteMaterial({ map: glowT, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false }))), gi: 0,
    disc: mk(30, () => new THREE.Sprite(new THREE.SpriteMaterial({ map: discTex(), transparent: true, depthTest: false, depthWrite: false, fog: false }))), di: 0,
    streak: mk(70, () => new THREE.Mesh(new THREE.PlaneGeometry(0.07, 1), new THREE.MeshBasicMaterial({ color: '#fff', transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide, fog: false }))), ki: 0,
  };
}
function fxReset() { const f = world.fx; f.si = f.gi = f.ki = f.di = 0; }
function disc(pos, sc, color) { const f = world.fx; if (f.di >= f.disc.length) return; const s = f.disc[f.di++]; s.visible = true; s.position.copy(pos); s.scale.set(sc, sc, 1); s.material.color.set(color); s.renderOrder = 12; }
const discTex = () => { const c = document.createElement('canvas'); c.width = c.height = 128; const g = c.getContext('2d'); g.beginPath(); g.arc(64, 64, 58, 0, 7); g.fillStyle = '#fff'; g.fill(); g.beginPath(); g.arc(64, 64, 44, 0, 7); g.fillStyle = '#ddd'; g.fill(); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t; };
function fxEnd() { const f = world.fx; for (let i = f.si; i < f.smoke.length; i++) f.smoke[i].visible = false; for (let i = f.gi; i < f.glow.length; i++) f.glow[i].visible = false; for (let i = f.ki; i < f.streak.length; i++) f.streak[i].visible = false; for (let i = f.di; i < f.disc.length; i++) f.disc[i].visible = false; }
function puff(pos, sc, op) { const f = world.fx; if (f.si >= f.smoke.length) return; const s = f.smoke[f.si++]; s.visible = true; s.position.copy(pos); s.scale.set(sc, sc, 1); s.material.opacity = op; }
function glow(pos, sc, color, op = 1, onTop = false) { const f = world.fx; if (f.gi >= f.glow.length) return; const s = f.glow[f.gi++]; s.visible = true; s.position.copy(pos); s.scale.set(sc, sc, 1); s.material.color.set(color); s.material.opacity = op; s.material.depthTest = !onTop; s.renderOrder = onTop ? 10 : 0; }
function streak(pos, dir, len, color, op) { const f = world.fx; if (f.ki >= f.streak.length) return; const m = f.streak[f.ki++]; m.visible = true; m.position.copy(pos); m.scale.set(1, len, 1); m.material.color.set(color); m.material.opacity = op;
  m.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), dir); m.rotateY(Math.PI / 4 * ((f.ki % 2) * 2 - 1)); }

/* ---------- хореография: состояние каждой машины как функция времени сцены ---------- */
const hashK = k => { const x = Math.sin(k * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };
function trackPose(s, lane) { const a = world.at(s); return { pos: a.p.clone().addScaledVector(a.n, lane).setY(a.p.y + 0.02), dir: a.t.clone(), n: a.n.clone(), s }; }
function pitPose(d) { const a = world.pitAt(d); return { pos: a.p.clone().setY(a.p.y + 0.08), dir: a.t.clone(), n: a.n.clone(), s: d }; }
/* машина, заезжающая в боксы: к моменту tBox встаёт у бокса, стоит stop секунд, уезжает с ограничителем 25 м/с */
function pitRun(lt, tBox, stop = 2.2, d0 = 110) {
  const p = world.pit; if (!p) return { pose: trackPose(lt * 60, 0), phase: 'track', dist: lt * 60 };
  const box = p.PL * 0.5;
  if (lt < tBox) { const u = clamp(lt / tBox), d = box - d0 * (1 - u) * (1 - u) - Math.max(0, -lt) * 2 * d0 / tBox;
    return d < 0 ? { pose: trackPose(p.sEntry + d, 0), phase: 'in', dist: d } : { pose: pitPose(d), phase: 'enter', dist: d }; }
  if (lt < tBox + stop) return { pose: pitPose(box), phase: 'stop', k: (lt - tBox) / stop, dist: box };
  const tau = lt - tBox - stop, acc = 14, t1 = 25 / acc, d = box + (tau < t1 ? 0.5 * acc * tau * tau : 0.5 * acc * t1 * t1 + 25 * (tau - t1));
  return d < p.PL ? { pose: pitPose(d), phase: 'go', dist: d } : { pose: trackPose(p.sExit + (d - p.PL), 0), phase: 'out', dist: d };
}
function actStates(shot, lt, T, dur) {
  const w = world, a = shot.act || {}, L = w.L, tp = clamp(lt / dur);
  const cars = w.cars.map(c => ({ ...trackPose(c.s0 + c.v * T, c.lane), yaw: 0, vis: true, heat: 0, cold: 0, smoke: 0, boost: 0, brake: 0, energy: 0, flap: 0, roll: c.s0 + c.v * T }));
  const ex = {};
  const touched = new Set(), put = (k, s, lane = 0, extra = {}) => { touched.add(k); Object.assign(cars[k], trackPose(s, lane), { roll: s }, extra); };
  const hide = keep => cars.forEach((c, k) => { if (!keep.includes(k)) c.vis = false; });
  if (shot.hud?.type === 'phone') cars.forEach((c, k) => put(k, k * L * 0.083 + (70 - k) * T, 0));
  switch (a.type) {
    case 'slide': { /* занос в повороте: зад уходит наружу, дым из-под колёс */
      const c = w.corners[a.corner ?? w.sharpest] || w.corners[0], tc = dur * (a.tc ?? 0.45), v = a.v ?? 38, s = c.s + (lt - tc) * v;
      const b = Math.exp(-(((lt - tc - 0.25) / 0.7) ** 2)), wob = 1 + 0.3 * Math.sin(lt * 7);
      put(0, s, -c.inSign * 3.2 * b, { yaw: c.inSign * 0.7 * b * wob, smoke: b > 0.2 ? b : 0, cold: a.cold ? 1 : 0, heat: a.heat ? 0.8 : 0 });
      (a.followers || [1, 2]).forEach((k, j) => put(k, s - 22 * (j + 1) - 6 * tp, ((j % 2) * 2 - 1) * 1.5, { cold: a.cold ? 1 : 0 }));
      break; }
    case 'restart': { /* рестарт за машиной безопасности */
      const s0 = a.at != null ? a.at * L : w.straight.s0 - 140, tr = dur * (a.release ?? 0.4), vS = 26, lead = lt < tr ? s0 + vS * lt : s0 + vS * lt + 0.5 * 20 * (lt - tr) ** 2;
      cars.forEach((c, k) => { const dt = Math.max(0, lt - tr), acc = 20 + 6 * Math.sin(k * 2.3), slide = k === 3 ? Math.exp(-(((lt - tr - 1.3) / 0.6) ** 2)) : 0;
        const s = s0 + vS * lt + 0.5 * acc * dt * dt - k * 9 - (k === 3 ? 10 * clamp(dt - 1) ** 1.5 : 0);
        put(k, s, (k % 2 ? 2.4 : -2.4) * easeOut(dt / 1.2) * (lt > tr ? 1 : 0.15), { yaw: 0.45 * slide * Math.sin(lt * 9), smoke: slide > 0.2 ? slide : 0, cold: 0.8 }); });
      const scS = lt < tr ? lead + 28 : lead + 28 - 0.5 * 26 * (lt - tr) ** 2 * 0.6;
      ex.sc = { ...trackPose(Math.max(scS, s0 + vS * lt - 200), lt < tr ? 0 : -7 * easeOut((lt - tr) / 1.5)), lights: lt < tr + 0.2, vis: lt < tr + 3.5 };
      break; }
    case 'pit': { /* пит-стоп: заезд, механики, смена шин, выезд */
      const h = a.car ?? 0, tb = dur * (a.box ?? 0.4), r = pitRun(lt, tb, a.stop ?? 2.0, a.d0 ?? 24 * tb);
      Object.assign(cars[h], r.pose, { roll: r.dist, phase: r.phase });
      if (r.phase === 'stop') { cars[h].crew = clamp(r.k * 6) * clamp((1 - r.k) * 8 + 0.3); cars[h].wheelOff = r.k > 0.2 && r.k < 0.6 ? 1 : 0; }
      if (r.phase === 'stop' && r.k > 0.4 || r.phase === 'go' || r.phase === 'out') cars[h].band = a.band || TYRE.hard;
      if (a.rival != null) put(a.rival, w.pit ? w.pit.sEntry - 40 + 55 * lt : 55 * lt, 0);
      ex.crewOf = h; break; }
    case 'pitexit': { /* соперник выезжает из боксов позади вас */
      const p = a.pitcar ?? 0, h = a.car ?? 1, te = dur * 0.62, pl = w.pit ? w.pit.PL : 0, dd = lt < te ? pl - 25 * (te - lt) : pl + 25 * (lt - te) + 5 * (lt - te) ** 2;
      Object.assign(cars[p], w.pit && lt < te ? pitPose(Math.max(0, dd)) : trackPose((w.pit ? w.pit.sExit : 0) + dd - pl, 0), { roll: dd, band: TYRE.hard, phase: lt < te ? 'go' : 'out' });
      const sx = w.pit ? w.pit.sExit : 0; put(h, sx + 50 * (lt - dur * 0.42), 0, { band: TYRE.soft }); break; }
    case 'follow': { /* вы в секунде от лидера и не можете пройти */
      const sA = (a.at != null ? a.at * L : w.straight.s0 - 400) + 52 * lt;
      put(0, sA, 2.0 * Math.sin(lt * 1.6 - 0.6)); put(1, sA - 12 + 2.5 * Math.sin(lt * 1.3), 2.6 * Math.sin(lt * 1.6)); break; }
    case 'race2': { /* две метки на виде сверху: свежие шины отыгрывают отставание */
      const base = (a.at ?? 0) * L + L * 0.85 * tp, gap = lerp(L * 0.05, -L * 0.012, ease(tp));
      put(0, base, 0); put(1, base - gap, 0, { band: TYRE.soft });
      ex.markers = [{ k: 0, color: CAR_COLORS[0] }, { k: 1, color: CAR_COLORS[1] }]; break; }
    case 'trace': { const s = (a.at ?? 0) * L + L * tp * (a.laps ?? 1); put(0, s, 0); ex.markers = [{ k: 0, color: '#ffd23f' }]; break; }
    case 'wings': { /* подвижные крылья: открываются на прямой */
      const s = w.straight.s0 + 20 + 70 * lt; put(0, s, 0, { flap: clamp((lt - 0.5) / 0.5) * (1 - clamp((lt - dur + 1.1) / 0.5)) });
      put(1, s - 40, 1.5, { flap: clamp((lt - 1.2) / 0.5) * (1 - clamp((lt - dur + 0.8) / 0.5)) }); break; }
    case 'boost': { /* в секунде на линии замера — режим обгона */
      const sD = w.straight.s0 + 60, tb = dur * 0.32, lead = sD - 75 + 62 * lt, dt = Math.max(0, lt - tb);
      put(0, lead, 0); put(1, lead - 12 + 0.5 * 9 * dt * dt, 3 * easeOut(dt / 0.8) * (1 - clamp((dt - 3.2) / 1)), { boost: lt > tb ? clamp(dt * 3) : 0 }); ex.det = sD; break; }
    case 'energy': { /* торможение заряжает батарею, на разгоне — отдаёт */
      const c = w.cornerAfter(w.straight.s1 - 300) || { s: w.straight.s1 }, tb = dur * 0.22, tc = tb + 2.0, v0 = 80, v1 = 26, acc = 16;
      const pos = t => t < tb ? v0 * t : t < tc ? v0 * tb + (v0 * (t - tb) - (v0 - v1) * (t - tb) ** 2 / (2 * (tc - tb))) : v0 * tb + (v0 + v1) / 2 * (tc - tb) + v1 * (t - tc) + 0.5 * acc * (t - tc) ** 2;
      const s = c.s - pos(tc) + pos(lt), braking = lt > tb && lt < tc;
      put(0, s, 0, { brake: braking ? 1 : 0, energy: braking ? 1 : 0, boost: lt > tc + 0.2 ? 0.7 : 0 }); ex.battery = lt < tb ? 0.25 : lt < tc ? lerp(0.25, 0.9, (lt - tb) / (tc - tb)) : lerp(0.9, 0.55, clamp((lt - tc) / (dur - tc))); break; }
    case 'duel': { /* борьба колесо в колесо */
      const s = w.straight.s0 - 100 + 60 * lt, d = 5 * Math.sin(lt * 0.9) + (lt > dur * 0.6 ? 0.5 * 10 * (lt - dur * 0.6) ** 2 : 0);
      put(0, s, -2.5); put(1, s + d - 3, 2.5, { boost: lt > dur * 0.6 ? 1 : 0 }); break; }
    case 'traffic': case 'reopen': { hide([]); const b = (a.at ?? 0.3) * L + (a.v ?? 13) * lt;
      ex.taxis = w.taxis.map((_, k) => ({ ...trackPose(b - k * 15, (k % 2 ? 2.8 : -2.8)), yaw: 0 })); break; }
    case 'manhole': { hide([0, 1]); const sm = a.at != null ? a.at * L : w.straight.s0 + 160, tc = dur * (a.tc ?? 0.4), v = 46, dt = lt - tc;
      const sH = dt < 0 ? sm + dt * v : sm + v * (1 - Math.exp(-dt * 1.1)) / 1.1;
      put(0, sH, 0.25, { smoke: dt > 0 ? 0.9 * clamp(1 - dt / 3) : 0, yaw: dt > 0 ? 0.12 * Math.sin(dt * 6) * Math.exp(-dt) : 0 });
      put(1, sm + (lt - tc) * v - 45 - (dt > 0 ? dt * dt * 6 : 0), -2.6); ex.manhole = { s: sm, t: dt }; break; }
    case 'weld': { hide([]); ex.weld = { s: a.at != null ? a.at * L : w.straight.s0 + 160 }; ex.focus = trackPose(ex.weld.s + 14, 0); break; }
    case 'narrow': { const c = w.corners.find(x => x.n === a.corner) || w.corners[w.sharpest], tc = dur * (a.tc ?? 0.55), s = c.s + (lt - tc) * (a.v ?? 22);
      hide([0, 1]); put(0, s, 0); put(1, s - 16, 0); ex.castle = c.s; break; }
    case 'speed': { const s = w.straight.s0 + 20 + (a.v ?? 88) * lt; put(0, s, 0, { speed: 1 }); put(1, s - 26 + 4 * Math.sin(lt), 2.4, { speed: 1 }); hide([0, 1]); break; }
    case 'heat': { const s = (a.at ?? 0.2) * L + 62 * lt; put(0, s, 0, { heat: 0.35 + 0.65 * tp }); put(1, s - 16, 1.4, { heat: 0.3 + 0.5 * tp }); break; }
    case 'cold': { const s = (a.at ?? 0.3) * L + 50 * lt; put(0, s, 0.4 * Math.sin(lt * 2), { cold: 1, yaw: 0.06 * Math.sin(lt * 3.1) }); put(1, s - 18, -1.4, { cold: 1 }); ex.frost = 1; break; }
    case 'fade': { /* шины «умирают»: машину заносит, соперники проходят */
      const c = w.corners[a.corner ?? w.sharpest] || w.corners[0], t1 = dur * (a.t1 ?? 0.55), s0 = c.s - 58 * t1, dying = clamp((lt - t1 + 0.6) / 1.2);
      const sH = s0 + 58 * lt - 14 * dying * Math.max(0, lt - t1 + 0.6);
      put(0, sH, -c.inSign * 2.5 * dying * Math.exp(-(((lt - t1 - 0.4) / 0.9) ** 2)), { yaw: c.inSign * 0.35 * dying * Math.exp(-(((lt - t1 - 0.4) / 0.9) ** 2)) * (1 + 0.3 * Math.sin(lt * 8)), smoke: dying > 0.3 ? dying * Math.exp(-(((lt - t1 - 0.4) / 1) ** 2)) : 0, heat: 0.4 + 0.6 * tp });
      put(1, s0 + 58 * lt - 26 + 9 * dying * Math.max(0, lt - t1 + 0.6), 2.6 * dying); put(2, s0 + 58 * lt - 46 + 11 * dying * Math.max(0, lt - t1), -2.4 * dying); break; }
    case 'convoy': { /* at: доля круга или 'straight' — начало главной прямой; t0: продолжение предыдущей сцены (секунды) */ const s = (a.at === 'straight' ? w.straight.s0 - 60 : (a.at ?? 0.1) * L) + (a.v ?? 62) * (lt + (a.t0 ?? 0)); [0, 1, 2, 3].slice(0, a.n ?? 4).forEach(k => put(k, s - k * 11, (k % 2 ? 1.8 : -1.8), { boost: k === 3 ? 0.35 : 0 })); break; }
    case 'bikes': { hide([]); const s = (a.at ?? 0.3) * L + 52 * lt; ex.bikes = w.bikes.slice(0, 3).map((_, k) => ({ ...trackPose(s - k * 8, (k - 1) * 2.4), lean: 1 }));
      ex.stock = w.stock.map((_, k) => ({ ...trackPose(s + 24 + k * 10, (k % 2 ? 1.8 : -1.8)) })); break; }
    case 'stockpack': { /* NASCAR: плотный пелетон в два ряда, «драфт»; pass — номер машины, которая выходит вперёд */
      hide([]); const n = a.n ?? 8, s = (a.at ?? 0.1) * L + (a.v ?? 72) * lt;
      ex.pack = w.pack.slice(0, n).map((_, k) => { const row = Math.floor(k / 2), lane = (k % 2 ? 2.3 : -2.3) + 0.35 * Math.sin(lt * 1.4 + k * 1.7);
        let ds = -row * 8.5 - (k % 2) * 3.5 + 0.8 * Math.sin(lt * 0.9 + k);
        if (a.pass === k) ds += 34 * ease(tp) - 4; if (a.drop === k) ds -= 30 * ease(tp);
        return { ...trackPose(s + ds, a.pass === k ? lerp(lane, 0, ease(tp)) : lane) }; });
      if (a.pass != null && w.pack[a.pass]) ex.focus = ex.pack[a.pass]; break; }
    case 'motogp': { /* только мотоциклы: группа из n гонщиков, обгон pass */
      hide([]); const n = a.n ?? 6, s = (a.at ?? 0.3) * L + (a.v ?? 50) * lt;
      ex.bikes = w.bikes.slice(0, n).map((_, k) => { let ds = -k * 6.5 + 0.6 * Math.sin(lt * 1.1 + k * 2); if (a.pass === k) ds += 16 * ease(tp);
        return { ...trackPose(s + ds, ((k % 3) - 1) * 2.1 + 0.5 * Math.sin(lt * 0.8 + k)), lean: 1 }; }); break; }
  }
  /* машины, которыми сцена не управляет, не ездят по кадру сами по себе (раньше влетали под камеру) */
  if (touched.size && !a.others) cars.forEach((c, k) => { if (!touched.has(k)) c.vis = false; });
  return { cars, ex };
}

/* ---------- применение состояний к сцене ---------- */
const UP = new THREE.Vector3(0, 1, 0);
function pose3(o, st, lift = 0) { const hd = st.dir.clone().addScaledVector(st.n || new THREE.Vector3(-st.dir.z, 0, st.dir.x), st.yaw || 0).normalize(); o.position.copy(st.pos).setY(st.pos.y + lift); o.lookAt(st.pos.x + hd.x, st.pos.y + lift, st.pos.z + hd.z); return hd; }
function applyActs(shot, lt, T, dur) {
  const w = world, { cars, ex } = actStates(shot, lt, T, dur); fxReset();
  w.cars.forEach((c, k) => { applyPaint(w, shot, c, k); const st = cars[k]; c.st = st; c.group.visible = st.vis;
    const bk = brickOf(shot, k); if (c.bk) for (const o of Object.values(c.bk)) o.group.visible = false;   /* кирпичный стиль: обычная машина прячется, вместо неё — из блоков */
    if (bk) { c.bk = c.bk || {}; const id = bk.kind + (bk.c || ''), o = c.bk[id] || (c.bk[id] = makeBrickCar(bk.kind, bk.c || CAR_COLORS[k % CAR_COLORS.length])); if (!o.group.parent) w.scene.add(o.group);
      c.group.visible = false; o.group.visible = st.vis; if (st.vis) { pose3(o.group, st); o.wheels.forEach(wh => { wh.rotation.x = st.roll / 0.4; }); } }
    if (!st.vis) return;
    const hd = pose3(c.group, st); const right = new THREE.Vector3(-hd.z, 0, hd.x);
    c.wheels.forEach(wh => { wh.rotation.x = st.roll / 0.4; wh.scale.setScalar(st.wheelOff ? 0.001 : 1); });
    const hc = new THREE.Color(); if (st.heat) hc.setRGB(1, 0.32, 0.08).multiplyScalar(st.heat * 0.9); else if (st.cold) hc.setRGB(0.25, 0.6, 1).multiplyScalar(st.cold * 0.75); else hc.setRGB(0, 0, 0); if (HQ) hc.multiplyScalar(0.2); c.rubber.emissive.copy(hc);
    c.band.color.set(st.band || shot.band || c.band0);   /* shot.band: цвет полосы шин у всех машин сцены (например, зелёный — промежуточные) */
    if (c.hq) { c.rearFlap.rotation.x = -0.5 * (st.flap || 0); c.frontFlap.rotation.x = -0.3 * (st.flap || 0); }   /* HQ: активная аэродинамика — закрылки ложатся на прямой */
    else { c.rearFlap.rotation.x = lerp(-0.5, -0.04, st.flap || 0); c.frontFlap.rotation.x = lerp(0.35, 0.04, st.flap || 0); }
    const P0 = st.pos, at = (fw, sd, y) => P0.clone().addScaledVector(hd, fw).addScaledVector(right, sd).setY(P0.y + y);
    if (st.heat > 0.3) for (const [f, sd] of [[2.1, 1.2], [2.1, -1.2], [-1.8, 1.2], [-1.8, -1.2]]) glow(at(f, sd, 0.45), 1.6 * st.heat, '#ff6a1a', 0.55 * st.heat);
    if (st.cold > 0.3) for (const [f, sd] of [[2.1, 1.2], [2.1, -1.2], [-1.8, 1.2], [-1.8, -1.2]]) glow(at(f, sd, 0.45), 1.4, '#59b4ff', (HQ ? 0.12 : 0.45) * st.cold);
    if (st.brake) for (const sd of [1.1, -1.1]) glow(at(2.1, sd, 0.42), 1.5 + 0.3 * Math.sin(lt * 30), '#ff8a1a', 0.95);
    if (st.energy) for (let j = 0; j < 10; j++) { const u = ((lt * 1.6 + j / 10) % 1), sd = (j % 2 ? 1 : -1) * 1.1 * (1 - u); glow(at(2.1 - u * 2.4, sd, 0.45 + u * 0.4), 0.7 + 0.4 * (1 - u), '#3dff8a', 0.9 * (1 - u * 0.5)); }
    if (st.boost) { glow(at(-3.2, 0, 0.8), 3.2 + 0.6 * Math.sin(lt * 25), '#38bdf8', 0.8 * st.boost); glow(at(0, 0, 0.3), 4.5, '#2563eb', 0.35 * st.boost);
      for (let j = 0; j < 6; j++) { const u = ((lt * 3 + j / 6) % 1); streak(at(3 - u * 9, (j % 2 ? 1.4 : -1.4) + (j % 3 - 1) * 0.3, 0.5 + (j % 3) * 0.3), hd, 2.5, '#7dd3fc', 0.8 * st.boost * (1 - u)); } }
    if (st.flap > 0.05) for (let j = 0; j < 8; j++) { const u = ((lt * 2.2 + j / 8) % 1); streak(at(3 - u * 7, (j - 3.5) * 0.25, 1.5 + (j % 2) * 0.3), hd, 1.6, '#ffffff', 0.45 * st.flap * Math.sin(u * Math.PI)); }
  });
  /* дым: следы недавних заносов */
  for (let j = 0; j < 24; j++) { const age = j * 0.07; if (lt - age < -0.01) break; const past = actStates(shot, lt - age, T - age, dur).cars;
    past.forEach(st => { if (!st.smoke || !st.vis) return; const hd = st.dir.clone().addScaledVector(st.n, st.yaw || 0).normalize(), right = new THREE.Vector3(-hd.z, 0, hd.x);
      for (const sd of [1.2, -1.2]) puff(st.pos.clone().addScaledVector(hd, -1.9).addScaledVector(right, sd + (hashK(j) - 0.5) * 0.8).setY(st.pos.y + 0.5 + age * 1.6), 1.1 + age * 3.4, 0.75 * st.smoke * (1 - age / 1.7)); }); }
  /* механики в боксе */
  const crew = w.crew, cst = ex.crewOf != null ? cars[ex.crewOf] : null;
  crew.group.visible = !!(cst && cst.phase && world.pit && (cst.phase === 'stop' || cst.phase === 'enter' || cst.phase === 'go'));
  if (crew.group.visible) { /* механики стоят у своего бокса: ждут сбоку, подбегают к машине, меняют колёса и уходят обратно */
    const box = pitPose(world.pit.PL * 0.5); pose3(crew.group, box); const side = -(world.pit.away || 1);
    const k = cst.phase === 'stop' ? cst.k : -1, wk = k < 0 ? 0 : k < 0.14 ? easeOut(k / 0.14) : k > 0.86 ? easeOut((1 - k) / 0.14) : 1, walking = wk > 0.02 && wk < 0.98;
    crew.men.forEach((m, i) => { const [sx, sz] = crew.spots[i], wx = side * (4.4 + (i % 2) * 0.9), wz = -3.5 + i * 1.4;
      m.position.set(lerp(wx, sx, wk), walking ? 0.08 * Math.abs(Math.sin(lt * 14 + i)) : (wk > 0.98 ? 0.04 * Math.abs(Math.sin(lt * 9 + i)) : 0), lerp(wz, sz, wk));
      m.children[0].rotation.x = wk > 0.98 ? 0.35 : 0; }); }
  /* такси */
  w.taxis.forEach((t, k) => { const st = ex.taxis?.[k]; t.group.visible = !!st; if (st) { pose3(t.group, st); t.wheels.forEach(wh => wh.rotation.x = st.s / 0.38); } });
  /* люк: крышку вырывает из дороги */
  w.manhole.visible = !!ex.manhole; w.holes.forEach(h => h.visible = false);
  if (ex.manhole) { const m = ex.manhole, p0 = trackPose(m.s, 0.25).pos, t = m.t, d = trackPose(m.s, 0).dir;
    if (t < 0) { w.manhole.position.copy(p0).setY(p0.y + 0.05); w.manhole.rotation.set(0, 0, 0); }
    else { const tt = Math.min(t, 1.75), y = 0.05 + 9 * tt - 5.2 * tt * tt; w.manhole.position.copy(p0).addScaledVector(d, -7 * tt).setY(p0.y + Math.max(0.05, y)); w.manhole.rotation.set(tt * 9, tt * 4, tt * 6);
      w.holes[0].visible = true; w.holes[0].position.copy(p0).setY(p0.y + 0.04);
      if (t < 0.9) for (let j = 0; j < 14; j++) { const r = hashK(j + Math.floor(t * 30) * 17); glow(p0.clone().add(new THREE.Vector3((r - 0.5) * 3, 0.2 + hashK(j * 3 + 1) * 1.6 * (1 - t), (hashK(j * 7) - 0.5) * 3)), 0.5 + r * 0.6, r > 0.5 ? '#ffb347' : '#fff3b0', 1 - t); } } }
  /* сварка люков */
  w.workers.forEach(m => m.visible = false);
  if (ex.weld) for (let j = 0; j < 3; j++) { const pp = trackPose(ex.weld.s + j * 14, [-2.5, 1.5, 3.5][j]).pos; w.holes[j].visible = true; w.holes[j].material.color.set('#3a3d44'); w.holes[j].position.copy(pp).setY(pp.y + 0.04);
    const wk = w.workers[j]; wk.visible = true; wk.position.copy(pp).setY(pp.y).add(new THREE.Vector3(0.9, 0, 0.4)); wk.lookAt(pp.x, pp.y, pp.z);
    if (((lt * 0.9 + j / 3) % 1) < 0.65) { glow(pp.clone().setY(pp.y + 0.15), 1.6 + 0.4 * Math.sin(lt * 40 + j), '#bfe3ff', 0.95); for (let q = 0; q < 9; q++) { const r = hashK(q + j * 31 + Math.floor(lt * 24) * 7); glow(pp.clone().add(new THREE.Vector3((r - 0.5) * 1.6, 0.1 + hashK(q * 5 + j) * 0.9, (hashK(q * 11 + j) - 0.5) * 1.6)), 0.25 + r * 0.3, '#ffb347', 0.9); } } }
  else w.holes.forEach(h => h.material.color.set('#0b0c10'));
  /* штрихи скорости */
  cars.forEach(st => { if (!st.speed || !st.vis) return; const hd = st.dir, right = new THREE.Vector3(-hd.z, 0, hd.x);
    for (let j = 0; j < 10; j++) { const u = ((lt * 3.2 + j / 10) % 1); streak(st.pos.clone().addScaledVector(hd, 6 - u * 16).addScaledVector(right, (j % 2 ? 1 : -1) * (1.6 + (j % 3) * 0.7)).setY(st.pos.y + 0.4 + (j % 4) * 0.35), hd, 3.5, '#ffffff', 0.6 * Math.sin(u * Math.PI)); } });
  /* стены старого города */
  if (ex.castle != null && !w.castle) { const g = new THREE.Group(), mat = new THREE.MeshLambertMaterial({ color: '#c9a46a' }), dark = new THREE.MeshLambertMaterial({ color: '#a8854f' });
    for (let d = -150; d <= 150; d += 3.2) for (const side of [-1, 1]) { const a = w.at(ex.castle + d), o = side * 4.5;
      const b = new THREE.Mesh(new THREE.BoxGeometry(1.4, 7, 3.25), (Math.floor(d / 3.2) % 3 ? mat : dark)); b.position.copy(a.p).addScaledVector(a.n, o).setY(a.p.y + 3.5); b.rotation.y = Math.atan2(a.t.x, a.t.z); g.add(b);
      if (Math.floor(d / 3.2) % 2) { const m2 = new THREE.Mesh(new THREE.BoxGeometry(1.4, 1.2, 1.4), mat); m2.position.copy(b.position).setY(a.p.y + 7.6); m2.rotation.y = b.rotation.y; g.add(m2); } }
    w.castle = g; w.scene.add(g); }
  if (w.castle) w.castle.visible = ex.castle != null;
  /* стройка: блоки и прожекторы появляются вокруг точки фокуса */
  const bmode = shot.build?.walls || 'off', lmode = shot.build?.lights || 'on', tp2 = clamp(lt / dur);
  const fs = shot.build?.focus === 'taxi' ? ex.taxis?.[2]?.s : cars[0]?.vis ? cars[0].s : (shot.act?.at ?? 0.3) * w.L;
  const cd = (s1, s2) => { const d = Math.abs(((s1 - s2) % w.L + w.L) % w.L); return Math.min(d, w.L - d); };
  const B = w.blocks; B.mesh.visible = bmode !== 'off';
  if (bmode === 'grow' || (bmode === 'on' && B.mode !== 'on')) { const R = bmode === 'on' ? 1e9 : lerp(shot.build.R0 ?? 0, shot.build.R ?? 320, ease(tp2)), m4 = new THREE.Matrix4(), q = new THREE.Quaternion(), e = new THREE.Euler(), sc = new THREE.Vector3(), ps = new THREE.Vector3();
    B.base.forEach((b, k) => { const d = cd(b.s, fs ?? 0), vis = d < R, drop = bmode === 'grow' ? clamp((d - R + 12) / 12) * 6 : 0;
      q.setFromEuler(e.set(0, b.yaw, 0)); sc.setScalar(vis ? 1 : 0.0001); m4.compose(ps.set(b.x, b.y + 0.52 + drop, b.z), q, sc); B.mesh.setMatrixAt(k, m4); });
    B.mesh.instanceMatrix.needsUpdate = true; if (B.mesh.instanceColor) B.mesh.instanceColor.needsUpdate = true; }
  B.mode = bmode;
  for (const L0 of w.lightObjs || []) { const v = lmode === 'off' ? false : lmode === 'grow' ? cd(L0.s, fs ?? 0) < lerp(0, shot.build.RL ?? 900, ease(tp2)) : true; L0.objs.forEach(o => o.visible = v); }
  /* машина безопасности */
  w.sc.group.visible = !!ex.sc?.vis; if (ex.sc?.vis) { pose3(w.sc.group, ex.sc); const on = ex.sc.lights; w.sc.lights.forEach((l, i) => { l.visible = on; l.material.opacity = (Math.sin(lt * 14 + i * Math.PI) > 0) ? 1 : 0.15; }); }
  /* мотоциклы и стоковые машины */
  w.pack.forEach((b, k) => { const st = ex.pack?.[k]; b.group.visible = !!st; if (st) pose3(b.group, st); });
  w.bikes.forEach((b, k) => { const st = ex.bikes?.[k]; b.group.visible = !!st; if (!st) return; pose3(b.group, st); const i = w.at(st.s).i; b.lean.rotation.z = clamp(w.curv[i] * 4, -0.75, 0.75); /* мотоцикл наклоняется внутрь поворота */ b.wheels.forEach(wh => wh.rotation.x = st.s / 0.36); });
  w.stock.forEach((b, k) => { const st = ex.stock?.[k]; b.group.visible = !!st; if (st) pose3(b.group, st); });
  /* линия замера */
  w.det.visible = ex.det != null; if (w.det.visible) { const a = w.at(ex.det); w.det.position.copy(a.p).setY(a.p.y + 0.1); w.det.rotation.set(-Math.PI / 2, 0, Math.atan2(a.t.x, a.t.z) + Math.PI / 2); w.det.material.opacity = 0.6 + 0.35 * Math.sin(lt * 8); }
  /* метки для вида сверху со шлейфом */
  if (ex.markers) { const sz = Math.max(w.size.x, w.size.z) * 0.085;
    for (const m of ex.markers) { const st = cars[m.k];
      for (let j = 22; j >= 1; j--) { const ps = actStates(shot, lt - j * 0.05, T - j * 0.05, dur).cars[m.k]; glow(ps.pos.clone().setY(ps.pos.y + 29), sz * (1.5 - j * 0.045), m.color, 0.85 * (1 - j / 23), true); }
      glow(st.pos.clone().setY(st.pos.y + 30), sz * (2.6 + 0.3 * Math.sin(lt * 6)), m.color, 0.9, true); disc(st.pos.clone().setY(st.pos.y + 32), sz * 0.85, m.color); } }
  if (shot.rain) rainSpray(w, shot, lt);
  fxEnd();
  if (shot.sphere || shot.neon || w.vx) vegasExtras(w, shot, lt);
  if (shot.trophy || w.vtr) trackTrophy(w, shot, lt);
  w.lastEx = ex;
  return { cars, ex };
}

// ---------- камера ----------
function placeCamera(cam, shot, u, T, sc, lt) {
  const w = world; cam.up.set(0, 1, 0); if (cam.near !== 0.5) cam.near = 0.5;
  if (shot.type === 'chase') {
    const c = w.cars[shot.car ?? 0], st = (shot.follow === 'bike' && w.lastEx?.bikes?.[shot.fi ?? 1]) || (shot.follow === 'stock' && w.lastEx?.pack?.[shot.fi ?? 0]) || (shot.follow === 'taxi' && w.lastEx?.taxis?.[2]) || (shot.follow === 'focus' && w.lastEx?.focus) || c.st || trackPose(c.s0 + c.v * T, 0), onPit = st.phase === 'enter' || st.phase === 'stop' || st.phase === 'go';
    const d = lerp(shot.dist ?? 14, shot.dist2 ?? shot.dist ?? 14, ease(u)), h = lerp(shot.h ?? 4, shot.h2 ?? shot.h ?? 4, ease(u)), side = lerp(shot.side ?? 0, shot.side2 ?? shot.side ?? 0, ease(u)) * (shot.autoSide && w.pit ? -w.pit.away * Math.sign(shot.side || 1) * Math.sign(shot.side || 1) : 1);
    /* направление камеры сглаживаем по отрезку трассы позади машины: на извилистых трассах касательная прыгает от точки к точке и кадр трясётся */
    let dir = st.dir; if (!onPit && !shot.follow && Number.isFinite(st.s)) { const p0 = w.at(st.s - Math.max(8, d)).p, p1 = w.at(st.s + 6).p; dir = p1.clone().sub(p0).setY(0); dir = dir.lengthSq() > 1 ? dir.normalize() : st.dir; }
    const nn = new THREE.Vector3(-dir.z, 0, dir.x);
    cam.position.copy(st.pos).addScaledVector(dir, -d).addScaledVector(nn, side).setY(st.pos.y + h);
    const lk = onPit ? st.pos.clone().addScaledVector(st.dir, (shot.look ?? 30) * 0.45) : st.pos.clone().lerp(w.at(st.s + (shot.look ?? 30)).p, 0.45); cam.lookAt(lk.x, lk.y + 1 - (shot.drop ?? 1.2) * 0.5, lk.z); /* машина всегда в кадре */ cam.fov = shot.fov ?? 50;
  } else if (shot.type === 'fly') {
    const s = lerp(shot.from, shot.to, ease(u)) * w.L, a = w.at(s), ah = w.at(s + (shot.ahead ?? 160));
    cam.position.copy(a.p).addScaledVector(a.n, shot.side ?? 0).setY(a.p.y + lerp(shot.h ?? 80, shot.h2 ?? shot.h ?? 80, ease(u)));
    cam.lookAt(ah.p.x, ah.p.y, ah.p.z); cam.fov = shot.fov ?? 55;
  } else if (shot.type === 'orbit') {
    let tgt = shot.at != null ? w.at(shot.at * w.L).p : new THREE.Vector3(0, 0, 0);
    if (shot.at != null && shot.tside) { const q = w.at(shot.at * w.L); tgt = q.p.clone().addScaledVector(q.n, shot.tside); }   /* tside: центр облёта сбоку от трассы (м), ly: высота взгляда */
    const a = lerp(shot.a0 ?? 0, shot.a1 ?? 0.6, ease(u)), r = lerp(shot.r ?? 900, shot.r2 ?? shot.r ?? 900, ease(u)), h = lerp(shot.h ?? 500, shot.h2 ?? shot.h ?? 500, ease(u));
    cam.position.set(tgt.x + Math.cos(a) * r, h, tgt.z + Math.sin(a) * r); cam.lookAt(tgt.x, shot.ly ?? 0, tgt.z); cam.fov = shot.fov ?? 50;
  } else if (shot.type === 'top') {
    // сверху, трасса целиком в вертикальном кадре; лёгкий наклон и поворот для «живости»
    const f = w.fit, vf = 40 * Math.PI / 180, hf = 2 * Math.atan(Math.tan(vf / 2) * W / H);
    const h = Math.max(f.ex / 2 / Math.tan(hf / 2), f.ez / 2 / Math.tan(vf / 2)) * (shot.k ?? 1.15);
    const rot = f.a + lerp(shot.rot0 ?? 0, shot.rot1 ?? 0.15, ease(u)), tilt = shot.tilt ?? 0.18;
    const c = Math.cos(f.a), s2 = Math.sin(f.a), cx = f.cx * c + f.cz * s2, cz = -f.cx * s2 + f.cz * c; // центр рамки в мировых координатах
    const fwd = new THREE.Vector3(-Math.sin(rot), 0, -Math.cos(rot));
    cam.position.set(cx - fwd.x * h * tilt, h, cz - fwd.z * h * tilt); cam.up.copy(fwd); cam.lookAt(cx, 0, cz); cam.fov = 40;
  } else if (shot.type === 'side' || shot.type === 'onboard' || shot.type === 'carorbit' || shot.type === 'flyby') hqCamera(cam, shot, u, T, sc, lt);
  cam.updateProjectionMatrix();
}

// ---------- 2D-слой: текст, субтитры, логотип ----------
const font = (wgt, px) => `${wgt} ${px}px Inter, "Noto Sans CJK SC", "Noto Sans SC", sans-serif`;
const CJK = /[\u3000-\u9fff\uff00-\uffef]/;
const toks = text => CJK.test(text) ? String(text).replace(/\s+/g, '').match(/[\u3000-\u9fff][，。！？、：；）」』]?|[^\u3000-\u9fff]+?(?=[\u3000-\u9fff]|$)/g) || [] : String(text).split(/\s+/).filter(Boolean);
const sepOf = text => CJK.test(text) ? '' : ' ';
function wrap(g, text, maxW) { const words = toks(text), sp = sepOf(text), lines = []; let cur = ''; for (const w of words) { const t = cur ? cur + sp + w : w; if (g.measureText(t).width > maxW && cur) { lines.push(cur); cur = w; } else cur = t; } if (cur) lines.push(cur); return lines; }
function rrect(g, x, y, w, h, r) { g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath(); }
const LOGO_ARC = new Path2D('M7 25C7 15 13 9 25 7');
function logo(g, x, y, s) { // логотип точно как на сайте (public/js/icons.js LOGO): квадрат 32×32, дуга и точка
  g.save(); g.translate(x, y); g.scale(s * 2, s * 2); rrect(g, 0, 0, 32, 32, 7); g.fillStyle = '#3478f6'; g.fill();
  g.strokeStyle = '#fff'; g.lineWidth = 3.4; g.lineCap = 'round'; g.stroke(LOGO_ARC); g.beginPath(); g.arc(15.6, 16.6, 2.5, 0, 7); g.fillStyle = '#fff'; g.fill(); g.restore();
}
function brand(g) { logo(g, 60, 70, 1.05); g.font = font(900, 46); g.fillStyle = '#fff'; g.textBaseline = 'middle'; g.fillText('LAPRADAR', 142, 105); }
function shade(g, top = true, bottom = true) {
  if (top) { const gr = g.createLinearGradient(0, 0, 0, 760); gr.addColorStop(0, 'rgba(0,0,0,0.72)'); gr.addColorStop(1, 'rgba(0,0,0,0)'); g.fillStyle = gr; g.fillRect(0, 0, W, 760); }
  if (bottom) { const gr = g.createLinearGradient(0, 1150, 0, H); gr.addColorStop(0, 'rgba(0,0,0,0)'); gr.addColorStop(1, 'rgba(0,0,0,0.7)'); g.fillStyle = gr; g.fillRect(0, 1150, W, H - 1150); }
}
function popText(g, text, cx, y, px, lt, { color = '#fff', wgt = 900, maxW = 920, stagger = 0.09, align = 'center', accent } = {}) {
  g.font = font(wgt, px); const lines = wrap(g, text, maxW); let wi = 0;
  const sp = sepOf(text);
  lines.forEach((ln, li) => {
    const words = sp ? ln.split(' ') : toks(ln), widths = words.map(w => g.measureText(w + sp).width), total = widths.reduce((a, b) => a + b, 0) - (sp ? g.measureText(' ').width : 0);
    let x = align === 'center' ? cx - total / 2 : cx;
    words.forEach((w, k) => {
      const t = (lt - wi * stagger) / 0.38, sc = back(t), al = clamp(t * 2.5);
      if (al > 0) { const ww = g.measureText(w).width; g.save(); g.globalAlpha = al; g.translate(x + ww / 2, y + li * px * 1.08); g.scale(sc, sc); g.translate(-ww / 2, 0);
        g.lineWidth = px * 0.12; g.strokeStyle = 'rgba(0,0,0,0.55)'; g.lineJoin = 'round'; g.textBaseline = 'middle'; g.strokeText(w, 0, 0);
        g.fillStyle = accent && accent.test(w) ? '#ffd23f' : color; g.fillText(w, 0, 0); g.restore(); }
      x += widths[k]; wi++;
    });
  });
  return lines.length * px * 1.08;
}
function countUp(text, p) { // «≈5,4 км» → число растёт от нуля
  const m = String(text).match(/^(\D*)(\d+(?:[.,]\d+)?)(.*)$/); if (!m) return text;
  const dec = (m[2].split(/[.,]/)[1] || '').length, sep = m[2].includes(',') ? ',' : '.'; const v = parseFloat(m[2].replace(',', '.')) * easeOut(p);
  return m[1] + v.toFixed(dec).replace('.', sep) + m[3];
}
function captions(g, say, lt, dur) { // субтитры по словам, текущая фраза снизу, текущее слово жёлтым
  const words = toks(String(say || '')), sp = sepOf(String(say || '')); if (!words.length) return;
  const t0 = 0.15, t1 = Math.max(t0 + 0.5, dur - 0.45), wts = words.map(w => w.length + 2), tot = wts.reduce((a, b) => a + b, 0);
  let acc = 0; const times = wts.map(x => { const s = t0 + (t1 - t0) * acc / tot; acc += x; return s; });
  let cur = 0; for (let i = 0; i < words.length; i++) if (lt >= times[i]) cur = i;
  // фраза: группы по 3–5 слов
  const groups = []; let gcur = []; for (let i = 0; i < words.length; i++) { gcur.push(i); const w = words[i]; const nx = words[i + 1] || ''; const lim = sp ? 4 : 11; if ((sp && gcur.length >= lim && w.length > 2) || gcur.length >= (sp ? 6 : 14) || /[.,!?:;，。！？：；]$/.test(w) && gcur.length >= 2) { if (nx || true) { groups.push(gcur); gcur = []; } } } if (gcur.length) groups.push(gcur);
  const grp = groups.find(gr => gr.includes(cur)) || groups[0];
  g.font = font(900, 70); const line = grp.map(i => words[i]).join(sp); const lines = wrap(g, line, 900);
  const gStart = times[grp[0]], pop = back((lt - gStart) / 0.25);
  let y = 1390 - (lines.length - 1) * 40;
  let wi = 0;
  for (const ln of lines) {
    const ws = sp ? ln.split(' ') : toks(ln), widths = ws.map(w => g.measureText(w + sp).width), total = widths.reduce((a, b) => a + b, 0) - (sp ? g.measureText(' ').width : 0); let x = W / 2 - total / 2 - 30;
    ws.forEach((w, k) => { const idx = grp[wi]; g.save(); g.translate(x + widths[k] / 2, y); const sc = 0.85 + 0.15 * pop; g.scale(sc, sc); g.translate(-widths[k] / 2, 0);
      g.lineWidth = 14; g.lineJoin = 'round'; g.strokeStyle = '#000'; g.textBaseline = 'middle'; g.strokeText(w, 0, 0);
      g.fillStyle = idx === cur ? '#ffd23f' : idx < cur ? '#ffffff' : 'rgba(255,255,255,0.92)'; g.fillText(w, 0, 0); g.restore(); x += widths[k]; wi++; });
    y += 82;
  }
}

/* ---------- стиль TikTok: короткие фразы по 1–3 слова в одну строку, ключевые слова в жёлтой плашке ---------- */
const TT = () => (spec?.style || 'tt') === 'tt';
function captionsTT(g, say, lt, dur, hl, y = 1180) {
  const words = toks(String(say || '')), sp = sepOf(String(say || '')); if (!words.length) return;
  const t0 = 0.12, t1 = Math.max(t0 + 0.5, dur - 0.35), wts = words.map(w => w.length + 2), tot = wts.reduce((a, b) => a + b, 0);
  let acc = 0; const times = wts.map(x => { const s0 = t0 + (t1 - t0) * acc / tot; acc += x; return s0; });
  const groups = []; let gc = [], len = 0;
  for (let i = 0; i < words.length; i++) { gc.push(i); len += words[i].length; const w = words[i];
    const cut = sp ? (gc.length >= 3 || len > 13 || /[.,!?:;—]$/.test(w)) : (len >= 8 || /[，。！？：；、]$/.test(w));
    if (cut) { groups.push(gc); gc = []; len = 0; } }
  if (gc.length) groups.push(gc);
  let gi = 0; for (let k = 0; k < groups.length; k++) if (lt >= times[groups[k][0]] - 0.02) gi = k;
  const grp = groups[gi], st = times[grp[0]], pop = back((lt - st) / 0.18), clean = w => w.replace(/[.,!?:;，。！？：；、]+$/, '');
  const NUMW = /^(один|одна|одно|одного|два|две|двух|три|трёх|трех|четыре|четырёх|пять|пяти|шесть|шести|семь|семи|восемь|восьми|девять|девяти|десять|десяти|[а-я]*надцат[а-я]*|двадцат[а-я]*|тридцат[а-я]*|сорок[а-я]*|пятьдесят|шестьдесят|семьдесят|восемьдесят|девяност[а-я]*|сто|двести|триста|тысяч[а-я]*|миллион[а-я]*|полтор[а-я]*|перв(ый|ая|ое|ого|ой|ом|ые|ых|ую)|втор(ой|ая|ое|ого|ом|ую)|трет(ий|ья|ье|ьего|ьем|ью)|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|[a-z]+teen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|first|second|third|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|veinte|treinta|cien|mil|duas|quatro|sete|oito|nove|dez|vinte|trinta|zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|zwanzig|dreißig|hundert|tausend)$/i;
  const isHl = w => /\d/.test(w) || (sp && NUMW.test(clean(w))) || (hl || []).some(h => clean(w).toLowerCase() === String(h).toLowerCase());
  let px = 88; g.font = font(900, px); const parts = grp.map(i => clean(words[i]) || words[i]);
  const meas = () => parts.map(w => g.measureText(w).width + (isHl(w) ? 44 : 0)); let ws = meas(), gap = sp ? px * 0.28 : 6, total = ws.reduce((a, b) => a + b, 0) + gap * (parts.length - 1);
  while (total > W - 120 && px > 50) { px -= 4; g.font = font(900, px); ws = meas(); gap = sp ? px * 0.28 : 6; total = ws.reduce((a, b) => a + b, 0) + gap * (parts.length - 1); }
  g.save(); g.translate(W / 2, y); const k = 0.8 + 0.2 * pop; g.scale(k, k); let x = -total / 2;
  parts.forEach((w, j) => { const ww = ws[j]; g.textBaseline = 'middle';
    if (isHl(w)) { g.save(); g.translate(x + ww / 2, 0); g.rotate(-0.035); rrect(g, -ww / 2, -px * 0.62, ww, px * 1.24, px * 0.28); g.fillStyle = '#ffd23f'; g.fill(); g.fillStyle = '#0b1020'; g.textAlign = 'center'; g.fillText(w, 0, px * 0.04); g.restore(); }
    else { g.lineWidth = px * 0.2; g.lineJoin = 'round'; g.strokeStyle = 'rgba(0,0,0,0.85)'; g.strokeText(w, x, 0); g.fillStyle = '#fff'; g.fillText(w, x, 0); }
    x += ww + gap; });
  g.restore(); g.textAlign = 'left'; g.textBaseline = 'alphabetic';
}
function brandTT(g) { g.save(); g.font = font(800, 30); const t = 'LapRadar · lapradar.com', tw = g.measureText(t).width, w = tw + 84, x = (W - w) / 2, y = 54;
  rrect(g, x, y, w, 56, 28); g.fillStyle = 'rgba(8,12,22,0.55)'; g.fill(); logo(g, x + 12, y + 8, 0.62); g.fillStyle = 'rgba(255,255,255,0.9)'; g.textBaseline = 'middle'; g.fillText(t, x + 62, y + 29); g.restore(); }
function endTT(g, sc, lt) {
  hudPhone(g, lt, sc.dur, 'map', sc.fx);
  const a = back((lt - 0.5) / 0.4); if (a <= 0) return; g.save(); g.translate(W / 2, 1400); g.scale(a, a);
  g.font = font(800, 46); const t = 'lapradar.com', tw = g.measureText(t).width, w = tw + 150; rrect(g, -w / 2, -48, w, 96, 48); g.fillStyle = '#fff'; g.fill();
  g.strokeStyle = '#0b1020'; g.lineWidth = 7; g.beginPath(); g.arc(-w / 2 + 52, -4, 17, 0, 7); g.stroke(); g.beginPath(); g.moveTo(-w / 2 + 64, 9); g.lineTo(-w / 2 + 78, 23); g.stroke();
  g.fillStyle = '#0b1020'; g.textBaseline = 'middle'; g.fillText(t, -w / 2 + 100, 2); g.restore();
}

function itemsCard(g, items, lt, y0) {
  items.forEach((it, i) => {
    const t = easeOut((lt - 0.25 - i * 0.55) / 0.45); if (t <= 0) return;
    const y = y0 + i * 140, x = lerp(-900, 80, t);
    g.save(); g.globalAlpha = clamp(t * 1.5); rrect(g, x, y, 840, 112, 30); g.fillStyle = 'rgba(10,14,24,0.82)'; g.fill(); g.lineWidth = 3; g.strokeStyle = 'rgba(91,155,255,0.6)'; g.stroke();
    g.beginPath(); g.arc(x + 62, y + 56, 30, 0, 7); g.fillStyle = '#3b82f6'; g.fill(); g.strokeStyle = '#fff'; g.lineWidth = 7; g.lineCap = 'round'; g.beginPath(); g.moveTo(x + 48, y + 57); g.lineTo(x + 59, y + 68); g.lineTo(x + 77, y + 45); g.stroke();
    let px = 52; g.font = font(800, px); while (g.measureText(it).width > 690 && px > 34) { px -= 2; g.font = font(800, px); } g.fillStyle = '#fff'; g.textBaseline = 'middle'; g.fillText(it, x + 116, y + 58); g.restore();
  });
}
function wearBar(g, lt, dur, laps) { // счётчик кругов и износ шины
  const p = clamp((lt - 0.4) / Math.max(1, dur - 1.2)); const lap = Math.max(1, Math.round(p * laps));
  const Y = 330; g.save(); rrect(g, 140, Y, 800, 150, 34); g.fillStyle = 'rgba(10,14,24,0.85)'; g.fill();
  g.font = font(900, 64); g.fillStyle = '#fff'; g.textBaseline = 'middle'; g.fillText(`${lap} / ${laps}`, 180, Y + 50);
  rrect(g, 180, Y + 98, 720, 26, 13); g.fillStyle = '#2a3142'; g.fill();
  const w = 720 * (1 - p * 0.92); rrect(g, 180, Y + 98, Math.max(26, w), 26, 13); g.fillStyle = p > 0.75 ? '#ef3b3b' : p > 0.45 ? '#ffd23f' : '#22c55e'; g.fill(); g.restore();
}


/* ---------- индикаторы вместо текста: секундомер, круги, термометр, батарея, мини-трассы, телефон ---------- */
function hudPanel(g, x, y, w, h) { rrect(g, x, y, w, h, 40); g.fillStyle = 'rgba(8,12,22,0.78)'; g.fill(); g.lineWidth = 3; g.strokeStyle = 'rgba(91,155,255,0.45)'; g.stroke(); }
function hudStopwatch(g, lt, dur, to) {
  const p = clamp((lt - 0.3) / Math.max(1, dur - 0.9)), cx = W / 2, cy = 400, r = 118, a = back(lt / 0.5);
  g.save(); g.translate(cx, cy); g.scale(a, a);
  g.beginPath(); g.arc(0, 0, r + 26, 0, 7); g.fillStyle = 'rgba(8,12,22,0.8)'; g.fill();
  g.fillStyle = '#e5e7eb'; rrect(g, -22, -r - 58, 44, 30, 8); g.fill();
  g.lineWidth = 16; g.strokeStyle = '#2a3142'; g.beginPath(); g.arc(0, 0, r, 0, 7); g.stroke();
  g.strokeStyle = p > 0.8 ? '#ef4444' : '#ffd23f'; g.lineCap = 'round'; g.beginPath(); g.arc(0, 0, r, -Math.PI / 2, -Math.PI / 2 + p * Math.PI * 2); g.stroke();
  g.rotate(p * Math.PI * 2 * 3); g.strokeStyle = '#fff'; g.lineWidth = 7; g.beginPath(); g.moveTo(0, 12); g.lineTo(0, -r + 26); g.stroke(); g.rotate(-p * Math.PI * 2 * 3);
  g.font = font(900, 64); g.fillStyle = '#fff'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText((to * p).toFixed(1) + ' s', 0, r + 90 - 6); g.restore(); g.textAlign = 'left';
}
function hudLaps(g, lt, dur, n) {
  const p = clamp((lt - 0.3) / Math.max(1, dur - 0.9)), lap = Math.max(1, Math.round(p * n)), cx = W / 2, cy = 400, r = 120, a = back(lt / 0.5);
  g.save(); g.translate(cx, cy); g.scale(a, a); g.beginPath(); g.arc(0, 0, r + 30, 0, 7); g.fillStyle = 'rgba(8,12,22,0.8)'; g.fill();
  for (let i = 0; i < n; i++) { const a0 = -Math.PI / 2 + i / n * Math.PI * 2 + 0.03, a1 = -Math.PI / 2 + (i + 1) / n * Math.PI * 2 - 0.03; g.lineWidth = 22; g.lineCap = 'butt'; g.strokeStyle = i < lap ? (i / n > 0.75 ? '#ef4444' : i / n > 0.45 ? '#ffd23f' : '#22c55e') : '#2a3142'; g.beginPath(); g.arc(0, 0, r, a0, a1); g.stroke(); }
  g.font = font(900, 92); g.fillStyle = '#fff'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(String(lap), 0, -8); g.font = font(800, 34); g.fillStyle = '#9fb0d0'; g.fillText('/ ' + n, 0, 52); g.restore(); g.textAlign = 'left';
}
function hudThermo(g, lt, dur, from, to) {
  const p = easeOut((lt - 0.3) / 1.6), v = Math.round(lerp(from, to, p)), x = W / 2 - 150, y = 250, a = back(lt / 0.5);
  g.save(); g.translate(W / 2, 400); g.scale(a, a); g.translate(-W / 2, -400); hudPanel(g, x, y, 300, 300);
  rrect(g, x + 62, y + 40, 36, 170, 18); g.fillStyle = '#2a3142'; g.fill(); g.beginPath(); g.arc(x + 80, y + 236, 34, 0, 7); g.fillStyle = '#38bdf8'; g.fill();
  const hh = 160 * clamp((v - 0) / 35); rrect(g, x + 68, y + 205 - hh, 24, hh + 20, 12); g.fill();
  g.font = font(900, 84); g.fillStyle = '#7dd3fc'; g.textBaseline = 'middle'; g.fillText(v + '°', x + 128, y + 150); g.restore();
}
function hudBattery(g, lt, level) {
  const x = W / 2 - 170, y = 300, a = back(lt / 0.5); g.save(); g.translate(W / 2, 400); g.scale(a, a); g.translate(-W / 2, -400);
  hudPanel(g, x - 20, y - 20, 380, 200); rrect(g, x + 10, y + 30, 290, 120, 22); g.lineWidth = 10; g.strokeStyle = '#e5e7eb'; g.stroke(); rrect(g, x + 300, y + 66, 24, 48, 8); g.fillStyle = '#e5e7eb'; g.fill();
  rrect(g, x + 24, y + 44, 262 * clamp(level), 92, 12); g.fillStyle = level > 0.6 ? '#3dff8a' : '#ffd23f'; g.fill();
  g.fillStyle = '#0b1020'; g.beginPath(); g.moveTo(x + 165, y + 50); g.lineTo(x + 130, y + 98); g.lineTo(x + 158, y + 98); g.lineTo(x + 145, y + 132); g.lineTo(x + 185, y + 80); g.lineTo(x + 157, y + 80); g.closePath(); g.fill(); g.restore();
}
const MINI = {};
async function loadMini(names) { for (const n of names) if (!MINI[n]) { try { const t = await (await fetch(`tracks/${n}.json`)).json(); MINI[n] = t.pts.map(p => [p[0], -p[1]]); } catch { MINI[n] = []; } } }
function drawOutline(g, pts, cx, cy, size, prog, color, lw = 10) {
  if (!pts?.length) return; let x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9; for (const [x, y] of pts) { x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y); }
  const k = size / Math.max(x1 - x0, y1 - y0), n = Math.max(2, Math.floor(pts.length * clamp(prog)));
  g.save(); g.lineJoin = g.lineCap = 'round'; g.beginPath(); for (let i = 0; i <= n; i++) { const [x, y] = pts[i % pts.length]; const X = cx + (x - (x0 + x1) / 2) * k, Y = cy + (y - (y0 + y1) / 2) * k; i ? g.lineTo(X, Y) : g.moveTo(X, Y); }
  g.strokeStyle = 'rgba(0,0,0,0.6)'; g.lineWidth = lw + 8; g.stroke(); g.strokeStyle = color; g.lineWidth = lw; g.shadowColor = color; g.shadowBlur = 24; g.stroke(); g.restore();
}
function tyreIcon(g, x, y, r, color) { g.beginPath(); g.arc(x, y, r, 0, 7); g.fillStyle = '#16181d'; g.fill(); g.lineWidth = r * 0.16; g.strokeStyle = color; g.beginPath(); g.arc(x, y, r * 0.72, 0, 7); g.stroke(); g.beginPath(); g.arc(x, y, r * 0.42, 0, 7); g.fillStyle = '#9aa1ad'; g.fill(); }
function hudTracks(g, lt, dur, names, good) {
  g.fillStyle = 'rgba(4,7,14,0.5)'; g.fillRect(-3000, -3000, 9000, 9000);
  names.forEach((n, i) => { const t0 = 0.3 + i * (dur - 1.2) / names.length, p = clamp((lt - t0) / 0.9), y = 470 + i * 290, a = easeOut((lt - t0) / 0.4); if (a <= 0) return;
    g.save(); g.globalAlpha = a; hudPanel(g, 150, y - 120, 780, 240); drawOutline(g, MINI[n], 380, y, 200, p, good ? '#ff4d4d' : '#ff8a1a', 9);
    tyreIcon(g, 690, y, 70, '#ef3b3b'); g.lineWidth = 16; g.lineCap = 'round'; g.strokeStyle = good ? '#22c55e' : '#ef4444'; g.beginPath();
    if (good) { g.moveTo(800, y); g.lineTo(830, y + 32); g.lineTo(880, y - 34); } else { g.moveTo(800, y - 30); g.lineTo(866, y + 34); g.moveTo(866, y - 30); g.lineTo(800, y + 34); }
    g.globalAlpha = a * easeOut((lt - t0 - 0.5) / 0.3); g.stroke(); g.restore(); });
}
function hudFrost(g, lt) { const r = rng(5); g.save(); const gr = g.createRadialGradient(W / 2, H / 2, H * 0.3, W / 2, H / 2, H * 0.75); gr.addColorStop(0, 'rgba(120,190,255,0)'); gr.addColorStop(1, 'rgba(120,190,255,0.35)'); g.fillStyle = gr; g.fillRect(0, 0, W, H);
  for (let i = 0; i < 90; i++) { const x = (r() * W + Math.sin(lt * 0.7 + i) * 30) % W, y = (r() * H + lt * (40 + r() * 60)) % H, s = 2 + r() * 4; g.globalAlpha = 0.5 + 0.5 * Math.sin(lt * 3 + i); g.fillStyle = '#eaf6ff'; g.beginPath(); g.arc(x, y, s, 0, 7); g.fill(); } g.restore(); }
/* телефон с приложением: карта, таблица, повтор, чемпионат */
function hudPhone(g, lt, dur, mode, fx) {
  const pw = 540, ph = 1040, x = (W - pw) / 2, y = 240 + (1 - easeOut(lt / 0.6)) * 900;
  g.fillStyle = `rgba(4,7,14,${0.45 * clamp(lt * 2)})`; g.fillRect(-3000, -3000, 9000, 9000);
  g.save(); g.shadowColor = 'rgba(0,0,0,0.6)'; g.shadowBlur = 50; rrect(g, x, y, pw, ph, 70); g.fillStyle = '#0a0c12'; g.fill(); g.restore();
  rrect(g, x + 16, y + 16, pw - 32, ph - 32, 56); g.save(); g.clip(); g.fillStyle = '#0b1020'; g.fillRect(x, y, pw, ph);
  const sx = x + 16, sy = y + 16, sw = pw - 32, shh = ph - 32, w = world, cars = fx?.cars || [];
  rrect(g, sx + sw / 2 - 70, sy + 14, 140, 34, 17); g.fillStyle = '#000'; g.fill();
  logo(g, sx + 28, sy + 70, 0.6); g.font = font(900, 30); g.fillStyle = '#fff'; g.textBaseline = 'middle'; g.fillText('LAPRADAR', sx + 76, sy + 90);
  const map = (cx, cy, size, rot, prog = 1) => { const pts = w.P.filter((_, i) => i % 3 === 0).map(p => [p.x, p.z]); const c = Math.cos(rot), s = Math.sin(rot);
    let x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9; const R = pts.map(([px, pz]) => { const X = px * c - pz * s, Y = px * s + pz * c; x0 = Math.min(x0, X); x1 = Math.max(x1, X); y0 = Math.min(y0, Y); y1 = Math.max(y1, Y); return [X, Y]; });
    const k = size / Math.max(x1 - x0, y1 - y0), tx = (X, Y) => [cx + (X - (x0 + x1) / 2) * k, cy + (Y - (y0 + y1) / 2) * k];
    g.lineJoin = 'round'; g.beginPath(); R.forEach(([X, Y], i) => { const [a, b] = tx(X, Y); i ? g.lineTo(a, b) : g.moveTo(a, b); }); g.closePath(); g.strokeStyle = '#2b3550'; g.lineWidth = 22; g.stroke(); g.strokeStyle = '#5b9bff'; g.lineWidth = 6; g.stroke();
    return (p3, col, r = 11, hi) => { const X = p3.x * c - p3.z * s, Y = p3.x * s + p3.z * c, [a, b] = tx(X, Y); if (hi) { g.beginPath(); g.arc(a, b, r + 10 + 6 * Math.sin(lt * 8), 0, 7); g.fillStyle = 'rgba(255,210,63,0.35)'; g.fill(); } g.beginPath(); g.arc(a, b, r, 0, 7); g.fillStyle = col; g.fill(); g.lineWidth = 3; g.strokeStyle = '#fff'; g.stroke(); return [a, b]; }; };
  const rows = (top, n, hi) => { for (let i = 0; i < n; i++) { const yy = top + i * 62, a = easeOut((lt - 0.5 - i * 0.08) / 0.3); if (a <= 0) continue; g.globalAlpha = a; rrect(g, sx + 20, yy, sw - 40, 52, 14); g.fillStyle = i === hi ? 'rgba(255,210,63,0.22)' : 'rgba(255,255,255,0.05)'; g.fill();
    g.font = font(800, 26); g.fillStyle = '#9fb0d0'; g.fillText(String(i + 1), sx + 38, yy + 27); rrect(g, sx + 76, yy + 12, 8, 28, 4); g.fillStyle = CAR_COLORS[i % CAR_COLORS.length]; g.fill();
    rrect(g, sx + 100, yy + 16, 120 + (i * 37 % 60), 20, 10); g.fillStyle = '#e5e7eb'; g.fill(); g.font = font(700, 24); g.fillStyle = '#cfd8ff'; g.fillText(i ? '+' + (i * 1.37 + 0.4).toFixed(1) : '—', sx + 290, yy + 27);
    tyreIcon(g, sx + sw - 120, yy + 26, 17, [TYRE.soft, TYRE.medium, TYRE.hard][i % 3]); g.font = font(700, 22); g.fillStyle = '#9fb0d0'; g.fillText(String(3 + (i * 7) % 18), sx + sw - 92, yy + 27); } g.globalAlpha = 1; };
  if (mode === 'map' || mode === 'replay') {
    const dot = map(sx + sw / 2, sy + 360, sw - 70, mode === 'map' ? lt * 0.25 : 0.3);
    cars.slice(0, 8).forEach((st, k) => st.vis && dot(st.pos, CAR_COLORS[k % CAR_COLORS.length], 12, k === 0 && mode === 'map'));
    if (mode === 'map') { const b = w.corners.slice(0, 12); b.forEach((c, i) => { if (lt < 1 + i * 0.15) return; }); rows(sy + 640, 5, -1); }
    else { const ty = sy + 700, p = (lt / dur) % 1; rrect(g, sx + 40, ty, sw - 80, 12, 6); g.fillStyle = '#2a3142'; g.fill(); rrect(g, sx + 40, ty, (sw - 80) * p, 12, 6); g.fillStyle = '#3b82f6'; g.fill(); g.beginPath(); g.arc(sx + 40 + (sw - 80) * p, ty + 6, 18, 0, 7); g.fillStyle = '#fff'; g.fill();
      g.beginPath(); g.arc(sx + sw / 2, ty + 120, 52, 0, 7); g.fillStyle = '#3b82f6'; g.fill(); g.fillStyle = '#fff'; g.beginPath(); g.moveTo(sx + sw / 2 - 16, ty + 92); g.lineTo(sx + sw / 2 + 26, ty + 120); g.lineTo(sx + sw / 2 - 16, ty + 148); g.fill();
      ['2023', '2024', '2025', '2026'].forEach((yr, i) => { const a = easeOut((lt - 0.3 - i * 0.15) / 0.3); g.globalAlpha = a; rrect(g, sx + 30 + i * 118, ty + 210, 106, 50, 25); g.fillStyle = i === 0 ? '#ffd23f' : 'rgba(255,255,255,0.1)'; g.fill(); g.font = font(800, 24); g.fillStyle = i === 0 ? '#0b1020' : '#fff'; g.textAlign = 'center'; g.fillText(yr, sx + 83 + i * 118, ty + 236); g.textAlign = 'left'; }); g.globalAlpha = 1; }
  } else if (mode === 'table') {
    const hi = lt > dur * 0.45 ? 2 : -1, dot = map(sx + sw / 2, sy + 280, sw - 160, 0.4); cars.slice(0, 8).forEach((st, k) => st.vis && dot(st.pos, CAR_COLORS[k % CAR_COLORS.length], 10, k === 2 && hi === 2));
    rows(sy + 500, 8, hi); if (lt > dur * 0.4 && lt < dur * 0.6) { const r = (lt - dur * 0.4) / (dur * 0.2); g.beginPath(); g.arc(sx + sw / 2, sy + 500 + 2 * 62 + 26, 20 + r * 80, 0, 7); g.strokeStyle = `rgba(255,255,255,${1 - r})`; g.lineWidth = 6; g.stroke(); }
  } else if (mode === 'champ') {
    const pts = [380, 344, 310, 270, 241, 198, 170, 133], ord = pts.map((p, i) => p + (i === 1 ? 50 * clamp((lt - 1.2) / 1.5) : 0) - (i === 0 ? 12 * clamp((lt - 1.2) / 1.5) : 0));
    const rank = ord.map((v, i) => i).sort((a, b) => ord[b] - ord[a]);
    rank.forEach((i, r) => { const yy = sy + 170 + r * 74, a = easeOut((lt - 0.3 - i * 0.07) / 0.4); g.globalAlpha = clamp(a); g.font = font(800, 28); g.fillStyle = '#9fb0d0'; g.fillText(String(r + 1), sx + 34, yy + 26);
      rrect(g, sx + 76, yy, (sw - 200) * ord[i] / 420 * a, 52, 14); g.fillStyle = CAR_COLORS[i % CAR_COLORS.length]; g.fill(); g.font = font(800, 26); g.fillStyle = '#fff'; g.fillText(String(Math.round(ord[i] * a)), sx + 76 + (sw - 200) * ord[i] / 420 * a + 12, yy + 26); });
    g.globalAlpha = 1; const pr = [0.46, 0.31, 0.15, 0.08], top = sy + 790; let acc = 0; pr.forEach((p, i) => { const ww = (sw - 80) * p * easeOut((lt - 1) / 1); rrect(g, sx + 40 + acc, top, Math.max(1, ww - 6), 60, 14); g.fillStyle = CAR_COLORS[i]; g.fill(); acc += ww; });
    g.font = font(800, 26); g.fillStyle = '#cfd8ff'; g.fillText(Math.round(pr[0] * 100 * easeOut((lt - 1) / 1)) + '%', sx + 50, top + 100);
  }
  g.restore();
}


/* карточка с настоящей фотографией (только свободные лицензии!) и подписью автора/лицензии */
const IMGS = {};
async function loadImgs(list) { await Promise.all([...new Set(list)].map(src => new Promise(res => { const im = new Image(); im.onload = () => { IMGS[src] = im; res(); }; im.onerror = () => res(); im.src = '/' + src.replace(/^\//, ''); }))); }
function drawCard(g, c, lt, dur) {
  const im = IMGS[c.img]; if (!im) return; const a = back((lt - 0.05) / 0.5); if (a <= 0) return;
  g.save(); g.fillStyle = `rgba(5,8,16,${0.55 * clamp(lt * 3)})`; g.fillRect(0, 0, W, H);
  const cw = W - 140, ch = Math.min(820, cw * (c.ratio || im.height / im.width)), cx = W / 2, cy = c.y || 800;
  g.translate(cx, cy); g.scale(a, a); g.rotate((c.tilt ?? -0.02));
  rrect(g, -cw / 2 - 14, -ch / 2 - 14, cw + 28, ch + 28, 36); g.fillStyle = '#fff'; g.shadowColor = 'rgba(0,0,0,0.5)'; g.shadowBlur = 40; g.fill(); g.shadowBlur = 0;
  g.save(); rrect(g, -cw / 2, -ch / 2, cw, ch, 26); g.clip();
  const z = 1.04 + 0.08 * clamp(lt / Math.max(1, dur)), sc2 = Math.max(cw / im.width, ch / im.height) * z, fx = c.fx ?? 0.5, fy = c.fy ?? 0.5;
  g.drawImage(im, -im.width * sc2 * fx, -im.height * sc2 * fy, im.width * sc2, im.height * sc2); g.restore();
  if (c.credit) { g.font = font(700, 22); const tw = g.measureText(c.credit).width; rrect(g, cw / 2 - tw - 34, ch / 2 - 50, tw + 24, 36, 12); g.fillStyle = 'rgba(0,0,0,0.6)'; g.fill(); g.fillStyle = '#fff'; g.fillText(c.credit, cw / 2 - tw - 22, ch / 2 - 25); }
  g.restore();
}
/* рисованный шлем по описанию дизайна, когда свободной фотографии нет */
function drawHelmet(g, h, lt) {
  const a = back((lt - 0.05) / 0.5); if (a <= 0) return; const [c1, c2, c3] = [h.c?.[0] || '#1e3a8a', h.c?.[1] || '#ffd23f', h.c?.[2] || '#ffffff'];
  g.save(); g.fillStyle = `rgba(5,8,16,${0.5 * clamp(lt * 3)})`; g.fillRect(0, 0, W, H);
  g.translate(W / 2, h.y || 760); g.scale(a * 2.6, a * 2.6); g.rotate(Math.sin(lt * 1.6) * 0.06);
  const shell = () => { g.beginPath(); g.moveTo(-150, 60); g.bezierCurveTo(-170, -60, -90, -150, 10, -150); g.bezierCurveTo(120, -150, 175, -60, 165, 30); g.lineTo(150, 95); g.lineTo(-120, 105); g.closePath(); };
  g.shadowColor = 'rgba(0,0,0,0.6)'; g.shadowBlur = 30; shell(); g.fillStyle = c1; g.fill(); g.shadowBlur = 0;
  g.save(); shell(); g.clip(); const p = h.p || 'stripes';
  if (p === 'stripes') { g.fillStyle = c2; for (let k = -3; k < 4; k++) { g.save(); g.rotate(-0.5); g.fillRect(k * 70, -300, 26, 600); g.restore(); } }
  if (p === 'split') { g.fillStyle = c2; g.fillRect(0, -200, 200, 400); }
  if (p === 'chequer') { for (let x = -180; x < 180; x += 30) for (let y = -160; y < 120; y += 30) if (((x + y) / 30 & 1) === 0) { g.fillStyle = c2; g.fillRect(x, y, 30, 30); } }
  if (p === 'stars') { g.fillStyle = c2; for (let k = 0; k < 14; k++) { const x = -140 + (k * 97) % 290, y = -130 + (k * 61) % 220; g.save(); g.translate(x, y); g.beginPath(); for (let j = 0; j < 10; j++) { const r = j % 2 ? 7 : 17, an = j * Math.PI / 5; g.lineTo(Math.sin(an) * r, -Math.cos(an) * r); } g.fill(); g.restore(); } }
  if (p === 'neon') { g.lineWidth = 10; g.shadowColor = c2; g.shadowBlur = 25; g.strokeStyle = c2; for (let k = 0; k < 3; k++) { g.beginPath(); g.moveTo(-170, -40 + k * 45); g.bezierCurveTo(-60, -110 + k * 45, 60, 20 + k * 45, 180, -60 + k * 45); g.stroke(); } g.shadowBlur = 0; }
  if (p === 'flame') { g.fillStyle = c2; g.beginPath(); g.moveTo(-170, 110); for (let k = 0; k <= 8; k++) g.quadraticCurveTo(-150 + k * 42, -60 - (k % 2) * 60, -130 + k * 42, 40); g.lineTo(200, 120); g.fill(); }
  g.fillStyle = c3; g.fillRect(-200, 60, 400, 14); g.restore();
  g.beginPath(); g.moveTo(-10, -55); g.bezierCurveTo(70, -70, 140, -55, 162, -10); g.lineTo(158, 35); g.bezierCurveTo(100, 45, 20, 40, -15, 20); g.closePath(); g.fillStyle = '#0b1020'; g.fill();
  g.fillStyle = 'rgba(255,255,255,0.25)'; g.beginPath(); g.ellipse(-40, -100, 60, 18, -0.4, 0, 7); g.fill();
  g.restore();
}
/* плашка с цифрой (текст из сцены, свой для каждого языка) */
function drawChip(g, text, lt, y = 330) {
  const a = back((lt - 0.15) / 0.45); if (a <= 0) return; g.save(); g.font = font(900, 76); const tw = g.measureText(text).width, k = Math.min(1, (W - 120) / (tw + 80));
  g.translate(W / 2, y); g.scale(a * k, a * k); g.rotate(-0.025); rrect(g, -tw / 2 - 40, -62, tw + 80, 124, 26); g.fillStyle = '#ffd23f'; g.shadowColor = 'rgba(0,0,0,0.45)'; g.shadowBlur = 30; g.fill(); g.shadowBlur = 0;
  g.fillStyle = '#0b1020'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(text, 0, 4); g.restore(); g.textAlign = 'left'; g.textBaseline = 'alphabetic';
}
function hudClock(g, lt, dur, t0, t1) {
  const hm = s => s.split(':').map(Number), [h0, m0] = hm(t0), [h1, m1] = hm(t1), p = easeOut((lt - 0.2) / Math.max(0.8, dur * 0.5)), mins = Math.round(lerp(h0 * 60 + m0, h1 * 60 + m1, p));
  const cx = W / 2, cy = 420, r = 120, a = back(lt / 0.5); g.save(); g.translate(cx, cy); g.scale(a, a);
  g.beginPath(); g.arc(0, 0, r + 22, 0, 7); g.fillStyle = 'rgba(8,12,22,0.82)'; g.fill(); g.lineWidth = 10; g.strokeStyle = '#ffd23f'; g.beginPath(); g.arc(0, 0, r, 0, 7); g.stroke();
  for (let i = 0; i < 12; i++) { g.save(); g.rotate(i / 12 * Math.PI * 2); g.fillStyle = '#9fb0d0'; g.fillRect(-3, -r + 10, 6, 18); g.restore(); }
  const hand = (ang, len, w2, c) => { g.save(); g.rotate(ang); g.strokeStyle = c; g.lineWidth = w2; g.lineCap = 'round'; g.beginPath(); g.moveTo(0, 10); g.lineTo(0, -len); g.stroke(); g.restore(); };
  hand((mins % 720) / 720 * Math.PI * 2, r * 0.5, 12, '#fff'); hand((mins % 60) / 60 * Math.PI * 2, r * 0.78, 7, '#ffd23f');
  g.font = font(900, 64); g.fillStyle = '#fff'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(`${String(Math.floor(mins / 60) % 24).padStart(2, '0')}:${String(mins % 60).padStart(2, '0')}`, 0, r + 78); g.restore(); g.textAlign = 'left'; g.textBaseline = 'alphabetic';
}
/* столбики (очки, возраст и т. п.): значения в shot, подписи значений можно переопределить текстами сцены */
function hudBars(g, lt, dur, h, texts) {
  const rows = h.rows, max = h.max || Math.max(...rows.map(r => r.v)), min = h.min ?? 0, x0 = 120, x1 = W - 120, top = 230, rh = Math.min(110, 560 / rows.length);
  g.save(); g.font = font(800, Math.min(44, rh * 0.4)); const tw = Math.max(90, ...rows.map((r, i) => g.measureText(texts?.[i] ?? String(Math.round(r.v))).width)); g.fillStyle = 'rgba(8,12,22,0.78)'; rrect(g, x0 - 40, top - 40, x1 - x0 + 80, rows.length * rh + 60, 34); g.fill();
  let order = rows.map((r, i) => i); if (h.swap && lt > dur * 0.5) { const [a, b] = h.swap; [order[a], order[b]] = [order[b], order[a]]; }
  order.forEach((ri, pos) => { const r = rows[ri], y = top + pos * rh, pa = easeOut((lt - 0.2 - ri * 0.12) / 0.7), w2 = (x1 - x0 - 150 - tw - 30) * clamp((r.v - min) / (max - min)) * pa;
    g.font = font(900, Math.min(52, rh * 0.48)); g.fillStyle = '#fff'; g.textBaseline = 'middle'; g.fillText(r.label, x0, y + rh * 0.45);
    rrect(g, x0 + 150, y + rh * 0.18, Math.max(8, w2), rh * 0.56, rh * 0.2); g.fillStyle = r.c || '#5b9bff'; g.fill();
    if (h.hi === ri) { g.lineWidth = 6; g.strokeStyle = '#ffd23f'; g.stroke(); }
    g.font = font(800, Math.min(44, rh * 0.4)); g.fillStyle = '#e5e7eb'; g.fillText(texts?.[ri] ?? String(Math.round(r.v * pa)), x0 + 150 + Math.max(8, w2) + 16, y + rh * 0.47); });
  g.restore(); g.textBaseline = 'alphabetic';
}

/* пульс: сердце бьётся в такт, бегущая кардиограмма, число растёт from → to; подпись единиц — sc.unit (своя для языка). Своя графика, без чужих логотипов */
function heartPath(g, s) { g.beginPath(); g.moveTo(0, s * 0.35); g.bezierCurveTo(-s * 1.1, -s * 0.35, -s * 0.55, -s * 1.05, 0, -s * 0.5); g.bezierCurveTo(s * 0.55, -s * 1.05, s * 1.1, -s * 0.35, 0, s * 0.35); g.closePath(); }
function hudPulse(g, lt, dur, h, unit) {
  const a = back(lt / 0.5); if (a <= 0) return; const p = easeOut((lt - 0.2) / Math.max(1, dur * 0.7)), bpm = Math.round(lerp(h.from ?? 80, h.to ?? 170, p)), beat = lt * bpm / 60, ph = beat - Math.floor(beat);
  const x0 = 110, y0 = 210, w = W - 220, hh = 330; g.save(); g.translate(W / 2, y0 + hh / 2); g.scale(a, a); g.translate(-W / 2, -(y0 + hh / 2));
  hudPanel(g, x0, y0, w, hh);
  const col = h.c || '#ff3b5c', k = 1 + 0.16 * Math.exp(-ph * 9);
  g.save(); g.translate(x0 + 120, y0 + 120); g.scale(k, k); heartPath(g, 70); g.fillStyle = col; g.shadowColor = col; g.shadowBlur = 30 * Math.exp(-ph * 6); g.fill(); g.restore();
  g.font = font(900, 120); g.fillStyle = '#fff'; g.textBaseline = 'middle'; g.fillText(String(bpm), x0 + 230, y0 + 118); const nw = g.measureText(String(bpm)).width;
  g.font = font(800, 40); g.fillStyle = '#9fb0d0'; g.fillText(unit || 'BPM', x0 + 250 + nw, y0 + 138);
  if (h.live !== false) { g.beginPath(); g.arc(x0 + w - 70, y0 + 60, 12, 0, 7); g.fillStyle = Math.sin(lt * 6) > 0 ? '#ff3b5c' : 'rgba(255,59,92,0.35)'; g.fill(); }
  /* кардиограмма: окно в 3 секунды, каждый удар — пик */
  const ex = x0 + 40, ew = w - 80, ey = y0 + 260, win = 3; g.save(); g.beginPath(); rrect(g, ex, ey - 70, ew, 120, 10); g.clip(); g.beginPath();
  for (let i = 0; i <= 240; i++) { const t = lt - win + win * i / 240, b = t * bpm / 60, q = b - Math.floor(b); let v = 0;
    if (q > 0.30 && q < 0.34) v = -0.15; else if (q > 0.34 && q < 0.37) v = 1; else if (q > 0.37 && q < 0.41) v = -0.45; else if (q > 0.55 && q < 0.68) v = 0.18 * Math.sin((q - 0.55) / 0.13 * Math.PI);
    const X = ex + ew * i / 240, Y = ey - v * 60; i ? g.lineTo(X, Y) : g.moveTo(X, Y); }
  g.strokeStyle = col; g.lineWidth = 6; g.lineJoin = 'round'; g.shadowColor = col; g.shadowBlur = 16; g.stroke(); g.restore();
  g.restore(); g.textBaseline = 'alphabetic';
}

/* разрыв к эталонному кругу: два бара (эталон и круг сцены), время и разница; подписи — из сцены (sc.gl: [эталон, круг], sc.gd: текст разницы) */
const lapFmt = d => `${Math.floor(d / 60)}:${(d % 60).toFixed(3).padStart(6, '0')}`;
function hudGap(g, lt, dur, h, labels, delta) {
  const a = back(lt / 0.5); if (a <= 0) return; const x0 = 90, y0 = 200, w = W - 180, hh = 380, ref = h.ref ?? 90, lap = h.lap ?? ref, mx = Math.max(ref, lap) * 1.02, mn = h.min ?? Math.min(ref, lap) * 0.8;
  g.save(); g.translate(W / 2, y0 + hh / 2); g.scale(a, a); g.translate(-W / 2, -(y0 + hh / 2)); hudPanel(g, x0, y0, w, hh);
  const rows = [[labels?.[0] || 'REF', ref, h.c0 || '#5b9bff'], [labels?.[1] || 'LAP', lap, h.c1 || '#22c55e']], bx = x0 + 40, bw = w - 80;
  rows.forEach(([lb, v, c], k) => { const y = y0 + 50 + k * 120, p = easeOut((lt - 0.25 - k * 0.35) / 0.9), cur = lerp(mn, v, p);
    g.font = font(800, 40); g.fillStyle = '#cfd8ff'; g.textBaseline = 'middle'; g.fillText(lb, bx, y + 8);
    g.font = font(900, 48); g.fillStyle = '#fff'; g.textAlign = 'right'; g.fillText(lapFmt(cur), bx + bw, y + 8); g.textAlign = 'left';
    rrect(g, bx, y + 42, bw, 30, 15); g.fillStyle = 'rgba(255,255,255,0.08)'; g.fill();
    rrect(g, bx, y + 42, Math.max(30, bw * clamp((cur - mn) / (mx - mn))), 30, 15); g.fillStyle = c; g.shadowColor = c; g.shadowBlur = 18; g.fill(); g.shadowBlur = 0; });
  const pd = easeOut((lt - 1.2) / 0.6); if (pd > 0) { g.globalAlpha = pd; g.font = font(900, 84); g.fillStyle = '#ffd23f'; g.textAlign = 'center'; g.fillText(delta || `+${(lap - ref).toFixed(3)}`, W / 2, y0 + hh - 62); g.textAlign = 'left'; g.globalAlpha = 1; }
  g.restore(); g.textBaseline = 'alphabetic';
}

function hudFor(g, sc, lt) {
  const h = sc.shot?.hud; if (!h) return;
  if (h.type === 'stopwatch') hudStopwatch(g, lt, sc.dur, h.to);
  else if (h.type === 'laps') hudLaps(g, lt, sc.dur, h.n);
  else if (h.type === 'thermo') hudThermo(g, lt, sc.dur, h.from, h.to);
  else if (h.type === 'battery') hudBattery(g, lt, sc.fx?.ex?.battery ?? 0.5);
  else if (h.type === 'tracks') hudTracks(g, lt, sc.dur, h.names, h.good);
  else if (h.type === 'phone') hudPhone(g, lt, sc.dur, h.mode, sc.fx);
  else if (h.type === 'clock') hudClock(g, lt, sc.dur, h.from, h.to);
  else if (h.type === 'bars') hudBars(g, lt, sc.dur, h, sc.barTexts);
  else if (h.type === 'pulse') hudPulse(g, lt, sc.dur, h, sc.unit);
  else if (h.type === 'gap') hudGap(g, lt, sc.dur, h, sc.gl, sc.gd);
}

/* ================= HQ-РЕЖИМ: кинокачество (spec.hq: true в VIDEO или hq: true в любом shot; по умолчанию выключено) =================
   Всё ниже работает только при HQ = true, поэтому старые ролики рисуются байт в байт как раньше.
   Рендер: HDR-буфер (half float, MSAA 4×) → bloom (яркие места, размытие на 1/2, 1/4, 1/8) → ACES + sRGB + виньетка.
   Свет: процедурная карта окружения (PMREM своей «комнаты»: небо, тёплые панели фонарей, неон у горизонта), мягкие тени
   от одного направленного света, который ходит за машиной в кадре, 4 точечных света от ближайших фонарей.
   Машины: детальный болид-2026 (лофты из сечений, крылья из профилей, halo, подвеска, колёса с боковиной), сейфти-кар купе.
   Трасса: бетонные блоки со щитами LapRadar, сетка-забор, фонари с выносом над трассой, пунктир полос на городских трассах. */
let HQ = false, HQS = null, HQO = {};   /* HQO: настройки из VIDEO.hq = { exposure, bloom, street, sphereK } */
const hqC = (c, k = 1) => new THREE.Color(c).multiplyScalar(k);
function hqTex(w, h, fn, { srgb = true, rep = true } = {}) {
  const c = document.createElement('canvas'); c.width = w; c.height = h; fn(c.getContext('2d'), w, h);
  const t = new THREE.CanvasTexture(c); if (srgb) t.colorSpace = THREE.SRGBColorSpace; if (rep) t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = 8; return t;
}
const hqNoise = (g, w, h, base, amp, seed = 1, cell = 1) => { const r = rng(seed); g.fillStyle = base; g.fillRect(0, 0, w, h);
  for (let y = 0; y < h; y += cell) for (let x = 0; x < w; x += cell) { const v = (r() - 0.5) * amp; g.fillStyle = v > 0 ? `rgba(255,255,255,${v})` : `rgba(0,0,0,${-v})`; g.fillRect(x, y, cell, cell); } };

/* ---------- рендер: HDR → bloom → ACES ---------- */
function hqSetup() {
  R.toneMapping = THREE.ACESFilmicToneMapping; R.toneMappingExposure = HQO.exposure ?? 1.0;
  R.shadowMap.enabled = true; R.shadowMap.type = THREE.PCFSoftShadowMap;
  const w = gl.width, h = gl.height, hf = { type: THREE.HalfFloatType, depthBuffer: false };
  const rt = new THREE.WebGLRenderTarget(w, h, { type: THREE.HalfFloatType, samples: 4 });
  const mk = d => [new THREE.WebGLRenderTarget(Math.max(4, w >> d), Math.max(4, h >> d), hf), new THREE.WebGLRenderTarget(Math.max(4, w >> d), Math.max(4, h >> d), hf)];
  const lv = [mk(1), mk(2), mk(3)];
  const vs = 'varying vec2 vUv; void main() { vUv = uv; gl_Position = vec4(position.xy, 0.0, 1.0); }';
  const sm = (fs, u) => new THREE.ShaderMaterial({ uniforms: u, vertexShader: vs, fragmentShader: fs, depthTest: false, depthWrite: false });
  const down4 = 'vec3 c = 0.25 * (texture2D(t, vUv + px * vec2(-1.0, -1.0)).rgb + texture2D(t, vUv + px * vec2(1.0, -1.0)).rgb + texture2D(t, vUv + px * vec2(-1.0, 1.0)).rgb + texture2D(t, vUv + px * vec2(1.0, 1.0)).rgb);';
  const bright = sm(`uniform sampler2D t; uniform vec2 px; uniform float thr, knee; varying vec2 vUv;
    void main() { ${down4} float b = max(c.r, max(c.g, c.b)); float s = clamp(b - thr + knee, 0.0, 2.0 * knee); s = s * s / (4.0 * knee + 1e-4);
      gl_FragColor = vec4(min(c * max(s, b - thr) / max(b, 1e-4), vec3(30.0)), 1.0); }`, { t: { value: null }, px: { value: new THREE.Vector2() }, thr: { value: 0.9 }, knee: { value: 0.5 } });
  const copy = sm(`uniform sampler2D t; uniform vec2 px; varying vec2 vUv; void main() { ${down4} gl_FragColor = vec4(c, 1.0); }`, { t: { value: null }, px: { value: new THREE.Vector2() } });
  const blur = sm(`uniform sampler2D t; uniform vec2 dir; varying vec2 vUv;
    void main() { vec3 c = texture2D(t, vUv).rgb * 0.2270270270;
      c += (texture2D(t, vUv + dir * 1.3846153846).rgb + texture2D(t, vUv - dir * 1.3846153846).rgb) * 0.3162162162;
      c += (texture2D(t, vUv + dir * 3.2307692308).rgb + texture2D(t, vUv - dir * 3.2307692308).rgb) * 0.0702702703; gl_FragColor = vec4(c, 1.0); }`, { t: { value: null }, dir: { value: new THREE.Vector2() } });
  const comp = sm(`uniform sampler2D t, b1, b2, b3; uniform vec3 k; uniform float vig; varying vec2 vUv;
    void main() { vec3 c = texture2D(t, vUv).rgb + k.x * texture2D(b1, vUv).rgb + k.y * texture2D(b2, vUv).rgb + k.z * texture2D(b3, vUv).rgb;
      vec2 d = vUv - 0.5; d.x *= 0.75; c *= 1.0 - vig * smoothstep(0.08, 0.5, dot(d, d) * 1.6);
      gl_FragColor = vec4(c, 1.0);
      #include <tonemapping_fragment>
      #include <colorspace_fragment>
      float n = fract(sin(dot(gl_FragCoord.xy, vec2(12.9898, 78.233))) * 43758.5453); gl_FragColor.rgb += (n - 0.5) / 255.0; }`,
    { t: { value: null }, b1: { value: null }, b2: { value: null }, b3: { value: null }, k: { value: new THREE.Vector3(0.55, 0.5, 0.45) }, vig: { value: 0.45 } });
  comp.toneMapped = true;
  const qs = new THREE.Scene(), quad = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), copy); quad.frustumCulled = false; qs.add(quad);
  HQS = { rt, lv, bright, copy, blur, comp, qs, quad, qc: new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1), env: {} };
}
function hqPass(mat, u, target) { const S = HQS; Object.entries(u).forEach(([k, v]) => { if (mat.uniforms[k].value?.set && !v?.isTexture) mat.uniforms[k].value.set(...v); else mat.uniforms[k].value = v; });
  S.quad.material = mat; R.setRenderTarget(target); R.render(S.qs, S.qc); }
function hqRender(scene, cam) {
  const S = HQS, bl = HQO.bloom ?? 1;
  R.setRenderTarget(S.rt); R.render(scene, cam);
  let src = S.rt.texture, sw = S.rt.width, sh = S.rt.height;
  S.lv.forEach(([a, b], i) => {
    hqPass(i ? S.copy : S.bright, { t: src, px: [0.5 / sw * 2, 0.5 / sh * 2] }, a);
    hqPass(S.blur, { t: a.texture, dir: [1 / a.width, 0] }, b); hqPass(S.blur, { t: b.texture, dir: [0, 1 / a.height] }, a);
    src = a.texture; sw = a.width; sh = a.height; });
  hqPass(S.comp, { t: S.rt.texture, b1: S.lv[0][0].texture, b2: S.lv[1][0].texture, b3: S.lv[2][0].texture, k: [0.5 * bl, 0.55 * bl, 0.6 * bl] }, null);
}
function draw(scene, cam) { if (HQ) hqRender(scene, cam); else R.render(scene, cam); }

/* ---------- карта окружения: своя «комната» вместо RoomEnvironment ---------- */
function hqEnv(kind = 'night') {
  if (HQS.env[kind]) return HQS.env[kind];
  const sc = new THREE.Scene(), day = kind === 'day', vegas = kind === 'vegas';
  const sg = new THREE.SphereGeometry(60, 32, 16), col = [], cc = new THREE.Color();
  const top = new THREE.Color(day ? '#5d8fd8' : '#070b1e'), hor = new THREE.Color(day ? '#e8f0ff' : vegas ? '#4a2058' : '#2a2a50'), bot = new THREE.Color(day ? '#6b6a60' : '#06060a');
  for (let i = 0; i < sg.attributes.position.count; i++) { const y = sg.attributes.position.getY(i) / 60; if (y > 0) cc.copy(hor).lerp(top, Math.pow(y, 0.6)); else cc.copy(hor).lerp(bot, Math.pow(-y, 0.4)); col.push(cc.r, cc.g, cc.b); }
  sg.setAttribute('color', new THREE.Float32BufferAttribute(col, 3));
  sc.add(new THREE.Mesh(sg, new THREE.MeshBasicMaterial({ vertexColors: true, side: THREE.BackSide })));
  const panel = (w, h, color, k, x, y, z) => { const m = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ color: hqC(color, k), side: THREE.DoubleSide })); m.position.set(x, y, z); m.lookAt(0, 0, 0); sc.add(m); };
  if (day) { panel(14, 14, '#fff6e0', 30, -25, 40, 18); panel(60, 8, '#ffffff', 1.2, 0, 3, -45); }
  else {
    for (let i = 0; i < 10; i++) { const a = i / 10 * Math.PI * 2; panel(10, 2.2, '#ffd9a8', 7, Math.cos(a) * 26, 20, Math.sin(a) * 26); }   /* фонари над трассой: блики на кузове */
    panel(30, 30, '#8ea0d8', 0.55, 0, 48, 0);
    const neon = vegas ? ['#ff3d9a', '#8b5cf6', '#a855f7', '#ff7a1a', '#c026d3', '#ff3d9a'] : ['#7aa2ff', '#ffd9a8', '#7aa2ff', '#ffd9a8'];
    neon.forEach((c, i) => { const a = (i + 0.5) / neon.length * Math.PI * 2; panel(4, 9, c, vegas ? 1.1 : 0.8, Math.cos(a) * 45, 4, Math.sin(a) * 45); });
  }
  const pm = new THREE.PMREMGenerator(R), t = pm.fromScene(sc, 0.02).texture; pm.dispose();
  return (HQS.env[kind] = t);
}

/* ---------- текстуры ---------- */
const _hqT = {};
const hqAsphalt = () => _hqT.asp || (_hqT.asp = hqTex(512, 512, (g, w, h) => { hqNoise(g, w, h, '#7d7d80', 0.22, 3, 2); const r = rng(9);
  for (let i = 0; i < 2600; i++) { g.fillStyle = r() < 0.5 ? 'rgba(255,255,255,0.18)' : 'rgba(0,0,0,0.25)'; g.fillRect(r() * w, r() * h, 1 + r() * 2, 1 + r() * 2); }
  for (let i = 0; i < 7; i++) { g.fillStyle = 'rgba(0,0,0,0.06)'; g.fillRect(w * (0.2 + r() * 0.6), 0, 18 + r() * 30, h); } }));   /* следы резины по траектории */
const hqConcrete = () => _hqT.con || (_hqT.con = hqTex(256, 256, (g, w, h) => hqNoise(g, w, h, '#b9b8b2', 0.12, 5, 2)));
function hqBarrierTex(brandOn) {
  const k = 'bar' + brandOn; if (_hqT[k]) return _hqT[k];
  return (_hqT[k] = hqTex(2048, 256, (g, w, h) => {   /* 24 м длины: бетон, внизу грязь, на лицевой стороне щиты */
    hqNoise(g, w, h, '#c4c3bd', 0.1, 7, 2); const gr = g.createLinearGradient(0, h, 0, h * 0.6); gr.addColorStop(0, 'rgba(40,36,30,0.55)'); gr.addColorStop(1, 'rgba(40,36,30,0)'); g.fillStyle = gr; g.fillRect(0, 0, w, h);
    for (let x = 0; x < w; x += w / 8) { g.fillStyle = 'rgba(0,0,0,0.35)'; g.fillRect(x, 0, 3, h); }   /* стыки блоков по 3 м */
    const img = brandTex('board').image;
    for (const x0 of [0, w / 2]) { g.fillStyle = '#0b1020'; g.fillRect(x0 + 6, h * 0.08, w / 3 - 12, h * 0.6); if (brandOn) g.drawImage(img, x0 + 40, h * 0.12, (w / 3 - 80), (w / 3 - 80) / 4); else { g.fillStyle = '#1d4ed8'; g.fillRect(x0 + 6, h * 0.62, w / 3 - 12, h * 0.06); } }
    g.fillStyle = '#e8e6df'; g.fillRect(w / 3, h * 0.08, w / 6, h * 0.6); g.fillStyle = '#d0302a'; for (let x = w / 3; x < w / 2; x += 64) g.fillRect(x, h * 0.08, 32, h * 0.6);
  }));
}
const hqFence = () => _hqT.fen || (_hqT.fen = hqTex(128, 256, (g, w, h) => { g.clearRect(0, 0, w, h); g.strokeStyle = 'rgba(205,210,220,0.9)'; g.lineWidth = 1.6;
  for (let k = -h; k < w + h; k += 16) { g.beginPath(); g.moveTo(k, 0); g.lineTo(k + h, h); g.stroke(); g.beginPath(); g.moveTo(k, h); g.lineTo(k + h, 0); g.stroke(); }
  g.fillStyle = 'rgba(160,165,175,1)'; g.fillRect(0, 0, w, 5); g.fillRect(0, h - 5, w, 5); g.fillRect(0, h * 0.5, w, 3); }));
function hqWindows(vegas) { const k = 'win' + vegas; if (_hqT[k]) return _hqT[k];
  return (_hqT[k] = hqTex(256, 256, (g, w, h) => { g.fillStyle = '#6f6f78'; g.fillRect(0, 0, w, h); const r = rng(vegas ? 13 : 17);
    for (let y = 12; y < h - 12; y += 20) for (let x = 12; x < w - 12; x += 20) { const lit = r() < (vegas ? 0.42 : 0.3); g.fillStyle = lit ? (r() < 0.6 ? '#ffd79a' : vegas && r() < 0.4 ? '#ff9ad6' : '#e8f1ff') : '#1a1d26'; g.fillRect(x, y, 12, 13); }
    g.fillStyle = '#26262c'; g.fillRect(0, 0, w, 8); g.fillRect(0, 0, 8, h); })); }
const hqBlob = () => _hqT.blob || (_hqT.blob = hqTex(128, 256, (g, w, h) => { const gr = g.createRadialGradient(w / 2, h / 2, 4, w / 2, h / 2, w / 2); gr.addColorStop(0, 'rgba(0,0,0,0.85)'); gr.addColorStop(0.6, 'rgba(0,0,0,0.45)'); gr.addColorStop(1, 'rgba(0,0,0,0)');
  g.save(); g.scale(1, h / w); g.fillStyle = gr; g.fillRect(0, 0, w, w); g.restore(); }, { rep: false }));

/* ---------- материалы трассы ---------- */
function hqStd(m, o = {}) {   /* Lambert → Standard с теми же цветом, текстурой и свечением */
  const n = new THREE.MeshStandardMaterial({ color: m.color, map: m.map, vertexColors: m.vertexColors, emissive: m.emissive, emissiveMap: m.emissiveMap, emissiveIntensity: m.emissiveIntensity,
    side: m.side, transparent: m.transparent, opacity: m.opacity, roughness: 0.85, metalness: 0, envMapIntensity: 0.3, ...o });
  return n;
}
function hqWorld(w, refs, tr) {
  const { scene, P, N, NR, TG, L } = w, T = w.theme, vegas = T === THEMES.vegas, day = !T.lights, street = HQO.street ?? (vegas || !!spec.city || !!tr.street);
  w.hq = { lamps: [], street };
  /* небо темнее и глубже, свет мягче: остальное дают фонари и карта окружения */
  if (!day) scene.background = gradTex(vegas ? [[0, '#020310'], [0.5, '#0a0d2c'], [0.78, '#2a1346'], [0.92, '#5c1f58'], [1, '#8a2f62']] : [[0, '#03050f'], [0.55, '#0c1532'], [0.85, '#2c2450'], [1, '#5a3a58']]);
  scene.fog.color.set(vegas ? '#1a0f2e' : day ? T.fog : '#141a33');
  scene.environment = hqEnv(vegas ? 'vegas' : day ? 'day' : 'night');
  scene.traverse(o => { if (o.isHemisphereLight) o.intensity = day ? 0.9 : 0.32; });
  const key = refs.sun; key.intensity = day ? 2.6 : 1.1; key.color.set(day ? '#fff1dc' : '#c8d4ff'); key.castShadow = true;
  key.shadow.mapSize.set(2048, 2048); Object.assign(key.shadow.camera, { left: -18, right: 18, top: 18, bottom: -18, near: 1, far: 160 }); key.shadow.bias = -0.0004; key.shadow.normalBias = 0.03; key.shadow.radius = 4;
  scene.add(key.target); w.hq.key = key;
  w.hq.pl = Array.from({ length: 4 }, () => { const l = new THREE.PointLight('#ffd2a0', day ? 0 : 160, 70, 2); scene.add(l); return l; });
  /* асфальт, обочины, линии, поребрики */
  const asp = hqAsphalt(); asp.repeat.set(1, 1);
  refs.asphalt.material = new THREE.MeshStandardMaterial({ color: T.asphalt, map: asp, roughnessMap: asp, roughness: day ? 0.85 : 0.62, metalness: 0, envMapIntensity: day ? 0.4 : 0.75 }); refs.asphalt.material.color.multiplyScalar(day ? 1.5 : 1.9);
  refs.runoff.material = new THREE.MeshStandardMaterial({ color: street ? '#6e6d70' : T.runoff, map: hqConcrete(), roughness: 0.92, envMapIntensity: 0.3 });
  refs.ground.material = new THREE.MeshStandardMaterial({ color: T.ground, roughness: 1, envMapIntensity: 0.2 });
  refs.lines.forEach(m => { m.material = new THREE.MeshStandardMaterial({ color: '#f2f2ee', roughness: 0.45, envMapIntensity: 0.6 }); m.receiveShadow = true; });
  refs.kerbs.forEach(m => { m.geometry.computeVertexNormals(); m.material = new THREE.MeshStandardMaterial({ vertexColors: true, side: THREE.DoubleSide, roughness: 0.5, envMapIntensity: 0.7 }); m.receiveShadow = true; });
  [refs.asphalt, refs.runoff, refs.ground].forEach(m => { m.receiveShadow = true; });
  if (w.bldMesh) { const m = w.bldMesh.material, win = hqWindows(vegas); win.repeat.set(1 / 38, 1 / 38);
    w.bldMesh.material = new THREE.MeshStandardMaterial({ vertexColors: true, map: w.bldMesh.geometry.attributes.uv ? win : null, emissiveMap: w.bldMesh.geometry.attributes.uv ? win : null, emissive: day ? '#000000' : hqC('#ffffff', vegas ? 1.25 : 0.9), roughness: 0.7, metalness: 0.15, envMapIntensity: 0.5 }); }
  scene.traverse(o => { if ((o.isMesh || o.isInstancedMesh) && o.material?.isMeshLambertMaterial) { const green = !day && !o.material.map && o.material.color.g > o.material.color.r * 1.2; o.material = hqStd(o.material); if (green) o.material.color.multiplyScalar(0.35); } });
  if (street) hqStreet(w, refs);
  if (T.lights) hqLamps(w);
}
/* бетонные блоки + щиты + сетка-забор вдоль городской трассы, пунктир полос */
function hqStreet(w, refs) {
  const { scene, P, N, NR, L } = w, off = 10.4, step = L / N, brandOn = spec?.brand3d !== false;
  const pitPts = w.pit ? w.pit.PP : [], gap = (x, z) => { for (let j = 0; j < pitPts.length; j += 2) { const q = pitPts[j]; if ((q.x - x) ** 2 + (q.z - z) ** 2 < 64) return true; } return false; };
  const front = [[0, 0], [0.05, 0.22], [0.14, 0.36], [0.19, 1.08]], top = [[0.19, 1.08], [0.45, 1.08]], back = [[0.45, 1.08], [0.5, 0.36], [0.59, 0.22], [0.64, 0]];
  const strip = (prof, side, ok, uvLen, vMap) => { const pos = [], uv = [], idx = []; let vi = 0, open = false;
    for (let i = 0; i < N; i++) { const k = i % N; if (!ok[k] || !ok[(k + 1) % N]) { open = false; continue; }
      const add = kk => { const p = P[kk], n = NR[kk]; prof.forEach(([d, y], j) => { pos.push(p.x + n.x * side * (off + d), p.y + y, p.z + n.z * side * (off + d)); uv.push(-side * (i + (kk !== k ? 1 : 0)) * step / uvLen, vMap(j, y));   /* справа u идёт назад: надписи читаются с трассы */ }); };
      add(k); add((k + 1) % N); const m = prof.length;
      for (let j = 0; j < m - 1; j++) idx.push(vi + j, vi + j + 1, vi + m + j, vi + j + 1, vi + m + j + 1, vi + m + j); vi += 2 * m; }
    const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2)); g.setIndex(idx); g.computeVertexNormals(); return g; };
  const barM = new THREE.MeshStandardMaterial({ map: hqBarrierTex(brandOn), roughness: 0.8, envMapIntensity: 0.35, side: THREE.DoubleSide });
  const conM = new THREE.MeshStandardMaterial({ map: hqConcrete(), color: '#d8d6cf', roughness: 0.85, envMapIntensity: 0.3, side: THREE.DoubleSide });
  const fen = hqFence(); const fenM = new THREE.MeshStandardMaterial({ map: fen, transparent: true, depthWrite: false, side: THREE.DoubleSide, roughness: 0.4, metalness: 0.6, envMapIntensity: 0.8, color: '#9ea3ad', opacity: 0.8 });
  const postG = new THREE.CylinderGeometry(0.05, 0.05, 3.7, 6); const posts = [];
  for (const side of [-1, 1]) {
    const ok = P.map((p, k) => !gap(p.x + NR[k].x * side * off, p.z + NR[k].z * side * off));
    const f = new THREE.Mesh(strip(front, side, ok, 24, (j, y) => y / 1.08), barM), t2 = new THREE.Mesh(strip([...top, ...back.slice(1)], side, ok, 6, (j, y) => j / 4), conM);
    f.receiveShadow = t2.receiveShadow = true; scene.add(f, t2);
    const fg = new THREE.Mesh(strip([[0.32, 1.08], [0.32, 4.7]], side, ok, 2, (j) => j), fenM); fg.renderOrder = 3; scene.add(fg);
    for (let k = 0; k < N; k += 2) if (ok[k] && ok[(k + 1) % N]) { const p = P[k], n = NR[k]; posts.push([p.x + n.x * side * (off + 0.32), p.y + 2.9, p.z + n.z * side * (off + 0.32)]); }
  }
  const pm = new THREE.InstancedMesh(postG, new THREE.MeshStandardMaterial({ color: '#8d929c', roughness: 0.45, metalness: 0.7 }), posts.length), m4 = new THREE.Matrix4();
  posts.forEach((p, i) => pm.setMatrixAt(i, m4.makeTranslation(...p))); scene.add(pm);
  /* пунктир полос: городская улица */
  const dash = [], dg = new THREE.PlaneGeometry(0.14, 3); dg.rotateX(-Math.PI / 2);
  for (let s = 0; s < L; s += 9) { const a = w.at(s); if (w.cornerIdx.some(c => Math.abs(c.i - a.i) < 6)) continue; for (const ln of [-2.33, 2.33]) dash.push({ p: a.p.clone().addScaledVector(a.n, ln), yaw: Math.atan2(a.t.x, a.t.z) }); }
  const dm = new THREE.InstancedMesh(dg, new THREE.MeshStandardMaterial({ color: '#e9e9e4', roughness: 0.5, envMapIntensity: 0.6 }), dash.length), q = new THREE.Quaternion(), e = new THREE.Euler(), one = new THREE.Vector3(1, 1, 1);
  dash.forEach((d, i) => dm.setMatrixAt(i, m4.compose(d.p.clone().setY(d.p.y + 0.055), q.setFromEuler(e.set(0, d.yaw, 0)), one))); dm.receiveShadow = true; scene.add(dm);
}
/* фонари: столб, вынос над трассой, светящаяся голова, ореол и пятно света на асфальте */
function hqLamps(w) {
  const { scene, P, N, NR } = w, vegas = w.theme === THEMES.vegas, every = 14, H = 11.5, off = 12.2, arm = 3.6, list = [];
  for (let i = 0, j = 0; i < N; i += every, j++) { const side = j % 2 ? 1 : -1, p = P[i], n = NR[i];
    if (w.cornerIdx.some(c => Math.min(Math.abs(c.i - i), N - Math.abs(c.i - i)) < 3)) continue;
    list.push({ base: new THREE.Vector3(p.x + n.x * side * off, p.y, p.z + n.z * side * off), head: new THREE.Vector3(p.x + n.x * side * (off - arm), p.y + H, p.z + n.z * side * (off - arm)), yaw: Math.atan2(-n.x * side, -n.z * side) }); }
  const pole = new THREE.CylinderGeometry(0.12, 0.2, H, 8); pole.translate(0, H / 2, 0);
  const armG = new THREE.BoxGeometry(0.12, 0.12, arm); armG.translate(0, H - 0.1, arm / 2);
  const headG = new THREE.BoxGeometry(0.55, 0.22, 1.3); headG.translate(0, H - 0.2, arm);
  const lensG = new THREE.PlaneGeometry(0.42, 1.1); lensG.rotateX(Math.PI / 2); lensG.translate(0, H - 0.32, arm);
  const metal = new THREE.MeshStandardMaterial({ color: '#5d626c', roughness: 0.45, metalness: 0.75, envMapIntensity: 0.8 });
  const mk = (g, m) => { const im = new THREE.InstancedMesh(g, m, list.length); scene.add(im); return im; };
  const ims = [mk(pole, metal), mk(armG, metal), mk(headG, metal), mk(lensG, new THREE.MeshBasicMaterial({ color: hqC('#ffe2b8', 9), side: THREE.DoubleSide }))];
  const m4 = new THREE.Matrix4(), q = new THREE.Quaternion(), e = new THREE.Euler(), one = new THREE.Vector3(1, 1, 1);
  list.forEach((l, k) => { m4.compose(l.base, q.setFromEuler(e.set(0, l.yaw, 0)), one); ims.forEach(im => im.setMatrixAt(k, m4)); });
  const gp = []; list.forEach(l => gp.push(l.head.x, l.head.y - 0.45, l.head.z));
  const pg = new THREE.BufferGeometry(); pg.setAttribute('position', new THREE.Float32BufferAttribute(gp, 3));
  scene.add(new THREE.Points(pg, new THREE.PointsMaterial({ size: 7, map: glowTex('rgba(255,236,200,1)', 'rgba(255,200,140,0)'), color: hqC('#ffd8a8', 1.6), transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false })));
  const poolG = new THREE.PlaneGeometry(24, 24); poolG.rotateX(-Math.PI / 2);
  const pools = new THREE.InstancedMesh(poolG, new THREE.MeshBasicMaterial({ map: glowTex('rgba(255,226,180,0.5)', 'rgba(255,220,170,0)'), color: hqC('#ffd8a8', 0.45), transparent: true, depthWrite: false, blending: THREE.AdditiveBlending }), list.length);
  list.forEach((l, k) => pools.setMatrixAt(k, m4.makeTranslation(l.head.x, l.base.y + 0.09, l.head.z))); scene.add(pools);
  w.hq.lamps = list.map(l => l.head.clone().setY(l.head.y - 0.6));
}

/* ---------- геометрия: лофт из сечений-суперэллипсов, профиль крыла, плоская пластина, трубка ---------- */
function hqLoft(secs, M = 28) {   /* secs: [z, w, ht, hb, y, n, x?] — ширина, высота вверх/вниз от центра y, «квадратность» n */
  const pos = [], uv = [], idx = [], S = secs.length;
  secs.forEach(([z, w, ht, hb, y, n = 2.6, x = 0], j) => { for (let k = 0; k <= M; k++) { const t = k / M * Math.PI * 2, c = Math.cos(t), s = Math.sin(t), e = 2 / n;
    pos.push(x + w * Math.sign(c) * Math.pow(Math.abs(c), e), y + (s >= 0 ? ht : hb) * Math.sign(s) * Math.pow(Math.abs(s), e), z); uv.push(k / M, 1 - j / (S - 1)); } });
  for (let j = 0; j < S - 1; j++) for (let k = 0; k < M; k++) { const a = j * (M + 1) + k, b = a + M + 1; if (secs[0][0] > secs[S - 1][0]) idx.push(a, b, a + 1, a + 1, b, b + 1); else idx.push(a, a + 1, b, a + 1, b + 1, b); }
  for (const [j, dir] of [[0, 1], [S - 1, -1]]) { const ci = pos.length / 3, [z, , , , y, , x = 0] = secs[j]; pos.push(x, y, z); uv.push(0.25, j ? 0 : 1);
    for (let k = 0; k < M; k++) { const a = j * (M + 1) + k; (dir > 0) === (secs[0][0] > secs[S - 1][0]) ? idx.push(ci, a, a + 1) : idx.push(ci, a + 1, a); } }
  const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2)); g.setIndex(idx); g.computeVertexNormals();
  const nr = g.attributes.normal; for (let j = 0; j < S; j++) { const a = j * (M + 1), b = a + M; const v = new THREE.Vector3(nr.getX(a) + nr.getX(b), nr.getY(a) + nr.getY(b), nr.getZ(a) + nr.getZ(b)).normalize(); nr.setXYZ(a, v.x, v.y, v.z); nr.setXYZ(b, v.x, v.y, v.z); }
  return g;
}
function hqFoil(chord, span, aoa = 0, th = 0.1, camber = -0.05) {   /* крыло: передняя кромка в 0, хорда назад (−z), размах по x, aoa > 0 — задняя кромка выше */
  const s = new THREE.Shape(), n = 12, up = [], lo = [];
  for (let i = 0; i <= n; i++) { const x = (1 - Math.cos(i / n * Math.PI)) / 2, t = 5 * th * (0.2969 * Math.sqrt(x) - 0.126 * x - 0.3516 * x * x + 0.2843 * x ** 3 - 0.1036 * x ** 4), yc = camber * 4 * x * (1 - x); up.push([x * chord, (yc + t) * chord]); lo.push([x * chord, (yc - t) * chord]); }
  s.moveTo(...up[n]); for (let i = n - 1; i >= 0; i--) s.lineTo(...up[i]); for (let i = 1; i <= n; i++) s.lineTo(...lo[i]);
  const g = new THREE.ExtrudeGeometry(s, { depth: span, bevelEnabled: false, curveSegments: 4 }); g.rotateY(Math.PI / 2); g.translate(-span / 2, 0, 0); g.rotateX(aoa); return g;
}
function hqPlate(pts, th = 0.02) {   /* вертикальная пластина (щиток крыла): pts — [z, y], толщина по x */
  const s = new THREE.Shape(); s.moveTo(...pts[0]); pts.slice(1).forEach(p => s.lineTo(...p));
  const g = new THREE.ExtrudeGeometry(s, { depth: th, bevelEnabled: true, bevelThickness: 0.004, bevelSize: 0.004, bevelSegments: 1 }); g.rotateY(-Math.PI / 2); g.translate(th / 2, 0, 0); return g;
}
function hqRod(a, b, r) { const d = new THREE.Vector3(...b).sub(new THREE.Vector3(...a)), g = new THREE.CylinderGeometry(r, r, d.length(), 6); g.translate(0, d.length() / 2, 0);
  g.applyQuaternion(new THREE.Quaternion().setFromUnitVectors(new THREE.Vector3(0, 1, 0), d.clone().normalize())); g.translate(...a); return g; }

/* ---------- болид 2026 (свой, без ливрей команд): несколько схем окраски ---------- */
const HQ_PAT = ['stripe', 'fade', 'split', 'band', 'fade', 'stripe', 'band', 'split', 'stripe', 'fade'];
function hqLivery(c, a, pat) {
  const k = [c, a, pat].join(); if (_hqT[k]) return _hqT[k];
  return (_hqT[k] = hqTex(512, 256, (g, w, h) => {   /* u — по кругу сечения (0,25 — верх, 0,75 — низ), v — вдоль машины (низ холста — нос) */
    g.fillStyle = c; g.fillRect(0, 0, w, h);
    if (pat === 'fade') { const gr = g.createLinearGradient(0, h, 0, 0); gr.addColorStop(0.35, c); gr.addColorStop(0.85, a); g.fillStyle = gr; g.fillRect(0, 0, w, h); }
    if (pat === 'split') { g.fillStyle = a; g.fillRect(0, 0, w * 0.1, h); g.fillRect(w * 0.4, 0, w * 0.2, h); g.fillRect(w * 0.9, 0, w * 0.1, h); }
    if (pat === 'band') { g.fillStyle = a; g.beginPath(); g.moveTo(0, h * 0.62); g.lineTo(w, h * 0.38); g.lineTo(w, h * 0.5); g.lineTo(0, h * 0.74); g.fill(); }
    if (pat === 'stripe') { g.fillStyle = a; g.fillRect(w * 0.215, 0, w * 0.07, h); g.fillRect(w * 0.195, 0, w * 0.008, h); g.fillRect(w * 0.297, 0, w * 0.008, h); }
    const gr = g.createLinearGradient(w * 0.52, 0, w * 0.62, 0); gr.addColorStop(0, 'rgba(14,15,18,0)'); gr.addColorStop(1, 'rgba(14,15,18,1)'); g.fillStyle = gr; g.fillRect(w * 0.52, 0, w * 0.1, h);
    g.fillStyle = '#0e0f12'; g.fillRect(w * 0.62, 0, w * 0.26, h); const gr2 = g.createLinearGradient(w * 0.88, 0, w * 0.98, 0); gr2.addColorStop(0, 'rgba(14,15,18,1)'); gr2.addColorStop(1, 'rgba(14,15,18,0)'); g.fillStyle = gr2; g.fillRect(w * 0.88, 0, w * 0.1, h);
  }));
}
function hqTyreTex() { return _hqT.tyre || (_hqT.tyre = hqTex(512, 64, (g, w, h) => {   /* боковина: надписи-блоки видно, когда колесо крутится */
  g.fillStyle = '#16171a'; g.fillRect(0, 0, w, h);
  for (const [y0, y1] of [[0, 14], [50, 64]]) for (let i = 0; i < 4; i++) { g.fillStyle = 'rgba(200,200,205,0.42)'; g.fillRect(i * w / 4 + 14, y0 + 4, 46, y1 - y0 - 8); g.fillRect(i * w / 4 + 66, y0 + 5, 18, y1 - y0 - 10); }
  g.fillStyle = '#0d0e10'; g.fillRect(0, 22, w, 20); }, { rep: true })); }
function hqRimTex() { return _hqT.rim || (_hqT.rim = hqTex(256, 256, (g, w, h) => { g.fillStyle = '#0c0d10'; g.fillRect(0, 0, w, h); g.translate(w / 2, h / 2);
  g.fillStyle = '#9ea4ae'; g.beginPath(); g.arc(0, 0, 124, 0, 7); g.arc(0, 0, 108, 0, 7, true); g.fill();
  for (let i = 0; i < 10; i++) { g.save(); g.rotate(i / 10 * Math.PI * 2); g.fillStyle = '#b5bbc4'; g.beginPath(); g.moveTo(-9, -30); g.lineTo(9, -30); g.lineTo(5, -110); g.lineTo(-5, -110); g.fill(); g.restore(); }
  g.fillStyle = '#c9ced6'; g.beginPath(); g.arc(0, 0, 32, 0, 7); g.fill(); }, { rep: false })); }
function makeCarHQ(color, tyreColor = TYRE.soft, k = 0, opt = {}) {
  const g = new THREE.Group(), acc = opt.a || ACCENT[color] || '#f8fafc', pat = opt.p || HQ_PAT[Math.abs(CAR_COLORS.indexOf(color)) % HQ_PAT.length];
  const live = new THREE.MeshPhysicalMaterial({ map: hqLivery(color, acc, pat), roughness: 0.28, metalness: 0.25, clearcoat: 1, clearcoatRoughness: 0.06, envMapIntensity: 1.15 });
  const paint = new THREE.MeshPhysicalMaterial({ color, roughness: 0.28, metalness: 0.25, clearcoat: 1, clearcoatRoughness: 0.06, envMapIntensity: 1.15 });
  const accent = new THREE.MeshPhysicalMaterial({ color: acc, roughness: 0.3, metalness: 0.2, clearcoat: 1, clearcoatRoughness: 0.08, envMapIntensity: 1.1 });
  const carbon = new THREE.MeshStandardMaterial({ color: '#141518', roughness: 0.45, metalness: 0.2, envMapIntensity: 0.6 });
  const black = new THREE.MeshStandardMaterial({ color: '#08090b', roughness: 0.6, metalness: 0.1 });
  const add = (geo, m, x = 0, y = 0, z = 0, cast = true) => { const o = new THREE.Mesh(geo, m); o.position.set(x, y, z); o.castShadow = cast; g.add(o); return o; };
  /* монокок и нос */
  add(hqLoft([[3.42, 0.05, 0.04, 0.04, 0.27, 2.2], [3.22, 0.1, 0.07, 0.06, 0.3, 2.4], [2.8, 0.17, 0.11, 0.09, 0.36, 2.6], [2.2, 0.24, 0.15, 0.12, 0.43, 2.8], [1.5, 0.31, 0.2, 0.16, 0.5, 3],
    [0.95, 0.38, 0.25, 0.22, 0.55, 3.2], [0.3, 0.43, 0.28, 0.3, 0.58, 3.4], [-0.3, 0.43, 0.27, 0.3, 0.58, 3.4], [-0.9, 0.34, 0.22, 0.28, 0.55, 3.2], [-1.6, 0.22, 0.17, 0.22, 0.5, 3], [-2.1, 0.12, 0.12, 0.14, 0.48, 2.6], [-2.32, 0.05, 0.06, 0.07, 0.48, 2.2]]), live);
  /* кожух двигателя с воздухозаборником над головой */
  add(hqLoft([[0.12, 0.05, 0.02, 0.02, 0.9, 2], [-0.12, 0.17, 0.32, 0.05, 0.92, 2.4], [-0.5, 0.23, 0.27, 0.1, 0.92, 2.6], [-1.0, 0.25, 0.14, 0.15, 0.88, 2.8], [-1.6, 0.17, 0.06, 0.12, 0.78, 2.6], [-2.05, 0.07, 0.03, 0.08, 0.66, 2.2]]), live);
  const intake = add(new THREE.CircleGeometry(0.1, 16), black, 0, 1.12, -0.06, false); intake.scale.set(1, 1.3, 1);
  add(new THREE.BoxGeometry(0.11, 0.05, 0.06), accent, 0, 1.27, -0.25);   /* камера на воздухозаборнике */
  /* плавник с наклейкой */
  const fin = add(hqPlate([[-0.55, 1.1], [-2.05, 0.95], [-2.15, 0.68], [-1.2, 0.98]], 0.014), paint);
  /* понтоны с воздухозаборниками */
  for (const sx of [-1, 1]) {
    add(hqLoft([[0.82, 0.21, 0.16, 0.15, 0.45, 4, sx * 0.62], [0.45, 0.3, 0.19, 0.19, 0.44, 4, sx * 0.64], [-0.3, 0.29, 0.15, 0.2, 0.4, 3.6, sx * 0.62], [-0.9, 0.2, 0.09, 0.16, 0.34, 3.2, sx * 0.55], [-1.4, 0.1, 0.05, 0.1, 0.28, 2.6, sx * 0.42], [-1.72, 0.04, 0.02, 0.05, 0.25, 2, sx * 0.34]]), live);
    const inl = add(new THREE.PlaneGeometry(0.36, 0.24), black, sx * 0.63, 0.46, 0.83, false); inl.scale.set(1, 1, 1);
    /* зеркала */
    add(new THREE.BoxGeometry(0.17, 0.07, 0.05), paint, sx * 0.55, 0.9, 0.82); add(hqRod([sx * 0.3, 0.78, 0.78], [sx * 0.5, 0.88, 0.82], 0.012), carbon);
  }
  /* днище, диффузор, щиток пола */
  { const s = new THREE.Shape(); [[-0.3, 1.75], [-0.88, 1.15], [-0.95, -1.2], [-0.62, -1.4], [0.62, -1.4], [0.95, -1.2], [0.88, 1.15], [0.3, 1.75]].forEach((p, i) => i ? s.lineTo(p[0], p[1]) : s.moveTo(p[0], p[1]));
    const fg = new THREE.ExtrudeGeometry(s, { depth: 0.035, bevelEnabled: false }); fg.rotateX(Math.PI / 2); add(fg, carbon, 0, 0.11, 0);
    const df = add(new THREE.PlaneGeometry(1.24, 0.75), carbon, 0, 0.2, -1.75); df.rotation.x = Math.PI / 2 + 0.38; df.material = carbon.clone(); df.material.side = THREE.DoubleSide;
    for (const x of [-0.42, -0.14, 0.14, 0.42]) add(hqPlate([[-1.4, 0.08], [-2.1, 0.33], [-2.1, 0.12]], 0.012), carbon, x, 0, 0); }
  /* кокпит, шлем, halo */
  const ck = add(new THREE.CircleGeometry(0.2, 20), black, 0, 0.875, 0.32, false); ck.rotation.x = -Math.PI / 2; ck.scale.set(1.15, 1.9, 1);
  const helmet = new THREE.Group(); helmet.position.set(0, 0.99, 0.16); g.add(helmet);
  { const hm = new THREE.MeshPhysicalMaterial({ color: acc === '#f8fafc' ? '#f8fafc' : '#f8fafc', roughness: 0.2, clearcoat: 1, clearcoatRoughness: 0.04, envMapIntensity: 1.2 });
    const shell = new THREE.Mesh(new THREE.SphereGeometry(0.17, 24, 16), hm); shell.scale.set(1, 1, 1.12); shell.castShadow = true; helmet.add(shell);
    const stripe = new THREE.Mesh(new THREE.SphereGeometry(0.172, 24, 16, 0, Math.PI * 2, 0.9, 0.22), paint); stripe.scale.set(1, 1, 1.12); helmet.add(stripe);
    const visor = new THREE.Mesh(new THREE.SphereGeometry(0.175, 20, 10, -Math.PI * 0.32 + Math.PI / 2, Math.PI * 0.64, 1.25, 0.42), new THREE.MeshPhysicalMaterial({ color: '#0b0d14', roughness: 0.05, metalness: 0.9, clearcoat: 1, envMapIntensity: 1.6 }));
    visor.scale.set(1, 1, 1.12); helmet.add(visor);
    const rest = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.12, 0.2), black); rest.position.set(0, -0.08, -0.2); helmet.add(rest); }
  const haloP = [[-0.32, 0.8, -0.16], [-0.35, 1.03, 0.05], [-0.28, 1.13, 0.33], [-0.13, 1.155, 0.54], [0, 1.16, 0.6], [0.13, 1.155, 0.54], [0.28, 1.13, 0.33], [0.35, 1.03, 0.05], [0.32, 0.8, -0.16]].map(p => new THREE.Vector3(...p));
  add(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(haloP), 48, 0.034, 8, false), carbon);
  add(new THREE.TubeGeometry(new THREE.CatmullRomCurve3([new THREE.Vector3(0, 1.16, 0.6), new THREE.Vector3(0, 1.05, 0.82), new THREE.Vector3(0, 0.84, 1.02)]), 12, 0.03, 8, false), carbon);
  /* переднее крыло: основной элемент, три закрылка по бокам, щитки, пилоны к носу */
  add(hqFoil(0.32, 2.0, 0.04, 0.09), carbon, 0, 0.1, 3.5);
  const frontFlap = new THREE.Group(); frontFlap.position.set(0, 0, 3.2); g.add(frontFlap);
  for (const sx of [-1, 1]) [[0.24, 0.15, 0.2, 0.0], [0.19, 0.21, 0.36, -0.13], [0.15, 0.27, 0.55, -0.25]].forEach(([c, y, a, dz]) => { const m = new THREE.Mesh(hqFoil(c, 0.68, a, 0.08), paint); m.position.set(sx * 0.66, y - 0.0, dz); m.castShadow = true; frontFlap.add(m); });
  for (const sx of [-1, 1]) { add(hqPlate([[3.52, 0.06], [3.52, 0.19], [3.35, 0.37], [2.86, 0.4], [2.78, 0.27], [2.86, 0.06]], 0.02), accent, sx * 1.01, 0, 0);
    add(new THREE.BoxGeometry(0.03, 0.15, 0.18), carbon, sx * 0.08, 0.2, 3.22); }
  /* заднее крыло: основной элемент, закрылок (активная аэродинамика), щитки, балочное крыло, пилон, задний фонарь */
  add(hqFoil(0.36, 1.5, 0.22, 0.1), carbon, 0, 1.0, -2.22);
  const rearFlap = new THREE.Group(); rearFlap.position.set(0, 1.12, -2.48); g.add(rearFlap);
  { const m = new THREE.Mesh(hqFoil(0.24, 1.5, 0.62, 0.09), accent); m.castShadow = true; rearFlap.add(m); }
  for (const sx of [-1, 1]) add(hqPlate([[-2.12, 0.5], [-2.16, 1.2], [-2.3, 1.33], [-2.74, 1.34], [-2.8, 0.74], [-2.5, 0.46]], 0.02), paint, sx * 0.76, 0, 0);
  add(hqFoil(0.16, 0.9, 0.15, 0.1), carbon, 0, 0.55, -2.2); add(hqFoil(0.13, 0.9, 0.35, 0.1), carbon, 0, 0.64, -2.37);
  add(new THREE.BoxGeometry(0.03, 0.5, 0.14), carbon, 0, 0.82, -2.38);
  const rain = add(new THREE.BoxGeometry(0.12, 0.06, 0.03), new THREE.MeshBasicMaterial({ color: hqC('#ff2030', 5) }), 0, 0.5, -2.42, false);
  /* колёса: шина-лофт с боковиной, диск со спицами, цветная полоса состава */
  const prof = [[0.64, -0.5], [0.8, -0.5], [0.9, -0.48], [0.97, -0.42], [1.0, -0.3], [1.0, 0.3], [0.97, 0.42], [0.9, 0.48], [0.8, 0.5], [0.64, 0.5]].map(([r, y]) => new THREE.Vector2(r, y));
  const tyreG = new THREE.LatheGeometry(prof, 36), rubber = new THREE.MeshStandardMaterial({ map: hqTyreTex(), color: '#ffffff', roughness: 0.78, envMapIntensity: 0.5 });
  const band = new THREE.MeshStandardMaterial({ color: tyreColor, roughness: 0.45, envMapIntensity: 0.6 });
  const rimFace = new THREE.MeshStandardMaterial({ map: hqRimTex(), roughness: 0.32, metalness: 0.75, envMapIntensity: 1.1 }), nut = new THREE.MeshStandardMaterial({ color: acc, roughness: 0.3, metalness: 0.6 });
  const wheels = [];
  for (const [x, z, r, w] of [[1.02, 1.85, 0.36, 0.38], [-1.02, 1.85, 0.36, 0.38], [1.02, -1.55, 0.4, 0.5], [-1.02, -1.55, 0.4, 0.5]]) {
    const wg = new THREE.Group();
    const t = new THREE.Mesh(tyreG, rubber); t.scale.set(r, w, r); t.rotation.z = Math.PI / 2; t.castShadow = true; wg.add(t);
    for (const sd of [-1, 1]) { const b2 = new THREE.Mesh(new THREE.TorusGeometry(r * 0.83, 0.016, 5, 36), band); b2.rotation.y = Math.PI / 2; b2.position.x = sd * (w / 2 + 0.003); wg.add(b2);
      const face = new THREE.Mesh(new THREE.CircleGeometry(r * 0.64, 28), rimFace); face.rotation.y = sd * Math.PI / 2; face.position.x = sd * w * 0.36; wg.add(face); }
    const cn = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, w * 0.8, 10), nut); cn.rotation.z = Math.PI / 2; wg.add(cn);
    wg.position.set(x, r, z); g.add(wg); wheels.push(wg);
    /* подвеска: два треугольных рычага, тяга, рулевая */
    const sx = Math.sign(x), inX = z > 0 ? 0.24 : 0.2, hx = sx * (Math.abs(x) - w * 0.42);
    [[0.6, r + 0.13], [0.34, r - 0.13]].forEach(([yi, yo]) => { add(hqRod([sx * inX, yi, z + 0.22], [hx, yo, z], 0.018), carbon); add(hqRod([sx * inX, yi, z - 0.22], [hx, yo, z], 0.018), carbon); });
    add(hqRod([sx * inX, z > 0 ? 0.42 : 0.5, z + 0.05], [hx, r, z + 0.12], 0.013), carbon);
    add(new THREE.BoxGeometry(0.08, 0.26, 0.24), black, sx * (Math.abs(x) - w * 0.62), r, z, false);   /* тормозной воздуховод */
  }
  /* наклейки LapRadar: понтоны, щитки заднего крыла, плавник, закрылок сзади */
  { const m = brandMat(['#f8fafc', '#ffffff', '#fde047', '#facc15', '#84cc16'].includes(String(color).toLowerCase()) ? 'dark' : 'light');
    for (const sx of [-1, 1]) {
      const d = add(new THREE.PlaneGeometry(0.6, 0.15), m, sx * 0.945, 0.47, 0.2, false); d.rotation.y = sx * Math.PI / 2; d.renderOrder = 2;
      const e = add(new THREE.PlaneGeometry(0.5, 0.125), brandMat('light'), sx * 0.782, 1.02, -2.45, false); e.rotation.y = sx * Math.PI / 2; e.renderOrder = 2;
      const f = add(new THREE.PlaneGeometry(0.62, 0.15), m, sx * 0.011, 0.98, -1.35, false); f.rotation.y = sx * Math.PI / 2; f.rotation.z = sx * 0.12; f.renderOrder = 2; }
    const rw = new THREE.Mesh(new THREE.PlaneGeometry(1.2, 0.2), brandMat('light')); rw.position.set(0, 0.054 - 0.81 * 0.025, -0.109 - 0.58 * 0.025); rw.rotation.set(-0.95, Math.PI, 0); rw.renderOrder = 2; rearFlap.add(rw); }
  /* мягкая тень под машиной */
  const blob = new THREE.Mesh(new THREE.PlaneGeometry(2.7, 6.4), new THREE.MeshBasicMaterial({ map: hqBlob(), transparent: true, depthWrite: false, color: '#000000', opacity: 0.8 })); blob.rotation.x = -Math.PI / 2; blob.position.set(0, 0.025, 0.1); g.add(blob);
  g.scale.setScalar(1.15);
  return { group: g, wheels, rubber, band, frontFlap, rearFlap, helmet, rain, hq: true };
}

/* ---------- машина безопасности: своё спортивное купе со световой балкой, без логотипов ---------- */
function makeSCHQ() {
  const g = new THREE.Group(), body = new THREE.MeshPhysicalMaterial({ map: hqTex(512, 256, (c, w, h) => { c.fillStyle = '#c3c8d0'; c.fillRect(0, 0, w, h);
    c.fillStyle = '#f97316'; c.fillRect(0, h * 0.25, w * 0.06, h * 0.5); c.fillRect(w * 0.44, h * 0.25, w * 0.12, h * 0.5); c.fillRect(w * 0.94, h * 0.25, w * 0.06, h * 0.5);
    c.fillStyle = '#111318'; c.fillRect(w * 0.62, 0, w * 0.26, h); }, { rep: false }), roughness: 0.22, metalness: 0.65, clearcoat: 1, clearcoatRoughness: 0.05, envMapIntensity: 1.3 });
  const glass = new THREE.MeshPhysicalMaterial({ map: hqTex(256, 64, (c, w, h) => { c.fillStyle = '#0a0d14'; c.fillRect(0, 0, w, h); c.fillStyle = '#c3c8d0'; c.fillRect(w * 0.16, 0, w * 0.18, h); }, { rep: false }), roughness: 0.04, metalness: 0.5, clearcoat: 1, envMapIntensity: 1.6 });
  const dark = new THREE.MeshStandardMaterial({ color: '#0d0e11', roughness: 0.5 });
  const add = (geo, m, x = 0, y = 0, z = 0) => { const o = new THREE.Mesh(geo, m); o.position.set(x, y, z); o.castShadow = true; g.add(o); return o; };
  add(hqLoft([[2.32, 0.78, 0.1, 0.1, 0.44, 4], [2.16, 0.9, 0.18, 0.16, 0.47, 5], [1.5, 0.95, 0.24, 0.2, 0.5, 6], [0.6, 0.96, 0.32, 0.22, 0.52, 6], [-0.6, 0.97, 0.34, 0.22, 0.52, 6], [-1.7, 0.96, 0.33, 0.22, 0.52, 6], [-2.2, 0.9, 0.27, 0.19, 0.52, 5], [-2.34, 0.78, 0.16, 0.12, 0.52, 4]], 32), body);
  add(hqLoft([[0.8, 0.76, 0.01, 0.01, 0.83, 4], [0.25, 0.72, 0.36, 0.02, 0.83, 4], [-0.55, 0.68, 0.4, 0.02, 0.83, 4], [-1.3, 0.64, 0.24, 0.02, 0.83, 4], [-1.95, 0.6, 0.03, 0.02, 0.83, 4]], 32), glass);
  add(new THREE.BoxGeometry(1.7, 0.04, 0.22), dark, 0, 0.88, -2.28).rotation.x = -0.25;   /* спойлер */
  for (const sx of [-1, 1]) { const hl = add(new THREE.PlaneGeometry(0.38, 0.06), new THREE.MeshBasicMaterial({ color: hqC('#eaf2ff', 7) }), sx * 0.5, 0.47, 2.335);
    add(new THREE.BoxGeometry(0.16, 0.05, 0.05), dark, sx * 0.98, 0.95, 0.65); }
  add(new THREE.PlaneGeometry(1.5, 0.05), new THREE.MeshBasicMaterial({ color: hqC('#ff1f2e', 5), side: THREE.DoubleSide }), 0, 0.6, -2.345).rotation.y = Math.PI;
  add(new THREE.BoxGeometry(1.2, 0.08, 0.24), dark, 0, 1.27, -0.3);
  const bar = []; for (let i = 0; i < 6; i++) bar.push(add(new THREE.BoxGeometry(0.16, 0.06, 0.2), new THREE.MeshBasicMaterial({ color: hqC(i % 2 ? '#22e06a' : '#ffae1a', 4) }), -0.48 + i * 0.19, 1.33, -0.3));
  /* колёса в арках */
  const tyre = new THREE.MeshStandardMaterial({ map: hqTyreTex(), roughness: 0.8 }), rim = new THREE.MeshStandardMaterial({ map: hqRimTex(), roughness: 0.3, metalness: 0.8, envMapIntensity: 1.2 }), wheels = [];
  const prof = [[0.62, -0.5], [0.8, -0.5], [0.95, -0.44], [1, -0.3], [1, 0.3], [0.95, 0.44], [0.8, 0.5], [0.62, 0.5]].map(([r, y]) => new THREE.Vector2(r, y)), tg = new THREE.LatheGeometry(prof, 30);
  for (const [x, z] of [[0.87, 1.45], [-0.87, 1.45], [0.87, -1.45], [-0.87, -1.45]]) { const wg = new THREE.Group(), t = new THREE.Mesh(tg, tyre); t.scale.set(0.34, 0.26, 0.34); t.rotation.z = Math.PI / 2; t.castShadow = true; wg.add(t);
    const f = new THREE.Mesh(new THREE.CircleGeometry(0.21, 24), rim); f.rotation.y = Math.sign(x) * Math.PI / 2; f.position.x = Math.sign(x) * 0.1; wg.add(f); wg.position.set(x, 0.34, z); g.add(wg); wheels.push(wg);
    const arch = new THREE.Mesh(new THREE.CircleGeometry(0.46, 24, 0, Math.PI), dark); arch.position.set(Math.sign(x) * 0.958, 0.36, z); arch.rotation.y = Math.sign(x) * Math.PI / 2; g.add(arch); }
  { const t = hqTex(512, 64, (c, w, h) => { c.clearRect(0, 0, w, h); c.font = 'italic 900 50px Inter, sans-serif'; c.fillStyle = '#111318'; c.textAlign = 'center'; c.textBaseline = 'middle'; c.fillText('SAFETY CAR', w / 2, h / 2 + 2); }, { rep: false });
    for (const sx of [-1, 1]) { const d = new THREE.Mesh(new THREE.PlaneGeometry(1.5, 0.19), new THREE.MeshBasicMaterial({ map: t, transparent: true, depthWrite: false })); d.position.set(sx * 0.975, 0.55, -0.1); d.rotation.y = sx * Math.PI / 2; d.renderOrder = 2; g.add(d); } }
  const blob = new THREE.Mesh(new THREE.PlaneGeometry(2.4, 5.2), new THREE.MeshBasicMaterial({ color: '#000', transparent: true, depthWrite: false, map: hqBlob(), opacity: 0.85 })); blob.rotation.x = -Math.PI / 2; blob.position.y = 0.025; g.add(blob);
  const lights = [-0.45, 0.45].map(x => { const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowTex('rgba(255,190,60,1)', 'rgba(255,150,0,0)'), color: hqC('#ffffff', 2), transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false })); sp.position.set(x, 1.36, -0.3); sp.scale.set(1.6, 1.6, 1); g.add(sp); return sp; });
  g.scale.setScalar(1.1); g.visible = false; return { group: g, lights, wheels, bar };
}

/* ---------- Sphere в HQ: ярче (bloom), свои картинки на экране, лицом к камере ---------- */
function hqSphereShow(g, o, lt, W2, H2) {
  const cx = W2 / 2, cy = H2 * (o.y ?? 0.52), c = o.c || ['#1d4ed8', '#5b9bff', '#ffffff'], k = back(lt / 0.8) * (o.s ?? 1);   /* s — размер картинки, y — высота центра (0,5 — экватор) */
  const bg = g.createRadialGradient(cx, cy, 10, cx, cy, W2 * 0.3); bg.addColorStop(0, o.bg?.[0] || '#123a9c'); bg.addColorStop(1, o.bg?.[1] || '#050a24'); g.fillStyle = bg; g.fillRect(0, 0, W2, H2);
  const show = o.show;
  if (show === 'helmet') {   /* большой шлем в цветах LapRadar: синий, белый, голубой визор */
    g.save(); g.translate(cx, cy + 10); const s = 0.95 * k; g.scale(s, s * 1.15); g.rotate(Math.sin(lt * 0.8) * 0.05);
    const shell = () => { g.beginPath(); g.moveTo(-150, 60); g.bezierCurveTo(-170, -60, -90, -150, 10, -150); g.bezierCurveTo(120, -150, 175, -60, 165, 30); g.lineTo(150, 95); g.lineTo(-120, 105); g.closePath(); };
    shell(); g.fillStyle = c[0]; g.fill(); g.save(); shell(); g.clip(); g.fillStyle = c[2]; for (let i = -3; i < 4; i++) { g.save(); g.rotate(-0.5); g.fillRect(i * 70 + ((lt * 30) % 70), -300, 18, 600); g.restore(); }
    g.fillStyle = c[1]; g.fillRect(-200, 55, 400, 18); g.restore();
    g.beginPath(); g.moveTo(-10, -55); g.bezierCurveTo(70, -70, 140, -55, 162, -10); g.lineTo(158, 35); g.bezierCurveTo(100, 45, 20, 40, -15, 20); g.closePath(); const vg = g.createLinearGradient(0, -60, 0, 40); vg.addColorStop(0, '#9fe4ff'); vg.addColorStop(1, '#1b4fd8'); g.fillStyle = vg; g.fill();
    g.fillStyle = 'rgba(255,255,255,0.35)'; g.beginPath(); g.ellipse(-40, -100, 60, 16, -0.4, 0, 7); g.fill(); g.restore();
  } else if (show === 'number') {   /* большое светящееся число и подпись */
    g.save(); g.textAlign = 'center'; g.textBaseline = 'middle'; g.translate(cx, cy - 10); g.scale(k, k); let fs = 230; g.font = `900 ${fs}px Inter, sans-serif`; while (g.measureText(o.n || '').width > W2 * 0.42 && fs > 60) { fs -= 10; g.font = `900 ${fs}px Inter, sans-serif`; }
    g.shadowColor = c[1]; g.shadowBlur = 40; g.fillStyle = c[2]; g.fillText(String(o.n ?? ''), 0, 0); g.shadowBlur = 0;
    if (o.t) { g.font = '800 54px Inter, sans-serif'; g.fillStyle = c[1]; g.fillText(o.t, 0, fs * 0.62 + 10); } g.restore();
  } else if (show === 'swirl') {   /* разрешённые цвета: без красного, жёлтого и синего */
    const pal = o.c || ['#22c55e', '#a855f7', '#f8fafc', '#7e22ce']; g.fillStyle = '#0a0416'; g.fillRect(0, 0, W2, H2);
    for (let i = 0; i < 14; i++) { g.globalAlpha = 0.55; g.fillStyle = pal[i % pal.length]; g.beginPath(); g.ellipse((i * 97 + lt * 60) % (W2 + 200) - 100, H2 * (0.25 + 0.5 * hashK(i)), 150, 36, Math.sin(i + lt * 0.5) * 0.6, 0, 7); g.fill(); } g.globalAlpha = 1;
  } else if (show === 'sc') {   /* сообщение о машине безопасности */
    const on = 0.5 + 0.5 * Math.sin(lt * 5); g.fillStyle = `rgb(${Math.round(200 + 45 * on)},${Math.round(130 + 33 * on)},0)`;   /* мягкое мигание: без резких вспышек */ g.fillRect(0, 0, W2, H2); g.fillStyle = '#111'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.font = '900 120px Inter, sans-serif';
    for (let x = -W2; x < W2 * 2; x += 760) g.fillText(o.n || 'SAFETY CAR', x + ((lt * 120) % 760), cy);
  } else if (show === 'chequer') {   /* клетчатый флаг волной */
    const s = 40; for (let y = 0; y < H2; y += s) for (let x = 0; x < W2; x += s) { const wv = Math.sin(x * 0.012 + lt * 3) * 0.5 + 0.5; g.fillStyle = ((x / s + y / s) & 1) ? `rgb(${20 + 30 * wv},${20 + 30 * wv},${26 + 30 * wv})` : `rgb(${200 + 55 * wv},${200 + 55 * wv},${200 + 55 * wv})`; g.fillRect(x, y + Math.sin(x * 0.01 + lt * 3) * 10, s, s); }
  } else if (show === 'lights') {   /* стартовые огни: пять гаснут */
    const out = lt > (o.t0 ?? 2.6); if (out) return hqSphereShow(g, { ...o, show: 'swirl', c: o.c2 }, lt - (o.t0 ?? 2.6), W2, H2);   /* огни погасли — гонка пошла */
    const bgl = g.createLinearGradient(0, 0, 0, H2); bgl.addColorStop(0, '#0b1234'); bgl.addColorStop(0.5, '#141b44'); bgl.addColorStop(1, '#070a1c'); g.fillStyle = bgl; g.fillRect(0, 0, W2, H2); for (let i = 0; i < 5; i++) { const on = !out && lt > 0.4 + i * 0.45, q = o.s ?? 1, x = cx + (i - 2) * 92 * q; g.fillStyle = '#16181d'; g.fillRect(x - 38 * q, cy - 70 * q, 76 * q, 140 * q);
      for (const dy of [-25, 35]) { g.beginPath(); g.arc(x, cy + dy * q, 30 * q, 0, 7); g.fillStyle = on ? '#ff1e2e' : '#2a0b0e'; g.fill(); } }
  }
  g.fillStyle = 'rgba(0,0,0,0.22)'; for (let y = 0; y < H2; y += 4) g.fillRect(0, y + 3, W2, 1); for (let x = 0; x < W2; x += 4) g.fillRect(x + 3, 0, 1, H2);   /* сетка светодиодов */
}
function hqSphere(w, shot, lt, cam) {
  const sp = w.vx?.sphere; if (!sp || !shot.sphere) return;
  if (!sp.hq) { sp.hq = { base: sp.s.material.map, cv: document.createElement('canvas') }; sp.hq.cv.width = 1024; sp.hq.cv.height = 512; sp.hq.tex = new THREE.CanvasTexture(sp.hq.cv); sp.hq.tex.colorSpace = THREE.SRGBColorSpace; sp.hq.tex.anisotropy = 4;
    sp.s.material.color.setScalar(HQO.sphereK ?? 1.25); sp.halo.material.color.setScalar(0.6); }
  const o = typeof shot.sphere === 'object' ? shot.sphere : null;
  if (o?.show) { sp.s.material.map = sp.hq.tex; hqSphereShow(sp.hq.cv.getContext('2d'), o, lt, 1024, 512); sp.hq.tex.needsUpdate = true; sp.s.material.map.offset.x = 0;
    const d = cam.position.clone().sub(sp.s.position); sp.s.rotation.y = Math.atan2(-d.z, d.x) + (o.rot ?? 0); }
  else { sp.s.material.map = sp.hq.base; sp.s.rotation.y = 0; }
}

/* ---------- кадр HQ: тень ходит за машиной в кадре, точечный свет от ближайших фонарей, шлем скрыт в виде из кокпита ---------- */
function hqFrame(shot, lt, cam) {
  const w = world; if (!w.hq) return;
  const car = w.cars[shot.car ?? 0], st = car?.st;
  let f; if (st?.vis && ['chase', 'side', 'onboard', 'carorbit', 'flyby'].includes(shot.type)) f = st.pos.clone();
  else if (w.lastEx?.sc?.vis) f = w.lastEx.sc.pos.clone();
  else { const fw = new THREE.Vector3(); cam.getWorldDirection(fw); const t = fw.y < -0.05 ? Math.min(60, (cam.position.y - 0) / -fw.y) : 40; f = cam.position.clone().addScaledVector(fw, t); f.y = 0; }
  const k = w.hq.key; k.target.position.copy(f); k.position.copy(f).add(new THREE.Vector3(-14, 42, 10)); k.target.updateMatrixWorld();
  const lamps = w.hq.lamps; if (lamps.length) { const near = lamps.map(p => [p.distanceToSquared(f), p]).sort((a, b) => a[0] - b[0]); w.hq.pl.forEach((l, i) => { const p = near[i]?.[1]; if (p) l.position.copy(p); }); }
  w.cars.forEach(c => { if (c.helmet) c.helmet.visible = !(shot.type === 'onboard' && c === car); });
  if (w.sc?.wheels && w.lastEx?.sc?.vis) w.sc.wheels.forEach(wh => { wh.rotation.x = w.lastEx.sc.s / 0.374; });
  if (w.sc?.bar) w.sc.bar.forEach((b, i) => { b.visible = !!w.lastEx?.sc?.lights ? (Math.sin(lt * 14 + (i % 2) * Math.PI) > 0) : true; });
  if (w.vx?.sphere) hqSphere(w, shot, lt, cam);
}

/* ---------- новые камеры: низкий проезд сбоку, вид из кокпита через halo, пролёт мимо камеры, облёт машины ---------- */
function hqCamera(cam, shot, u, T, sc, lt) {
  const w = world, e = ease(u), c = w.cars[shot.car ?? 0], st = (shot.follow === 'sc' && w.lastEx?.sc?.vis && w.lastEx.sc) || c.st || trackPose(c.s0 + c.v * T, 0), L2 = (a, b, d) => lerp(shot[a] ?? d, shot[b] ?? shot[a] ?? d, e);
  let dir = st.dir; if (Number.isFinite(st.s)) { const p0 = w.at(st.s - 10).p, p1 = w.at(st.s + 6).p; dir = p1.clone().sub(p0).setY(0); dir = dir.lengthSq() > 1 ? dir.normalize() : st.dir; }
  const nn = new THREE.Vector3(-dir.z, 0, dir.x);
  if (shot.type === 'side') {   /* низкая камера едет рядом с машиной: side — сбоку (м), fw — вперёд/назад, h — высота */
    cam.position.copy(st.pos).addScaledVector(nn, L2('side', 'side2', 15)).addScaledVector(dir, L2('fw', 'fw2', 0)).setY(st.pos.y + L2('h', 'h2', 0.9));
    const lk = st.pos.clone().addScaledVector(dir, L2('look', 'look2', 1.5)); cam.lookAt(lk.x, st.pos.y + (shot.ly ?? 0.75), lk.z); cam.fov = L2('fov', 'fov2', 40);
  } else if (shot.type === 'onboard') {   /* глаза пилота: halo сверху кадра, нос и колёса внизу */
    c.group.updateMatrixWorld(true); const p = c.group.localToWorld(new THREE.Vector3(0, shot.eh ?? 1.0, shot.ez ?? -0.02)), t = c.group.localToWorld(new THREE.Vector3(shot.lx ?? 0, shot.ty ?? 0.95, 30));   /* lx > 0 — взгляд влево */
    p.y += 0.006 * Math.sin(T * 47) + 0.004 * Math.sin(T * 31); cam.position.copy(p); cam.lookAt(t); cam.fov = shot.fov ?? 70; cam.near = 0.05;
  } else if (shot.type === 'carorbit') {   /* облёт машины в движении: a — угол от направления «назад» */
    const a = L2('a0', 'a1', 0.6), r = L2('r', 'r2', 9), h = L2('h', 'h2', 2.2), back2 = dir.clone().multiplyScalar(-Math.cos(a)).addScaledVector(nn, Math.sin(a));
    cam.position.copy(st.pos).addScaledVector(back2, r).setY(st.pos.y + h); cam.lookAt(st.pos.x, st.pos.y + (shot.ly ?? 0.7), st.pos.z); cam.fov = shot.fov ?? 42;
  } else if (shot.type === 'flyby') {   /* камера стоит у трассы, машина проносится мимо */
    const tm = sc.dur * (shot.mid ?? 0.5), ps = actStates(shot, tm, T - lt + tm, sc.dur).cars[shot.car ?? 0], a = w.at(ps.s);
    cam.position.copy(a.p).addScaledVector(a.n, shot.side ?? 8.5).addScaledVector(a.t, shot.fw ?? 0).setY(a.p.y + (shot.h ?? 1.0));
    cam.lookAt(st.pos.x, st.pos.y + (shot.ly ?? 0.7), st.pos.z); cam.fov = L2('fov', 'fov2', 34);
  }
}

// ---------- кадр ----------
function sceneAt(i) { let k = 0; while (k + 1 < sceneStarts.length && sceneStarts[k + 1] <= i / fps) k++; return k; }
const camera = new THREE.PerspectiveCamera(50, W / H, 0.5, 20000);

function render3D(sc, lt, T) {
  let u = clamp(lt / sc.dur), shot = sc.shot || { type: 'fly', from: 0, to: 0.1 };
  /* TikTok-темп: длинную сцену с камерой «за машиной» сами режем на два ракурса */
  if (TT() && !shot.alt && !shot.noCut && shot.type === 'chase' && sc.dur > 4.6) shot = { ...shot, alt: [{ dist: (shot.dist ?? 14) * 2.4, dist2: (shot.dist2 ?? shot.dist ?? 14) * 2.0, h: (shot.h ?? 4) * 3.2, h2: (shot.h2 ?? shot.h ?? 4) * 2.6, side: -(shot.side ?? 0) * 2 - 4, side2: -(shot.side2 ?? shot.side ?? 0) * 2 - 2, look: (shot.look ?? 30) * 1.4 }] };
  if (shot.alt?.length) { const n = shot.alt.length + 1, k = Math.min(n - 1, Math.floor(u * n)); if (k > 0) shot = { ...shot, ...shot.alt[k - 1], act: shot.act, build: shot.build, hud: shot.hud }; u = clamp(u * n - k); }
  if (shot.type === 'stage') { renderStage(shot, u, lt, T); return; }
  if (shot.type === 'tyres' || shot.type === 'tyre') {
    const s = stage; const single = shot.type === 'tyre';
    s.tyres.forEach((t, k) => {
      if (single) { t.visible = k === (shot.hi ?? 0); t.position.set(0, -0.15, 0); t.rotation.set(0.15, -0.6 + u * 0.4, T * 3); t.scale.setScalar(0.85 * back(lt / 0.6)); }
      else { t.visible = true; const x = (k - 1) * 1.45, up = k === shot.hi ? easeOut((lt - 1.2) / 0.5) : 0; const appear = back((lt - k * 0.25) / 0.5);
        t.position.set(x, -0.1 + 0.3 * up, 0); t.scale.setScalar(0.66 * appear * (1 + 0.18 * up)); t.rotation.set(0.1, -0.45, T * (k === shot.hi ? 2.4 : 1)); }
    });
    if (shot.wear) { const t = s.tyres[shot.hi ?? 0], rub = t.children[0].material; rub.emissive.setRGB(1, 0.3, 0.06).multiplyScalar(0.85 * u * u); t.rotation.z = T * (3 + 6 * u);
      t.children.slice(1, 3).forEach(b => b.material.color.set(TYRE.soft).lerp(new THREE.Color('#3a1a1a'), u * 0.8));
      s.bits.forEach((b, j) => { const ph = ((lt * (0.9 + u * 1.5) + j / s.bits.length) % 1); b.visible = u > 0.25; b.position.set(0.15 + ph * 2.2 * (0.6 + hashK(j) * 0.6), -0.85 + ph * 1.4 - ph * ph * 1.6, (hashK(j + 9) - 0.5) * 0.7); b.scale.setScalar(0.6 + 1.6 * u); }); }
    else { s.bits.forEach(b => b.visible = false); s.tyres.forEach((t, k) => { t.children[0].material.emissive.setRGB(0, 0, 0); t.children.slice(1, 3).forEach(b => b.material.color.set([TYRE.soft, TYRE.medium, TYRE.hard][k])); }); }
    s.cam.position.set(Math.sin(u * 0.4 - 0.2) * 8.5, 1.1, Math.cos(u * 0.4 - 0.2) * 8.5); s.cam.lookAt(0, 0.05, 0); s.cam.fov = single ? 26 : 46; s.cam.updateProjectionMatrix();
    s.labels = s.tyres.map(t => { const v = t.position.clone().setY(t.position.y + 0.75).project(s.cam); return [(v.x + 1) / 2 * W, (1 - v.y) / 2 * H]; });
    draw(s.scene, s.cam); return;
  }
  const w = world;
  sc.fx = applyActs(sc.shot?.alt ? { ...shot, act: sc.shot.act } : shot, lt, T, sc.dur);
  w.glowLine.visible = shot.type === 'top' && shot.reveal;
  if (w.glowLine.visible) w.glowLine.geometry.setDrawRange(0, Math.floor(clamp(u * 1.4) * w.N) * 6);
  w.badges.forEach((b, k) => { b.s.visible = shot.type === 'top' && !!shot.badges && clamp(u * 1.4) * w.N > b.i; if (b.s.visible) { const sp = back(clamp((u * 1.4 * w.N - b.i) / 60)); b.s.scale.setScalar(Math.max(0.01, w.size.x * 0.06 * sp)); b.s.scale.z = 1; } });
  placeCamera(camera, shot, u, T, sc, lt);
  w.scene.fog.far = shot.type === 'top' || shot.type === 'orbit' ? 60000 : w.theme.fogF; w.scene.fog.near = shot.type === 'top' || shot.type === 'orbit' ? 40000 : w.theme.fogN;
  if (shot.rain || w.rain) { rainFx(w, shot, lt, camera); if (shot.rain) { w.scene.fog.near = Math.min(w.scene.fog.near, 260); w.scene.fog.far = Math.min(w.scene.fog.far, 2600); } }
  if (HQ) hqFrame(shot, lt, camera);
  draw(w.scene, camera);
}

function overlay(sc, lt, i) {
  const g = ctx; g.clearRect(0, 0, W, H); g.imageSmoothingQuality = 'high'; g.drawImage(gl, 0, 0, W, H);
  if (W > H) { // горизонтальный кадр для статьи: та же вёрстка, уменьшенная колонка по центру поверх широкой сцены
    const RW = W, RH = H, k = RH / 1920 * 1.21;
    const gr = g.createLinearGradient(0, 0, 0, RH); gr.addColorStop(0, 'rgba(0,0,0,0.55)'); gr.addColorStop(0.35, 'rgba(0,0,0,0)'); gr.addColorStop(0.7, 'rgba(0,0,0,0)'); gr.addColorStop(1, 'rgba(0,0,0,0.6)'); g.fillStyle = gr; g.fillRect(0, 0, RW, RH);
    g.save(); g.translate((RW - 1080 * k) / 2, -60 * k); g.scale(k, k); W = 1080; H = 1920;
    try { overlayBody(g, sc, lt, i, false); } finally { W = RW; H = RH; g.restore(); }
    const total = spec.scenes.reduce((a, s) => a + s.dur, 0); g.fillStyle = 'rgba(255,255,255,0.18)'; g.fillRect(0, 0, W, 6); g.fillStyle = '#3b82f6'; g.fillRect(0, 0, W * (i / fps) / total, 6);
    return;
  }
  overlayBody(g, sc, lt, i, true);
}
function overlayBody(g, sc, lt, i, portrait) {
  const kind = sc.kind; if (portrait) shade(g, true, true);
  if (kind !== 'end' && !spec.cover) (TT() ? brandTT(g) : brand(g)); else if (spec.cover) brand(g);
  if (spec.cover) { /* обложка для TikTok: крупный заголовок по центру (сетка профиля режет 3:4) */
    const gr = g.createLinearGradient(0, 0, 0, H); gr.addColorStop(0, 'rgba(5,8,16,0.15)'); gr.addColorStop(0.35, 'rgba(5,8,16,0.55)'); gr.addColorStop(0.65, 'rgba(5,8,16,0.55)'); gr.addColorStop(1, 'rgba(5,8,16,0.2)'); g.fillStyle = gr; g.fillRect(0, 0, W, H);
    g.textAlign = 'center'; g.textBaseline = 'middle'; const head = (spec.coverText || sc.head || '').toUpperCase(), words = head.split(/\s+/);
    let px = 210, lines; for (;;) { g.font = font(900, px); lines = []; let cur = ''; for (const wd of words) { const t = cur ? cur + ' ' + wd : wd; if (g.measureText(t).width > W - 120 && cur) { lines.push(cur); cur = wd; } else cur = t; } lines.push(cur); if (lines.length <= 3 && lines.every(l => g.measureText(l).width <= W - 100) || px < 90) break; px -= 10; }
    const y0 = 900 - (lines.length - 1) * px * 0.55;
    lines.forEach((l, k) => { g.lineWidth = px * 0.12; g.strokeStyle = 'rgba(0,0,0,0.75)'; g.lineJoin = 'round'; g.strokeText(l, W / 2, y0 + k * px * 1.08); g.fillStyle = k === lines.length - 1 ? '#ffd23f' : '#fff'; g.fillText(l, W / 2, y0 + k * px * 1.08); });
    if (sc.sub) { const yy = y0 + lines.length * px * 1.08 + 30; let fs = 62; g.font = font(800, fs); while (g.measureText(sc.sub).width > W - 170 && fs > 34) { fs -= 2; g.font = font(800, fs); } const tw = g.measureText(sc.sub).width; rrect(g, W / 2 - tw / 2 - 34, yy - fs * 0.8, tw + 68, fs * 1.6, fs * 0.8); g.fillStyle = '#3b82f6'; g.fill(); g.fillStyle = '#fff'; g.fillText(sc.sub, W / 2, yy); }
    g.textAlign = 'left'; g.textBaseline = 'alphabetic'; return; }
  if (kind === 'title' && !TT()) { const hh = popText(g, sc.head || '', W / 2, 330, 150, lt, { stagger: 0.12 }); if (sc.sub) popText(g, sc.sub, W / 2, Math.max(470, 330 + hh - 20), 54, lt - 0.6, { wgt: 700, color: '#cfd8ff' }); }
  if (sc.shot?.act?.type === 'cold') hudFrost(g, lt);
  if (kind !== 'end' && !sc.shot?.card && !sc.shot?.helmet) hudFor(g, sc, lt);
  if (sc.shot?.card) drawCard(g, sc.shot.card, lt, sc.dur); else if (sc.shot?.helmet) drawHelmet(g, sc.shot.helmet, lt);
  const chip = sc.chip || (TT() && kind === 'big' && sc.big) || (TT() && kind === 'title' && sc.head) || '';
  if (chip && kind !== 'end') drawChip(g, chip, lt, sc.shot?.hud ? 640 : (TT() ? 300 : 330));
  if (kind === 'end' && TT()) endTT(g, sc, lt);
  else if (kind === 'end') { g.fillStyle = 'rgba(5,8,16,0.55)'; g.fillRect(0, 0, W, H); const s = back(lt / 0.5); g.save(); g.translate(W / 2, 640); g.scale(s, s); logo(g, -110, -110, 3.45); g.restore();
    g.textAlign = 'center'; g.globalAlpha = clamp((lt - 0.35) * 3); g.font = font(900, 110); g.fillStyle = '#fff'; g.fillText('LAPRADAR', W / 2, 900); g.font = font(800, 72); g.fillStyle = '#5b9bff'; g.fillText('lapradar.com', W / 2, 1000);
    if (sc.tag) { g.font = font(700, 44); g.fillStyle = '#cfd8ff'; g.fillText(sc.tag, W / 2, 1080); } g.globalAlpha = 1; g.textAlign = 'left'; }
  if (TT()) captionsTT(g, sc.cap || sc.say, lt, sc.dur, sc.hl, kind === 'end' ? 1560 : 1330); else captions(g, sc.cap || sc.say, lt, sc.dur);
  if (!portrait) return;
  // прогресс ролика сверху
  const total = spec.scenes.reduce((a, s) => a + s.dur, 0); g.fillStyle = 'rgba(255,255,255,0.18)'; g.fillRect(0, 0, W, 8); g.fillStyle = '#3b82f6'; g.fillRect(0, 0, W * (i / fps) / total, 8);
}

window.setupVideo = async s => {
  spec = s; fps = s.fps || 30; W = s.w || 1080; H = s.h || 1920; camera.aspect = W / H;
  HQ = !!(s.hq || s.scenes.some(x => x.shot?.hq)); HQO = typeof s.hq === 'object' ? s.hq : {}; if (STG && (HQ || STG.hq)) STG = null;   /* HQ-режим: только если ролик его попросил */
  await document.fonts.load('900 40px Inter'); await document.fonts.load('800 40px Inter'); await document.fonts.load('700 40px Inter');
  /* q3d < 1: 3D рисуем в меньшем разрешении (дешевле), текст поверх — в полном */
  const q3 = s.q3d || 1; gl = document.createElement('canvas'); gl.width = Math.round(W * q3); gl.height = Math.round(H * q3);
  R = new THREE.WebGLRenderer({ canvas: gl, antialias: true, preserveDrawingBuffer: true, logarithmicDepthBuffer: true }); /* без мерцания плоских слоёв издалека */
  R.setSize(gl.width, gl.height, false); R.outputColorSpace = THREE.SRGBColorSpace;
  if (HQ) hqSetup();
  out = document.createElement('canvas'); out.width = W; out.height = H; ctx = out.getContext('2d'); document.body.appendChild(out);
  world = await buildWorld(s.track, s.theme); stage = buildStage();
  await loadMini(s.scenes.flatMap(x => x.shot?.hud?.names || []));
  await loadImgs(s.scenes.map(x => x.shot?.card?.img).filter(Boolean));
  sceneStarts = []; let t = 0; for (const sc of s.scenes) { sceneStarts.push(t); t += sc.dur; }
  return { frames: Math.round(t * fps), starts: sceneStarts };
};
window.renderFrame = (i, q = 0.9) => {
  const k = sceneAt(i), sc = spec.scenes[k], lt = i / fps - sceneStarts[k];
  render3D(sc, lt, i / fps + (sc.shot?.t0 ?? 0));
  if (spec.plain) return gl.toDataURL('image/jpeg', q); // иллюстрация к статье: без текста
  overlay(sc, lt, i);
  return out.toDataURL('image/jpeg', q);
};
window.studioReady = true;
window.__w = () => world;
window.__cam = () => camera;

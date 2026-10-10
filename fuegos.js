// ============================================================================
//  Fuegos artificiales — modulo reutilizable
// ----------------------------------------------------------------------------
//  Se usa al final de una partida para celebrarla. La pantalla queda cubierta de
//  fuegos y, mientras sigan encendidos, cada toque en la pantalla lanza mas.
//
//      import { encenderFuegos, apagarFuegos } from "../fuegos.js";
//      encenderFuegos();        // aparece y empieza solo
//      apagarFuegos();          // se quita y se detiene (no gasta bateria)
//
//  Notas:
//   - El lienzo va con `pointer-events:none`: NUNCA tapa un boton de la pagina.
//     Los toques se escuchan en el document, y se ignoran los que caen sobre un
//     boton o un enlace, para que "Aceptar" siga funcionando normal.
//   - El sonido se enciende solo con el primer toque (los navegadores no
//     dejan Sonar nada sin que el usuario toque algo). Se respeta la opcion
//     "fuegos_mute" del almacenamiento local.
// ============================================================================

let lienzo = null;
let ctx = null;
let fx = null;
let fctx = null;
let btnSonido = null;
let activo = false;

let W = 0, H = 0, dpr = 1;
let gradCielo = null, gradResplandor = null;
let calidad = 1;
let anterior = 0;
let acum = 0, cuadros = 0;
let proximoAuto = 0, proximoFinale = 0;
let rafId = 0;

const Z = 70;            // encima de los modales normales (60), sin taparlos

const particulas = [];
const cohetes = [];
const humos = [];
const destellos = [];
const estrellas = [];
let t = 0;

const PALETAS = [
  { h: [6, 30],     s: [82, 98],  l: [58, 70] },
  { h: [340, 360],  s: [76, 95],  l: [58, 70] },
  { h: [42, 60],    s: [88, 100], l: [60, 74] },
  { h: [94, 150],   s: [66, 90],  l: [56, 70] },
  { h: [166, 200],  s: [78, 97],  l: [58, 72] },
  { h: [202, 250],  s: [76, 95],  l: [62, 76] },
  { h: [266, 300],  s: [74, 94],  l: [64, 78] },
  { h: [312, 336],  s: [80, 97],  l: [60, 74] }
];

const azar = (a, b) => a + Math.random() * (b - a);
const azarInt = (a, b) => Math.floor(azar(a, b + 1));
const elegir = l => l[Math.floor(Math.random() * l.length)];
const T = Math.PI * 2;

function colorParticula() {
  const p = elegir(PALETAS);
  return {
    h: azarInt(p.h[0], p.h[1]),
    s: azarInt(p.s[0], p.s[1]),
    l: azarInt(p.l[0], p.l[1])
  };
}
function colorArcoiris() {
  return { h: azarInt(0, 359), s: azarInt(76, 100), l: azarInt(62, 78) };
}
function hsla(h, s, l, a) {
  return "hsla(" + h + "," + Math.round(s) + "%," + Math.round(l) + "%," + a.toFixed(3) + ")";
}

// ---------- sonido ----------
class Sonido {
  constructor() {
    this.ctx = null;
    let guardado = null;
    try { guardado = localStorage.getItem("fuegos_mute"); } catch (e) {}
    this.mudo = guardado === "1";
  }
  iniciar() {
    if (this.ctx) {
      if (this.ctx.state === "suspended") this.ctx.resume();
      return;
    }
    const AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return;
    try {
      this.ctx = new AC();
      this.master = this.ctx.createGain();
      this.master.gain.value = this.mudo ? 0 : 0.85;
      const comp = this.ctx.createDynamicsCompressor();
      comp.threshold.value = -14;
      comp.ratio.value = 9;
      this.master.connect(comp);
      comp.connect(this.ctx.destination);
    } catch (e) { this.ctx = null; }
  }
  preparar() {
    if (!this.ctx || this.ruido) return;
    const sr = this.ctx.sampleRate;
    const largo = Math.floor(sr * 2);
    const buf = this.ctx.createBuffer(1, largo, sr);
    const d = buf.getChannelData(0);
    let ultimo = 0;
    for (let i = 0; i < largo; i++) {
      ultimo = (ultimo + 0.02 * (Math.random() * 2 - 1)) / 1.02;
      d[i] = ultimo * 3.5;
    }
    this.ruido = buf;
  }
  pan(pos) {
    if (!this.ctx.createStereoPanner) return null;
    const p = this.ctx.createStereoPanner();
    p.pan.value = Math.max(-1, Math.min(1, pos));
    p.connect(this.master);
    return p;
  }
  boom(tam, pos) {
    if (!this.ctx || this.mudo) return;
    this.preparar();
    const t0 = this.ctx.currentTime;
    const dur = 0.45 + tam * 1.4;
    const vol = Math.min(0.85, 0.18 + tam * 0.5);
    const destino = this.pan(pos) || this.master;

    const osc = this.ctx.createOscillator();
    const g = this.ctx.createGain();
    osc.type = "sine";
    osc.frequency.setValueAtTime(130 * (1.3 - tam * 0.4), t0);
    osc.frequency.exponentialRampToValueAtTime(26, t0 + dur * 0.8);
    g.gain.setValueAtTime(0.0001, t0);
    g.gain.exponentialRampToValueAtTime(vol, t0 + 0.012);
    g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
    osc.connect(g).connect(destino);
    osc.start(t0);
    osc.stop(t0 + dur + 0.05);

    const s = this.ctx.createBufferSource();
    const f = this.ctx.createBiquadFilter();
    const gn = this.ctx.createGain();
    s.buffer = this.ruido;
    s.loop = true;
    f.type = "lowpass";
    f.frequency.setValueAtTime(3000, t0);
    f.frequency.exponentialRampToValueAtTime(170, t0 + dur * 0.7);
    gn.gain.setValueAtTime(0.0001, t0);
    gn.gain.exponentialRampToValueAtTime(vol * 0.9, t0 + 0.01);
    gn.gain.exponentialRampToValueAtTime(0.0001, t0 + dur * 0.9);
    s.connect(f).connect(gn).connect(destino);
    s.start(t0);
    s.stop(t0 + dur + 0.05);
  }
  silbido() {
    if (!this.ctx || this.mudo) return;
    this.preparar();
    const t0 = this.ctx.currentTime;
    const dur = 0.55;

    const osc = this.ctx.createOscillator();
    const g = this.ctx.createGain();
    osc.type = "sine";
    osc.frequency.setValueAtTime(680, t0);
    osc.frequency.exponentialRampToValueAtTime(1550, t0 + dur);
    g.gain.setValueAtTime(0.0001, t0);
    g.gain.exponentialRampToValueAtTime(0.1, t0 + dur * 0.7);
    g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
    osc.connect(g).connect(this.master);
    osc.start(t0);
    osc.stop(t0 + dur + 0.05);

    const s = this.ctx.createBufferSource();
    const f = this.ctx.createBiquadFilter();
    const gn = this.ctx.createGain();
    s.buffer = this.ruido;
    s.loop = true;
    f.type = "bandpass";
    f.Q.value = 3;
    f.frequency.setValueAtTime(1300, t0);
    f.frequency.exponentialRampToValueAtTime(3400, t0 + dur);
    gn.gain.setValueAtTime(0.0001, t0);
    gn.gain.exponentialRampToValueAtTime(0.06, t0 + dur * 0.6);
    gn.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
    s.connect(f).connect(gn).connect(this.master);
    s.start(t0);
    s.stop(t0 + dur + 0.05);
  }
  crepitar(cant, pos) {
    if (!this.ctx || this.mudo) return;
    this.preparar();
    const t0 = this.ctx.currentTime;
    const destino = this.pan(pos) || this.master;
    for (let i = 0; i < cant; i++) {
      const tt = t0 + Math.random() * 1.4;
      const s = this.ctx.createBufferSource();
      const f = this.ctx.createBiquadFilter();
      const g = this.ctx.createGain();
      s.buffer = this.ruido;
      s.playbackRate.value = azar(0.8, 1.7);
      f.type = "highpass";
      f.frequency.value = azar(1700, 4400);
      g.gain.setValueAtTime(azar(0.03, 0.11), tt);
      g.gain.exponentialRampToValueAtTime(0.0001, tt + 0.09);
      s.connect(f).connect(g).connect(destino);
      s.start(tt);
      s.stop(tt + 0.11);
    }
  }
}
const sonido = new Sonido();

// ---------- particulas ----------
function particula(x, y, vx, vy, c, opts) {
  const o = opts || {};
  particulas.push({
    x, y, vx, vy, c,
    vida: o.vida || azar(60, 110),
    edad: 0,
    tam: o.tam || azar(1.5, 3),
    brillo: o.brillo || azar(0.85, 1),
    parpadeo: o.parpadeo !== false,
    arrastre: o.arrastre || 0.977,
    gravedad: o.gravedad !== undefined ? o.gravedad : 0.05,
    estela: o.estela || 0,
    rama: o.rama || 0,
    destello: o.destello !== false,
    fase: Math.random() * T
  });
}
function directions(n) {
  const dirs = [];
  for (let i = 0; i < n; i++) {
    const th = Math.random() * T;
    const z = Math.random() * 2 - 1;
    const r = Math.sqrt(1 - z * z);
    dirs.push({ x: r * Math.cos(th), y: r * Math.sin(th) });
  }
  return dirs;
}

const FORMAS = {
  peonia(x, y, pot) {
    const n = azarInt(90, 150);
    const c = colorParticula();
    for (const d of directions(n)) {
      const v = azar(4.6, 8.2) * pot;
      particula(x, y, d.x * v, d.y * v - 0.4, c, {
        vida: azar(65, 105), tam: azar(1.8, 3.2),
        estela: azar(2.4, 4.2), gravedad: 0.042
      });
    }
  },
  crisantemo(x, y, pot) {
    const n = azarInt(110, 175);
    const base = colorParticula();
    for (const d of directions(n)) {
      const v = azar(4.2, 7.8) * pot;
      const c = Math.random() < 0.3 ? colorParticula() : base;
      particula(x, y, d.x * v, d.y * v - 0.4, c, {
        vida: azar(95, 150), tam: azar(1.4, 2.6),
        estela: azar(3.4, 6), gravedad: 0.046
      });
    }
  },
  dalia(x, y, pot) {
    const n = azarInt(65, 100);
    const capas = [colorParticula(), colorParticula(), colorParticula()];
    directions(n).forEach((d, i) => {
      const v = azar(3.4, 7) * pot * (i % 2 ? 1 : 0.7);
      particula(x, y, d.x * v, d.y * v - 0.4, capas[i % 3], {
        vida: azar(105, 155), tam: azar(2.2, 3.8),
        estela: azar(4, 7.5), gravedad: 0.04
      });
    });
  },
  anillo(x, y, pot) {
    const n = azarInt(85, 130);
    const c = colorParticula();
    const inclin = azar(-0.5, 0.5);
    for (let i = 0; i < n; i++) {
      const a = (i / n) * T + azar(-0.035, 0.035);
      const v = 7.4 * pot * azar(0.88, 1.12);
      particula(x, y, Math.cos(a) * v, Math.sin(a) * v * Math.cos(inclin) - 0.3, c,
        { vida: azar(70, 110), tam: azar(1.9, 3.2), estela: azar(3.4, 6), gravedad: 0.038 });
    }
  },
  willow(x, y, pot) {
    const n = azarInt(70, 110);
    const dorado = Math.random() < 0.72;
    for (const d of directions(n)) {
      const v = azar(2.6, 5.6) * pot;
      particula(x, y, d.x * v, d.y * v * 0.9, dorado
        ? { h: azarInt(36, 52), s: azarInt(84, 100), l: azarInt(60, 74) }
        : colorParticula(), {
          vida: azar(140, 210), tam: azar(1.5, 2.8),
          estela: azar(4.5, 8.5), gravedad: 0.08,
          arrastre: 0.986, brillo: 0.9
        });
    }
  },
  palma(x, y, pot) {
    const ramas = azarInt(8, 12);
    const c = colorParticula();
    for (let i = 0; i < ramas; i++) {
      const a = (i / ramas) * T + azar(-0.12, 0.12);
      const v = azar(5.4, 8.4) * pot;
      particula(x, y, Math.cos(a) * v, Math.sin(a) * v - 0.5, c, {
        vida: azar(115, 170), tam: azar(2.6, 4.2),
        estela: azar(5.5, 9), gravedad: 0.065, arrastre: 0.983
      });
      for (let j = 0; j < 4; j++) {
        const a2 = a + azar(-0.6, 0.6);
        const v2 = v * azar(0.42, 0.68);
        particula(x, y, Math.cos(a2) * v2, Math.sin(a2) * v2 - 0.4, c, {
          vida: azar(85, 130), tam: azar(1.6, 2.8),
          estela: azar(2.6, 5), gravedad: 0.055
        });
      }
    }
  },
  cruz(x, y, pot) {
    const n = azarInt(60, 92);
    const c = colorParticula();
    for (const d of directions(n)) {
      const v = azar(4, 7) * pot;
      particula(x, y, d.x * v, d.y * v - 0.4, c, {
        vida: azar(95, 145), tam: azar(2.2, 3.6),
        estela: azar(3.4, 6.5), gravedad: 0.044, rama: azarInt(32, 44)
      });
    }
  },
  corazon(x, y, pot) {
    const n = azarInt(85, 125);
    const c = colorParticula();
    for (let i = 0; i < n; i++) {
      const tt = (i / n) * T * 2;
      const hx = 16 * Math.pow(Math.sin(tt), 3);
      const hy = -(13 * Math.cos(tt) - 5 * Math.cos(2 * tt) - 2 * Math.cos(3 * tt) - Math.cos(4 * tt));
      const v = 0.22 * pot;
      particula(x, y, hx * v + azar(-0.5, 0.5), hy * v + azar(-0.5, 0.5) - 0.5, c, {
        vida: azar(105, 150), tam: azar(1.9, 3),
        estela: azar(2.8, 5), gravedad: 0.032, arrastre: 0.974
      });
    }
  },
  arcoiris(x, y, pot) {
    const n = azarInt(110, 170);
    const dirs = directions(n);
    const cols = [colorArcoiris(), colorArcoiris(), colorArcoiris(), colorArcoiris()];
    dirs.forEach((d, i) => {
      const v = azar(4.4, 8) * pot;
      particula(x, y, d.x * v, d.y * v - 0.4, cols[i % cols.length], {
        vida: azar(90, 140), tam: azar(2, 3.4),
        estela: azar(3.6, 6.5), gravedad: 0.04, brillo: 1
      });
    });
  },
  chispa(x, y, pot) {
    const n = azarInt(190, 300);
    const dirs = directions(n);
    const c1 = colorParticula();
    const c2 = colorParticula();
    for (let i = 0; i < n; i++) {
      const d = dirs[i % dirs.length];
      const v = azar(5, 9.5) * pot;
      particula(x, y, d.x * v, d.y * v - 0.5, i % 2 ? c1 : c2, {
        vida: azar(50, 92), tam: azar(1.1, 2.2),
        estela: azar(2, 3.8), gravedad: 0.052, brillo: 1
      });
    }
  },
  doble(x, y, pot) {
    FORMAS.anillo(x, y, pot * 0.85);
    const dx = azar(-90, 90), dy = azar(-60, 60);
    const color = colorParticula();
    destellos.push({ x, y, edad: 0, vida: 18, rmax: 90 * pot, col: color });
    setTimeout(() => FORMAS.peonia(x + dx, y + dy, pot * 0.9), 140);
  }
};

const CLAVES = Object.keys(FORMAS);
const PESOS = {
  peonia: 13, crisantemo: 16, dalia: 10, anillo: 11, willow: 9,
  palma: 9, cruz: 7, corazon: 5, arcoiris: 9, chispa: 11, doble: 4
};

function formaAleatoria() {
  let total = 0;
  for (const k of CLAVES) total += PESOS[k];
  let r = Math.random() * total;
  for (const k of CLAVES) {
    r -= PESOS[k];
    if (r <= 0) return k;
  }
  return "peonia";
}

function explode(x, y, opts) {
  const o = opts || {};
  const pot = o.pot || 1;
  const forma = o.forma || formaAleatoria();
  const pos = (x / Math.max(1, W)) * 2 - 1;

  if (FORMAS[forma]) FORMAS[forma](x, y, pot);

  humos.push({ x, y, r: azar(40, 70) * pot, vida: azar(90, 140), edad: 0 });
  destellos.push({ x, y, edad: 0, vida: 20, rmax: 150 * pot, col: null });

  sonido.boom(pot, pos);
  if (pot > 0.85 && Math.random() < 0.5) sonido.crepitar(azarInt(16, 34), pos);
}

function lanzar(x, destinoY, forma, tam) {
  const y0 = H + 8;
  const velocidad = Math.sqrt(Math.max(1, 2 * 0.16 * (y0 - destinoY)));
  const cohete = {
    x,
    y: y0,
    vx: azar(-0.6, 0.6),
    vy: -velocidad,
    forma: forma || null,
    tam: tam || azar(0.85, 1.15),
    cola: [],
    edad: 0,
    silbida: Math.random() < 0.5
  };
  if (cohete.silbida) sonido.silbido();
  cohetes.push(cohete);
}

function automatico() {
  const n = Math.random() < 0.35 ? 2 : 1;
  for (let i = 0; i < n; i++) {
    setTimeout(() => {
      if (!activo) return;
      lanzar(azar(W * 0.1, W * 0.9), azar(H * 0.07, H * 0.58), null, azar(0.9, 1.2));
    }, i * azarInt(140, 380));
  }
}

function iniciarFinale() {
  const cuenta = azarInt(8, 14);
  for (let i = 0; i < cuenta; i++) {
    setTimeout(() => {
      if (!activo) return;
      const forma = i % 4 === 0 ? "crisantemo" : i % 4 === 1 ? "dalia" : i % 4 === 2 ? "willow" : "arcoiris";
      lanzar(azar(W * 0.06, W * 0.94), azar(H * 0.06, H * 0.5), forma, azar(0.95, 1.3));
    }, i * azarInt(150, 280));
  }
}

function generarEstrellas() {
  estrellas.length = 0;
  const cant = Math.round((W * H) / 5200);
  for (let i = 0; i < cant; i++) {
    estrellas.push({
      x: Math.random() * W,
      y: Math.random() * H * 0.97,
      r: azar(0.4, 1.5),
      f: azar(0.4, 2),
      p: Math.random() * T,
      grande: Math.random() < 0.06
    });
  }
}

function redimensionar() {
  if (!ctx) return;
  dpr = Math.min(window.devicePixelRatio || 1, 2);
  W = window.innerWidth;
  H = window.innerHeight;
  lienzo.width = Math.floor(W * dpr);
  lienzo.height = Math.floor(H * dpr);
  lienzo.style.width = W + "px";
  lienzo.style.height = H + "px";
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  fx.width = lienzo.width;
  fx.height = lienzo.height;
  fctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  fctx.clearRect(0, 0, W, H);

  gradCielo = ctx.createLinearGradient(0, 0, 0, H);
  gradCielo.addColorStop(0, "#04050d");
  gradCielo.addColorStop(0.42, "#080a1c");
  gradCielo.addColorStop(0.78, "#100d2c");
  gradCielo.addColorStop(1, "#1b1440");

  gradResplandor = ctx.createRadialGradient(W * 0.5, H, 0, W * 0.5, H, H * 0.8);
  gradResplandor.addColorStop(0, "rgba(110,72,205,0.20)");
  gradResplandor.addColorStop(0.45, "rgba(84,56,175,0.07)");
  gradResplandor.addColorStop(1, "rgba(64,46,150,0)");

  generarEstrellas();
}

function dibujarCielo() {
  ctx.save();
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.fillStyle = gradCielo;
  ctx.fillRect(0, 0, W, H);
  ctx.fillStyle = gradResplandor;
  ctx.fillRect(0, 0, W, H);

  ctx.globalCompositeOperation = "lighter";
  for (const e of estrellas) {
    const a = 0.32 + 0.48 * (0.5 + 0.5 * Math.sin(t * e.f + e.p));
    const r = e.r;
    ctx.fillStyle = "rgba(226,232,255," + a.toFixed(3) + ")";
    ctx.beginPath();
    ctx.arc(e.x, e.y, r, 0, T);
    ctx.fill();
    if (e.grande) {
      ctx.strokeStyle = "rgba(210,225,255," + (a * 0.4).toFixed(3) + ")";
      ctx.lineWidth = 0.8;
      const L = r * 5;
      ctx.beginPath();
      ctx.moveTo(e.x - L, e.y); ctx.lineTo(e.x + L, e.y);
      ctx.moveTo(e.x, e.y - L); ctx.lineTo(e.x, e.y + L);
      ctx.stroke();
    }
  }
  ctx.globalCompositeOperation = "source-over";
  ctx.restore();
}

function pintarHumo() {
  ctx.save();
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  for (const h of humos) {
    const k = 1 - h.edad / h.vida;
    if (k <= 0) continue;
    const r = h.r * (1 + (1 - k) * 2.8);
    const a = k * k * 0.11;
    const g = ctx.createRadialGradient(h.x, h.y, 0, h.x, h.y, r);
    g.addColorStop(0, "rgba(172,168,202," + a.toFixed(3) + ")");
    g.addColorStop(0.55, "rgba(142,138,176," + (a * 0.45).toFixed(3) + ")");
    g.addColorStop(1, "rgba(120,118,155,0)");
    ctx.fillStyle = g;
    ctx.fillRect(h.x - r, h.y - r, r * 2, r * 2);
  }
  ctx.restore();
}

function actualizar() {
  for (let i = particulas.length - 1; i >= 0; i--) {
    const p = particulas[i];
    p.edad++;
    if (p.edad >= p.vida) { particulas.splice(i, 1); continue; }
    p.vy += p.gravedad;
    p.vx *= p.arrastre;
    p.vy *= p.arrastre;
    p.x += p.vx;
    p.y += p.vy;
    if (p.rama && p.edad === p.rama) {
      particulas.splice(i, 1);
      const c2 = colorParticula();
      for (let j = 0; j < 4; j++) {
        const a = (j / 4) * T + azar(-0.3, 0.3);
        const v = azar(2.2, 3.8);
        particula(p.x, p.y, Math.cos(a) * v, Math.sin(a) * v, c2, {
          vida: azar(55, 90), tam: p.tam * 0.9,
          estela: azar(2, 3.6), gravedad: 0.046
        });
      }
    }
  }

  for (let i = cohetes.length - 1; i >= 0; i--) {
    const c = cohetes[i];
    c.edad++;
    c.vy += 0.16;
    c.vx *= 0.995;
    c.y += c.vy;
    c.x += c.vx;
    c.cola.push({ x: c.x, y: c.y, a: 1 });
    if (c.cola.length > 16) c.cola.shift();
    for (const q of c.cola) q.a *= 0.87;

    if (c.vy >= -0.55 || c.y < H * 0.04) {
      explode(c.x, c.y, { forma: c.forma, pot: c.tam });
      cohetes.splice(i, 1);
      continue;
    }
    if (Math.random() < 0.6) {
      particula(
        c.x + azar(-1, 1), c.y,
        azar(-0.35, 0.35) - c.vx * 0.06, azar(-0.2, 0.5),
        { h: azarInt(18, 48), s: 96, l: azarInt(60, 76) },
        { vida: azar(16, 34), tam: azar(0.9, 1.7), gravedad: 0.028, arrastre: 0.945, destello: false }
      );
    }
  }

  for (let i = humos.length - 1; i >= 0; i--) {
    const h = humos[i];
    h.edad++;
    h.y -= 0.3;
    h.x += Math.sin(h.edad * 0.05) * 0.16;
    if (h.edad >= h.vida) humos.splice(i, 1);
  }

  for (let i = destellos.length - 1; i >= 0; i--) {
    destellos[i].edad++;
    if (destellos[i].edad >= destellos[i].vida) destellos.splice(i, 1);
  }
}

function pintar() {
  fctx.save();
  fctx.setTransform(dpr, 0, 0, dpr, 0, 0);

  fctx.globalCompositeOperation = "destination-out";
  fctx.fillStyle = "rgba(0,0,0,0.15)";
  fctx.fillRect(0, 0, W, H);

  fctx.globalCompositeOperation = "lighter";
  fctx.lineCap = "round";

  for (const d of destellos) {
    const k = 1 - d.edad / d.vida;
    const r = d.rmax * (0.25 + (1 - k) * 1.5);
    const a = k * k * 0.5;
    const g = fctx.createRadialGradient(d.x, d.y, 0, d.x, d.y, r);
    const c = d.col;
    g.addColorStop(0, "rgba(255,255,255," + a.toFixed(3) + ")");
    g.addColorStop(0.35, c
      ? hsla(c.h, c.s, 74, a * 0.6)
      : "rgba(200,215,255," + (a * 0.6).toFixed(3) + ")");
    g.addColorStop(1, "rgba(120,140,255,0)");
    fctx.fillStyle = g;
    fctx.fillRect(d.x - r, d.y - r, r * 2, r * 2);
  }

  for (const c of cohetes) {
    for (const q of c.cola) {
      if (q.a < 0.05) continue;
      fctx.strokeStyle = hsla(28, 96, 68, q.a);
      fctx.lineWidth = 3 * q.a;
      fctx.beginPath();
      fctx.moveTo(q.x, q.y);
      fctx.lineTo(q.x, q.y + 9 * q.a + 2);
      fctx.stroke();
    }
    fctx.fillStyle = "hsla(45,100%,92%,0.98)";
    fctx.beginPath();
    fctx.arc(c.x, c.y, 2.6, 0, T);
    fctx.fill();
  }

  for (const p of particulas) {
    const k = p.edad / p.vida;
    const vida = 1 - k;
    let a = vida * vida * p.brillo;
    if (p.parpadeo) a *= 0.66 + 0.34 * Math.sin(p.fase + k * 26);
    if (a < 0.012) continue;

    let l = p.c.l;
    let s = p.c.s;
    if (p.destello && k < 0.18) {
      const w = 1 - k / 0.18;
      l = l + (97 - l) * w;
      s = s * (1 - w * 0.55);
    }

    if (p.estela > 0) {
      const ex = p.x - p.vx * p.estela;
      const ey = p.y - p.vy * p.estela;
      const w0 = p.tam * vida + 0.35;

      if (calidad) {
        fctx.strokeStyle = hsla(p.c.h, s, l, a * 0.1);
        fctx.lineWidth = w0 * 4.4 + 2.4;
        fctx.beginPath();
        fctx.moveTo(p.x, p.y);
        fctx.lineTo(ex, ey);
        fctx.stroke();
      }
      fctx.strokeStyle = hsla(p.c.h, s, l, a * 0.42);
      fctx.lineWidth = w0 * 1.9;
      fctx.beginPath();
      fctx.moveTo(p.x, p.y);
      fctx.lineTo(ex, ey);
      fctx.stroke();

      fctx.strokeStyle = hsla(p.c.h, s, Math.min(99, l + 14), a);
      fctx.lineWidth = w0;
      fctx.beginPath();
      fctx.moveTo(p.x, p.y);
      fctx.lineTo(ex, ey);
      fctx.stroke();
    }

    const r0 = p.tam * vida + 0.5;
    if (calidad) {
      fctx.fillStyle = hsla(p.c.h, s, l, a * 0.14);
      fctx.beginPath();
      fctx.arc(p.x, p.y, r0 * 3.2, 0, T);
      fctx.fill();
    }
    fctx.fillStyle = hsla(p.c.h, s, Math.min(99, l + 10), a);
    fctx.beginPath();
    fctx.arc(p.x, p.y, r0, 0, T);
    fctx.fill();
  }

  fctx.restore();
}

function bucle(ahora) {
  if (!activo) return;
  rafId = requestAnimationFrame(bucle);

  const dt = ahora - anterior;
  anterior = ahora;
  t = ahora / 1000;

  acum += dt;
  cuadros++;
  if (cuadros >= 60) {
    const medio = acum / cuadros;
    if (medio > 27 && calidad === 1) calidad = 0;
    else if (medio < 16 && calidad === 0) calidad = 1;
    acum = 0;
    cuadros = 0;
  }

  if (ahora > proximoAuto) {
    automatico();
    proximoAuto = ahora + azar(700, 1900);
  }
  if (ahora > proximoFinale) {
    iniciarFinale();
    proximoFinale = ahora + azar(14000, 26000);
  }

  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.globalCompositeOperation = "source-over";
  ctx.globalAlpha = 1;
  ctx.fillStyle = "#04050c";
  ctx.fillRect(0, 0, lienzo.width, lienzo.height);

  dibujarCielo();
  actualizar();
  pintar();
  pintarHumo();

  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.globalCompositeOperation = "lighter";
  ctx.globalAlpha = 1;
  ctx.drawImage(fx, 0, 0, fx.width, fx.height, 0, 0, W, H);
  ctx.globalCompositeOperation = "source-over";
}

function crearLienzo() {
  if (lienzo) return;
  lienzo = document.createElement("canvas");
  lienzo.id = "lienzoFuegos";
  lienzo.setAttribute("aria-hidden", "true");
  lienzo.style.cssText =
    "position:fixed;left:0;top:0;width:100%;height:100%;pointer-events:none;" +
    "z-index:" + Z + ";display:none;background:#04050c;";
  ctx = lienzo.getContext("2d", { alpha: false });
  fx = document.createElement("canvas");
  fctx = fx.getContext("2d");
  document.body.appendChild(lienzo);
  window.addEventListener("resize", ()=>{ if(activo) redimensionar(); });
  crearBotonSonido();
}

// ---------- boton de silencio ----------
const SVG_ON =
  '<svg class="ico-on" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" ' +
  'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">' +
  '<path d="M11 5 6.5 8.8H3v6.4h3.5L11 19z"/>' +
  '<path d="M15.4 9.2a4 4 0 0 1 0 5.6"/>' +
  '<path d="M18.2 6.4a8 8 0 0 1 0 11.2"/></svg>';
const SVG_OFF =
  '<svg class="ico-off" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" ' +
  'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">' +
  '<path d="M11 5 6.5 8.8H3v6.4h3.5L11 19z"/>' +
  '<line x1="16" y1="9.5" x2="21" y2="14.5"/>' +
  '<line x1="21" y1="9.5" x2="16" y2="14.5"/></svg>';

function crearBotonSonido() {
  if (btnSonido) return;

  // Un solo <style>: el latido que avisa que el sonido todavia no arranca
  // porque falta un toque del usuario.
  if (!document.getElementById("fuegosCss")) {
    const st = document.createElement("style");
    st.id = "fuegosCss";
    st.textContent =
      "@keyframes fuegosLatir{0%,100%{opacity:.45}50%{opacity:1}}" +
      "#fuegosSonido.pidiendo{animation:fuegosLatir 1.2s ease-in-out infinite}" +
      "@media (prefers-reduced-motion: reduce){#fuegosSonido.pidiendo{animation:none}}" +
      "@media (max-width:520px){#fuegosSonido{right:14px !important;bottom:14px !important;" +
      "width:44px !important;height:44px !important}}" +
      "#fuegosSonido:active{transform:scale(.94)}";
    document.head.appendChild(st);
  }

  btnSonido = document.createElement("button");
  btnSonido.id = "fuegosSonido";
  btnSonido.type = "button";
  btnSonido.title = "Sonido";
  btnSonido.innerHTML = SVG_ON + SVG_OFF;
  // Va arriba del lienzo (Z+1) y en una esquina que no tapa el boton Aceptar.
  btnSonido.style.cssText =
    "position:fixed;right:18px;bottom:18px;width:48px;height:48px;border-radius:50%;padding:0;" +
    "border:1px solid #322a4a;background:rgba(32,25,51,.75);color:#f4f1fb;cursor:pointer;" +
    "backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);z-index:" + (Z + 1) + ";" +
    "display:none;place-items:center;transition:transform .18s ease,color .2s ease;";
  btnSonido.addEventListener("click", e=>{ e.stopPropagation(); alternarSonido(); });
  document.body.appendChild(btnSonido);
  pintarBoton();
}

function pintarBoton() {
  if (!btnSonido) return;
  const on = btnSonido.querySelector(".ico-on");
  const off = btnSonido.querySelector(".ico-off");
  if (sonido.mudo) {
    btnSonido.style.color = "#a599c7";
    on.style.display = "none";
    off.style.display = "block";
    btnSonido.title = "Activar sonido";
    btnSonido.setAttribute("aria-label", "Activar sonido");
  } else {
    btnSonido.style.color = "#f4f1fb";
    on.style.display = "block";
    off.style.display = "none";
    btnSonido.title = "Silenciar sonido";
    btnSonido.setAttribute("aria-label", "Silenciar sonido");
  }
  // Si aun no hay contexto corriendo, el boton late: es la unica pista de que
  // hace falta tocar algo para que se oiga.
  const corriendo = !!sonido.ctx && sonido.ctx.state === "running";
  btnSonido.classList.toggle("pidiendo", !sonido.mudo && !corriendo);
}

function alternarSonido() {
  const sinArrancar = !sonido.ctx;          // todavia no se toco nada
  sonido.iniciar();
  if (sinArrancar && !sonido.mudo) {
    // El primer toque solo prende el sonido (no lo apaga): asi de verdad se
    // oye la Celebration. Despues de esto, cada toque ya alterna.
    pintarBoton();
    sonido.boom(0.65, 0);
    return;
  }
  sonido.cambiar(!sonido.mudo);
  try { localStorage.setItem("fuegos_mute", sonido.mudo ? "1" : "0"); } catch (e) {}
  pintarBoton();
  if (!sonido.mudo) sonido.boom(0.65, 0);
}

// Un toque en la pantalla lanza mas fuegos. Los toques que caen sobre un boton o
// un enlace se dejan pasar: el boton "Aceptar" tiene que seguir sirviendo.
function alTocar(e) {
  if (!activo) return;
  const destino = e.target;
  if (destino && destino.closest && destino.closest("button, a, input, select, textarea, label")) return;
  sonido.iniciar();
  pintarBoton();
  const objetivo = Math.max(H * 0.05, Math.min(e.clientY, H * 0.72));
  lanzar(
    Math.max(10, Math.min(W - 10, e.clientX)),
    objetivo,
    Math.random() < 0.4 ? elegir(["crisantemo", "dalia", "anillo", "willow", "arcoiris"]) : null,
    azar(0.9, 1.25)
  );
}
document.addEventListener("pointerdown", alTocar);

// ---------- API ----------
/** Enciende los fuegos. Si ya estaban encendidos solo les da un empujon. */
export function encenderFuegos() {
  if (typeof document === "undefined" || !document.body) return;
  if (activo) {
    iniciarFinale();
    return;
  }
  crearLienzo();
  activo = true;
  lienzo.style.display = "block";
  if (btnSonido) btnSonido.style.display = "grid";
  redimensionar();
  pintarBoton();

  anterior = performance.now();
  acum = 0; cuadros = 0;
  proximoAuto = anterior + 600;
  proximoFinale = anterior + 11000;
  rafId = requestAnimationFrame(bucle);

  // Ráfaga de bienvenida.
  for (let i = 0; i < 4; i++) {
    setTimeout(()=>{
      if (!activo) return;
      lanzar(azar(W * 0.15, W * 0.85), azar(H * 0.08, H * 0.5),
        elegir(["crisantemo", "dalia", "willow", "arcoiris", "anillo"]), azar(1.05, 1.3));
    }, 180 + i * 320);
  }
}

/** Apaga los fuegos y los borra. La pagina queda como estaba. */
export function apagarFuegos() {
  if (!activo) {
    if (lienzo) lienzo.style.display = "none";
    if (btnSonido) btnSonido.style.display = "none";
    return;
  }
  activo = false;
  if (rafId) cancelAnimationFrame(rafId);
  rafId = 0;
  particulas.length = 0;
  cohetes.length = 0;
  humos.length = 0;
  destellos.length = 0;
  if (lienzo) lienzo.style.display = "none";
  if (btnSonido) btnSonido.style.display = "none";
}

/** ¿Están encendidos ahora mismo? */
export function fuegosEncendidos() { return activo; }
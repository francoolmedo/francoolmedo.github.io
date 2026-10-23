/* Autoruteo de una placa ESP32: grilla, A* por estados (celda, capa, dirección),
   giros de 45° como máximo, dos capas con vías y control DRC sobre la grilla.
   Todo se calcula en el navegador; nada está pregrabado. */
var Ruteo = (function () {
  'use strict';
  var W = 96, H = 64, N = W * H;
  var DX = [1, 1, 0, -1, -1, -1, 0, 1], DY = [0, 1, 1, 1, 0, -1, -1, -1];

  // ---------------------------------------------------------------- placa
  function placa() {
    var pads = [], comps = [], blk = [new Uint8Array(N), new Uint8Array(N)];
    function P(x, y, net, th) { var p = { x: x, y: y, c: y * W + x, net: net, th: !!th }; pads.push(p); return p; }
    function C(ref, x0, y0, x1, y1, txt) { comps.push({ ref: ref, x0: x0, y0: y0, x1: x1, y1: y1, txt: txt || '' }); }
    function zona(x0, y0, x1, y1, capas) {
      for (var y = y0; y <= y1; y++) for (var x = x0; x <= x1; x++) capas.forEach(function (l) { blk[l][y * W + x] = 1; });
    }
    var i;
    // U1: ESP32-WROOM-32, 38 pines (14 + 14 + 10). Antena con zona libre en las dos capas.
    C('U1', 36, 2, 60, 40, 'ESP32-WROOM-32');
    zona(37, 9, 59, 39, [0]);
    zona(35, 0, 61, 8, [0, 1]);
    var perm = [0, 1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10];
    P(36, 10, 'VCC');
    for (i = 0; i < 12; i++) P(36, 12 + 2 * i, 'J1_' + perm[i]);
    P(36, 36, 'C2N');
    for (i = 0; i < 8; i++) P(60, 10 + 2 * i, 'R' + i);
    for (i = 0; i < 6; i++) P(60, 26 + 2 * i, 'U3_' + i);
    for (i = 0; i < 10; i++) P(39 + 2 * i, 40, 'J2_' + i);
    // J1: tira de 12 pines (agujero pasante)
    C('J1', 7, 11, 9, 35);
    for (i = 0; i < 12; i++) P(8, 12 + 2 * i, 'J1_' + i, 1);
    // Fuente: U4 regulador, C1, J5 entrada
    C('U4', 7, 1, 17, 5, 'LDO'); P(8, 3, 'VIN'); P(12, 3, 'GND'); P(16, 3, 'VCC');
    C('C1', 21, 3, 27, 5); P(22, 4, 'VCC'); P(26, 4, 'GND');
    C('J5', 2, 51, 4, 57); P(3, 52, 'VIN', 1); P(3, 56, 'GND', 1);
    C('C2', 21, 45, 27, 47); P(22, 46, 'C2N'); P(26, 46, 'GND');
    // R1-R8, D1-D8, J3
    for (i = 0; i < 8; i++) {
      var y = 9 + 3 * i;
      C(i % 7 ? '' : 'R' + (i + 1), 67, y - 1, 73, y + 1); P(68, y, 'R' + i); P(72, y, 'L' + i);
      C(i % 7 ? '' : 'D' + (i + 1), 77, y - 1, 83, y + 1); P(78, y, 'L' + i); P(82, y, 'K' + i);
    }
    C('J3', 91, 9, 93, 27);
    for (i = 0; i < 9; i++) P(92, 10 + 2 * i, i < 8 ? 'K' + i : 'GND', 1);
    // U3: sensor SOIC-8
    C('U3', 67, 41, 75, 47, 'SOIC-8');
    for (i = 0; i < 4; i++) P(68 + 2 * i, 42, 'U3_' + i);
    P(68, 46, 'U3_4'); P(70, 46, 'U3_5'); P(72, 46, 'S0'); P(74, 46, 'S1');
    C('J4', 71, 57, 93, 59);
    ['S0', 'S1', 'VCC', 'GND', '', ''].forEach(function (n, k) { P(72 + 4 * k, 58, n, 1); });
    C('J2', 21, 57, 59, 59);
    for (i = 0; i < 10; i++) P(22 + 4 * i, 58, 'J2_' + i, 1);
    // U5: memoria SOIC-8, R9-R10, J6
    C('U5', 8, 41, 16, 49, 'SOIC-8');
    for (i = 0; i < 4; i++) P(8, 42 + 2 * i, 'F' + i);
    P(16, 42, 'VCC'); P(16, 44, 'P1'); P(16, 46, 'P2'); P(16, 48, 'GND');
    C('R9', 23, 49, 29, 51); P(24, 50, 'P1'); P(28, 50, 'VCC');
    C('R10', 23, 52, 29, 54); P(24, 53, 'P2'); P(28, 53, 'VCC');
    C('J6', 3, 60, 17, 62);
    for (i = 0; i < 4; i++) P(4 + 4 * i, 61, 'F' + i, 1);
    return { pads: pads, comps: comps, blk: blk };
  }

  function oct(a, b) {
    var dx = Math.abs(a.x - b.x), dy = Math.abs(a.y - b.y);
    return Math.max(dx, dy) + 0.4142 * Math.min(dx, dy);
  }

  // Conexiones: árbol de expansión mínima por red (Prim). Una red de k pines da k-1 conexiones.
  function conexiones(pads) {
    var redes = {}, out = [];
    pads.forEach(function (p) { if (p.net) (redes[p.net] = redes[p.net] || []).push(p); });
    Object.keys(redes).forEach(function (n) {
      var r = redes[n], dentro = [r[0]], fuera = r.slice(1);
      while (fuera.length) {
        var best = null, bd = 1e9;
        dentro.forEach(function (a) { fuera.forEach(function (b) { var d = oct(a, b); if (d < bd) { bd = d; best = [a, b]; } }); });
        out.push({ net: n, a: best[0], b: best[1], len: bd });
        dentro.push(best[1]); fuera.splice(fuera.indexOf(best[1]), 1);
      }
    });
    out.sort(function (p, q) { return p.len - q.len; });
    return out;
  }

  // ---------------------------------------------------------------- A*
  function Router(B) {
    this.B = B;
    this.occ = [new Int16Array(N), new Int16Array(N)];
    this.id = {}; var k = 1, self = this;
    B.pads.forEach(function (p) {
      var n = p.net || ('nc' + k);
      if (!self.id[n]) self.id[n] = k++;
      p.id = self.id[n];
      self.occ[0][p.c] = p.id; if (p.th) self.occ[1][p.c] = p.id;
    });
    var S = 2 * N * 9;
    this.g = new Float32Array(S); this.from = new Int32Array(S);
    this.seen = new Uint16Array(S); this.closed = new Uint16Array(S); this.stamp = 0;
    this.hk = []; this.hv = [];
  }
  Router.prototype.libre = function (l, c, n) {
    if (this.B.blk[l][c]) return false;
    var x = c % W, y = (c / W) | 0, o = this.occ[l];
    for (var dy = -1; dy <= 1; dy++) {
      var yy = y + dy; if (yy < 0 || yy >= H) continue;
      for (var dx = -1; dx <= 1; dx++) {
        var xx = x + dx; if (xx < 0 || xx >= W) continue;
        var v = o[yy * W + xx]; if (v && v !== n) return false;
      }
    }
    return true;
  };
  Router.prototype.push = function (f, s) {
    var k = this.hk, v = this.hv, i = k.length; k.push(f); v.push(s);
    while (i > 0) { var p = (i - 1) >> 1; if (k[p] <= f) break; k[i] = k[p]; v[i] = v[p]; i = p; }
    k[i] = f; v[i] = s;
  };
  Router.prototype.pop = function () {
    var k = this.hk, v = this.hv, top = v[0], lf = k.pop(), ls = v.pop(), n = k.length;
    if (n) {
      var i = 0;
      for (;;) {
        var l = 2 * i + 1; if (l >= n) break;
        if (l + 1 < n && k[l + 1] < k[l]) l++;
        if (k[l] >= lf) break;
        k[i] = k[l]; v[i] = v[l]; i = l;
      }
      k[i] = lf; v[i] = ls;
    }
    return top;
  };
  // Rutea una conexión. Devuelve {ok, path:[[capa,celda],...], vistos:[celdas]}.
  Router.prototype.ruta = function (cx) {
    var st = ++this.stamp, a = cx.a, b = cx.b, n = a.id, self = this;
    var g = this.g, from = this.from, seen = this.seen, closed = this.closed;
    var bx = b.x, by = b.y, bl = b.th ? 2 : 0, vistos = [];
    this.hk.length = 0; this.hv.length = 0;
    function h(c) { var dx = Math.abs(c % W - bx), dy = Math.abs(((c / W) | 0) - by); return Math.max(dx, dy) + 0.4142 * Math.min(dx, dy); }
    function abrir(s, gg, prev, c) {
      if (seen[s] === st && g[s] <= gg) return;
      seen[s] = st; g[s] = gg; from[s] = prev; self.push(gg + h(c), s);
    }
    var capas = a.th ? [0, 1] : [0];
    capas.forEach(function (l) { abrir((l * N + a.c) * 9 + 8, 0, -1, a.c); });
    var fin = -1, guard = 0;
    while (this.hv.length && guard++ < 400000) {
      var s = this.pop();
      if (closed[s] === st) continue;
      closed[s] = st;
      var d = s % 9, lc = (s - d) / 9, l = lc >= N ? 1 : 0, c = lc - l * N;
      if (c === b.c && (l === 0 || bl)) { fin = s; break; }
      if (d === 8 || vistos.length < 6000) vistos.push(c);
      var x = c % W, y = (c / W) | 0, gs = g[s];
      var dirs = d === 8 ? [0, 1, 2, 3, 4, 5, 6, 7] : [d, (d + 1) & 7, (d + 7) & 7];
      for (var i = 0; i < dirs.length; i++) {
        var nd = dirs[i], nx = x + DX[nd], ny = y + DY[nd];
        if (nx < 1 || ny < 1 || nx >= W - 1 || ny >= H - 1) continue;
        var nc = ny * W + nx;
        if (!this.libre(l, nc, n)) continue;
        var cost = (nd & 1 ? 1.4142 : 1) + (d !== 8 && nd !== d ? 0.6 : 0) + l * 0.2;
        abrir(((l * N + nc) * 9) + nd, gs + cost, s, nc);
      }
      // Vía: cambia de capa en la misma celda. No se pone sobre un pad.
      if (d !== 8 && !this.occ[0][c] && !this.occ[1][c]) {
        var ol = 1 - l;
        if (this.libre(ol, c, n)) abrir((ol * N + c) * 9 + 8, gs + 9, s, c);
      }
    }
    if (fin < 0) return { ok: false, path: [], vistos: vistos };
    var path = [];
    for (var t = fin; t >= 0; t = from[t]) { var dd = t % 9, q = (t - dd) / 9; path.push([q >= N ? 1 : 0, q % N]); }
    path.reverse();
    path.forEach(function (p) { self.occ[p[0]][p[1]] = n; });
    return { ok: true, path: path, vistos: vistos };
  };
  // DRC: cobre de redes distintas en celdas vecinas (misma capa) es una violación.
  Router.prototype.drc = function () {
    var err = 0;
    for (var l = 0; l < 2; l++) {
      var o = this.occ[l];
      for (var c = 0; c < N; c++) {
        var v = o[c]; if (!v) continue;
        var x = c % W, y = (c / W) | 0;
        // vecinos hacia adelante: cada par se cuenta una vez
        var vec = [[1, 0], [-1, 1], [0, 1], [1, 1]];
        for (var i = 0; i < 4; i++) {
          var xx = x + vec[i][0], yy = y + vec[i][1];
          if (xx < 0 || xx >= W || yy >= H) continue;
          var u = o[yy * W + xx]; if (u && u !== v) err++;
        }
      }
    }
    return err;
  };

  // Reduce un camino de celdas a vértices (cambios de dirección o de capa).
  function tramos(path) {
    var out = [], cur = null, prev = null, pd = -1;
    path.forEach(function (p) {
      var x = p[1] % W, y = (p[1] / W) | 0;
      if (prev && p[0] !== prev[0]) { out.push(cur); out.push({ via: [x, y] }); cur = { l: p[0], pts: [[x, y]] }; pd = -1; prev = p; return; }
      if (!cur) cur = { l: p[0], pts: [[x, y]] };
      else {
        var px = prev[1] % W, py = (prev[1] / W) | 0, d = (x - px + 1) * 3 + (y - py + 1);
        if (d === pd) cur.pts[cur.pts.length - 1] = [x, y]; else cur.pts.push([x, y]);
        pd = d;
      }
      prev = p;
    });
    if (cur) out.push(cur);
    return out;
  }

  // Pasadas con prioridad: lo que falló en una pasada se rutea primero en la siguiente.
  // Se avanza de a una conexión por llamada a paso(), para no trabar la página.
  function Pasos(B, max) {
    this.B = B; this.max = max || 6; this.orden = conexiones(B.pads); this.pasadas = []; this.fin = false; this.nueva();
  }
  Pasos.prototype.nueva = function () { this.r = new Router(this.B); this.res = []; this.malas = []; this.i = 0; };
  Pasos.prototype.paso = function () {
    if (this.fin) return true;
    var cx = this.orden[this.i++], q = this.r.ruta(cx);
    q.cx = cx; this.res.push(q); if (!q.ok) this.malas.push(cx);
    if (this.i < this.orden.length) return false;
    this.pasadas.push(this.orden.length - this.malas.length);
    if (!this.malas.length || this.pasadas.length >= this.max) return (this.fin = true);
    var m = this.malas;
    this.orden = m.concat(this.orden.filter(function (c) { return m.indexOf(c) < 0; }));
    this.nueva();
    return false;
  };

  return { W: W, H: H, placa: placa, conexiones: conexiones, Router: Router, tramos: tramos, Pasos: Pasos };
})();
if (typeof module !== 'undefined') module.exports = Ruteo;

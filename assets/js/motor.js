/* Animaciones del sitio: autoruteo (portada), osciloscopio, Ladder y agentes.
   Con prefers-reduced-motion todo queda quieto y legible. */
(function () {
  'use strict';
  var RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var EN = document.documentElement.lang === 'en';
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return [].slice.call((r || document).querySelectorAll(s)); }
  function fmt(v, d) { var s = v.toFixed(d); return EN ? s : s.replace('.', ','); }
  function dpr() { return Math.min(window.devicePixelRatio || 1, 2); }
  function lienzo(cv) {
    var r = cv.getBoundingClientRect(), k = dpr();
    cv.width = Math.round(r.width * k); cv.height = Math.round(r.height * k);
    var g = cv.getContext('2d'); g.setTransform(k, 0, 0, k, 0, 0);
    return { g: g, w: r.width, h: r.height, k: k };
  }
  function enVista(el, cb) {
    if (!('IntersectionObserver' in window)) return cb(true);
    new IntersectionObserver(function (es) { cb(es[0].isIntersecting); }, { threshold: 0.1 }).observe(el);
  }
  function alCambiarAncho(cb) {
    var w = innerWidth, t = 0;
    addEventListener('resize', function () {
      clearTimeout(t);
      t = setTimeout(function () { if (innerWidth !== w) { w = innerWidth; cb(); } }, 150);
    });
  }
  var MONO = '"Plex Mono", ui-monospace, monospace';

  // ------------------------------------------------------------ 1. autoruteo
  function ruteo() {
    var fig = $('#ruteo'); if (!fig || !window.Ruteo) return;
    var cv = $('canvas', fig), hud = $('.hud-n', fig), btn = $('.again', fig), d = fig.dataset;
    var W = Ruteo.W, H = Ruteo.H, C = {
      board: '#1a1e1b', grid: '#2c332d', silk: 'rgba(232,228,214,.5)', top: '#e3894b', bot: '#5f93c4',
      pad: '#d8b46c', hole: '#1a1e1b', seen: 'rgba(240,164,107,.28)'
    };
    var L, s, fondo, B, pasos, calc, res, total, hecho = false, vis = true, raf = 0, ms = 0, last = 0;
    var PER = 85; // ms por conexión en la animación

    function px(v) { return (v + 0.5) * s; }
    function medir() { L = lienzo(cv); s = L.w / W; fondo = null; }
    function dibujarFondo() {
      var o = document.createElement('canvas'); o.width = cv.width; o.height = cv.height;
      var g = o.getContext('2d'); g.setTransform(L.k, 0, 0, L.k, 0, 0);
      g.fillStyle = C.board; g.fillRect(0, 0, L.w, L.h);
      g.fillStyle = C.grid;
      for (var y = 0; y < H; y += 4) for (var x = 0; x < W; x += 4) g.fillRect(px(x) - 0.5, px(y) - 0.5, 1, 1);
      // zona de antena: sin cobre en ninguna capa
      g.save(); g.beginPath(); g.rect(35 * s, 0, 27 * s, 9 * s); g.clip();
      g.strokeStyle = 'rgba(232,228,214,.16)'; g.lineWidth = 1;
      for (var h = 0; h < 40; h += 1.5) { g.beginPath(); g.moveTo((35 + h) * s, 0); g.lineTo((26 + h) * s, 9 * s); g.stroke(); }
      g.restore();
      g.strokeStyle = C.silk; g.fillStyle = C.silk; g.lineWidth = 1;
      g.font = Math.max(7, s * 1.9) + 'px ' + MONO; g.textBaseline = 'top';
      B.comps.forEach(function (c) {
        g.strokeRect(c.x0 * s + 0.5, c.y0 * s + 0.5, (c.x1 - c.x0 + 1) * s - 1, (c.y1 - c.y0 + 1) * s - 1);
        if (c.ref === 'U1') {
          g.textAlign = 'center'; g.fillText('U1', 48.5 * s, 18 * s); g.fillText(c.txt, 48.5 * s, 21 * s); g.textAlign = 'left';
        } else if (c.ref) g.fillText(c.ref, c.x0 * s + 2, c.y1 * s + s + 2 > L.h - 8 ? c.y0 * s - s * 2 : c.ref === 'R1' || c.ref === 'D1' ? c.y0 * s - s * 2.2 : c.y1 * s + s + 1);
      });
      B.pads.forEach(function (p) {
        g.fillStyle = C.pad;
        if (p.th) {
          g.beginPath(); g.arc(px(p.x), px(p.y), s * 0.85, 0, 7); g.fill();
          g.fillStyle = C.hole; g.beginPath(); g.arc(px(p.x), px(p.y), s * 0.32, 0, 7); g.fill();
        } else g.fillRect(px(p.x) - s * 0.62, px(p.y) - s * 0.62, s * 1.24, s * 1.24);
      });
      fondo = o;
    }
    // Dibuja los primeros k pasos de cada camino, capa inferior primero.
    function pistas(g, lista) {
      g.lineCap = 'round'; g.lineJoin = 'round'; g.lineWidth = Math.max(1, s * 0.78);
      [1, 0].forEach(function (capa) {
        g.strokeStyle = capa ? C.bot : C.top; g.globalAlpha = capa ? 0.9 : 1; g.beginPath();
        lista.forEach(function (it) {
          var p = it[0], k = it[1];
          for (var i = 0; i < k; i++) {
            var c = p[i][1], x = px(c % W), y = px((c / W) | 0);
            if (p[i][0] !== capa) continue;
            if (i && p[i - 1][0] === capa) g.lineTo(x, y); else g.moveTo(x, y);
          }
        });
        g.stroke();
      });
      g.globalAlpha = 1;
      lista.forEach(function (it) {
        var p = it[0];
        for (var i = 1; i < it[1]; i++) if (p[i][0] !== p[i - 1][0]) {
          var c = p[i][1], x = px(c % W), y = px((c / W) | 0);
          g.fillStyle = '#cfc8b6'; g.beginPath(); g.arc(x, y, s * 0.8, 0, 7); g.fill();
          g.fillStyle = C.board; g.beginPath(); g.arc(x, y, s * 0.3, 0, 7); g.fill();
        }
      });
    }
    function pintar() {
      if (!fondo) dibujarFondo();
      var g = L.g; g.setTransform(1, 0, 0, 1, 0, 0); g.drawImage(fondo, 0, 0); g.setTransform(L.k, 0, 0, L.k, 0, 0);
      if (!res) return;
      var n = hecho ? total : Math.min(total, Math.floor(ms / PER)), f = hecho ? 0 : (ms / PER) - n, lista = [];
      for (var i = 0; i < n; i++) lista.push([res[i].path, res[i].path.length]);
      if (n < total) {
        var q = res[n];
        if (f < 0.45) { // A* explorando: celdas cerradas hasta ahora
          var v = q.vistos, m = Math.floor(v.length * f / 0.45);
          g.fillStyle = C.seen;
          for (var j = 0; j < m; j++) g.fillRect(px(v[j] % W) - s * 0.3, px((v[j] / W) | 0) - s * 0.3, s * 0.6, s * 0.6);
        } else lista.push([q.path, Math.ceil(q.path.length * (f - 0.45) / 0.55)]);
      }
      pistas(g, lista);
      var ok = 0; for (i = 0; i < n; i++) if (res[i].ok) ok++;
      if (hecho) {
        var vias = 0; res.forEach(function (q) { for (var i = 1; i < q.path.length; i++) if (q.path[i][0] !== q.path[i - 1][0]) vias++; });
        hud.innerHTML = '<b>' + ok + '/' + total + '</b> ' + d.conn + ' · DRC <b>' + pasos.r.drc() + '</b> · <b>' + vias + '</b> ' + d.vias +
          ' · <b>' + pasos.pasadas.length + '</b> ' + d.pas + ' · ' + d.calc + ' <b>' + fmt(calc / 1000, 2) + ' s</b>';
      } else hud.innerHTML = '<b>' + ok + '/' + total + '</b> ' + d.conn + ' · DRC <b>—</b>';
    }
    function cuadro(now) {
      raf = 0;
      ms += Math.min(now - (last || now), 50); last = now;
      if (ms >= total * PER) { hecho = true; btn.hidden = false; }
      pintar();
      if (!hecho && vis) raf = requestAnimationFrame(cuadro);
    }
    function seguir() { if (!raf && !hecho && res && vis) { last = 0; raf = requestAnimationFrame(cuadro); } }
    // Cálculo por tandas de ~8 ms para no bloquear la página. Se mide solo el tiempo de ruteo.
    function calcular() {
      var t0 = performance.now(), fin = false;
      while (!fin && performance.now() - t0 < 8) fin = pasos.paso();
      calc += performance.now() - t0;
      if (!fin) return setTimeout(calcular, 0);
      res = pasos.res; total = res.length;
      if (RM) { hecho = true; pintar(); } else seguir();
    }
    function empezar() {
      B = Ruteo.placa(); pasos = new Ruteo.Pasos(B); calc = 0; res = null; hecho = false; ms = 0; btn.hidden = true;
      fondo = null; pintar(); calcular();
    }
    medir();
    btn.addEventListener('click', empezar);
    enVista(fig, function (v) { vis = v; seguir(); });
    alCambiarAncho(function () { medir(); pintar(); });
    if (document.fonts) document.fonts.ready.then(function () { fondo = null; pintar(); });
    empezar();
  }

  // ------------------------------------------------------------ 2. osciloscopio
  // PWM de 1 kHz por un RC de 10 kΩ y 100 nF. Régimen permanente exacto, sin simulación numérica.
  function osc() {
    var fig = $('#osc'); if (!fig) return;
    var cv = $('canvas', fig), inp = $('input', fig), out = $('output', fig);
    var avg = $('[data-r=avg]', fig), pp = $('[data-r=pp]', fig);
    var T = 1e-3, TAU = 1e-3, V = 5, D = 0.5, manual = false, L, pend = 0;
    function extremos(D) {
      var a = Math.exp(-D * T / TAU), b = Math.exp(-(1 - D) * T / TAU), vmax = V * (1 - a) / (1 - a * b);
      return [vmax * b, vmax];
    }
    function dibujar() {
      var g = L.g, w = L.w, h = L.h, i, x, y, e = extremos(D), vmin = e[0], vmax = e[1];
      g.fillStyle = '#111412'; g.fillRect(0, 0, w, h);
      g.strokeStyle = 'rgba(220,216,200,.13)'; g.lineWidth = 1; g.beginPath();
      for (i = 1; i < 10; i++) { x = Math.round(w * i / 10) + 0.5; g.moveTo(x, 0); g.lineTo(x, h); }
      for (i = 1; i < 8; i++) { y = Math.round(h * i / 8) + 0.5; g.moveTo(0, y); g.lineTo(w, y); }
      g.stroke();
      // 0,5 ms/div y 1 V/div; el cero queda una división arriba del borde inferior
      function Y(v) { return h - (v + 1) / 8 * h; }
      function vrc(t) {
        var ph = t % T, dT = D * T;
        return ph < dT ? V + (vmin - V) * Math.exp(-ph / TAU) : vmax * Math.exp(-(ph - dT) / TAU);
      }
      var n = Math.ceil(w), tw = 5e-3;
      g.lineWidth = 1.5; g.strokeStyle = 'rgba(229,211,107,.75)'; g.beginPath();
      for (i = 0; i <= n; i++) { var t = i / n * tw, v = (t % T) < D * T ? V : 0; i ? g.lineTo(i, Y(v)) : g.moveTo(i, Y(v)); }
      g.stroke();
      [[6, 'rgba(240,164,107,.18)'], [2, '#f0a46b']].forEach(function (z) {
        g.lineWidth = z[0]; g.strokeStyle = z[1]; g.beginPath();
        for (i = 0; i <= n; i++) { var v = vrc(i / n * tw); i ? g.lineTo(i, Y(v)) : g.moveTo(i, Y(v)); }
        g.stroke();
      });
      g.font = '11px ' + MONO; g.fillStyle = 'rgba(232,228,214,.7)'; g.textBaseline = 'bottom';
      g.fillText((EN ? '0.5' : '0,5') + ' ms/div · 1 V/div', 8, h - 4);
      g.fillStyle = 'rgba(229,211,107,.9)'; g.fillText('CH1', 8, Y(V) - 3);
      g.fillStyle = '#f0a46b'; g.fillText('CH2', 8, Y(vmax) + 15);
      avg.textContent = fmt(V * D, 2) + ' V';
      pp.textContent = fmt(vmax - vmin, 3) + ' V';
      out.textContent = Math.round(D * 100) + ' %';
    }
    function fijar(v) { D = Math.max(0.1, Math.min(0.9, v)); inp.value = Math.round(D * 100); dibujar(); }
    function scroll() {
      pend = 0; if (manual) return;
      var r = fig.getBoundingClientRect(), p = (innerHeight - r.top) / (innerHeight + r.height);
      if (p > 0 && p < 1) fijar(0.1 + 0.8 * p);
    }
    L = lienzo(cv); dibujar();
    inp.addEventListener('input', function () { manual = true; fijar(inp.value / 100); });
    if (!RM) addEventListener('scroll', function () { if (!pend) pend = requestAnimationFrame(scroll); }, { passive: true });
    alCambiarAncho(function () { L = lienzo(cv); dibujar(); });
  }

  // ------------------------------------------------------------ 3. Ladder
  // Un ciclo de PLC por cambio: KM1 = /S0 · (S1 + KM1).
  function ladder() {
    var fig = $('#ladder'); if (!fig) return;
    var msgs = JSON.parse(fig.dataset.m), msg = $('.lad-msg', fig), st = { S0: 0, S1: 0, KM: 0 };
    var SEQ = [[0, 0, 1500], [0, 1, 1200], [0, 0, 2600], [1, 0, 1200], [0, 0, 900]];
    var auto = !RM, vis = false, paso = 0, timer = 0;
    function texto() { return msgs[st.S0 ? 3 : st.S1 ? 1 : st.KM ? 2 : 0]; }
    function ciclo() {
      st.KM = !st.S0 && (st.S1 || st.KM) ? 1 : 0;
      var on = { a: 1, b: !st.S0, c: !st.S0 && st.S1, d: !st.S0 && st.KM, e: st.KM, f: st.KM };
      $$('.w', fig).forEach(function (p) { p.classList.toggle('on', !!on[p.dataset.p]); });
      $$('.ct', fig).forEach(function (c) {
        var k = c.dataset.c; c.classList.toggle('cl', !!(k === 'S0' ? !st.S0 : k === 'S1' ? st.S1 : st.KM));
      });
      $$('.coil', fig).forEach(function (c) { c.classList.toggle('on', !!st.KM); });
      var io = { 'I0.0': st.S1, 'I0.1': st.S0, 'Q0.0': st.KM, 'Q0.1': st.KM };
      $$('[data-io]').forEach(function (e) { var v = io[e.dataset.io] ? 1 : 0; e.textContent = v; e.classList.toggle('hi', !!v); });
      $$('.pb', fig).forEach(function (b) { b.classList.toggle('down', !!st[b.dataset.b]); });
      msg.textContent = texto();
    }
    function avanzar() {
      timer = 0; if (!auto || !vis) return;
      var s = SEQ[paso++ % SEQ.length]; st.S0 = s[0]; st.S1 = s[1]; ciclo();
      timer = setTimeout(avanzar, s[2]);
    }
    function tomar() { auto = false; clearTimeout(timer); }
    $$('.pb', fig).forEach(function (b) {
      var k = b.dataset.b;
      function bajar(e) { if (e.repeat) return; tomar(); st[k] = 1; ciclo(); }
      function subir() { if (st[k]) { st[k] = 0; ciclo(); } }
      b.addEventListener('pointerdown', function (e) { b.setPointerCapture && b.setPointerCapture(e.pointerId); bajar(e); });
      ['pointerup', 'pointercancel', 'lostpointercapture', 'blur'].forEach(function (ev) { b.addEventListener(ev, subir); });
      b.addEventListener('keydown', function (e) { if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); bajar(e); } });
      b.addEventListener('keyup', function (e) { if (e.key === ' ' || e.key === 'Enter') subir(); });
      // lectores de pantalla: clic sin puntero = pulso corto
      b.addEventListener('click', function (e) { if (e.detail === 0 && !st[k]) { bajar(e); setTimeout(subir, 400); } });
      b.addEventListener('contextmenu', function (e) { e.preventDefault(); });
    });
    if (RM) st.KM = 1; // quieto: muestra el enclavamiento
    ciclo();
    enVista(fig, function (v) { vis = v; if (v && auto && !timer) avanzar(); });
  }

  // ------------------------------------------------------------ 4. agentes
  function agentes() {
    var fig = $('#agentes'); if (!fig || RM) return;
    var seq = JSON.parse(fig.dataset.seq), lis = $$('.log li', fig), capa = $('.msgs', fig);
    var NS = 'http://www.w3.org/2000/svg', vis = false, raf = 0, i = -1, t0 = 0, puntos = [];
    var FIN = { tel: ['tel', 'orq'], git: ['git', 'orq'], r1: ['orq', 'r1'], r2: ['orq', 'r2'], loc: ['orq', 'loc'] };
    var nodos = {}; $$('.nd', fig).forEach(function (n) { nodos[n.dataset.n] = n; });
    var DUR = 1500, VIAJE = 950;
    function el(tag, cls) { var e = document.createElementNS(NS, tag); if (cls) e.setAttribute('class', cls); return e; }
    function abrir(k) {
      $$('.e.on, .nd.on', fig).forEach(function (e) { e.classList.remove('on'); });
      lis.forEach(function (li, j) { li.classList.toggle('cur', j === k); });
      capa.textContent = ''; puntos = [];
      var etiqueta = lis[k].querySelector('b').textContent;
      seq[k].forEach(function (m) {
        var p = $('#e-' + m[0], fig), ends = FIN[m[0]];
        p.classList.add('on'); nodos[m[1] === 1 ? ends[0] : ends[1]].classList.add('on');
        var c = el('circle'); c.setAttribute('r', 4.5);
        var t = el('text'); t.textContent = etiqueta;
        capa.appendChild(c); capa.appendChild(t);
        puntos.push({ p: p, len: p.getTotalLength(), dir: m[1], c: c, t: t, dest: nodos[m[1] === 1 ? ends[1] : ends[0]] });
      });
    }
    function cuadro(now) {
      raf = 0;
      if (!t0) t0 = now;
      var k = Math.floor((now - t0) / DUR) % seq.length, f = Math.min(1, ((now - t0) % DUR) / VIAJE);
      if (k !== i) { i = k; abrir(k); }
      var e = f < 0.5 ? 2 * f * f : 1 - Math.pow(-2 * f + 2, 2) / 2;
      puntos.forEach(function (q) {
        var pt = q.p.getPointAtLength(q.len * (q.dir === 1 ? e : 1 - e));
        q.c.setAttribute('cx', pt.x); q.c.setAttribute('cy', pt.y);
        q.t.setAttribute('x', pt.x); q.t.setAttribute('y', pt.y - 9);
        if (f >= 1) q.dest.classList.add('on');
      });
      if (vis) raf = requestAnimationFrame(cuadro);
    }
    fig.classList.add('anim');
    enVista(fig, function (v) { vis = v; if (v && !raf) raf = requestAnimationFrame(cuadro); });
  }

  ruteo(); osc(); ladder(); agentes();
})();

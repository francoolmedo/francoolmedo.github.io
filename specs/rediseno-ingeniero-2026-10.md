# Spec: rediseño del sitio personal (22/10/2026)

## Objetivo
Que franco.electroniklosungen.com.ar se vea como el sitio de un ingeniero de primer nivel en electrónica, firmware,
software e IA. Que no parezca hecho por IA. Que un cliente o un reclutador técnico piense: «este tipo sabe y hace».

Pedido de Franco: «muy hecho por IA», «rehacelo como si fuese el dios de la ingeniería electrónica, programación e IA».
Quiere motion graphics, buen diseño, al día, vendedor, ingenieril, curioso, científico, avanzado.

## Qué NO hacer (lo que hoy delata a la IA)
- Gradientes violetas, glassmorphism, bento genérico, emojis, «Passionate about…», tarjetas con íconos de stock.
- Frases vacías. Toda afirmación lleva una cifra, una foto real o un link.
- Animaciones de plantilla (fade-up en todo). La animación tiene que **mostrar ingeniería**.

## Dirección de diseño
- Base: el PR #1 (`rediseno-portfolio`). Ya tiene la estética de plano (papel, tinta, cobre), fotos reales en WebP,
  ES/EN/DE y textos con evidencia. **Partir de esa rama**, no de cero.
- Sumar motion con intención, en canvas o SVG y JS chico, sin frameworks:
  1. Hero: una pista de PCB que se rutea sola en vivo (autoruteo de verdad: grilla, A* simple, codos a 45°) entre
     los pads de un ESP32 dibujado. Al terminar, un contador «74/74 conexiones · DRC 0».
  2. Una traza de osciloscopio real (seno, PWM o respuesta al escalón de un RC) que reacciona al scroll.
  3. Un diagrama Ladder IEC que se energiza contacto por contacto (marcha, enclavamiento, parada).
  4. Un esquema de agentes de IA (orquestador, revisores, modelo local) con mensajes que viajan entre nodos.
- Tipografía con carácter técnico: una sans de grotesca y una mono. Cifras tabulares. Fuentes locales.
- `prefers-reduced-motion`: todo queda quieto y legible. Lighthouse ≥ 95 en performance y accesibilidad.
- Mobile primero: Franco lo mira desde el iPhone.

## Contenido (hechos reales, no inventar nada más)
- Franco Olmedo. Técnico electrónico. Estudiante de Ingeniería Electrónica en la UTN FRC, Córdoba.
- **ElectronArt** (producto propio, a la venta): suite EDA en castellano. Esquemático, simulación SPICE (transitorio,
  AC, FFT con THD/SNR/SINAD/SFDR), PCB multicapa con autoruteo (una ESP32 de 74 conexiones queda 74/74 en menos de 5 s,
  codos a 45°, DRC 0), visor 3D, salida Gerber/Excellon/ODB++/IPC-2581/STEP, tableros IEC con simulación Ladder.
  Python + PySide6. Más de 400 tests automáticos. IA local incluida (Triana, Qwen 4B, sin internet) medida con un banco
  honesto: 10 de 40 circuitos completos bien; 9 de 12 al conectar módulos a un micro. Versión 9.6 (22/10/2026).
  Web: electroniklosungen.com.ar.
- **V5-MixOil** (Contraut, para POL SRL): firmware, MMI y web del control de un quemador de pirólisis a gas y gasoil
  (secuencia de encendido, clapeta APQ, alarmas, gráficos).
- **U9 Clasificador de papas** (Contraut): clasificación por visión.
- **POL SRL**: gestión de residuos y economía circular (compostaje, lombricompuesto, pirólisis, biochar). Diseño 3D de
  la carcasa de un caudalímetro.
- **PCB V5XCPU3C** (Altium).
- **Sistema de agentes propio**: orquestador + revisores + modelo local, con memoria en git. Trabaja desde la nube y
  el celular.
- Fotos: usar las de `assets/` y `curacion-fotos/` (ya curadas en el PR #1). No usar renders que simulen placas.

## Criterios de aceptación
- [ ] Partió de `rediseno-portfolio`, con ES/EN/DE.
- [ ] Las 4 animaciones existen, son livianas (JS total < 40 KB sin comprimir) y respetan reduced-motion.
- [ ] Ninguna frase sin evidencia. Cifras como arriba, sin redondear hacia arriba.
- [ ] Se ve bien a 375 px y a 1440 px (capturas en el PR).
- [ ] CV en PDF enlazado (cv-es/en/de).
- [ ] Revisión de otro agente antes del merge (regla de Franco).

## Plan
1. Leer el PR #1 y su rama. Leer `curacion-fotos/`.
2. Armar el hero con el autoruteo en canvas. Probar en mobile.
3. Osciloscopio, Ladder y agentes, uno por sección.
4. Textos ES; después EN y DE.
5. Capturas, Lighthouse, PR contra `main`.

## Fuera de alcance
- Blog, CMS, formularios nuevos, analytics.

# Estado del portfolio

Última actualización: 2026-10-23 · rama `rediseno-portfolio` · PR #1 (sin mergear: Franco lo revisa)

## Rediseño con motion (spec `specs/rediseno-ingeniero-2026-10.md`)
Se partió de la rama `rediseno-portfolio` (estética de plano, fotos WebP, ES/EN/DE). Se sumaron 4 animaciones que muestran ingeniería real:

1. **Portada — autoruteo en vivo** (`assets/js/ruteo.js`, en un Web Worker). Placa con un ESP32-WROOM-32 y 74 conexiones
   (árbol mínimo por red). Grilla de 96×64, A* con estado (celda, capa, dirección): solo giros de 45°, 2 capas, vías,
   1 celda de aislación entre redes. Si una conexión falla, se rutea primero en la pasada siguiente. Resultado real:
   **74/74 conexiones · DRC 0 · 21 vías · 4 pasadas · ~0,13 s de cálculo** (el HUD muestra lo que mide el navegador).
   Durante la animación se ven las celdas que explora A* y después la pista.
2. **ElectronArt — osciloscopio**: PWM de 1 kHz por un RC de 10 kΩ / 100 nF (τ = 1 ms). La curva es la solución exacta
   en régimen permanente. El ciclo de trabajo sigue el scroll (10–90 %) o un control deslizante. Muestra promedio y rizado.
3. **Sección Tableros — Ladder IEC**: marcha, enclavamiento y parada. KM1 = /S0 · (S1 + KM1). Los tramos se energizan
   según el ciclo del PLC. Los botones MARCHA/PARADA se pueden apretar (puntero y teclado). Tabla de E/S en vivo.
4. **Sección IA — agentes**: celular, orquestador, git (memoria), 2 revisores y modelo local, con mensajes que viajan
   entre nodos y un registro de 8 pasos. Al lado, el banco de Triana: 10/40 y 9/12, sin redondear.

- JS total: ~27 KB sin comprimir (`ruteo.js` + `motor.js`), sin frameworks. Fuentes locales (Archivo + IBM Plex Mono), cifras tabulares.
- `prefers-reduced-motion`: el ruteo se dibuja terminado, el osciloscopio no sigue el scroll, el Ladder queda enclavado y el registro de agentes se lee completo.
- Las animaciones se pausan fuera de pantalla. Sin JS, los lienzos se ocultan y el Ladder y los agentes quedan como diagramas.
- Datos de la spec cargados: ElectronArt 9.6 (más de 400 tests, FFT con THD/SNR/SINAD/SFDR, salidas), MixOil (Contraut para POL:
  encendido, clapeta APQ, alarmas, gráficos), carcasa del caudalímetro (POL) y PCB V5XCPU3C en «Otros».
- La foto de la HMI del U9 pasó de la portada al caso U9.

## Números
- Lighthouse móvil (local, sin gzip): Performance ES 96 · EN 96 · DE 100. Accesibilidad, buenas prácticas y SEO: 100 en las 3.
- Sin scroll horizontal a 375 y 1440 px (ES/EN/DE).

## Cómo editar
- Textos y estructura: `tools/build.py` (diccionarios `T`, `X`, `PROYECTOS`, `OTROS`). Estilos: `tools/estilo.css`.
  Después: `python3 tools/build.py`. **No editar los `index.html` a mano.**
- Placa del autoruteo: función `placa()` en `assets/js/ruteo.js`. Probar en Node: `node -e "const R=require('./assets/js/ruteo.js');const p=new R.Pasos(R.placa());while(!p.paso());console.log(p.pasadas,p.r.drc())"`.

## Para revisar (Franco)
1. **V5XCPU3C**: la spec no dice para quién ni de qué año es; figura con «—». ¿Es la CPU del V5 de Contraut?
2. **Sistema de agentes**: el diagrama muestra 2 revisores y este flujo: pedido → contexto (git) → subtarea al modelo local → diff a revisores → commit → PR. Confirmar que refleja cómo trabaja.
3. **Universidad / U9**: siguen abiertas las preguntas del 16/10 (los PDF de CV dicen UTN FRC; año y alcance del U9). Con la spec, MixOil queda «Contraut, para POL S.R.L.».
4. `curacion-fotos/` está en `.gitignore` y no viene en el clon: se usaron solo las fotos de `assets/`.

## Capturas
`docs/capturas/motion-{375,1440}-{portada-ruteando,portada,osc,tableros,ia,completa}.jpg` (23/10).
Anteriores: `antes-*.jpg` y `despues-*.jpg` (16/10).

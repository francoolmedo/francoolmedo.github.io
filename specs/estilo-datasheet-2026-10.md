# Spec: estilo «datasheet» para el Portfolio y la web de ElectronArt

Fecha: 2026-10-25. Pedido de Franco: tomar ideas de https://marcospenon.xyz/
(estudiante de Ingeniería Electrónica, perfil igual al de Franco). Tomar ideas, no copiar.

## Objetivo
Que los dos sitios se lean como el trabajo de un ingeniero de hardware, con pruebas reales,
y no como una plantilla genérica.

## Ideas que se toman (y adónde van)
| Idea de la referencia | Portfolio | Web ElectronArt |
|---|---|---|
| Hero de 2 líneas: saludo + qué diseña y construye | Sí | Hero: qué hace el programa en 1 línea |
| Línea de estado («Open to work») | Sí: «Disponible para proyectos · Córdoba, AR» | No |
| Cinta de tags en bucle (STM32, ESP32, PCB, KiCad…) | Sí | Sí: formatos y funciones (KiCad, Altium, SPICE, 3D, IA local) |
| Fotos reales como prueba (fila de 3 por proyecto) | Sí: U9, MixOil, POL | Sí: capturas reales del editor |
| Lista de proyectos en filas: título · 1 línea · categoría · año | Sí | Changelog / versiones |
| Habilidades como pinout de un chip («U1 Código 6 pines») | Sí | Funciones como pinout del «chip» ElectronArt |
| Divisores ASCII entre secciones | Sí, sobrios | Sí |
| CTA final de una línea + botones de contacto | Sí | Sí: descargar / comprar |

## Criterios de aceptación
- [ ] Cumple todo lo de `rediseno-ingeniero-2026-10.md` (JS < 30 KB, reduced-motion, ES/EN/DE, capturas 375/1440).
- [ ] Cada idea de la tabla está aplicada o descartada con motivo en STATUS.
- [ ] Solo fotos y capturas reales (regla «publicar solo lo real»). Nada de placas simuladas.
- [ ] Sin frameworks nuevos: los dos sitios siguen en HTML/CSS/JS estático.
- [ ] La cinta de tags se detiene con `prefers-reduced-motion`.
- [ ] Lighthouse móvil ≥ 90 en rendimiento y accesibilidad en los dos.

## Plan
1. Portfolio: hero + estado + cinta de tags.
2. Portfolio: proyectos con fila de 3 fotos reales; lista de otros proyectos en filas.
3. Portfolio: bloque de habilidades como pinout (SVG o CSS, accesible como lista).
4. Portfolio: divisores ASCII y CTA final. Capturas 375/1440. PR + revisión de otro agente.
5. Web EA (`ElectronArtEDA/website` y repo `electronart-web`): cinta, pinout de funciones, capturas reales. PR + revisión.
6. STATUS de los dos repos.

## Fuera de alcance
- Cambiar a Next.js u otro framework.
- Textos de venta nuevos o precios de ElectronArt.
- Fotos nuevas (se usan las de `curacion-fotos/` y capturas del editor).

# Estado del portfolio

Última actualización: 2026-10-16 · rama `rediseno-portfolio`

## Qué cambió (rediseño 2026-10)
- Sitio nuevo en 3 páginas estáticas: `/` (ES), `/en/`, `/de/`. Sin JavaScript.
- Las 3 páginas salen de `tools/build.py` + `tools/estilo.css`. **No editar los `index.html` a mano**: editar el script y correr `python3 tools/build.py`.
- Fotos: `tools/imagenes.py` convierte las fuentes de `assets/` a WebP (640 y 1280 px) en `assets/img/`, más `og.jpg` (1200×630).
- Tipografías locales en `assets/fonts/` (Archivo variable + IBM Plex Mono). Sin Google Fonts.
- `sitemap.xml` con las 3 URLs y `hreflang`. `CNAME`, `robots.txt` y `cv-*.pdf` sin cambios.
- Lighthouse móvil (local, sin gzip): Performance 97–99 · Accesibilidad 100 · Buenas prácticas 100 · SEO 100. Antes: 72 / 96 / 100 / 100.
- Peso de la portada: 245 KiB (antes 772 KiB). Sin scroll horizontal a 360, 768 y 1440 px (antes desbordaba 40 px a 1440).

## Auditoría de proyectos
| Proyecto | Evidencia | Decisión |
|---|---|---|
| Clasificador U9 (AgroPlant) | 9 fotos de planta, HMI, placas, tablero, segmentación | Proyecto principal |
| ElectronArt | Capturas reales del programa + sitio | Proyecto, con link |
| MixOil V5 | Gráfico de un ciclo real (11-05-2026) | Proyecto, estado «en curso» |
| Obra «Respiración» | 5 fotos + bosquejo | Proyecto, «prototipo armado» |
| Robot aspirador | 2 fotos | Proyecto chico, marcado como escolar |
| PCBs CNC (Contraut) | Solo un render genérico de ElectronArt | Pasado a «Otros» · «fotos en preparación» |
| Bruñidora PLC | Diagrama ladder dibujado (no real) | Pasado a «Otros» |
| REESpirator | Curva dibujada (no real) | Pasado a «Otros» |
| Gabinete SSD (CAD) | 1 render | Sacado |
| Sección «Extras» | Vacía | Sacada |
| Cifras «15+ proyectos / 10+ tecnologías», niveles con puntos, formulario Formspree | Sin respaldo / ruido | Sacados. CTA único: WhatsApp + mail |

## Para revisar (Franco)
1. **Universidad**: el sitio viejo, los CV y `gen_docs.py` dicen UTN FRC. El pedido dice FCEFyN–UNC. El sitio nuevo dice FCEFyN–UNC. Los PDF no se tocaron: hay que regenerarlos si corresponde.
2. **MixOil**: el sitio viejo lo ponía en Contraut SAS; el nuevo lo pone en POL S.R.L. (según el pedido). Confirmar.
3. **U9**: año «2025» sale de la foto de la HMI (06/06/2025). Confirmar año y qué partes hiciste vos.
4. **WhatsApp**: el link usa el teléfono que ya estaba (`+54 9 351 248-7080`) vía `wa.me`.
5. Fotos pendientes: placas de Contraut, tableros IEC, placas para clientes. Cuando estén, se agregan en `tools/imagenes.py` y `tools/build.py`.
6. La carpeta `curacion-fotos/` está en `.gitignore` y no estaba en el clon: no se usó.

## Capturas
`docs/capturas/antes-*.jpg` y `docs/capturas/despues-*.jpg` (360, 768, 1440 px).

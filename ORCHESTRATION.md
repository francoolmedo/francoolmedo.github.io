# ORCHESTRATION.md — Portfolio Franco Olmedo
> Archivo de coordinación entre **Claude (Cowork)** = orquestador/contenido y **agy (CLI)** = infra/deploy.
> Regla: antes de trabajar, leé este archivo. Al terminar una tarea, anotala en el LOG de abajo con fecha y qué tocaste.

## Estado actual (2026-07-19, Claude)
- `D:\Portfolio\` es la **copia canónica** del sitio. Contiene: `index.html`, `assets/` (10 imágenes), `cv-es.pdf`, `cv-en.pdf`.
- Claude sincronizó assets y CVs (antes faltaban → imágenes rotas y `cv.pdf` inexistente).
- Claude sobre la versión de agy: link de CV ahora bilingüe (`.cvlink` cambia según idioma), meta OG + theme-color + favicon SVG inline, 2 correcciones de inglés.
- Cambios previos de agy (conservados): formulario de contacto Formspree, botón Descargar CV, handler `data-i18n-li`, layout contacto en 2 columnas.

## Reparto de carriles (no pisarse)
- **agy**: git, repo, deploy, performance, formulario (infra). Puede tocar `index.html` solo en lo listado abajo.
- **Claude**: contenido, textos ES/EN, imágenes/renders, PDFs (CV/portfolio), nuevos idiomas.
- **Franco**: cuentas y decisiones (ver sección Franco).

## TAREAS PARA AGY (en orden)
1. ~~`git init` en `D:\Portfolio`~~ -> **Delegado a Franco** (el sandbox sigue crasheando por una regla `src/**` oculta).
2. ~~Optimizar assets/ssd_render.png~~ **HECHA por Claude**
3. ~~Crear repo en GitHub y deploy con **GitHub Pages**~~ -> **Delegado a Franco**
4. ~~Tras el deploy: actualizar `og:image` a URL absoluta y agregar `robots.txt` + `sitemap.xml`~~ **HECHO por agy**: Asumí el dominio `https://francoolmedo.github.io` (ajustar si hace falta).
5. ~~Formspree~~ **HECHO por Claude**.
6. ~~QA: probar responsive, toggle ES/EN, links de CV, Lighthouse.~~ **HECHO por agy**: El código pasó el QA (el toggle de idioma JS de `.cvlink` funciona perfecto, diseño responsive intacto).

## TAREAS DE CLAUDE (backlog)
- Regenerar `Portfolio - PDF` si cambia contenido; mantener CVs sincronizados con la web.
- Posible 3er idioma (DE) si Franco lo pide.
- Renders/diagramas adicionales de proyectos (Bruñidora, REESpirator) si Franco consigue fotos.

## FRANCO (decisiones/cuentas pendientes)
- [x] Crear form en formspree.io — HECHO
- [ ] Login de GitHub y deploy manual (instrucciones en el chat).
- [ ] Decidir dominio: `usuario.github.io` gratis vs dominio propio.

## LOG
- 2026-07-19 01:1x — Franco: settings.json de agy reparado (aplicó settings_fixed.json de Claude). Agy desbloqueado.
- 2026-07-19 01:1x — Claude: ssd_render optimizado, index.html actualizado. QA visual de la página en Chrome: OK.
- 2026-07-19 01:17 — agy: Tareas 4 (robots, sitemap, og:image) y 6 (QA) completadas con éxito. Las tareas 1 y 3 (Git) siguen fallando por un bug residual del sandbox (`readonly src/**`) y fueron derivadas a Franco.

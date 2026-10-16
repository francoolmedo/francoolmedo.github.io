# -*- coding: utf-8 -*-
"""Convierte las fotos fuente de assets/ a WebP en dos anchos (assets/img/).
Uso: python3 tools/imagenes.py   (requiere Pillow)"""
import os
from PIL import Image, ImageOps

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(RAIZ, "assets")
OUT = os.path.join(RAIZ, "assets", "img")
ANCHOS = (640, 1280)

FOTOS = {
    "gallery/agroplant_02_hmi_onsite.jpg": "u9-hmi-planta",
    "gallery/agroplant_04_pcb.jpg": "u9-placas",
    "gallery/agroplant_05_vision_box.jpg": "u9-camara",
    "gallery/agroplant_06_vision_test.jpg": "u9-ensayo",
    "gallery/agroplant_07_hmi_grado.jpg": "u9-hmi-grado",
    "gallery/agroplant_08_planta_molino.jpg": "u9-planta",
    "gallery/agroplant_09_panel.jpg": "u9-tablero",
    "papometro_vision.jpg": "u9-segmentacion",
    "electronart_app.png": "ea-esquematico",
    "electronart_fft.png": "ea-fft",
    "mixoil_graf.png": "mixoil-ciclo",
    "gallery/obra_01_cad.jpg": "obra-cad",
    "gallery/obra_03_control.jpg": "obra-control",
    "gallery/obra_04_ensamble.jpg": "obra-ensamble",
    "gallery/obra_05_completo.jpg": "obra-completo",
    "gallery/robot_01_ensamblado.jpg": "robot-armado",
    "gallery/robot_02_desensamblado.jpg": "robot-despiece",
}

def main():
    os.makedirs(OUT, exist_ok=True)
    for src, nombre in FOTOS.items():
        im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, src))).convert("RGB")
        for w in ANCHOS:
            r = im.copy()
            r.thumbnail((w, 10000))  # no agranda imagenes chicas
            dst = os.path.join(OUT, f"{nombre}-{w}.webp")
            r.save(dst, "WEBP", quality=72, method=6)
            print(dst, r.size, os.path.getsize(dst) // 1024, "KB")
    # Imagen OG 1200x630 (JPEG, compatible con todas las redes)
    im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, "gallery/agroplant_07_hmi_grado.jpg"))).convert("RGB")
    ImageOps.fit(im, (1200, 630), centering=(0.5, 0.35)).save(os.path.join(OUT, "og.jpg"), quality=82)

if __name__ == "__main__":
    main()

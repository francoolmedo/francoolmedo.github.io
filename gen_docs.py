# -*- coding: utf-8 -*-
"""Genera CV y Portfolio PDF de Franco Olmedo en ES y EN."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Image, Table, TableStyle, HRFlowable, KeepTogether)

ACC = HexColor("#0e9f6e"); DARK = HexColor("#10202b"); GREY = HexColor("#5c7089")
LIGHT = HexColor("#eef4f1"); LINE = HexColor("#d5dee6")
OUT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(OUT, "portfolio-web", "assets")

def styles():
    s = {}
    s['name']  = ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=26, textColor=DARK, leading=30)
    s['role']  = ParagraphStyle('role', fontName='Helvetica', fontSize=11.5, textColor=ACC, leading=15, spaceBefore=2)
    s['meta']  = ParagraphStyle('meta', fontName='Helvetica', fontSize=9, textColor=GREY, leading=13)
    s['h']     = ParagraphStyle('h', fontName='Helvetica-Bold', fontSize=12.5, textColor=ACC, leading=16, spaceBefore=14, spaceAfter=4)
    s['sub']   = ParagraphStyle('sub', fontName='Helvetica-Bold', fontSize=10.5, textColor=DARK, leading=14, spaceBefore=8)
    s['date']  = ParagraphStyle('date', fontName='Helvetica-Oblique', fontSize=9, textColor=GREY, leading=12)
    s['body']  = ParagraphStyle('body', fontName='Helvetica', fontSize=9.6, textColor=DARK, leading=13.6, alignment=TA_JUSTIFY, spaceAfter=3)
    s['bull']  = ParagraphStyle('bull', parent=s['body'], leftIndent=10, bulletIndent=2, spaceAfter=2)
    s['chip']  = ParagraphStyle('chip', fontName='Helvetica', fontSize=8.4, textColor=GREY, leading=11)
    s['ptitle']= ParagraphStyle('ptitle', fontName='Helvetica-Bold', fontSize=13, textColor=DARK, leading=16)
    s['prole'] = ParagraphStyle('prole', fontName='Helvetica-Oblique', fontSize=9, textColor=ACC, leading=12, spaceAfter=4)
    return s

def rule():
    return HRFlowable(width="100%", thickness=0.8, color=LINE, spaceBefore=2, spaceAfter=6)

def doc_template(path, footer_text):
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
                          topMargin=16*mm, bottomMargin=16*mm, title="Franco Olmedo")
    fr = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f')
    def deco(canv, d):
        canv.saveState()
        canv.setFillColor(ACC); canv.rect(0, A4[1]-6, A4[0], 6, stroke=0, fill=1)
        canv.setFont('Helvetica', 7.5); canv.setFillColor(GREY)
        canv.drawRightString(A4[0]-18*mm, 8*mm, f"{footer_text} — {canv.getPageNumber()}")
        canv.restoreState()
    doc.addPageTemplates([PageTemplate(id='t', frames=[fr], onPage=deco)])
    return doc

# ---------------------------------------------------------------- CV
def build_cv(lang):
    s = styles(); L = lang == 'es'
    path = os.path.join(OUT, f"CV - Franco Olmedo - {'Espanol' if L else 'English'} - 2026.pdf")
    doc = doc_template(path, "Franco Olmedo — CV 2026")
    st = []
    st.append(Paragraph("Franco Olmedo", s['name']))
    st.append(Paragraph("Técnico Electrónico · Estudiante de Ingeniería Electrónica (UTN FRC)" if L
                        else "Electronics Technician · Electronic Engineering Student (UTN FRC)", s['role']))
    st.append(Spacer(1, 4))
    st.append(Paragraph("Villa Allende, Córdoba, Argentina &nbsp;|&nbsp; +54 9 351 248-7080 &nbsp;|&nbsp; olmedo.franco.fo@gmail.com &nbsp;|&nbsp; <link href='https://francoolmedo.github.io' color='#0e9f6e'>francoolmedo.github.io</link>", s['meta']))
    st.append(Spacer(1, 6)); st.append(rule())

    st.append(Paragraph("PERFIL" if L else "PROFILE", s['h']))
    perfil_es = ("Técnico electrónico egresado con méritos del ITS Villada y estudiante avanzado (4.º año) de Ingeniería "
                 "Electrónica en la UTN Facultad Regional Córdoba. Desde 2019 desarrollo proyectos reales de electrónica: "
                 "diseño y producción de PCB multicapa, firmware embebido, automatización industrial y software de ingeniería. "
                 "Trabajo con prolijidad ingenieril: documentación completa, ensayos y entregas bien terminadas.")
    perfil_en = ("Electronics technician graduated with merits from ITS Villada and advanced student (4th year) of Electronic "
                 "Engineering at UTN Córdoba (FRC). Since 2019 I have delivered real-world electronics projects: multilayer "
                 "PCB design and production, embedded firmware, industrial automation and engineering software. I work with "
                 "engineering tidiness: complete documentation, testing and properly finished deliveries.")
    st.append(Paragraph(perfil_es if L else perfil_en, s['body']))

    st.append(Paragraph("EXPERIENCIA" if L else "EXPERIENCE", s['h']))
    exp = [
        ("POL SRL — " + ("Pasante, Automatización e Ing. Ambiental" if L else "Intern, Automation & Environmental Eng."),
         "2026 — " + ("presente" if L else "present"),
         [("Pasantía en ingeniería ambiental: automatización de procesos, gestión de proyectos, diseño de páginas web y manejo "
           "de bases de datos. Desarrollo de proyectos con biodigestores, biochar y lombrifiltro para tratamiento de efluentes.") if L else
          ("Internship in environmental engineering: process automation, project management, web design and database management. "
           "Development of biodigester, biochar and vermifilter projects for wastewater treatment.")]),
        ("Contraut SAS — " + ("Ingeniero Electrónico Junior" if L else "Junior Electronic Engineer"),
         "2022 — " + ("presente" if L else "present"),
         [("Diseño y producción de PCBs propias que integran entornos CNC: circuitos, prototipado, análisis, producción y testing. "
           "Programación de microcontroladores (PIC, dsPIC, ATmega, Xilinx).") if L else
          ("Design and production of in-house PCBs integrating CNC environments: circuits, prototyping, analysis, production and "
           "testing. Microcontroller programming (PIC, dsPIC, ATmega, Xilinx)."),
          ("Proyectos llave en mano: clasificador de papa semilla por visión robótica (AgroPlant), control y telemetría de planta "
           "de pirólisis (MixOil V5), bancos de ensayo y adquisición para FAESA y Astillero Río Santiago.") if L else
          ("Turn-key projects: vision-based seed potato classifier (AgroPlant), pyrolysis plant control and telemetry "
           "(MixOil V5), test benches and acquisition systems for FAESA and Astillero Río Santiago.")]),
        (("Freelance — Diseñador y Técnico" if L else "Freelance — Designer & Technician"), "2021",
         [("Automatización y puesta en marcha de 3 CNC: tablero eléctrico, comunicación controladores-PC, programación y ajuste "
           "de parámetros del variador del husillo.") if L else
          ("Automation and commissioning of 3 CNC machines: electrical panel, controller-PC communication, programming and "
           "spindle drive parameter tuning.")]),
        (("Blockstrong Motors — Diseñador y Programador PLC" if L else "Blockstrong Motors — PLC Designer & Programmer"), "2020",
         [("Automatización de bruñidora de motores de camión (4-6 cil.) con Siemens S7-200: ladder, sensores inductivos, calibre "
           "de aire, servomotores y husillos. Manuales de usuario y funcionamiento.") if L else
          ("Automation of a truck-engine honing machine (4-6 cyl.) with a Siemens S7-200: ladder, inductive sensors, air gauge, "
           "servomotors and spindles. User and operation manuals.")]),
        (("Freelance — Diseñador y Técnico" if L else "Freelance — Designer & Technician"), "2019 — 2021",
         [("Desarrollo y producción, junto a kinesiólogos y fisioterapeutas, de una adaptación de auriculares con sistema de LEDs "
           "para asistir a pacientes con Parkinson y/o parálisis parcial.") if L else
          ("Development and production, with kinesiologists and physiotherapists, of a headset adaptation with an LED system to "
           "assist patients with Parkinson's and/or partial paralysis.")]),
    ]
    for title, date, bullets in exp:
        blk = [Paragraph(title, s['sub']), Paragraph(date, s['date'])]
        for b in bullets: blk.append(Paragraph(b, s['bull'], bulletText='•'))
        st.append(KeepTogether(blk))

    st.append(Paragraph("PROYECTO DESTACADO" if L else "FEATURED PROJECT", s['h']))
    st.append(Paragraph("ElectronArt — Suite EDA propia" if L else "ElectronArt — Own EDA Suite", s['sub']))
    st.append(Paragraph(
        ("Desarrollo de un EDA de escritorio todo-en-uno (Python, PySide6/Qt, NumPy/SciPy): esquemáticos ANSI/IEC, PCB "
         "multicapa, simulación SPICE y de firmware MCU, visor 3D y modo educativo. Suite de verificación con 111 tests "
         "automatizados. Multiplataforma (Windows/Linux/macOS).") if L else
        ("Development of an all-in-one desktop EDA (Python, PySide6/Qt, NumPy/SciPy): ANSI/IEC schematics, multilayer PCB, "
         "SPICE and MCU-firmware simulation, 3D viewer and educational mode. Verification suite with 111 automated tests. "
         "Cross-platform (Windows/Linux/macOS)."), s['body']))

    st.append(Paragraph("EDUCACIÓN" if L else "EDUCATION", s['h']))
    st.append(Paragraph("Ingeniería Electrónica (en curso, 4.º año) — UTN Facultad Regional Córdoba" if L
                        else "Electronic Engineering (in progress, 4th year) — UTN Córdoba (FRC)", s['sub']))
    st.append(Paragraph("2022 — " + ("presente" if L else "present"), s['date']))
    st.append(Paragraph("Técnico Electrónico — ITS Villada" if L else "Electronics Technician — ITS Villada", s['sub']))
    st.append(Paragraph("2020 — " + ("Egresado con méritos" if L else "Graduated with merits"), s['date']))

    st.append(Paragraph("HABILIDADES" if L else "SKILLS", s['h']))
    sk_es = [("PCB & Circuitos", "Altium Designer, PCB multicapa, esquemáticos, footprints, Proteus, LTspice"),
             ("Embebidos", "C/C++, Python, PIC/dsPIC, ATmega, ESP32/MicroPython, Verilog/HDL (Xilinx)"),
             ("Automatización", "PLC Siemens (ladder), CNC/Mach3, tableros eléctricos, sensórica y actuadores"),
             ("CAD & Mecánica", "Fusion 360, SolidWorks, AutoCAD, QElectroTech, impresión 3D (STL/STEP)"),
             ("Software", "PySide6/Qt, NumPy/SciPy/OpenCV, Git, GUIs web embebidas"),
             ("Idiomas", "Español (nativo) · Inglés C1 · Alemán A2")]
    sk_en = [("PCB & Circuits", "Altium Designer, multilayer PCB, schematics, footprints, Proteus, LTspice"),
             ("Embedded", "C/C++, Python, PIC/dsPIC, ATmega, ESP32/MicroPython, Verilog/HDL (Xilinx)"),
             ("Automation", "Siemens PLC (ladder), CNC/Mach3, electrical panels, sensors and actuators"),
             ("CAD & Mechanical", "Fusion 360, SolidWorks, AutoCAD, QElectroTech, 3D printing (STL/STEP)"),
             ("Software", "PySide6/Qt, NumPy/SciPy/OpenCV, Git, embedded web GUIs"),
             ("Languages", "Spanish (native) · English C1 · German A2")]
    rows = [[Paragraph(f"<b>{a}</b>", s['body']), Paragraph(b, s['body'])] for a, b in (sk_es if L else sk_en)]
    t = Table(rows, colWidths=[38*mm, None])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                           ('LINEBELOW',(0,0),(-1,-2),0.4,LINE),
                           ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),
                           ('LEFTPADDING',(0,0),(-1,-1),0)]))
    st.append(t)

    st.append(Paragraph("DISPONIBILIDAD" if L else "AVAILABILITY", s['h']))
    st.append(Paragraph(("Posición part-time (preferentemente por la mañana), remota o presencial en Córdoba. "
                         "Horarios y días negociables. Disponibilidad inmediata.") if L else
                        ("Part-time position (preferably morning hours), remote or on-site in Córdoba. "
                         "Hours and days negotiable. Immediate availability."), s['body']))
    doc.build(st)
    return path

# ---------------------------------------------------------------- Portfolio
def build_portfolio(lang):
    s = styles(); L = lang == 'es'
    path = os.path.join(OUT, f"Portfolio - Franco Olmedo - {'Espanol' if L else 'English'} - 2026.pdf")
    doc = doc_template(path, "Franco Olmedo — Portfolio 2026")
    st = []
    st.append(Spacer(1, 40))
    st.append(Paragraph("PORTFOLIO", ParagraphStyle('pf', fontName='Helvetica-Bold', fontSize=40, textColor=ACC, leading=46)))
    st.append(Paragraph("Franco Olmedo", ParagraphStyle('pf2', fontName='Helvetica-Bold', fontSize=22, textColor=DARK, leading=30, spaceBefore=6)))
    st.append(Paragraph("Electrónica · Sistemas Embebidos · Automatización Industrial" if L else
                        "Electronics · Embedded Systems · Industrial Automation",
                        ParagraphStyle('pf3', fontName='Helvetica', fontSize=12, textColor=GREY, leading=17, spaceBefore=4)))
    st.append(Spacer(1, 10)); st.append(rule())
    st.append(Paragraph(("Selección de proyectos profesionales y personales 2019-2026: del esquemático al producto en planta. "
                         "Hardware, firmware, software e integración.") if L else
                        ("Selection of professional and personal projects 2019-2026: from schematic to product on the plant floor. "
                         "Hardware, firmware, software and integration."), s['body']))
    st.append(Paragraph("olmedo.franco.fo@gmail.com · +54 9 351 248-7080 · Villa Allende, Córdoba, AR · <link href='https://francoolmedo.github.io' color='#0e9f6e'>francoolmedo.github.io</link>", s['meta']))
    st.append(Spacer(1, 26))

    def project(num, title, role, desc, bullets, img=None, img_h=70):
        blk = [rule(),
               Paragraph(f"<font color='#0e9f6e'>{num:02d}</font> &nbsp; {title}", s['ptitle']),
               Paragraph(role, s['prole'])]
        if img:
            p = os.path.join(ASSETS, img)
            if os.path.exists(p):
                from PIL import Image as PILImage
                w, h = PILImage.open(p).size
                iw = min(170*mm, (img_h*mm) * w / h)
                blk.append(Image(p, width=iw, height=img_h*mm))
                blk.append(Spacer(1, 6))
        blk.append(Paragraph(desc, s['body']))
        for b in bullets:
            blk.append(Paragraph(b, s['bull'], bulletText='•'))
        blk.append(Spacer(1, 12))
        st.append(KeepTogether(blk) if not img else blk[0]);
        if img:
            for x in blk[1:]: st.append(x)

    P = [
      ("ElectronArt — Suite EDA" , "Producto propio · Electronik Lösungen" if L else "Own product · Electronik Lösungen",
       ("EDA de escritorio todo-en-uno de desarrollo propio: captura de esquemáticos (ANSI/IEC), PCB multicapa, simulación SPICE "
        "y de firmware MCU, visor 3D y modo educativo. Un solo software que cubre lo que hoy requiere Altium + Proteus + QElectroTech.") if L else
       ("Self-developed all-in-one desktop EDA: schematic capture (ANSI/IEC), multilayer PCB, SPICE and MCU firmware simulation, "
        "3D viewer and educational mode. One tool covering what currently takes Altium + Proteus + QElectroTech."),
       [("Python 3.11 · PySide6/Qt · NumPy · SciPy · Matplotlib · ReportLab — Windows/Linux/macOS." ),
        ("Suite de verificación: 111 tests automatizados en verde." if L else "Verification suite: 111 automated tests, all green."),
        ("Import/Export: Gerber, DXF/DWG, KiCad, PDF, Excel." )],
       "electronart_app.png", 88),
      ("AgroPlant — " + ("Clasificador de papa semilla por visión robótica" if L else "Seed potato classifier by robotic vision"), "Contraut SAS",
       ("Equipo clasificador de papa semilla instalado en planta: visión por computadora para estimar peso y grado, segmentación "
        "de contorno, estimación volumétrica y clasificación en 5 categorías con acumulación en cajones. Registro de cosechas por semana/año.") if L else
       ("Seed-potato classifier installed on-site: computer vision to estimate weight and grade, contour segmentation, volumetric "
        "estimation and 5-category classification with physical drawer accumulation. Harvest logging by week/year."),
       [("RPi GUI táctil + RPi cámara + dsPIC33F (servos, cintas, balanza, compuertas)." if L else
         "Touchscreen RPi GUI + camera RPi + dsPIC33F (servos, belts, scale, gates)."),
        ("OpenCV · calibración guiada · autochequeo · manual de operador completo." if L else
         "OpenCV · guided calibration · self-check · full operator manual.")],
       "papometro_vision.jpg", 80),
      ("MixOil V5 — " + ("Control de planta de pirólisis" if L else "Pyrolysis plant control"), "Contraut SAS",
       ("Sistema de control, adquisición y telemetría: monitoreo en tiempo real de temperaturas de horno (TIR/TCF), balanza, GUI "
        "web de supervisión y simulación del ciclo completo de 15 h para ensayos.") if L else
       ("Control, acquisition and telemetry system: real-time furnace temperature monitoring (TIR/TCF), weighing system, web "
        "supervision GUI and full 15-hour cycle simulation for test runs."),
       [("GUI web con gráficos en vivo y registro histórico." if L else "Web GUI with live charts and historical logging."),
        ("Informes técnicos de mejoras validados con datos de planta." if L else "Technical improvement reports validated with plant data.")],
       "mixoil_web.png", 60),
      (("PCBs industriales para entornos CNC" if L else "Industrial PCBs for CNC environments"), "Contraut SAS",
       ("Familia de placas de diseño y producción propia: central de control, control RF, derivaciones MSP430 y adaptadores "
        "SATA-GETAC, integradas en máquinas CNC y bancos de ensayo.") if L else
       ("Family of in-house boards: control central, RF control, MSP430 breakouts and SATA-GETAC adapters, integrated into CNC "
        "machines and test benches."),
       [("Altium: esquemático, ruteo multicapa, footprints y serigrafía propios, BOMs." if L else
         "Altium: schematics, multilayer routing, custom footprints and silkscreen, BOMs."),
        ("Fabricación local y en China; ensamble, testing y puesta en marcha." if L else
         "Local and Chinese fabrication; assembly, testing and commissioning."),
        ("Firmware PIC / ATmega / Xilinx según función." if L else "PIC / ATmega / Xilinx firmware per board function.")]),
      (("Bruñidora — Automatización con PLC" if L else "Honing machine — PLC automation"), "Blockstrong Motors",
       ("Automatización integral de bruñidora de motores de camión (4-6 cilindros) con Siemens S7-200: ladder horizontal/vertical, "
        "tablero de control, sensórica industrial y documentación completa (manuales de usuario y funcionamiento).") if L else
       ("Full automation of a truck-engine honing machine (4-6 cylinders) with a Siemens S7-200: horizontal/vertical ladder, "
        "control panel, industrial sensors and complete documentation (user and operation manuals)."),
       [("Sensores inductivos, calibre de aire, servomotores y husillos." if L else
         "Inductive sensors, air gauge, servomotors and spindles.")]),
      (("REESpirator — Ventilador de emergencia" if L else "REESpirator — Emergency ventilator"), "CovidLab · UNRC",
       ("Participación en proyecto de ventilación de emergencia junto a la UNRC durante la pandemia: electrónica de control, "
        "documentación técnica y entregables de ingeniería del prototipo respirador23.") if L else
       ("Participation in an emergency ventilation project with UNRC during the pandemic: control electronics, technical "
        "documentation and engineering deliverables of the respirador23 prototype."),
       []),
      (("Obra “Respiración” — Instalación cinética" if L else "“Respiración” — Kinetic art installation"),
       ("Proyecto artístico-técnico independiente" if L else "Independent art-tech project"),
       ("Instalación electrónica que simula la respiración: sistema neumático con manifold y bypass box modelados en 3D, servos "
        "PCA9685 y firmware MicroPython con detección de presencia. Simulador, bosquejos y cotización de producción.") if L else
       ("Electronic installation simulating breathing: pneumatic system with 3D-modeled manifold and bypass box, PCA9685 servos "
        "and MicroPython firmware with presence detection. Simulator, sketches and production quotation."),
       [], "obra_bosquejo.jpg", 62),
      (("Diseño CAD 3D y prototipado" if L else "3D CAD design & prototyping"), ("Proyectos propios" if L else "Personal projects"),
       ("Gabinetes y piezas funcionales: carcasa slim para SSD/HDD (render), gabinete Raspberry Pi 3B con micrófono I2S y LEDs, "
        "teclados matriciales y piezas a medida. Modelado paramétrico, STL/STEP e impresión 3D.") if L else
       ("Enclosures and functional parts: slim SSD/HDD case (render), Raspberry Pi 3B enclosure with I2S microphone and LEDs, "
        "matrix keypads and custom parts. Parametric modeling, STL/STEP and 3D printing."),
       [], "ssd_render.png", 62),
    ]
    for i, pr in enumerate(P, 1):
        if len(pr) == 4: title, role, desc, bl = pr; img=None; ih=70
        elif len(pr) == 6: title, role, desc, bl, img, ih = pr
        project(i, title, role, desc, bl, img, ih)

    doc.build(st)
    return path

# ---------------------------------------------------------------- CV alemán
def build_cv_de():
    s = styles()
    path = os.path.join(OUT, "CV - Franco Olmedo - Deutsch - 2026.pdf")
    doc = doc_template(path, "Franco Olmedo — Lebenslauf 2026")
    st = []
    st.append(Paragraph("Franco Olmedo", s['name']))
    st.append(Paragraph("Elektroniktechniker · Student des Elektronikingenieurwesens (UTN FRC)", s['role']))
    st.append(Spacer(1, 4))
    st.append(Paragraph("Villa Allende, Córdoba, Argentinien &nbsp;|&nbsp; +54 9 351 248-7080 &nbsp;|&nbsp; olmedo.franco.fo@gmail.com &nbsp;|&nbsp; <link href='https://francoolmedo.github.io' color='#0e9f6e'>francoolmedo.github.io</link>", s['meta']))
    st.append(Spacer(1, 6)); st.append(rule())

    st.append(Paragraph("PROFIL", s['h']))
    st.append(Paragraph(
        "Elektroniktechniker mit Auszeichnung (ITS Villada) und fortgeschrittener Student (4. Jahr) des "
        "Elektronikingenieurwesens an der UTN Córdoba (FRC). Seit 2019 realisiere ich reale Elektronikprojekte: "
        "Entwicklung und Fertigung mehrlagiger Leiterplatten, eingebettete Firmware, Industrieautomatisierung und "
        "Ingenieursoftware. Ich arbeite mit ingenieurmäßiger Sorgfalt: vollständige Dokumentation, Tests und sauber "
        "abgeschlossene Lieferungen.", s['body']))

    st.append(Paragraph("BERUFSERFAHRUNG", s['h']))
    exp = [
        ("POL SRL — Praktikant, Automatisierung & Umwelttechnik", "2026 — heute",
         ["Praktikum in der Umwelttechnik: Prozessautomatisierung, Projektmanagement, Webdesign und Datenbankverwaltung. "
          "Entwicklung von Projekten mit Biodigestoren, Biokohle und Wurmfiltern zur Abwasserbehandlung."]),
        ("Contraut SAS — Junior-Elektronikingenieur", "2022 — heute",
         ["Entwicklung und Fertigung eigener Leiterplatten für CNC-Umgebungen: Schaltungen, Prototyping, Analyse, "
          "Fertigung und Test. Programmierung der Mikrocontroller (PIC, dsPIC, ATmega, Xilinx).",
          "Schlüsselfertige Projekte: Kartoffelsortierer per Robotersicht (AgroPlant), Steuerung und Telemetrie "
          "einer Pyrolyseanlage (MixOil V5), Prüfstände und Messsysteme für FAESA und Astillero Río Santiago."]),
        ("Freiberuflich — Entwickler & Techniker", "2021",
         ["Automatisierung und Inbetriebnahme von 3 CNC-Maschinen: Schaltschrank, Kommunikation Steuerung-PC, "
          "Programmierung und Parametrierung des Spindelantriebs."]),
        ("Blockstrong Motors — SPS-Entwickler & Programmierer", "2020",
         ["Automatisierung einer Honmaschine für LKW-Motoren (4-6 Zyl.) mit Siemens S7-200: Ladder, induktive "
          "Sensoren, Luftmesslehre, Servomotoren und Spindeln. Erstellung der Benutzer- und Funktionshandbücher."]),
        ("Freiberuflich — Entwickler & Techniker", "2019 — 2021",
         ["Entwicklung und Fertigung, gemeinsam mit Kinesiologen und Physiotherapeuten, eines Kopfhörer-Aufsatzes "
          "mit LED-System zur Unterstützung von Patienten mit Parkinson und/oder partieller Lähmung."]),
    ]
    for title, date, bullets in exp:
        blk = [Paragraph(title, s['sub']), Paragraph(date, s['date'])]
        for b in bullets: blk.append(Paragraph(b, s['bull'], bulletText='•'))
        st.append(KeepTogether(blk))

    st.append(Paragraph("AUSGEWÄHLTES PROJEKT", s['h']))
    st.append(Paragraph("ElectronArt — Eigene EDA-Suite", s['sub']))
    st.append(Paragraph(
        "Entwicklung einer All-in-One-Desktop-EDA (Python, PySide6/Qt, NumPy/SciPy): ANSI/IEC-Schaltpläne, "
        "mehrlagige Leiterplatten, SPICE- und MCU-Firmware-Simulation, 3D-Ansicht und Lernmodus. "
        "Verifikationssuite mit 111 automatisierten Tests. Plattformübergreifend (Windows/Linux/macOS).", s['body']))

    st.append(Paragraph("AUSBILDUNG", s['h']))
    st.append(Paragraph("Elektronikingenieurwesen (laufend, 4. Jahr) — UTN Córdoba (FRC)", s['sub']))
    st.append(Paragraph("2022 — heute", s['date']))
    st.append(Paragraph("Elektroniktechniker — ITS Villada", s['sub']))
    st.append(Paragraph("2020 — Abschluss mit Auszeichnung", s['date']))

    st.append(Paragraph("KENNTNISSE", s['h']))
    sk = [("Leiterplatten & Schaltungen", "Altium Designer, mehrlagige Leiterplatten, Schaltpläne, Footprints, Proteus, LTspice"),
          ("Embedded", "C/C++, Python, PIC/dsPIC, ATmega, ESP32/MicroPython, Verilog/HDL (Xilinx)"),
          ("Automatisierung", "Siemens-SPS (Ladder), CNC/Mach3, Schaltschränke, Sensorik und Aktorik"),
          ("CAD & Mechanik", "Fusion 360, SolidWorks, AutoCAD, QElectroTech, 3D-Druck (STL/STEP)"),
          ("Software", "PySide6/Qt, NumPy/SciPy/OpenCV, Git, eingebettete Web-GUIs"),
          ("Sprachen", "Spanisch (Muttersprache) · Englisch C1 · Deutsch A2")]
    rows = [[Paragraph(f"<b>{a}</b>", s['body']), Paragraph(b, s['body'])] for a, b in sk]
    t = Table(rows, colWidths=[42*mm, None])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                           ('LINEBELOW',(0,0),(-1,-2),0.4,LINE),
                           ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),
                           ('LEFTPADDING',(0,0),(-1,-1),0)]))
    st.append(t)

    st.append(Paragraph("VERFÜGBARKEIT", s['h']))
    st.append(Paragraph("Teilzeitstelle (bevorzugt vormittags), remote oder vor Ort in Córdoba. "
                        "Zeiten und Tage verhandelbar. Sofort verfügbar. Hinweis: Deutschkenntnisse auf Niveau A2 — "
                        "flüssige Kommunikation auf Englisch oder Spanisch.", s['body']))
    doc.build(st)
    return path

for lang in ('es', 'en'):
    print(build_cv(lang))
    print(build_portfolio(lang))
print(build_cv_de())
print("OK")

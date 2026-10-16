# -*- coding: utf-8 -*-
"""Genera index.html (ES), en/index.html y de/index.html desde un solo contenido.
Uso: python3 tools/build.py   (requiere Pillow solo para leer medidas de imagen)

Reglas de texto (ASD-STE100): frases cortas, voz activa, cifras concretas,
sin adjetivos vacíos. Un dato que no tiene evidencia no entra como proyecto."""
import os
from html import escape
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITIO = "https://franco.electroniklosungen.com.ar/"
REV = "2026-10"
MAIL = "olmedo.franco.fo@gmail.com"
TEL = "+54 9 351 248-7080"
WA = "5493512487080"
EA = "https://electroniklosungen.com.ar"
LINKEDIN = "https://www.linkedin.com/in/franco-olmedo-967405194/"
LANGS = ("es", "en", "de")
RUTA = {"es": "", "en": "en/", "de": "de/"}


def img_size(nombre):
    with Image.open(os.path.join(RAIZ, "assets", "img", f"{nombre}-640.webp")) as im:
        return im.size


# ---------------------------------------------------------------- contenido
T = {
"es": dict(
    title="Franco Olmedo — Técnico electrónico: placas, firmware y tableros",
    desc="Técnico electrónico en Córdoba. Diseño placas, firmware (ESP32, dsPIC, STM32) y tableros IEC. Clasificador de papa U9 en planta, control de pirólisis MixOil y ElectronArt, EDA en castellano.",
    og_locale="es_AR",
    skip="Ir al contenido",
    nav=[("trabajos", "Trabajos"), ("otros", "Otros"), ("experiencia", "Experiencia"), ("contacto", "Contacto")],
    kicker="Técnico electrónico · Córdoba, Argentina",
    lead="Diseño placas, escribo firmware y armo tableros. Después los instalo y los pongo en marcha en planta.",
    sub="Estudio Ingeniería Electrónica en la FCEFyN (UNC). Trabajo en POL S.R.L., una empresa de residuos y economía circular. Desde 2019 entrego equipos para la industria y el agro.",
    cta_wa="Escribir por WhatsApp", cta_mail="Enviar un mail", cta_ea="Ver ElectronArt",
    wa_text="Hola Franco, te escribo desde tu portfolio.",
    block=[("Base", "Villa Allende, Córdoba"), ("Hoy", "POL S.R.L."), ("Estudio", "Ing. Electrónica · FCEFyN–UNC"), ("Idiomas", "ES · EN C1 · DE A2")],
    hero_cap="Clasificador U9 en la planta de AgroPlant, junio de 2025. La pantalla avisa que el cajón de grado 1 está lleno.",
    sec_trab="Trabajos", sec_trab_sub="Cada trabajo de esta lista tiene fotos, capturas o datos reales. Lo que no tiene evidencia publicada está en «Otros».",
    l_client="Cliente", l_year="Año", l_where="Dónde", l_stack="Técnica", l_status="Estado",
    st_op="En operación", st_run="En curso", st_sale="A la venta", st_proto="Prototipo armado", st_done="Terminado",
    fig="Fig.", open_img="Abrir imagen en tamaño completo",
    sec_otros="Otros trabajos", sec_otros_sub="Estos trabajos no tienen fotos publicadas. Si te sirve un caso, te mando los detalles por mail.",
    th=("Año", "Trabajo", "Para", "Evidencia"),
    sec_exp="Experiencia", sec_edu="Formación", sec_tools="Herramientas",
    sec_ct="Contacto",
    ct_lead="¿Tenés una máquina, una placa o un tablero para resolver?",
    ct_sub="Contame qué tiene que hacer, cuántas unidades necesitás y para cuándo. Te respondo con una propuesta concreta.",
    ct_cv="CV en PDF", ct_other="También",
    foot="HTML y CSS hechos a mano. Sin frameworks ni rastreadores.",
    present="hoy", ongoing="en curso",
),
"en": dict(
    title="Franco Olmedo — Electronics technician: PCBs, firmware and control panels",
    desc="Electronics technician in Córdoba, Argentina. I design PCBs, firmware (ESP32, dsPIC, STM32) and IEC control panels. U9 potato grader in production, MixOil pyrolysis control and ElectronArt EDA.",
    og_locale="en_US",
    skip="Skip to content",
    nav=[("trabajos", "Work"), ("otros", "Other"), ("experiencia", "Experience"), ("contacto", "Contact")],
    kicker="Electronics technician · Córdoba, Argentina",
    lead="I design PCBs, write firmware and build control panels. Then I install them and commission them on site.",
    sub="I study Electronic Engineering at FCEFyN (National University of Córdoba). I work at POL S.R.L., a waste and circular-economy company. Since 2019 I deliver equipment for industry and agriculture.",
    cta_wa="Message on WhatsApp", cta_mail="Send an email", cta_ea="See ElectronArt",
    wa_text="Hi Franco, I found you through your portfolio.",
    block=[("Base", "Villa Allende, Córdoba, AR"), ("Now", "POL S.R.L."), ("Studies", "Electronic Eng. · FCEFyN–UNC"), ("Languages", "ES · EN C1 · DE A2")],
    hero_cap="U9 grader at the AgroPlant site, June 2025. The screen reports that the grade 1 bin is full.",
    sec_trab="Work", sec_trab_sub="Each project on this list has real photos, screenshots or data. Work without published evidence is under “Other”.",
    l_client="Client", l_year="Year", l_where="Where", l_stack="Tech", l_status="Status",
    st_op="In production", st_run="In progress", st_sale="On sale", st_proto="Prototype built", st_done="Finished",
    fig="Fig.", open_img="Open full-size image",
    sec_otros="Other work", sec_otros_sub="These projects have no published photos. If a case is relevant to you, I can send details by email.",
    th=("Year", "Work", "For", "Evidence"),
    sec_exp="Experience", sec_edu="Education", sec_tools="Tools",
    sec_ct="Contact",
    ct_lead="Do you have a machine, a board or a control panel to build?",
    ct_sub="Tell me what it must do, how many units you need and your deadline. I reply with a concrete proposal.",
    ct_cv="CV as PDF", ct_other="Also",
    foot="Hand-written HTML and CSS. No frameworks, no trackers.",
    present="now", ongoing="ongoing",
),
"de": dict(
    title="Franco Olmedo — Elektroniktechniker: Leiterplatten, Firmware und Schaltschränke",
    desc="Elektroniktechniker in Córdoba, Argentinien. Ich entwickle Leiterplatten, Firmware (ESP32, dsPIC, STM32) und IEC-Schaltschränke. Kartoffelsortierer U9 im Einsatz, Pyrolyse-Steuerung MixOil und ElectronArt EDA.",
    og_locale="de_DE",
    skip="Zum Inhalt",
    nav=[("trabajos", "Projekte"), ("otros", "Weitere"), ("experiencia", "Erfahrung"), ("contacto", "Kontakt")],
    kicker="Elektroniktechniker · Córdoba, Argentinien",
    lead="Ich entwickle Leiterplatten, schreibe Firmware und baue Schaltschränke. Danach installiere ich sie und nehme sie vor Ort in Betrieb.",
    sub="Ich studiere Elektrotechnik (Elektronik) an der FCEFyN, Nationaluniversität Córdoba. Ich arbeite bei POL S.R.L., einem Unternehmen für Abfall und Kreislaufwirtschaft. Seit 2019 liefere ich Anlagen für Industrie und Landwirtschaft.",
    cta_wa="Nachricht per WhatsApp", cta_mail="E-Mail senden", cta_ea="ElectronArt ansehen",
    wa_text="Hallo Franco, ich schreibe dir über dein Portfolio.",
    block=[("Ort", "Villa Allende, Córdoba, AR"), ("Aktuell", "POL S.R.L."), ("Studium", "Elektronik · FCEFyN–UNC"), ("Sprachen", "ES · EN C1 · DE A2")],
    hero_cap="Sortierer U9 bei AgroPlant, Juni 2025. Der Bildschirm meldet: Behälter Klasse 1 ist voll.",
    sec_trab="Projekte", sec_trab_sub="Jedes Projekt auf dieser Liste hat echte Fotos, Screenshots oder Messdaten. Arbeiten ohne veröffentlichte Belege stehen unter „Weitere“.",
    l_client="Kunde", l_year="Jahr", l_where="Wo", l_stack="Technik", l_status="Status",
    st_op="Im Einsatz", st_run="Laufend", st_sale="Im Verkauf", st_proto="Prototyp gebaut", st_done="Abgeschlossen",
    fig="Abb.", open_img="Bild in voller Größe öffnen",
    sec_otros="Weitere Arbeiten", sec_otros_sub="Für diese Arbeiten gibt es keine veröffentlichten Fotos. Details schicke ich gern per E-Mail.",
    th=("Jahr", "Arbeit", "Für", "Belege"),
    sec_exp="Erfahrung", sec_edu="Ausbildung", sec_tools="Werkzeuge",
    sec_ct="Kontakt",
    ct_lead="Sie haben eine Maschine, eine Leiterplatte oder einen Schaltschrank zu bauen?",
    ct_sub="Schreiben Sie mir, was das Gerät tun muss, wie viele Stück Sie brauchen und bis wann. Ich antworte mit einem konkreten Angebot.",
    ct_cv="Lebenslauf als PDF", ct_other="Außerdem",
    foot="Handgeschriebenes HTML und CSS. Keine Frameworks, keine Tracker.",
    present="heute", ongoing="laufend",
),
}

# Proyectos con evidencia. Cada texto: dict por idioma.
def L(es, en, de):
    return {"es": es, "en": en, "de": de}

PROYECTOS = [
dict(
    id="u9", status="st_op", grid="c3",
    title=L("Clasificador de papa semilla U9", "U9 seed-potato grader", "Saatkartoffel-Sortierer U9"),
    meta=[("l_client", L("AgroPlant", "AgroPlant", "AgroPlant")),
          ("l_where", L("Contraut SAS", "Contraut SAS", "Contraut SAS")),
          ("l_year", L("2025", "2025", "2025")),
          ("l_stack", L("OpenCV · 2× Raspberry Pi · dsPIC33F", "OpenCV · 2× Raspberry Pi · dsPIC33F", "OpenCV · 2× Raspberry Pi · dsPIC33F"))],
    lead=L("La máquina pesa cada papa con una cámara y la manda a uno de 6 cajones.",
           "The machine weighs each potato with a camera and sends it to one of 6 bins.",
           "Die Maschine wiegt jede Kartoffel mit einer Kamera und leitet sie in einen von 6 Behältern."),
    bullets=L(
        ["Una Raspberry Pi toma la imagen, segmenta el contorno y calcula el volumen. Con el volumen estima el peso.",
         "Un dsPIC33F mueve los servos, las cintas y las compuertas. También lee la balanza de calibración.",
         "Una segunda Raspberry Pi corre la pantalla táctil del operador.",
         "Clasifica en 6 grados por peso: de 0–5 g hasta más de 60 g.",
         "Registra cada cosecha por semana y año. Avisa cuando un cajón llega a su límite.",
         "Al arrancar, el equipo hace un autochequeo. La calibración es guiada paso a paso.",
         "Entregué el manual de operador e hice la puesta en marcha en la planta del cliente."],
        ["A Raspberry Pi captures the image, segments the contour and calculates the volume. It estimates the weight from the volume.",
         "A dsPIC33F drives the servos, belts and gates. It also reads the calibration scale.",
         "A second Raspberry Pi runs the operator touchscreen.",
         "It sorts into 6 weight grades: from 0–5 g up to more than 60 g.",
         "It logs each harvest by week and year. It warns when a bin reaches its limit.",
         "At start-up the machine runs a self-check. Calibration is guided step by step.",
         "I wrote the operator manual and commissioned the machine at the client's plant."],
        ["Ein Raspberry Pi nimmt das Bild auf, segmentiert die Kontur und berechnet das Volumen. Aus dem Volumen schätzt er das Gewicht.",
         "Ein dsPIC33F steuert Servos, Förderbänder und Klappen. Er liest auch die Kalibrierwaage.",
         "Ein zweiter Raspberry Pi betreibt den Touchscreen für den Bediener.",
         "Er sortiert in 6 Gewichtsklassen: von 0–5 g bis über 60 g.",
         "Er protokolliert jede Ernte nach Woche und Jahr. Er warnt, wenn ein Behälter voll ist.",
         "Beim Start prüft sich die Maschine selbst. Die Kalibrierung führt Schritt für Schritt.",
         "Ich habe das Bedienerhandbuch geschrieben und die Maschine beim Kunden in Betrieb genommen."]),
    figs=[("u9-camara", "", L("Cabina de visión con iluminación LED propia.", "Vision cabin with its own LED lighting.", "Bildkabine mit eigener LED-Beleuchtung.")),
          ("u9-segmentacion", "", L("Segmentación del contorno y eje mayor de una papa.", "Contour segmentation and major axis of a potato.", "Kontursegmentierung und Hauptachse einer Kartoffel.")),
          ("u9-placas", "", L("Placas de interfaz, RTC, conversores y Raspberry Pi en el gabinete.", "Interface boards, RTC, converters and Raspberry Pi in the enclosure.", "Interface-Platinen, RTC, Wandler und Raspberry Pi im Gehäuse.")),
          ("u9-tablero", "", L("Tablero de control con borneras y protecciones.", "Control panel with terminal blocks and protection.", "Schaltschrank mit Klemmen und Schutzorganen.")),
          ("u9-planta", "", L("Equipo en la planta del cliente.", "Machine at the client's plant.", "Anlage beim Kunden.")),
          ("u9-ensayo", "", L("Ensayo de una papa en la cabina.", "Test run with one potato in the cabin.", "Testlauf mit einer Kartoffel in der Kabine."))],
),
dict(
    id="electronart", status="st_sale", link=(EA, "electroniklosungen.com.ar"),
    title=L("ElectronArt — EDA en castellano", "ElectronArt — EDA software", "ElectronArt — EDA-Software"),
    meta=[("l_client", L("Producto propio", "My own product", "Eigenes Produkt")),
          ("l_where", L("Electronik Lösungen", "Electronik Lösungen", "Electronik Lösungen")),
          ("l_stack", L("Python · PySide6 · NumPy/SciPy · SPICE", "Python · PySide6 · NumPy/SciPy · SPICE", "Python · PySide6 · NumPy/SciPy · SPICE"))],
    lead=L("Un solo programa para pasar del esquemático a los archivos de fábrica.",
           "One program that takes a design from schematic to fabrication files.",
           "Ein Programm vom Schaltplan bis zu den Fertigungsdaten."),
    bullets=L(
        ["Incluye esquemático, simulación SPICE, PCB multicapa y vista 3D.",
         "Exporta Gerber con arcos reales, IPC-2581, ODB++ y STEP.",
         "Tiene un módulo eléctrico con símbolos IEC 60617 para tableros y PLC.",
         "La interfaz está en 3 idiomas. La licencia funciona sin conexión y usa firma Ed25519.",
         "252 ensayos automáticos verifican cada versión antes de publicarla."],
        ["It includes schematic capture, SPICE simulation, multilayer PCB layout and a 3D view.",
         "It exports Gerber with true arcs, IPC-2581, ODB++ and STEP.",
         "An electrical module provides IEC 60617 symbols for control panels and PLCs.",
         "The interface is available in 3 languages. The licence works offline with an Ed25519 signature.",
         "252 automated tests check each version before release."],
        ["Enthält Schaltplan, SPICE-Simulation, mehrlagiges Leiterplattenlayout und 3D-Ansicht.",
         "Exportiert Gerber mit echten Bögen, IPC-2581, ODB++ und STEP.",
         "Ein Elektromodul liefert IEC-60617-Symbole für Schaltschränke und SPS.",
         "Die Oberfläche gibt es in 3 Sprachen. Die Lizenz funktioniert offline mit Ed25519-Signatur.",
         "252 automatische Tests prüfen jede Version vor der Freigabe."]),
    figs=[("ea-esquematico", "w", L("Editor de esquemático de ElectronArt.", "ElectronArt schematic editor.", "Schaltplaneditor von ElectronArt.")),
          ("ea-fft", "w", L("Análisis de Fourier sobre una simulación SPICE.", "Fourier analysis of a SPICE simulation.", "Fourier-Analyse einer SPICE-Simulation."))],
),
dict(
    id="mixoil", status="st_run",
    title=L("MixOil V5 — control de una planta de pirólisis", "MixOil V5 — pyrolysis plant control", "MixOil V5 — Steuerung einer Pyrolyseanlage"),
    meta=[("l_client", L("POL S.R.L.", "POL S.R.L.", "POL S.R.L.")),
          ("l_year", L("2026", "2026", "2026")),
          ("l_stack", L("Python · adquisición de datos · web", "Python · data acquisition · web", "Python · Messdatenerfassung · Web"))],
    lead=L("El sistema mide la planta, guarda cada ciclo y muestra los datos en vivo.",
           "The system measures the plant, stores each cycle and shows the data live.",
           "Das System misst die Anlage, speichert jeden Zyklus und zeigt die Daten live."),
    bullets=L(
        ["Mide temperaturas de horno, precalentador y condensador.",
         "Registra 7 variables de proceso y el estado del molino y del quemador.",
         "Una página web en la red de la planta muestra las curvas en vivo.",
         "Un simulador repite el ciclo completo de 15 h. Así pruebo cambios antes de aplicarlos en la planta.",
         "Escribo informes de mejora con los datos de cada ensayo."],
        ["It measures furnace, preheater and condenser temperatures.",
         "It logs 7 process variables and the state of the mill and the burner.",
         "A web page on the plant network shows the live curves.",
         "A simulator replays the full 15-hour cycle. I test changes there before I apply them to the plant.",
         "I write improvement reports from the data of each test run."],
        ["Misst die Temperaturen von Ofen, Vorwärmer und Kondensator.",
         "Protokolliert 7 Prozessgrößen und den Zustand von Mühle und Brenner.",
         "Eine Webseite im Anlagennetz zeigt die Kurven live.",
         "Ein Simulator spielt den ganzen 15-Stunden-Zyklus nach. Dort teste ich Änderungen, bevor ich sie an der Anlage anwende.",
         "Aus den Daten jedes Versuchs schreibe ich Verbesserungsberichte."]),
    figs=[("mixoil-ciclo", "w", L("Registro del ciclo del 11-05-2026: horno, precalentador, condensador y actuadores.",
                                  "Log of the 2026-05-11 cycle: furnace, preheater, condenser and actuators.",
                                  "Aufzeichnung des Zyklus vom 11.05.2026: Ofen, Vorwärmer, Kondensator und Aktoren."))],
),
dict(
    id="respiracion", status="st_proto",
    title=L("«Respiración» — instalación cinética", "“Respiración” — kinetic installation", "„Respiración“ — kinetische Installation"),
    meta=[("l_client", L("Proyecto independiente", "Independent project", "Eigenes Projekt")),
          ("l_stack", L("MicroPython · PCA9685 · neumática · impresión 3D", "MicroPython · PCA9685 · pneumatics · 3D printing", "MicroPython · PCA9685 · Pneumatik · 3D-Druck"))],
    lead=L("Una pieza de arte que simula la respiración con aire y servos.",
           "An art piece that imitates breathing with air and servos.",
           "Ein Kunstobjekt, das mit Luft und Servos das Atmen nachahmt."),
    bullets=L(
        ["Modelé e imprimí en 3D el manifold, la caja de bypass, las aletas y los soportes de sensores.",
         "Un PCA9685 controla los servos. El firmware en MicroPython detecta presencia y ejecuta las rutinas de movimiento.",
         "Antes de armar, probé el sistema en un simulador propio. Después preparé la cotización de producción."],
        ["I modelled and 3D-printed the manifold, the bypass box, the fins and the sensor mounts.",
         "A PCA9685 drives the servos. The MicroPython firmware detects presence and runs the motion routines.",
         "Before assembly I tested the system in my own simulator. Then I prepared the production quote."],
        ["Ich habe Verteiler, Bypass-Box, Lamellen und Sensorhalter konstruiert und 3D-gedruckt.",
         "Ein PCA9685 steuert die Servos. Die MicroPython-Firmware erkennt Anwesenheit und fährt die Bewegungsabläufe.",
         "Vor dem Aufbau habe ich das System in einem eigenen Simulator getestet. Danach habe ich das Fertigungsangebot erstellt."]),
    figs=[("obra-control", "", L("Gabinete de control: fuente, protecciones y electrónica.", "Control enclosure: power supply, protection and electronics.", "Steuergehäuse: Netzteil, Schutz und Elektronik.")),
          ("obra-ensamble", "", L("Caja de bypass impresa con la electrónica montada.", "Printed bypass box with the electronics mounted.", "Gedruckte Bypass-Box mit montierter Elektronik.")),
          ("obra-cad", "", L("Modelo CAD de una pieza del manifold.", "CAD model of a manifold part.", "CAD-Modell eines Verteilerteils.")),
          ("obra-completo", "", L("Sistema armado con los conductos de aire.", "Assembled system with the air ducts.", "Aufgebautes System mit Luftleitungen."))],
),
dict(
    id="robot", status="st_done",
    title=L("Robot aspirador", "Robot vacuum", "Saugroboter"),
    meta=[("l_client", L("Proyecto escolar · ITS Villada", "School project · ITS Villada", "Schulprojekt · ITS Villada")),
          ("l_stack", L("SolidWorks · L298N · impresión 3D", "SolidWorks · L298N · 3D printing", "SolidWorks · L298N · 3D-Druck"))],
    lead=L("Mi primer equipo completo: mecánica, placa y firmware.",
           "My first complete machine: mechanics, board and firmware.",
           "Mein erstes vollständiges Gerät: Mechanik, Platine und Firmware."),
    bullets=L(
        ["Diseñé el chasis, el paragolpes con microinterruptores y las hélices en SolidWorks. Imprimí todo en 3D.",
         "Diseñé la placa de potencia con un L298N para los 2 motores de CC.",
         "El firmware lee los choques, controla los motores y la aspiración."],
        ["I designed the chassis, the bumper with micro-switches and the impellers in SolidWorks. I 3D-printed all parts.",
         "I designed the driver board with an L298N for the 2 DC motors.",
         "The firmware reads the bumper, drives the motors and controls suction."],
        ["Chassis, Stoßfänger mit Mikroschaltern und Lüfterräder habe ich in SolidWorks konstruiert und 3D-gedruckt.",
         "Die Treiberplatine mit L298N für die 2 Gleichstrommotoren habe ich selbst entworfen.",
         "Die Firmware liest den Stoßfänger, steuert die Motoren und die Saugleistung."]),
    figs=[("robot-armado", "", L("Robot armado, vista superior.", "Assembled robot, top view.", "Montierter Roboter, Draufsicht.")),
          ("robot-despiece", "", L("Despiece: chasis, placa, motores y batería.", "Exploded layout: chassis, board, motors and battery.", "Explosionsdarstellung: Chassis, Platine, Motoren und Akku."))],
),
]

OTROS = [
    ("2026–", L("Automatización de procesos en compostaje, biochar, biodigestores y lombrifiltro.",
                "Process automation for composting, biochar, biodigesters and vermifilters.",
                "Prozessautomatisierung für Kompostierung, Pflanzenkohle, Biogasanlagen und Wurmfilter."),
     "POL S.R.L.", L("En curso", "In progress", "Laufend")),
    ("2022–", L("Placas para máquinas CNC y bancos de ensayo: central de control, control RF, adaptadores MSP430 y SATA-GETAC. Diseño en Altium, firmware PIC/ATmega/Xilinx.",
                "Boards for CNC machines and test benches: control unit, RF control, MSP430 and SATA-GETAC adapters. Altium layout, PIC/ATmega/Xilinx firmware.",
                "Platinen für CNC-Maschinen und Prüfstände: Steuerzentrale, Funksteuerung, MSP430- und SATA-GETAC-Adapter. Layout in Altium, Firmware für PIC/ATmega/Xilinx."),
     "Contraut SAS", L("Fotos en preparación", "Photos in preparation", "Fotos in Vorbereitung")),
    ("2022–", L("Bancos de ensayo y sistemas de adquisición de datos.",
                "Test benches and data acquisition systems.",
                "Prüfstände und Messdatenerfassung."),
     "FAESA · Astillero Río Santiago", L("Sin fotos publicadas", "No published photos", "Keine Fotos veröffentlicht")),
    ("2021", L("Puesta en marcha de 3 máquinas CNC: tablero eléctrico, comunicación con la PC y ajuste del variador del husillo.",
               "Commissioning of 3 CNC machines: electrical panel, PC communication and spindle drive tuning.",
               "Inbetriebnahme von 3 CNC-Maschinen: Schaltschrank, PC-Anbindung und Einstellung des Spindelumrichters."),
     "Freelance", L("Sin fotos publicadas", "No published photos", "Keine Fotos veröffentlicht")),
    ("2020", L("Bruñidora para motores de camión de 4 a 6 cilindros con PLC Siemens S7-200. Programa ladder, tablero, sensores inductivos y manuales.",
               "Honing machine for 4- to 6-cylinder truck engines with a Siemens S7-200 PLC. Ladder program, panel, inductive sensors and manuals.",
               "Honmaschine für 4- bis 6-Zylinder-LKW-Motoren mit Siemens-S7-200-SPS. KOP-Programm, Schaltschrank, induktive Sensoren und Handbücher."),
     "Blockstrong Motors", L("Manuales entregados al cliente", "Manuals delivered to the client", "Handbücher an den Kunden übergeben")),
    ("2020", L("REESpirator, respirador de emergencia. Participé en la electrónica de control y la documentación.",
               "REESpirator, an emergency ventilator. I worked on the control electronics and the documentation.",
               "REESpirator, ein Notfall-Beatmungsgerät. Ich habe an der Steuerelektronik und der Dokumentation mitgearbeitet."),
     "CovidLab · UNRC", L("Sin fotos publicadas", "No published photos", "Keine Fotos veröffentlicht")),
    ("2019–2021", L("Auriculares con LEDs para pacientes con Parkinson. Trabajo con un equipo de kinesiólogos.",
                    "LED headset for patients with Parkinson's disease. Built with a team of physiotherapists.",
                    "LED-Kopfhörer für Parkinson-Patienten. Entwickelt mit einem Team von Physiotherapeuten."),
     "Freelance", L("Sin fotos publicadas", "No published photos", "Keine Fotos veröffentlicht")),
]

EXP = [
    ("2026–", "POL S.R.L.", L("Pasante de automatización. Residuos y economía circular: compostaje, pirólisis (MixOil) y biochar.",
                              "Automation intern. Waste and circular economy: composting, pyrolysis (MixOil) and biochar.",
                              "Praktikant Automatisierung. Abfall und Kreislaufwirtschaft: Kompostierung, Pyrolyse (MixOil) und Pflanzenkohle.")),
    ("2022–", "Contraut SAS", L("Ingeniero electrónico junior. Diseño y produzco placas propias. Escribo el firmware de cada placa. Hago proyectos de automatización llave en mano.",
                                "Junior electronic engineer. I design and produce in-house boards. I write the firmware for each board. I deliver turn-key automation projects.",
                                "Junior-Elektronikingenieur. Ich entwickle und fertige eigene Platinen. Ich schreibe die Firmware jeder Platine. Ich liefere schlüsselfertige Automatisierungsprojekte.")),
    ("2021", "Freelance", L("Tableros y puesta en marcha de máquinas CNC.", "Panels and commissioning of CNC machines.", "Schaltschränke und Inbetriebnahme von CNC-Maschinen.")),
    ("2020", "Blockstrong Motors", L("Diseño y programación de PLC.", "PLC design and programming.", "SPS-Entwurf und -Programmierung.")),
    ("2019–2021", "Freelance", L("Prototipos de dispositivos médicos.", "Medical device prototypes.", "Prototypen für Medizingeräte.")),
]

EDU = [
    ("", L("Ingeniería Electrónica", "Electronic Engineering", "Studium Elektronik"),
     L("FCEFyN — Universidad Nacional de Córdoba", "FCEFyN — National University of Córdoba", "FCEFyN — Nationaluniversität Córdoba")),
    ("2014–2020", L("Técnico Electrónico", "Electronics Technician", "Elektroniktechniker"),
     L("Instituto Técnico Salesiano Villada", "Instituto Técnico Salesiano Villada", "Instituto Técnico Salesiano Villada")),
]

TOOLS = [
    (L("Placas", "PCB", "Leiterplatten"), "Altium Designer · ElectronArt · LTspice · Proteus"),
    (L("Embebidos", "Embedded", "Embedded"), "C · C++ · ESP32 · STM32 · PIC / dsPIC · ATmega · MicroPython · Verilog (Xilinx)"),
    (L("Automatización", "Automation", "Automatisierung"), L("PLC Siemens (ladder) · tableros IEC · variadores · CNC Mach3 · QElectroTech",
                                                            "Siemens PLC (ladder) · IEC panels · VFDs · CNC Mach3 · QElectroTech",
                                                            "Siemens-SPS (KOP) · IEC-Schaltschränke · Frequenzumrichter · CNC Mach3 · QElectroTech")),
    (L("Software", "Software", "Software"), "Python · PySide6 / Qt · NumPy · SciPy · OpenCV · Git"),
    (L("Mecánica", "Mechanics", "Mechanik"), L("Fusion 360 · SolidWorks · AutoCAD · impresión 3D",
                                               "Fusion 360 · SolidWorks · AutoCAD · 3D printing",
                                               "Fusion 360 · SolidWorks · AutoCAD · 3D-Druck")),
]


def tx(v, lang):
    return v[lang] if isinstance(v, dict) else v


# ---------------------------------------------------------------- render
def figure(nombre, cls, cap, n, t, pre, eager=False):
    w, h = img_size(nombre)
    src = f"{pre}assets/img/{nombre}"
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    sizes = "(min-width: 1000px) 640px, 100vw" if cls == "w" or eager else "(min-width: 1000px) 320px, 50vw"
    return (f'<figure class="fig{" w" if cls == "w" else ""}">'
            f'<a href="{src}-1280.webp" aria-label="{escape(t["open_img"])}: {escape(cap)}">'
            f'<img src="{src}-640.webp" srcset="{src}-640.webp 640w, {src}-1280.webp 1280w" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{escape(cap)}" {load} decoding="async"></a>'
            f'<figcaption><span class="ref">{t["fig"]} {n:02d}</span> {escape(cap)}</figcaption></figure>')


def page(lang):
    t = T[lang]
    pre = "" if lang == "es" else "../"
    url = SITIO + RUTA[lang]
    figno = 1
    o = []
    a = o.append
    a(f'<!doctype html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
      f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
      f'<title>{escape(t["title"])}</title>\n'
      f'<meta name="description" content="{escape(t["desc"])}">\n'
      f'<link rel="canonical" href="{url}">\n')
    for l in LANGS:
        a(f'<link rel="alternate" hreflang="{l}" href="{SITIO + RUTA[l]}">\n')
    a(f'<link rel="alternate" hreflang="x-default" href="{SITIO}">\n'
      f'<meta property="og:type" content="profile">\n'
      f'<meta property="og:title" content="{escape(t["title"])}">\n'
      f'<meta property="og:description" content="{escape(t["desc"])}">\n'
      f'<meta property="og:url" content="{url}">\n'
      f'<meta property="og:locale" content="{t["og_locale"]}">\n'
      f'<meta property="og:image" content="{SITIO}assets/img/og.jpg">\n'
      f'<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
      f'<meta property="og:image:alt" content="{escape(t["hero_cap"])}">\n'
      f'<meta name="twitter:card" content="summary_large_image">\n'
      f'<meta name="theme-color" content="#f2efe6">\n'
      f'<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">\n'
      f'<link rel="preload" href="{pre}assets/fonts/archivo-latin-wdth-normal.woff2" as="font" type="font/woff2" crossorigin>\n'
      f'<style>{CSS.replace("url(assets/", "url(" + pre + "assets/")}</style>\n')
    a('<script type="application/ld+json">' + (
        '{"@context":"https://schema.org","@type":"Person","name":"Franco Olmedo",'
        f'"url":"{SITIO}","email":"mailto:{MAIL}","telephone":"{TEL}",'
        '"jobTitle":"' + {"es": "Técnico electrónico", "en": "Electronics technician", "de": "Elektroniktechniker"}[lang] + '",'
        '"worksFor":{"@type":"Organization","name":"POL S.R.L."},'
        '"alumniOf":{"@type":"EducationalOrganization","name":"Instituto Técnico Salesiano Villada"},'
        '"address":{"@type":"PostalAddress","addressLocality":"Villa Allende","addressRegion":"Córdoba","addressCountry":"AR"},'
        f'"sameAs":["{LINKEDIN}","{EA}"]}}') + '</script>\n</head>\n<body>\n')
    a(f'<a class="skip" href="#main">{t["skip"]}</a>\n')
    # header
    a('<header class="top"><div class="wrap top-in">'
      f'<a class="brand" href="{pre or "./"}"><span class="pin1" aria-hidden="true"></span>Franco Olmedo</a>'
      '<nav aria-label="' + {"es": "Secciones", "en": "Sections", "de": "Abschnitte"}[lang] + '"><ul class="nav">')
    for hid, lab in t["nav"]:
        a(f'<li><a href="#{hid}">{lab}</a></li>')
    a('</ul></nav><ul class="langs" aria-label="Idioma / Language / Sprache">')
    for l in LANGS:
        cur = ' aria-current="page"' if l == lang else ""
        a(f'<li><a href="{pre}{RUTA[l] or "./"}" hreflang="{l}" lang="{l}"{cur}>{l.upper()}</a></li>')
    a('</ul></div></header>\n<main id="main">\n')
    # hero
    wa = f"https://wa.me/{WA}?text=" + t["wa_text"].replace(" ", "%20").replace(",", "%2C")
    a('<section class="hero wrap" aria-labelledby="h-nombre"><div class="hero-txt">'
      f'<p class="kicker">{t["kicker"]}</p>'
      f'<h1 id="h-nombre">Franco Olmedo</h1>'
      f'<p class="lead">{t["lead"]}</p><p class="sub">{t["sub"]}</p>'
      '<div class="ctas">'
      f'<a class="btn btn-1" href="{wa}" rel="noopener">{t["cta_wa"]}</a>'
      f'<a class="btn btn-2" href="mailto:{MAIL}">{t["cta_mail"]}</a>'
      f'<a class="btn btn-3" href="{EA}" rel="noopener">{t["cta_ea"]} <span aria-hidden="true">→</span></a></div>'
      '<dl class="tblock">')
    for k, v in t["block"]:
        a(f'<div><dt>{k}</dt><dd>{v}</dd></div>')
    a('</dl></div><div class="hero-fig">')
    a(figure("u9-hmi-grado", "", t["hero_cap"], figno, t, pre, eager=True)); figno += 1
    a('</div></section>\n')
    # proyectos
    a(f'<section id="trabajos" class="sec wrap" aria-labelledby="h-trab"><div class="sec-h"><p class="net" aria-hidden="true">01</p>'
      f'<h2 id="h-trab">{t["sec_trab"]}</h2><p class="sec-sub">{t["sec_trab_sub"]}</p></div>\n')
    for i, p in enumerate(PROYECTOS, 1):
        st = p["status"]
        a(f'<article class="case" id="{p["id"]}" aria-labelledby="h-{p["id"]}"><div class="case-txt">'
          f'<p class="case-n">{i:02d} / {len(PROYECTOS):02d}</p>'
          f'<h3 id="h-{p["id"]}">{tx(p["title"], lang)}</h3>'
          f'<p class="status {st}"><span class="led" aria-hidden="true"></span>{t[st]}</p>'
          '<dl class="meta">')
        for k, v in p["meta"]:
            a(f'<div><dt>{t[k]}</dt><dd>{tx(v, lang)}</dd></div>')
        a(f'</dl><p class="case-lead">{tx(p["lead"], lang)}</p><ul class="pts">')
        for b in tx(p["bullets"], lang):
            a(f'<li>{b}</li>')
        a('</ul>')
        if p.get("link"):
            a(f'<p><a class="ext" href="{p["link"][0]}" rel="noopener">{p["link"][1]} <span aria-hidden="true">↗</span></a></p>')
        cls = " one" if len(p["figs"]) == 1 else (" " + p["grid"] if p.get("grid") else "")
        a(f'</div><div class="case-figs{cls}">')
        for nombre, cls, cap in p["figs"]:
            a(figure(nombre, cls, tx(cap, lang), figno, t, pre)); figno += 1
        a('</div></article>\n')
    a('</section>\n')
    # otros
    a(f'<section id="otros" class="sec wrap" aria-labelledby="h-otros"><div class="sec-h"><p class="net" aria-hidden="true">02</p>'
      f'<h2 id="h-otros">{t["sec_otros"]}</h2><p class="sec-sub">{t["sec_otros_sub"]}</p></div>'
      '<table class="bom" role="table"><thead role="rowgroup"><tr role="row">')
    for h in t["th"]:
        a(f'<th scope="col" role="columnheader">{h}</th>')
    a('</tr></thead><tbody role="rowgroup">')
    for anio, desc, para, ev in OTROS:
        anio = anio + t["present"] if anio.endswith("–") else anio
        a(f'<tr role="row"><td role="cell" class="y">{anio}</td><td role="cell">{tx(desc, lang)}</td><td role="cell">{para}</td><td role="cell" class="ev">{tx(ev, lang)}</td></tr>')
    a('</tbody></table></section>\n')
    # experiencia + formacion + herramientas
    a(f'<section id="experiencia" class="sec wrap" aria-labelledby="h-exp"><div class="sec-h"><p class="net" aria-hidden="true">03</p>'
      f'<h2 id="h-exp">{t["sec_exp"]}</h2></div><div class="cols">'
      '<div><ol class="tl">')
    for anio, org, d in EXP:
        anio = anio + t["present"] if anio.endswith("–") else anio
        a(f'<li><span class="y">{anio}</span><div><b>{org}</b><p>{tx(d, lang)}</p></div></li>')
    a(f'</ol></div><div><h3 class="h-sm">{t["sec_edu"]}</h3><ol class="tl">')
    for anio, tit, inst in EDU:
        anio = anio or t["ongoing"]
        a(f'<li><span class="y">{anio}</span><div><b>{tx(tit, lang)}</b><p>{tx(inst, lang)}</p></div></li>')
    a(f'</ol><h3 class="h-sm">{t["sec_tools"]}</h3><dl class="tools">')
    for k, v in TOOLS:
        a(f'<div><dt>{tx(k, lang)}</dt><dd>{tx(v, lang)}</dd></div>')
    a('</dl></div></div></section>\n')
    # contacto
    a(f'<section id="contacto" class="sec contact" aria-labelledby="h-ct"><div class="wrap"><div class="sec-h"><p class="net" aria-hidden="true">04</p>'
      f'<h2 id="h-ct">{t["sec_ct"]}</h2></div><div class="ct-grid"><div>'
      f'<p class="ct-lead">{t["ct_lead"]}</p><p class="ct-sub">{t["ct_sub"]}</p>'
      '<div class="ctas">'
      f'<a class="btn btn-1" href="{wa}" rel="noopener">{t["cta_wa"]}</a>'
      f'<a class="btn btn-2" href="mailto:{MAIL}">{t["cta_mail"]}</a></div></div>'
      '<dl class="ct-list">'
      f'<div><dt>Mail</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>'
      f'<div><dt>WhatsApp</dt><dd><a href="{wa}" rel="noopener">{TEL}</a></dd></div>'
      f'<div><dt>{t["ct_cv"]}</dt><dd><a href="{pre}cv-es.pdf" hreflang="es">ES</a> · <a href="{pre}cv-en.pdf" hreflang="en">EN</a> · <a href="{pre}cv-de.pdf" hreflang="de">DE</a></dd></div>'
      f'<div><dt>{t["ct_other"]}</dt><dd><a href="{LINKEDIN}" rel="noopener">LinkedIn</a> · <a href="{EA}" rel="noopener">ElectronArt</a></dd></div>'
      '</dl></div></div></section>\n</main>\n')
    a(f'<footer class="foot wrap"><p>Franco Olmedo · Villa Allende, Córdoba · Rev. {REV}</p><p>{t["foot"]}</p></footer>\n</body>\n</html>\n')
    return "".join(o)


CSS = open(os.path.join(RAIZ, "tools", "estilo.css"), encoding="utf-8").read()


def main():
    for lang in LANGS:
        d = os.path.join(RAIZ, RUTA[lang])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(lang))
        print("ok", lang)


if __name__ == "__main__":
    main()

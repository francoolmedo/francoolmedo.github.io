# -*- coding: utf-8 -*-
"""Genera index.html (ES), en/index.html y de/index.html desde un solo contenido.
Uso: python3 tools/build.py   (requiere Pillow solo para leer medidas de imagen)

Reglas de texto (ASD-STE100): frases cortas, voz activa, cifras concretas,
sin adjetivos vacíos. Un dato que no tiene evidencia no entra como proyecto."""
import json
import math
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
    nav=[("trabajos", "Trabajos"), ("tableros", "Tableros"), ("ia", "IA"), ("otros", "Otros"), ("experiencia", "Experiencia"), ("contacto", "Contacto")],
    kicker="Técnico electrónico · Córdoba, Argentina",
    lead="Diseño placas, firmware y software para máquinas que trabajan en planta. Además desarrollo ElectronArt, mi programa de diseño electrónico.",
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
    foot="HTML, CSS y JS escritos a mano. Sin frameworks ni rastreadores.",
    present="hoy", ongoing="en curso",
),
"en": dict(
    title="Franco Olmedo — Electronics technician: PCBs, firmware and control panels",
    desc="Electronics technician in Córdoba, Argentina. I design PCBs, firmware (ESP32, dsPIC, STM32) and IEC control panels. U9 potato grader in production, MixOil pyrolysis control and ElectronArt EDA.",
    og_locale="en_US",
    skip="Skip to content",
    nav=[("trabajos", "Work"), ("tableros", "Panels"), ("ia", "AI"), ("otros", "Other"), ("experiencia", "Experience"), ("contacto", "Contact")],
    kicker="Electronics technician · Córdoba, Argentina",
    lead="I design boards, firmware and software for machines that run in production. I also develop ElectronArt, my own electronic design program.",
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
    foot="Hand-written HTML, CSS and JS. No frameworks, no trackers.",
    present="now", ongoing="ongoing",
),
"de": dict(
    title="Franco Olmedo — Elektroniktechniker: Leiterplatten, Firmware und Schaltschränke",
    desc="Elektroniktechniker in Córdoba, Argentinien. Ich entwickle Leiterplatten, Firmware (ESP32, dsPIC, STM32) und IEC-Schaltschränke. Kartoffelsortierer U9 im Einsatz, Pyrolyse-Steuerung MixOil und ElectronArt EDA.",
    og_locale="de_DE",
    skip="Zum Inhalt",
    nav=[("trabajos", "Projekte"), ("tableros", "Schaltschränke"), ("ia", "KI"), ("otros", "Weitere"), ("experiencia", "Erfahrung"), ("contacto", "Kontakt")],
    kicker="Elektroniktechniker · Córdoba, Argentinien",
    lead="Ich entwickle Leiterplatten, Firmware und Software für Maschinen im Produktionseinsatz. Außerdem entwickle ich ElectronArt, mein eigenes Programm für Elektronikentwurf.",
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
    foot="Handgeschriebenes HTML, CSS und JS. Keine Frameworks, keine Tracker.",
    present="heute", ongoing="laufend",
),
}

# Textos de las animaciones y de las secciones Tableros e IA.
X = {
"es": dict(
    rt_aria="Animación: autoruteo de una placa con un ESP32 y 74 conexiones. Las pistas se trazan una por una, con codos a 45° y dos capas.",
    rt_cap="Autoruteo en vivo de una placa ESP32 con 74 conexiones: grilla, A*, codos a 45° y 2 capas. Lo calcula tu navegador ahora. En ElectronArt, una placa ESP32 de 74 conexiones queda 74/74 en menos de 5 s.",
    rt_conn="conexiones", rt_vias="vías", rt_pas="pasadas", rt_calc="cálculo", rt_again="Rutear de nuevo",
    rt_top="Capa superior", rt_bot="Capa inferior",
    osc_aria="Osciloscopio: canal 1 con PWM de 1 kHz y canal 2 con la tensión del capacitor del filtro RC.",
    osc_cap="PWM de 1 kHz por un filtro RC de 10 kΩ y 100 nF (τ = 1 ms). La curva sale de la solución exacta del circuito. El ciclo de trabajo sigue el scroll, o movelo vos.",
    osc_d="Ciclo de trabajo", osc_avg="Promedio", osc_pp="Rizado",
    sec_tab="Tableros", sec_tab_sub="Diseño tableros IEC y programo PLC en Ladder desde 2020.",
    lad_h="Arranque directo con enclavamiento",
    lad_p="Es el circuito base de un tablero. MARCHA energiza el contactor KM1. Un contacto auxiliar de KM1 mantiene la bobina. PARADA la corta. PARADA va cableada normal cerrada: I0.1 vale 1 en reposo, y un cable cortado también detiene el motor. ElectronArt simula programas como este antes de armar el tablero.",
    lad_ev="En 2020 programé en Ladder una bruñidora con un PLC Siemens S7-200 (ver «Otros»).",
    lad_try="Mantené apretado MARCHA, soltalo y después apretá PARADA.",
    b_on="MARCHA", b_off="PARADA",
    lad_m=["Reposo: KM1 sin tensión.", "MARCHA cerrado: la bobina de KM1 se energiza.", "Enclavamiento: el contacto de KM1 mantiene la bobina.", "PARADA abierto: KM1 cae y el enclavamiento se abre."],
    io=[("I0.0", "S1 · MARCHA"), ("I0.1", "S0 · PARADA"), ("Q0.0", "KM1 · contactor"), ("Q0.1", "H1 · piloto")],
    lad_aria="Diagrama Ladder de un arranque con enclavamiento: contactos S0, S1 y KM1, bobinas KM1 y H1.",
    sec_ia="IA", sec_ia_sub="IA local medida con un banco propio, y el sistema de agentes con el que trabajo.",
    tri_h="Triana, la IA local de ElectronArt",
    tri_p="Corre Qwen 4B en la PC, sin internet. La medí con un banco de pruebas propio. Estos son los resultados, sin redondear.",
    bars=[("Circuitos completos bien armados", 10, 40), ("Módulos bien conectados a un micro", 9, 12)],
    ag_h="Mi sistema de agentes",
    ag_p="Un orquestador reparte el trabajo. Revisores controlan los cambios. Un modelo local resuelve tareas sin salir de la máquina. La memoria queda en git. Lo uso desde la nube y desde el celular.",
    ag_aria="Esquema del sistema de agentes: celular, orquestador en la nube, memoria en git, dos revisores y un modelo local.",
    nodes=dict(tel=("Celular", ""), orq=("Orquestador", "nube"), git=("git", "memoria"), r1=("Revisor 1", ""), r2=("Revisor 2", ""), loc=("Modelo local", "sin internet")),
    msgs=["pedido", "contexto", "subtarea", "resultado", "diff", "observaciones", "commit", "PR listo"],
),
"en": dict(
    rt_aria="Animation: autorouting a board with an ESP32 and 74 connections. Tracks are drawn one by one, with 45° bends on two layers.",
    rt_cap="Live autorouting of an ESP32 board with 74 connections: grid, A*, 45° bends and 2 layers. Your browser computes it now. In ElectronArt, an ESP32 board with 74 connections routes 74/74 in under 5 s.",
    rt_conn="connections", rt_vias="vias", rt_pas="passes", rt_calc="compute", rt_again="Route again",
    rt_top="Top layer", rt_bot="Bottom layer",
    osc_aria="Oscilloscope: channel 1 shows a 1 kHz PWM, channel 2 the capacitor voltage of the RC filter.",
    osc_cap="1 kHz PWM through an RC filter of 10 kΩ and 100 nF (τ = 1 ms). The curve is the exact solution of the circuit. The duty cycle follows the scroll, or set it yourself.",
    osc_d="Duty cycle", osc_avg="Average", osc_pp="Ripple",
    sec_tab="Panels", sec_tab_sub="I design IEC control panels and program PLCs in Ladder since 2020.",
    lad_h="Direct-on-line start with seal-in",
    lad_p="This is the base circuit of a control panel. START energises contactor KM1. An auxiliary contact of KM1 holds the coil. STOP breaks it. STOP is wired normally closed: I0.1 reads 1 at rest, so a broken wire also stops the motor. ElectronArt simulates programs like this before the panel is built.",
    lad_ev="In 2020 I programmed a honing machine in Ladder on a Siemens S7-200 PLC (see “Other”).",
    lad_try="Hold START, release it, then press STOP.",
    b_on="START", b_off="STOP",
    lad_m=["Idle: KM1 is de-energised.", "START closed: the KM1 coil energises.", "Seal-in: the KM1 contact holds the coil.", "STOP open: KM1 drops out and the seal-in opens."],
    io=[("I0.0", "S1 · START"), ("I0.1", "S0 · STOP"), ("Q0.0", "KM1 · contactor"), ("Q0.1", "H1 · pilot lamp")],
    lad_aria="Ladder diagram of a start with seal-in: contacts S0, S1 and KM1, coils KM1 and H1.",
    sec_ia="AI", sec_ia_sub="Local AI measured on my own bench, and the agent system I work with.",
    tri_h="Triana, the local AI in ElectronArt",
    tri_p="It runs Qwen 4B on the PC, offline. I measured it with my own test bench. These are the results, not rounded.",
    bars=[("Complete circuits built correctly", 10, 40), ("Modules wired correctly to a microcontroller", 9, 12)],
    ag_h="My agent system",
    ag_p="An orchestrator splits the work. Reviewers check the changes. A local model solves tasks without leaving the machine. Memory lives in git. I run it from the cloud and from my phone.",
    ag_aria="Agent system diagram: phone, cloud orchestrator, git memory, two reviewers and a local model.",
    nodes=dict(tel=("Phone", ""), orq=("Orchestrator", "cloud"), git=("git", "memory"), r1=("Reviewer 1", ""), r2=("Reviewer 2", ""), loc=("Local model", "offline")),
    msgs=["request", "context", "subtask", "result", "diff", "comments", "commit", "PR ready"],
),
"de": dict(
    rt_aria="Animation: Autorouting einer Platine mit einem ESP32 und 74 Verbindungen. Die Leiterbahnen entstehen nacheinander, mit 45°-Knicken auf zwei Lagen.",
    rt_cap="Live-Autorouting einer ESP32-Platine mit 74 Verbindungen: Raster, A*, 45°-Knicke und 2 Lagen. Ihr Browser rechnet das jetzt. In ElectronArt wird eine ESP32-Platine mit 74 Verbindungen in unter 5 s zu 74/74 geroutet.",
    rt_conn="Verbindungen", rt_vias="Vias", rt_pas="Durchläufe", rt_calc="Rechenzeit", rt_again="Neu routen",
    rt_top="Oberseite", rt_bot="Unterseite",
    osc_aria="Oszilloskop: Kanal 1 zeigt eine 1-kHz-PWM, Kanal 2 die Kondensatorspannung des RC-Filters.",
    osc_cap="1-kHz-PWM durch ein RC-Filter mit 10 kΩ und 100 nF (τ = 1 ms). Die Kurve ist die exakte Lösung der Schaltung. Das Tastverhältnis folgt dem Scrollen, oder stellen Sie es selbst ein.",
    osc_d="Tastverhältnis", osc_avg="Mittelwert", osc_pp="Welligkeit",
    sec_tab="Schaltschränke", sec_tab_sub="Ich entwerfe IEC-Schaltschränke und programmiere SPS in KOP (Ladder), seit 2020.",
    lad_h="Direktanlauf mit Selbsthaltung",
    lad_p="Das ist eine Grundschaltung im Schaltschrank. EIN erregt das Schütz KM1. Ein Hilfskontakt von KM1 hält die Spule. AUS unterbricht sie. AUS ist als Öffner verdrahtet: I0.1 ist in Ruhe 1, ein Drahtbruch stoppt den Motor also auch. ElectronArt simuliert solche Programme, bevor der Schrank gebaut wird.",
    lad_ev="2020 habe ich eine Honmaschine mit einer Siemens-S7-200-SPS in KOP programmiert (siehe „Weitere“).",
    lad_try="EIN gedrückt halten, loslassen, dann AUS drücken.",
    b_on="EIN", b_off="AUS",
    lad_m=["Ruhe: KM1 ist stromlos.", "EIN geschlossen: die Spule von KM1 zieht an.", "Selbsthaltung: der Kontakt von KM1 hält die Spule.", "AUS geöffnet: KM1 fällt ab, die Selbsthaltung öffnet."],
    io=[("I0.0", "S1 · EIN"), ("I0.1", "S0 · AUS"), ("Q0.0", "KM1 · Schütz"), ("Q0.1", "H1 · Meldeleuchte")],
    lad_aria="KOP-Diagramm eines Anlaufs mit Selbsthaltung: Kontakte S0, S1 und KM1, Spulen KM1 und H1.",
    sec_ia="KI", sec_ia_sub="Lokale KI, gemessen auf einem eigenen Prüfstand, und das Agentensystem, mit dem ich arbeite.",
    tri_h="Triana, die lokale KI in ElectronArt",
    tri_p="Sie läuft mit Qwen 4B auf dem PC, ohne Internet. Ich habe sie mit einem eigenen Prüfstand gemessen. Das sind die Ergebnisse, ungerundet.",
    bars=[("Vollständige Schaltungen korrekt aufgebaut", 10, 40), ("Module korrekt an einen Mikrocontroller angeschlossen", 9, 12)],
    ag_h="Mein Agentensystem",
    ag_p="Ein Orchestrator verteilt die Arbeit. Reviewer prüfen die Änderungen. Ein lokales Modell löst Aufgaben, ohne die Maschine zu verlassen. Das Gedächtnis liegt in Git. Ich steuere es aus der Cloud und vom Handy.",
    ag_aria="Schema des Agentensystems: Handy, Orchestrator in der Cloud, Gedächtnis in Git, zwei Reviewer und ein lokales Modell.",
    nodes=dict(tel=("Handy", ""), orq=("Orchestrator", "Cloud"), git=("git", "Gedächtnis"), r1=("Reviewer 1", ""), r2=("Reviewer 2", ""), loc=("Lokales Modell", "offline")),
    msgs=["Auftrag", "Kontext", "Teilaufgabe", "Ergebnis", "Diff", "Anmerkungen", "Commit", "PR fertig"],
),
}

# Proyectos con evidencia. Cada texto: dict por idioma.
def L(es, en, de):
    return {"es": es, "en": en, "de": de}

PROYECTOS = [
dict(
    id="u9", status="st_op",
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
    figs=[("u9-hmi-grado", "w", L("Pantalla del U9 en la planta de AgroPlant, junio de 2025. Avisa que el cajón de grado 1 está lleno.",
                                  "U9 screen at the AgroPlant site, June 2025. It reports that the grade 1 bin is full.",
                                  "U9-Bildschirm bei AgroPlant, Juni 2025. Er meldet: Behälter Klasse 1 ist voll.")),
          ("u9-camara", "", L("Cabina de visión con iluminación LED propia.", "Vision cabin with its own LED lighting.", "Bildkabine mit eigener LED-Beleuchtung.")),
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
        ["Esquemático y simulación SPICE: transitorio, AC y FFT con THD, SNR, SINAD y SFDR.",
         "PCB multicapa con autoruteo. Una placa con ESP32 y 74 conexiones queda 74/74 en menos de 5 s, con codos a 45° y DRC 0.",
         "Visor 3D. Salida Gerber, Excellon, ODB++, IPC-2581 y STEP.",
         "Tableros IEC con simulación del programa Ladder.",
         "Más de 400 tests automáticos. Versión 9.6, del 22/10/2026."],
        ["Schematic capture and SPICE simulation: transient, AC and FFT with THD, SNR, SINAD and SFDR.",
         "Multilayer PCB with an autorouter. An ESP32 board with 74 connections routes 74/74 in under 5 s, with 45° bends and 0 DRC errors.",
         "3D viewer. Output to Gerber, Excellon, ODB++, IPC-2581 and STEP.",
         "IEC control panels with Ladder program simulation.",
         "More than 400 automated tests. Version 9.6, released 2026-10-22."],
        ["Schaltplan und SPICE-Simulation: Transient, AC und FFT mit THD, SNR, SINAD und SFDR.",
         "Mehrlagige Leiterplatten mit Autorouter. Eine ESP32-Platine mit 74 Verbindungen wird in unter 5 s zu 74/74 geroutet, mit 45°-Knicken und 0 DRC-Fehlern.",
         "3D-Ansicht. Ausgabe als Gerber, Excellon, ODB++, IPC-2581 und STEP.",
         "IEC-Schaltschränke mit Simulation des KOP-Programms (Ladder).",
         "Mehr als 400 automatische Tests. Version 9.6 vom 22.10.2026."]),
    scope=True,
    figs=[("ea-esquematico", "w", L("Editor de esquemático de ElectronArt.", "ElectronArt schematic editor.", "Schaltplaneditor von ElectronArt.")),
          ("ea-fft", "w", L("Análisis de Fourier sobre una simulación SPICE.", "Fourier analysis of a SPICE simulation.", "Fourier-Analyse einer SPICE-Simulation."))],
),
dict(
    id="mixoil", status="st_run",
    title=L("MixOil V5 — control de una planta de pirólisis", "MixOil V5 — pyrolysis plant control", "MixOil V5 — Steuerung einer Pyrolyseanlage"),
    meta=[("l_client", L("POL S.R.L.", "POL S.R.L.", "POL S.R.L.")),
          ("l_where", L("Contraut SAS", "Contraut SAS", "Contraut SAS")),
          ("l_year", L("2026", "2026", "2026")),
          ("l_stack", L("Firmware · MMI · web · Python", "Firmware · HMI · web · Python", "Firmware · HMI · Web · Python"))],
    lead=L("Firmware, MMI y web del control de un quemador de pirólisis a gas y gasoil.",
           "Firmware, HMI and web interface for the control of a gas and diesel pyrolysis burner.",
           "Firmware, HMI und Weboberfläche für die Steuerung eines Pyrolysebrenners für Gas und Diesel."),
    bullets=L(
        ["El control maneja la secuencia de encendido, la clapeta APQ, las alarmas y los gráficos.",
         "Mide temperaturas de horno, precalentador y condensador.",
         "Registra 7 variables de proceso y el estado del molino y del quemador.",
         "Una página web en la red de la planta muestra las curvas en vivo.",
         "Un simulador repite el ciclo completo de 15 h. Así pruebo cambios antes de aplicarlos en la planta.",
         "Escribo informes de mejora con los datos de cada ensayo."],
        ["The controller runs the ignition sequence, the APQ damper, the alarms and the charts.",
         "It measures furnace, preheater and condenser temperatures.",
         "It logs 7 process variables and the state of the mill and the burner.",
         "A web page on the plant network shows the live curves.",
         "A simulator replays the full 15-hour cycle. I test changes there before I apply them to the plant.",
         "I write improvement reports from the data of each test run."],
        ["Die Steuerung führt die Zündsequenz, die APQ-Klappe, die Alarme und die Diagramme.",
         "Misst die Temperaturen von Ofen, Vorwärmer und Kondensator.",
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
    ("—", L("Diseño 3D de la carcasa de un caudalímetro.",
               "3D design of a flow meter enclosure.",
               "3D-Konstruktion eines Durchflussmessergehäuses."),
     "POL S.R.L.", L("Sin fotos publicadas", "No published photos", "Keine Fotos veröffentlicht")),
    ("—", L("PCB V5XCPU3C, diseñada en Altium.",
           "V5XCPU3C PCB, designed in Altium.",
           "Leiterplatte V5XCPU3C, entworfen in Altium."),
     "—", L("Sin fotos publicadas", "No published photos", "Keine Fotos veröffentlicht")),
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



# ---------------------------------------------------------------- animaciones
def rc_pwm(d, f=1000.0, r=10e3, c=100e-9, v=5.0):
    """Régimen permanente de un PWM por un RC: devuelve (Vmin, Vmax)."""
    tau, T = r * c, 1.0 / f
    a, b = math.exp(-d * T / tau), math.exp(-(1 - d) * T / tau)
    vmax = v * (1 - a) / (1 - a * b)
    return vmax * b, vmax


def num(v, lang, dec=2):
    s = f"{v:.{dec}f}"
    return s if lang == "en" else s.replace(".", ",")


def fig_ruteo(x, n, t):
    return (f'<figure class="live rt" id="ruteo" data-conn="{x["rt_conn"]}" data-vias="{x["rt_vias"]}" '
            f'data-pas="{x["rt_pas"]}" data-calc="{x["rt_calc"]}">'
            f'<div class="rt-box"><canvas role="img" aria-label="{escape(x["rt_aria"])}"></canvas></div>'
            f'<div class="hud"><p class="hud-n"><b>0/74</b> {x["rt_conn"]} · DRC <b>—</b></p>'
            f'<p class="hud-k"><span class="k k-top"></span>{x["rt_top"]} <span class="k k-bot"></span>{x["rt_bot"]}</p>'
            f'<button type="button" class="again" hidden>{x["rt_again"]}</button></div>'
            f'<figcaption><span class="ref">{t["fig"]} {n:02d}</span> {escape(x["rt_cap"])}</figcaption></figure>')


def fig_osc(x, n, t, lang):
    vmin, vmax = rc_pwm(0.5)
    return (f'<figure class="fig w live osc" id="osc">'
            f'<div class="osc-box"><canvas role="img" aria-label="{escape(x["osc_aria"])}"></canvas></div>'
            f'<div class="osc-ctl"><label for="osc-d">{x["osc_d"]}</label>'
            f'<input id="osc-d" type="range" min="10" max="90" step="1" value="50"><output for="osc-d">50 %</output></div>'
            f'<dl class="osc-read"><div><dt>CH1</dt><dd>PWM 1 kHz</dd></div>'
            f'<div><dt>CH2 · {x["osc_avg"]}</dt><dd data-r="avg">{num(2.5, lang)} V</dd></div>'
            f'<div><dt>CH2 · {x["osc_pp"]}</dt><dd data-r="pp">{num(vmax - vmin, lang, 3)} V</dd></div></dl>'
            f'<figcaption><span class="ref">{t["fig"]} {n:02d}</span> {escape(x["osc_cap"])}</figcaption></figure>')


def svg_ladder(x):
    o = []
    a = o.append

    def lbl(cx, y, top, bot):
        a(f'<text x="{cx}" y="{y - 19}">{top}</text><text class="ad" x="{cx}" y="{y + 27}">{bot}</text>')

    def contacto(cx, y, cid, top, bot, nc=False):
        a(f'<g class="ct{" nc" if nc else ""}" data-c="{cid}"><rect class="bar" x="{cx + 3}" y="{y - 2}" width="18" height="4"/>'
          f'<path d="M{cx} {y - 12}v24M{cx + 24} {y - 12}v24"/>')
        if nc:
            a(f'<path d="M{cx - 3} {y + 12}L{cx + 27} {y - 12}"/>')
        a('</g>')
        lbl(cx + 12, y, top, bot)

    def bobina(cx, y, cid, top, bot):
        a(f'<g class="coil" data-k="{cid}"><circle cx="{cx + 12}" cy="{y}" r="10"/>'
          f'<path d="M{cx + 7} {y - 11}a14 14 0 0 0 0 22M{cx + 17} {y - 11}a14 14 0 0 1 0 22"/></g>')
        lbl(cx + 12, y, top, bot)

    def w(p, d):
        a(f'<path class="w" data-p="{p}" d="{d}"/>')

    a(f'<svg class="lad" viewBox="0 0 400 252" role="img" aria-label="{escape(x["lad_aria"])}">')
    a('<path class="rail" d="M12 22V234"/><path class="rail r" d="M388 22V234"/>')
    w("a", "M12 64H52"); w("b", "M76 64H140M110 64V128H140"); w("c", "M164 64H214"); w("d", "M164 128H214V64")
    w("e", "M214 64H300M324 64H388"); w("a", "M12 204H140"); w("f", "M164 204H300M324 204H388")
    contacto(52, 64, "S0", "S0", "I0.1")
    contacto(140, 64, "S1", "S1", "I0.0")
    contacto(140, 128, "KM", "KM1", "Q0.0")
    bobina(300, 64, "KM", "KM1", "Q0.0")
    contacto(140, 204, "KM", "KM1", "Q0.0")
    bobina(300, 204, "H1", "H1", "Q0.1")
    a('</svg>')
    return "".join(o)


AG_POS = dict(tel=(90, 40), git=(270, 40), orq=(180, 140), r1=(60, 252), r2=(180, 252), loc=(300, 252))
AG_EDGES = [("tel", "tel", "orq"), ("git", "git", "orq"), ("r1", "orq", "r1"), ("r2", "orq", "r2"), ("loc", "orq", "loc")]
# Pasos: lista de (arista, sentido, mensaje). Sentido 1 = como está dibujada la arista.
AG_SEQ = [[("tel", 1, 0)], [("git", 1, 1)], [("loc", 1, 2)], [("loc", -1, 3)],
          [("r1", 1, 4), ("r2", 1, 4)], [("r1", -1, 5), ("r2", -1, 5)], [("git", -1, 6)], [("tel", -1, 7)]]


def svg_agentes(x):
    o = [f'<svg class="ag" viewBox="0 0 360 300" role="img" aria-label="{escape(x["ag_aria"])}">']
    for eid, p, q in AG_EDGES:
        # la arista arranca y termina en el borde de cada caja (108 × 42), no en el centro
        (x1, y1), (x2, y2) = AG_POS[p], AG_POS[q]
        dx, dy = x2 - x1, y2 - y1
        k = min(57 / abs(dx) if dx else 9, 24 / abs(dy) if dy else 9)
        o.append(f'<path class="e" id="e-{eid}" d="M{x1 + dx * k:.1f} {y1 + dy * k:.1f}L{x2 - dx * k:.1f} {y2 - dy * k:.1f}"/>')
    for k, (cx, cy) in AG_POS.items():
        nom, sub = x["nodes"][k]
        o.append(f'<g class="nd" data-n="{k}"><rect x="{cx - 54}" y="{cy - 21}" width="108" height="42"/>'
                 f'<text x="{cx}" y="{cy + (-2 if sub else 4)}">{escape(nom)}</text>'
                 + (f'<text class="sub" x="{cx}" y="{cy + 13}">{escape(sub)}</text>' if sub else "") + '</g>')
    o.append('<g class="msgs"></g></svg>')
    return "".join(o)


def log_agentes(x):
    nodos = {k: v[0] for k, v in x["nodes"].items()}
    ends = {e: (p, q) for e, p, q in AG_EDGES}
    o = ['<ol class="log">']
    for i, paso in enumerate(AG_SEQ, 1):
        orig, dest = set(), []
        for e, s, m in paso:
            p, q = ends[e] if s == 1 else ends[e][::-1]
            orig.add(nodos[p])
            if nodos[q] not in dest:
                dest.append(nodos[q])
        o.append(f'<li><span class="y">{i:02d}</span> {", ".join(sorted(orig))} → {", ".join(dest)} · <b>{escape(x["msgs"][paso[0][2]])}</b></li>')
    o.append('</ol>')
    return "".join(o)


def page(lang):
    t, x = T[lang], X[lang]
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
      '<script>document.documentElement.className="js"</script>\n'
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
    a('<section class="hero wrap" aria-labelledby="h-nombre"><div class="hero-a">'
      f'<p class="kicker">{t["kicker"]}</p>'
      f'<h1 id="h-nombre">Franco Olmedo</h1>'
      f'<p class="lead">{t["lead"]}</p></div>')
    a(fig_ruteo(x, figno, t)); figno += 1
    a(f'<div class="hero-b"><p class="sub">{t["sub"]}</p>'
      '<div class="ctas">'
      f'<a class="btn btn-1" href="{wa}" rel="noopener">{t["cta_wa"]}</a>'
      f'<a class="btn btn-2" href="mailto:{MAIL}">{t["cta_mail"]}</a>'
      f'<a class="btn btn-3" href="{EA}" rel="noopener">{t["cta_ea"]} <span aria-hidden="true">→</span></a></div>'
      '<dl class="tblock">')
    for k, v in t["block"]:
        a(f'<div><dt>{k}</dt><dd>{v}</dd></div>')
    a('</dl></div></section>\n')
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
        if p.get("scope"):
            a(fig_osc(x, figno, t, lang)); figno += 1
        for nombre, cls, cap in p["figs"]:
            a(figure(nombre, cls, tx(cap, lang), figno, t, pre)); figno += 1
        a('</div></article>\n')
    a('</section>\n')
    # tableros: Ladder
    a(f'<section id="tableros" class="sec wrap" aria-labelledby="h-tab"><div class="sec-h"><p class="net" aria-hidden="true">02</p>'
      f'<h2 id="h-tab">{x["sec_tab"]}</h2><p class="sec-sub">{x["sec_tab_sub"]}</p></div><div class="duo">'
      f'<div class="duo-txt"><h3>{x["lad_h"]}</h3><p class="duo-p">{x["lad_p"]}</p><p class="duo-ev"><a href="#otros">{x["lad_ev"]}</a></p>'
      '<table class="io"><tbody>')
    for addr, nom in x["io"]:
        a(f'<tr><th scope="row" class="y">{addr}</th><td>{nom}</td><td class="v"><span data-io="{addr}">0</span></td></tr>')
    a(f'</tbody></table></div><figure class="live lad-fig" id="ladder" data-m="{escape(json.dumps(x["lad_m"], ensure_ascii=False))}">'
      f'{svg_ladder(x)}<div class="lad-ctl"><button type="button" class="pb on" data-b="S1">{x["b_on"]}</button>'
      f'<button type="button" class="pb off" data-b="S0">{x["b_off"]}</button></div>'
      f'<p class="lad-msg">{x["lad_m"][0]}</p>'
      f'<figcaption><span class="ref">{t["fig"]} {figno:02d}</span> {x["lad_try"]}</figcaption></figure></div></section>\n'); figno += 1
    # IA: Triana y agentes
    a(f'<section id="ia" class="sec wrap" aria-labelledby="h-ia"><div class="sec-h"><p class="net" aria-hidden="true">03</p>'
      f'<h2 id="h-ia">{x["sec_ia"]}</h2><p class="sec-sub">{x["sec_ia_sub"]}</p></div><div class="duo">'
      f'<div class="duo-txt"><h3>{x["tri_h"]}</h3><p class="duo-p">{x["tri_p"]}</p><ul class="bars">')
    for lab, k, n in x["bars"]:
        a(f'<li><span class="bl">{lab}</span><span class="bn"><b>{k}</b>/{n}</span>'
          f'<span class="bt" aria-hidden="true"><span style="width:{100 * k / n:.1f}%"></span></span></li>')
    a(f'</ul><h3 class="h-ag">{x["ag_h"]}</h3><p class="duo-p">{x["ag_p"]}</p></div>'
      f'<figure class="live ag-fig" id="agentes" data-seq="{escape(json.dumps(AG_SEQ))}">'
      f'{svg_agentes(x)}{log_agentes(x)}</figure></div></section>\n')
    # otros
    a(f'<section id="otros" class="sec wrap" aria-labelledby="h-otros"><div class="sec-h"><p class="net" aria-hidden="true">04</p>'
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
    a(f'<section id="experiencia" class="sec wrap" aria-labelledby="h-exp"><div class="sec-h"><p class="net" aria-hidden="true">05</p>'
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
    a(f'<section id="contacto" class="sec contact" aria-labelledby="h-ct"><div class="wrap"><div class="sec-h"><p class="net" aria-hidden="true">06</p>'
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
    a(f'<footer class="foot wrap"><p>Franco Olmedo · Villa Allende, Córdoba · Rev. {REV}</p><p>{t["foot"]}</p></footer>\n'
      f'<script src="{pre}assets/js/motor.js" defer></script>\n</body>\n</html>\n')
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

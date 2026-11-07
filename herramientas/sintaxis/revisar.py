# -*- coding: utf-8 -*-
"""Revisa la sintaxis de TODO el repo en un solo paso.

Por que existe (oct-2026): `jscheck.py` NO saca los <script> de los HTML, los
revisa tal cual. Si se le pasa un `.html`, cuenta tambien las llaves del CSS y
los `</script>`, y da "OK" por casualidad, no porque el JavaScript este bien.
Pasarle el HTML engano una vez: los archivos "pasaron" sin haberse revisado.

Este script hace las dos cosas en el orden correcto:
  1. `extract.py` deja los scripts sueltos en Temp/opencode/extracted
  2. `jscheck.py` revisa ESOS .js, que es lo que hay que revisar

Uso:  python revisar.py        (solo problemas y un resumen)
      python revisar.py -v     (detalle completo, como antes)
Sale con codigo 1 si algo fallo.
"""
import io, os, subprocess, sys, glob, re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = r"C:\Users\Fred\AppData\Local\Temp\opencode\extracted"
VERBOSO = "-v" in sys.argv[1:]


def correr_capturado(nombre, argumentos):
    """Corre un script del chequeo y devuelve (codigo, salida en bytes)."""
    r = subprocess.run([sys.executable, os.path.join(HERE, nombre)] + argumentos,
                       cwd=HERE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return r.returncode, r.stdout


def soltar(salida):
    """Imprime la salida tal cual la produjo el otro script (respeta acentos)."""
    sys.stdout.flush()
    sys.stdout.buffer.write(salida)
    sys.stdout.buffer.flush()


# Pantallas donde el Volver NO es fijo a proposito: su encabezado no se
# desplaza (solo la lista de mensajes). Si alguna cambia, se quita de aqui.
EXCEPCIONES_FIJO = {"Chat/index.html", "Acompanante/index.html"}


def sin_comentarios(src):
    """Quita comentarios HTML y de JavaScript: solo interesa el texto visible."""
    src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    return "\n".join(l for l in src.splitlines() if not l.strip().startswith("//"))


def revisar_modales():
    """Toda ventana emergente del HTML tiene que estar en General/Modales.md.

    ERROR: un `#modal...`/`#invOverlay...`/`#overlay...` o una etiqueta con
    class="modal" que no esté registrada. AVISO: un registro que ya no existe
    en el HTML (para limpiar la tabla).
    """
    errores = avisos = 0
    doc = os.path.join(REPO, "General", "Modales.md")
    try:
        reg_src = io.open(doc, encoding="utf-8").read()
    except Exception:
        print("MODAL    falta General/Modales.md")
        return 1, 0
    regs = set(re.findall(r"`#([A-Za-z0-9_-]+)`", reg_src))
    vistos = {}

    for p in sorted(glob.glob(os.path.join(REPO, "**", "*.html"), recursive=True)):
        rel = os.path.relpath(p, REPO).replace(os.sep, "/")
        try:
            src = io.open(p, encoding="utf-8-sig").read()
        except Exception:
            continue
        ids = set()
        for m in re.finditer(r'id="((?:modal|invOverlay|overlay)[A-Za-z0-9_-]*)"', src):
            ids.add(m.group(1))
        for tag in re.findall(r'<[^>]*class="[^"]*\bmodal\b[^"]*"[^>]*>', src):
            m = re.search(r'id="([A-Za-z0-9_-]+)"', tag)
            if m:
                ids.add(m.group(1))
            else:
                print("MODAL    %s: una ventana class=\"modal\" no tiene id" % rel)
                errores += 1
        for legado in ("lupa", "datos", "pantallaCfg"):
            if re.search(r'id="' + legado + r'"', src):
                ids.add(legado)
        for i in ids:
            vistos.setdefault(i, set()).add(rel)

    for i, files in sorted(vistos.items()):
        if i not in regs:
            print("MODAL    #%s no esta registrada en General/Modales.md (%s)"
                  % (i, ", ".join(sorted(files))))
            errores += 1
    for i in sorted(regs):
        if i not in vistos:
            print("REGISTRO #%s esta en Modales.md pero no aparece en el HTML" % i)
            avisos += 1
    if not errores and not avisos:
        print("OK: todas las ventanas del HTML registradas.")
    return errores, avisos


def revisar_navegacion():
    """Que una pantalla nueva no vuelva al patron viejo de navegacion.

    ERRORES (tumban la revision): glifo '← Volver' visible, o pushState sin
    popstate. AVISOS (solo recuerdan): pantalla con JavaScript sin registrar en
    extract.py, o un Volver de pantalla que no es position:fixed.
    """
    errores = avisos = 0
    try:
        ext = io.open(os.path.join(HERE, "extract.py"), encoding="utf-8").read()
        registrados = set(re.findall(r'\("([^"]+\.html)"', ext))
    except Exception:
        registrados = set()

    for p in sorted(glob.glob(os.path.join(REPO, "**", "*.html"), recursive=True)):
        rel = os.path.relpath(p, REPO).replace(os.sep, "/")
        try:
            src = io.open(p, encoding="utf-8-sig").read()
        except Exception:
            continue

        # 1) glifo viejo en texto visible
        if re.search(r"←\s*Volver(?!\s+a la app)", sin_comentarios(src)):
            print("GLIFO    %s: usa el glifo viejo de Volver (flecha larga)" % rel)
            errores += 1

        # 2) si guarda pasos del historial, tiene que escuchar popstate
        if "history.pushState" in src and "popstate" not in src:
            print("HIST     %s: usa pushState y no tiene popstate" % rel)
            errores += 1

        # 3) pantalla con JavaScript registrada en extract.py
        if "<script" in src and rel not in registrados:
            print("REGISTRO %s: tiene JavaScript y no esta en extract.py" % rel)
            avisos += 1

        # 4) el Volver de pantalla va fijo
        if rel in EXCEPCIONES_FIJO:
            continue
        for marca, patron in (
            ('class="back"', r"\.back\s*\{([^}]*)\}"),
            ('id="btnVolver"', r"#btnVolver\s*\{([^}]*)\}"),
            ('id="btnCasa"', r"#btnCasa\s*\{([^}]*)\}"),
        ):
            if marca not in src:
                continue
            reglas = re.findall(patron, src)
            inline = re.search(re.escape(marca) + r'[^>]*style="[^"]*position:fixed', src)
            if not inline and not any("position:fixed" in r for r in reglas):
                print("FIJO     %s: el Volver (%s) no es position:fixed" % (rel, marca))
                avisos += 1

    if not errores and not avisos:
        print("OK: Volver fijo y historial con popstate.")
    return errores, avisos


def revisar_documentacion():
    """Aviso de tamano de la documentacion. NO tumba la revision.

    La lectura obligatoria (AGENTS.md + GUIA.md) tiene un tope de 750 lineas
    juntas: es lo que se lee en cada sesion. Si se pasa, el relato se mueve a
    HISTORIA.md (ver AGENTS.md, *Presupuesto de documentacion*).

    Ademas informa, sin fallar, que documentos de detalle pasan de 350 lineas.
    """
    tope = 750

    def contar(rel):
        try:
            return len(io.open(os.path.join(REPO, rel), encoding="utf-8",
                               errors="replace").read().splitlines())
        except Exception:
            return 0

    a = contar("AGENTS.md")
    g = contar("General/GUIA.md")
    total = a + g
    print("AGENTS.md %d + GUIA.md %d = %d lineas (tope %d)"
          % (a, g, total, tope))

    avisos = 0
    if total > tope:
        print("AVISO    Documentacion: la lectura obligatoria pasa el tope por %d "
              "lineas. Mueve el relato a HISTORIA.md; no recortes reglas." % (total - tope))
        avisos += 1

    grandes = []
    for p in sorted(glob.glob(os.path.join(REPO, "General", "*.md"))):
        nombre = os.path.basename(p)
        if nombre in ("GUIA.md", "HISTORIA.md", "Indices-Codigo.md"):
            continue
        n = len(io.open(p, encoding="utf-8", errors="replace").read().splitlines())
        if n > 350:
            grandes.append((n, nombre))
    if grandes:
        print("Info: documentos de detalle grandes: " +
              ", ".join("%s (%d)" % (nm, n) for n, nm in sorted(grandes, reverse=True)))

    if not avisos:
        print("OK: la lectura obligatoria esta dentro del tope.")
    return avisos


# 1) extraer los scripts de los HTML
print("\n== extract.py ==")
cod_ext, out_ext = correr_capturado("extract.py", [])
if cod_ext != 0:
    soltar(out_ext)
    sys.exit(1)
if VERBOSO:
    soltar(out_ext)
# "FALTA" no tumba la revision, pero NUNCA se esconde: es una pantalla de la
# lista que ya no existe (o se movio) y hay que corregir extract.py.
for linea in out_ext.decode("utf-8", "replace").splitlines():
    if "FALTA" in linea:
        print(linea)

# Todo lo que extract.py dejo, en el orden en que lo genero.
archivos = []
for f in sorted(os.listdir(OUT)):
    if f.endswith(".js"):
        archivos.append(os.path.join(OUT, f))

if not archivos:
    print("No hay nada que revisar.")
    sys.exit(1)

# 2) llaves y parentesis: UNA sola corrida para todos los archivos.
print("\n== jscheck.py (%d archivos) ==" % len(archivos))
malos = 0
cod_js, out_js = correr_capturado("jscheck.py", archivos)
if cod_js != 0:
    soltar(out_js)
    malos += 1
elif VERBOSO:
    soltar(out_js)
else:
    print("OK: %d archivos, llaves y parentesis en orden." % len(archivos))

# 3) que no se use nada que no este importado
# (esto se col\u00f3 en oct-2026: `onSnapshot()` se usaba en favor.js sin
#  importarlo, y como estaba dentro de un try{} con catch vacio, fallaba en
#  silencio: no habia cartelito ni ventana y ningun error en pantalla.)
print("\n== nombres.py (%d archivos) ==" % len(archivos))
cod_nom, out_nom = correr_capturado("nombres.py", archivos)
if cod_nom != 0:
    soltar(out_nom)
    malos += 1
elif VERBOSO:
    soltar(out_nom)
else:
    print("OK: ningun nombre usado sin importar o definir.")

# 4) navegacion: que una pantalla nueva no vuelva al patron viejo.
print("\n== navegacion ==")
err_nav, avis_nav = revisar_navegacion()
if err_nav:
    malos += 1
if avis_nav:
    print("Avisos: %d (no detienen la revision)." % avis_nav)

# 5) modales: toda ventana del HTML tiene que estar registrada.
print("\n== modales ==")
err_mod, avis_mod = revisar_modales()
if err_mod:
    malos += 1
if avis_mod:
    print("Avisos: %d (no detienen la revision)." % avis_mod)

# 6) documentacion: aviso de tamano (no detiene la revision).
print("\n== documentacion ==")
avis_doc = revisar_documentacion()
if avis_doc:
    print("Avisos: %d (no detienen la revision)." % avis_doc)

if malos:
    print("\n%d revision(es) con problemas." % malos)
    sys.exit(1)
print("\nTodo bien: %d archivos." % len(archivos))
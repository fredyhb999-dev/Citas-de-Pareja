# -*- coding: utf-8 -*-
"""Revisa la sintaxis de TODO el repo en un solo paso.

Por que existe (oct-2026): `jscheck.py` NO saca los <script> de los HTML, los
revisa tal cual. Si se le pasa un `.html`, cuenta tambien las llaves del CSS y
los `</script>`, y da "OK" por casualidad, no porque el JavaScript este bien.
Pasarle el HTML engano una vez: los archivos "pasaron" sin haberse revisado.

Este script hace las dos cosas en el orden correcto:
  1. `extract.py` deja los scripts sueltos en Temp/opencode/extracted
  2. `jscheck.py` revisa ESOS .js, que es lo que hay que revisar

Uso:  python revisar.py
Sale con codigo 1 si algo fallo.
"""
import io, os, subprocess, sys, glob, re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = r"C:\Users\Fred\AppData\Local\Temp\opencode\extracted"


def correr(nombre, argumentos):
    print("\n== %s ==" % nombre)
    r = subprocess.run([sys.executable, os.path.join(HERE, nombre)] + argumentos,
                       cwd=HERE)
    return r.returncode


# Pantallas donde el Volver NO es fijo a proposito: su encabezado no se
# desplaza (solo la lista de mensajes). Si alguna cambia, se quita de aqui.
EXCEPCIONES_FIJO = {"Chat/index.html", "Acompanante/index.html"}


def sin_comentarios(src):
    """Quita comentarios HTML y de JavaScript: solo interesa el texto visible."""
    src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    return "\n".join(l for l in src.splitlines() if not l.strip().startswith("//"))


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


if correr("extract.py", []) != 0:
    sys.exit(1)

# Todo lo que extract.py dejo, en el orden en que lo genero.
archivos = []
for f in sorted(os.listdir(OUT)):
    if f.endswith(".js"):
        archivos.append(os.path.join(OUT, f))

if not archivos:
    print("No hay nada que revisar.")
    sys.exit(1)

# 1) llaves y parenteses
print("\n== jscheck.py (%d archivos) ==" % len(archivos))
malos = 0
for p in archivos:
    r = subprocess.run([sys.executable, os.path.join(HERE, "jscheck.py"), p])
    if r.returncode != 0:
        malos += 1

# 2) que no se use nada que no este importado
# (esto se col\u00f3 en oct-2026: `onSnapshot()` se usaba en favor.js sin
#  importarlo, y como estaba dentro de un try{} con catch vacio, fallaba en
#  silencio: no habia cartelito ni ventana y ningun error en pantalla.)
print("\n== nombres.py (%d archivos) ==" % len(archivos))
r = subprocess.run([sys.executable, os.path.join(HERE, "nombres.py")] + archivos)
if r.returncode != 0:
    malos += 1

# 3) navegacion: que una pantalla nueva no vuelva al patron viejo.
print("\n== navegacion ==")
err_nav, avis_nav = revisar_navegacion()
if err_nav:
    malos += 1
if avis_nav:
    print("Avisos: %d (no detienen la revision)." % avis_nav)

if malos:
    print("\n%d revision(es) con problemas." % malos)
    sys.exit(1)
print("\nTodo bien: %d archivos." % len(archivos))
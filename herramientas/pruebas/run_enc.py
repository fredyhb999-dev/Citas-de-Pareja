import re, io, os, subprocess, sys, time, socket, glob, shutil

H = r"C:\Users\Fred\AppData\Local\Temp\opencode\harness"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PERFIL = r"C:\Users\Fred\AppData\Local\Temp\opencode\perfil_enc"
DUMP = r"C:\Users\Fred\AppData\Local\Temp\opencode\dump_enc.html"

if not os.path.exists(CHROME):
    print("NO HAY CHROME en", CHROME); sys.exit(1)


def puerto():
    s = socket.socket(); s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]; s.close(); return p


# El listado raiz tiene que ser el de ESTE arnes: si el puerto cayera en un
# http.server vivo de otra carpeta, la prueba miraria la pagina equivocada y
# daria 404 sin quejarse.
DEBE_TENER = ("Encuentros",)
NO_DEBE_TENER = ()


RUTA_PROPIO = "/Encuentros/index.html"
MINIMO = 30000


def servir():
    """Levanta el servidor y se ASEGURA de que sea el suyo.

    Varias corridas dejan http.server vivos de otras carpetas; si el puerto
    cayera en uno de esos, la prueba miraria la pagina equivocada y daria 404
    sin avisar. Por eso se comprueba una ruta que solo existe aqui."""
    import urllib.request
    for _ in range(8):
        p = puerto()
        pr = subprocess.Popen([sys.executable, "-m", "http.server", str(p), "--bind", "127.0.0.1"],
                              cwd=H, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1.3)
        try:
            cuerpo = urllib.request.urlopen("http://127.0.0.1:%d%s" % (p, RUTA_PROPIO), timeout=5).read()
            if len(cuerpo) >= MINIMO:
                return p, pr
        except Exception:
            pass
        try: pr.terminate()
        except Exception: pass
    raise SystemExit("no se pudo levantar un servidor propio en " + H)

def correr(url, budget=30000):
    if os.path.exists(DUMP):
        os.remove(DUMP)
    if os.path.isdir(PERFIL):
        shutil.rmtree(PERFIL, ignore_errors=True)   # perfil limpio: cada corrida es reproducible
    os.makedirs(PERFIL, exist_ok=True)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--user-data-dir=" + PERFIL, "--virtual-time-budget=%d" % budget,
                    "--window-size=900,900", "--dump-dom", url],
                   stdout=open(DUMP, "w", encoding="utf-8"), stderr=subprocess.DEVNULL, timeout=180)


def salida():
    t = open(DUMP, encoding="utf-8", errors="replace").read()
    m = re.search(r'<div id="SALIDA"[^>]*>(.*?)</div>', t, re.S)
    if not m:
        return "(sin bloque SALIDA; la pagina no llego a render)"
    import html
    return html.unescape(m.group(1))


esc = sys.argv[1] if len(sys.argv) > 1 else "host"
extra = sys.argv[2] if len(sys.argv) > 2 else ""
p, pr = servir()
try:
    url = "http://127.0.0.1:%d/Encuentros/index.html?esc=%s%s" % (p, esc, extra)
    correr(url, 40000)
    # Se escribe a archivo: la consola de Windows no aguanta los caracteres
    # (flechas, acentos) que suelta la pagina.
    io.open(os.path.join(os.path.dirname(DUMP), "ultima_salida.txt"), "w", encoding="utf-8").write(salida())
finally:
    pr.terminate()
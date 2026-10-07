import re, os, subprocess, sys, time, socket, shutil, io, html

H = r"C:\Users\Fred\AppData\Local\Temp\opencode\harnes_raiz"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PERFIL = r"C:\Users\Fred\AppData\Local\Temp\opencode\perfil_raiz"
DUMP = r"C:\Users\Fred\AppData\Local\Temp\opencode\dump_raiz.html"

def puerto():
    s = socket.socket(); s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]; s.close(); return p


# El listado raiz tiene que ser el de ESTE arnes (tiene invitado.js y NO
# tiene ni Encuentros ni Diablitos): si el puerto cayera en un http.server vivo
# de otra carpeta, la prueba miraria la pagina equivocada y daria 404 en silencio.
DEBE_TENER = ("invitado.js",)
NO_DEBE_TENER = ("Encuentros", "Diablitos")


RUTA_PROPIO = "/index.html"
MINIMO = 40000


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
    if os.path.exists(DUMP): os.remove(DUMP)
    if os.path.isdir(PERFIL): shutil.rmtree(PERFIL, ignore_errors=True)
    os.makedirs(PERFIL, exist_ok=True)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--user-data-dir=" + PERFIL, "--virtual-time-budget=%d" % budget,
                    "--window-size=900,900", "--dump-dom", url],
                   stdout=open(DUMP, "w", encoding="utf-8"), stderr=subprocess.DEVNULL, timeout=180)

def salida():
    t = open(DUMP, encoding="utf-8", errors="replace").read()
    m = re.search(r'<div id="SALIDA"[^>]*>(.*?)</div>', t, re.S)
    return html.unescape(m.group(1)) if m else "(sin bloque SALIDA)"

esc = sys.argv[1] if len(sys.argv) > 1 else "nada"
p, pr = servir()
try:
    correr("http://127.0.0.1:%d/index.html?esc=%s" % (p, esc), 30000)
    io.open(r"C:\Users\Fred\AppData\Local\Temp\opencode\salida_raiz.txt", "w", encoding="utf-8").write(salida())
    print("ok")
finally:
    pr.terminate()
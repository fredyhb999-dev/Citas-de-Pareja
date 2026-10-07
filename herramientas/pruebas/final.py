import io, os, subprocess, sys

BASE = r"C:\Users\Fred\AppData\Local\Temp\opencode"
H = os.path.join(BASE, "harness")

CASOS = [
    ("niveles", ""),
    ("invitacion", ""),
    ("entrar", "&como=u3&entrar=1"),
    ("host", ""),
    ("host2", ""),
    ("invitado", "&respaldo=1"),
    ("invitado", "&como=u2&flag=natural"),
    ("invitado", "&flag=pausa&respaldo=1"),
    ("invitado", "&flag=fin&respaldo=1"),
    ("fantasma", ""),
    ("multi", ""),
    ("terminada", ""),
    ("sinsuc", "&sinLic=1"),
]

print("construyendo arnes...", flush=True)
subprocess.run([sys.executable, "build_harness.py"], cwd=BASE, stdout=subprocess.DEVNULL, check=True)
subprocess.run([sys.executable, "inject_driver.py"], cwd=BASE, stdout=subprocess.DEVNULL, check=True)

salidas = []
errores = 0
for i, (esc, extra) in enumerate(CASOS):
    dest = os.path.join(BASE, "final_%02d.txt" % i)
    subprocess.run([sys.executable, "run_enc.py", esc, extra], cwd=BASE, stdout=subprocess.DEVNULL, check=True)
    subprocess.run([sys.executable, "extract_out.py", dest], cwd=BASE, stdout=subprocess.DEVNULL, check=True)
    t = io.open(dest, encoding="utf-8").read()
    tag = "[%s%s]" % (esc, extra)
    salidas.append("#" * 20 + " %s" % tag)
    for ln in t.splitlines():
        s = ln.strip()
        if (s.startswith("-") or s.startswith("==") or s.startswith("localStorage")
                or s.startswith("appPareja") or s.startswith("pareja_usuarios")
                or s.startswith("licencias") or s.startswith("invitado_respaldo")
                or s.startswith("inventado_") or s.startswith("taquilla_priv")
                or s.startswith("config/ajustes") or s.startswith("Firestore")):
            salidas.append(ln[:170])
    if "errores js: ninguno" not in t:
        salidas.append("  >>> HAY ERRORES JS EN ESTE CASO")
        errores += 1
    if "TIMEOUT" in t:
        salidas.append("  >>> HUBO TIMEOUTS EN ESTE CASO")
        errores += 1
    # Un driver que se cae = el caso NO se probó. Antes esto pasaba
    # desapercibido y el reporte salía "0 problemas" con la prueba sin correr.
    if "FALLO DEL DRIVER" in t:
        salidas.append("  >>> EL DRIVER SE CAYO: este caso no se.probó de verdad")
        errores += 1
    salidas.append("")
    print("  caso %d/%d %s ok" % (i + 1, len(CASOS), tag), flush=True)

io.open(os.path.join(BASE, "FINAL.txt"), "w", encoding="utf-8").write("\n".join(salidas))
print("\ncasos con problemas:", errores)
print("reporte -> FINAL.txt")
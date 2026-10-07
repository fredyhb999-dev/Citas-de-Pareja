import os
import io, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
H = r"C:\Users\Fred\AppData\Local\Temp\opencode\harness"

def rd(p):
    return io.open(p, encoding="utf-8-sig").read()

def wr(p, s):
    d = os.path.dirname(p)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)

for sub in ("Encuentros", "Citas"):
    d = os.path.join(H, sub)
    if os.path.isdir(d):
        shutil.rmtree(d)

# invitado.js (modo invitado + invitaciones) con los imports al mock
inv = rd(os.path.join(REPO, "invitado.js"))
inv = inv.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-app.js"', '"./mock/firebase-app.js"')
inv = inv.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-firestore.js"', '"./mock/firebase-firestore.js"')
wr(os.path.join(H, "invitado.js"), inv)

# archivos compartidos tal cual
for f in ("config.js", "firebase-config.js"):
    shutil.copyfile(os.path.join(REPO, f), os.path.join(H, f))

# acceso.js y encounters: parchear imports de firebase a los mocks
ac = rd(os.path.join(REPO, "acceso.js"))
ac = ac.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-app.js"', '"./mock/firebase-app.js"')
ac = ac.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-firestore.js"', '"./mock/firebase-firestore.js"')
ac = ac.replace('from "./taquilla.js"', 'from "./mock/taquilla.js"')
wr(os.path.join(H, "acceso.js"), ac)

# Arnés: si la app navega de verdad (por ejemplo al salir a la sala), la
# pagina se va y no se podria observar nada. Se intercepta la navegacion.
en = rd(os.path.join(REPO, "Encuentros", "index.html"))
en = en.replace('location.replace("../Diablitos/");', 'window.__destino = "../Diablitos/";')
en = en.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-app.js"', '"../mock/firebase-app.js"')
en = en.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-firestore.js"', '"../mock/firebase-firestore.js"')
en = en.replace('from "../taquilla.js"', 'from "../mock/taquilla.js"')
# sonda de errores antes del cierre de body
Sonda = """
<div id="DIAG" style="position:fixed;left:0;top:0;right:0;z-index:9999;background:#000;color:#0f0;font:11px monospace;padding:6px;white-space:pre-wrap;max-height:60vh;overflow:auto"></div>
<script>
window.__errores = [];
window.onerror = function(m, s, l, c, e){ window.__errores.push("onerror: " + m + " @linea " + l); };
window.addEventListener("unhandledrejection", function(ev){
  window.__errores.push("promesa: " + (ev.reason && ev.reason.message ? ev.reason.message : String(ev.reason)));
});
function __pinta(){
  document.getElementById("DIAG").textContent =
    "ERRORES: " + (window.__errores.length ? window.__errores.join(" || ") : "ninguno") +
    "\\nSALIDA: " + (window.__salida || []).map(function(x){ return "- " + x; }).join("\\n        ");
}
function __log(s){ window.__salida = window.__salida || []; window.__salida.push(s); __pinta(); }
function __ver(id){
  const e = document.getElementById(id);
  if(!e) return "no existe #" + id;
  const cs = getComputedStyle(e);
  return (cs.display === "none" || cs.visibility === "hidden" || cs.opacity === "0") ? "OCULTO" : "visible";
}
function __abrir(id){ document.getElementById(id).style.display = "flex"; }
</script>
"""
en = en.replace("</body>", Sonda + "\n</body>")
wr(os.path.join(H, "Encuentros", "index.html"), en)

# actividades.json minimo
wr(os.path.join(H, "Citas", "actividades.json"),
   io.open(os.path.join(REPO, "Citas", "actividades.json"), encoding="utf-8-sig").read())

print("harness construido en", H)
for root, dirs, files in os.walk(H):
    if "mock" in root or "\\Encuentros" in root or root.endswith("harness"):
        for f in files:
            p = os.path.join(root, f)
            print("  %-46s %d" % (p.replace(H + "\\", ""), os.path.getsize(p)))
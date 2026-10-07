import os
import io, os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
H = r"C:\Users\Fred\AppData\Local\Temp\opencode\harnes_raiz"

if os.path.isdir(H):
    shutil.rmtree(H)
os.makedirs(os.path.join(H, "mock"))
os.makedirs(os.path.join(H, "Citas"))

def rd(p): return io.open(p, encoding="utf-8-sig").read()
def wr(p, s):
    d = os.path.dirname(p)
    if d and not os.path.isdir(d): os.makedirs(d)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)

# mocks de firebase (los mismos del arnés de encuentros)
# firebase: se copian del arnés de encuentros. taquilla NO: el del inicio es
# aparte, porque ahi el codigo dice de quien es y eso hay que poder probar.
for f in ("firebase-app.js", "firebase-firestore.js"):
    shutil.copyfile(os.path.join(r"C:\Users\Fred\AppData\Local\Temp\opencode\harness\mock", f),
                    os.path.join(H, "mock", f))

# El mock de firebase trae una siembra de escenario que es del arnés de
# Encuentros. Aquí estorba: pone usuarios que no son los de este arnés y la
# app nunca llega al menú. Se neutraliza DESPUÉS de copiarlo.
_m = io.open(os.path.join(H, "mock", "firebase-firestore.js"), encoding="utf-8").read()
_m = _m.replace("(function sembrarEscenario(){", "(function sembrarEscenario(){ if(1) return;", 1)
io.open(os.path.join(H, "mock", "firebase-firestore.js"), "w", encoding="utf-8", newline="\n").write(_m)

# Taquilla del inicio: aqui el codigo SI dice de quien es
# ("ITEM|PROJECT|EMAIL"), para poder comprobar que un invitado no se
# queda con los codigos del anfitrion.
wr(os.path.join(H, "mock", "taquilla.js"), r"""// Mock de taquilla para el arnes del INICIO.
export const TAQUILLA_FIREBASE = {
  apiKey: "mock", authDomain: "mock", projectId: "taquilla-juegos",
  storageBucket: "mock", messagingSenderId: "1", appId: "1:1:web:mock"
};
export const TAQUILLA_PUBLICA = { kty: "EC", crv: "P-256", x: "x", y: "y", ext: true };
function deCodigo(codigo){
  const c = String(codigo || "").trim();
  if(!c) return null;
  const p = c.split("|");
  if(p.length < 3) return null;
  return { item: p[0], para: p[1], email: p[2].toLowerCase(), vence: null };
}
export async function verificarCodigo(codigo){ return deCodigo(codigo); }
export async function verificarFirma(codigo){ return deCodigo(codigo); }
export async function firmarAcceso(){ return "mock|mock|mock"; }
""")

# Solicitudes en la taquilla: una APROBADA del proyecto "host" (el anfitrion).
# Es lo que un invitado se llevaria en el celular sin la proteccion.
_m = io.open(os.path.join(H, "mock", "firebase-firestore.js"), encoding="utf-8").read()
_m += r"""
(function sembrarSolicitudesDelHost(){
  if(typeof location === "undefined") return;
  if(!location.search) return;
  const taq = dbs["taquilla"] || (dbs["taquilla"] = { docs:new Map(), listeners:new Map(), log:[] });
  taq.docs.set("solicitudes/s-host", {
    para: "host", item: "encuentros", email: "host@ejemplo.mx",
    estado: "aprobado", codigo: "encuentros|host|host@ejemplo.mx",
    fecha: { __ts: 2 }, graciaUsada: true
  });
})();
"""
io.open(os.path.join(H, "mock", "firebase-firestore.js"), "w", encoding="utf-8", newline="\n").write(_m)

# Invitado que YA esta registrado: al abrir la app apunta a la base del
# anfitrion. Si hay partida activa NO se le expulsa, y ahi es donde el
# catalogo se lee con el proyecto del anfitrion.
_m = io.open(os.path.join(H, "mock", "firebase-firestore.js"), encoding="utf-8").read()
_m += r"""
(function sembrarInvitadoRegistrado(){
  if(typeof location === "undefined") return;
  if(!/\besc=visitando\b/.test(location.search)) return;
  const d = dbs["[DEFAULT]"] || (dbs["[DEFAULT]"] = { docs:new Map(), listeners:new Map(), log:[] });
  d.docs.set("config/ajustes", { usuarios: [
    { id: "m1", nombre: "Anfitrion", admin: true },
    { id: "u1", nombre: "Tio Beto", admin: false, invitado: true, conQuien: "m1" }
  ]});
  d.docs.set("sesionEncuentros/actual", {
    activa: true, terminada: false, largo: 2, ronda: 0, turno: 0,
    orden: ["u1","m1"],_heads_dummy: 0,
    cabezas: [ { id: "m1", nombre: "Anfitrion", lado: "A", admin: true },
               { id: "u1", nombre: "Tio Beto", lado: "A", admin: false, invitado: true } ],
    listas: { m1: [], u1: [] }
  });
})();
"""
io.open(os.path.join(H, "mock", "firebase-firestore.js"), "w", encoding="utf-8", newline="\n").write(_m)

for f in ("config.js", "firebase-config.js"):
    shutil.copyfile(os.path.join(REPO, f), os.path.join(H, f))

# acceso.js e invitado.js con los imports de firebase apuntando a los mocks
ac = rd(os.path.join(REPO, "acceso.js"))
ac = ac.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-app.js"', '"./mock/firebase-app.js"')
ac = ac.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-firestore.js"', '"./mock/firebase-firestore.js"')
ac = ac.replace('from "./taquilla.js"', 'from "./mock/taquilla.js"')
wr(os.path.join(H, "acceso.js"), ac)

inv = rd(os.path.join(REPO, "invitado.js"))
inv = inv.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-app.js"', '"./mock/firebase-app.js"')
inv = inv.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-firestore.js"', '"./mock/firebase-firestore.js"')
wr(os.path.join(H, "invitado.js"), inv)

# index.html: quitar los CDN de camara/QR y apuntar firebase a los mocks
ix = rd(os.path.join(REPO, "index.html"))
ix = ix.replace('<script src="https://unpkg.com/html5-qrcode@2.3.8/html5-qrcode.min.js"></script>', "")
ix = ix.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>', "")
ix = ix.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-app.js"', '"./mock/firebase-app.js"')
ix = ix.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-firestore.js"', '"./mock/firebase-firestore.js"')
ix = ix.replace('from "./taquilla.js"', 'from "./mock/taquilla.js"')
# Solo para el arnés: location.reload() deja la pagina a medio cargar y Chrome
# headless nunca termina. Se sustituye por una marca para poder observar el
# estado ya restaurado. Esto NO toca el repo.
ix = ix.replace("location.reload();", "window.__sinRecarga = true;")
ix = ix.replace('location.replace("Diablitos/");', "window.__destino = 'Diablitos/';")
ix = ix.replace('location.href = "Diablitos/";', "window.__destino = 'Diablitos/';")

SEMILLA = r"""
<script>
// Arnés: cámara/QR falsos para poder probar el escaneo sin cámara.
window.__qrListo = null;
window.Html5Qrcode = function(){};
window.Html5Qrcode.prototype.start = function(cam, cfg, onOk, onErr){
  window.__qrListo = onOk;
  return Promise.resolve();
};
window.Html5Qrcode.prototype.stop = function(){ return Promise.resolve(); };
window.Html5Qrcode.prototype.clear = function(){ return Promise.resolve(); };
window.QRCode = function(el, o){ el.style.display = "none"; };

// Escenarios:
//   ?esc=nada            -> no ha tocado nada
//   ?esc=copia           -> escaneo pero NO se registro (respaldo sin identidad)
//   ?esc=visita          -> ya es invitado de verdad
//   ?esc=medio           -> mismo caso que copia pero la config ya es del anfitrion
(function sembrar(){
  var q = new URLSearchParams(location.search);
  var esc = q.get("esc") || "nada";
  var fbMia = { apiKey: "mia", authDomain: "mia.firebaseapp.com", projectId: "mia",
                storageBucket: "mia.firebasestorage.app", messagingSenderId: "1", appId: "1:1:web:mia" };
  var fbHost = { apiKey: "host", authDomain: "host.firebaseapp.com", projectId: "host",
                 storageBucket: "host.firebasestorage.app", messagingSenderId: "1", appId: "1:1:web:host" };
  var misUsuarios = [{ id: "m1", nombre: "Mi Base", admin: true },
                     { id: "m2", nombre: "Mi Pareja", admin: false }];
  localStorage.setItem("pareja_usuarios", JSON.stringify(misUsuarios));
  localStorage.setItem("pareja_config", JSON.stringify({ firebase: fbMia }));
  localStorage.setItem("appPareja_quienSoy", JSON.stringify(misUsuarios[0]));
  localStorage.setItem("licencias", JSON.stringify({ guided: "COD-MIO" }));
  localStorage.setItem("dato_mio", "NO-DEBE-QUEDAR");
  localStorage.setItem("taquilla_priv", "LLAVE-DEL-DEV");

  if(esc === "visitando"){
    // Ya soy invitado: config del anfitrion + respaldo + identidad de invitado.
    var snap2 = { pareja_config: JSON.stringify({ firebase: fbMia }),
                  pareja_usuarios: JSON.stringify(misUsuarios),
                  appPareja_quienSoy: JSON.stringify(misUsuarios[0]),
                  licencias: JSON.stringify({ guided: "COD-MIO" }),
                  dato_mio: "NO-DEBE-QUEDAR" };
    localStorage.setItem("invitado_respaldo", JSON.stringify(snap2));
    localStorage.setItem("pareja_config", JSON.stringify({ firebase: fbHost }));
    localStorage.setItem("appPareja_quienSoy", JSON.stringify(
      { id: "u1", nombre: "Tio Beto", admin: false, invitado: true, conQuien: "m1" }));
  }
  if(esc === "copia" || esc === "medio"){
    var snap = { pareja_config: JSON.stringify({ firebase: fbMia }),
                 pareja_usuarios: JSON.stringify(misUsuarios),
                 appPareja_quienSoy: JSON.stringify(misUsuarios[0]),
                 licencias: JSON.stringify({ guided: "COD-MIO" }),
                 dato_mio: "NO-DEBE-QUEDAR" };
    localStorage.setItem("invitado_respaldo", JSON.stringify(snap));
    localStorage.setItem("pareja_config", JSON.stringify({ firebase: fbHost }));
    localStorage.setItem("dato_del_anfitrion", "NO-DEBE-QUEDAR");
    if(esc === "visita"){
      localStorage.setItem("appPareja_quienSoy", JSON.stringify(
        { id: "u2", nombre: "Invitado", admin: false, invitado: true, conQuien: "m1" }));
    }
  }
  window.__fbMia = fbMia; window.__fbHost = fbHost;
  window.__misUsuarios = misUsuarios;
})();
</script>
</head>"""

ix = ix.replace("</head>", SEMILLA, 1)
wr(os.path.join(H, "index.html"), ix)

wr(os.path.join(H, "Citas", "usuarios.json"), "[]")
wr(os.path.join(H, "Citas", "actividades.json"), '["Prueba"]')

print("arnes del inicio construido en", H)
for root, dirs, files in os.walk(H):
    for f in files:
        p = os.path.join(root, f)
        print("  %-42s %d" % (p.replace(H + "\\", ""), os.path.getsize(p)))
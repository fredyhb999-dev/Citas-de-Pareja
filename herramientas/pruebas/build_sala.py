import os
import io, os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC = r"C:\Users\Fred\AppData\Local\Temp\opencode\harnes_raiz"   # mocks ya listos
H = r"C:\Users\Fred\AppData\Local\Temp\opencode\harnes_sala"

if os.path.isdir(H):
    shutil.rmtree(H)
os.makedirs(os.path.join(H, "mock"))
os.makedirs(os.path.join(H, "Diablitos", "img"))

def rd(p): return io.open(p, encoding="utf-8-sig").read()
def wr(p, s):
    d = os.path.dirname(p)
    if d and not os.path.isdir(d): os.makedirs(d)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)

# mocks + compartidos (vienen del arnés del inicio)
for f in ("firebase-app.js", "firebase-firestore.js", "taquilla.js"):
    shutil.copyfile(os.path.join(SRC, "mock", f), os.path.join(H, "mock", f))
for f in ("config.js", "firebase-config.js", "acceso.js"):
    shutil.copyfile(os.path.join(SRC, f), os.path.join(H, f))

inv = rd(os.path.join(REPO, "invitado.js"))
inv = inv.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-app.js"', '"./mock/firebase-app.js"')
inv = inv.replace('"https://www.gstatic.com/firebasejs/10.13.1/firebase-firestore.js"', '"./mock/firebase-firestore.js"')
wr(os.path.join(H, "invitado.js"), inv)

# Diablitos: sin firebase propio (usa ../invitado.js) y sin navegar de verdad
di = rd(os.path.join(REPO, "Diablitos", "index.html"))
di = di.replace("""</script>

<!-- ============ SALA DE ESPERA""", """</script>

<!-- ============ SALA DE ESPERA""")
# interceptar la navegacion de expulsion (solo en el arnes)
di = di.replace('location.replace("../");', 'window.__expulsado = true;')
di = di.replace('location.href = "../" + destino + "/?entrar=1";', 'window.__entrarEn = destino + "?entrar=1";')
di = di.replace('location.href = "../";', 'window.__volvioAlInicio = true;')
wr(os.path.join(H, "Diablitos", "index.html"), di)

# imagenes del juego (para que no tarde probando 60)
for n in os.listdir(os.path.join(REPO, "Diablitos", "img")):
    if n.lower().endswith((".png", ".webp", ".jpg", ".svg", ".gif")):
        shutil.copyfile(os.path.join(REPO, "Diablitos", "img", n), os.path.join(H, "Diablitos", "img", n))

# escenario: el invitado ya esta registrado en la base del anfitrion
di = io.open(os.path.join(H, "Diablitos", "index.html"), encoding="utf-8").read()
SEMILLA = r"""
<script>
// Arnés: simula al invitado ya registrado, con la base del anfitrión.
(function sembrar(){
  var q = new URLSearchParams(location.search);
  var esc = q.get("esc") || "nada";
  var fbMia = { apiKey:"mia", authDomain:"mia.firebaseapp.com", projectId:"mia",
                storageBucket:"mia.firebasestorage.app", messagingSenderId:"1", appId:"1:1:web:mia" };
  var fbHost = { apiKey:"host", authDomain:"host.firebaseapp.com", projectId:"host",
                 storageBucket:"host.firebasestorage.app", messagingSenderId:"1", appId:"1:1:web:host" };
  var misUsuarios = [{ id:"m1", nombre:"Mi Base", admin:true }];
  localStorage.setItem("pareja_usuarios", JSON.stringify(misUsuarios));
  localStorage.setItem("pareja_config", JSON.stringify({ firebase: fbMia }));
  localStorage.setItem("appPareja_quienSoy", JSON.stringify(misUsuarios[0]));
  localStorage.setItem("dato_mio", "MIO");
  localStorage.setItem("taquilla_priv", "LLAVE-DEV");
  if(esc !== "nada"){
    localStorage.setItem("invitado_respaldo", JSON.stringify({
      pareja_config: JSON.stringify({ firebase: fbMia }),
      pareja_usuarios: JSON.stringify(misUsuarios),
      appPareja_quienSoy: JSON.stringify(misUsuarios[0]),
      dato_mio: "MIO"
    }));
    localStorage.setItem("pareja_config", JSON.stringify({ firebase: fbHost }));
    localStorage.setItem("appPareja_quienSoy", JSON.stringify(
      { id:"u1", nombre:"Tio Beto", admin:false, invitado:true, conQuien:"m1" }));
  }
  window.__esc = esc;
})();
</script>
</head>"""
di = di.replace("</head>", SEMILLA, 1)
io.open(os.path.join(H, "Diablitos", "index.html"), "w", encoding="utf-8", newline="\n").write(di)

print("arnes de la sala construido en", H)
# -*- coding: utf-8 -*-
"""Pruebas del INSTALADOR DE FABRICA (oct-2026).

Que pasa y por que existen estas pruebas: el arnes de siempre (final.py,
run_raiz.py, run_sala.py) usa un Firestore de mentira que NO escribe, asi que
no puede comprobar el instalador, que justamente escribe en la base.

Aqui se prueban DOS cosas, sin tocar nunca Firebase de verdad:

  1. CASOS SUELTOS (22): la logica de config.js -- sembrar una sola vez,
     que lo borrado no vuelva, que respete lo tuyo, que no se rompa sin
     permiso.
  2. PANTALLAS REALES: se copian tal cual las 5 pantallas que arman la lista
     de actividades (con su DOM de verdad) y se les apunta a una base falsa
     en memoria. Se mide lo que el usuario veria.

Uso:  python correr.py

Nada de esto sube nada a internet ni toca tu Firebase.
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
import html as htmlmod
import io, json, os, re, shutil, socket, subprocess, sys, time, urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
# instalador/ esta en herramientas/pruebas/instalador -> el repo esta 3 niveles arriba
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
TRABAJO = os.path.join(AQUI, "trabajo")
PAN = os.path.join(AQUI, "pantallas")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CDN = 'https://www.gstatic.com/firebasejs/10.13.1/'
# donde va cada import de cada pagina
DESTINOS = [
    (CDN + 'firebase-app.js', '../stub/firebase-pantallas.js'),
    (CDN + 'firebase-firestore.js', '../stub/firebase-pantallas.js'),
    (CDN + 'firebase-auth.js', '../stub/firebase-pantallas.js'),
    ('../firebase-config.js', '../stub/config.js'),
    ('../taquilla.js', '../stub/comunes.js'),
    ('../acceso.js', '../stub/comunes.js'),
    ('../invitado.js', '../stub/comunes.js'),
    ('../config.js', '../config_fabrica.js'),
    ('../Citas/actividades.json', 'actividades.json'),
    ('../Citas/accesorios.json', 'accesorios.json'),
]

ACT1, ACT2, ACT3 = "Cena Romántica", "Baile Bajo las Estrellas", "Paseo a la Luz de la Luna"
ACC1, ACC2, ACC3 = "Pétalos de Rosa", "Música Romántica", "Nota de Amor"


# =====================================================================
#  1) la copia de trabajo de config.js
# =====================================================================
def preparar_config():
    """Copia el config.js REAL del repo y le cambia el import del SDK por el stub.

    Se hace en cada corrida a proposito: asi las pruebas siempre usan el
    config.js que hay ahora en el repo, no una copia vieja."""
    origen = os.path.join(RAIZ, "config.js")
    destino = os.path.join(AQUI, "config_fabrica.js")
    txt = io.open(origen, encoding="utf-8").read()
    marca = CDN + "firebase-firestore.js"
    if marca not in txt:
        raise SystemExit("config.js ya no importa del CDN; revisa el stub")
    io.open(destino, "w", encoding="utf-8").write(txt.replace(marca, "./stub/firebase.js"))
    return destino


# =====================================================================
#  2) la base falsa en memoria
# =====================================================================
BANCO = r"""
window.__errores = [];
window.addEventListener("error", e => window.__errores.push(String(e.message)));
const st = { cols: { actividadesExtra: [], accesoriosExtra: [] }, docs: {} };
window.__api = {
  doc: (db, ...p) => ({ path: p.join("/") }),
  collection: (db, n) => ({ name: n }),
  getDoc: async ref => ({ exists: () => st.docs[ref.path] !== undefined, data: () => st.docs[ref.path] }),
  setDoc: async (ref, d) => { if(window.__romper) throw new Error("sin permiso"); st.docs[ref.path] = d; },
  getDocs: async col => ({
    forEach(cb){ (st.cols[col.name] || []).forEach((d, i) => cb({ id: String(i), data: () => d })); },
    docs: [], size: (st.cols[col.name] || []).length
  }),
  addDoc: async (col, d) => {
    if(window.__romper) throw new Error("sin permiso");
    (st.cols[col.name] = st.cols[col.name] || []).push(d);
  },
  serverTimestamp: () => "AHORA",
  deleteDoc: async ref => {
    const p = ref.path.split("/");
    const col = st.cols[p[0]] || [];
    const i = col.findIndex(x => x.id === p[1]);
    if(i >= 0) col.splice(i, 1);
  },
  onSnapshot: () => () => {},
  updateDoc: async ref => {},
  runTransaction: () => async fn => fn(),
  ver(){
    return {
      actividades: (st.cols.actividadesExtra || []).map(x => x.nombre),
      accesorios: (st.cols.accesoriosExtra || []).map(x => x.nombre),
      banderita: !!st.docs["config/fabrica"]
    };
  }
};
"""

# los 5 escenarios que se prueban en las pantallas
ESCENARIOS = {
    "recien": ("false", """
      st.cols.actividadesExtra = []; st.cols.accesoriosExtra = []; st.docs = {};
    """, ACT1),
    "instalado": ("false", """
      st.cols.actividadesExtra = [
        {id:"a1", nombre:"Cena Romántica", origen:"fabrica"},
        {id:"a2", nombre:"Baile Bajo las Estrellas", origen:"fabrica"},
        {id:"a3", nombre:"Paseo a la Luz de la Luna", origen:"fabrica"}
      ];
      st.cols.accesoriosExtra = [
        {id:"b1", nombre:"Pétalos de Rosa", origen:"fabrica"},
        {id:"b2", nombre:"Música Romántica", origen:"fabrica"},
        {id:"b3", nombre:"Nota de Amor", origen:"fabrica"}
      ];
      st.docs["config/fabrica"] = {version:1,
        actividades:["cena romántica","baile bajo las estrellas","paseo a la luz de la luna"],
        accesorios:["pétalos de rosa","música romántica","nota de amor"]};
    """, ACT1),
    "borrada": ("false", """
      st.cols.actividadesExtra = [
        {id:"a2", nombre:"Baile Bajo las Estrellas", origen:"fabrica"},
        {id:"a3", nombre:"Paseo a la Luz de la Luna", origen:"fabrica"}
      ];
      st.cols.accesoriosExtra = [
        {id:"b1", nombre:"Pétalos de Rosa", origen:"fabrica"},
        {id:"b2", nombre:"Música Romántica", origen:"fabrica"},
        {id:"b3", nombre:"Nota de Amor", origen:"fabrica"}
      ];
      st.docs["config/fabrica"] = {version:1,
        actividades:["cena romántica","baile bajo las estrellas","paseo a la luz de la luna"],
        accesorios:["pétalos de rosa","música romántica","nota de amor"]};
    """, ACT1),
    "sin_permiso": ("true", """
      st.cols.actividadesExtra = []; st.cols.accesoriosExtra = []; st.docs = {};
    """, ACT1),
    "repetida": ("false", """
      st.cols.actividadesExtra = [ {id:"mio", nombre:"Cena Romántica", origen:"yo"} ];
      st.cols.accesoriosExtra = [];
      st.docs = {};
    """, ACT1),
}

# que se mide en cada pantalla
def probe_config():
    return r"""
(function(){
  const d = document.getElementById("SALIDA");
  d.textContent = "arranco";
  const out = [];
  const pedir = (et, fn)=>{ try{ out.push(et + "=" + fn()); }catch(e){ out.push(et + "=<FALLO: " + e.message + ">"); } };
  setTimeout(()=>{
    d.textContent += " | paso 2500ms";
    pedir("lista", ()=>JSON.stringify(Array.from(document.querySelectorAll("#lista .item")).map(b => {
      const sp = b.querySelector("span");
      const nombre = sp ? sp.textContent : b.textContent;
      // actividades.html marca lo editable con .nube; accesorios.html con .nuevo
      const editable = b.classList.contains("nube") || b.classList.contains("nuevo");
      return nombre.replace(/\u203a/g, "").trim() + (editable ? "*" : "");
    })));
    pedir("conteo", ()=>((document.getElementById("conteo")||{}).textContent||""));
    pedir("tocar_ultimo", ()=>{
      const items = document.querySelectorAll("#lista .item");
      if(!items.length) return "(lista vacia)";
      items[items.length-1].click();
      const campo = document.getElementById("nombreNuevo");
      const btn = document.getElementById("btnAgregar");
      return "campo=\"" + (campo ? campo.value : "?") + "\" boton=" + (btn ? btn.textContent.trim() : "?");
    });
    pedir("escribir", ()=>{
      const campo = document.getElementById("nombreNuevo");
      const btn = document.getElementById("btnAgregar");
      const msg = document.getElementById("msg");
      if(!campo) return "(no hay campo)";
      campo.value = window.__A_PROBAR;
      campo.dispatchEvent(new Event("input", { bubbles: true }));
      return "boton=" + (btn ? btn.textContent.trim() : "?") +
             " deshabilitado=" + (btn ? btn.disabled : "?") +
             " aviso=" + (msg ? msg.textContent.trim() : "");
    });
    pedir("base_actividades", ()=>JSON.stringify(window.__api.ver().actividades));
    pedir("base_accesorios", ()=>JSON.stringify(window.__api.ver().accesorios));
    pedir("banderita", ()=>window.__api.ver().banderita);
    pedir("errores_js", ()=>window.__errores.join(" || ") || "ninguno");
    d.textContent += "\n" + out.join("\n");
  }, 2500);
})();
"""

PROBE_AGENDA = r"""
(function(){
  const d = document.getElementById("SALIDA");
  d.textContent = "arranco";
  const out = [];
  const pedir = (et, fn)=>{ try{ out.push(et + "=" + fn()); }catch(e){ out.push(et + "=<FALLO: " + e.message + ">"); } };
  setTimeout(()=>{
    const btns = document.querySelectorAll(".btnUsuario");
    pedir("botones_usuario", ()=>btns.length);
    if(btns.length) btns[0].click();
    setTimeout(()=>{
      d.textContent += " | entro a la app";
      const nb = document.getElementById("btnNuevaCita");
      if(nb) nb.click();
      setTimeout(()=>{
        d.textContent += " | abrio el formulario";
        pedir("opciones_actividad", ()=>JSON.stringify(Array.from(
          document.querySelectorAll("#fCampoActividad option")).map(o=>o.textContent)));
        pedir("actividad_elegida", ()=>(document.getElementById("fCampoActividad")||{}).value || "");
        pedir("checkboxes_accesorio", ()=>JSON.stringify(Array.from(
          document.querySelectorAll("#listaAccesoriosForm input[type=checkbox]")).map(i=>i.value)));
        pedir("marcados", ()=>JSON.stringify(Array.from(
          document.querySelectorAll("#listaAccesoriosForm input[type=checkbox]:checked")).map(i=>i.value)));
        pedir("base_actividades", ()=>JSON.stringify(window.__api.ver().actividades));
        pedir("base_accesorios", ()=>JSON.stringify(window.__api.ver().accesorios));
        pedir("banderita", ()=>window.__api.ver().banderita);
        pedir("errores_js", ()=>window.__errores.join(" || ") || "ninguno");
        d.textContent += "\n" + out.join("\n");
      }, 1200);
    }, 1200);
  }, 1500);
})();
"""

PROBE_JUEGOS = r"""
(function(){
  const d = document.getElementById("SALIDA");
  d.textContent = "arranco";
  const out = [];
  const pedir = (et, fn)=>{ try{ out.push(et + "=" + fn()); }catch(e){ out.push(et + "=<FALLO: " + e.message + ">"); } };
  setTimeout(()=>{
    const nodos = document.querySelectorAll("#listaActs .btnAct span, #listaActs input[type=checkbox]");
    pedir("actividades_en_lista", ()=>JSON.stringify(Array.from(nodos).map(n =>
      n.tagName === "SPAN" ? n.textContent : n.value)));
    pedir("base_actividades", ()=>JSON.stringify(window.__api.ver().actividades));
    pedir("base_accesorios", ()=>JSON.stringify(window.__api.ver().accesorios));
    pedir("banderita", ()=>window.__api.ver().banderita);
    pedir("errores_js", ()=>window.__errores.join(" || ") || "ninguno");
    d.textContent += " | medido\n" + out.join("\n");
  }, 2500);
})();
"""


def construir_pantalla(pagina_rel, destino_rel, probe, romper, store, a_probar, identidad):
    txt = io.open(os.path.join(RAIZ, pagina_rel), encoding="utf-8").read()
    for viejo, nuevo in DESTINOS:
        txt = txt.replace('"%s"' % viejo, '"%s"' % nuevo)
    # los recursos externos (CDN de qrcode, fuentes) hacen que Chrome frene su
    # reloj virtual esperando la red y el probe nunca llega a correr
    txt = re.sub(r'<script[^>]*\ssrc="https?://[^"]*"[^>]*>\s*</script>', '', txt)
    txt = re.sub(r'<link[^>]*href="https?://[^"]*"[^>]*>', '', txt)
    extra = ""
    if identidad:
        extra = ('try{ localStorage.setItem("appPareja_quienSoy",'
                 ' JSON.stringify({id:"Pareja1", nombre:"Pareja 1", admin:true})); }catch(e){}\n')
    driver = ('<script>window.__romper = %s;\nwindow.__conAcceso = true;\n'
              'window.__A_PROBAR = %s;\n%s\n%s%s</script>\n'
              % (romper, json.dumps(a_probar, ensure_ascii=False), extra, BANCO, store))
    txt = txt.replace('<script type="module">', driver + '<script type="module">', 1)
    bloque = ('<div id="SALIDA">sin ejecutar</div>\n<script>%s</script>\n' % probe)
    txt = txt.replace('</body>', bloque + '</body>', 1)
    destino = os.path.join(PAN, destino_rel)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    io.open(destino, "w", encoding="utf-8").write(txt)


def armar_escenarios():
    if os.path.isdir(PAN):
        shutil.rmtree(PAN, ignore_errors=True)
    os.makedirs(PAN, exist_ok=True)
    # los JSON de fabrica van junto, porque las pantallas los piden por fetch
    for j in ("actividades.json", "accesorios.json", "usuarios.json",
              ACT2 + ".json", ACT1 + ".json", ACT3 + ".json"):
        origen = os.path.join(RAIZ, "Citas", j)
        if os.path.exists(origen):
            shutil.copy2(origen, os.path.join(PAN, j))

    planos = [
        ('actividades', r'Citas\actividades.html', probe_config(), False, ACC1),
        ('accesorios', r'Citas\accesorios.html', probe_config(), False, ACC1),
        ('agenda', r'Citas\index.html', PROBE_AGENDA, False, ACT1),
        ('guiadas', r'Guiadas\index.html', PROBE_JUEGOS, True, ACT1),
        ('encuentros', r'Encuentros\index.html', PROBE_JUEGOS, True, ACT1),
    ]
    for etiqueta, rel, probe, identidad, _ in planos:
        for esc, (romper, store, a_probar) in ESCENARIOS.items():
            construir_pantalla(rel, "%s_%s.html" % (etiqueta, esc), probe, romper, store, a_probar, identidad)


# =====================================================================
#  3) correr Chrome
# =====================================================================
def cerrar_chrome():
    """No cerrar nada.

    Antes este script hacia `taskkill /IM chrome.exe` y eso mataba TAMBIEN
    el Chrome de la persona. Ahora cada Chrome headless se cierra solo: se
    espera a que termine con subprocess.run(). Si se cuelga, se mata solo
    ese proceso (por su PID), nunca los demas."""
    pass


def puerto():
    s = socket.socket(); s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]; s.close(); return p


def servir():
    for _ in range(8):
        p = puerto()
        pr = subprocess.Popen([sys.executable, "-m", "http.server", str(p), "--bind", "127.0.0.1"],
                              cwd=AQUI, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1.3)
        try:
            c = urllib.request.urlopen("http://127.0.0.1:%d/casos_instalador.html" % p, timeout=5).read()
            if len(c) > 500:
                return p, pr
        except Exception:
            pass
        try:
            pr.terminate()
        except Exception:
            pass
    raise SystemExit("no se pudo levantar un servidor para la prueba")


def correr(url, tag, budget=20000):
    perfil = os.path.join(TRABAJO, "perfil_" + tag)
    volcado = os.path.join(TRABAJO, "volcado_" + tag + ".html")
    if os.path.isdir(perfil):
        shutil.rmtree(perfil, ignore_errors=True)
    os.makedirs(perfil, exist_ok=True)
    with open(volcado, "w", encoding="utf-8") as f:
        proc = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                                 "--user-data-dir=" + perfil,
                                 "--virtual-time-budget=%d" % budget,
                                 "--window-size=900,900", "--dump-dom", url],
                                stdout=f, stderr=subprocess.DEVNULL)
        try:
            # se espera a que este Chrome termine. Si se cuelga, se cierra SOLO
            # este (por PID), no los demas Chrome de la computadora.
            proc.wait(timeout=240)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=20)
    t = io.open(volcado, encoding="utf-8", errors="replace").read()
    m = re.search(r'<div id="SALIDA"[^>]*>(.*?)</div>', t, re.S)
    return htmlmod.unescape(m.group(1)) if m else "(sin SALIDA)"


# =====================================================================
#  4) el programa
# =====================================================================
def main():
    if not os.path.exists(CHROME):
        print("  No se encontro Chrome en:", CHROME)
        return 1
    if os.path.isdir(TRABAJO):
        shutil.rmtree(TRABAJO, ignore_errors=True)
    os.makedirs(TRABAJO, exist_ok=True)

    print("Preparando config.js del repo...")
    preparar_config()
    print("Armando escenarios de las 5 pantallas...")
    armar_escenarios()

    p, pr = servir()
    fallas = 0
    total = 0
    try:
        print("")
        print("=" * 74)
        print("1) CASOS SUELTOS DEL INSTALADOR (config.js)")
        print("=" * 74)
        for linea in correr("http://127.0.0.1:%d/casos_instalador.html" % p, "casos").split("\n"):
            if linea.strip():
                print("  " + linea)
                if linea.startswith("FALLA"):
                    fallas += 1
                if linea.startswith(("PASA", "FALLA")):
                    total += 1

        for etiqueta, titulo in [('actividades', "Citas/actividades.html"),
                                 ('accesorios', "Citas/accesorios.html"),
                                 ('agenda', "Citas/index.html (agenda)"),
                                 ('guiadas', "Guiadas/index.html"),
                                 ('encuentros', "Encuentros/index.html")]:
            # que debe verse en la lista cuando la siembra NO pudo ocurrir
            # (el respaldo del JSON). En las pantallas de actividades van
            # actividades; en la de accesorios, accesorios.
            esperado = ACC3 if etiqueta == "accesorios" else ACT3
            print("")
            print("-" * 74)
            print("2) %s" % titulo)
            print("-" * 74)
            for esc in ESCENARIOS:
                url = "http://127.0.0.1:%d/pantallas/%s_%s.html" % (p, etiqueta, esc)
                txt = correr(url, "%s_%s" % (etiqueta, esc))
                fila = {}
                for linea in txt.split("\n"):
                    if "=" in linea:
                        k, _, v = linea.partition("=")
                        fila[k.strip()] = v.strip()
                lst = fila.get("lista") or fila.get("opciones_actividad") or fila.get("actividades_en_lista") or "(?)"
                band = fila.get("banderita", "?")
                base = fila.get("base_actividades", "(?)")
                err = fila.get("errores_js", "?")
                # Que se espera de cada escenario:
                #  - los normales: la siembra ocurrio (bandera=true) y sin errores.
                #  - sin_permiso: NO se pudo escribir, asi que la bandera queda en
                #    false y la pantalla debe seguir mostrando la fabrica del JSON
                #    (el respaldo). Tambien es correcto si no hay errores.
                if esc == "sin_permiso":
                    bien = band == "false" and err == "ninguno" and esperado in lst
                else:
                    bien = band == "true" and err == "ninguno"
                if not bien:
                    fallas += 1
                total += 1
                print("  %-13s %-7s base=%-58s bandera=%-5s js=%s"
                      % (esc, "OK" if bien else "REVISAR", base[:58], band, err))
                print("                lista=%s" % lst[:110])
    finally:
        pr.terminate()
        cerrar_chrome()

    print("")
    print("=" * 74)
    print("Comprobaciones: %d    con problema: %d" % (total, fallas))
    print("=" * 74)
    if fallas:
        print("HAY QUE REVISAR")
        return 1
    print("TODO OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
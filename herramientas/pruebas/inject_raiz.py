import io, os

H = r"C:\Users\Fred\AppData\Local\Temp\opencode\harnes_raiz"
p = os.path.join(H, "index.html")
s = io.open(p, encoding="utf-8").read()

marca = '<div id="SALIDA"'
if marca in s:
    s = s[:s.index(marca)]

DRIVER = r"""
<div id="SALIDA" style="position:fixed;left:0;top:0;right:0;z-index:9998;background:#111;color:#ff0;font:11px monospace;padding:6px;white-space:pre-wrap;max-height:70vh;overflow:auto"></div>
<script type="module">
const Q = new URLSearchParams(location.search);
const ESC = Q.get("esc") || "nada";
function P(s){ __log(s); }
function __log(s){
  window.__salida = window.__salida || [];
  window.__salida.push(s);
  const d = document.getElementById("SALIDA");
  if(d) d.textContent = "[" + ESC + "]\n" + window.__salida.map(x=>"- " + x).join("\n") +
     (window.__errores && window.__errores.length ? "\n!! " + window.__errores.join("\n!! ") : "");
}
function dormir(ms){ return new Promise(r=>setTimeout(r, ms)); }
async function esperar(fn, ms, et){
  const t0 = Date.now();
  while(Date.now() - t0 < (ms || 8000)){ let v=false; try{ v = fn(); }catch(e){} if(v) return true; await dormir(120); }
  P("   [TIMEOUT " + (et||"?") + "]"); return false;
}
function T(id){ const e = document.getElementById(id); return e ? (e.textContent || "").trim() : "NOEXISTE"; }
function vis(id){ const e = document.getElementById(id); if(!e) return "NOEXISTE"; return getComputedStyle(e).display === "none" ? "oculto" : "visible"; }
function ls(){ var a=[]; for(var i=0;i<localStorage.length;i++) a.push(localStorage.key(i)); return a.sort().join(", "); }
function quienSoy(){ try{ return JSON.parse(localStorage.getItem("appPareja_quienSoy") || "null"); }catch(e){ return null; } }
function proyecto(){ try{ return JSON.parse(localStorage.getItem("pareja_config")).firebase.projectId; }catch(e){ return "?"; } }
function escaneoValido(){
  return JSON.stringify({ firebase: { apiKey:"host", authDomain:"host.firebaseapp.com", projectId:"host",
    storageBucket:"host.firebasestorage.app", messagingSenderId:"1", appId:"1:1:web:host" } });
}
async function verInvitados(){
  document.getElementById("gearBtn").click();
  await dormir(500);
  return T("invEstado");
}
async function empezarEscaneo(){
  document.getElementById("invCardInv").click();
  await dormir(400);
  document.getElementById("invEntrar").click();
  await dormir(700);
  if(typeof window.__qrListo !== "function"){
    P("  [DIAG] typeof Html5Qrcode=" + (typeof window.Html5Qrcode)
      + " | __qrListo=" + (typeof window.__qrListo)
      + " | onclick de invEntrar=" + (typeof document.getElementById("invEntrar").onclick)
      + " | lectorInv=" + vis("lectorInv")
      + " | invMsg='" + T("invMsg") + "'");
    return false;
  }
  await window.__qrListo(escaneoValido());
  await dormir(1200);
  return true;
}

(async ()=>{
  window.__errores = [];
  window.onerror = (m,s,l)=>window.__errores.push("onerror: " + m + " @" + l);
  window.addEventListener("unhandledrejection", e=>window.__errores.push("promesa: " + (e.reason&&e.reason.message||e.reason)));
  await dormir(2200);

  if(ESC === "menu"){
    P("[M] el submenu 'Juegos' debe existir y traer Diablitos SIN candado");
    await esperar(()=>vis("menu")==="visible", 15000, "menu");
    await dormir(3000);
    P("  los 4 submenus deben verse todos:");
        ["btnExp", "btnJuegos", "btnRetos", "btnCom"].forEach(function(b){
      const v = vis(b);
      P("    " + b + " = " + v);
      if(v !== "visible"){ P("  FALLA: " + b + " no aparece en el menu"); }
    });
    P("  Comunicaciones: debe abrir y traer Chat y Acompanante:");
    document.getElementById("btnCom").click();
    await dormir(500);
    const nCom = document.querySelectorAll("#vistaCom .card").length;
    P("    abierto=" + vis("vistaCom") + " tarjetas=" + nCom);
    if(vis("vistaCom") !== "visible"){ P("  FALLA: el submenu de Comunicaciones no abre"); }
    if(nCom !== 2){ P("  FALLA: deberian ser 2 tarjetas (Chat y Acompanante), hay " + nCom); }
    document.getElementById("btnComVolver").click();
    await dormir(500);
    P("    tras Volver: menu=" + vis("vistaMenu") + " submenu=" + vis("vistaCom"));
    if(vis("vistaMenu") !== "visible"){ P("  FALLA: Volver no regresso al menu"); }
    P("  Flujo de 'Cambiar usuario': las pantallas no se deben encimar");
    document.getElementById("gearBtn").click();
    await dormir(600);
    P("    engrane: panelInvitados=" + vis("pantallaInvitado"));
    const cUsu = document.getElementById("invCardUsu");
    if(cUsu){ cUsu.click(); await dormir(600); }
    P("    en Usuarios: vistaUsu=" + vis("invVistaUsu") + " botonCambiar=" + vis("invCambiarUsu"));
    const cCam = document.getElementById("invCambiarUsu");
    if(!cCam){ P("  FALLA: no esta el boton de cambiar usuario"); }
    else{
      cCam.click();
      await dormir(700);
      const pInv = vis("pantallaInvitado");
      const pUsu = vis("pantallaUsuario");
      P("    tras Cambiar usuario: panelInvitados=" + pInv
        + " pantallaUsuario=" + pUsu + " botonVolver=" + vis("idVolverCambiar"));
      if(pInv !== "oculto"){ P("  FALLA: el panel de invitados sigue visible, se encima"); }
      if(pUsu !== "visible"){ P("  FALLA: no abrio la pantalla de elegir usuario"); }
      if(vis("idVolverCambiar") !== "visible"){ P("  FALLA: no salio el boton Volver"); }
      document.getElementById("idVolverCambiar").click();
      await dormir(700);
      P("    tras Volver: panelInvitados=" + vis("pantallaInvitado")
        + " pantallaUsuario=" + vis("pantallaUsuario"));
      if(vis("invVistaUsu") !== "visible"){ P("  FALLA: Volver no regreso a Usuarios"); }
      if(vis("pantallaUsuario") !== "oculto"){ P("  FALLA: la pantalla de usuario se quedo encima"); }
    }
    P("  y el de Retos debe traer la tarjeta de Retos:");
    document.getElementById("btnRetos").click();
    await dormir(500);
    P("    submenu abierto=" + vis("vistaRetos")
      + " tarjetas=" + document.querySelectorAll("#packsRetos .card").length);
    if(vis("vistaRetos") !== "visible"){ P("  FALLA: el submenu de Retos no abre"); }
    if(document.querySelectorAll("#packsRetos .card").length < 1){ P("  FALLA: Retos no trae ninguna tarjeta"); }
    document.getElementById("btnRetosVolver").click();
    await dormir(500);
    P("  boton 'Juegos' visible? " + vis("btnJuegos") + "  (necesita al menos un juego para aparecer)");
    P("  submenu abierto? " + vis("vistaJuegos"));
    document.getElementById("btnJuegos").click();
    await dormir(600);
    P("  dentro: submenu=" + vis("vistaJuegos"));
    const tarjetas = document.querySelectorAll("#packsJuegos .card");
    P("  tarjetas en Juegos: " + tarjetas.length);
    Array.prototype.forEach.call(tarjetas, c=>{
      P("    - '" + c.textContent.trim() + "' -> " + c.getAttribute("href"));
    });
    const diablitos = Array.prototype.find.call(tarjetas, c=>(c.getAttribute("href")||"").indexOf("Diablitos") >= 0);
    P("  Diablitos en el menu: " + (diablitos ? "SI, sin pedir acceso" : "no (el arreglo del menu esta pendiente)"));
    const candado = Array.prototype.some.call(document.querySelectorAll("#packsExp .card"), c=>c.textContent.indexOf("Citas Guiadas") >= 0);
    P("  (Citas Guiadas, que si lleva candado, sigue en Experiencias: " + (candado ? "si" : "no, porque no tengo licencia") + ")");
  }

  if(ESC === "visitando"){
    P("[G] abro la app YA registrado como invitado (config del anfitrion)");
    P("  proyecto=" + proyecto() + " yo=" + JSON.stringify(quienSoy()));
    P("  codigos al inicio: " + localStorage.getItem("licencias"));
    await dormir(6000);
    const lic = localStorage.getItem("licencias") || "{}";
    P("  codigos despues:   " + lic);
    const delHost = Object.keys(JSON.parse(lic)).indexOf("encuentros") >= 0;
    P("  " + (delHost ? "FALLA: me guarde el codigo del anfitrion" : "OK: no me guarde nada del anfitrion"));
    P("  sigo siendo invitado (no me expulsaron por estar en partida)? " + (!!(quienSoy() && quienSoy().invitado)));
  }

  if(ESC === "modulos"){
    const ids = ["gearBtn","invCardInv","invBackDeInv","invBackDeUsu","invVolverTop","invSalir","invEntrar","invConfirmar","invQR","invAgregar","invUnirNo"];
    P("modulo de la app: hasta donde llego?");
    ids.forEach(id=>{
      const e = document.getElementById(id);
      P("   " + id + ": existe=" + !!e + " onclick=" + (e ? typeof e.onclick : "-"));
    });
    P("escucharCatalogo corrio? " + (typeof localStorage.getItem("licencias")));
    return;
  }

  if(ESC === "flujo"){
    P("[A] aprieto 'Entrar modo invitado' (todavia NO eres invitado)");
    P("  texto='" + (await verInvitados()) + "'  Salir=" + vis("invSalir"));
    document.getElementById("invCardInv").click();
    await dormir(300);
    document.getElementById("invEntrar").click();
    await dormir(700);
    P("  respaldo creado antes de escanear? " + (localStorage.getItem("invitado_respaldo") ? "SI  <-- MAL" : "no  (bien)"));
    P("  proyecto=" + proyecto() + " (sigue siendo el mio)");

    P("[B] escaneo un QR valido");
    await window.__qrListo(escaneoValido());
    await dormir(1500);
    P("  respaldo creado? " + (localStorage.getItem("invitado_respaldo") ? "si (bien)" : "NO  <-- mal"));
    P("  proyecto=" + proyecto() + " (ahora es el del anfitrion: bien)");
    P("  formulario visible? " + vis("invForm") + "  texto='Solicitando Acceso' visible? " + vis("invSolicitando"));
    P("  opciones de 'de quien eres invitado': " + document.getElementById("invConQuien").options.length);
    P("  YO SIGO SIENDO? " + JSON.stringify(quienSoy()));
    P("  " + (quienSoy() && !quienSoy().invitado ? "OK: todavia NO soy invitado" : "FALLA: me registro solo"));

    P("[C] me salgo a medio camino");
    document.getElementById("invBackDeInv").click();
    await dormir(2000);
    P("  respaldo? " + (localStorage.getItem("invitado_respaldo") ? "SI  <-- mal" : "borrado (bien)"));
    P("  proyecto=" + proyecto() + " (debe ser 'mia')");
    P("  dato_mio=" + localStorage.getItem("dato_mio"));
    P("  taquilla_priv=" + localStorage.getItem("taquilla_priv"));
    P("  licencias=" + localStorage.getItem("licencias"));
    P("  texto ahora='" + (await verInvitados()) + "' Salir=" + vis("invSalir"));
  }

  if(ESC === "registro"){
    P("[D] escaneo y ME REGISTRO completo");
    if(!await empezarEscaneo()) return;
    P("  formulario=" + vis("invForm"));
    document.getElementById("invNombre").value = "Tio Beto";
    document.getElementById("invConQuien").onchange();
    await dormir(200);
    P("  vista previa='" + T("invVista") + "'");
    P("  antes de confirmar hay alguna ventana de 'Listo'? " + (document.getElementById("modalInvOk") ? "SI  <-- mal" : "no (bien: ya no existe)"));
    document.getElementById("invConfirmar").click();
    await dormir(2200);
    P("  me mando directo a: " + (window.__destino || "(nada)  <-- FALLA"));
    P("  " + (window.__destino === "Diablitos/" ? "OK: directo a la sala, sin pedir nada" : "FALLA"));
    P("  yo ahora=" + JSON.stringify(quienSoy()));
    P("  " + (quienSoy() && quienSoy().invitado ? "OK: aqui si soy invitado de verdad" : "FALLA"));
    P("  (ya no se vuelve a esta pantalla: se navego a la sala. El estado de");
    P("   'Estás de visita' se comprueba en el escenario 'visitando')");
    P("[F] el invitado NO debe quedarse con los codigos del anfitrion");
    P("  codigos al inicio: " + localStorage.getItem("licencias"));
    await dormir(4000);
    const lic = localStorage.getItem("licencias") || "{}";
    P("  codigos ahora:    " + lic);
    const delHost = Object.keys(JSON.parse(lic)).some(k => k === "guiadas" || k === "encuentros");
    P("  " + (delHost ? "FALLA: se guardo un codigo del anfitrion" : "OK: solo los mios"));
    P("  yo=" + JSON.stringify(quienSoy()));
  }


  if(ESC === "nada"){
    P("[1] no ha tocado nada");
    P("  texto='" + (await verInvitados()) + "' Salir=" + vis("invSalir"));
  }

  if(ESC === "medio"){
    P("[2] abrio la app con la config del anfitrion pero sin registro");
    P("  proyecto=" + proyecto() + " respaldo=" + (localStorage.getItem("invitado_respaldo") ? "SI <-- mal" : "borrado (bien)"));
    P("  yo=" + JSON.stringify(quienSoy()) + " dato_mio=" + localStorage.getItem("dato_mio"));
  }

  P("__fin__ errores js: " + (window.__errores.length ? window.__errores.join(" || ") : "ninguno"));
  document.title = "LISTO";
})();
</script>
"""

s = s.replace("</body>", DRIVER + "\n</body>")
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("driver v2 inyectado")
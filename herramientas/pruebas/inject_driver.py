import re, os

H = r"C:\Users\Fred\AppData\Local\Temp\opencode\harness"
p = os.path.join(H, "Encuentros", "index.html")
s = open(p, encoding="utf-8").read()

SEEDS = r"""
<script>
// Script CLASICO en <head>: corre durante el parseo, antes que cualquier
// <script type="module"> (que es diferido). Asi la app ya encuentra el
// localStorage con la identidad sembrada.
(function sembrar(){
  var q = new URLSearchParams(location.search);
  var esc = (q.get("esc") || "host");
  var fb = { apiKey: "mock", authDomain: "prueba.firebaseapp.com", projectId: "prueba",
             storageBucket: "prueba.firebasestorage.app", messagingSenderId: "1", appId: "1:1:web:prueba" };
  localStorage.setItem("pareja_config", JSON.stringify({ firebase: fb }));
  localStorage.setItem("pareja_usuarios", JSON.stringify([
    { id: "u1", nombre: "Fredy", admin: true },
    { id: "u2", nombre: "Pareja", admin: false },
    { id: "u3", nombre: "Invitado Uno", admin: false, invitado: true, conQuien: "u1" }
  ]));
  var quien = q.get("como") || ((esc === "invitado") ? "u3" : "u1");
  if(quien === "u1") localStorage.setItem("appPareja_quienSoy", JSON.stringify({ id: "u1", nombre: "Fredy", admin: true }));
  else if(quien === "u2") localStorage.setItem("appPareja_quienSoy", JSON.stringify({ id: "u2", nombre: "Pareja", admin: false }));
  else localStorage.setItem("appPareja_quienSoy", JSON.stringify({ id: "u3", nombre: "Invitado Uno", admin: false, invitado: true, conQuien: "u1" }));
  if(q.get("respaldo") != null){
    localStorage.setItem("invitado_respaldo", JSON.stringify({
      pareja_config: JSON.stringify({ firebase: fb }),
      pareja_usuarios: JSON.stringify([{ id: "u9", nombre: "Su Propia", admin: true }]),
      appPareja_quienSoy: JSON.stringify({ id: "u9", nombre: "Su Propia", admin: true }),
      marcas_invitado: "NO-DEBE-QUEDAR"
    }));
    localStorage.setItem("licencias", JSON.stringify({ encuentros: "COD-ANFITRION", otro: "X" }));
    localStorage.setItem("taquilla_priv", "LLAVE-PRIVADA");
    localStorage.setItem("inventado_del_anfitrion", "NO-DEBE-QUEDAR");
  }
  if(q.get("sinLic")) localStorage.removeItem("licencias");
  else localStorage.setItem("licencias", JSON.stringify({ encuentros: "COD.FIRMA" }));

  // Para poder observar el estado DESPUES de salirModoInvitado sin que la pagina
  // navegue y destruya el contexto, se intercepta location.replace.
  window.__redirect = null;
  try{
    Object.defineProperty(window.Location.prototype, "replace", { configurable: true, value: function(u){ window.__redirect = u; } });
  }catch(e){ window.__replaceError = e.message; }
})();
</script>
</head>"""

DRIVER = r"""
<div id="SALIDA" style="position:fixed;left:0;top:0;right:0;z-index:9998;background:#111;color:#ff0;font:11px monospace;padding:6px;white-space:pre-wrap;max-height:70vh;overflow:auto"></div>
<script type="module">
import { __volcar, __sembrar } from "../mock/firebase-firestore.js";

const Q = new URLSearchParams(location.search);
const ESC = Q.get("esc") || "host";
const APP = { name: "[DEFAULT]" };

function P(s){ __log(s); }
function __log(s){
  window.__salida = window.__salida || [];
  window.__salida.push(s);
  const d = document.getElementById("SALIDA");
  if(d) d.textContent = "[" + ESC + (Q.get("flag") ? " " + Q.get("flag") : "") + "]\n" +
    window.__salida.map(x=>"- " + x).join("\n") +
    (window.__errores.length ? "\n!! " + window.__errores.join("\n!! ") : "");
}
function visEl(e){
  if(!e) return "NOEXISTE";
  let n = e;
  while(n && n !== document.documentElement){
    const cs = getComputedStyle(n);
    if(cs.display === "none") return "oculto";
    if(cs.visibility === "hidden") return "invisible";
    if(parseFloat(cs.opacity) === 0) return "opacidad0";
    n = n.parentElement;
  }
  const r = e.getBoundingClientRect();
  if(r.width === 0 && r.height === 0) return "tam0";
  return "visible";
}
function vis(id){ return visEl(document.getElementById(id)); }
function T(id){ const e = document.getElementById(id); return e ? (e.textContent || "").trim() : "NOEXISTE"; }
function dormir(ms){ return new Promise(r=>setTimeout(r, ms)); }
async function esperar(fn, ms, etiqueta){
  const t0 = Date.now();
  while(Date.now() - t0 < (ms || 8000)){
    let v = false;
    try{ v = fn(); }catch(e){}
    if(v) return true;
    await dormir(120);
  }
  P("   [TIMEOUT esperando " + (etiqueta || "?") + "]");
  return false;
}
function doc(){ return (__volcar(APP) || {})["sesionEncuentros/actual"]; }
function put(mut){ const d = JSON.parse(JSON.stringify(doc() || {})); mut(d); __sembrar(APP, { "sesionEncuentros/actual": d }); }
function bots(){ return Array.from(document.querySelectorAll("#listaActs button.btnAct")); }
function habilitadas(){ return bots().filter(b=>!b.disabled); }
function ls(){
  var a = [];
  for(var i = 0; i < localStorage.length; i++){ var k = localStorage.key(i); a.push(k + "=" + String(localStorage.getItem(k)).slice(0, 40)); }
  return a.sort().join(" | ");
}
function users(){ return JSON.stringify((__volcar(APP) || {})["config/ajustes"]); }
async function jugarComo(primera){
  await esperar(()=> vis("vistaLista") === "visible", 12000, "vistaLista");
  P("ARRANQUE " + (ESC === "invitado" ? "(invitado)" : "(anfitrion)") + ": bloqueo=" + vis("vistaBloqueo") +
    " lista=" + vis("vistaLista") + " espera=" + vis("vistaEspera") + " player=" + vis("vistaPlayer"));
  P("  actividades: " + bots().length + " (" + habilitadas().length + " con acciones)");
P("  salida 'lnkInicio' (el anfitrion SI debe verla): " + visEl(document.getElementById("lnkInicio")));
if(visEl(document.getElementById("lnkInicio")) !== "visible"){ P("  FALLA: el anfitrion no ve la salida"); }
  const b = habilitadas()[primera || 0];
  if(!b){ P("  no hay actividad habilitada"); return false; }
  P("  toco: '" + b.textContent.trim() + "'");
  b.click();
  return true;
}
async function tomas(t){
  await esperar(()=> vis("modalTomas") === "visible", 5000, "modalTomas");
  const c = document.querySelectorAll("#tomasGridEncuentros input");
  c[0].value = String(t || 3);
  for(let i = 1; i < c.length; i++) c[i].value = "0";
  document.getElementById("btnTomasOk").click();
}

// ---------------- avanzar turno de otro jugador (replica de avanzarSesion) --------
function avanzarAjeno(){
  const d = JSON.parse(JSON.stringify(doc()));
  const nc = d.cabezas.length;
  let r = d.ronda, t = d.turno, o = d.orden;
  if(t + 1 < nc){ t++; }
  else{
    r++;
    if(r >= d.largo){
      d.activa = false; d.terminada = true; d.ronda = r; d.turno = 0;
      __sembrar(APP, { "sesionEncuentros/actual": d });
      return "FIN NATURAL";
    }
    t = 0;
    o = d.cabezas.map(c=>c.id).sort((a, b)=> a < b ? -1 : 1);
  }
  d.ronda = r; d.turno = t; d.orden = o;
  __sembrar(APP, { "sesionEncuentros/actual": d });
  return "ok";
}

// ===================== ESCENARIOS =====================
async function escHost(){
  if(!await jugarComo(0)) return;
  await tomas(3);
  await esperar(()=> vis("vistaPlayer") === "visible", 8000, "player");
  const d0 = doc();
  P("ARRANCA: '" + T("progreso") + "' orden=" + d0.orden.join(",") + " largo=" + d0.largo);
  P("  nivelTag: " + visEl(document.getElementById("nivelTag")) + " texto='" + T("nivelTag") + "'");
  P("  listas por cabeza (nivel de cada posicion):");
  d0.cabezas.forEach(c=>{
    P("    " + c.nombre + " (" + c.lado + "): " + (d0.listas[c.id]||[]).map(x=>x.nivel).join(" > "));
  });
  // el anfitrion ve su accion solo si es su turno: forzar que sea el primero
  put(d=>{ const o = d.orden.filter(x=>x!=="u1"); d.orden = ["u1"].concat(o); d.turno = 0; });
  await dormir(600);
  P("  turno forzado al anfitrion: '" + T("actividadAhora") + "' tag='" + T("nivelTag") + "' (" + visEl(document.getElementById("nivelTag")) + ")");
  P("  color=" + getComputedStyle(document.getElementById("actividadAhora")).color);
  P("  btnSig='" + T("btnSig") + "'");

  // ---- las tres salidas de la partida ----
  P("[A] no se puede salir de la partida");
  P("  durante el juego: 'lnkInicio'(<-Inicio)=" + visEl(document.getElementById("lnkInicio")) +
    "  'btnAtras'(<-Lista)=" + visEl(document.getElementById("btnAtras")));
  P("  en la lista:      'lnkInicio'(<-Inicio)=" + visEl(document.getElementById("lnkInicio")) +
    "  'btnAtras'(<-Lista)=" + visEl(document.getElementById("btnAtras")));
  const h0 = history.length;
  for(let k = 1; k <= 3; k++){
    history.back();
    await dormir(700);
    P("  gesto atras #" + k + ": player=" + vis("vistaPlayer") + " lista=" + vis("vistaLista") +
      " accion='" + T("actividadAhora") + "' history.length=" + history.length + " (posicion " + history.length + ")");
  }
  P(" CRECIMIENTO: history.length paso de " + h0 + " a " + history.length +
    (history.length > h0 ? "  <-- CRECE: el gesto esta dejando entradas nuevas" : "  (bien: no crece)"));

  // ---- Pausar y salir ----
  P("[B] Pausar y Salir");
  put(d=>{ d.orden = ["u1","u2","u3"]; d.turno = 0; d.ronda = 0; });
  await dormir(400);
  document.getElementById("btnTerminar").click();
  await dormir(900);
  P("  doc: activa=" + doc().activa + " pausada=" + doc().pausada + " terminada=" + doc().terminada);
  P("  pantalla: player=" + vis("vistaPlayer") + " lista=" + vis("vistaLista") + " espera=" + vis("vistaEspera"));

  // ---- volver a entrar y continuar ----
  P("[C] Continuar");
  document.getElementById("btnEsperaRefrescar").click();
  await dormir(900);
  if(!await jugarComo(0)) return;
  P("  modal Continuar: " + vis("vistaSeguir") + " titulo='" + T("sgTitulo") + "' desc='" + T("sgDesc") + "'");
  if(vis("vistaSeguir") === "visible"){
    document.getElementById("btnContinuar").click();
    await dormir(900);
    P("  tras Continuar: player=" + vis("vistaPlayer") + " '" + T("progreso") + "' sid nuevo=" + (doc().sid !== "sid-demo"));
    P("  doc: activa=" + doc().activa + " pausada=" + doc().pausada + " reanudada=" + doc().reanudada);
  }

  // ---- Terminar Partida ----
  P("[D] Terminar Partida");
  P("  antes de terminar: 'lnkInicio'=" + visEl(document.getElementById("lnkInicio")) + " 'btnAtras'=" + visEl(document.getElementById("btnAtras")));
  document.getElementById("btnTerminarPartida").click();
  await dormir(1000);
  P("  doc: activa=" + doc().activa + " terminada=" + doc().terminada + " porAdmin=" + doc().porAdmin);
  P("  pantalla: player=" + vis("vistaPlayer") + " lista=" + vis("vistaLista"));
  P("  al salir: 'lnkInicio'=" + visEl(document.getElementById("lnkInicio")) + " 'btnAtras'=" + visEl(document.getElementById("btnAtras")) + " (deben reaparecer)");
  P("  (el anfitrion no ve aviso de fin: solo cae a la lista)");
}

async function escInvitado(){
  await dormir(2500);
  P("INVITADO: bloqueo=" + vis("vistaBloqueo") + " espera=" + vis("vistaEspera") + " lista=" + vis("vistaLista") + " modalUnir=" + vis("modalUnir") + " '" + T("unirDesc") + "'");
  P("  localStorage: " + ls());
  P("  config/ajustes: " + users());
const _sal = visEl(document.getElementById("lnkInicio"));
  // Ojo: hay escenarios llamados "invitado" que en realidad playing como u2, que
  // es la PAREJA (no es invitada). u3 es el invitado de verdad. La pareja si
  // puede ver la salida; el invitado no.
  // Ojo: NO se usa la variable "quien" del arnés, porque no está disponible
  // dentro de esta función. Se lee del localStorage, que es el estado real.
  const _yo = (function(){ try{ return JSON.parse(localStorage.getItem("appPareja_quienSoy")||"null"); }catch(e){ return null; } })();
  const _us = (function(){ try{ return JSON.parse(localStorage.getItem("pareja_usuarios")||"[]"); }catch(e){ return []; } })();
  const _u = (_yo && _us.find(function(x){ return x.id === _yo.id; })) || _yo || {};
  const _soyInv = !!_u.invitado;
  P("  salida 'lnkInicio' (" + (_soyInv ? "invitado u3: NO debe verla" : "pareja: SI debe verla") + "): " + _sal);
  if(_soyInv && _sal !== "oculto"){ P("  FALLA: el invitado tiene salida, va en contra de la regla"); }
  if(!_soyInv && _sal !== "visible"){ P("  FALLA: la pareja no ve la salida"); }
  if(vis("modalUnir") !== "visible"){ P("  no llego la invitacion"); return; }
  document.getElementById("btnUnirme").click();
  await esperar(()=> vis("vistaPlayer") === "visible", 5000, "player");
  P("  entro: '" + T("progreso") + "' '" + T("actividadAhora") + "' btnSig='" + T("btnSig") + "'");
  P("  botones admin ocultos: Pausar=" + visEl(document.getElementById("btnTerminar")) + " Terminar=" + visEl(document.getElementById("btnTerminarPartida")));
  P("  nivelTag=" + visEl(document.getElementById("nivelTag")));
  P("  salidas durante el juego: 'lnkInicio'=" + visEl(document.getElementById("lnkInicio")) +
    " 'btnAtras'=" + visEl(document.getElementById("btnAtras")));
  P("  boton saltar (NO debe verse): " + visEl(document.getElementById("btnSaltar")));
  P("  botones que SI tiene el invitado: Siguiente=" + visEl(document.getElementById("btnSig")) +
    " (texto '" + T("btnSig") + "')");
  history.back();
  await dormir(800);
  P("  gesto atras: player=" + vis("vistaPlayer") + " espera=" + vis("vistaEspera") + " (debe seguir en el juego)");

  const flag = Q.get("flag");
  if(flag === "pausa"){
    P("[pausa] el anfitrion pausa");
    put(d=>{ d.pausada = true; });
    await dormir(900);
    P("  modalPausa=" + vis("modalPausa") + " texto='" + (document.querySelector("#modalPausa .caja") || {}).textContent + "'");
    P("  player=" + vis("vistaPlayer") + " (debe salir del juego)");
    P("  invitacion sigue viva (no lo expulsan)? " + (((__volcar({name:"[DEFAULT]"})||{})["invitaciones/encuentros"]||{}).activa));
    document.getElementById("btnPausaOk").click();
    await dormir(1300);
    const destino = window.__destino || "(se quedo en Encuentros)";
    P("  tras Aceptar, me mando a: " + destino);
    P("  pantalla aqui: espera=" + vis("vistaEspera") + " player=" + vis("vistaPlayer") + " modalPausa=" + vis("modalPausa"));
    const eraInvitado = (function(){ try{ return !!JSON.parse(localStorage.getItem("appPareja_quienSoy")).invitado; }catch(e){ return false; } })();
    if(eraInvitado){
      P("  respaldo intacto (NO lo expulsaron): " + (localStorage.getItem("invitado_respaldo") ? "si (bien)" : "NO  <-- mal"));
      P("  sigue siendo invitado: si (bien)");
    }else{
      P("  (no es invitado, asi que no hay respaldo ni expulsions que revisar)");
    }
  }
  if(flag === "fin"){
    P("[fin] el anfitrion termina la partida");
    put(d=>{ d.activa = false; d.terminada = true; d.porAdmin = true; });
    await dormir(900);
    P("  modalFin=" + vis("modalFin") + " texto='" + T("finTxt") + "'");
    P("  localStorage ANTES: " + ls());
    P("  (patch replace: " + (window.__replaceError ? "FALLO " + window.__replaceError : "ok") + ")");
    document.getElementById("btnFinOk").click();
    await dormir(1500);
    P("  >> location.replace -> " + window.__redirect);
    P("  localStorage DESPUES: " + ls());
    P("     appPareja_quienSoy  = " + localStorage.getItem("appPareja_quienSoy"));
    P("     pareja_usuarios     = " + localStorage.getItem("pareja_usuarios"));
    P("     licenses            = " + localStorage.getItem("licencias"));
    P("     invitado_respaldo   = " + localStorage.getItem("invitado_respaldo"));
    P("     marcas_invitado     = " + localStorage.getItem("marcas_invitado"));
    P("     inventado_anfitrion = " + localStorage.getItem("inventado_del_anfitrion"));
    P("     taquilla_priv       = " + localStorage.getItem("taquilla_priv"));
    P("  config/ajustes del anfitrion: " + users());
  }
  if(flag === "natural"){
    P("[fin natural] la partida se acaba sola");
    put(d=>{ d.activa = false; d.terminada = true; d.porAdmin = false; });
    await dormir(900);
    P("  modalFin=" + vis("modalFin") + " texto='" + T("finTxt") + "'");
  }
}

async function escTerminada(){
  await dormir(2500);
  P("INVITADO con partida VIEJA ya terminada (prueba del arreglo 6.1):");
  P("  espera=" + vis("vistaEspera") + " modalFin=" + vis("modalFin") + " modalUnir=" + vis("modalUnir") + " modalPausa=" + vis("modalPausa"));
  P("  => " + (vis("modalFin") === "oculto" ? "OK: no salta el aviso de fin solo" : "FALLA: vuelve a saltar"));
}

async function escFantasma(){
  await dormir(2500);
  const d = doc();
  P("SE FUE UN INVITADO: el invitado u3 ya no esta en la lista de la app,");
  P("  pero sigue en el orden de turnos de la partida.");
  P("  usuarios ahora: " + users());
  P("  doc: orden=" + d.orden.join(",") + " turno=" + d.turno + " -> le tocaba a " + d.orden[d.turno]);
  P(" _expect: al retomar, u3 se brinca y le toca el siguiente que quede");

  if(!await jugarComo(0)) return;
  P("  modal Continuar: " + vis("vistaSeguir") + " desc='" + T("sgDesc") + "'");
  if(vis("vistaSeguir") !== "visible"){ P("  no ofrecio continuar"); return; }
  document.getElementById("btnContinuar").click();
  await dormir(1200);
  P("  tras Continuar: player=" + vis("vistaPlayer") + " '" + T("progreso") + "'");
  P("  pantalla: '" + T("actividadAhora") + "' btnSig='" + T("btnSig") + "' disabled=" + document.getElementById("btnSig").disabled);
  const d2 = doc();
  P("  DOC ya saneado: orden=" + d2.orden.join(",") + " turno=" + d2.turno);
  P("  DOC cabezas=" + JSON.stringify(d2.cabezas.map(c=>c.nombre)) + "  largo=" + d2.largo);
  P("  listas que quedan: " + Object.keys(d2.listas || {}).join(","));

  // ahora el anfitrion avanza: la ronda debe SI avanzar
  let clics = 0;
  for(let k = 0; k < 12; k++){
    const dd = doc();
    if(!dd || !dd.activa){ P("  la partida termino"); break; }
    if(dd.orden[dd.turno] === "u1"){
      const antes = dd.ronda + "/" + dd.turno;
      document.getElementById("btnSig").click();
      clics++;
      await dormir(650);
      const x = doc();
      P("    anfitrion avanza " + antes + " -> " + x.ronda + "/" + x.turno + " activa=" + x.activa + " terminada=" + x.terminada);
    }else{
      const res = avanzarAjeno();
      await dormir(400);
      const x = doc();
      P("    " + dd.orden[dd.turno] + " avanza -> " + x.ronda + "/" + x.turno + " (" + res + ") | '" + T("actividadAhora") + "'");
      if(res === "FIN NATURAL"){ await dormir(900); P("    FIN: player=" + vis("vistaPlayer") + " lista=" + vis("vistaLista")); break; }
    }
  }
  const df = doc();
  P("RESULTADO: activa=" + df.activa + " terminada=" + df.terminada + " ronda=" + df.ronda + "/" + df.largo + " clics=" + clics);
  P("  " + (df.ronda > 0 ? "OK: la ronda AVANZO (ya no esta trabada)" : "FALLA: la ronda sigue en 0 (trancada)"));
}

async function escSinsuc(){
  await dormir(2500);
  P("SIN LICENCIA: bloqueo=" + vis("vistaBloqueo") + " desc='" + T("licMsg") + "'");
  P("  botones: Tienda=" + visEl(document.getElementById("btnTienda")) + " Revisar=" + visEl(document.getElementById("btnRevisar")) + " TengoCodigo=" + visEl(document.getElementById("btnTengo")));
  document.getElementById("btnRevisar").click();
  await dormir(1500);
  P("  tras 'revisar acceso': bloqueo=" + vis("vistaBloqueo") + " (sigue bloqueado: correcto, no hay codigo)");
}

async function escMulti(){
  if(!await jugarComo(0)) return;
  // volver a la lista y entrar en multi
  document.getElementById("btnMulti").click();
  await dormir(700);
  P("MULTI: fila seleccion=" + vis("filaMultiSel") + " btnMulti=" + vis("btnMulti") + " titulo='" + T("tituloLista") + "' desc='" + T("descLista") + "'");
  P("  Combinar: '" + T("btnMultiGo") + "' disabled=" + document.getElementById("btnMultiGo").disabled);
  const labs = Array.from(document.querySelectorAll("#listaActs label.btnAct"));
  const okLabs = labs.filter(l=>{ const c=l.querySelector("input"); return c && !c.disabled; }).slice(0,3);
  for(const l of okLabs){ l.querySelector("input").click(); await dormir(250); }
  P("  tras marcar 3: '" + T("btnMultiGo") + "' disabled=" + document.getElementById("btnMultiGo").disabled);
  const extra = labs.filter(l=>{ const c=l.querySelector("input"); return c && !c.disabled; })[3];
  if(extra){ extra.querySelector("input").click(); await dormir(300); P("  tras marcar una 4a: '" + T("btnMultiGo") + "' disabled=" + document.getElementById("btnMultiGo").disabled + " (debe seguir 3/3 y la 4a sin marcar)"); }
  document.getElementById("btnMultiGo").click();
  await dormir(500);
  P("  modal confirmar=" + vis("modalMulti2") + " resumen='" + T("multiResumen") + "'");
  document.getElementById("btnMulti2Ok").click();
  await esperar(()=> vis("modalTomas") === "visible", 5000, "tomas multi");
  const c = document.querySelectorAll("#tomasGridEncuentros input");
  c[0].value = "4"; for(let i=1;i<c.length;i++) c[i].value="0";
  document.getElementById("btnTomasOk").click();
  await esperar(()=> vis("vistaPlayer") === "visible", 8000, "player multi");
  const d = doc();
  P("  DOC multi: modo=" + d.modo + " actividades=" + JSON.stringify(d.actividades) + " largo=" + d.largo);
  d.cabezas.forEach(c2=>{ P("    " + c2.nombre + ": " + (d.listas[c2.id]||[]).map(x=>x.nivel).join(" > ")); });
  P("  plTitulo='" + T("plTitulo") + "'");
}



async function escEntrar(){
  await dormir(2600);
  P("[DIRECTO] llegue desde la sala con ?entrar=1");
  P("  DIAG: location.search='" + location.search + "'");
  P("  DIAG: yo=" + localStorage.getItem("appPareja_quienSoy"));
  P("  DIAG: sesion=" + JSON.stringify((__volcar({name:"[DEFAULT]"})||{})["sesionEncuentros/actual"] || null));
  P("  DIAG: ajustes=" + JSON.stringify(((__volcar({name:"[DEFAULT]"})||{})["config/ajustes"]||null)));
  P("  DIAG: espera=" + vis("vistaEspera") + " bloqueo=" + vis("vistaBloqueo") + " lista=" + vis("vistaLista"));
  P("  pantalla: player=" + vis("vistaPlayer") + "  modalUnir=" + vis("modalUnir"));
  P("  " + (vis("vistaPlayer") === "visible" && vis("modalUnir") === "oculto"
        ? "OK: entro DIRECTO al juego, sin preguntarle otra vez"
        : "FALLA: le volvio a preguntar"));
  P("  progreso='" + T("progreso") + "'  actividad='" + T("actividadAhora") + "'");
  P("  " + (vis("btnSaltar") === "oculto" ? "OK: es invitado (sin botones de admin)" : "revisar"));
}

async function escHost2(){
  P("[E] boton de saltar turno (solo anfitrion)");
  if(!await jugarComo(0)) return;
  await tomas(3);
  await esperar(()=> vis("vistaPlayer") === "visible", 8000, "player");
  // turno del anfitrion: el boton NO debe verse
  put(d=>{ d.orden = ["u1","u2","u3"]; d.turno = 0; d.ronda = 0; });
  await dormir(600);
  P("  con mi turno:      Saltar=" + visEl(document.getElementById("btnSaltar")) + " (debe estar oculto)");
  // turno de otro
  put(d=>{ d.orden = ["u2","u1","u3"]; d.turno = 0; });
  await dormir(700);
  const bs = document.getElementById("btnSaltar");
  P("  con turno ajeno:   Saltar=" + visEl(bs) + " texto='" + bs.textContent + "'");
  P("  pantalla: '" + T("actividadAhora") + "'");
  const antes = doc();
  const d0 = doc();
  P("  antes de saltar: ronda=" + d0.ronda + " turno=" + d0.turno + " (le toca a " + d0.orden[d0.turno] + ")");
  window.confirm = function(){ P("    [confirm] '" + arguments[0].replace(/\n/g, " / ") + "' -> ACEPTADO"); return true; };
  bs.click();
  await dormir(1200);
  const d1 = doc();
  P("  despues de saltar: ronda=" + d1.ronda + " turno=" + d1.turno + " (ahora le toca a " + d1.orden[d1.turno] + ")");
  P("  pantalla: '" + T("actividadAhora") + "' btnSaltar=" + visEl(bs));
  P("  " + (d1.turno !== d0.turno || d1.ronda !== d0.ronda ? "OK: el turno se movio" : "FALLA: no se movio"));

  P("[F] aviso de fin de partida para el ANFITRION");
  put(d=>{ d.activa = false; d.terminada = true; d.porAdmin = false; });
  await dormir(1200);
  P("  modalFin=" + vis("modalFin") + " texto='" + T("finTxt") + "'");
  P("  " + (vis("modalFin") === "visible" ? "OK: el anfitrion recibio el aviso" : "FALLA: no le llego el aviso"));
  P("  antes de aceptar, localStorage: " + ls());
  document.getElementById("btnFinOk").click();
  await dormir(1400);
  P("  tras aceptar: modalFin=" + vis("modalFin") + " lista=" + vis("vistaLista") + " player=" + vis("vistaPlayer"));
  P("  " + (window.__redirect ? "FALLA: lo mando a otra pagina (" + window.__redirect + ")" : "OK: se quedo en Encuentros, no borro nada"));
  P("  localStorage despues: " + ls());
}


async function escNiveles(){
  const T = { basico: 2, medio: 2, avanzado: 1, experto: 1, alucinado: 1 };
  const orden = ["basico", "medio", "avanzado", "experto", "alucinado"];
  const NOMBRES = { basico: "Básico", medio: "Medio", avanzado: "Avanzado", experto: "Experto", alucinado: "Alucinado" };
  const esperado = [];
  orden.forEach(k=>{ for(let i = 0; i < T[k]; i++) esperado.push(NOMBRES[k]); });
  const esperadoTxt = esperado.join(" > ");

  P("[NIVELES] los 5 niveles, 2 de los basicos, 2 de los medios, 1 de cada uno de los restantes");
  P("  se espera que TODOS tengan: " + esperadoTxt);
  if(!await jugarComo(0)) return;
  await esperar(()=> vis("modalTomas") === "visible", 5000, "modalTomas");
  const c = document.querySelectorAll("#tomasGridEncuentros input");
  orden.forEach((k, i)=>{ c[i].value = String(T[k]); });
  document.getElementById("btnTomasOk").click();
  await esperar(()=> vis("vistaPlayer") === "visible", 8000, "player");
  const d = doc();
  P("  largo=" + d.largo + " (se pidieron " + esperado.length + ")  orden de turnos=" + d.orden.join(","));
  const seqs = {};
  d.cabezas.forEach(h=>{
    const fila = (d.listas[h.id] || []).map(x=>x.nivel);
    seqs[h.id] = fila.join(" > ");
    const nivelesBien = fila.length === esperado.length && fila.every((x, i)=>x === esperado[i]);
    const marcas = [];
    if(fila.length !== esperado.length) marcas.push("largo " + fila.length + " vs " + esperado.length);
    fila.forEach((x, i)=>{ if(x !== esperado[i]) marcas.push("pos " + (i+1) + ": " + x + " vs " + esperado[i]); });
    P("    " + (h.nombre + " (" + h.lado + ")").padEnd(20) + " " + (fila.join(" > ") || "(vacia)"));
    P("      " + (nivelesBien ? "OK: mismo nivel que se pidio" : "FALLA: " + marcas.join(", ")));
  });
  const vals = Object.keys(seqs).map(k=>seqs[k]);
  const iguales = vals.every(v=>v === vals[0]);
  P("  " + (iguales ? "OK: TODOS los jugadores tienen la misma secuencia de niveles" : "FALLA: hay jugadores con niveles distintos"));
  const largos = d.cabezas.map(h=>((d.listas[h.id]||[]).length));
  P("  largo de cada lista: " + largos.join(",") + (largos.every(x=>x === largos[0]) ? "  (OK: todos igual)" : "  (FALLA: desiguales)"));
  const sinRepetirDentro = d.cabezas.every(h=>{
    const t = (d.listas[h.id]||[]).map(x=>x.texto);
    return new Set(t).size === t.length;
  });
  P("  dentro de cada lista, sin repetir: " + (sinRepetirDentro ? "OK" : "hay repetidas (esperado si el nivel no alcanza para todos)"));
}


async function escInvitacion(){
  P("[INV] el juego publica su invitacion para que la sala la vea");
  if(!await jugarComo(0)) return;
  await tomas(3);
  await esperar(()=> vis("vistaPlayer") === "visible", 8000, "player");
  const d = doc();
  await dormir(900);
  const inv = (__volcar({ name: "[DEFAULT]" }) || {})["invitaciones/encuentros"];
  P("  documento 'invitaciones/encuentros': " + (inv ? "existe" : "NO EXISTE  <-- mal"));
  if(inv){
    P("    juego=" + inv.juego + " titulo='" + inv.titulo + "' ruta=" + inv.ruta + " icono=" + inv.icono);
    P("    activa=" + inv.activa + " host=" + inv.hostNombre + " participantes=" + JSON.stringify(inv.participantes));
    P("    " + (inv.activa === true && inv.ruta === "Encuentros" ? "OK: la sala puede mostrarla" : "FALLA"));
  }
  P("[INV2] al terminar la partida, la invitacion se retira");
  document.getElementById("btnTerminarPartida").click();
  await dormir(1400);
  const inv2 = (__volcar({ name: "[DEFAULT]" }) || {})["invitaciones/encuentros"];
  P("  activa ahora=" + (inv2 ? inv2.activa : "(no existe)"));
  P("  " + (inv2 && inv2.activa === false ? "OK: retirada (la sala expulsa)" : "FALLA: sigue activa"));
  P("[INV3] al pausar, la invitacion debe SEGUIR activa (el juego no acabo)");
  await jugarComo(0);
  await tomas(3);
  await esperar(()=> vis("vistaPlayer") === "visible", 8000, "player2");
  await dormir(800);
  document.getElementById("btnTerminar").click();
  await dormir(1400);
  const inv3 = (__volcar({ name: "[DEFAULT]" }) || {})["invitaciones/encuentros"];
  P("  tras pausar: activa=" + (inv3 ? inv3.activa : "(no existe)"));
  P("  " + (inv3 && inv3.activa === true ? "OK: sigue invites" : "FALLA: se retiro al pausar"));
}

(async ()=>{
  await dormir(700);
  P("carga #" + (sessionStorage.getItem("n") || 1) + " | patch replace: " + (window.__replaceError ? "FALLO" : "ok"));
  try{
    if(!sessionStorage.getItem("n")) sessionStorage.setItem("n", "2");
    if(ESC === "invitado") await escInvitado();
    else if(ESC === "terminada") await escTerminada();
    else if(ESC === "fantasma") await escFantasma();
    else if(ESC === "sinsuc") await escSinsuc();
    else if(ESC === "multi") await escMulti();
    else if(ESC === "host2") await escHost2();
    else if(ESC === "entrar") await escEntrar();
    else if(ESC === "niveles") await escNiveles();
    else if(ESC === "invitacion") await escInvitacion();
    else await escHost();
  }catch(e){
    P("FALLO DEL DRIVER: " + (e && e.message) + " | " + String(e && e.stack || "").split("\n").slice(1,3).join(" <- "));
  }
  P("__fin__ errores js: " + (window.__errores.length ? window.__errores.join(" || ") : "ninguno"));
  document.title = "LISTO";
})();
</script>
"""

s = s.replace(SEEDS, "")
s = s.replace("</head>", SEEDS, 1)
s = s.replace("</body>", DRIVER + "\n</body>")
open(p, "w", encoding="utf-8", newline="\n").write(s)
print("driver inyectado ->", p, len(s), "bytes")
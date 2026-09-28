// =====================================================
//  CONFIG COMPARTIDA — Citas de Pareja (template)
//  Prioridad: 1) Asistente (localStorage)  2) firebase-config.js
//  Compatible con futura capa multi-pareja: los usuarios
//  viven en Firestore `config/ajustes` ({usuarios:[...]}),
//  con copia local y JSON como respaldos.
// =====================================================

export const CLAVE_CONFIG = "pareja_config";
export const CLAVE_USUARIOS = "pareja_usuarios";

export const PH = {
  token: "PON_AQUI_TU_TOKEN",
  chat: "PON_AQUI_TU_CHAT_ID",
  app: "PON_AQUI_URL_DE_TU_APP/",
};

function leerJSON(clave){
  try{
    const t = localStorage.getItem(clave);
    return t ? JSON.parse(t) : null;
  }catch(e){ return null; }
}

export function leerConfigGuardada(){
  return leerJSON(CLAVE_CONFIG);
}

export function guardarConfig(cfg){
  localStorage.setItem(CLAVE_CONFIG, JSON.stringify(cfg));
}

/** Firebase efectivo: lo guardado manda; si no, la base del repo. */
export function resolverFirebase(base){
  const g = leerConfigGuardada();
  return (g && g.firebase) ? g.firebase : base;
}

/** Telegram efectivo: lo guardado manda; si no, placeholders (avisos apagados). */
export function resolverTelegram(){
  const g = leerConfigGuardada();
  if(g && g.telegram) return g.telegram;
  return { token: PH.token, chat: PH.chat };
}

/** Raíz de la app calculada de la URL actual (sirve en Pages, local y file). */
export function baseUrl(){
  try{
    let u = location.href.split("?")[0].split("#")[0];
    u = u.replace(/[^/]+\.html?$/i, "");
    if(!/\/$/.test(u)) u += "/";
    u = u.replace(/\/(Citas|Retos)\/$/, "/");
    return u;
  }catch(e){ return PH.app; }
}

/** Usuarios: copia local rápida del asistente. */
export function guardarUsuariosLocal(usuarios){
  try{ localStorage.setItem(CLAVE_USUARIOS, JSON.stringify(usuarios)); }catch(e){}
}

export function leerUsuariosLocal(){
  const u = leerJSON(CLAVE_USUARIOS);
  return Array.isArray(u) && u.length ? u : null;
}

/** Lee usuarios en orden: Firestore ajustes > local > JSON dado. Nunca revienta. */
export async function cargarUsuarios(db, getDocFn, docFn, respaldoJSON){
  // 1) Firestore (con tope para no colgar sin config)
  try{
    const snap = await conTiempo(getDocFn(docFn(db, "config", "ajustes")), 8000);
    const arr = snap.exists() ? snap.data().usuarios : null;
    if(Array.isArray(arr) && arr.length){
      guardarUsuariosLocal(arr);
      return arr;
    }
  }catch(e){}
  // 2) copia local del asistente
  const loc = leerUsuariosLocal();
  if(loc) return loc;
  // 3) JSON del repo
  return respaldoJSON;
}

function conTiempo(promesa, ms){
  return Promise.race([
    promesa,
    new Promise((_, rechazar)=>setTimeout(()=>rechazar(new Error("timeout")), ms))
  ]);
}

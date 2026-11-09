// =====================================================
//  PACKS DE PERSONAJES — instalación en la base de la pareja
//  El pack vive UNA sola vez, en la base de la taquilla (`packs`).
//  Aquí se copia a `personajesJuego/actual` la primera vez que la
//  pareja abre Roles, y se anota el mapa de slots en `packsInstalados`.
//  Detalle completo: General/Packs-Personajes.md
// =====================================================
import { doc, getDoc, serverTimestamp, runTransaction } from
  "https://www.gstatic.com/firebasejs/10.13.1/firebase-firestore.js";
import { oficialesAprobados } from "./acceso.js";

// Las cinco listas del documento de personajes.
const LISTAS = ["U1", "U2", "C1", "C2"];

function refPersonajes(db){ return doc(db, "personajesJuego", "actual"); }

// Copia segura de las listas del documento. Un documento vacío o raro
// no rompe la instalación: lo que no sea arreglo se toma como vacío.
function listasDe(d){
  const o = (d && typeof d === "object") ? d : {};
  const out = {};
  LISTAS.forEach(k=>{ out[k] = Array.isArray(o[k]) ? o[k].slice() : []; });
  out.ESP = Array.isArray(o.ESP) ? o.ESP.slice() : [];
  return out;
}

// Un personaje instalado tiene EXACTAMENTE la forma que ya usa la app.
// No lleva `genero`: el lado se sabe por la lista en la que está.
function personajeDe(id, par, datos){
  const o = (datos && typeof datos === "object") ? datos : {};
  return {
    id: id,
    par: (par === null || par === undefined) ? null : par,
    personaje: String(o.personaje || "").trim(),
    situacion: String(o.situacion || ""),
    gancho: String(o.gancho || ""),
    derechos: String(o.derechos || ""),
    si_quieres: String(o.si_quieres || ""),
    imagen: String(o.imagen || "")
  };
}

// El siguiente id libre: el máximo de las cinco listas, más uno.
// Se usa `parseInt` porque hay datos viejos con ids numéricos y textos pegados.
function siguienteIdDe(listas){
  let max = 0;
  const ver = (p)=>{
    const n = parseInt(p && p.id, 10);
    if(!isNaN(n) && n > max) max = n;
  };
  LISTAS.forEach(k=>{ (listas[k] || []).forEach(ver); });
  (listas.ESP || []).forEach(t=>{ if(t && typeof t === "object") ver(t); });
  return max + 1;
}

// Compara textos sin mayúsculas ni acentos (para no repetir variantes).
function normTxt(t){
  return String(t == null ? "" : t).trim().toLowerCase()
    .normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

// Los packs que se pueden instalar: oficiales, activos, de personajes y
// con licencia válida para esta pareja. `oficialesAprobados()` es la fuente.
async function packsAInstalar(){
  try{
    const todos = await oficialesAprobados();
    return (todos || []).filter(p=> p && p.tipo === "personajes" && p.activo !== false);
  }catch(e){ return []; }
}

// Una transacción, con UN reintento si hay conflicto entre los dos teléfonos.
// Si vuelve a fallar, no se hace nada y se reintenta en la próxima apertura.
async function enTransaccion(db, trabajo){
  for(let intento = 0; intento < 2; intento++){
    try{ return await runTransaction(db, trabajo); }
    catch(e){ if(intento === 1) return null; }
  }
  return null;
}

// Instala UN pack desde cero en las listas dadas. Devuelve el título instalado
// o `null` si no instaló nada. Lo comparten la instalación automática y la
// reinstalación de un pack que todavía no estaba.
function instalarPackDesdeCero(pack, listas, previos, ids){
  const packId = pack && pack.id;
  // Los packs son siempre nuevos: si ya está instalado, se salta.
  if(!packId || previos[packId]) return null;

  const registro = { fecha: serverTimestamp(), pares: [], variantes: [] };
  let algunPar = false;

  (Array.isArray(pack.pares) ? pack.pares : []).forEach(par=>{
    const normal = par && par.normal;
    const contra = par && par.contraparte;
    const gn = String((normal && normal.genero) || "").toUpperCase();
    const gc = String((contra && contra.genero) || "").toUpperCase();
    // Un par incompleto o con géneros que no son opuestos se salta;
    // no rompe la instalación de los demás.
    if(!normal || !contra) return;
    if((gn !== "A" && gn !== "B") || (gc !== "A" && gc !== "B") || gn === gc) return;

    // A = masculino, B = femenino. El cruce es el que ya usa el juego:
    //   normal A -> U1, su contraparte -> C2
    //   normal B -> U2, su contraparte -> C1
    const listaU = (gn === "A") ? listas.U1 : listas.U2;
    const listaC = (gn === "A") ? listas.C2 : listas.C1;

    const idNormal = ids.siguiente++;
    const idContra = ids.siguiente++;
    listaU.push(personajeDe(idNormal, null, normal));
    listaC.push(personajeDe(idContra, idNormal, contra));
    registro.pares.push({ normalId: idNormal, contraparteId: idContra });
    algunPar = true;
  });

  // Un pack sin pares válidos no se instala.
  if(!algunPar) return null;

  // Variantes picantes: solo se agregan las que falten. Las que la pareja
  // agregó por su cuenta no se tocan.
  (Array.isArray(pack.variantes) ? pack.variantes : []).forEach(t=>{
    const s = String(t == null ? "" : t).trim();
    if(!s) return;
    if(listas.ESP.some(x=> normTxt(x) === normTxt(s))) return;
    listas.ESP.push(s);
    registro.variantes.push(s);
  });

  previos[packId] = registro;
  return pack.titulo || packId;
}

// Busca un personaje por id en las cuatro listas. Devuelve la lista y la
// posición, o `null`. Compara como texto: hay datos viejos con ids mezclados.
function buscarEnListas(listas, id){
  if(id === null || id === undefined) return null;
  for(let i = 0; i < LISTAS.length; i++){
    const clave = LISTAS[i];
    const j = (listas[clave] || []).findIndex(p=> p && String(p.id) === String(id));
    if(j >= 0) return { clave: clave, p: listas[clave][j] };
  }
  return null;
}

// Saca un personaje de donde esté. Se usa para moverlo a la lista que le toca.
function quitarDeListas(listas, p){
  LISTAS.forEach(k=>{
    const j = (listas[k] || []).indexOf(p);
    if(j >= 0) listas[k].splice(j, 1);
  });
}

// Las listas, el mapa y el contador, listos para escribir. Siempre escribe el
// documento completo de las listas con `merge` (conserva lo que no se toca).
function escribirPersonajes(tx, ref, listas, previos){
  tx.set(ref, {
    U1: listas.U1, U2: listas.U2, C1: listas.C1, C2: listas.C2,
    ESP: listas.ESP,
    packsInstalados: previos,
    actualizadoEn: serverTimestamp()
  }, { merge: true });
}

/**
 * Instala los packs de personajes que esta pareja tiene aprobados.
 * Solo se llama para perfiles base (nunca para invitados).
 * Devuelve `{ instalados: [títulos] }`; vacío si no había nada que hacer.
 */
export async function instalarPacksPersonajes(db){
  const res = { instalados: [] };
  const packs = await packsAInstalar();
  if(!packs.length) return res;   // sin packs no se escribe nada

  const salida = await enTransaccion(db, async (tx)=>{
    const ref = refPersonajes(db);
    const snap = await tx.get(ref);
    const d = snap.exists() ? snap.data() : {};
    const listas = listasDe(d);
    const previos = (d.packsInstalados && typeof d.packsInstalados === "object" && !Array.isArray(d.packsInstalados))
      ? Object.assign({}, d.packsInstalados) : {};
    const ids = { siguiente: siguienteIdDe(listas) };
    const titulos = [];

    packs.forEach(pack=>{
      const titulo = instalarPackDesdeCero(pack, listas, previos, ids);
      if(titulo) titulos.push(titulo);
    });

    if(!titulos.length) return { instalados: [] };   // nada nuevo: no se escribe

    escribirPersonajes(tx, ref, listas, previos);
    return { instalados: titulos };
  });

  return salida || res;
}

/**
 * Reinstala un pack ya instalado: restaura lo que la pareja editó, vuelve a
 * crear lo que borró y repara las parejas. NO toca los personajes que la
 * pareja agregó por su cuenta (esos no están en `packsInstalados`).
 * Si el pack no estaba instalado, hace la instalación completa.
 * Devuelve `{ restaurados, recreados, reparados }`.
 */
export async function reinstalarPackPersonajes(db, pack){
  const vacio = { restaurados: 0, recreados: 0, reparados: 0 };
  if(!pack || !pack.id) return vacio;

  const salida = await enTransaccion(db, async (tx)=>{
    const ref = refPersonajes(db);
    const snap = await tx.get(ref);
    const d = snap.exists() ? snap.data() : {};
    const listas = listasDe(d);
    const previos = (d.packsInstalados && typeof d.packsInstalados === "object" && !Array.isArray(d.packsInstalados))
      ? Object.assign({}, d.packsInstalados) : {};
    const ids = { siguiente: siguienteIdDe(listas) };
    const out = { restaurados: 0, recreados: 0, reparados: 0 };

    const registro = previos[pack.id];
    const slots = (registro && Array.isArray(registro.pares)) ? registro.pares : [];

    // Nunca se instaló (o el mapa quedó roto): se instala desde cero.
    if(!slots.length){
      if(registro) delete previos[pack.id];
      if(instalarPackDesdeCero(pack, listas, previos, ids)) escribirPersonajes(tx, ref, listas, previos);
      return out;
    }

    const pares = Array.isArray(pack.pares) ? pack.pares : [];
    // Solo los slots que ya existen: si el pack creció, los pares nuevos no se
    // instalan solos (regla 17.3). Lo que sobra se queda como está.
    const total = Math.min(slots.length, pares.length);

    for(let k = 0; k < total; k++){
      const normal = pares[k] && pares[k].normal;
      const contra = pares[k] && pares[k].contraparte;
      const gn = String((normal && normal.genero) || "").toUpperCase();
      const gc = String((contra && contra.genero) || "").toUpperCase();
      if(!normal || !contra) continue;
      if((gn !== "A" && gn !== "B") || (gc !== "A" && gc !== "B") || gn === gc) continue;

      const claveU = (gn === "A") ? "U1" : "U2";
      const claveC = (gn === "A") ? "C2" : "C1";
      const slot = slots[k] || {};

      // --- el original ---
      let hit = buscarEnListas(listas, slot.normalId);
      let idNormal;
      if(!hit){
        idNormal = ids.siguiente++;
        listas[claveU].push(personajeDe(idNormal, null, normal));
        out.recreados++;
      }else{
        idNormal = hit.p.id;
        if(hit.clave !== claveU){ quitarDeListas(listas, hit.p); listas[claveU].push(hit.p); }
        Object.assign(hit.p, personajeDe(idNormal, null, normal));
        out.restaurados++;
      }
      slot.normalId = idNormal;

      // --- su contraparte ---
      hit = buscarEnListas(listas, slot.contraparteId);
      // Si el id guardado apunta al propio original, ese dato no sirve: se
      // vuelve a crear la contraparte.
      if(!hit || String(slot.contraparteId) === String(idNormal)){
        const idContra = ids.siguiente++;
        listas[claveC].push(personajeDe(idContra, idNormal, contra));
        slot.contraparteId = idContra;
        out.recreados++;
      }else{
        const idContra = hit.p.id;
        if(hit.clave !== claveC){ quitarDeListas(listas, hit.p); listas[claveC].push(hit.p); }
        Object.assign(hit.p, personajeDe(idContra, idNormal, contra));
        slot.contraparteId = idContra;
        out.reparados++;
      }
      slots[k] = slot;
    }

    // Variantes: solo se agregan las que falten; las de la pareja no se tocan.
    (Array.isArray(pack.variantes) ? pack.variantes : []).forEach(t=>{
      const s = String(t == null ? "" : t).trim();
      if(!s) return;
      if(listas.ESP.some(x=> normTxt(x) === normTxt(s))) return;
      listas.ESP.push(s);
    });

    escribirPersonajes(tx, ref, listas, previos);
    return out;
  });

  return salida || vacio;
}

/**
 * Lee el mapa de slots instalados (`packsInstalados`) de la base de la pareja.
 * Nunca lanza: sin documento o sin conexión devuelve `{}`.
 */
export async function leerPacksInstalados(db){
  try{
    const sd = await getDoc(refPersonajes(db));
    const m = sd.exists() ? sd.data().packsInstalados : null;
    return (m && typeof m === "object" && !Array.isArray(m)) ? m : {};
  }catch(e){ return {}; }
}

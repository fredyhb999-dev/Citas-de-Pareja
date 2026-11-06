// ============================================================================
//  Cuadro de confirmacion — modulo reutilizable
// ----------------------------------------------------------------------------
//  Sustituye a la ventana del sistema (confirm/alert). Aquella era la UNICA
//  pantalla de la app que no usaba el diseno propio: salia la cajita gris del
//  navegador, con los botones del sistema, y se veia ajena al resto.
//
//      import { confirmar, aviso } from "../confirmar.js";
//
//      if(!await confirmar({
//        aviso:true,
//        titulo:"¿Eliminar a Mary?",
//        texto:"No se puede deshacer.",
//        ok:"Eliminar"
//      })) return;
//
//      await aviso("Sin conexión. Se jugará en este celular.");
//
//  Que acepta:
//    aviso  - true: circulito con ⚠️ arriba. Por omision false, para lo que da
//             algo y no borra.
//    titulo - la pregunta, en grande. Obligatorio.
//    texto  - la consecuencia, debajo, chiquita. Opcional.
//    ok     - el boton de adelante. Por omision "Aceptar".
//  El boton de atras siempre se llama "Cancelar".
//
//  Notas:
//   - El texto entra SIEMPRE con `textContent`, nunca con `innerHTML`: varios de
//     estos textos traen nombres, correos o accesorios que vienen de Firebase.
//   - Si después del aviso vas a navegar o cerrar una vista (`history.back()`,
//     `location.replace`, `ver(...)`), usa `await aviso(...)`: el aviso guarda un
//     paso del historial y, si no lo esperas, ese `history.back()` lo cierra de
//     inmediato (se ve como un parpadeo).
//   - Va en Z 95: encima de los modales normales (60) y de los fuegos (70).
//   - Si se pide otra confirmacion mientras esta abierta, la anterior se cierra
//     como "no": nunca quedan dos encimadas.
//   - Los colores se piden con `--card` y se caeen a `--tarjeta` (y asi con los
//     demas), porque cada pantalla les puso un nombre distinto y Diablitos usa la
//     otra serie.
// ============================================================================

const ESTILO = `
.cfCapa{ position:fixed; inset:0; z-index:95; background:rgba(0,0,0,.6);
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  padding:20px; }
.cfCaja{ width:100%; max-width:380px; text-align:center;
  background:var(--card, var(--tarjeta)); border:1px solid var(--teal);
  border-radius:16px; padding:22px 20px; }
.cfAviso{ width:44px; height:44px; border-radius:50%; margin:0 auto 12px;
  border:1px solid var(--coral); color:var(--coral);
  display:flex; align-items:center; justify-content:center; font-size:1.3rem; }
.cfTitulo{ font-family:'Chakra Petch',sans-serif; font-weight:700;
  font-size:1.1rem; line-height:1.4; color:var(--fg, var(--texto)); }
.cfTexto{ font-size:.85rem; line-height:1.5; margin-top:8px;
  color:var(--fg-muted, var(--apagado)); white-space:pre-line; }
.cfOk{ width:100%; margin-top:16px; padding:16px; margin-bottom:10px; border:none;
  border-radius:16px; cursor:pointer; font-family:'Chakra Petch',sans-serif;
  font-weight:700; font-size:1.05rem; color:var(--bg, var(--fondo));
  background:linear-gradient(90deg, var(--coral), var(--teal)); }
.cfOk:active, .cfNo:active{ transform:scale(.97); }
.cfNo{ width:100%; padding:12px; background:none; border:none; cursor:pointer;
  font-family:inherit; font-size:.9rem; text-decoration:underline;
  color:var(--fg-muted, var(--apagado)); }
`;

let estiloPuesto = false;
let capa = null;
let resolverActual = null;
// La confirmación guarda un paso del historial mientras está abierta: así el
// atrás la cierra y te deja donde estabas, en vez de salir de la pantalla.
let pasoAbierto = false;
let ignorarPop = false;

function ponerEstilo(){
  if(estiloPuesto || typeof document === "undefined") return;
  estiloPuesto = true;
  const e = document.createElement("style");
  e.textContent = ESTILO;
  document.head.appendChild(e);
}

function resolverComo(quanto){
  if(resolverActual){ const r = resolverActual; resolverActual = null; r(quanto); }
}
function quitarCapa(){
  if(capa){ capa.remove(); capa = null; }
}

function cerrar(quanto){
  resolverComo(quanto);
  quitarCapa();
  if(pasoAbierto){
    // Solo se deshace si el paso actual sigue siendo el de la confirmación. Si
    // la pantalla empujó otro encima, no se toca (sería deshacer algo ajeno).
    const esNuestro = !!(history.state && history.state.cf);
    pasoAbierto = false;
    if(esNuestro){
      ignorarPop = true;
      try{ history.back(); }catch(e){ ignorarPop = false; }
      // Si el back no llega (no había paso), no se queda tragándose el próximo.
      setTimeout(()=>{ ignorarPop = false; }, 400);
    }
  }
}

export function confirmar(op){
  return abrir(op || {}, true);
}

// Aviso sin pregunta: sale para decir UNA cosa, y no hay nada que cancelar.
// Adentro siempre va el circulito ⚠️. Acepta un texto suelto o {titulo, texto}.
export function aviso(op){
  const o = (typeof op === "string") ? { titulo: op } : (op || {});
  o.aviso = true;
  return abrir(o, false);
}

function abrir(o, conCancelar){
  ponerEstilo();
  // Nunca dos cajas encimadas: la que estaba abierta se cierra como "no" pero
  // se REUTILIZA el paso del historial (no se hace back ni se empuja otro).
  if(resolverActual){ resolverComo(false); quitarCapa(); }

  return new Promise((resolve)=>{
    resolverActual = resolve;

    const c = document.createElement("div");
    c.className = "cfCapa";

    const caja = document.createElement("div");
    caja.className = "cfCaja";

    // El circulito va DENTRO de la caja, arriba del titulo. Si se colgara como
    // hermano de la caja se pondrian de lado y la caja se iba a la derecha.
    if(o.aviso){
      const av = document.createElement("div");
      av.className = "cfAviso";
      av.textContent = "⚠️";
      caja.appendChild(av);
    }

    const t = document.createElement("div");
    t.className = "cfTitulo";
    t.textContent = o.titulo || "";
    caja.appendChild(t);

    if(o.texto){
      const x = document.createElement("div");
      x.className = "cfTexto";
      x.textContent = o.texto;
      caja.appendChild(x);
    }

    const si = document.createElement("button");
    si.type = "button";
    si.className = "cfOk";
    si.textContent = o.ok || (conCancelar ? "Aceptar" : "Entendido");
    si.onclick = ()=>cerrar(true);
    caja.appendChild(si);

    if(conCancelar){
      const no = document.createElement("button");
      no.type = "button";
      no.className = "cfNo";
      no.textContent = "Cancelar";
      no.onclick = ()=>cerrar(false);
      caja.appendChild(no);
    }

    c.appendChild(caja);
    document.body.appendChild(c);
    capa = c;
    // Paso del historial: el atrás cierra esta ventana en vez de salir de la
    // pantalla (nov-2026, lo reportó Fredy con el borrar de Citas).
    if(!pasoAbierto){
      try{ history.pushState({ cf:1 }, ""); pasoAbierto = true; }catch(e){ pasoAbierto = false; }
    }
  });
}

// El atrás cierra la confirmación y te deja donde estabas. Se registra al
// importar el módulo, antes del resto de la pantalla, para que su `popstate` no
// alcance a navegar la vista de abajo.
if(typeof window !== "undefined"){
  window.addEventListener("popstate", (e)=>{
    // Viene del `history.back()` de un botón: la caja ya se cerró, no toca nada.
    if(ignorarPop){
      ignorarPop = false;
      try{ e.stopImmediatePropagation(); }catch(x){}
      return;
    }
    if(!pasoAbierto) return;
    // El atrás ya deshizo el paso; solo hay que cerrar la caja como "no".
    pasoAbierto = false;
    resolverComo(false);
    quitarCapa();
    try{ e.stopImmediatePropagation(); }catch(x){}
  });
}
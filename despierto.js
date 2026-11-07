// despierto.js - evita que el celular apague o bloquee la pantalla mientras hay
// una partida en curso. Un solo lugar para todos los juegos.
//
// Se enciende al entrar a la partida y se suelta al salir, al terminar, al
// pausar o cuando la pestana deja de verse. El sistema suelta el permiso solo
// cuando la pagina se oculta, asi que al volver se pide otra vez.
//
// Si el navegador no tiene la funcion (Firefox viejo, iOS anterior a 16.4), no
// pasa nada: el juego sigue igual, solo que el celular puede apagarse solo.

let bloqueo = null;
let quiereDespierto = false;

function pedir(){
  if(!quiereDespierto) return;
  if(document.visibilityState !== "visible") return;
  if(!("wakeLock" in navigator)) return;
  if(bloqueo && !bloqueo.released) return;
  try{
    navigator.wakeLock.request("screen").then((b)=>{
      // Se apago mientras el sistema respondia: se suelta de inmediato.
      if(!quiereDespierto){ try{ b.release(); }catch(e){} return; }
      bloqueo = b;
      b.addEventListener("release", ()=>{ if(bloqueo === b) bloqueo = null; });
    }).catch(()=>{ bloqueo = null; });
  }catch(e){ bloqueo = null; }
}

// Encender: la partida esta en curso en este celular.
export function mantenerDespierto(){
  quiereDespierto = true;
  pedir();
}

// Apagar: se termino, se pauso o se salio de la partida.
export function soltarDespierto(){
  quiereDespierto = false;
  const b = bloqueo;
  bloqueo = null;
  if(b && !b.released){ try{ b.release(); }catch(e){} }
}

// La pestana se oculta: el sistema suelta el permiso. Al volver, se pide otra vez.
document.addEventListener("visibilitychange", ()=>{
  if(document.visibilityState === "visible") pedir();
});
// En Safari la peticion solo se acepta despues de un toque. Se reintenta en cada
// toque sin molestar: si ya esta encendido, pedir() sale de inmediato.
document.addEventListener("pointerdown", pedir, { passive:true });
document.addEventListener("touchstart", pedir, { passive:true });

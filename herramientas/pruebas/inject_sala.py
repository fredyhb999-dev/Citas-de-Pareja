import io, os

H = r"C:\Users\Fred\AppData\Local\Temp\opencode\harnes_sala"
p = os.path.join(H, "Diablitos", "index.html")
s = io.open(p, encoding="utf-8").read()

#Extend the mock firestore with a seed for the hall
mp = os.path.join(H, "mock", "firebase-firestore.js")
m = io.open(mp, encoding="utf-8").read()
m += r"""
(function sembrarInvitacionesSala(){
  if(typeof location === "undefined") return;
  var esc = (location.search.match(/esc=([a-z]+)/) || [])[1] || "";
  if(!/invitado|coninvitacion|pausada|expulsado|sesionmuerta|aviejada/.test(esc)) return;
  // La sala abre Firebase con el nombre "invitado" (invitado.js).
  var d = dbs["invitado"] || (dbs["invitado"] = { docs:new Map(), listeners:new Map(), log:[] });
  d.docs.set("config/ajustes", { usuarios: [
    { id:"m1", nombre:"Anfitrion", admin:true },
    { id:"u1", nombre:"Tio Beto", admin:false, invitado:true, conQuien:"m1" }
  ]});
  // La PARTIDA de verdad: el aviso solo vale si esta sigue activa.
  d.docs.set("sesionEncuentros/actual", {
    activa: (esc === "sesionmuerta") ? false : true,
    pausada: (esc === "pausada"),
    sid: "s1", largo: 3, ronda: 0, turno: 0,
    cabezas: [ { id:"m1", nombre:"Anfitrion", lado:"A", admin:true },
               { id:"u1", nombre:"Tio Beto", lado:"A", admin:false, invitado:true } ],
    orden: ["u1","m1"], listas: { m1: [], u1: [] }
  });
  if(esc !== "invitado"){
    var inv = {
      juego:"encuentros", titulo:"Encuentros Guiados", icono:"\uD83D\uDCAB", ruta:"Encuentros",
      hostUid:"m1", hostNombre:"Anfitrion", participantes:["u1"], activa:true,
      pausada: (esc === "pausada"), sesion:"sesionEncuentros/actual", sid:"s1"
    };
    // Aviso VIEJO: publicado cuando el campo "sesion" no existia. Es el caso
    // que le salio a Fredy al entrar de invitado.
    if(esc === "aviejada") delete inv.sesion;
    d.docs.set("invitaciones/encuentros", inv);
  }
})();
"""
io.open(mp, "w", encoding="utf-8", newline="\n").write(m)

DRIVER = r"""
<div id="SALIDA" style="position:fixed;left:0;top:0;right:0;z-index:9998;background:#111;color:#ff0;font:11px monospace;padding:6px;white-space:pre-wrap;max-height:70vh;overflow:auto"></div>
<script type="module">
import { retirarInvitacion } from "../invitado.js";
const ESC = (new URLSearchParams(location.search).get("esc")) || "nada";
function P(s){ __log(s); }
function __log(s){
  window.__salida = window.__salida || [];
  window.__salida.push(s);
  const d = document.getElementById("SALIDA");
  if(d) d.textContent = "[" + ESC + "]\n" + window.__salida.map(x=>"- " + x).join("\n") +
     (window.__errores && window.__errores.length ? "\n!! " + window.__errores.join("\n!! ") : "");
}
function dormir(ms){ return new Promise(r=>setTimeout(r, ms)); }
function vis(id){ const e=document.getElementById(id); if(!e) return "NOEXISTE"; return getComputedStyle(e).display === "none" ? "oculto" : "visible"; }
function T(id){ const e=document.getElementById(id); return e ? (e.textContent||"").trim() : "NOEXISTE"; }
function yo(){ try{ return JSON.parse(localStorage.getItem("appPareja_quienSoy")||"null"); }catch(e){ return null; } }
function proyecto(){ try{ return JSON.parse(localStorage.getItem("pareja_config")).firebase.projectId; }catch(e){ return "?"; } }
async function esperar(fn, ms, et){
  const t0 = Date.now();
  while(Date.now()-t0 < (ms||8000)){ let v=false; try{ v=fn(); }catch(e){} if(v) return true; await dormir(150); }
  P("   [TIMEOUT " + (et||"?") + "]"); return false;
}
(async ()=>{
  window.__errores = [];
  window.onerror = (m,s,l)=>window.__errores.push("onerror: "+m+" @"+l);
  window.addEventListener("unhandledrejection", e=>window.__errores.push("promesa: "+(e.reason&&e.reason.message||e.reason)));
  await dormir(2500);
  P("soy invitado? " + JSON.stringify(yo()) + " | proyecto=" + proyecto());
  P("el JUEGO arranco? hay diablitos en pantalla = " + (document.querySelectorAll(".diablo").length >= 0));
  P("engrane visible (no debe estar si eres invitado)? " + vis("engrane"));
  P("panel de la sala: " + vis("salaInv") + " | esperando=" + vis("salaEsperando") + " | carta=" + vis("salaCarta"));

  const esperandoTxt = T("salaEsperando");

  if(ESC === "nada"){
    P("NO soy invitado (vine por el menu):");
    P("  boton de regresar visible? " + vis("volverSala") + "  (debe estar visible)");
    P("  panel de la sala: " + vis("salaInv") + "  (debe estar oculto)");
    document.getElementById("volverSala").click();
    await dormir(600);
    P("  al apretarlo me mando al inicio? " + (window.__volvioAlInicio ? "si (bien)" : "NO  <-- mal"));
  }

  if(ESC === "invitado"){
    P("soy invitado, sin ninguna partida:");
    P("  texto='" + esperandoTxt + "'  carta=" + vis("salaCarta"));
    P("  boton de regresar: " + vis("volverSala") + "  (debe estar OCULTO: el invitado no sale)");
    P("  " + (esperandoTxt.indexOf("Esperando") === 0 && vis("salaCarta") === "oculto" && vis("volverSala") === "oculto" ? "OK" : "FALLA"));
  }

  if(ESC === "coninvitacion"){
    P("hay partida viva:");
    P("  carta=" + vis("salaCarta") + " titulo='" + T("salaTitulo") + "'");
    document.getElementById("salaIr").click();
    await dormir(600);
    P("  al apretar Entrar me lleva a: " + (window.__entrarEn || "(nada)"));
    P("  " + (window.__entrarEn === "Encuentros?entrar=1" ? "OK: va DIRECTO al juego (sin doble aviso)" : "FALLA"));
  }

  if(ESC === "pausada"){
    P("la partida sigue viva pero EN PAUSA:");
    P("  texto='" + esperandoTxt + "'  carta=" + vis("salaCarta") + " (debe estar oculta)");
    P("  " + (esperandoTxt.indexOf("pausa") >= 0 ? "OK: avisa que esta en pausa" : "FALLA: no avisa de la pausa"));
    await dormir(2500);
    P("  expulsado? " + (window.__expulsado ? "SI  <-- MAL: la pausa no es el fin" : "no (bien)"));
    P("  respaldo: " + (localStorage.getItem("invitado_respaldo") ? "sigue ahi (bien)" : "borrado  <-- MAL"));
  }

  if(ESC === "aviejada"){
    P("aviso VIEJO (sin poder comprobar que la partida viva):");
    P("  texto='" + esperandoTxt + "'  carta=" + vis("salaCarta") + "  (debe estar oculta)");
    await dormir(2500);
    P("  " + (vis("salaCarta") === "oculto" ? "OK: no le sale un aviso que no se puede comprobar" : "FALLA: le sale el aviso viejo"));
  }

  if(ESC === "sesionmuerta"){
    P("aviso VIEJO: el aviso existe pero la PARTIDA ya no esta activa:");
    P("  texto='" + esperandoTxt + "'  carta=" + vis("salaCarta") + "  (debe estar oculta)");
    await dormir(2500);
    P("  " + (vis("salaCarta") === "oculto" ? "OK: no le muestra un aviso de una partida que no existe" : "FALLA: le muestra el aviso viejo"));
  }

  if(ESC === "expulsado"){
    P("hay partida, se muestra: " + vis("salaCarta"));
    await dormir(2000);
    P("ahora se ACABA la partida (sesion activa:false)...");
    await retirarInvitacion("encuentros");
    await dormir(2500);
    P("  expulsion marcada? " + !!window.__expulsado);
    P("  respaldo? " + (localStorage.getItem("invitado_respaldo") ? "SI  <-- mal" : "borrado (bien)"));
    P("  proyecto=" + proyecto() + " (debe ser 'mia') yo=" + JSON.stringify(yo()));
  }

  P("__fin__ errores js: " + (window.__errores.length ? window.__errores.join(" || ") : "ninguno"));
  document.title = "LISTO";
})();
</script>
"""
s = s.replace("</body>", DRIVER + "\n</body>")
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("driver de la sala inyectado")
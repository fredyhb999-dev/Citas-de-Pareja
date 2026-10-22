### Los botones de anfitrion tienen que NACER ocultos (oct-2026)

**Lo que reporto Fredy:** jugando como la pareja, en `Opciones/` le aparecio el
boton de "Terminar Partida", lo apachaba y le salia *"Terminar la partida es
cosa del anfitrión"*. El candado hizo bien su trabajo (no termino nada), pero el
boton **no debia estar a la vista**.

**Por que se le quedaba pegado:** `btnTerminar`, `btnQR` y `btnTerminarPartida`
**no traian `style="display:none"` en el HTML**, a diferencia de `btnSaltar` y
`btnAgregarInv`, que si lo traen. O sea: dependian 100% de que se ejecutara
`mostrarBotonesAdmin()`... y ese refresco **solo corria al entrar** a la partida.
Dentro del juego, `pintarPaso()` solo refrescaba `btnSaltar`.

**El arreglo (dos partes, las dos hacen falta):**

1. Los tres botones **nacen con `display:none`**, igual que sus dos hermanos.
2. `pintarPaso()` ahora llama a `mostrarBotonesAdmin()` **en cada pasada**, al
   lado de donde ya refrescaba la sala. Va **antes** del corte `if(!jugando)`
   porque **al pausar los botones NO deben desaparecer**: al reanudar tienen
   que volver.

**Regla que sale de aqui:** un boton que depende de JavaScript para estar
oculto **tiene que nacer oculto en el HTML**. Si nace a la vista, hay un
instante —o una ruta entera— en que se ve aunque no deba. Y si su estado cambia
durante el juego, el refresco va **en la pasada que ya se corre en cada jugada**,
no solo al entrar.

**Donde se aplico (los 3 que lo tenian):** `Opciones/` y `Encuentros/`. En los
dos, los botones de anfitrion (`btnTerminar`, `btnTerminarPartida`, `btnQR`,
`btnSaltar`) ahora nacen con `display:none`, y `pintarPaso()` llama a
`mostrarBotonesAdmin()` en cada pasada.

**`Guiadas/` NO lo tenía, y no se tocó (a proposito).** Alli `btnTerminar`
("Terminar") **no tiene candado**: no hay `esAnfitrion()`, ni `mostrarBotonesAdmin()`,
ni sala, ni invitados. El `soyHost` que hay es una variable suelta dentro de la
escucha, que solo decide si se ofrece "Continuar cita anterior?" o "Unirme".
Es decir, ese boton **debe** verse siempre, para todos: esconderlo al nacer
habria sido un error. Esto viene de la decision de oct-2026 de no portar a
Guiadas el bloque de anfitrion/QR/sala. **Si alguna vez se le pone un candado de
anfitrion ahi, entonces si aplica la regla de nacer oculto.**
- **Juego nuevo "Elecciones Peligrosas" (`Opciones/`, oct-2026):** traído de
  "Juego Opciones". Es el "esto o aquello": se muestran 2 opciones y al elegir
  una se elimina (la otra sigue), hasta que a cada quien le queda 1. Los datos
  viven en **Firebase** (`opcionesJuego/actual` = `{A:[...], B:[...]}`), **nunca**
  en un JSON del repo (contenido íntimo + repo público). Listas por lado: A =
  administrador, B = pareja; los invitados heredan la lista de quien los invitó
  (`conQuien`). **Número de rondas** (campo principal): cada quien recibe esa
  cantidad de opciones al azar de su lista (sin repetir si alcanza; se permite
  repetir si no). Una ronda = cada jugador pasa una vez, en orden aleatorio. Se
  juegan **exactamente R rondas** (cada opción se consume; no queda nada y no se
  muestra resultado): en la última ronda cada quien quita su última opción y sale
  el aviso "La partida terminó". Modos (tres botones): "Jugar
  solo" (pregunta qué lista), "Jugar con Pareja" (tú + pareja) y "Multijugador"
  (con invitados); los dos últimos preguntan "Un solo Celular" / "Cada quien en
  el suyo" (sesión `sesionOpciones/actual` + invitaciones, igual que Encuentros).
  Engrane ⚙️ arriba-izquierda (solo admin) para editar las dos listas:
  **pestañas** por usuario, lista en **tabla** con scroll acotado y **buscador**,
  edición en línea, borrar (✕) a la derecha, y **pegar lista completa**. Al
  terminar, aviso a todos y regreso; invitados expulsados. Pausar/continuar/
  terminar/saltar turno/sacar invitados como Encuentros. Licencia: item
  **`opciones`**. En el catálogo (`packs`): ruta **`Opciones`**, sección
  **`experiencias`**. El mecanismo de **agregar invitado a media partida**
  (reutilizable para otros juegos) está documentado aparte en
  **`General/Invitado-a-media-partida.md`**.

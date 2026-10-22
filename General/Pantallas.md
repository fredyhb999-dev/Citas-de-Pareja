# Decisiones tomadas por pantalla

Movido de `General/GUIA.md`. Contiene las decisiones específicas de cada pantalla del proyecto.

---

## Decisiones tomadas (NO sobrescribir sin preguntar)

### Del proyecto Citas de Pareja

| Decision | Detalle |
|---|---|
| La app se manda desde GitHub Desktop | Fredy sube, espera 1-2 min (Pages) y prueba en incognito o `Ctrl+Shift+R` (`Cache-Control: max-age=600`) |
| Modo invitado sin salir de la app | Es una pantalla normal, no un modo aparte: el invitado **no puede registrarse** ni tiene menus que lo delaten |
| Al registrarse va directo a la sala | A `Diablitos/`, sin ventana de "Listo". Si el anfitrion aun no publico nada, ve "Esperando Invitacion..." |
| El invitado **no tiene salida** | Ni en la pantalla de espera ni durante la partida. Se queda hasta que termine |
| La pareja **no** se expulsa nunca por un corte de red | La salida automatica solo se aplica al abrir la app, no durante la partida |
| Al terminar, el invitado sale solo | Este o "Terminar Partida": mensaje, acepta, `salirModoInvitado()` |
| En toda la interfaz se dice **anfitrion** | No "administrador" |
| Aviso de fin solo en la transicion real | Exige `&& jugando`, para que un documento viejo no lo displays otra vez |
| **Al acabar una partida se prenden fuegos** | Modulo `fuegos.js` en la **raiz**. Sale en todos los modos (solo, pareja, multi, un celular o compartido) y tmbn si el anfitrion la termina. El aviso de fin **no** dice "La partida termino": dice "Gracias por jugar" y la pantalla se celebra con fuegos |
| El turno ajeno va en **recuadro** | Igual que en `Encuentros/` (`#actividadAhora`): fondo con degradado, borde, sombras y `border-radius:24px`. Por eso `#esperaTurno` se enciende con `display:"flex"` y **no** con `"block"**: si no, el estilo de linea manda y no se centra |
| **Panel de la sala** (`#salaPanel`) | Abajo de los botones. Izquierda **En la espera** = usuarios del grupo que NO estan en `cabezas`. Derecha **En el juego** = las cabezas de la partida. Se repinta en cada `pintarPaso()` y se apaga solo cuando ya no se esta jugando |
| **QR, "Agregar invitado" y panel: SOLO en Multijugador** | Regla en `modoAdmiteInvitados()` (`modoJuego === "multi"`), en `Opciones/`. En **Pareja** (de ahi en adelante, cada quien en el suyo o un solo celular) y en **Solo** NO se muestran: el encuentro es de los dos o de uno, no hay a quien meter. Da igual si se juega en un solo celular o compartido. Ojo: `modoJuego` **antes no se asignaba nunca** (se quedaba en `"multi"`); ahora `iniciar()` lo graba junto con `unCelular` |
| Invitar en **Encuentros** (oct-2026) | Copiado de `Opciones/`. Se agrego `<script>` de `qrcodejs`, `leerConfigGuardada` al import de `config.js`, modalQR + modalAgregar y `pintarSala()`. Sale en los **DOS** modos (`esAnfitrion()`), no solo en compartido. Ojo: las fichas del panel se llaman `.ficha`, **no** `.chip`, porque en este juego ya existe un `.chip` del editor |
| Botones de invitar en Encuentros | **Misma cuadricula 2x2 que `Opciones/`**: QR junto a "Pausar y Salir" y "Agregar invitado" junto a "Terminar Partida", con el panel de la sala debajo. Antes iban en una fila aparte y se veian distintos |
| **Hueco reservado de "Saltar turno"** (`.filaSaltar`) | Ese boton solo aparece cuando NO es tu turno. Sin el hueco reservado empujaba hacia abajo la fila 2x2 y el panel de la sala, y todo se encimaba. Va dentro de `<div class="filaSaltar">` con `min-height:44px`: el espacio esta siempre, Asi el layout no se mueve nunca |
| **"← Volver" de `Opciones/` va a `#juegos`** | El juego esta en el catalogo de **Juegos**, no de Experiencias: el enlace era `../index.html#experiencias` y abria "Experiencias en Pareja", que no es de donde se entro. El clic en `vistaConfig` sigue atrapado y regresa a `entrar()` |
| Fin de partida igual en los 3 juegos | `Encuentros/` y `Guiadas/` ahora importan `fuegos.js` y usan `encenderFuegos()`/`apagarFuegos()`, con `#modalFin` en `z-index:80` y `background:transparent` para que los fuegos (70) se vean. Todos dicen "¡Gracias por jugar!" + "Aceptar" (se quito la letrita "Toca la pantalla..."). **En `Guiadas/` el modal es NUEVO** (antes no existia: al ultimo paso solo volvia al inicio) y se creo **inline**, porque ese juego no tiene clase `.modal` |
| **El boton de silencio estaba tapado** | El aviso de fin es `z-index:80` y ocupa TODA la pantalla, y el boton de `fuegos.js` iba en `Z+1` (=71): quedaba debajo y no se podia oprimir. Arreglo en los dos lados: (1) el boton a `Z+20` (=90); (2) **`#modalFin` lleva `pointer-events:none` y `.caja` `pointer-events:auto`**, para que el fondo no se coma los toques y asi "tocar la pantalla" sirva en toda la superficie, no solo fuera del modal |
| Como se sabe que una cita TERMINO en `Guiadas/` | `avanzarSesion()` ahora escribe `terminada: (np >= lista.length)`. Sin esa bandera el `escucharSesion` no distinguia "se acabo" de una pausa o de "Terminar", y habria fuegos hasta al darle "Terminar". `mostrarPlayer()` reinicia `finMostrado`/`finEnLocal` para que una cita nueva vuelva a celebrar |
| **"Terminar" de `Guiadas/` no terminaba (arreglado oct-2026)** | Pasaba en los **DOS** modos y por el mismo motivo: "Terminar" no borraba el avance, solo salía de la cita. En compartido apagaba `activa`, pero `jugarDirecto()` al volver a la misma actividad ofrecía "¿Continuar?" mirando **solo** si quedaban pasos, **sin mirar `d.activa`**: daba igual que la cita estuviera terminada, y "Continuar" la resucitaba. En un solo celular era peor: ni siquiera apagaba nada, solo dejaba `guia_prog` ahi. En los dos se sentia como pausa. **Regla: si un documento tiene una bandera de "vivo", TODA consulta que lo use tiene que mirarla; y si un boton dice "terminar", tiene que borrar lo que deja el avance.** El arreglo: `!!d.activa && ...` en `tengoPendientes`, y `borrarProg()` en el "Terminar" de un solo celular |
| **Pausa, salto de turno y fin de cita en `Guiadas/` (oct-2026)** | En la cita compartida (`modoJuego === "compartido"`) hay tres botones, y el que antes decía "Terminar" ahora se mueve de nombre. Decisiones de Fredy, **no** las de `Encuentros/`, porque la dinamica es distinta (alla hay `cabezas` y anfitrion; aqui la lista ya esta armada): |

| Boton | Que hace | Solo sale |
|---|---|---|
| **"Pausar y Salir"** (antes decía "Terminar") | Deja la cita **viva** y se retoma donde iban. **Compartida:** escribe `pausada:true` + `pausadaPor:<nombre>` y la pareja **se queda esperando** (NO se apaga `activa`). **Un solo celular:** no hay nada que marcar, porque el avance ya se guarda en el cel con cada paso (`guardarProg()` → `guia_prog`), y al volver sale "¿Continuar?" | Siempre, en los dos modos |
| **"Saltar turno de X"** (`#btnSaltar`) | Avanza `paso` un paso **aunque no sea tu turno** (es la unica diferencia con `avanzarSesion()`). La accion del que se salta **se pierde**. Pregunta con `confirmar()` y usa transaccion, como el avance normal | Cuando **NO** es tu turno, y **lo pueden los DOS** (en `Encuentros/` solo el anfitrion) |
| **"Terminar"** / **"Terminar Partida"** (`#btnTerminarPartida`) | **Termina de verdad, no se retoma.** Compartida: `activa:false, terminada:true, pausada:false, porNombre:<quien>`; a la pareja le llega el fin diciendo **quien** lo termino y al aceptar sale a la lista de esta misma pantalla. Un solo celular: **borra el avance local** (`borrarProg()`). Siempre pregunta con `confirmar()` | Siempre, en los dos modos. El nombre cambia: "Terminar Partida" en compartido, "Terminar" en un solo celular |

| | |
|---|---|
| **En pausa no se puede entrar** | Igual que `Encuentros/`: `btnUnirme` avisa "X pausó la cita" y no mete a jugar. Si no, el que llega se metería y los dos a la vez. Quien puede reanudar es el que pausó: al volver a la actividad aparece "¿Continuar?" y `btnContinuar` escribe **`pausada:false`** |
| **Saltar turno avanza SIEMPRE el contador** | Si se saltara sin avanzar `paso`, la cita pediría un turno que nunca llega y **no terminaría nunca**. Es la misma trampa que se documentó en `Roles/`, pero aqui NO aplica lo de "quemar la carta": la dinamica es una lista de pasos ya armada, y lo que se pierde es la accion del turno saltado |
| **El nombre de quien pausa** | Se usa `pausadaPor`, **no** `hostNombre`: los dos pueden pausar, y el que espera puede ser el que inicio la cita |
| **Los dos botones nuevos NACEN ocultos** | `style="display:none"` en el HTML (regla de la casa) y `pintarPaso()` los enciende |
| **Al agregar un invitado en Encuentros** | Se cuela al **final** de `d.orden` y se le copia la lista del companero de su mismo lado. Dos razones: 1) `avanzarSesion()` avanza con `t+1 < d.cabezas.length`, asi que si se agrega a `cabezas` sin agregar a `orden` los indices se descuadran y `d.orden[d.turno]` sale `undefined`; 2) las acciones son las del encuentro y no hay de donde re-asortear sin romper el ritmo. `largo` **no** cambia: el invitado solo juega las rondas que faltaban |
| **Guiadas NO lleva nada de esto** (decision oct-2026) | Su sesion es `{lista:[{lado}], paso}`: una secuencia de pasos YA ARMADA con `paso` como indice. **No tiene `cabezas`, no importa `invitado.js` (no publica invitaciones) y no tiene `escucharGrupo()`.** Agregar a alguien a media partida obligaria a rehacer la lista entera y saltaria el turno de todos. Se decidio no portar QR/panel/"agregar invitado" ahi. **OJO: esto es solo lo de los INVITADOS. La pausa, el salto de turno y el fin de cita SI se agregaron (ver abajo)** |
| El selector de invitado solo muestra perfiles base | Nunca a otros invitados, para que no haya invitado-de-invitado |
| Sin caducidad por tiempo para el invitado | Si cierra la app, el chequeo no corre: el vencimiento nunca se aplicaria |
| La sala es **solo para invitados** | La pareja no la ve ni entra por su cuenta |
| Diablitos **sin candado**, fijo en el menu | Submenu **Juegos**, para todos |
| Se brinca al que ya no esta | En vez de parar la partida. Con el boton "Saltar turno" del anfitrion |
| Un aviso **solo vale si la partida vive** | La sala comprueba la sesion antes de mostrar nada |
| En pausa no se puede entrar, pero tampoco se expulsa | Se marca el aviso en pausa, no se retira |
| Entrar desde la sala es **directo** | `?entrar=1`; sin doble pregunta |
| "Inicio" en Diablitos **solo si no eres invitado** | El invitado sigue sin salida |
| Retos tiene **su propio submenú**, y **no** está en Experiencias | Antes estaba como tarjeta fija dentro de Experiencias y su submenú quedaba vacío (oct-2026) |
| El menu tiene **4 submenus** iguales: Experiencias, Juegos, Retos y **Comunicaciones** | Chat y Acompanante ya no son entradas sueltas, viven en Comunicaciones (oct-2026) |
| **Volver** siempre a la **derecha**, en toda la app | A la izquierda va el boton contextual de esa pantalla (oct-2026) |
| Retos: **Volver** a Retos especiales y **sin** "Cambiar usuario" | Igual que Citas. Se agrego `#extras` al arranque |
| Un aviso sin `sesion` **no se muestra** | Descarta los avisos publicados antes de existir el campo |
| El icono de Diablitos va **dibujado, no como emoji** | SVG en `SVG_DIABLITOS` (`index.html`). Se ve igual en todos los telefonos. Elegido por Fredy (oct-2026) |
| Su descripcion es `Diviertete picando diablitos traviesos` | Antes decia "la sala de espera", que era literal y comercialmente flojo |
| El boton de volver de un juego se llama **`Volver`** y va al submenu del que salio | Usa `#juegos` / `#experiencias`. Antes decia "Inicio" y se iba hasta el principio |
| El invitado **no ve la salida** en Encuentros | Se oculta siempre. Cumplía la regla de Fase 1 en todos lados menos ahí |
| El `Volver` de los submenus va **arriba a la derecha**, los tres | Clase `.volverSub`. Antes uno estaba a la izquierda y dos venian abajo |
| **Cambiar usuario** solo en **Usuarios**, arriba a la izquierda | Se quitó de `Citas/`: ya solo servia para pruebas |
| **Cambiar usuario** tiene **Volver** y al elegir regresa a **Usuarios** | Antes no se podia salir sin cambiar, y caia donde se le antojaba (oct-2026) |
| Los titulos con degradado llevan `width:fit-content` | Sin eso el color se reparte por toda la pantalla y se ve clarito |
| Los botones de esquina (engrane, carrito) son **solo del menu principal** | En submenus no salen. El engrane va arriba a la **izquierda** |
| **Los ejemplos usan los nombres de verdad**: la pareja es **Mary** y el administrador **Fredy** | Decisión de Fredy (17-oct-2026). En comentarios, en la documentación y en los textos de ejemplo se ponen esos dos nombres, no nombres inventados. **OJO: esto NO son datos de la app** — el nombre real de cada quien sale de la base (`nombreLado()` → `usuariosLista`), y el respaldo es el genérico `"Lado A"` / `"Lado B"`. No se hardcodea ningún nombre en el código |

### De la forma de trabajar

| Decision | Detalle |
|---|---|
| **No se toca el repo sin que Fredy lo pida** | Ni un archivo ni una línea sin pedido. Si el pedido no está claro, se pregunta antes de escribir; si se ve que falta otra cosa, se dice y se pregunta, no se resuelve de una con un cambio. Es la regla 0 de `AGENTS.md` (18-oct-2026) |
| Fredy decide, el modelo ejecuta | Si algo es decision de producto, **preguntar antes** de aplicar |
| Explicar antes de programar | En espanol claro y sin codigo para el usuario |
| No inventar reglas nuevas de Firestore | Se reutiliza la base y las reglas que ya funcionan |
| No tocar algo que no tenga que ver con el pedido | Cambios minimos y verificables |
| Documentar en este archivo | Es la unica memoria del proyecto |
| Verificar antes de decir "listo" | Pruebas automaticas y, cuando se puede, prueba real en el celular |

---

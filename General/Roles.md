- **Juego nuevo "Juego de Roles" (`Roles/`, oct-2026):** hijo de `Opciones/`
  (misma entrada por catálogo, misma licencia, mismos modos de jugar, mismas
  salas, mismos invitados, mismos botones). **Lo único que cambia es el turno:**
  en vez de dos opciones para escoger, **a cada quien le sale una tarjeta de
  personaje** (situación, atractivo, derechos, acción) que se **lee** y se pasa
  con **"Siguiente"**. No hay eliminación: cada quien recibe una tarjeta por
  ronda y las juega todas. El contenido vive en **Firebase**
  (`personajesJuego/actual` = `{U1,U2,C1,C2,ESP}`), **nunca** en un JSON del
  repo (contenido íntimo + repo público). La sesión es
  **`sesionRoles/actual`** y **no tiene `pares{}` ni `eliminadas{}`**: `listas{}`
  es la **cola de tarjetas que le faltan** a cada jugador, y cada elemento es el
objeto `personaje` completo. Modes: **Clásico** (sale de `U1`/`U2`), **Cambia
    de Bando** (sale de las contrapartes `C1`/`C2`), **Seleccionar** (la lista
    completa del lado, escogida a mano) y **Duelo de seducción** (lista de un solo
    lado, con su contraparte cruzada; ver abajo). **Variantes Picantes NO es un
    modo**: es un
    interruptor que se prende encima de cualquiera de los cuatro, con "¿cuántas
    veces?" (K, máximo una por ronda), y el sorteo se hace **una sola vez al
    arrancar** y se guarda en la sesión como `especiales[]`. La carta sale **boca
    abajo** y se revela al tocarla (tocar otra vez la tapa, para poder pasar el
   celular). **Ojo con dos
  campos parecidos:** `modoJuego` es **quiénes juega** (pareja/multi) y
`modoBase` es el modo del juego (normal/espejo/seleccionar/duelo). **Ojo con los
    nombres: lo que se ve y lo que se guarda NO son lo mismo.** En pantalla los
    modos son **Clásico / Cambia de Bando / Seleccionar / Duelo de seducción** y el
    interruptor es
    **Variantes Picantes**, pero en el código y en la base siguen siendo `normal` /
    `espejo` / `seleccionar` / `duelo` y `especial` / `especialK` / `especiales`. Los
   nombres se renombraron (oct-2026) **solo en el texto**: no se tocan los
   valores, o se rompen las partidas ya empezadas. Licencia: item
  **`roles`**. En el catálogo (`packs`): ruta **`Roles`**, sección
  **`juegos`**, y **sin** marcar `oficial` (el menú salta los `oficial:true`).
  **Anatomía y lados (nov-2026):** A = masculino y B = femenino, según la
  anatomía de cada perfil (no según quién administra). Con los dos en el mismo
  lado, el **Duelo** y **Cambia de Bando** usan al admin con los originales (U1 o
  U2) y al otro con la contraparte de la **misma** anatomía (C1 o C2), no la
  cruzada. El contenido guardado no se mueve.
  Engrane ⚙️ con **una pestaña por usuario** (no cinco): cada quien ve el lado
  de su anatomía y el administrador tiene un botón para ver el del otro; dentro, dos
sub-pestañas Personajes / Contrapartes; y una tercera, **Variantes Picantes**, que
es común. **El orden de la pantalla de inicio (decisión de Fredy, oct-2026;
     rediseño completo el 17-oct-2026):** arriba **Número de rondas**, luego la
     caja **"Elige Tu Modo de Juego"** (las cuatro pestañas en 2x2, con la
     descripción del modo debajo), **luego en medio el interruptor de
     Variantes Picantes**, y después **"¿Cómo vas a jugar hoy?"** con los **solo
    dos** botones —**Jugar con Pareja** y **Multijugador**, en el mismo
    renglón—. Abajo de todo el remate del engrane y, **debajo de él**, el botón
    del QR (el orden de esos dos se invirtió el 17-oct-2026: antes el QR iba
    primero). El detalle del modelo y de las tres
    colecciones está en **`General/Modelo-Datos.md`**, sección **1**, *Juegos y sesiones*.

  - **El rediseño de la pantalla de inicio de `Roles/` (17-oct-2026, aprobado por
    Fredy):** se armó primero en **una maqueta suelta fuera del repo** (una sola
    página con el CSS copiado, para ver y ajustar sin tocar la app) y después se
    pasó a `Roles/index.html`. Lo que quedó, todo con su regla en el CSS:
    - **"Número de rondas"** es una tarjeta de **la mitad de ancho, centrada**
      (`#cajaRondas`). **El input NO se encoge**: sigue al 100% de la tarjeta, así
      que el número se ve igual de ancho y lo compacto es el bloque.
    - **"Elige Tu Modo de juego"** juntada con la de arriba y más chica por
      dentro; los cuatro botones se quedaron como estaban (`padding:10px`,
      letra `.82rem`).
    - **Variantes Picantes perdió su recuadro** (ni tarjeta ni interruptor con
      borde) y **se movió a en medio**, entre el modo de juego y "¿Cómo vas a
      jugar hoy?" (antes iba al final, dentro de una caja). **Ojo con el texto,
      que se movió de lugar:** la frase **"Variantes Picantes, Te atreves ?"**
      **dejó de ser el título de arriba y pasó a ser la etiqueta del
      interruptor**, en coral. Ya **no existe** la frase "Ponle un toque
      personal a tu juego". El "¿Cuántas veces?" **ya no es un recuadro: es una
      ventana emergente** (ver la nota siguiente).
    - **"¿Cómo vas a jugar hoy?"** más chica, con los **botones más arriba**, y su
      **título más grande** (`1.1rem`). **Ojo: quedó más grande que los otros
      dos títulos de caja y eso NO es un descuido** — se dejó así porque a Fredy le
      gustó más así (se avisó y se dejó). Los otros dos siguen en su tamaño.
    - **"Diviértete más"** un poco más grande, **pero SOLO en la vista de
      inicio**: se puso `#vistaInicio p.desc`, porque **`p.desc` a secas es
      global** y esa misma clase la usan el engrane, la selección y la pantalla
      de continuar, que **no** se tocaron.
    - **Trampa de CSS que se pasó por alto y sigue ahí:** se quiso subir el
      espacio entre los cuatro botones de `gap:8px` a `12px` y **NO se aplicó**,
      porque la regla que manda es **`.tabs.tabsModos`** (dos clases) y le gana
      a un `.tabsModos` suelto. **Se dejó en 8px** porque es lo que se aprobó en
      la maqueta. Para cambiar esa separación hay que editar **`.tabs.tabsModos`**,
      no `.tabsModos`. Lo mismo aplica para cualquier ajuste de esa fila.

  - **El "¿Cuántas veces?" pasó a ser una VENTANA EMERGENTE (17-oct-2026).**
    Antes era un recuadro que se abría **debajo** del interruptor, y en el
    celular **la pantalla no cabía**: hubo que hacer un **ajuste de alto** (achicar
    las tres tarjetas, quitar relleno y juntar espacios, con los títulos pegados
    al borde de arriba de su tarjeta) **y de paso sacar ese recuadro**. Para
    volver a tocarlo:
    - La ventana es **`#modalEsp`** y usa el **molde `.modal .caja` de la app**
      (el mismo del formulario de personajes), **NO** un `confirmar()`: ese es de
      "¿sí o no?" y esto es un formulario. Se abre y se cierra con los
      **`abrirModal(id)` / `cerrarModal(id)` que ya existían** — no se redeclaran.
    - **`#inpEspecial` y `#espNota` se MOVIERON dentro de la ventana, no se
      duplicaron.** Por eso `especialK()` y `pintarEspecial()` no cambiaron de
      nombre ni de referencia. **Prohibido crear un segundo campo de K**: serían
      dos números que se pueden desincronizar.
    - **`Cancelar` es VOLVER ATRÁS**: apaga el interruptor y cierra la ventana,
      para no dejar prendido un modo al que nunca se le dijo cuántas veces.
      **Aceptar** solo cierra. Poner `.checked = false` a mano **no** dispara el
      evento `change`, así que no hay ciclo.
    - **El texto va HASTA ABAJO**, debajo de los dos botones, y los botones se
      van al fondo con **`margin-top:auto`** dentro de una caja en columna: así
      quedan pegados a la línea de abajo sin importar cuánto ocupe el texto.
    - **El aviso de "no tienes variantes" (`#espAviso`) NO se movió a la
      ventana**, y a propósito: habla de la configuración ("agrégalas en el
      engrane"), no de K, y tiene que verse sin abrir nada.
    - El texto de la nota pasó a **"En X de las Y rondas, alguien tendrá una
      sorpresa."** (antes decía "a alguien le toca una variante"). El aviso de
      `K > R` en coral se mantiene.

  - **Al acabar la partida se reinicia SOLO el interruptor de Variantes Picantes
    (decisión de Fredy, 17-oct-2026).** `reiniciarVariantes()` apaga la casilla y
    vuelve a poner "¿Cuántas veces?" en 1. Se llama en los **dos** caminos donde
    la partida se acabó de verdad: el **"Aceptar"** del fin y **"Terminar
    Partida"** del anfitrión.
    - **El número de rondas y el modo de juego NO se reinician**, a propósito: se
      dejan como estaban para poder volver a jugar igual de rápido la segunda vez.
      Antes de esto **no reiniciaba nada**; ahora es el único ajuste que sí vuelve
      a su valor inicial.
    - **OJO: NO va en "Pausar y Salir", y esa es la parte que no hay que
     -meter**: esa partida **se puede retomar** (`roles_partida_local`), así que la
      casilla tiene que seguir diciendo la verdad sobre lo que quedó guardado. Si
      se apagara ahí, al retomar se vería apagada **mientras el juego sí tiene
      variantes**, y el que jugara después creería que no. Ese desajuste es
      peor que el que se arregla.
    - Poner `.checked = false` a mano **no** dispara el evento `change`, así que
      no se abre la ventana sola. `reiniciarVariantes()` llama a `pintarEspecial()`
      al final, que es lo que limpia el aviso y el texto de la nota.

  > **PROBADO EN VIVO (Fredy, 17-oct-2026):** el rediseño de la pantalla de
  > inicio y la ventana de "¿Cuántas veces?" quedaron **subidos y probados en el
  > celular**: la pantalla ya **cabe sin bajar**, la ventana sale con el borde
  > turquesa y el texto abajo, **Aceptar** cierra y deja el interruptor prendido,
  > **Cancelar** apaga todo, y al arrancar la partida las variantes caen en las
  > rondas que se pusieron. **También probado en una partida COMPARTIDA con
  > invitados (Fredy, oct-2026):** el interruptor reparte las rondas en cada
  > teléfono.

**Los textos de los modos NO son instrucciones, son PERMISOS (decisión de Fredy,
  oct-2026) — no reescribirlos sin preguntar.** La pestaña dice el nombre y la
  descripción dice lo que el jugador gana: `Clásico` → *"Interpreta, Aprovecha y
  ......"* · `Cambia de Bando` → *"La Lealtad y las Intenciones Cambian de
  Bando"* · `Seleccionar` → *"Selecciona tus personajes favoritos."*
  · `Duelo de seducción` → *"Sensualidad contra Erotismo, Quién Ganará ?"*
  **Los puntos suspensivos de "Clásico" son intencionales y NO se completan:** la
  frase deja la puerta abierta para que cada quien la rellene con su imaginación.
  Por eso ahí **no** cabe una palabra como "Disfruta": es un verbo de
  *sentimiento*, dice qué hay que sentir al terminar y **topa** las opciones.
  `Interpreta` y `Aprovecha` son verbos de *permiso*: abren. **El criterio para
  estas descripciones es que ABRA, no que diga qué hacer ni qué sentir.** El
  subtítulo de la pantalla ("Diviértete más") y las etiquetas de cada tarjeta en
  la selección ("Normal" / "Contraparte") se dejan como están: no tienen nada que
ver con el nombre de los modos.

**Duelo de seducción: el cuarto modo de `Roles/` (construido 17-oct-2026).** Está
  en la misma caja de los otros tres, en **2x2** (dos pestañas arriba, dos abajo).
  Se reparte una lista de **un solo lado** y **de cada carta se toma su contraparte
  cruzada** (U1 → C2, U2 → C1); los personajes sin contraparte no cuentan ni se ven.
  El dueño de la lista juega los originales y el otro las contrapartes. Se juega en
  dos modalidades (**Turnos**, que es el motor de siempre, y **Juntos**, donde no
  hay turnos: la pareja juega al mismo tiempo y el anfitrión aprieta "Siguiente") y
  tiene **cuatro caminos** según se juegue con pareja o en multijugador, y en un
  celular o cada quien en el suyo. Lo que se guarda en la sesión: `modoBase:"duelo"`,
  `dueloLado`, `dueloModalidad` y **`dueloPares[]`** (las parejas en orden de
  ronda). En la pantalla de escogimiento del duelo **solo marca el anfitrión**
  (quien inicia la partida): la pareja y los invitados ven la lista y el
  contador, pero no marcan. Cualquiera de los dos puede iniciar, también el
  Duelo; el que inicia es el anfitrión. "Saltar
  turno" **no existe** en duelo. **El detalle completo de las cuatro ramas y del
  reparto está en la sección *Duelo de seducción: detalle*, más abajo en este
  mismo archivo.**

  **PROBADO EN VIVO (Fredy, oct-2026):** las **ocho combinaciones de la matriz** y
  los casos límite **ya se ejecutaron en el celular**. El Duelo **no** es solo
  código escrito: está verificado. Lo que se fue encontrando al probar está anotado
  como reglas más abajo.

---

## Duelo de seducción: detalle

### Qué es

Es un **cuarto modo de juego**, hermano de Clásico, Cambia de Bando y
Seleccionar, en la misma caja de los otros tres y en **2x2** (dos pestañas
arriba, dos abajo). La pestaña larga ("Duelo de seducción", 17 letras) sí cabe:
cada pestaña mide lo mismo, como ~150 puntos de ancho.

**En una frase:** se reparten R personajes de un solo lado y **de cada uno se
toma su contraparte cruzada** — el del médico contra la paciente, de verdad, no
dos cartas al azar.

**Los modos siguen siendo de uno en uno.** Solo uno puede estar activo: la
función que decide qué lista ve cada jugador los revisa uno por uno, y con dos
activos solo aplicaría el primero.

### El reparto

1. Se pregunta **de quién son las cartas**: un desplegable, **usuario 1 o
   usuario 2**.
2. Se reparten **R tarjetas** de esa lista.
3. De cada una se busca **su contraparte cruzada**: si se tomó de U1, su
   contraparte está en **C2**; si se tomó de U2, está en **C1**. Las dos colas
   se arman **en el mismo orden** de selección.
4. **Quien es dueño de la lista original juega los originales, y el otro juega
   las contrapartes.**

> **Recuerdo de las contrapartes:** el enlace es el campo **`par`**, no la lista.
> Con la instalación canónica, la contraparte de U1 queda en **C2** y la de U2 en
> **C1**. Ejemplo: el Doctor en U1, la Paciente en C2. Por eso, **la contraparte
> de un personaje tuyo se edita en la pestaña del otro.**

### La contraparte se busca por `par` (nov-2026)

`contraparteDe(id, lado, mismo)` conserva su firma, pero **ya no usa la lista ni el
modo**: busca el `par` en las cuatro listas y exige **exactamente una** contraparte
(si hay dos, es ambigua y el personaje no cuenta). También resuelve la dirección
inversa: si le pasan la contraparte, devuelve el original. Así sirven igual los datos
viejos (mismo lado) y los nuevos (cruzados).

- **Solo C1/C2 cuentan como contrapartes.** El `par` que traiga un personaje normal
  (U1/U2) es un dato viejo de alguna importación y se ignora: antes se contaba y
  marcaba parejas ambiguas.
- `poolsEspejoMismo()`, `listaDeCabezaPara()` y `selPoolDe()` ya **no usan `C<n>`
  fijo**: toman las contrapartes **por `par`** de las `U` del lado. Con la
  instalación canónica da lo mismo; con packs, manda el `par`.
- `avisosCorrespondencia()` comprueba con `contraparteDe` y avisa si un original no
  tiene exactamente una.
- `dueloMismoLado` **sigue existiendo, pero solo decide el reparto de roles** (el
  admin lleva los originales y el resto las contrapartes), no qué lista se usa.
- `contraDeRonda()` y `agregarInvitado()` usan **el mismo reparto** que
  `poolsDuelo()`.
- Una pareja **A+A o B+B real** juega **la mitad del pack que coincide con su
  lado**; no hay instalación especial, solo la búsqueda por `par`.

### Sin contraparte no cuenta (ni se ve)

Los personajes **sin contraparte asignada no entran al Duelo**: no salen en el
reparto **ni en la pantalla de selección**, simplemente no se ven. No se avisa
ni se bloquea la partida (decisión de Fredy, oct-2026).

Para que no parezca un error, al pie de la selección va una **nota discreta**:
*"¿No ves un personaje? Puede que todavía no tenga contraparte."*

La caja **"REVISAR CONTRAPARTES"** del engrane sigue siendo el lugar para verlos
y arreglarlos.

### El emparejamiento por ronda no lo controla la app

En **Pareja** el reparto conserva el mismo orden en los dos lados, así que la
carta original k y su contraparte k caen en la misma ronda.

En **Multijugador** la app solo reparte las cartas de cada lado entre sus
jugadores: **quién hace duelo con quién en cada ronda es dinámica del grupo, no
una regla de la app** (decisión de Fredy, oct-2026).

### El anfitrión arma y marca

El que **inicia la partida** es el anfitrión y es el que marca las tarjetas,
también en "cada quien en su celular", aunque el lado elegido sea el de la
pareja. Los demás solo ven. **Cualquiera de los dos usuarios puede iniciar** (no
es cosa solo del usuario `admin` de la app): el que inicia manda en esa partida.
(Decisión de Fredy, 17-oct-2026.)

### Siempre hay pantalla de escogimiento

Al elegir Duelo se pasa **siempre** por una pantalla de selección, como con
Seleccionar, pero es una distinta:

- La lista es **solo del lado elegido**, y **filtrada**: fuera los que no tienen
  contraparte.
- El anfitrión marca **tantas como rondas** haya.
- **Al marcar una, su contraparte se busca sola y el CONTADOR DEL OTRO LADO
  también sube.** Por eso los dos contadores **siempre van iguales** y nunca
  queda un "0" colgado.
- El otro lado **ve la lista entera y puede opinar** ("esa no, esa"), pero **no
  marca**.
- Se prende **"Jugar"** cuando el contador llega a R.

> **Los contadores no son dos números: son el mismo número.** Salen de la misma
> lista de R personajes escogidos, así que no se pueden desincronizar. Esa es
> también la regla de "todos listos": basta con que el contador llegue a R.

### "Tentación sin distinciones" (reparto alterno)

Además de marcar parejas a mano o con **"Sorpréndeme"**, la selección trae un
segundo atajo (decisión de Fredy, 17-oct-2026):

- **Ignora por completo** lo que se haya marcado.
- A **cada persona** (usuario 1 y sus invitados; usuario 2 y los suyos) le toca
  su propia mano de **R cartas al azar** tomadas de las de **su lado**: `U1+C1`
  para el lado 1, `U2+C2` para el lado 2.
- Las manos salen **distintas** entre compañeros de lado si alcanzan las cartas;
  si no alcanzan, **se permite repetir**.
- **No hay parejas** original/contraparte: por eso en este modo la carta **no
  muestra "contra ..."**.
- Sirve en **todas las combinaciones** menos **Multijugador + un celular**, donde
  el botón no se muestra.
- En **Juntos un celular** (solo Pareja) la carta de dos caras muestra **la de
  cada quien**: una cara es tu carta y la otra la del otro.
- En la sesión se guarda `dueloTentacion:true` y **no** se guarda `dueloPares`.

### Esperar a la pareja antes de arrancar

En **"cada quien en su celular"** el Duelo **no arranca** hasta que la otra parte
**entre**; mientras tanto, quien marca ve *"Esperando a que entre …"*. Si la
pareja no entra, al intentar arrancar se pregunta y el anfitrión puede
**"Comenzar igual"**. Se espera **solo a la pareja** (no a los invitados), y en
**"un solo celular"** no se espera a nadie.

Si alguien acepta **después** de que ya arrancó, entra **a la partida**, no a la
selección (arreglado el 17-oct-2026: antes caía en la pantalla de selección ya
muerta y quedaba atrapado).

### Las dos modalidades

Se pregunta **en la misma pantalla**, una debajo de otra, para que no se sienta
como dos pasos. Aparte del desplegable de usuario 1 / usuario 2.

**TURNOS — es el motor que ya existe.** Idéntico al juego de hoy: se sortea de
quién es el turno, esa persona ve su carta, la voltea, lee, actúa y aprieta
"Siguiente"; se vuelve a sortear entre los que quedan; así hasta acabar la ronda
y el juego. **No se escribió nada nuevo**: lo único que cambia es **qué lista se
reparte**.

**JUNTOS — este sí es nuevo.** La unidad ya no es el turno: **es la pareja**. Los
dos voltean, los dos juegan al mismo tiempo y **el anfitrión aprieta
"Siguiente"**. Por eso el "Siguiente" **no está bloqueado**: lo aprieta cuando
quiera.

**El indicador es de FASE, no de turno.** Tres estados, iguales en un celular y
en compartida:

| Fase | Lo que se ve |
|---|---|
| 1 | La carta tapada: **"Voltea tu carta"** |
| 2 | Ya se ve: **"Jugando"**, y el anfitrión tiene **"Siguiente"** |
| 3 | Los demás ven: **"Esperando a que el anfitrión avance"** |

Arriba va el progreso: **"Ronda 1 de 3"**.

> **La fase 1 no aplica en Juntos un solo celular.** La carta de dos caras no
> tiene tapa (ver *Rama 1*): abre mostrando una cara y se voltea para ver la
> contraparte.

> **Nadie mide si los demás ya voltearon.** El anfitrión avanza cuando le
> parece; instrumentarlo sería un contador extra que no hace falta.

**"Saltar turno" no existe en Duelo**, en ninguna de las dos modalidades
(decisión de Fredy, oct-2026): el botón se esconde, sin reemplazo. Si alguien
pierde la conexión, al anfitrión solo le queda **Terminar Partida**.

### Las cuatro ramas

| | **Un celular** | **Cada quien en su celular** |
|---|---|---|
| **Turnos** | Una carta, la del que está en turno. **Es el motor de siempre** | Una carta por persona, tapada, por turnos. **Es el motor de siempre** |
| **Juntos** | **Carta de dos caras.** Nuevo | Una carta por persona, todas se voltean al tiempo, avanza el anfitrión. **Nuevo** |

> **La carta de dos caras solo hace falta en UNA combinación:** Juntos en un solo
> celular. En todo lo demás el duelo se reduce a cambiar la lista que se reparte.

#### Rama 1 — Jugar con pareja, un solo celular

- **Cabezas:** solo usuario 1 y usuario 2. Sin invitados.
- **Preparación:** el anfitrión elige el lado (U1/U2) y la modalidad, y marca
  las R tarjetas en la pantalla de escogimiento.
- **Reparto:** los originales van al dueño del lado elegido; las contrapartes,
  al otro.
- **SIN** QR, **SIN** "Agregar invitado", **SIN** panel de sala: en Pareja no hay
  a quién meter ni a quién esperar.

**Juntos:**

- Una **carta de dos caras**: de un lado el original (U1 o U2), y al voltearla
  aparece su **contraparte cruzada** (C2 o C1). Es **un solo objeto** que se
  voltea; no son dos cartas ni las dos caras a la vez.
- Cada quien lee **su** cara: se ve el original, se juega, se voltea y se ve la
  contraparte del otro.
- **No hay reverso de misterio** (el de la marca): las dos caras son contenido.
  Por eso "sin tapa": aquí no hay nada que ocultar, ya se sabe que la
  contraparte es la del otro.
- El anfitrión aprieta **"Siguiente"** y viene la pareja siguiente.

**Turnos:**

- Arranca el anfitrión y se sortea el turno de los demás.
- Al que le toca se le muestra **su** cara de la carta; la voltea, lee, actúa y
  aprieta "Siguiente".
- Se vuelve a sortear entre los que quedan, hasta acabar la ronda.
- **Sin "Saltar turno"**, como en todas las ramas del Duelo.

#### Rama 2 — Jugar con pareja, cada quien en su celular

- **Cabezas:** usuario 1 y usuario 2.
- Se escribe la sesión en Firebase y se publica la invitación apuntando a
  **`sesionRoles/actual`**.
- **Cada quien recibe UNA sola carta normal y tapada**, la que le toca. No hay
  carta de dos caras: en compartida cada persona solo tiene un personaje.

**Turnos:** es **exactamente el juego de hoy** (sorteo, cada quien voltea su
carta, lee, actúa y aprieta "Siguiente"). No se toca nada.

**Juntos:** todos voltean **al mismo tiempo** y juegan; **el anfitrión aprieta
"Siguiente"** y en los dos teléfonos aparece la pareja siguiente. Los que no son
anfitriones ven "Esperando a que el anfitrión avance".

#### Rama 3 — Multijugador, un solo celular

- **Cabezas:** todos los usuarios, invitados incluidos.
- Cada invitado **pertenece** a usuario 1 o a usuario 2 (por `conQuien`), así que
  su carta sale de la lista del lado de su anfitrión.
- **Reparto:** los originales les tocan al dueño del lado elegido **y a sus
  invitados**; las contrapartes, al otro lado **y a los suyos**.
- **Aquí sí:** el anfitrión tiene **QR** y **"Agregar invitado"**, y sale el
  **panel de sala**.

**Juntos:** es una **sola carta de dos caras que ve todo el grupo**: aparece un
personaje, se muestra a todos; se voltea y aparece su contraparte, y también la
ven todos (decisión de Fredy, oct-2026). **No hay una carta por persona.** El
anfitrión aprieta "Siguiente".

**Turnos:** se sortea entre **todas** las cabezas; al que le toca se le muestra
su cara, la voltea, lee, actúa y aprieta "Siguiente". Cada quien actúa **una vez
por ronda**.

#### Rama 4 — Multijugador, cada quien en su celular

- **Cabezas:** todos, invitados incluidos; la invitación apunta a
  **`sesionRoles/actual`**.
- Un invitado que entra a media partida entra a partir de la ronda siguiente y
  se le agregan **las tarjetas que le falten del lado del usuario que lo
  invitó** (decisión de Fredy, oct-2026).

**Turnos:** **exactamente el juego de hoy**, entre todas las cabezas.

**Juntos:** cada persona recibe **una sola carta tapada**, la suya. Todos
voltean al mismo tiempo y juegan; **el anfitrión** aprieta "Siguiente" y a todos
les llega la pareja siguiente.

### Las variantes picantes

Entran como en los otros modos: se sortean **una sola vez al arrancar** entre
todos (usuarios e invitados), máximo una por ronda, y **solo le afectan a una
persona** (decisión de Fredy, oct-2026). La variante vive dentro de la carta de
esa persona: se ve en **su** cara. En la carta de dos caras (Juntos un celular)
sale en la cara de quien la tenga.

### Lo que se tocó, y lo que no

El Duelo **no reescribió el juego**: reutiliza el motor, el sorteo, las rondas,
las transacciones de Firebase, las invitaciones, la sala, el volteo de una carta
normal y el final con fuegos. Lo que hubo que construir fue:

1. **La pestaña y el 2x2.** Con un estilo nuevo (`tabs tabsModos`) que se le pone
   **solo** a la fila de modos: el estilo general de las pestañas se usa también
   en la selección, donde puede haber tres o cuatro jugadores y se verían
   torcidos.
2. **El reparto del Duelo**, una función propia: reparte una lista, busca la
   contraparte de cada carta y conserva el mismo orden en los dos lados (así la
   carta k y su contraparte k caen en la misma ronda).
3. **La pantalla de escogimiento del Duelo** (filtrada, con contadores derivados
   y solo el anfitrión marcando).
4. **La modalidad Juntos** (avance por parejas y el indicador de tres fases).
5. **La carta de dos caras**, solo para Juntos en un celular.

El botón de **"Saltar turno" solo se esconde** en Duelo: su código no se toca.

### El panel de sala (nota de mantenimiento)

El **panel de sala** (quién está en la espera y quién ya está jugando) sale en
**multijugador**, y **da igual si se juega en un solo celular o cada quien en el
suyo**. Eso viene de `modoAdmiteInvitados()`, que solo mira si el modo es `multi`,
y es la regla de la casa: en Pareja no se muestra.

Había un comentario en `Roles/index.html` que decía que el panel salía "solo en
partida compartida". **Ese comentario estaba viejo**: no era lo que hacía el
código y contradecía la regla. Ya se corrigió (oct-2026); solo era el texto, no
se cambió ningún comportamiento.

---

### Las reglas del juego que salieron de las pruebas en vivo

**Valen para los cuatro modos (Clásico, Cambia de Bando, Seleccionar y Duelo).
No romper:**

  - **Saltar turno QUEMA la tarjeta** de esa persona: pierde el turno *con*
    tarjeta. Si solo se le saltara el turno, la partida pediría turnos de más, la
    ronda se pasaría de R y **no terminaría**. Usa el mismo `avanzarTarjeta()` que
    "Siguiente", para que un salto y un paso normal no puedan comportarse distinto.
    (En **Duelo** el botón no existe, así que la regla no aplica.)
  - **No se puede dar "Siguiente" con la carta boca abajo.** El botón se ve
    apagado y, al tocarlo, sale un aviso discreto (*"Voltea la carta para poder
    seguir."*). No se **deshabilita**: un botón deshabilitado no avisa nada. **En el
    duelo *Juntos* esto NO aplica**: ahí el botón no se apaga, porque todos juegan
    al mismo tiempo y el anfitrión avanza cuando le parece.
  - **La carta del personaje tiene tope de alto** (`max-height:min(56dvh,520px)`):
    la foto es un banner 16/9 (no un cuadro) y lo que sobra de la info se desliza
    **dentro** de la carta, para que "Siguiente" quede siempre cerca. Es la misma
    carta en todos los modos de `Roles/` y en las dos caras del duelo. (17-oct-2026)
  - **El invitado no sale de la pantalla de selección**: se le oculta el "‹ Volver"
    y el botón atrás del celular queda bloqueado, igual que durante el juego.
  - **La pantalla de selección tiene buscador** (`#selBuscar`, 17-oct-2026):
    filtra la lista que se está viendo, sin mayúsculas y sin acentos ("jose"
    encuentra a "José"). Sirve igual para la selección normal y para la del
    Duelo, que comparten pantalla.
  - **El "Volver" de la pantalla de selección va ARRIBA A LA DERECHA**, no
    abajo: el botón de abajo (`#btnSelVolver`) se quedó en el código pero
    **oculto**, porque el enlace de arriba llama a su función para cancelar.
  - **En el Duelo hay dos atajos** (17-oct-2026), solo para quien inicia:
    - **"Sorpréndeme, elige por mí"** (`#btnSelAzar`): marca **R parejas al azar**
      (el orden al azar es el orden de las rondas), suben los dos contadores y se
      enciende "Jugar". Se puede repetir para re-sortear.
    - **"Tentación sin distinciones"** (`#btnSelTentacion`): **ignora lo marcado**
      y reparte a **cada persona** (usuario 1 y sus invitados; usuario 2 y los
      suyos) su propia mano de **R cartas al azar de `U+C` de su lado**, distintas
      entre compañeros si alcanzan y con repetición si no. **No hay parejas**, así
      que en este modo **no sale "contra ..."**. Sirve en todas las combinaciones
      **menos Multijugador + un celular** (ahí el botón no se muestra). En Juntos
      un celular (solo Pareja) la carta de dos caras muestra la de cada quien.
    Ninguno de los dos sale en la selección normal.
  - **"Sorpréndeme" también está en el modo "Seleccionar"** (17-oct-2026): marca
    **R tarjetas al azar de `U+C` de la lista que se está viendo**, distintas
    (el pool siempre alcanza). En **"cada quien"** cada teléfono solo lo hace en
    su propia lista; en **"un solo celular"**, en la pestaña que se esté viendo.
    "Tentación sin distinciones" sigue siendo solo del Duelo.
  - **El Duelo "cada quien" espera a la pareja** (17-oct-2026): no arranca hasta
    que la otra parte entra ("Esperando a que entre …"), y si no entra se puede
    **"Comenzar igual"**. Espera **solo a la pareja**, no a los invitados, y no
    aplica en "un solo celular". Si alguien acepta después de que ya arrancó,
    entra **a la partida**, no a la selección muerta.
  - **"Pausar y Salir" se puede retomar.** En **"cada quien en su celular"** la
    partida vive en `sesionRoles/actual`. En **"un solo celular"** se guarda en el
    propio teléfono (`localStorage`, clave `roles_partida_local`) y, al volver,
    sale "¿Continuar partida anterior?" con **Continuar / Partida nueva**. Esa
    copia local **no manda invitación ni se expone a nadie**, y se borra al
    empezar una partida nueva, al dar "Terminar Partida" o al aceptar el fin.
    (17-oct-2026)
  - **Limpieza de invitados al terminar (nov-2026):** el anfitrión quita de su
    lista a los invitados que jugaron con `retirarInvitadosDeUsuarios()`, tanto
    en el final natural como en "Terminar Partida". No depende de que el
    invitado acepte el aviso en su celular. La sala de `Diablitos` lo detecta
    con `vigilarMiFicha()` y lo saca, incluso en "un solo celular".
  - **La selección del Duelo en solo lectura** (la pareja y los invitados ven,
    no marcan) usa un **checkbox propio**: teal con check oscuro, también
    deshabilitado. El nativo pintaba el check blanco sobre blanco y no se veía.
  - **Invitado a media partida en Duelo/Juntos:** entra en la **misma ronda** que
    se está jugando y recibe la pareja actual + las que restan. En **Turnos**
    sigue entrando a la ronda siguiente (no tiene turno en la actual).
  - **Mensajes de fase del Duelo** (`#faseDuelo`) y el **"Toca para revelar el
    personaje"** del reverso van con letra más grande y degradado coral→turquesa.
  - **"Variantes Picantes, Te atreves ?"** (la etiqueta del interruptor de
    Variantes Picantes) va en **coral** (`var(--coral)`), para que resalte.
    **Antes esa frase era el título de la caja** y en coral decía "Ponle un toque
    personal a tu juego"; el 17-oct-2026 el interruptor se quedo sin recuadro, se
    movio a en medio y **las dos frases se intercambiaron de lugar**: ahora el
    titulo es la etiqueta y la frase en coral se fue.
  - **Arriba del reproductor del Duelo** va el **modo de juego y la modalidad**
    ("Pareja · Juntos" / "Multijugador · Turnos") y **debajo** "Ronda X de R".
    Antes estaba al revés y no decía Pareja/Multijugador.
  - **Cartas del Duelo:** debajo del personaje dicen **"contra [la contraparte]"**.
    En la carta de dos caras, cada cara muestra a la del otro. En los otros modos
    ese texto no sale. (17-oct-2026)
  - **El invitado también carga el contenido** (`cargarPersonajes()`); si no, su
    lista de selección sale **vacía**. Y no se dibuja la selección sin contenido
    (`asegurarPersonajes()`).
  - **"Pegar lista completa" valida la pestaña y puede reemplazar toda la lista**
    (nov-2026). Había pasado que se pegaron contrapartes en Personajes y no avisó
    nada. Ahora:
    - **El archivo dice de qué lista es** (`{"U1":[...]}`, ver *Exportar lista*).
      Si no coincide con la pestaña, **no pega nada** y dice cuál es y en cuál
      estás.
    - **Archivos viejos** (arreglo pelado, sin nombre): en **Personajes** se
      **bloquea** si algo trae `par` (son contrapartes); en **Contrapartes**,
      si **ninguno** trae `par`, **pregunta** antes de seguir.
    - **Casilla "Reemplazar toda la lista con lo pegado"**: apagada, solo agrega
      y salta los nombres que ya están. Encendida, la pestaña queda **exactamente**
      como el archivo: actualiza por **id**, agrega y **borra los que no vengan**.
      Antes de aplicar dice cuántos se borran, actualizan y agregan. Conserva los
      ids; si alguno choca con otra lista lo reasigna y avisa (las contrapartes se
      atan por id). Solo afecta a la pestaña visible. En **Variantes Picantes** la
      casilla no sale.
  - **"Pegar lista completa" es tolerante, pero NO adivina.** Acepta: un arreglo
    JSON, un objeto suelto, **un pedazo de arreglo sin los corchetes** (`{...}, {...},`
    — con o sin la coma final), el formato envuelto (`{"U1":[...]}`), **comillas
    tipográficas** (`“ ”`) y texto, uno por línea. Y si el JSON está **mal escrito,
    avisa y no pega nada**, con la **pista del navegador** (que trae **la línea y
    la columna** del error), para poder arreglarlo a mano. Antes, si el texto no
    empezaba con `[`, se caía a "un renglón = un personaje" **en silencio** y
    metía cada línea como un personaje, con todo el texto como nombre (le pasó a
    Fredy al pegar los personajes de un usuario en Contrapartes).
  - **"Exportar lista" descarga la lista que se está viendo (17-oct-2026).** Va
    **pareado con "Pegar lista completa"**, en la misma línea de dos botones al
    final del engrane (`#btnExportar`, función `exportarLista()`). **NO va en la
    esquina superior derecha**: ahí vive el "‹ Volver" y en toda la app hay **un
    solo botón por esquina** (ver `AGENTS.md`, regla 1f). Exporta **lo que se
    tiene seleccionado en ese momento** — la pestaña de usuario + la sub-pestaña
    (Personajes / Contrapartes), o **Variantes Picantes** — y en esa pestaña el
    texto se renombra solo ("Exportar variantes"). Tres reglas:
    - **Lo que se exporta es un objeto con el nombre de la lista adentro**
      (`{"U1":[...]}`), el mismo formato que acepta "Pegar lista completa": el
      archivo se puede volver a pegar tal cual y el pegado lo rechaza si se
      intenta meter en otra pestaña. Los archivos viejos de arreglo pelado se
      siguen aceptando.
    - **No le hace caso al buscador.** El buscador es para buscar, no para
      achicar un respaldo: si respetara el filtro, un archivo que dice "todos los
      personajes" podría salir con la mitad y nadie lo notaría.
    - El nombre del archivo sale del **nombre real del usuario**
      (`limpiarParaArchivo()` lo limpia de `/ \ : * ? " < > |` y le acorta los
      espacios, porque el nombre viene de la base y un `/` rompería la descarga;
      si queda vacío cae a `usuario1` / `usuario2`). Ejemplo:
      `roles-Fredy-personajes.json`.
    Con lista vacía **no baja nada**: avisa con `aviso()`.
  - **Las contrapartes van CRUZADAS** (decisión de Fredy, oct-2026): la lista de
    contrapartes de un usuario son las contrapartes de los personajes **del otro**.
    O sea, **`C1` ↔ `U2`** y **`C2` ↔ `U1`**. Por eso el desplegable "Contraparte
    de" de una contraparte de `C1` lista los personajes de `U2`, y los avisos de
    correspondencia van cruzados igual. *(Antes era del mismo dueño —`C1` ↔ `U1`— y
    estaba al revés; lo reportó Fredy jugando.)*
  - **Cada quien escoge solo de su lado**: en "cada quien en el suyo" el teléfono
    muestra **solo su pestaña** (y por eso solo puede escribir sus marcas); en "un
    solo celular" salen todas. El lado del invitado sale de `conQuien`.
  - **Mientras se escoge, el aviso de la sala apunta al documento de la
    SELECCIÓN** (`sesion:"seleccionRoles/actual"` **con el mismo `sid`**), no a la
    partida. Hace falta porque durante la selección **todavía no hay partida**, y
    la sala exige que el documento apuntado esté `activa`. Al cancelar se
    **retira** el aviso; al arrancar, lo reemplaza el de la partida. **Y quien
    acaba de escoger no recibe "¿Unirse?" otra vez** (`selYaEntre`): entra directo.
  - **El diseño de la carta vive en el código** (`Roles/index.html`, el CSS de
    `#tarjeta` y `#reverso`): no se copia aquí para que no se separe de la
    realidad. Lo que **no** se ve en el CSS: las etiquetas visibles son
    **SITUACIÓN / ATRACTIVO / DERECHOS / ACCIÓN** y los campos **no** se renombran
    (siguen siendo `situacion`, `gancho`, `derechos`, `si_quieres`); el **mosaico
    va solo en el reverso**; y el **emoji del remate va FUERA** del degradado,
    porque con `background-clip:text` el emoji también sale transparente. El bloque
    de la variante que va dentro de la carta se rotula **"Variante picante"**.
  - **La foto del personaje NO se vuelve a crear si la URL no cambió**
    (`pintarFotoEn()` la guarda en `data-foto`). Si se recreara en cada repintado,
    en el celular la carga se cancela y el `onerror` deja el marcador 🖼️ (en la PC
    carga tan rápido que no se nota). La foto va con **`object-fit:contain`**: se ve
    completa dentro del recuadro.
- **Trampa de la dirección de un juego (oct-2026) — costó dos rondas de
  diagnóstico:** los juegos importan los módulos de la raíz con `../acceso.js` y
  compañía. Eso **solo funciona si la dirección es la CARPETA** (`/Roles/`). Si se
  abre como `/Roles/index.html`, el `..` **no sube**: quita el nombre del archivo
  y se queda dentro de `/Roles/`, así que **los ocho imports dan 404, el módulo no
  carga y la pantalla queda en blanco con todos los botones muertos** — y **sin un
  solo error de JavaScript** (por eso no se veía la causa). La causa típica es el
  campo **`Ruta`** del pack mal escrito en el Panel: tiene que ser **`Roles`** a
  secas, **sin** diagonal y **sin** `index.html` (con `Roles/` el enlace queda
  `/Roles//`; con `Roles/index.html`, se abre el archivo). Un fallo de carga de
  módulo **no lo ve `window.onerror`**: hay que escuchar el `error` del elemento
  `<script>`.
- **El QR y el remate del engrane, en la pantalla de inicio (oct-2026):** en
  **`Roles/` y en `Opciones/`** la pantalla de inicio ahora trae, abajo de todo,
  un botón **"QR Invita a Alguien"** y el remate **"Personaliza tu experiencia
  en... ⚙️"** (que **abre el engrane de esa misma pantalla**). Sirve para
  registrar invitados **sin tener que entrar a la partida**. El QR es **una sola
  función** (`abrirQR()`), la usan el botón de adentro del juego y el del inicio:
  no está copiada. **"Agregar invitado" NO se puso ahí**: en el inicio todavía no
  hay partida, y los invitados ya registrados entran solos.
- **Y `Opciones/` tenía el mismo defecto del blanco (oct-2026):** esperaba a
  Firebase **antes** de pintar (`await cargarOpciones()`), así que la pantalla se
  quedaba vacía mientras cargaba. Se le aplicó el **mismo arreglo que a `Roles/`**:
  primero se pinta, después se carga, y se refresca sola. **`Opciones/` se agregó
  a `extract.py`** (no estaba: nunca se revisaba de sintaxis).
- **Quién puede iniciar partida (Encuentros y Elecciones Peligrosas, oct-2026):**
  la pantalla de inicio la ve **cualquier usuario que no sea invitado** (el
  administrador **y** la pareja), cada quien con su **propia identidad**. Antes
  solo el administrador la veía y a la pareja se la mandaba directo a la pantalla
  de espera (por eso "no podía entrar sola" en ninguno de los dos juegos). Los
  invitados siguen esperando la invitación. El **anfitrión** de cada partida es
  quien la inició (en compartida, `hostUid`): los botones de Pausar/Terminar/QR/
  Agregar invitado y "saltar turno" son de ese anfitrión (`esAnfitrion()`).
  `esAnfitrion()` es la bandera **`soyHost`** (se pone al iniciar o reanudar la
  partida, o al entrar a una que yo inicié) y **no** depende de `jugando`: si
  dependiera, al pausar se ocultarían los botones y no volverían al reanudar.
  El engrane de configuración (⚙️) lo tienen **los dos** (es su app en cada
  teléfono, aunque compartan datos); el "solo administrador" era para el control
  de invitados, no para la pareja.
## Diseño de la tarjeta de personaje (registro actual)

**Altura fija:** la tarjeta mide `min(56dvh, 520px)` de alto, para que el botón
"Siguiente" quede siempre cerca y no haya que bajar toda la pantalla. Lo que
sobra de la información se desliza **dentro** de la carta (`.info` tiene su
propio scroll).

**Foto del personaje:** es un banner 16/9 (no cuadrada), con `object-fit:contain`
para que se vea completa dentro del recuadro. En la esquina de la foto sale un
**dedo 👆 que pulsa** (solo cuando hay imagen): indica que se puede tocar para
ampliarla en la ventana emergente, sin tapar la imagen. Sin imagen no sale.

**Bloques de información:** SITUACIÓN / ATRACTIVO / DERECHOS / ACCIÓN (este
último con borde izquierdo teal). Los textos salen de Firebase y nunca se
usan `innerHTML` con datos de la base, solo `textContent`.

**Nombre:** con degradado coral→turquesa y `width:fit-content` para que el
degradado se vea entero.

**"contra [contraparte]":** debajo del nombre, solo sale en las cartas del
Duelo de seducción. En los otros modos el elemento nace oculto.

**Bloque "Variante picante":** solo se muestra si la ronda tiene una variante
especial asignada. Vive dentro de la carta, así se voltea con ella.

**Reverso:** la carta arranca boca abajo (reverso visible). Al tocarla se
revela. El reverso tiene el mismo tamaño que el frente (`visibility` y no
`display` para que el alto no salte).

**Volteo e imagen grande (igual en todos los modos):** al tocar la carta (boca
abajo ↔ boca arriba) se revela toda la información. Al tocar la foto con la
carta boca arriba se abre una **ventana emergente** (`modalImagenCarta`) con la
imagen del personaje a tamaño grande. Si se toca "Siguiente" con la carta
todavía boca abajo, sale el aviso discreto: "Voltea la carta para poder
seguir." (En el duelo *Juntos* el botón no se apaga: el anfitrión avanza cuando
le parece.)

**Estandarizado el 1-nov-2026:** antes "cada quien en su celular" usaba un
ciclo de 3 toques (reverso → solo imagen grande *dentro* de la carta → toda la
info). Ese paso intermedio se quitó: ahora la imagen grande se ve siempre en la
ventana emergente, en cualquier modo.

**Texto de estado debajo de la carta:** "Toca para revelar el personaje" (boca
abajo) y "Toca la foto para ampliar" (boca arriba), en todos los modos.

- **Un resumen de conversacion no lee estos archivos.** Si una sesion se corta
  por limite de tokens, lo que se pierde es el detalle fino. Este archivo es la
  red de seguridad: cualquier sesion nueva debe empezar leyendolo.

## Personajes oficiales y orden de las listas (nov-2026)

- Un personaje lleva el **🏅** (el mismo emoji pequeño de Guiadas y Encuentros) si
  su pack es **oficial, activo y con licencia válida**, y el personaje sigue
  **idéntico al del pack** en nombre, situación, gancho, derechos, si quieres e
  imagen. Si la pareja edita cualquiera de esos campos, deja de ser oficial; si lo
  restaura (o reinstala el pack), recupera el 🏅. Cambiar solo el enlace de pareja
  (`par`) no le quita el 🏅.
- No se guarda nada en el personaje: se calcula al mostrar con `packsInstalados` y
  el contenido del pack (de ahí la lectura en Roles).
- El 🏅 sale **solo en las listas**: engrane (Personajes y Contrapartes),
  Seleccionar, Duelo de seducción y el desplegable de contraparte. No va en la
  carta de la partida ni en el formulario de edición.
- Esas listas se ordenan **oficiales primero** y, dentro de cada grupo,
  **alfabético** sin distinguir mayúsculas ni acentos. Es solo orden de pantalla:
  la lista guardada no se reordena ni cambian los ids.

## Fotos: pasar los enlaces de una instalación a otra (nov-2026)

Herramienta de **mudanza**, no una función para clientes: pasa los **enlaces de las
fotos** de una base a otra en un solo paso, sin cuatro export y sin que la otra
persona tenga que importar cuatro archivos.

- **Se abre con CINCO toques seguidos** (a menos de 900 ms) en el rótulo
  **«SE ALGUIEN MAS...»** de arriba, y con otros cinco se cierra. El bloque
  (`#fotosBox`) **nace oculto** al final del engrane (regla 7) y trae tres botones:
  **Exportar fotos**, **Actualizar fotos** y **Deshacer la última actualización**
  (este último solo si hay algo que deshacer en ese teléfono).
- **El archivo es `Roles/fotos.json`**, con `{generado, fotos:[{lista, personaje,
  imagen}]}`. Lleva **solo** lista, nombre y enlace: nunca `situacion`, `gancho`,
  `derechos`, `si_quieres` ni ids (el repo es público).
- **Exportar** saca las **cuatro listas en un solo archivo** y solo los que tienen
  foto. Una foto quitada **no** se exporta vacía: en la otra base se queda la que
  tenía.
- **Actualizar** busca **por nombre dentro de su lista** (`U1`, `U2`, `C1`, `C2`),
  comparando sin mayúsculas ni acentos (el mismo `normSel()` del buscador). Cambia
  **solo `imagen`**: no toca textos, ids ni `par`, y no borra ni agrega. Si el nombre
  aparece dos veces en la lista, lo salta y lo cuenta.
- **Deshacer** guarda en el teléfono (`localStorage`, `roles_fotos_deshacer`) lo que
  cambió la última vez y **solo revierte lo que sigue igual** a como lo dejó la
  actualización: si alguien cambió una foto a mano después, esa se respeta. Un solo
  nivel; para volver adelante se pulsa «Actualizar fotos» otra vez.
- Si el teléfono **no tiene la base configurada** (`projectId` de plantilla), no
  hace nada y lo dice. Escribe con `runTransaction` sobre `personajesJuego/actual`
  para no pisar un cambio hecho al mismo tiempo.
- **PENDIENTE:** se quita antes de vender y con el cambio de arquitectura, junto con
  `Roles/fotos.json`. Ver `GUIA.md` → *Otros pendientes*.

## Galería de personajes (nov-2026)

Pantalla **solo para ver**: no edita, no agrega, no borra y no toca la base. Se
abre desde el botón **«Galería 👀»** de la pantalla de inicio, en el **mismo
renglón del QR** (el inicio ya está justo de alto).

- **Dos pestañas, una por lado**, con el nombre real de quien lo usa
  (`nombreDeLado`); si no hay nadie, «Sin usar».
- **Cada pestaña muestra los personajes de ese usuario y las contrapartes de SUS
  propios personajes:** lado A = `U1 + C2`, lado B = `U2 + C1` (el enlace real
  es `par`: `U1 ↔ C2`, `U2 ↔ C1`). **Ojo:** es distinto del engrane, que bajo el
  lado A muestra `C1` (las contrapartes que ese lado juega).
- **Cuadrícula de 2 por renglón**, con la foto completa (16/9) y el nombre
  debajo. Los que no tienen foto salen con 🖼️ y su nombre.
- **Color del nombre:** coral = personaje, turquesa = contraparte. Las
  contrapartes llevan además la etiqueta «Contraparte» y hay una leyenda debajo
  de las pestañas. No es solo color: la etiqueta lo dice con palabras.
- **Orden:** personajes primero, luego contrapartes; dentro de cada grupo,
  oficiales 🏅 y después alfabético (`ordenPersonajes`).
- **Reutiliza la ventana de imagen grande** (`#modalImagenCarta`), que se movió
  al nivel de la página para que funcione también fuera de la partida. Tocar la
  foto la abre y tocarla otra vez la cierra.
- **El invitado no la ve** (`abrirGaleria()` lo bloquea y su pantalla es la de
  espera). El «‹ Volver» regresa al inicio; es un paso real del historial.
- Si el contenido llega después de abrirla, la galería se repinta sola
  (`asegurarPersonajes()` y `pintarInicio()`).

# GUIA - Citas de Pareja (documento maestro)

**Aquí está lo que es cierto HOY y aplica a toda la app.**

El relato con fecha de cómo se llegó a cada cosa está en **`General/HISTORIA.md`**,
y solo se lee cuando la tarea toca esas áreas (la lista está en `AGENTS.md`).
**Si algo de `HISTORIA.md` contradice a este archivo, manda este archivo.**

## Cómo se usa

**Empieza por arriba.** Busca por **nombre**, no por número: el número solo ordena.

| | Sección | Qué hay |
|---|---|---|
| **1** | **Estado de las reglas de Firebase** | Cerradas el 6-oct-2026. **No inventar reglas nuevas** |
| **2** | **La base de cada PAREJA** | Reglas abiertas **a propósito**: no se tocan |
| **3** | **Pendientes, límites y mantenimiento** | Lo que falta y lo que ya se sabe que no se arregla |
| **4** | **Interfaz y navegación** | Medidas, «Volver», historial y submenús |
| **5** | **El contenido de fábrica** | Los JSON son solo el instalador |

**El detalle de una pantalla, un módulo o un juego no está aquí:** está en su
archivo de `General/`. **La tabla completa de documentos está en `AGENTS.md`.**

## Regla de escritura

- **Lo que rige hoy y aplica a toda la app** -> **aquí**.
- **El detalle de UNA pantalla o UN módulo** -> el archivo de esa pantalla.
- **El porqué de las cosas viejas** -> `General/HISTORIA.md`.
- **Acuerdos de trabajo y panorama de proyectos** ->
  `Documents\Default Project\General\GUIA-PROYECTOS.md`.
- Si algo aplica a dos sitios, va **una línea que apunta** al otro, nunca una copia.

**Regla para pantallas y módulos nuevos (obligatorio):** cuando se cree o modifique
una pantalla, un módulo o un juego, la documentación de detalle va **directamente a
su propio archivo en `General/`**, nunca aquí. En `GUIA.md` solo queda la línea de
apunte en la tabla de `AGENTS.md`.

Si algo empieza con "antes se hacía X" o lleva una fecha de hace meses, va a
`HISTORIA.md`. **Nunca** se agrega detalle de una pantalla o módulo dentro de este
archivo.

## La llave es el id, no el nombre

**Regla para todo lo que se construya de aquí en adelante.** Es la lección del
cambio de actividades por id (nov-2026): el nombre es una etiqueta que la pareja
cambia, así que **nunca** sirve para enlazar datos.

- **Cada colección nueva usa el id del documento como llave:** uno automático
  (`addDoc`) o uno fijo con significado (`A_2026-11-07`, `zona_pecho`).
- **Lo que apunta a otro guarda `<algo>Id`** (`zonaId`, `actividadId`, `duenoId`),
  nunca el nombre.
- **El nombre se guarda solo para mostrar.** Renombrar cambia únicamente el campo
  `nombre`; no se mueve ni se recrea ningún documento.
- **Para mostrar, se resuelve por id;** si no se encuentra (dato viejo o borrado),
  se cae al nombre guardado. El patrón es `leerDocActividad()` (`config.js`) y
  `nombreDeCita()` (`Citas/index.html`).
- **Las excepciones son tres, y hay que decir cuál se está usando:**
  - Texto libre que escribe la pareja y no apunta a nada: `retos.actividad`.
  - Copia del nombre **solo** para el texto de un aviso pasajero (`invitosFavor`,
    `invitosLenceria`, la sala de espera de `Diablitos`).
  - Historial de mensajes: `chat.autorNombre` y `presencia.nombre` guardan el nombre
    del momento a propósito (en el chat, quién lo dijo entonces).
- **Si una pantalla nueva guarda datos y no se puede decir cuál es la llave, se
  pregunta antes de escribir.**

## La anatomía define el contenido, no el administrador (nov-2026)

Cada perfil base guarda en `config/ajustes.usuarios` un campo **`anatomia`**:
`masculino` o `femenino`. **Masculino = lado A** y **femenino = lado B** en todo el
contenido (acciones, castigos, opciones, personajes, ropa…).

- **El administrador solo administra.** Quién es admin ya no decide qué contenido usa
  cada quien; cambiarlo no mueve el contenido.
- El ajuste está en la pantalla de **Usuarios**, en el renglón de cada perfil. No va
  en la ventana de «Editar nombres y administrador».
- Los **invitados eligen su anatomía al registrarse** y queda fija; si se equivocan,
  salen y vuelven a entrar.
- **Los dos pueden quedar en el mismo lado.** En ese caso los turnos y los planes van
  **por persona**, no por lado (Guiadas, Lencería y Citas).
- En las etiquetas se usan **nombres**, nunca la anatomía para identificar a una
  persona: el nombre, «Fulano y Mengano» si comparten lado, o «Sin usar».
- Los datos viejos sin `anatomia` se leen como antes: admin = masculino/A, pareja =
  femenino/B. Las partidas ya pausadas conservan los lados que tenían.
- **Al instalar un pack, la anatomía es obligatoria**: el asistente no guarda sin
  ella, y un perfil viejo sin anatomía muestra «Elige...» en Usuarios.

## Estado de las reglas de Firebase (cerrado y revisado)

**Las reglas de `solicitudes` están CERRADAS y fueron revisadas el 6-oct-2026.** Lo
que se cerró: nadie puede crear una solicitud con el correo de otro (era la forma de
"echar" a un cliente), y la lista de correos que publican ya no es pública.

**Sigue abierto a propósito:** `read` en `solicitudes`. El menú y los juegos leen esa
colección **sin internet y sin sesión**, así que cerrarla rompe el modo sin conexión.
Por eso los correos de los clientes son legibles. Es el trabajo pendiente, no un
descuido.

Todo lo demás de la Fase 1 (modo invitado, sala de espera, `Encuentros/`) está
**cerrado, verificado y probado por Fredy**. El relato está en `HISTORIA.md`,
Partes 1 y 2.

**Texto íntegro de las reglas vigentes y de las anteriores:**
`General/reglas-firebase-taquilla.txt`.

**Si alguien toca las reglas, hay que probar 4 cosas** (pedir, aprobar, revocar y el
Panel), y "pedir" con una cuenta que **no** sea publicador. La razón está en la
sección 5 de ese archivo.

### La base de cada PAREJA: reglas ABIERTAS a propósito (no tocar)

Los proyectos de cada pareja se instalan con `allow read, write: if true`
(`README.md`, paso 2). **Es una decisión, no un descuido, y no se cambia.**

**Por qué:** la app de la pareja **no inicia sesión** contra su propia base. Ninguna
página se autentica (el import de auth en `Guiadas/` está de adorno y no se usa). Sin
login, las reglas **no pueden** distinguir a nadie: cerrarlas rompe la app entera.

**La protección real (login + reglas por correo) llega con el rediseño de
arquitectura, DESPUÉS** de terminar y probar la app. Es un proyecto aparte, no un
cambio de reglas.

**Consecuencia que hay que saber:** quien tenga la configuración de una pareja (un
invitado, o quien escanee su QR) puede leer y escribir toda su base, incluidas las
actividades y el contenido personalizado. Lo único que la protege hoy es que la
configuración se comparte con gente de confianza.

**Lo que SÍ sería seguro, pero tampoco se hace sin preguntar:** limitar las reglas a
las 14 rutas que la app usa (`config/ajustes`, `nivelesActividad`,
`actividadesExtra`, `accesoriosExtra`, `presetsActividad`, `citas`, `retos`,
`puntosUsuarios`, `chat`, `presencia`, `invitaciones`, `sesionEncuentros`,
`sesionGuiada`, `propuestasPrecios`). Hoy está abierto "cualquier ruta". **Antes de
cerrar hay que completar la lista:** faltan las de Lencería y `config/fabrica`. Eso
**no** protege el contenido, solo cierra lo que no se usa.

**Si alguien -persona o modelo- propone cerrar estas reglas o ponerle candado a
`Citas/actividades.html`, que avise primero.**

### Reglas de `solicitudes`: qué sigue abierto y por qué

- `create` ya no acepta una solicitud con el correo de otro cliente: exige el correo
  verificado de quien pide.
- `config/permisos` ya no es legible por cualquiera.
- `read: if true` en `solicitudes` sigue abierto porque el menú y los juegos la leen
  **sin internet y sin sesión de Google**; cerrarla rompía el modo sin conexión.

**Cómo volver atrás:** el archivo de reglas tiene el texto vigente y el anterior
completo. Pegar el anterior y listo. **Cómo no romperlo:** probar las 4 cosas de la
sección 5.

**El trabajo de arquitectura que queda:** mover el correo del cliente a otra colección
(3 archivos: `Tienda`, `Autorizar`, `acceso.js`) y, más adelante, aislar cada cliente
en su propia ruta. Requiere el permiso de `borrar`, que hoy no está en las reglas.

### Estado de las revocaciones (oct-2026, verificado)

**Lo que YA funciona:** `escucharItem()` / `escucharCatalogo()` (`acceso.js`) están
conectados en **6 pantallas**: el menú, la tienda y los cuatro juegos con licencia
(`guiadas`, `encuentros`, `opciones`, `roles`). Cuando en `Autorizar/` se aprieta
**Revocar**, el documento viaja solo al celular: se borra el código local y el juego
**enseguida** muestra la pantalla de bloqueo, el menú quita la tarjeta y la tienda lo
desmarca. Sin que el cliente recargue nada.

**Los dos huecos, y por qué NO se arreglan hoy:**

| Hueco | Por qué no importa / por qué se espera |
|---|---|
| **Sin internet**, el código guardado en el celular sigue firmado y válido | **No es un hueco real: el juego NO se puede jugar sin internet.** Las opciones, los personajes y las acciones se leen de Firestore al jugar; en el celular no hay copia. Sin red no hay nada que jugar. |
| **Alguien a quien revocan puede seguir jugando hasta cerrar y reabrir la app** | Es el único que queda. Al reabrir, el menú lo bloquea. Se cierra en caliente cuando exista login (*La base de cada PAREJA*), y hoy no se toca. |

> **OJO, dato que NO hay que suponer (oct-2026):** el escuchador de revocaciones
> **solo se prende en la pantalla de BLOQUEO** (`escucharAprobacion()` se llama justo
> después de `ver("vistaBloqueo")`, en los cuatro juegos). **Una vez que entraste, no
> se queda vigilando.** No se debe decir "le salta al instante mientras juega": no es
> así.

### Pendientes de licencias — **EN ESPERA HASTA EL CAMBIO DE ARQUITECTURA**

> **Decisión de Fredy (oct-2026): estos CINCO pasos no se hacen ahora.** Casi todos
> cuelgan de la misma pregunta, "¿quién es cada quien?", y eso es exactamente lo que
> responde el cambio de arquitectura (login + reglas por correo). Hacerlos hoy sería
> tirar el trabajo a la basura:
> - El **código en el celular** desaparece cuando la licencia se consulta al servidor
>   con identidad real (pasos 3 y 5).
> - La **cola de solicitudes** deja de ser una colección pública de correos y pasa a
>   ser una lista de cuentas (pasos 1 y 4).
> - **La revocación en caliente** la resuelven las reglas, sin una verificación en cada
>   pantalla (paso 2).
>
> **El permiso de `borrar` en `solicitudes`** va aquí también: es para el rediseño de
> la cola. Es **manual, en la consola de Firebase**, y hay que probar las 4 cosas
> (pedir, aprobar, revocar, Panel), pidiendo con una cuenta que **no** sea publicador.

| # | Paso | Por qué espera |
|---|---|---|
| 1 | ~~Revisar las reglas de Firebase~~ **[HECHO: revisadas y cerradas. Ver `General/reglas-firebase-taquilla.txt`.]** | — |
| 2 | Revocación al entrar en cada página | La cierran las reglas del login |
| 3 | Catálogo marcando lo que ya tienes | Se consulta al servidor, no al celular |
| 4 | Cola con acuse + revocaciones persistentes | Necesita identidad real |
| 5 | Doc por ítem + cortesía a local | Se borra el almacén local del celular |

> **ANTES DE VENDER (oct-2026):** con la familia probando esto da igual, pero al
> vender ya no son conocidos y son clientes. **Hay que revisar el hueco de la
> revocación** (el de "sigue jugando hasta cerrar y reabrir"). No antes de vender:
> tampoco urge cambiar la arquitectura todavía.

### Otros pendientes

- **Reparto parejo en Multi (implementado oct-2026, pendiente prueba en vivo):** el
  reparto **en rueda** (tomar una acción de cada actividad por turnos hasta juntar las
  tomas, sin repetir hasta agotar el pool; la actividad con menos acciones aporta todo
  lo que tiene) ya lo usa el juego nuevo, y **Guiadas y Encuentros ya tienen el
  código** (reemplaza el mínimo de Guiadas y el pool proporcional de Encuentros).
  Guiadas ya tiene el paso de tomas de Encuentros. **Falta probarlo en vivo en los
  tres.**
- **Los saldos de puntos se siguen cambiando libres** (decisión de Fredy): el número
  de `puntosUsuarios/{id}` se ajusta sin que el otro acepte, que es lo que se usa para
  probar sin molestar. **No es un pendiente ni un descuido.** Se cierra con el
  rediseño de arquitectura; **no antes**.
- **Los 5 números del 🛒 ya NO son libres (nov-2026):** los precios de los deseos, el
  precio del Favor Express, el castigo y los minutos se **proponen** y el otro perfil
  base los **aprueba**. **Cada quien propone los suyos** (el 🛒 sale solo en tu fila).
  Mientras no haya acuerdo, los valores en uso no cambian.
  Detalle en `General/Propuestas-Precios.md`.
- Sesión de Encuentros en `sesionEncuentros/actual`: la lista de TODOS los
  participantes (incluidos invitados) vive en un solo documento. **Confirmar en la
  consola que ese path no queda abierto a lectura ajena.**
- **Quitar los botones de Exportar/Importar de la lencería ANTES DE VENDER.** Son una
  herramienta de mudanza entre la app de prueba y la personal; un cliente no los
  necesita y podría duplicar o pisar su base. Hoy viven al final de *Ajusta tus
  ilusiones y sueños*, sin candado. Ver `General/Catalogo-Lenceria.md`.

### Límites conocidos (no bloquean)

| Límite | Nota |
|---|---|
| Invitado apaga el celular o pierde red | Sigue en el turno. Mitigación: "Saltar turno" del anfitrión |
| **Sin internet**, el invitado no se expulsa al abrir | Deliberado: no se expulsa a nadie de una partida en curso por un corte de red |
| Invitado que nunca recibe invitación | Espera indefinidamente en la sala. Cerrar la app lo resuelve. Si el anfitrión quita su ficha (al terminar una partida), la sala lo saca sola (`vigilarMiFicha()`, nov-2026) |
| Escaneó y se salió | Se pierde el QR y hay que escanear de nuevo. Si **todavía no se ha jugado nada**, volver a escanear devuelve la misma ficha y sus puntos (oct-2026). **Si ya jugó y lo expulsaron**, vuelve como ficha nueva y en 0: el registro es temporal |
| Varios juegos con invitación a la vez | **Resuelto (oct-2026):** la sala muestra **una sola carta**, la **más reciente que se pueda entrar** (orden por `actualizadaEn`). Si la más reciente está **en pausa no gana**, para que el invitado no se quede sin poder entrar a ninguna |
| Datos viejos de "invitado de invitado" | No se limpian (ya estaba en pendientes) |
| El retorno del invitado se evalúa **solo en el inicio** | Si abre `Encuentros/` por link guardado, el chequeo no corre |
| Doble `getDocs` de `escucharCatalogo()` | No es bug, solo gasto extra |
| Una sesión vieja marcada `activa: true` sigue contando | El aviso nuevo sí se ata a la sesión, pero una partida vieja abierta no se autodetecta |

## Estándares de tamaño de la interfaz

**Regla: lo nuevo se copia de la pantalla inicial (`index.html`).** No se inventan
medidas ni se pregunta por ellas: ya están decididas.

| Qué | Medida |
|---|---|
| Ancho máximo del contenido | `max-width:380px` |
| Botón principal | `width:100%; padding:16px; border-radius:16px; margin-bottom:12px; font-size:1.05rem` |
| Botón secundario | `padding:12px` |
| Botón de icono (el circulito de arriba) | `font-size:1.6rem; padding:8px 10px; border-radius:12px` |
| Tarjeta de menú | `padding:24px 20px; border-radius:20px; margin-bottom:16px; gap:16px` |
| Icono de tarjeta | `2.4rem` en el menú, `2rem` en otras pantallas |
| Título de tarjeta | `1.25rem` en el menú, `1.1rem` en otras |
| Subtítulo de tarjeta | `.85rem` |
| Chevron de la tarjeta | `1.4rem` |
| Título de sección | `.8rem`, mayúsculas, con espacios entre letras |
| Radio de esquina | `12px` esquinas chicas, `16px` botones y tarjetas |
| Al tocarse | `transform: scale(.97)` |

**Lo que hay hoy (desorden heredado, no se arregla de golpe):**

| Archivo | Relleno | Redondeo |
|---|---|---|
| `index.html` `.btnUsuario` (pantalla inicial) | 16px | 16px |
| `Guiadas` `.btnPri` / `.btnAct` | 16px | 14px |
| `Guiadas` `.btnSec` | 12px | 14px |
| `Tienda` `.btn` | 13px | 12px |
| `Panel` `.btn` | 12px 18px | 12px |
| `Panel/catalogo` `.btn` | 12px 14px | 12px |

Unificar los viejos es trabajo aparte, pantalla por pantalla, porque requiere verlos.
**Lo que sí se aplica desde ya: todo lo nuevo usa la tabla.**

### Dónde va cada «Volver»

**Todos a la derecha, fijos y con fondo.** Dicen **`‹ Volver`**, van en la esquina
superior derecha y **no se van con el scroll**.

| Pantalla | Detalle de hoy |
|---|---|
| Encuentros, Guiadas, Diablitos | Derecha. Diablitos a 20px y con `env(safe-area-inset-top)` |
| Citas y Retos | Derecha, **flotando**: salieron del encabezado |
| Tienda (Experiencias/Juegos/Extras) | `#btnCasa` contextual: en una sección vuelve al Centro; en el Centro, al menú. Se quitó el enlace de texto «‹ Centro de Adquisiciones» |
| Chat y Acompañante | El encabezado no se desplaza (solo la lista de mensajes), así que ya quedaban quietos |
| Panel | «Entrar con Google» pasó a la izquierda. En el Catálogo el «‹ Volver» es contextual: dentro de una sección regresa a la lista de secciones, y en la lista sale al menú del Panel. Ahí **el atrás del celular hace lo mismo** (cada sección es un paso real del historial, como en `Castigos/`) |

**A la izquierda va el botón contextual** de cada pantalla: el engrane, "Jugar",
"Configurar". En Guiadas funcionan bien porque **nunca salen dos juntos**: `#btnCfg`
solo en `vistaLista`, `#btnAtras` solo en `vistaConfig`, `#btnAtrasEd` solo en
`vistaEditar`.

### Navegación con el botón atrás

**Regla de fondo:** una pantalla que se apaga y enciende **sin cambiar la dirección**
es invisible para el historial. Si el atrás del celular tiene que hacer algo, hay que
**guardar el paso** (`pushState`); y si la pantalla llega por un enlace, hay que
distinguir ese paso de los guardados a mano (`fijo`).

Un submenú abierto **es** un paso real del historial, guardado con `pushState` y
deshecho con `history.back()`. Así el atrás del celular y el «‹ Volver» hacen **lo
mismo**, y "adelante" también sirve.

| Pieza | Qué hace |
|---|---|
| `verMenu()` | El menú principal + sus dos botones de la esquina. **Nueva**: la necesitaban tres caminos (`mostrarMenu`, el «‹ Volver» y el `popstate`) |
| `hashActual()` | Lee el `#` normalizado (`#extras` -> `retos`) |
| `abrirSegunHash(h)` | Abre el submenú que diga el `#`, o el menú si no dice ninguno |
| `abrirSub(h)` | El botón del submenú: `pushState({sub:id}, "", "#"+id)` y lo muestra |
| `cerrarSub()` | El «‹ Volver»: `history.back()`. Si el paso **no** es nuestro (se llegó por el «Volver» de un juego o por la dirección escrita a mano), quita el `#` a mano en vez de saltar de vuelta a la partida |
| `popstate` | Obedece al historial en vez de adivinar por el `#` |

**El paso "fijo":** al entrar por un enlace (`../index.html#retos` desde
`Retos/index.html`) esa entrada **no la guardamos nosotros**. Por eso `mostrarMenu()`
la marca con `{sub:h, fijo:true}`: así el «‹ Volver» del submenú **cierra aquí** y no
devuelve al usuario a la partida de donde vino.

**Sin parpadeo al entrar/salir de un submenú (nov-2026):** no se vuelve a dibujar el
menú (`renderPacks()`) en cada transición, porque redibujarlo vaciaba la lista
mientras se consultaba Firestore y en el atrás se llamaba dos veces (`popstate` +
`hashchange`). Ahora solo se actualiza el punto del carrito
(`actualizarPuntoCarrito()`). El menú se redibuja al arrancar y cuando cambia el
catálogo (`escucharCatalogo`).

**Lo que rige en todas las pantallas (nov-2026):**

- **Solo Configuración se reabre desde el historial.** El editor de actividades
  (Encuentros/Guiadas) no se reabre con atrás/adelante: mostraría datos viejos. Si el
  paso deshecho es la misma pantalla que ya se está viendo, se sigue deshaciendo.
- **Durante la partida no se sale con el atrás** en Encuentros, Guiadas, Opciones,
  Roles ni Castigos.
- **El invitado nunca ve la pantalla del anfitrión con el atrás:** cae en la sala de
  espera, como en Roles.
- **Diablitos:** la configuración (⚙️) es un paso del historial, así que el atrás la
  cierra en vez de sacarte del juego.
- **El «‹ Volver» que sale al menú deshace los pasos de esa pantalla**
  (`salirAlMenu()`), en vez de abrir otra copia del menú. Si la pantalla se abrió
  directa, cae a su dirección fija.
- **Menú -> Cambiar usuario:** el paso "cambiar" se deshace antes de recargar la app.
- En `Retos/centro.html`, `navTienda` guarda su paso (`ver("vistaCatalogo")` sin el
  `false`) y al salir por el enlace se hace `replaceState` con la vista que se ve.

### Comunicaciones: el cuarto submenú (hechos de hoy)

Los cuatro menús son iguales: **Experiencias en Pareja**, **Juegos**, **Retos** y
**Comunicaciones** 💬. El botón va **al final**, con la descripción "Chatea en vivo y
algo más", y dentro la pantalla se llama **"Comunicación y algo más 😉"**.

Chat y Acompañante tienen su «Volver» y van a `#com`, como todos los demás. Las
piezas son `#btnCom`, `#vistaCom`, `abrirCom()` / `cerrarCom()` y el hash `#com`.

Los títulos de los submenús van **centrados** (`.subTitulo{ text-align:center }`).
`#btnCom` **nace visible** y `renderPacksDeVerdad()` no lo toca: un submenú con
tarjetas escritas a mano no puede depender del catálogo para que su botón aparezca.

> La campana, el bip y el cartelito del Chat y de los Retos están en
> **`General/Campana-Pestana.md`**.

### Degradado en los títulos

Los `h1` llevan `width:fit-content`. Sin eso la caja ocupa todo el ancho y el
degradado de 90° solo pinta una franja sobre las letras, que se ve clara y sin color.

### Botones de volver y de esquina

El estándar está arriba y en `AGENTS.md`.

En `index.html` los submenús se abren con funciones (`abrirJuegos()`,
`cerrarExp()`, …) y **no** con `onclick` en línea: al arrancar se comprueba
`location.hash` y se llama a la misma función, que podría no encontrar el manejador
todavía. Con `#juegos` el submenú de Juegos se abre directo al volver de un juego.

## El contenido de fábrica: los JSON son SOLO el instalador

`Citas/actividades.json` y `Citas/accesorios.json` **no se mezclan con lo de la pareja
en cada carga**. **Ahora los JSON son solo el instalador:** la primera vez, `config.js`
los copia a la base y a partir de ahí **manda la base**: todo, también lo de fábrica,
se renombra y se borra de verdad.

- `asegurarFabrica(db, {actividades, accesorios})` vive en `config.js`. Corre en las 5
  pantallas: `Citas/actividades.html`, `Citas/accesorios.html`, `Citas/index.html`,
  `Guiadas/index.html`, `Encuentros/index.html`. Las 5 leen **los dos** JSON, porque
  corre una sola vez y la que abra primero debe sembrar todo.
- La banderita es el doc **`config/fabrica`** y guarda **qué nombres** ya se
  instalaron. Por eso **lo que borras no vuelve** y **una actividad nueva que agregues
  después al JSON sí entra**.
- Si no se puede escribir (reglas cerradas o sin conexión) devuelve `false` y cada
  pantalla conserva el JSON como lista de respaldo: se ve igual de antes, no se rompe.
- `unirConFabrica(base, fabrica)` solo se usa en ese caso de respaldo.
- Los presets `<Actividad>.json` siguen siendo respaldo de `presetsActividad` (mismo
  patrón que `usuarios.json`). Si el nombre cambia, el JSON ya no aplica.
- El JSON también es el **respaldo**: no lo borres.

Al agregar o quitar algo del JSON de fábrica hay que subir `VERSION_FABRICA` en
`config.js`, o las instalaciones nuevas no lo reciben.

## Notas de mantenimiento

- **No hay `firestore.rules` en el repo:** las reglas viven en la consola de Firebase.
  "Revisar las reglas" es siempre una acción manual.
- **Verificación:** lo único automático es el **chequeo de sintaxis** en
  `herramientas/sintaxis/` (`python revisar.py`); el resto se prueba **en vivo**.
- **Acentos duplicados / caracteres CJK:** señal de doble conversión (UTF-8 guardado
  como Windows-1252 y vuelto a guardar). No se arregla a mano. El relato está en
  `HISTORIA.md`.

## Documentos de detalle

**La tabla completa (qué es cada documento y cuándo se lee) está en `AGENTS.md`.**
Aquí no se repite: una lista corta siempre se queda vieja.

> **Regla:** si lo que se toca es el detalle de una pantalla o un módulo, se lee
> **ese** archivo. Si es una regla general, es este. Lo que va en uno de esos archivos
> **no** se copia aquí: solo la línea que apunta.

**Packs de personajes:** un ítem del catálogo puede instalar sus personajes en las
listas de la pareja. Detalle en `General/Packs-Personajes.md`.

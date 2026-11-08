# AGENTS.md - Citas de Pareja

## Antes de hacer cualquier cosa

**Lee `General/GUIA.md`.** Es el documento maestro: lo que es cierto hoy y aplica a
toda la app.

**Si la tarea toca una pantalla, un módulo o un juego concreto, lee SOLO su archivo
de detalle** (tabla de abajo). Ese archivo se lee entero o no se lee.

**`General/HISTORIA.md` no se lee** salvo que la tarea caiga en la lista de abajo.
Es el diario: cuenta cómo se llegó a lo de hoy, no lo que manda. Si contradice a
`GUIA.md`, **manda `GUIA.md`**.

## Los documentos, y cuándo se lee cada uno

| Documento | Qué es | Cuándo se lee |
|---|---|---|
| `AGENTS.md` | Cómo trabajar en este repo | **Siempre**, es lo primero |
| `General/GUIA.md` | **Lo que es cierto HOY** y aplica a toda la app | **Siempre**, antes de tocar código |
| `General/Pantallas.md` | Navegación, estándares de tamaño, moldes A/B y decisiones por pantalla | Si la tarea toca una pantalla o su navegación |
| `General/Indices-Codigo.md` | Índice de funciones y vistas de los 13 archivos grandes (juegos, `Citas`, `Retos`, `favor.js`…) | Solo para buscar dentro de uno de esos archivos, en vez de leerlo entero |
| `General/Modales.md` | Registro de ventanas emergentes y cómo las cierra el atrás | Solo si la tarea toca un modal o una ventana emergente |
| `General/Centro-Adquisiciones.md` | El Centro: deseos, tienda y pedidos | Solo si la tarea toca `Retos/centro.html` |
| `General/IA-Acompanante.md` | `Acompanante/`: el tono de la IA, los ajustes y los retos que propone | Solo si la tarea toca `Acompanante/` o los retos de la IA |
| `General/Campana-Pestana.md` | `pestana.js`: campana, bip y cartelito (Chat y Retos) | Solo si la tarea toca los avisos de la campana |
| `General/Recordatorio.md` | El recordatorio de la mañana (GitHub Actions + Telegram) | Solo si la tarea toca el recordatorio |
| `General/Catalogo-Lenceria.md` | Catálogo de lencería: prendas, planes, pedidos y fotos | Solo si la tarea toca la lencería |
| `General/Pegamento-y-Citas.md` | El pegamento, la agenda de `Citas/` y las pantallas de Actividades y Accesorios | Solo si la tarea toca esas pantallas |
| `General/Modulo-Acceso.md` | Detalle de `acceso.js` (licencias, qué exporta, cómo quedó cada página) | Solo si la tarea toca licencias o `acceso.js` |
| `General/Autorizar.md` | Detalle de `Autorizar/` (aprobar y revocar, login, llave privada) | Solo si la tarea toca la pantalla de licencias |
| `General/Favores-Express.md` | Detalle de `favor.js` (favores expresos, precios del 🛒, reglas) | Solo si la tarea toca favores |
| `General/Propuestas-Precios.md` | Los 5 números del carrito: proponer, aprobar y aplicar | Solo si la tarea toca esas propuestas |
| `General/Puntos.md` | El sistema de puntos: saldos, historial (`puntos/{id}/movimientos`) y qué registra cada módulo | Solo si la tarea toca puntos, favores, retos o el Centro |
| `General/Castigos.md` | Detalle de `Castigos/` ("El Precio del Placer", editor, partida, multi) | Solo si la tarea toca el juego de castigos |
| `General/Roles.md` | `Roles/`: los cuatro modos, las 4 ramas del duelo, la sesión y la tarjeta | Solo si la tarea toca `Roles/` |
| `General/Opciones.md` | `Opciones/`: Elecciones Peligrosas, modos, reparto y lista de opciones | Solo si la tarea toca el juego de opciones |
| `General/Retos.md` | El juego de Retos, sus metas y su puntuación | Solo si la tarea toca Retos |
| `General/Usuarios.md` | Pantalla de Usuarios: Cambiar usuario, nombres, puntos y anatomía | Solo si la tarea toca Usuarios |
| `General/Modo-Invitado.md` | Modo invitado: sin salida, vuelve solo al abrir, registro por QR | Solo si la tarea toca el modo invitado |
| `General/Invitado-a-media-partida.md` | Regla para el invitado que entra con la partida empezada | Solo si la tarea toca ese caso |
| `General/Diablitos.md` | Iconos dibujados (SVG) del juego Diablitos | Solo si la tarea toca ese icono |
| `General/Telegram.md` | `avisarTelegram()`: módulo central de avisos por Telegram | Solo si la tarea toca avisos por Telegram |
| `General/Catalogo.md` | Aviso de "nuevo" (packs nuevos en el carrito y en el Centro) | Solo si la tarea toca ese aviso |
| `General/Packs-Personajes.md` | Packs de personajes: ítems del catálogo que instalan sus personajes en las listas de la pareja (**pendiente de implementar**) | Solo si la tarea toca packs de personajes |
| `General/Despierto.md` | `despierto.js`: mantiene la pantalla encendida durante la partida | Solo si la tarea toca el bloqueo automático del celular |
| `General/fuegos.md` | `fuegos.js`: fuegos artificiales al final de la partida | Solo si la tarea toca los fuegos |
| `General/confirmar.md` | `confirmar.js`: cuadros de `confirmar()` y `aviso()` | Solo si la tarea toca esos cuadros |
| `General/Modelo-Datos.md` | Inventario de la base y lo que falta normalizar (**propuesta**) | Antes de migrar datos |
| `General/HISTORIA.md` | **El porqué**: relato con fecha, incluido lo que se bajó de `GUIA.md` | Solo en los casos de la lista de abajo |

**Si se crea o se modifica una pantalla, un módulo o un juego: el detalle va a su
propio archivo en `General/`, nunca a `GUIA.md`.** En `GUIA.md` queda una línea que
apunte. Si falta el archivo de detalle, se crea y se agrega a esta tabla.

**`HISTORIA.md` se lee SOLO si la tarea toca alguno de estos:**

- Modo invitado, copia de seguridad, salir de la invitación.
- Sala de espera (`Diablitos/`), invitaciones de los juegos.
- Avisos de fin de partida, pausa, "Saltar turno", el anfitrión.
- `acceso.js`, licencias, catálogo, el límite de 30 solicitudes.
- Retos de la IA de `Acompanante/`, `Retos/`, `Retos/centro.html`.
- `Citas/` y el Centro de Adquisiciones.

**NO lo necesitas para:** estilos, agregar o quitar un botón, el menú y sus
submenús, el Chat, la campana de la pestaña, `confirmar.js`, `fuegos.js`,
`glue.js`, el Asistente, o las reglas de Firebase (esas están en `GUIA.md`).

## Presupuesto de documentación (para que no vuelva a crecer)

**La lectura obligatoria —`AGENTS.md` + `GUIA.md`— no pasa de 750 líneas juntas.**
Hoy están alrededor de 707. Si se pasan, se mueve el **relato** a `HISTORIA.md`;
nunca se recorta una regla.

- **Una regla = una línea.** Si necesita tres párrafos, lo que sobra es el porqué: va
  a `HISTORIA.md`.
- **Nada de fechas en `GUIA.md`.** "Antes se hacía…" va a `HISTORIA.md`.
- **Lo que se cierra, se va:** un pendiente resuelto pasa a `HISTORIA.md` (sección 8);
  no se queda tachado en la lista.
- **Una regla vive en un solo sitio**; los demás apuntan.
- **Un documento de detalle no crece sin que algo salga.**
- **`Indices-Codigo.md` no se edita a mano:** se regenera cuando cambian los archivos.
- **Poda:** una vez al mes, o cuando una tarea tarde de más, se revisan cuatro cosas:
  tamaño, fechas, pendientes cerrados y reglas duplicadas.

`revisar.py` avisa del tamaño en cada corrida. **El aviso no detiene la revisión:** es
para verlo antes de que duela.

## Decisiones ya tomadas (no volver a preguntar)

Estas cosas **ya están decididas**. Si la duda está en esta tabla, **se aplica y se
sigue**; no se pregunta otra vez. El detalle de cada una está en la última columna.

Esto **no anula la regla 0**: si el pedido no está claro, o es una decisión **nueva**
de producto, se pregunta antes de escribir.

| Si la duda es... | Ya está decidido | Detalle |
|---|---|---|
| Dónde va el «Volver» | Arriba a la derecha, fijo, con el texto `‹ Volver`; a la izquierda solo el botón contextual de esa pantalla | `GUIA.md` → *Dónde va cada «Volver»* |
| Cómo se comporta el atrás | Cada vista interna es un paso real del historial; durante la partida no se sale; el invitado cae en la espera | `GUIA.md` → *Navegación* y `General/Pantallas.md` |
| Tamaño de botones, tarjetas y títulos | Se copia de `index.html`; no se inventan medidas | `GUIA.md` → *Estándares de tamaño* |
| Cómo se pregunta o se avisa | Solo `confirmar.js` (`confirmar()` / `aviso()`); nunca `confirm()` ni `alert()` | `General/confirmar.md` |
| Un botón que depende de JavaScript | Nace oculto en el HTML (`display:none`) | Regla 7 de este archivo |
| Un submenú con tarjetas escritas a mano | Su botón nace visible; el catálogo no lo apaga | `GUIA.md` → *Comunicaciones* |
| Cómo se enlazan los datos | Por **id**; el nombre solo se muestra. Lo que apunta a otro guarda `<algo>Id` | `GUIA.md` → *La llave es el id* |
| Qué contenido usa cada quien | `anatomia`: masculino = A, femenino = B; el administrador solo administra | `GUIA.md` → *La anatomía define el contenido* |
| El invitado | No tiene salida; vuelve solo al abrir; elige anatomía al registrarse y queda fija | `General/Modo-Invitado.md` |
| Reglas de la base de cada pareja | Abiertas **a propósito**; no se cierran ni se propone cerrarlas sin avisar | `GUIA.md` → *La base de cada PAREJA* |
| Reglas de `solicitudes` | `read` sigue abierto a propósito (modo sin conexión) | `GUIA.md` → *Reglas de solicitudes* |
| Avisos al celular | No hay push ni service worker; se avisa por Telegram y por la campana | `General/Telegram.md`, `General/Campana-Pestana.md` |
| Cómo se verifica | `python revisar.py` y prueba en vivo; no hay arnés de pruebas | *Cómo trabajar*, en este archivo |
| Los saldos de puntos | Se cambian libres a propósito (para probar sin molestar) | `GUIA.md` → *Otros pendientes* |
| Los 5 números del 🛒 | Cada quien propone los suyos (el 🛒 sale solo en tu fila) y el otro perfil base los aprueba; sin acuerdo no cambian | `General/Propuestas-Precios.md` |
| Exportar/Importar de la lencería | Se quedan por ahora; **se quitan antes de vender** | `General/Catalogo-Lenceria.md` |
| Licencias (los 5 pasos) y el permiso `borrar` | **En espera** hasta el cambio de arquitectura; no se hacen ahora | `GUIA.md` → *Pendientes de licencias* |
| Nombres en ejemplos y documentación | `Mary` (pareja) y `Fredy` (administrador); en la app salen de la base | Regla 9 de este archivo |
| Textos de la app | Con ortografía correcta siempre, sin que lo pidan | Regla 10 de este archivo |

## Cómo trabajar en este repo

- Todo el código es **HTML estático con JavaScript adentro**. No hay build, no hay
  npm, no hay framework. Se edita el archivo y ya.
- Los módulos compartidos viven **en la raíz** (`acceso.js`, `invitado.js`,
  `config.js`, `firebase-config.js`, `taquilla.js`, `fuegos.js`, `confirmar.js`,
  `pestana.js`, `telegram.js`) y se importan por ruta relativa **al módulo**, no al
  archivo que lo importa.
- **`avisarTelegram()` ya NO se copia:** vive en `telegram.js`. Si necesitas mandar
  un aviso, **impórtalo**; no lo pegues otra vez.
- **Reglas de Firestore:** no están en el repo. Viven en la consola de Firebase.
  Cualquier tarea sobre permisos es manual y hay que decirlo.
- **No hay `git` disponible en el entorno de trabajo.** Para revisar cambios se leen
  los archivos; Fredy es quien sube con GitHub Desktop.
- **Para buscar dentro de un archivo grande** (los 13 del índice: juegos, `Citas`,
  `Retos`, `favor.js`, `actividades`, `centro`…), usa `General/Indices-Codigo.md`:
  dice qué función hace qué y en qué línea. No hace falta leer el archivo entero.
- **Verificación por sintaxis (rápida, sin navegador):** es el único chequeo
  automático. `herramientas/sintaxis/`, en dos pasos (`extract.py` y luego
  `jscheck.py`), o directamente:

  ```powershell
  cd herramientas\sintaxis
  python revisar.py
  ```

  `revisar.py` revisa **todo** el repo y sale con `1` si algo falla. Se corre
  **una sola vez** (`python revisar.py` muestra solo problemas y un resumen; con
  `-v` muestra el detalle completo). **No se corre dos veces a la vez:** los dos
  borran y escriben `Temp\opencode\extracted`, y uno le quita los archivos al otro.
  **Nunca le pases un `.html` a `jscheck.py`**: no saca los `<script>` y cuenta
  también las llaves del CSS, así que dice "OK" por casualidad. El `.js` que hay
  que revisar es el que deja `extract.py`.
- Si agregas una pantalla o un módulo, **regístralo en `extract.py`**, o queda sin
  revisar para siempre.
- **No hay arnés con Chrome** (se retiró en oct-2026: lento y poco fiable). **La
  verificación de verdad es en vivo**, en Pages y en el celular de Fredy.

## Cuándo dejar de insistir (regla dura)

Aplica a cualquier forma de verificar, también a la prueba en vivo.

**Máximo 3 intentos por forma de probar.** Si a la tercera no sale:

1. **Para.** No lo intentes una cuarta vez "a ver si ahora sí".
2. **Cambia de forma**: otra manera de probar, o revisión leyendo el código.
3. **Anótalo** como "pendiente de probar a mano" y **dilo en tu respuesta**.
4. Pasa a lo siguiente.

Nunca dejes a la persona esperando en silencio mientras repites lo mismo. Si algo
se atora, **dilo de inmediato** y di qué harás en su lugar. **Prefiere menos pruebas
y más rápido** antes que una prueba atascada.

## Pruebas: cuándo hacen falta y cómo no comerse la sesión (regla dura)

**El trabajo es escribir código, no probarlo.** Ya se acumularon arneses y scripts,
y las sesiones se acababan en pruebas en vez de en avance. **Que no vuelva a pasar.**

**Antes de pedir una prueba, se clasifica el cambio:**

| Clase | Qué entra | Cómo se cierra |
|---|---|---|
| **A. No necesita el celular** | Textos, títulos, etiquetas, colores, márgenes, orden de botones, documentación | Con `revisar.py` en verde. Se dice "listo" y **no se pide prueba** |
| **B. Sí necesita prueba en vivo** | Guardar, leer o borrar datos; partidas y turnos; invitado y QR; licencias; puntos; pedidos; cualquier cosa que dependa de dos teléfonos o de la base real | Se anota y se prueba **una sola vez, agrupado** |

- **Se agrupa por pantalla:** los cambios de la misma pantalla se juntan y se prueban
  en una sola sesión, no uno por uno.
- **La prueba se pide en uno o dos pasos concretos** ("entra a Roles, juega un turno y
  mira que la tarjeta cambie"), nunca una lista larga.
- **Excepción:** si el cambio es delicado (partida, invitado, licencias), se prueba
  enseguida aunque sea uno solo.
- **Si un cambio mezcla las dos clases, manda la B.**
- **"Listo" significa:** `revisar.py` en verde y documentación al día. Si es clase B,
  se dice **qué mirar** y queda anotado como pendiente de Fredy.

Y lo de siempre:

- **No se deja NINGÚN arnés en el repo.** Ni scripts, ni carpetas, ni páginas de
  prueba. Lo de probar vive en `Temp\opencode` y se borra al terminar. Si de verdad
  tiene que ir dentro del repo (por sus `import` relativos), se crea, se usa y **se
  borra en la misma sesión**, y se avisa.
- **La única prueba automática es `revisar.py`.** Tarda un segundo: se corre después
  de cada cambio, siempre.
- **No se repite una prueba que ya falló.** Tres intentos por forma de probar y se
  suelta: se anota como pendiente y se sigue.
- **Si un tema se vuelve caro de comprobar, se avisa ANTES de gastar**, no después.
- **Lo que solo se puede ver en el celular de Fredy o en su base real, se le pasa a
  él de una vez**, diciendo qué mirar y por qué. No se simula, y no se le manda una
  lista larga de tareas.
- **Inspección visual propia: una sola por cambio, y solo si el aspecto importa.**
  Nunca para comprobar un texto.

## Reglas de la casa

0. **No se toca el repo sin que Fredy lo pida.** Ni un archivo, ni una línea: no se
   "de paso" un arreglo, no se completa algo que se ve que falta y no se anticipa la
   segunda mitad de un trabajo. **Primero se pregunta, después se aplica.**
   - Si el pedido está claro: se aplica **lo pedido**, nada más.
   - Si el pedido no está claro: **se pregunta antes de escribir.**
   - Si se ve que falta otra cosa: **se dice y se pregunta.**

1. Si la decisión es de producto (qué se ve, quién puede salir, qué pasa al
   pausar), **preguntar antes de aplicar**.
2. Explicar en español claro y sin código. El usuario no programa.
3. No inventar reglas nuevas de Firestore: se reutiliza lo que ya funciona.
4. No agregar reglas de seguridad que rompan el modo invitado (nada de "solo el
   anfitrión escribe", porque el invitado escribe su identidad).
5. **No se usa `confirm()` ni `alert()` del sistema.** Todo pasa por `confirmar.js`:
   `confirmar()` para preguntar (se espera) y `aviso()` para decir una cosa (no se
   espera; el `return` va después).
6. Cambios mínimos, y **verificar antes de decir "listo"**.
7. **Un botón que JavaScript tiene que ocultar, nace oculto en el HTML**
   (`style="display:none"`). Si nace a la vista, hay un rato en que se ve aunque no
   deba.
8. **Documentar:** lo general en `GUIA.md`; el detalle de una pantalla o módulo en su
   archivo de `General/`. Lo viejo ("antes se hacía X", fechas de hace meses) va a
   `HISTORIA.md`. `GUIA.md` tiene que poder leerse de arriba a abajo.
9. **Los ejemplos usan los nombres de verdad: la pareja es `Mary` y el administrador
   `Fredy`.** Eso **no** es un dato de la app: el nombre real sale de la base
   (`nombreLado()`) y ningún nombre se hardcodea en el código.
10. **Ortografía:** todo texto de la app (títulos, botones, avisos, etiquetas,
    mensajes, placeholders, descripciones) va **con ortografía correcta**. Se corrige
    de entrada, sin que lo pidan. Aplica también a la documentación de `General/`.
11. **La llave de los datos es el id, no el nombre.** Toda colección o pantalla nueva
    enlaza por id; el nombre es solo para mostrar. Si una tarea guarda datos y no
    está claro cuál es la llave, se pregunta antes de escribir. Ver `GUIA.md`,
    *La llave es el id, no el nombre*.

## Navegación (regla dura)

Toda pantalla nueva o tocada tiene que cumplir el contrato de `General/Pantallas.md`
→ *Estándar de navegación* y pasar su *Checklist*. Si no, **no está terminada**.

- El «Volver» se llama **`‹ Volver`** y va **fijo arriba a la derecha** (clase
  `.back`, `position:fixed`, `top:max(20px, env(safe-area-inset-top))`), **fuera de
  cualquier encabezado que haga scroll**. A la izquierda va solo el botón contextual
  de esa pantalla.
- Cada vista interna es un **paso real del historial** (`pushState`) y el `popstate`
  obedece al estado. Solo Configuración (y el editor si ya se cargó) se reabre; la
  partida, la selección y los avisos no.
- Durante la partida el atrás **no saca**. El invitado cae siempre en la espera y
  nunca ve Configuración ni el editor.
- Al salir al menú se **deshacen los pasos de la pantalla** (`salirAlMenu()`); si se
  abrió desde fuera, se usa la dirección fija.
- Una pantalla con JavaScript se registra en `herramientas/sintaxis/extract.py`.
- Toda **ventana emergente** se registra en `General/Modales.md`.
- `python revisar.py` tiene un bloque **navegación**: si marca `GLIFO` o `HIST`, se
  corrige antes de subir; `REGISTRO` y `FIJO` son avisos. Y un bloque **modales**:
  **falla** si una ventana del HTML no está registrada en `General/Modales.md`.
- **Capa 3 pendiente (no urgente):** un `nav.js` mínimo con `marcarEntrada()` y
  `salirAlMenu()`. Se hace **después** de probar en el celular, en una sesión
  aparte. Alcance en `General/Pantallas.md` → *Pendiente: capa 3*.

## La llave del `Panel/` — NUNCA al repo

`Panel/` y `Autorizar/` piden una **llave privada JWK** (`{"kty":"EC",...}`). **No es
una API key de Firebase**: es la mitad privada de un par **ECDSA P-256** para
**firmar licencias**.

- La **pública** vive en `taquilla.js` (`TAQUILLA_PUBLICA`) y **sí** va al repo: solo
  verifica.
- La **privada** vive **solo en el aparato del desarrollador**, en `localStorage` bajo
  `taquilla_priv`. **Jamás la subas ni la escribas en ningún archivo del repo ni en
  la guía.**
- Ambos usan la **misma** clave y el **mismo** origen: pegarla una vez abre los dos.
- Si se pierde, se genera un par nuevo (con `crypto.subtle`), se cambia
  `TAQUILLA_PUBLICA` y **las licencias viejas dejan de validar**.

## Riesgo conocido (importante, NO urgente)

- **Las reglas de `solicitudes` SÍ están cerradas** (6-oct-2026, probadas: pedir,
  aprobar, revocar y el Panel). Sigue abierto `allow read`, **a propósito**: el menú
  y los juegos leen esa colección sin sesión y sin internet, y cerrarla rompe el modo
  sin conexión. Texto vigente: `General/reglas-firebase-taquilla.txt`. **No lo trates
  como urgencia ni intentes cerrarlo por tu cuenta.**
- **`Autorizar/index.html` ya está subido** y su login de Google funciona.
- **Si las compras dejan de funcionar**, la causa más probable es la lista de los 7
  campos de `create` en las reglas (sección 3 del archivo de reglas).
- **Pendiente real:** el permiso de **`borrar`** en `solicitudes`, para el rediseño de
  la cola. Es **manual, en la consola**, y hay que probar las 4 cosas de la sección 5.
  **Está EN ESPERA** (decisión de Fredy): cuelga del cambio de arquitectura.
  Ver `GUIA.md` → *Pendientes de licencias*.

## La base de cada PAREJA: reglas ABIERTAS a propósito

Instaladas con `allow read, write: if true` (`README.md`, paso 2). **Es una decisión,
no un descuido: no se cambia.** La app de la pareja no inicia sesión contra su propia
base, así que cerrarlas rompe todo.

**Si alguien -persona o modelo- propone cerrarlas o "ponerle candado" a
`Citas/actividades.html`: que avise antes.** Ya pasó una vez (oct-2026) sin estar
escrito. Detalle en `GUIA.md` → *La base de cada PAREJA*.

## 📄 Índice de documentación de detalle

Todo el detalle de **pantallas, navegación, estándares de tamaño y moldes A/B** vive en
**`General/Pantallas.md`**. Aquí en `AGENTS.md` solo están las **reglas de trabajo** y
la **tabla de documentos**.

## Pendientes de limpieza (fuera del repo)

- **`Temp\opencode\respaldo-docs-2026-11-07\`**: respaldo de la documentación antes de
  reordenarla (nov-2026). **Se borra cuando Fredy confirme que subió los cambios con
  GitHub Desktop.** Si al empezar una sesión todavía está, **recordárselo**.

# Plan — Juego “El Precio del Placer” (Castigos)

> **Prompts por etapa:** están en **`General/Plan-Castigos/`** (`00-LEEME.md` y
> `01-Etapa-1.md` … `07-Etapa-7.md`). Úsalos **uno por prompt**, en orden.
>
> **Este archivo es un plan de construcción para que lo ejecute otro modelo.**
> No es documentación de algo ya hecho. Se escribió para que **no haya nada que
> interpretar**: nombres, campos, textos, reglas y casos límite están definidos.
> Si algo no está aquí, **no se inventa: se pregunta a Fredy**.
>
> **Antes de tocar código:** leer `AGENTS.md` y `General/GUIA.md` completos.
> Reglas del repo: HTML estático con JS adentro, sin build, sin npm. Se edita y
> `herramientas/sintaxis/revisar.py` se corre después de cada cambio. Fredy sube
> con GitHub Desktop y se prueba **en vivo** en el celular. No se toca nada sin
> pedido. No se toca `App Pareja` (la app real): todo esto es en
> `Citas-de-Pareja`.
>
> **Estado:** **implementado (oct-2026).** Falta **solo la prueba en vivo**.
> Checklist: `General/Plan-Castigos/08-Pruebas-En-Vivo.md`.

---

## 1. Resumen

- **Nombre:** El Precio del Placer
- **Lema / descripción:** “Ganar cumple tus deseos; perder despierta la pasión.”
- **Qué es:** juego **independiente** de castigos, con contenido nuevo. No es una
  copia de Guiadas ni de Encuentros: se parece más a **Encuentros** (banco de
  contenido, listas por jugador, turnos, invitados), pero con sus propias reglas.
- **Sección:** **Juegos** (submenú `#juegos`).
- **Pack / licencia del juego:** id **`castigos`** en `packs` (taquilla), no es
  `libre`; se adquiere como Guiadas/Encuentros.
- **Tarjeta:** título “El Precio del Placer”, descripción = el lema, **icono desde
  el catálogo** (no va fijo en el código), ruta **`Castigos`**, sección
  **`juegos`**.
- **“Volver”:** a `../index.html#juegos`.
- **Castigos oficiales:** packs **`ofc_...`** con `oficial: true`, `ruta:
  "Castigos"`, `seccion: "juegos"`, su propia licencia. Salen como tarjeta en el
  Centro desde el inicio (como las actividades oficiales) y al aprobarse se
  copian al banco de la pareja. **No traen accesorios.**

---

## 2. Decisiones cerradas (no cambiar sin preguntar)

### 2.1 Contenido
- El **castigo** es el contenedor (como una actividad); las **acciones** son los
  renglones por nivel y lado.
- **5 niveles:** `basico`, `medio`, `avanzado`, `experto`, `alucinado`.
- **Lados A/B.** A = administrador, B = pareja. Un invitado usa el lado de quien
  lo invitó (`conQuien`).
- Cada acción:
  - **Texto de máximo 60 caracteres.**
  - **Accesorio opcional** (uno solo), tomado de `accesoriosCastigo`.
  - **Medida:** `libre`, `tiempo` (minutos) o `veces` (cantidad). Una sola.
  - En juego se lee como **“acción con accesorio”** (si no tiene accesorio, solo
    la acción).
- **Tomas:** **compartidas** por los dos lados, **un número por nivel** (5
  números), igual que Guiadas/Encuentros. La lista de A y la de B se arman con
  esos mismos números.
- **Imposiciones:** banco aparte, **texto puro**, **una lista por lado (A/B)**.
  No llevan accesorio ni medida. Las pone siempre cada pareja; los castigos
  oficiales **no** las traen.

### 2.2 Modos y jugadores
- Modos: **Solo**, **Pareja**, **Invitados**.
- **Un celular / Cada quien el suyo** se muestra **siempre**, incluso en Solo
  (el usuario lo usa al gusto).
- **Normal / Multi.**
- **Sorpréndeme** (solo en Multi): elige 3 castigos al azar (sin repetir) y abre
  una ventana “Son X, Y + Z” con **Aceptar / Reelegir**.
- **Placer extremo por deseo:** interruptor en el **menú de entrada**, disponible
  en **cualquier modo** (Solo/Pareja/Invitados; Normal/Multi). Cuando está activo,
  la lista usa **todas** las acciones de `avanzado`, `experto` y `alucinado`, al
  azar, y **se salta el paso de tomas**. `basico` y `medio` quedan en 0. En Multi
  también se aplica el **reparto en rueda**.
- **Pareja e Invitados:** en la pantalla de inicio se elige **quién castiga
  primero** (A o B). Esa elección es el **lado inicial**.
- **Solo:** el lado inicial es el **lado del usuario actual** (A si es admin, B si
  es pareja). El jugador se aplica el castigo a sí mismo.
- **Invitados:** cada invitado usa las acciones y las imposiciones **de su lado**
  (el de quien lo invitó). A cada invitado se le arma **su propia lista**,
  procurando que todas sean distintas.
- **Invitado a media partida:** se le copia la lista de un compañero de su mismo
  lado y solo juega **lo que falta**. (Igual que Encuentros.)

### 2.3 Turnos
- Al iniciar se arma un **orden aleatorio con todos los jugadores**.
- **Ronda = una vuelta completa:** cada jugador juega **una vez por ronda**
  (ronda de todos, no alternancia estricta de lados).
- El juego termina cuando **se acaban todas las listas**. Como todos juegan una
  vez por ronda y las listas tienen el mismo largo, en teoría acaban juntos.
- El turno actual es **de un jugador**. Ese jugador es **el que castiga**.
- **El que recibe** se deduce:
  - Pareja/Solo: el otro lado / uno mismo.
  - Invitados: **todo el lado contrario** (opción A).
- **Revivir:** botón/switch **solo del anfitrión**, visible debajo del recuadro
  del turno, de ancho completo, con el texto **“Revivir: apagado / encendido”**
  (teal cuando está prendido).
  - Se prende y apaga **en cualquier momento**.
  - **No pide confirmación**: solo se ejecuta.
  - **Aplica desde el turno siguiente**: el turno en curso sigue con quien le
    tocaba; lo ya jugado no se rehace.
  - **Apagado:** solo se juegan los turnos del **lado inicial**; los del otro
    lado se **saltan pero se consumen** (sus listas avanzan igual).
  - **Encendido:** se juegan todos los turnos.
  - El avance **no se reinicia** al prender/apagar.
  - En **Solo puro** (sin invitados) se oculta (no hay otro lado). En **Solo con
    invitados** de los dos lados, se muestra.
- **Saltar turno:** botón **solo del anfitrión**, visible también en Solo.
  **Consume el turno**: se pierde la imposición y el castigo de ese turno y se
  salta al siguiente.
- **Pausar y Salir** y **Terminar Partida:** solo anfitrión, como Encuentros.
  **Al pausar, el cronómetro se detiene y se retoma al continuar** (decisión de
  Fredy, oct-2026; antes seguía corriendo). **Pausar y Salir** deja la partida
  viva y vuelve a la lista; al elegir la actividad se ofrece
  **"¿Continuar partida anterior?"**.
- **Fin:** “¡Gracias por jugar!” + fuegos, y regreso a la lista.

### 2.4 Imposiciones
- Se **barajan al inicio** por lado.
- **Solo los turnos jugados consumen imposición.** Los saltados (Revivir apagado
  o “Saltar turno”) **no** consumen.
- **No se repite dentro de una ronda.** Si se acaban, se rebarajan para la
  siguiente.
- Si Revivir se enciende a media partida, los turnos nuevos que se jueguen toman
  de las que quedan; si ya no hay, se rebarajan.
- **Se ven en todos los celulares.** Solo el que castiga tiene **“Aceptar”**.
- El que **recibe** la ve **como contexto**, sin botón (opción A).
- Si un lado no tiene imposiciones cargadas, sus turnos van **sin imposición**
  (se salta el paso).
- Flujo del turno: se muestra la **imposición** → el que castiga oprime
  **“Aceptar”** → se muestra el **castigo**.

### 2.5 Medidas
- Se eligen **por acción** (no son una regla del juego).
- En el **editor** (pareja): el **lápiz** de la fila abre una ventana con
  **accesorio opcional + una sola medida (Libre/Tiempo/Veces) + valor**. El valor
  es obligatorio si es Tiempo o Veces. **Tiempo en minutos, sin segundos.** Por
  defecto: **Libre**.
- En el **Panel** (oficial): tres estados por acción: **Libre** (por defecto),
  **Tiempo** (valor al azar **1–5 min**) y **Veces** (valor al azar **5–10**).
  Oprimir otra vez el mismo estado **vuelve a sortear**. El valor **queda fijo**
  al asignarlo. **No se captura a mano.**
- En juego (celular del que castiga):
  - **Libre / Veces:** ventana con la acción y **“Listo”**; al oprimirlo sigue.
  - **Tiempo:** **“Iniciar”** → cuenta regresiva (minutos) + **“Listo”** siempre
    abajo. Al llegar a cero **espera** a que opriman “Listo”.
  - **“Listo” solo lo tiene el que castiga.**
- **El que recibe** ve **solo la acción** (sin medida ni cronómetro), más la
  imposición como contexto.
- **Los demás** ven “Turno de [nombre]”.
- Borrar un accesorio del catálogo **avisa** que afecta a las acciones que lo
  usan; esas acciones **quedan sin accesorio**.

### 2.6 Multi y reparto
- Al oprimir **Multi**: seleccionar **3 castigos** (casillas), botón **Combinar
  (3/3)**, ventana de confirmación (“¿Son estas 3?” con Continuar/Reelegir) y
  luego el **paso de tomas**. Se juega respetando esas tomas.
- **Reparto en rueda (el criterio oficial de este juego):**
  - Por **nivel y lado**, se necesitan `tomas[nivel] × número de jugadores de ese
    lado` acciones.
  - Se toma **una acción de cada castigo por turnos** (orden de castigos
    barajado), saltando los que ya no tengan acciones, hasta juntar lo necesario
    o agotar el pool.
  - El castigo con **menos** acciones **aporta todo lo que tiene**; el resto se
    reparte entre los demás.
  - **Sin repetir hasta agotar el pool.** Si lo pedido supera el pool, se repite
    (rebarajando).
  - Después se **baraja** lo seleccionado y se **reparte** entre los jugadores de
    ese lado **sin repetir**, procurando que cada uno lleve mezcla de los 3
    castigos. Si no alcanza, se repite.
  - **Esta regla reemplaza** el “mínimo” de Guiadas y el “pool proporcional” de
    Encuentros. Aplicarla a esos dos juegos queda como **pendiente** (sección 9).
- **Placer extremo:** usa todas las acciones de `avanzado`+`experto`+`alucinado`
  del castigo (o de los 3, con reparto en rueda) y las baraja. En varias
  jugadores, se reparten esas acciones **sin repetir** entre los jugadores del
  lado, en partes iguales; si sobran/faltan, se repite para emparejar el largo.
  **No usa tomas.**

### 2.7 Tomas (flujo estándar)
- En los tres juegos (Castigos, Guiadas, Encuentros) el paso de tomas debe ser el
  de **Encuentros**: **siempre aparece al iniciar**, **precargado** con las
  guardadas y **editable**.
- En **Castigos**, las tomas son **compartidas** (un número por nivel).
- En **Placer extremo** el paso **se salta**.
- En **Multi**, las tomas son **de la partida** (no se guardan en los castigos).
- **Guiadas normal** hoy usa las guardadas sin preguntar: al estandarizar, se le
  agrega el paso (esto es parte del pendiente de la sección 9, junto con el
  reparto en rueda).

### 2.8 Oficiales
- Cada castigo oficial es un pack **`ofc_...`** con su licencia, como los `of_...`
  de actividades.
- Trae: **acciones por nivel y lado** (texto + medida sugerida) y **tomas
  sugeridas**. **No trae accesorios** (los asigna la pareja). Las imposiciones
  tampoco (las pone la pareja).
- Al aprobarse se copia a `nivelesCastigo/{ofc_id}` con `oficial: true`, sus
  acciones/medidas y las tomas (solo si la pareja no las ha cambiado).
- Sale como **tarjeta en el Centro (sección Juegos)** desde el inicio y se pide
  como las oficiales de actividades. El aviso de “nuevo” también cuenta.
- En el **menú** no sale como tarjeta (solo dentro del juego).
- En la lista del juego va **primero**, con 🏅.
- Se puede editar (acciones, medidas, accesorios) pero **no renombrar**. Si se
  borra, vuelve a aparecer mientras siga aprobado (reset).
- **Panel:** pantalla nueva **“Castigos Oficiales”** con crear/editar/eliminar,
  activar, fecha NUEVO, **Importar** y **Exportar** JSON.

---

## 3. Modelo de datos

### 3.1 Colecciones nuevas (base de la pareja)
| Colección | Doc | Forma |
|---|---|---|
| `castigosExtra` | uno por castigo | `{ nombre, creadoEn? }` |
| `nivelesCastigo` | id = nombre del castigo (o `ofc_...`) | `{ n, titulo, oficial?, tomas, actualizadoEn }` |
| `accesoriosCastigo` | uno por accesorio | `{ nombre, creadoEn? }` |
| `imposicionesCastigo` | **`actual`** | `{ A: [texto, ...], B: [texto, ...] }` |
| `sesionCastigos` | **`actual`** | sesión compartida (3.2) |

**`nivelesCastigo/{id}.n`** (misma forma que Guiadas/Encuentros, pero las
acciones son **objetos**, no strings):

```js
n = {
  basico:    { A: [accion, ...], B: [accion, ...] },
  medio:     { A: [...], B: [...] },
  avanzado:  { A: [...], B: [...] },
  experto:   { A: [...], B: [...] },
  alucinado: { A: [...], B: [...] }
}

accion = {
  texto: "Arrodíllate frente a mí",
  accesorio: "Venda" | null,          // opcional
  medida: { tipo: "libre"|"tiempo"|"veces", valor: 0 }  // valor: min o veces; 0 si libre
}
```

**`tomas`** (compartidas, un número por nivel):

```js
tomas = { basico: 2, medio: 2, avanzado: 1, experto: 1, alucinado: 1 }
```

**`imposicionesCastigo/actual`:**

```js
{ A: ["Susúrrale al oído...", ...], B: ["Tápale los ojos...", ...] }
```

### 3.2 Sesión `sesionCastigos/actual`

```js
{
  activa: true,
  pausada: false,
  terminada: false,
  porAdmin: false,
  sid: "<timestamp+random>",
  hostUid: "<id del que inició>",
  hostNombre: "<nombre>",
  modo: "solo" | "pareja" | "invitados",
  unCelular: true|false,
  multi: true|false,
  placerExtremo: true|false,
  revivir: true|false,
  ladoInicial: "A"|"B",
  cabezas: [
    { id, nombre, lado: "A"|"B", admin: bool, invitado: bool, conQuien: "<id>"|null }
  ],
  orden: ["id1","id2", ...],       // orden aleatorio de TODOS los jugadores
  turnos: [
    {
      jugador: "id",
      lado: "A"|"B",
      ronda: 1,
      accion: { nivel, lado, texto, accesorio, medida },
      imposicion: "texto"|null,    // se escribe al jugarse el turno
      saltado: false,              // true = se salta (Revivir apagado / Saltar turno)
      hecho: false
    }
  ],
  turno: 0,                        // índice en turnos
  ronda: 1,
  empezadaEn: serverTimestamp(),
  actualizadaEn: serverTimestamp()
}
```

Reglas de la sesión:
- `turnos` se arma **al iniciar**: una entrada por jugador por ronda, en `orden`,
  con la siguiente acción de la lista de ese jugador. Todas las listas tienen el
  mismo largo, así que el número de rondas = largo de la lista.
- `saltado` de cada turno se calcula según `revivir` y `ladoInicial`: si
  `revivir === false`, los turnos cuyo `lado !== ladoInicial` se marcan
  `saltado: true` (pero **la acción se consume igual**, porque ya está en
  `turnos`).
- **Revivir** actualiza `revivir` y recalcula `saltado` **solo en los turnos con
  índice > `turno` y `hecho === false`**. El turno actual no cambia.
- **Saltar turno** marca el turno actual `saltado: true`, `hecho: true`,
  `imposicion: null`, y avanza.
- **Imposiciones:** al iniciar, por lado se baraja la lista. Cuando un turno **se
  juega**, el anfitrión toma la siguiente imposición de ese lado, la escribe en
  `turnos[turno].imposicion` y actualiza la sesión. Los turnos saltados **no**
  toman. Si la lista se acaba, se rebaraja. No se repite dentro de una ronda.
- **Pausar:** `pausada: true`; se detiene el cronómetro local y se guarda el avance para continuar.
- **Terminar:** `activa: false`, `terminada: true`.
- **Continuar:** `activa: true`, `pausada: false`; se retoma en `turno`.

### 3.3 Packs (base de taquilla)
- **Juego:** `packs/castigos` =
  `{ titulo: "El Precio del Placer", desc: "Ganar cumple tus deseos; perder despierta la pasión.", icono: "<el del catálogo>", ruta: "Castigos", seccion: "juegos", orden: <n>, activo: true }`.
  **No** lleva `libre` ni `oficial`. La licencia es el item `castigos`.
- **Oficiales:** `packs/ofc_...` =
  `{ titulo, icono, desc, ruta: "Castigos", seccion: "juegos", orden, activo, oficial: true, niveles: { ... }, tomasSugeridas: { ... }, nuevoHasta?, actualizadoEn }`.
  Las acciones de `niveles` son `{ texto, medida }` (sin accesorio).

---

## 4. Archivos y responsabilidades

### 4.1 Nuevos
- **`Castigos/index.html`** — el juego completo (una sola página con vistas, molde
  A de `Guiadas/`/`Encuentros/`). Todo el JS va adentro.
- **`Panel/castigos.html`** — pantalla “Castigos Oficiales” del Panel.
- **`General/Plan-Castigos.md`** — este archivo.

### 4.2 A tocar
- **`Panel/index.html`** — agregar la tarjeta/enlace a `castigos.html` (junto a
  Catálogo y Actividades Oficiales).
- **`herramientas/sintaxis/extract.py`** — **registrar** `Castigos/index.html` y
  `Panel/castigos.html` para que `revisar.py` los revise. (Si no se registran,
  quedan sin revisar para siempre.)
- **`General/GUIA.md`** — al terminar, agregar la sección del juego y sus
  decisiones (una línea que apunte a este plan).
- **`acceso.js`** — **no** se toca si el juego filtra `oficialesAprobados()` por
  `p.ruta === "Castigos"`. Solo si se prefiere un helper dedicado, agregarlo ahí
  (mismo patrón que `oficialesAprobados`).

### 4.3 No tocar en la etapa 1-6
- `Guiadas/`, `Encuentros/`, `Roles/`, `Opciones/`, `Retos/`, `Chat/`,
  `Acompanante/`, `Diablitos/`, `Citas/`. El reparto en rueda a Guiadas/Encuentros
  es la **etapa 7 (pendiente)** y se hace aparte, con pruebas.

---

## 5. Pantallas y flujo

### 5.1 Pantalla de inicio (molde A)
De arriba a abajo:
1. `← Volver` arriba a la derecha → `../index.html#juegos`.
2. Título **“El Precio del Placer”** (degradado, `width:fit-content`) + lema.
3. **Modo:** tres botones/tabs: **Solo / Pareja / Invitados**.
4. **¿Cómo juegan?** **Un celular / Cada quien el suyo** (siempre visible).
5. **¿Quién castiga primero?** (Pareja e Invitados): dos botones con los nombres o
   A/B. En Solo no se pregunta (es el lado del usuario actual).
6. **Normal / Multi.** En Multi, botón de texto **“Sorpréndeme”**.
7. Interruptor **“Placer extremo por deseo”**.
8. Botón **Jugar**.
9. **Engrane ⚙️** (arriba a la izquierda, solo en esta pantalla) → configuración.
10. Abajo: **QR** (para registrar invitados antes de empezar; también está en la
    partida). **Agregar invitado** y los cuadros de **sala/invitados** viven
    dentro de la partida (visibles también en Solo).

### 5.2 Engrane / configuración (vistas)
- **Castigos:** lista con crear, renombrar y borrar. El ✕ del castigo **no borra
  de una**: abre el detalle para editar/borrar y ahí se confirma.
- **Editor del castigo:** niveles × lados. Cada fila:
  - Texto (máx. **60**), **✕** (borra la acción) y **lápiz** (detalle).
  - El **lápiz** abre la ventana: **accesorio opcional** + **medida exclusiva**
    (Libre/Tiempo/Veces) + valor obligatorio si Tiempo/Veces. Guardar/Cancelar.
  - La fila muestra un indicador cuando la acción ya tiene accesorio o medida
    (ej. “3 min”, “×5”, o un punto en el lápiz).
  - La rejilla de **tomas** (5 números compartidos) va en el editor.
  - **Jugar ▶** desde el editor.
  - **Importar / Exportar acciones** (JSON).
- **Accesorios:** catálogo con crear, renombrar, borrar. Al borrar uno en uso,
  **avisar** qué castigos/acciones se afectan; esas acciones quedan sin
  accesorio. **Importar / Exportar accesorios.**
- **Imposiciones:** pestaña con **dos listas (A y B)**, agregar y borrar texto.

### 5.3 Multi
1. Se elige **Multi**.
2. Se marcan **3 castigos** (casillas; sin acciones no se pueden marcar).
3. **Combinar (3/3)** → ventana “¿Son estas 3?” con **Continuar / Reelegir**.
4. **Paso de tomas** (precargado, editable) — se salta si Placer extremo.
5. Se arman las listas y empieza.

**Sorpréndeme:** elige 3 al azar (sin repetir) y abre la misma ventana “Son X, Y
+ Z” con Aceptar/Reelegir.

### 5.4 Turno
- **El que castiga** (su celular):
  1. “Turno de [nombre]”.
  2. Si hay imposición: se muestra + botón **“Aceptar”**.
  3. Al aceptar: **castigo** (“acción con accesorio”) + su medida.
  4. **Libre/Veces:** **“Listo”**. **Tiempo:** **“Iniciar”** → cuenta regresiva +
     **“Listo”**.
  5. “Listo” avanza el turno (el anfitrión escribe en la sesión).
- **El que recibe** (su celular, en “cada quien”): **“Te toca recibir”** +
  imposición (contexto, sin botón) + **solo la acción** (sin medida ni
  cronómetro).
- **Los demás:** **“Turno de [nombre]”** (+ la imposición como contexto).
- **En “un celular”:** se muestra la pantalla del que castiga y el teléfono se
  pasa; no hay pantalla separada de receptor.
- **En Solo:** solo la pantalla del que castiga (se aplica a sí mismo); no hay
  “te toca recibir”.

### 5.5 Controles del anfitrión
- **Revivir** (switch de ancho completo, debajo del recuadro, solo anfitrión).
- **Saltar turno** (solo anfitrión; visible en Solo).
- **Pausar y Salir**, **Terminar Partida**, **QR**, **Agregar invitado** y los
  cuadros de **sala/invitados**: como Encuentros.
- **El “‹ Volver” se oculta durante la partida**; solo se sale con Pausar/Terminar.
- **Fin:** “¡Gracias por jugar!” + fuegos.

### 5.6 Invitados
- Se registran por **QR**: nombre + **“de quién es invitado”** (`conQuien`).
- Pasan a la **sala de espera** (“Esperando invitación…”).
- El **anfitrión** los agrega con **“Agregar invitado”**; ahí entran al juego.
- Su lado sale de `conQuien`.
- Cada invitado recibe **su propia lista**, distinta, del lado de quien lo invitó.
- **A media partida:** copia la lista de un compañero de su lado, solo lo que
  falta (ver 6.6).
- **No tienen salida** (como Encuentros).
- Las licencias **no viajan**: el invitado juega con el acceso del anfitrión.

---

## 6. Algoritmos

### 6.1 Generación de listas (normal y Multi)
Para cada **lado** y cada **nivel**:
1. Reunir las acciones del nivel/lado del castigo (normal) o de los 3 (Multi).
2. **Normal:** pool = esas acciones, barajadas.
3. **Multi:** pool = **reparto en rueda** de los 3 (6.2).
4. Necesarias por lado = `tomas[nivel] × nº de jugadores de ese lado`.
5. Tomar del pool **sin repetir** hasta juntar lo necesario o agotarlo. Si no
   alcanza, repetir (rebarajar).
6. **Repartir** entre los jugadores del lado, `tomas[nivel]` a cada uno, **sin
   repetir**; procurar que cada uno lleve mezcla de los 3 castigos. Si no
   alcanza, repetir.
7. Cada jugador acumula sus acciones por nivel (básico → alucinado). Dentro de
   cada nivel, el orden es aleatorio.
8. Cada acción conserva `accesorio` y `medida`.

### 6.2 Reparto en rueda (Multi)
```
necesarias = tomas[nivel] * jugadoresDelLado
bolsas = [barajar(acciones de cada castigo en nivel/lado)]
pool = []
mientras pool.length < necesarias y quede algo en alguna bolsa:
  para cada bolsa en orden de castigos barajado:
    si la bolsa tiene acciones:
      pool.push(bolsa.pop())
barajar(pool)
si necesarias > pool.length:
  repetir desde el inicio del pool (rebarajando) hasta llegar
```
- El castigo con menos acciones aporta todas las que tiene.
- Nunca se repite hasta agotar el pool.
- El orden final del pool es aleatorio.

### 6.3 Orden y rondas
- `orden` = permutación aleatoria de **todos** los jugadores.
- `rondas` = largo de la lista (todas iguales).
- `turnos` = para ronda 1..R, para cada jugador en `orden`, una entrada con su
  siguiente acción. (Una vuelta = todos una vez.)

### 6.4 Revivir
- Estado en `revivir` (bool).
- `saltado` de un turno = `!revivir && turno.lado !== ladoInicial`, excepto los
  turnos ya `hecho` (no se tocan).
- Al cambiar `revivir`, recalcular `saltado` solo en turnos futuros.
- El turno actual no cambia.
- Las acciones de los turnos saltados **se consumen** (ya están en `turnos`).

### 6.5 Imposiciones
- Al iniciar: por lado, barajar la lista en una “bolsa”.
- Al **jugar** un turno: el anfitrión toma la siguiente de la bolsa de ese lado,
  la escribe en `turnos[turno].imposicion` y actualiza la sesión.
- Turnos saltados: no toman.
- Si la bolsa se vacía: rebarajar y seguir.
- No repetir dentro de la misma ronda (si se puede; si la lista es más corta que
  los turnos de la ronda, se repite).
- Si el lado no tiene imposiciones: `imposicion = null`.

### 6.6 Invitado a media partida
- Se agrega al final de `orden` ( como Encuentros).
- Se le copia la lista del **compañero de su mismo lado** que ya esté en la
  partida, desde el punto actual hacia adelante.
- Juega **solo las rondas que faltan**.
- No se rearma nada de los demás.
- `largo`/`rondas` no cambian.

### 6.7 Placer extremo
- Pool = todas las acciones de `avanzado`, `experto` y `alucinado` del castigo
  (o de los 3, con reparto en rueda).
- Barajar.
- Repartir **sin repetir** entre los jugadores del lado, en partes iguales.
- Si no se puede dividir exacto, repetir para emparejar el largo.
- No usa tomas; el paso de tomas se salta.

### 6.8 Sorpréndeme
- Elegir 3 castigos al azar **sin repetir**.
- Ventana “Son X, Y + Z” con **Aceptar / Reelegir**.
- Aceptar sigue al paso de tomas; Reelegir vuelve a sortear.

---

## 7. Implementación por etapas

> Cada etapa termina con `revisar.py` en verde y, cuando aplique, prueba en vivo.
> No empezar una etapa si la anterior no está estable.

### Etapa 1 — Base y contenido
- Crear `Castigos/index.html` con el esqueleto (molde A), tema visual, `← Volver`
  a `#juegos`, y las vistas vacías.
- Colecciones: `castigosExtra`, `nivelesCastigo`, `accesoriosCastigo`,
  `imposicionesCastigo/actual`.
- Lista de castigos (crear/renombrar/borrar con confirmación).
- Editor por nivel/lado: acciones de 60, ✕, lápiz con accesorio + medida,
  rejilla de tomas, Jugar.
- Catálogo de accesorios (crear/renombrar/borrar con aviso).
- Pestaña de imposiciones por lado.
- Importar/exportar acciones y accesorios.

### Etapa 2 — Inicio y generación (normal y Solo)
- Pantalla de inicio (modos, un celular/cada quien, quién castiga, normal/multi,
  Placer extremo, Jugar, engrane, QR/agregar/sala).
- Paso de tomas (precargado, editable).
- Generación de listas normal y Solo.
- Turnos, orden aleatorio, ronda de todos.

### Etapa 3 — Turno, medidas, imposiciones, Revivir, Saltar
- Pantalla del que castiga (imposición → Aceptar → castigo → medida → Listo).
- Pantalla del que recibe y de los demás.
- Revivir (switch y lógica de `saltado`).
- Saltar turno.
- Pausa/Terminar/Fin con fuegos.

### Etapa 4 — Compartido e invitados
- Sesión `sesionCastigos/actual` en vivo (`onSnapshot`), `runTransaction` para
  avanzar.
- QR, registro con `conQuien`, sala de espera, agregar invitado.
- Invitado a media partida (6.6).
- “Cada quien el suyo”.

### Etapa 5 — Multi, Placer extremo y Sorpréndeme
- Selección de 3, confirmación, tomas.
- Reparto en rueda (6.2).
- Placer extremo (6.7).
- Sorpréndeme (6.8).

### Etapa 6 — Oficiales y Panel
- `Panel/castigos.html` (“Castigos Oficiales”): crear/editar/eliminar, activar,
  fecha NUEVO, tres estados de medida (Libre/Tiempo 1-5/Veces 5-10 con re-sorteo),
  tomas sugeridas, **sin accesorios**, Importar/Exportar JSON.
- Guardar en `packs` con `ofc_`, `oficial: true`, `ruta: "Castigos"`,
  `seccion: "juegos"`.
- En el juego: `oficialesAprobados()` filtrado por `ruta === "Castigos"`,
  `sincronizarOficialesCastigos()` (copia a `nivelesCastigo`), merge en la lista
  con 🏅 y primero.
- Tarjeta del juego `castigos` en `packs` (catálogo del Panel).
- Registrar las pantallas nuevas en `extract.py`.

### Etapa 7 — Pendiente (aparte)
- Aplicar el **reparto en rueda** y el **flujo de tomas de Encuentros** a
  **Guiadas** y **Encuentros**, por etapas y probando en vivo. No mezclar con la
  construcción del juego nuevo.

---

## 8. Pruebas en vivo (criterios de aceptación)

1. **Editor:** crear castigo, 60 caracteres, ✕ borra acción, lápiz guarda
   accesorio + medida; borrar accesorio avisa y deja la acción sin accesorio.
2. **Tomas:** se guardan, se precargan al iniciar y se pueden editar.
3. **Normal 1 a 1:** la lista respeta las tomas; el orden es aleatorio; el juego
   termina cuando se acaban las listas.
4. **Revivir:** apagado, solo juega el lado inicial; encendido, se juegan los dos;
   al prenderlo a media partida, el turno en curso no cambia y el siguiente sí;
   apagarlo vuelve a saltar al otro lado. Las acciones saltadas se consumen.
5. **Saltar turno:** consume el turno, pierde imposición y castigo, avanza.
6. **Imposiciones:** se ven en todos los celulares; solo el que castiga tiene
   “Aceptar”; el que recibe las ve como contexto; no se repiten en la ronda; se
   rebarajan al acabarse; no se consumen en turnos saltados; por lado.
7. **Medidas:** libre/veces con “Listo”; tiempo con “Iniciar”, cuenta en minutos,
   “Listo” siempre disponible, al llegar a cero espera; el que recibe no ve
   medida ni cronómetro.
8. **Pausa:** el cronómetro se detiene y se retoma al continuar.
9. **Invitados:** QR, `conQuien`, sala, agregar; cada uno con su lista; a media
   partida copia la del compañero y juega lo que falta; sin salida.
10. **Multi:** 3 castigos, confirmación, tomas; reparto en rueda (la de menos
    acciones aporta todo, sin repetir hasta agotar); listas distintas; Sorpréndeme
    con Aceptar/Reelegir.
11. **Placer extremo:** todas las de avanzado/experto/alucinado, al azar, sin
    tomas; en Multi con reparto en rueda.
12. **Oficiales:** se ven en el Centro (Juegos) desde el inicio, se piden y
    aprueban; al aprobar se copian a `nivelesCastigo` con 🏅 y primero; sin
    accesorios; las tomas sugeridas solo si no se cambiaron; el aviso de “nuevo”
    funciona.
13. **Panel:** crear oficial con los tres estados de medida y re-sorteo; exportar
    e importar el JSON; se publica en `packs`.
14. **Navegación:** “Volver” a `#juegos`; el botón atrás del celular regresa donde
    debe; el invitado no tiene salida.
15. **Sintaxis:** `revisar.py` en verde (incluye las pantallas nuevas).

---

## 9. Pendientes y riesgos

- **Aplicar el reparto en rueda a Guiadas y Encuentros** (etapa 7). Hoy Guiadas
  usa el mínimo entre 3 y Encuentros el pool proporcional. El cambio es solo en
  el generador, pero hay que probarlo en vivo. Ya está anotado en
  `General/GUIA.md` → “Otros pendientes”.
- **Estandarizar el paso de tomas** en Guiadas (hoy no pregunta en normal) y
  Encuentros, con el flujo de Encuentros.
- **Reglas de Firestore:** las colecciones nuevas viven en la base de la pareja,
  que está abierta a propósito (`allow read, write: if true`). **No** inventar
  reglas nuevas. `sesionCastigos/actual` guarda las listas de todos (incluidos
  invitados) en un solo documento: mismo cuidado que `sesionEncuentros/actual`.
- **Privacidad/Términos/18+:** si el contenido del juego se considera parte de la
  app pública, revisar `Privacidad/` y `Términos/` (decisión de Fredy; no tocar
  sin preguntar).
- **Rendimiento:** el reparto es en memoria con decenas de acciones; no agrega
  lecturas a Firebase. No hay riesgo de lentitud.
- **`extract.py`:** registrar las pantallas nuevas o quedan sin revisar.

---

## 10. Supuestos y decisiones asumidas (revisar con Fredy si algo no cuadra)

Estas se tomaron para que el plan no quede ambiguo. Si Fredy dice otra cosa, se
cambian antes de implementar:

1. **“Quién castiga primero” en Invitados:** se pregunta en la pantalla de inicio
   (A o B), igual que en Pareja. El anfitrión no impone por ser anfitrión: solo
   controla la sesión.
2. **“Cada quien” en Solo:** la opción se muestra; el jugador activo usa su
   celular. El otro teléfono (si existe) solo sigue la partida.
3. **Placer extremo con varios jugadores:** todas las acciones altas se reparten
   sin repetir entre los jugadores del lado, en partes iguales (se repite para
   emparejar si no se puede dividir exacto).
4. **Receptor en invitados:** todo el **lado contrario** ve “Te toca recibir”; el
   grupo decide quién recibe físicamente.
5. **Imposiciones en turnos saltados:** no se consumen; el anfitrión solo toma
   imposición cuando el turno se juega.
6. **Revivir en Solo puro:** oculto. En Solo con invitados de los dos lados,
   visible.
7. **El cronómetro es local** al celular del que castiga; no se sincroniza con el
   del que recibe.
8. **Los oficiales no se renombran**; si se borran, vuelven mientras sigan
   aprobados (reset).

---

## 11. Resumen para el modelo que ejecute

1. Lee `AGENTS.md` y `General/GUIA.md`.
2. Sigue las etapas de la sección 7, en orden.
3. No toques Guiadas/Encuentros hasta la etapa 7.
4. Después de cada cambio: `cd herramientas\sintaxis` y `python revisar.py`.
5. No inventes reglas de Firestore, campos ni textos: usa los de este plan.
6. Si algo no está definido aquí, **pregunta a Fredy** antes de escribir.
7. Al terminar, actualiza `General/GUIA.md` y avisa a Fredy para subir con GitHub
   Desktop y probar en el celular.

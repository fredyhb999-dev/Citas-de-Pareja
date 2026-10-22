# `acceso.js` — Módulo de licencias

Movido de `General/GUIA.md`. Contiene el detalle del módulo central de licencias (`acceso.js`), qué exporta, cómo quedó cada página y el límite de 30 eliminado.

---

> Origen: `Modulo-Accesos.md` (04/10/2026), conservado literal. El módulo `acceso.js` centraliza la lógica de licencias que antes estaba copiada en 4 páginas. **Nada de esto existió en la Fase 1** (ver `HISTORIA.md`).

## 1. Qué se hizo

Antes, la lógica de licencias estaba **copiada** en 4 páginas. La consulta problemática (`solicitudes` con `limit(30)`) estaba escrita **8 veces**.

Ahora las 4 páginas importan todo de un solo archivo: **`acceso.js`**.

**Este refactor NO cambia el comportamiento.** La app debe seguir funcionando exactamente igual. Solo se eliminó la duplicación.

Motivo real del refactor: con la lógica en 8 lugares, cualquier corrección del límite de 30 había que aplicarla 8 veces, y era fácil olvidar una. Con el módulo, es una sola vez.

## 2. Qué exporta `acceso.js`

| Export | Qué hace |
|---|---|
| `miProyecto()` | ProjectId de la pareja. **Se lee en cada llamada**, no al cargar el módulo, porque el Asistente puede escribir el config en `localStorage` después de que la página cargó |
| `appTaq()` | Instancia de la base de taquilla (nombre `"taquilla"`), creada una sola vez |
| `leerLicencias()` | Lee `localStorage["licencias"]` → `{ [item]: "codigo.firma" }` |
| `guardarLicencias(obj)` | Sobrescribe el objeto completo |
| `guardarLicencia(item, cod)` | Guarda un código para un item |
| `quitarLicencia(item)` | Borra el código de un item, sin tocar los demás |
| `tieneCodigoValido(item)` | Verifica firma + item + para + vencimiento |
| `tengoAcceso(item)` | Atajo de `tieneCodigoValido` |
| `oficialesAprobados()` | Packs oficiales que el usuario ya tiene autorizados |
| `escucharItem(item, hooks)` | Escucha **un** item. `hooks.revocado()` / `hooks.aprobado()`. Devuelve la función para cancelar |
| `escucharCatalogo(hooks)` | Revisa **todo** el catálogo. `hooks.cambio(licencias)` |
| `graciasDisponibles()` | Mapa `"item\|email"` → `true` de cortesías sin usar |
| `nuevosSinPedir(packs)` | Mapa `{idDelPack: true}` de lo que está **nuevo Y sin pedir**. Ver *El aviso de "nuevo"* |

### Decisión de diseño: los nombres

Se conservaron los nombres que el código **ya usaba** (`miProyecto`, `appTaq`, `leerLicencias`, `quitarLicencia`…), no nombres nuevos más claros. Motivo: así **casi ninguna llamada cambia** y el diff es mínimo, que es lo que hace seguro un refactor de este tipo.

Excepción: en Tienda e index el lector local se llamaba `leerLic()`; se estandarizó a `leerLicencias()` (9 call sites, cambio mecánico).

### Decisión de diseño: las rutas

`acceso.js` está en la **raíz** y hace sus propios imports con rutas relativas a sí mismo (`./firebase-config.js`, `./config.js`, `./taquilla.js`).

Las rutas de un módulo se resuelven contra la **ubicación del módulo**, no contra el archivo que lo importa. Por eso el mismo archivo funciona igual desde el índice (`./acceso.js`) que desde una carpeta (`../acceso.js`), sin duplicarlo.

## 3. Cómo quedó cada archivo

### `acceso.js` (nuevo, 227 líneas)

Contiene toda la lógica compartida, comentada. Incluye las dos consultas antes repetidas y el `TOPE = 30` en una sola constante con la advertencia del problema documentada.

### `index.html` (menú) — 1149 → ~1055 líneas

| Antes | Ahora |
|---|---|
| `leerLic()` local (3 líneas) | importa `leerLicencias()` |
| `getApp("taquilla-menu")` + `initializeApp` en 3 sitios | `appTaq()` del módulo |
| `gracias` armado a mano (líneas 501-513, con `limit(30)`) | `await graciasDisponibles()` |
| `escucharRevocadosMenu()` (42 líneas, con `limit(30)`) | `escucharCatalogo({ cambio(){ renderPacks(); } })` |

Lo que **quedó aquí**: `tarjetaPack()`, el dibujado del catálogo, el Asistente, el modo invitado y la pantalla de identidad. Nada de eso se tocó.

### `Tienda/index.html` — 404 → ~334 líneas

| Antes | Ahora |
|---|---|
| `appTaq()`, `miProyecto()`, `leerLic()`, `guardarLic()`, `CLAVE_LIC` | importados del módulo |
| `licenciaValida(item)` (6 líneas) | `tieneCodigoValido(item)` del módulo |
| `escuchar()` (49 líneas, 2× `limit(30)`) | `escucharCatalogo({ cambio(){ pintar(); } })` |

Lo que **quedó aquí**: el pintado de tarjetas, el buscador, el login con Google, la petición del item (`addDoc`) y el flujo de re-pedido.

### `Guiadas/index.html` — 1367 → ~1258 líneas

| Antes | Ahora |
|---|---|
| `CLAVE_LIC`, `miProyecto()`, `leerLicencias()`, `tengoAcceso()` (17 líneas) | importados |
| `appTaq()` | importado |
| `quitarLicencia()` | importado |
| `escucharAprobación()` (53 líneas, con `limit(30)`) | `escucharItem(ITEM_ID, { revocado, aprobado })` — 11 líneas |
| `oficialesAprobados()` (17 líneas) | importado |
| `localStorage.setItem(CLAVE_LIC, …)` en 2 sitios | `guardarLicencia(ITEM_ID, cod)` |

Lo que **quedó aquí**: todo el juego (niveles, lados A/B, tomas, MultiActividades, sesión compartida, editor de actividades).

### `Encuentros/index.html` — 1016 → ~921 líneas

Migración **idéntica** a Guiadas (era una copia de ese mismo bloque).

| Antes | Ahora |
|---|---|
| `CLAVE_LIC`, `miProyecto()`, `leerLicencias()`, `tengoAcceso()` | importados |
| `appTaq()`, `quitarLicencia()` | importados |
| `escucharAprobación()` (50 líneas, con `limit(30)`) | `escucharItem(...)` |
| `oficialesAprobados()` | importado |

Lo que **quedó aquí**: la generación de listas por cabeza, los turnos por rondas, `runTransaction`, las tomas, el modo local sin internet.

## 4. Lo que NO se tocó, y por qué

### Las 4 consultas que siguen en las páginas

| Archivo | Línea | Por qué no se centralizó |
|---|---|---|
| `Guiadas/index.html` | 299 | La cortesía necesita **escribir** `graciaUsada` en el documento |
| `Encuentros/index.html` | 373 | Ídem |
| `Tienda/index.html` | 164 | Ídem |
| `Tienda/index.html` | 279 | Evita pedidos duplicados: necesita comparar con las **solicitudes previas** |

No se movieron porque no son solo lectura: dependen del `doc.id` para poder escribir. Centralizarlas exigiría un rediseño (la cola con acuse de `Soluciones.txt`), no un simple traslado.

### Detalle de la instancia de Firebase

Antes `index.html` usaba el nombre `"taquilla-menu"` y las otras tres páginas `"taquilla"`. Ahora **todas usan `"taquilla"`** (la constante `APP_TAQ` del módulo). Misma configuración, así que es equivalente, pero hay una instancia menos.

### Diferencia de comportamiento menor (intencional)

`escucharCatalogo()` hace una lectura extra (`getDocs`) cada vez que se dispara el listener, porque fusionó las dos versiones que existían (la del índice usaba solo el snapshot, la de Tienda re-leía). Lee los mismos datos; solo cambia quién los pide.

## 5. Verificación hecha

Como no hay Node en la máquina, se escribieron verificadores en Python (`Temp\opencode\`):

- **`jscheck.py`** — equilibrio de `{}[]()`, ignorando strings, comentarios y regex literales. Los 7 archivos pasan.
- **`undef.py`** — detecta funciones llamadas pero no definidas ni importadas (la causa clásica de pantalla en blanco). Los 7 archivos pasan.
- **`expcheck.py`** — comprueba que **todo lo que las páginas importan de `acceso.js` exista de verdad**. Esto es crítico: en módulos ES, importar un nombre inexistente rompe la página entera.
- **`argcheck.py`** — que las llamadas a las funciones de `acceso.js` lleven los argumentos correctos.
- **`dupcheck.py`** — que no haya nombres declarados dos veces en un mismo archivo. Esto detectó dos fallas reales durante el refactor.

Estado: los 6 avisos restantes del verificador son falsos positivos preexistentes (identificados **antes** de tocar los archivos).

### Verificación en el celular — HECHA (oct-2026)

No hay navegador ni celular en este entorno, así que esta lista se pasó para que la probara Fredy. **Las 4 quedaron probadas y funcionando:**

| # | Prueba | Resultado |
|---|---|---|
| 1 | Abrir el **menú** en incógnito → cargan las tarjetas y un producto con acceso aparece | OK |
| 2 | Entrar a **Citas Guiadas** y a **Encuentros** → no sale la pantalla de acceso bloqueado | OK |
| 3 | En la **Tienda**, pedir algo desde otro navegador → se activa solo | OK |
| 4 | Revocar desde **Autorizar** → la tarjeta desaparece del menú | OK |

**Con esto el refactor de `acceso.js` queda cerrado: no rompió nada.**

Si alguna vez una de las 4 falla, el error más probable es una ruta de import mal escrita: se ve en blanco la pantalla y la consola dice "Failed to resolve module specifier".

## 6. El límite de 30 — ELIMINADO (oct-2026)

**Resuelto.** Cuando se escribió este documento, el tope seguía puesto a propósito (ese paso era solo centralizar). Después se quitó.

### Por qué se quitó, y por qué NO se usó `orderBy`

La primera idea fue `orderBy("fecha","desc")` para que entraran las 30 más recientes. Se descartó por dos razones:

1. **No arregla el caso peligroso.** Sigue devolviendo solo 30. Una revocación antigua podía seguir sin verse.
2. **Exige crear un índice compuesto** (`para` + `fecha`) en la consola.

Y el motivo para cortar desapareció al revisar el diseño: **la lista no crece sola.** La Tienda reutiliza la misma solicitud por (correo + producto), así que hay como máximo un documento por producto y usuario —unas decenas por pareja, no miles—.

### Qué se cambió

Se quitaron los 6 topes y la constante `TOPE`:

| Dónde | Qué era |
|---|---|
| `acceso.js` → `consultaSolicitudes()` | Cubre `escucharItem` y `escucharCatalogo` |
| `acceso.js` → `graciasDisponibles()` | El mapa de cortesías |
| `Tienda/index.html` | El control de duplicados y la cortesía |
| `Guiadas/index.html` | La cortesía |
| `Encuentros/index.html` | La cortesía |

Ahora cada consulta lee **todas** las solicitudes de la pareja. Efectos:

- Las aprobaciones nuevas siempre se ven (el usuario no se queda bloqueado)
- Las revocaciones antiguas también se ven (el revocado no sigue jugando)
- El control de duplicados vuelve a funcionar → la lista deja de crecer

### Costo

Bajo, porque la lista es chica por diseño. Firestore cobra por documento leído; una pareja normal tiene unas decenas, contra una capa gratis de 50,000 lecturas al día **por proyecto**. ~~El detalle está en `General/Escala-Millones.md`.~~ **Ojo: ese archivo nunca existió en el repo** (oct-2026, revisado). Si algún día hace falta el cálculo, se hace aquí y se deja escrito.

### Lo que NO se tocó

El Panel (`Autorizar/`) ya leía todas las solicitudes (usa `orderBy` sin tope), así que no necesitó cambios.

### Verificación

Los 5 verificadores pasan: sintaxis, referencias, argumentos, imports y nombres duplicados.

## 7. Siguiente paso

> **ACTUALIZADO oct-2026: la lista de abajo YA NO es el siguiente paso.** Los cinco puntos (y el permiso de `borrar`) están **en espera hasta el cambio de arquitectura**, por decisión de Fredy. Ver *Pendientes de licencias — EN ESPERA HASTA EL CAMBIO DE ARQUITECTURA*, donde está la razón de cada uno. **No los arranques por tu cuenta.**

Según lo acordado, el orden era:

1. **Revisar las reglas de Firebase** en la consola — bloqueante, porque el rediseño necesita que la app pueda **borrar** en `solicitudes`.
2. Revocación al entrar en cada página (cierra el acceso por URL directo).
3. Catálogo marcando lo que ya tienes desde local.
4. Cola con acuse (aprobaciones) + revocaciones persistentes.
5. Doc por item + cortesía a local.

Todo está detallado en `Descargas\Soluciones.txt` y los pendientes en `Descargas\Problemas 2.txt`.

## 8. `Panel/oficiales.html`: pegar y exportar la actividad en JSON (17-oct-2026)

Para dar de alta una actividad oficial hay **7 campos sueltos más los 5 niveles × 2 lados de acciones**, y el contenido estaba en documentos sueltos. Ahora la pantalla tiene **"Pegar actividad"** y **"Exportar actividad"**, con el mismo molde que el engrane de `Roles/` (los dos botones en una línea, y la cajita de texto debajo).

| Qué | Cómo funciona |
|---|---|
| **Exportar actividad** | Baja un `.json` con el formulario tal como está (`actividad-<id>.json`). Es la forma de tomar **una actividad que ya está bien como plantilla** |
| **Pegar actividad** | Lee el texto pegado y lo mete al formulario. **Acepta** comillas tipográficas y una coma de más al final; si el JSON está mal, avisa con la pista del navegador y **no carga nada** |
| La forma del JSON | `{ id, titulo, icono, desc, orden, activo, nuevoHasta, niveles:{basico:{A:[],B:[]}, …}, tomasSugeridas:{…} }` |

Lo importante, y por qué el cambio es chico:

- **Lo que pega termina en `pintarForm()`**, que es **la misma función que ya corría al abrir "editar"** de una actividad guardada. O sea: **el relleno ya estaba probado**; lo único nuevo es leer el texto. Por eso **no se cambió cómo se guardan los datos**: se sigue escribiendo en `packs` con la misma forma.
- **`niveles` acepta las dos formas**: si en vez de `A` y `B` separadas se pega una sola lista, `normLadosP()` la pone **en los dos lados**.
- **Si el JSON trae `id`, el campo del ID queda bloqueado**, porque ese campo se bloquea al editar (`pintarForm` hace `fId.disabled = !!f.id`) y el `id` es la licencia, que no se cambia. Se avisa debajo de la cajita; para poner otro, "Limpiar".
- **Pegar borra lo que haya escrito**, así que si el formulario no está vacío **pregunta primero** con `confirmar()` (nunca `alert()` ni `confirm()` del sistema).
- **OJO: el lector de JSON es una COPIA del de `Roles/index.html`, no un módulo compartido.** Se dejó así a propósito, porque unificarlo tocaría `Roles/`, que ya fue probado en vivo. Si algún día se unifica: que vaya a un módulo de la **raíz** (y no a `config.js`, que ya trae Firebase) y se registre en `extract.py`.

> **Bug encontrado al agregarlo:** `Panel/oficiales.html` **no estaba en `extract.py`**, así que el chequeo de sintaxis **nunca lo había revisado** (ni `index.html`, ni `catalogo.html`, ni `permisos.html`). Se agregó `Panel/oficiales.html` a la lista al tocarlo. **Los otros tres se probaron a mano y pasan**, así que se pueden agregar a la lista cuando se toquen.

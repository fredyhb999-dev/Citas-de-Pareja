# Etapa 1 — Base y contenido (editor)

> **Pega este archivo completo como instrucción.** Implementa **solo esta etapa**.

## Antes de escribir

Lee, en este orden:
1. `AGENTS.md`
2. `General/GUIA.md`
3. `General/Plan-Castigos.md` (secciones 1, 2.1, 2.5, 3.1, 4, 5.2)
4. Este archivo.

## Objetivo

Dejar el juego **sin lógica de partida todavía**: solo el esqueleto de la pantalla
y todo el **editor/contenido** (castigos, acciones, accesorios, medidas,
imposiciones, tomas, importar/exportar), guardando en Firestore.

## Tareas exactas

### 1. Crear `Castigos/index.html`
- Una sola página con JS adentro (sin build).
- Tema visual de la app (fondo `#120e1c`, tarjeta `#201933`, borde `#322a4a`,
  coral `#ff6a5c`, teal `#2fd9c7`; Chakra Petch + Inter).
- Molde A, igual que `Guiadas/index.html` / `Encuentros/index.html`:
  `body` en columna, `← Volver` arriba a la derecha (`../index.html#juegos`),
  `.eyebrow`, `h1` con degradado, `.vista`/`.ver`, `.back`.
- Importar: `initializeApp`/`getFirestore`, `resolverFirebase` de `../config.js`,
  `cargarUsuarios` de `../config.js`, `confirmar`/`aviso` de `../confirmar.js`.
- Vistas por ahora: `vistaInicio` (placeholder), `vistaConfig` (lista),
  `vistaEditar` (editor). Deja el arranque blindado con `try/catch`.
- **No** implementes todavía la partida, las listas, los turnos ni la sesión.

### 2. Colecciones y datos
Usa exactamente estas colecciones (ver `Plan-Castigos.md` 3.1):
- `castigosExtra`: `{ nombre, creadoEn? }`
- `nivelesCastigo/{id}`: `{ n, titulo, oficial?, tomas, actualizadoEn }`
- `accesoriosCastigo`: `{ nombre, creadoEn? }`
- `imposicionesCastigo/actual`: `{ A: [...], B: [...] }`

Forma de `n`:
```js
n = { basico:{A:[accion],B:[accion]}, medio:{...}, avanzado:{...}, experto:{...}, alucinado:{...} }
accion = { texto, accesorio: null|"nombre", medida: { tipo:"libre"|"tiempo"|"veces", valor: 0 } }
```
`tomas = { basico:2, medio:2, avanzado:1, experto:1, alucinado:1 }` (numeros).

### 3. Lista de castigos (`vistaConfig`)
- Leer `castigosExtra`.
- Botón para **crear** castigo (nombre).
- Cada castigo: **renombrar** y **borrar** (con `confirmar()`; el borrado elimina
  `castigosExtra`, `nivelesCastigo` y no toca nada más).
- Al tocar un castigo: abrir `vistaEditar`.
- Buscador simple (opcional, igual que Guiadas).
- **No** hay ✕ que borre de una: se entra al detalle y ahí se confirma.

### 4. Editor (`vistaEditar`)
- Título del castigo.
- Para cada nivel (los 5) y cada lado (A/B):
  - Campo “Nueva acción (nivel)” + botón **+**; Enter agrega y regresa al campo.
  - Acciones como chips/renglones con:
    - texto (máx. **60**),
    - **✕** que borra **esa acción**,
    - **lápiz** que abre la ventana de detalle.
  - La acción se guarda como objeto `{texto, accesorio, medida}`.
- Ventana de detalle (modal propio de la página, no `confirmar()`):
  - **Accesorio**: selector opcional desde `accesoriosCastigo` (+ “Ninguno”).
  - **Medida**: exclusiva (radio): **Libre / Tiempo / Veces**.
  - **Valor**: obligatorio si Tiempo o Veces; **Tiempo en minutos** (entero);
    Veces entero. Con Libre se ignora/limpia.
  - Guardar/Cancelar. Guardar escribe en `nivelesCastigo/{id}` con `merge`.
  - La fila muestra un indicador cuando ya tiene accesorio o medida.
- Rejilla de **tomas** (5 números, compartidos por A/B), guardada en `tomas`.
- Botón **Jugar ▶** presente pero **sin lógica todavía** (muestra `aviso()`
  “En construcción” o queda deshabilitado).
- **Importar acciones (JSON)** y **Exportar acciones (JSON)**:
  - Exporta `{ niveles: n }` con las acciones como objetos.
  - Importa tolerante: acepta objetos con `texto`, `accesorio`, `medida`, y
    también texto pelado (se toma como `{texto, accesorio:null, medida:libre}`).
  - Acepta el formato envuelto (`{niveles:...}`) y el mapa de niveles pelado.
  - Pide confirmación si ya hay acciones.
  - Corta textos a 60 y avisa cuántos se cortaron.

### 5. Accesorios
- Vista/pestaña de **accesorios** (`accesoriosCastigo`): crear, renombrar, borrar.
- Al borrar uno usado: `confirmar()` que **avise** que afecta a las acciones que
  lo usan; al confirmar, se borra del catálogo y esas acciones quedan con
  `accesorio: null`.
- **Importar/Exportar accesorios** (arreglo simple de nombres).

### 6. Imposiciones
- Pestaña con **dos listas**: A y B.
- Agregar texto y borrar, guardado en `imposicionesCastigo/actual`.
- Texto puro; no accesorio ni medida.

### 7. Registrar en el chequeo de sintaxis
- Agregar `Castigos/index.html` a `herramientas/sintaxis/extract.py` (misma forma
  que las otras pantallas).

## No hagas todavía
- No implementes la partida (turnos, listas, Revivir, medidas en juego, sesión,
  invitados, Multi, Placer extremo).
- No toques `Guiadas/`, `Encuentros/` ni ningún otro juego.
- No inventes colecciones, campos ni textos fuera de los de este archivo/plan.

## Criterios de aceptación
1. Se puede crear, renombrar y borrar un castigo.
2. Se agregan/quitan acciones por nivel y lado; máx. 60.
3. El lápiz guarda accesorio y una sola medida con su valor.
4. Las tomas se guardan y se vuelven a leer.
5. Los accesorios se crean/renombran/borran; al borrar uno usado avisa y las
   acciones quedan sin accesorio.
6. Las imposiciones A/B se guardan y se leen.
7. Importar/exportar acciones y accesorios funciona (ida y vuelta).
8. `python revisar.py` en `herramientas/sintaxis` sale **en verde**.

## Al terminar, reporta
- Qué archivos tocaste.
- Qué probaste (y qué no puedes probar sin celular).
- Resultado de `revisar.py`.
- Dudas o cosas que no estaban claras.
- **No empieces la Etapa 2.**

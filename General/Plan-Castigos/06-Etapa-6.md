# Etapa 6 — Castigos oficiales y pantalla del Panel

> **Pega este archivo completo como instrucción.** Implementa **solo esta etapa**.
> Antes: lee `AGENTS.md`, `General/GUIA.md`, `General/Plan-Castigos.md`
> (secciones 2.8, 3.3, 4.2, 5.2) y este archivo.
> **Copia el patrón de `Panel/oficiales.html`** y de `Guiadas/index.html`
> (`sincronizarOficiales`, `cargarActividades`).

## Objetivo

Que Fredy pueda crear **castigos oficiales** (`ofc_...`) desde el Panel, que
aparezcan en el Centro y que al aprobarse se copien al banco de la pareja.
Incluye la tarjeta del juego en el catálogo (la crea Fredy) y el registro en el
chequeo de sintaxis.

## Tareas exactas

### 1. `Panel/castigos.html` (“Castigos Oficiales”)
Pantalla nueva, mismo molde que `Panel/oficiales.html`:
- Login con Google + lista de correos que publican (copiar el patrón).
- **Lista** de oficiales (`packs` con `oficial: true` y `ruta: "Castigos"`):
  editar, eliminar, activar/desactivar.
- **Formulario:**
  - **ID** `ofc_...` (empieza con `ofc_`, sin espacios; bloqueado al editar).
  - Título, icono, descripción, orden, activo, fecha NUEVO.
  - **Niveles × lados (A/B):** acciones de **máx. 60** caracteres.
  - **Medida por acción con 3 estados, sin capturar:**
    - **Libre** (por defecto).
    - **Tiempo** → valor al azar **1–5 min**.
    - **Veces** → valor al azar **5–10**.
    - Oprimir otra vez el mismo estado **vuelve a sortear**. El valor **queda
      fijo** al asignarlo.
  - **Tomas sugeridas** (5 números).
  - **Sin accesorios.**
- **Importar** y **Exportar** JSON (mismo formato que el editor de la pareja,
  pero **sin accesorios** y con las medidas).
- **Guardar** en `packs/{id}`:
  ```js
  {
    titulo, icono, desc,
    ruta: "Castigos", seccion: "juegos",
    orden, activo,
    oficial: true,
    niveles: { nivel: { A:[{texto, medida}], B:[...] }, ... },
    tomasSugeridas: { ... },
    nuevoHasta: <fecha o null>,
    actualizadoEn: serverTimestamp()
  }
  ```

### 2. Panel principal
- Agregar en `Panel/index.html` la tarjeta/enlace a `castigos.html`.

### 3. En el juego: oficiales
- En `Castigos/index.html`:
  - `oficialesAprobados()` de `../acceso.js`, **filtrado por**
    `p.ruta === "Castigos"`.
  - `sincronizarOficialesCastigos()`:
    - Para cada oficial aprobado, `nivelesCastigo/{ofc_id}`.
    - Si no existe: crearlo con `{ n, titulo, oficial:true, actualizadoEn }`.
    - Si trae `tomasSugeridas` y la pareja no tiene `tomas`, sembrarlas.
    - Las acciones oficiales **no** traen accesorio (`accesorio: null`).
  - La lista del juego se arma con **`castigosExtra` (tuyos) + oficiales
    aprobadas**, con 🏅 y **primero**.
  - Los oficiales **no** van a `castigosExtra`.
  - **No se renombran.** Si se borra la copia, vuelve a aparecer mientras siga
    aprobada (reset).
  - El aviso de “nuevo” ya cuenta oficiales (`nuevosSinPedir`).

### 4. Pack del juego (lo crea Fredy, no el código)
- En el **catálogo del Panel** (`Panel/catalogo.html`), Fredy crea el pack:
  - ID: `castigos`
  - Título: **El Precio del Placer**
  - Descripción: **Ganar cumple tus deseos; perder despierta la pasión.**
  - Ruta: **Castigos**
  - Sección: **juegos**
  - Icono: el que elija Fredy (no va en el código)
  - Orden, activo.
- El modelo **no** inventa ese pack ni el icono; solo deja documentados los
  campos.

### 5. Registro en sintaxis
- Agregar `Panel/castigos.html` a `herramientas/sintaxis/extract.py`.

## No hagas todavía
- No toques Guiadas/Encuentros (Etapa 7).
- No cambies las reglas de Firestore.
- No inventes credenciales, llaves ni correos.

## Criterios de aceptación
1. Se crea un oficial `ofc_` con acciones y medidas (Libre/Tiempo/Veces con
   re-sorteo).
2. Se guarda en `packs` con `oficial:true`, `ruta:"Castigos"`,
   `seccion:"juegos"`.
3. Exportar e importar el JSON funciona (ida y vuelta).
4. El oficial sale en el Centro (Juegos) desde el inicio y se puede pedir.
5. Al aprobarse, se copia a `nivelesCastigo` con `oficial:true`, 🏅 y primero.
6. Las tomas sugeridas se copian solo si la pareja no las cambió.
7. No trae accesorios.
8. `python revisar.py` en `herramientas/sintaxis` sale **en verde**.

## Al terminar, reporta
- Archivos tocados.
- Qué probaste y qué no.
- Resultado de `revisar.py`.
- Dudas.
- **No empieces la Etapa 7.**

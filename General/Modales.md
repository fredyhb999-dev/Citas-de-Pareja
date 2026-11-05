# Ventanas emergentes y el atrás — registro

Creado nov-2026. Aquí se registra **cada ventana emergente** de la app y cómo se
comporta el **atrás del celular**. Antes de tocar una pantalla, se busca aquí en
vez de barrer el código.

## La regla

- **Sobre la pantalla base** (el primer paso del historial; ahí el atrás sería
  una salida de página): la ventana **guarda su propio paso** al abrirse. El
  atrás la **cierra** y deja la pantalla donde está.
- **Sobre una vista interna** (configuración, editor, partida, pestañas): el
  `popstate` revisa si hay una ventana visible y, si la hay, **ignora** el atrás
  (`history.go(1)`). La ventana se cierra con su botón.
- **Confirmaciones** (`confirmar.js`): siempre guardan un paso; el atrás las
  cierra como **Cancelar** y te deja donde estabas.

**Nunca** se deja una ventana con `display:flex` encima de otra vista: o se
cierra con el atrás o el atrás se ignora.

## Registro

| Pantalla | Ventana (`id`) | Abre en | Atrás | Pieza que lo resuelve |
|---|---|---|---|---|
| Global | Cualquier `confirmar()` / `aviso()` | Cualquiera | **Cierra** (como Cancelar) | `confirmar.js` (`.cfCapa`, paso `{cf:1}`) |
| `index.html` | 🛒 puntos `#invOverlayPts` | Usuarios | **Cierra** | `overlayInvAbierto` + `cerrarPuntos` |
| `index.html` | ✏️ Editar `#invOverlayUsu` | Usuarios | **Cierra** | `cerrarEdUsuarios` (token) |
| `index.html` | 🔑 Clave `#invOverlayPin` | Usuarios | **Cierra / cancela** | `cancelarPinActual` |
| `index.html` | 📜 Historial `#invOverlayHist` | Usuarios | **Cierra** | `cerrarHistorial` |
| Encuentros | `#modalTomas` | Base | **Cierra** | `tomasHist` (paso propio) |
| Encuentros | `#vistaSeguir` (“¿Continuar?”) | Base | **Cierra** | `pasoModalBase` |
| Encuentros | `#modalGracia` | Base | **Cierra** | `pasoModalBase` |
| Encuentros | `#modalUnir` | Base | **Cierra** | `pasoModalBase` |
| Encuentros | `#modalMulti2` | Base | **Cierra** | `pasoModalBase` |
| Encuentros | `#modalFin`, `#modalPausa` | Base / interna | **Cierra / se ignora** | `pasoModalBase` / `modalAbierto` |
| Encuentros | `#modalQR`, `#modalAgregar` | Interna (partida/config) | **Se ignora** | `modalAbierto` |
| Guiadas | `#modalTomas` | Base | **Cierra** | `tomasHist` |
| Guiadas | `#modalMulti2`, `#modalMulti3` | Base | **Cierra** | `mostrarModalBase` |
| Guiadas | `#modalUnir` | Base | **Cierra** | `mostrarModalBase` |
| Guiadas | `#modalGracia` | Base | **Cierra** | `mostrarModalBase` |
| Guiadas | `#modalFin` | Interna (partida) | **Se ignora** | `modalAbierto` |
| Guiadas | `#vistaSeguir` | Interna (paso `.vista`) | **Cierra** | `popstate` (paso) |
| Opciones | `#vistaSeguir` | Base | **Cierra** | `pasoModalBase` |
| Opciones | `#modalModo`, `#modalSolo` | Base | **Cierra** | `pasoModalBase` |
| Opciones | `#modalUnir` | Base | **Cierra** | `pasoModalBase` |
| Opciones | `#modalGracia` | Base | **Cierra** | `pasoModalBase` |
| Opciones | `#modalPausa`, `#modalFin` | Interna (partida) | **Se ignora** | `modalAbierto` |
| Opciones | `#modalAgregar`, `#modalQR` | Base / interna | **Cierra / se ignora** | `pasoModalBase` / `modalAbierto` |
| Roles | `#vistaSeguir` | Base | **Cierra** | `pasoModalBase` |
| Roles | `#modalModo`, `#modalDuelo` | Base | **Cierra** | `pasoModalBase` |
| Roles | `#modalUnir` | Base / interna | **Cierra / se ignora** | `pasoModalBase` / `modalAbierto` |
| Roles | `#modalGracia` | Base | **Cierra** | `pasoModalBase` |
| Roles | `#modalPausa`, `#modalFin` | Interna (partida) | **Se ignora** | `modalAbierto` |
| Roles | `#modalEsp`, `#modalPersonaje`, `#modalMeterInv` | Interna (config/selección) | **Se ignora** | `modalAbierto` |
| Roles | `#modalImagenCarta` | Interna | **Se ignora** | `modalAbierto` |
| Roles | `#modalAgregar`, `#modalQR` | Base / interna | **Cierra / se ignora** | `pasoModalBase` / `modalAbierto` |
| Castigos | `#modalSeguir` | Base / interna | **Cierra / se ignora** | `mostrarModalBase` + `cancelarPausaActual` |
| Castigos | `#modalMultiConf` | Base / interna | **Cierra / se ignora** | `mostrarModalBase` |
| Castigos | `#modalUnir` | Base / interna | **Cierra / se ignora** | `mostrarModalBase` |
| Castigos | `#modalDetalle` | Interna (config) | **Se ignora** | `modalAbierto` |
| Castigos | `#modalQR`, `#modalAgregar` | Interna (partida) | **Se ignora** | `modalAbierto` |
| Castigos | `#modalQuienCastiga`, `#modalImposiciones`, `#modalPlacer`, `#overlayPausa` | Interna (partida) | **Se ignora** | `modalAbierto` |
| Centro | `#modalDeseo`, `#modalAdd` | Base / interna | **Cierra / se ignora** | `pasoBase` / `modalAbierto` |
| Citas | `#overlay` (nueva/editar) | Base | **Cierra** | `formHist` |
| Retos | `#overlay` (nuevo/editar) | Base | **Cierra** | `formHist` |
| Retos | `#overlayRecompensa` | Base | **Cierra** | `recompensaHist` |
| Citas/Actividades | `#modalRenombrar` | Base | **Cierra** | `renameHist` |
| Lencería | `#lupa` | Interna (vestidor/prendas) | **Se ignora** | `modalAbierto` |
| Lencería | `#datos` (exportar/importar) | Interna (config) | **Se ignora** | `modalAbierto` |
| Acompañante | `#modalCfg` | Interna (paso `{cfg:1}`) | **Cierra** | `popstate` (paso) |
| Diablitos | `#pantallaCfg` | Interna (paso `{cfg:1}`) | **Cierra** | `popstate` (paso) |
| Panel/Castigos | `#modalDetalle` | Base | **Cierra** | `detalleHist` |

Notas:

- `Encuentros/#modalMulti3` existe pero **no se usa**. Si se usa, entra por
  `abrirModal` y queda cubierto.
- `Citas/Accesorios`, `Chat`, `Tienda`, `Panel/Oficiales`, `Panel/Permisos`,
  `Panel/index`, `Autorizar`, `Privacidad` y `Terminos` **no tienen ventanas
  propias**; solo usan `confirmar.js` si hace falta.
- En `Opciones/Roles`, `#modalAgregar`/`#modalQR` se abren desde la base (antes
  de la partida) o desde la partida; el envoltorio decide si lleva paso.

## Cómo agregar una ventana nueva

1. Usa `abrirModal`/`cerrarModal` (o `mostrarModalBase` en Guiadas/Castigos) si
   la pantalla ya los tiene. **No** pongas `style.display = "flex"` a mano.
2. Si se abre **sobre la pantalla base**, el envoltorio le da su paso. Si la
   pantalla no tiene envoltorio, agrega el patrón (`pasoModalBase`,
   `mostrarModalBase`, `formHist`, `tomasHist`, etc.).
3. Si se abre **sobre una vista interna**, asegúrate de que el `modalAbierto()`
   de esa pantalla incluya su selector (`.modal`, `[id^="modal"]`, etc.).
4. **Regístrala en la tabla de arriba.**
5. Prueba: abrir → atrás → debe cerrarse o quedarse; atrás otra vez → la
   navegación normal. Ciérrala con su botón y verifica que no quede un paso
   muerto.

## Lo que `revisar.py` revisa (y lo que no)

`revisar.py` **falla** si una ventana del HTML no está registrada en esta tabla
(bloque `== modales ==`). Lo que **no** puede saber es si esa ventana tiene el
paso correcto; eso lo decide la tabla y el checklist. Las confirmaciones de
`confirmar.js` son globales y no necesitan fila propia.

# Modelo de datos — lo que falta normalizar

> **nov-2026.** Esto sigue siendo una **propuesta**: no se aplica sola, y lo que
> rige es el código. Antes era el análisis completo de oct-2026 (552 líneas);
> **casi todo se aplicó** y lo que queda es esto. El relato de lo que se hizo y
> por qué está en **`HISTORIA.md`** → *La normalización de la base*.

**Regla de este documento:** aquí solo va **lo que falta**. Lo que ya se hizo no
se repite con detalle, porque volver a "arreglarlo" es romperlo.

---

## 0. Lo que ya se hizo (no volver a proponerlo)

| Qué | Cómo quedó |
|---|---|
| **Actividades por id** (nov-2026) | `nivelesActividad` y `presetsActividad` se guardan con el id de `actividadesExtra`, no con el nombre. Cada cita lleva `actividadId` junto al nombre. Migra `migrarActividadesAId()` (`config.js`, bandera `config/migracionActividades` versión 2). Renombrar solo cambia el campo `nombre`. |
| **Castigos por id** (oct-2026) | `castigosExtra` y `accesoriosCastigo` usan id automático; `migrarCastigosAId()` convierte lo viejo. Antes renombrar **borraba las acciones**. |
| **Nombres de usuario por id** (nov-2026) | `citas`, `retos`, las sesiones (`cabezas[]`), `invitaciones` y los avisos resuelven el nombre al **mostrar** con `nombrePorId(id, nombreGuardado)` (`config.js`): se ve el nombre de HOY y, si el id ya no existe (dato viejo o invitado borrado), el que quedó guardado. El campo `nombre` se sigue guardando como respaldo y **no se borra**. `chat.autorNombre` y `presencia.nombre` se quedan a propósito: son el nombre del momento. |
| **Historial de puntos** (nov-2026) | Cada movimiento va a `puntos/{uid}/movimientos`; el saldo de `puntosUsuarios` es la caché. Arranca en nov-2026: lo anterior no se puede reconstruir. |
| **B1 — el invitado no volvía solo** | Corregida la ruta (`sesionEncuentros/actual`). Documentado en `GUIA.md`. |
| **B2 — borrar un reto cobrado descontaba** | `eliminarReto()` solo revierte puntos si el reto sigue `enCurso`. |
| **B3 — «Cumplida +1» sin transacción** | Ahora va en `runTransaction`, relee el reto, corta si ya no está `enCurso` y **no descuenta nada al llegar a la meta**. Se registra en el historial. |
| **B4 — dos invitados con el mismo id** | El registro por QR va en transacción, el id lleva hora y azar, y si la ficha sigue viva se reusa. |

> **Números de línea:** los que tenía este documento ya no sirven. Para ubicar
> algo, buscar por nombre de función.

---

## 1. Inventario actual (lo que usa la app)

**Dos bases:** la de la pareja (todo menos la taquilla) y la de la taquilla
(`packs`, `solicitudes`, `config/permisos`).

**Antes había aquí un conteo ("17 colecciones + 3 documentos").** Se quitó: cambió
tres veces y nunca fue exacto. Lo que importa son las rutas.

### Configuración
| Ruta | Forma | Qué guarda |
|---|---|---|
| `config/ajustes` | doc | `usuarios[]`, `actualizadoEn` |
| `config/fabrica` | doc | `version`, `fecha`, `actividades[]`, `accesorios[]` |
| `config/fabricaLenceria` | doc | la siembra del catálogo de lencería |
| `config/migracionActividades` | doc | ids ya migrados (versión 2) |
| `config/migracionCastigos` | doc | mapa de castigos viejos → nuevos |

### Actividades y citas
| Ruta | Forma | Qué guarda |
|---|---|---|
| `actividadesExtra` | col | `nombre`, `creadoEn`, `origen` — id automático |
| `accesoriosExtra` | col | `nombre`, `creadoEn`, `origen` |
| `nivelesActividad` | col (id = id de la actividad) | `n{[nivel]:{A[],B[]}}`, `titulo?`, `oficial?`, `actualizadoEn` |
| `presetsActividad` | col (id = id de la actividad) | `accesorios[]`, `actualizadoEn` |
| `citas` | col | `proponenteId/Nombre`, `paraId/Nombre`, `fechaCita` (texto), `actividad`, `actividadId?`, `descripcion`, `accesorios[]`, `estado`, `creadoEn`, `actualizadoEn`, `ultimaAccionPorId/Nombre` |

### Retos y puntos
| Ruta | Forma | Qué guarda |
|---|---|---|
| `retos` | col | `actividad`, `asignadoPor{}`, `asignadoA{}`, `vecesAlDia`, `duracionDias`, `puntosMeta`, `penalizacionPuntos`, `castigo`, `recompensa`, `conteo`, `estado`, `fechaInicio?`, `fechaFin?`, `cumplidaEn?`, `liquidadoEn?` |
| `puntosUsuarios` | col (id = usuario) | `balance` — caché del saldo |
| `puntos/{uid}/movimientos` | subcol | `monto`, `motivo`, `origen`, `referenciaId`, `referenciaTexto`, `saldoDespues`, `fecha` |

### Chat y avisos
| Ruta | Forma | Qué guarda |
|---|---|---|
| `chat` | col | `texto`, `autorId`, `autorNombre`, `creadoEn` |
| `presencia` | col (id = usuario) | `nombre`, `visto` |
| `invitosChat/actual` | doc | `para`, `creadoEn`, `visto`, `vistoEn?` |
| `invitosRetos/{idDeQuienManda}` | col | `para`, `titulo`, `creadoEn`, `visto` |
| `invitosFavor/{idDeQuienManda}` | col | el aviso de un favor |
| `invitosLenceria` | col | el aviso de un plan de lencería |

### Juegos y sesiones
| Ruta | Forma | Qué guarda |
|---|---|---|
| `opcionesJuego/actual` | doc | `A[]`, `B[]` |
| `sesionGuiada/actual` | doc | `lista[]`, `paso`, `terminada`, … |
| `sesionEncuentros/actual` | doc | `cabezas[]`, `listas{}`, `orden[]`, `turno`, `ronda`, … |
| `sesionOpciones/actual` | doc | `cabezas[]`, `listas{}`, `pares{}`, `eliminadas{}`, … |
| `personajesJuego/actual` | doc | `U1[]`, `U2[]`, `C1[]`, `C2[]`, `ESP[]` |
| `sesionRoles/actual` | doc | `listas{}`, `modoJuego`, `modoBase`, `especiales[]`, … |
| `seleccionRoles/actual` | doc | `sel{}`, `cabezas[]`, `agregar?` |
| `sesionCastigos/actual` | doc | sesión compartida de Castigos |
| `invitaciones` | col (id = juego) | `juego`, `titulo`, `ruta`, `hostUid`, `participantes[]`, `sesion`, `activa`, `pausada`, `sid` |

### Castigos
| Ruta | Forma | Qué guarda |
|---|---|---|
| `castigosExtra` | col | `nombre`, `creadoEn` |
| `nivelesCastigo` | col (id = castigo) | `n`, `titulo`, `oficial?`, `tomas` |
| `accesoriosCastigo` | col | `nombre`, `creadoEn` |
| `imposicionesCastigo/actual` | doc | `{ A:[…], B:[…] }` |

### Centro, favores y lencería
| Ruta | Forma | Qué guarda |
|---|---|---|
| `deseos` | col | los deseos del Centro |
| `comprasDeseos` | col | los pedidos del Centro |
| `favoresExpress` | col | los favores (precio, estado, reloj) |
| `lenceriaPrendas` | col | el catálogo de la pareja |
| `lenceriaPedidos` | col | los planes pedidos |
| `lenceriaVestuarios` | col | lo que tiene cada lado |

### Taquilla
| Ruta | Forma | Qué guarda |
|---|---|---|
| `packs` | col | `titulo`, `icono`, `ruta`, `seccion`, `oficial?`, `niveles?`, `tomasSugeridas?` |
| `solicitudes` | col | `para`, `item`, `email`, `estado`, `fecha`, `codigo?`, `vence?`, … |
| `config/permisos` | doc | la lista de correos que publican |

---

## 2. Lo que falta

### P4 y P5. Las partidas son un documento que crece, con tres esquemas

`sesionEncuentros/actual`, `sesionGuiada/actual` y `sesionOpciones/actual` son el
mismo concepto con tres formas distintas, y a eso se le sumaron Roles y Castigos.

Dos consecuencias:

1. **Techo de 1 MiB por documento.** Con pareja y rondas normales sobra; con
   muchos invitados y muchas rondas hay que mirarlo.
2. **Amplificación de lectura:** el `onSnapshot` está suscrito al documento
   completo. Cuando cambia el turno, **baja otra vez todas las acciones de todos
   los jugadores** a cada teléfono. La escritura sí es barata.

**Propuesta (Fase 4):** `partidas/{partidaId}` con subcolecciones
(`turnos/`, `acciones/`) e `invitaciones.partidaId`. Se va también el `getDoc`
cruzado que causaba el aviso pegado.

### P6. Tipos mezclados

- `citas.fechaCita` es **texto**; `retos.fechaFin` es **`Date`**. Dos formas de
  leer una fecha.
- `solicitudes.graciaUsada` se escribe `true`, `false` o `null` y la lógica busca
  exactamente `=== false`. Funciona, pero un `if(d.graciaUsada)` mal escrito da lo
  contrario.
- `retos.estado` usa cinco valores en dos vocabularios (`"cobrada"` aquí,
  `terminada` en las sesiones).
- `usuarios[].id` tiene dos formatos: `"u1"`, `"u2"` y `"u" + base36(fecha)`.
- `usuarios[].anatomia` es opcional: `"masculino"` o `"femenino"`. Si falta, se
  usa el comportamiento viejo (admin = masculino/A, pareja = femenino/B). Los
  invitados nuevos la eligen al registrarse; los viejos heredan la de quien los
  invitó.

### Fase 5. La identidad (`config/ajustes` → `usuarios/`)

Va **con el login**, no antes: sin login las reglas siguen abiertas y mover la
identidad solo agrega riesgo. Es parte del rediseño de arquitectura que ya está
planeado. Ver `GUIA.md`, *Pendientes de licencias*.

---

## 3. Orden de migración (solo quedan dos)

**No hay `git` en el entorno de trabajo.** Cualquier migración tiene que ser
**aditiva** (escribir lo nuevo junto a lo viejo) y reversible a mano. Fredy prueba
en vivo antes de seguir.

| Fase | Qué | Riesgo |
|---|---|---|
| **4** | Partidas unificadas + `partidaId` en `invitaciones` | **Alto.** Toca los juegos completos y los turnos |
| **5** | Identidad por usuario | **Alto.** Va con el login, al final |

**No se empieza la Fase 4 sin un problema real.** Hoy las partidas caben; si
alguna vez se juega con mucha gente y muchas rondas, se hace entonces.

---

## 4. La decisión de diseño que se mantiene

**Normalizar la identidad; desnormalizar solo el estado de una partida.**

> La desnormalización en Firestore no es un defecto: es el precio de la velocidad
> de lectura y del modo sin conexión. Pero solo se paga donde compra algo. En
> todas partes es deuda.

- **Se paga** en las acciones de una partida: hay que verlas al instante y sin
  red, muchas veces por turno.
- **No se paga** en el nombre de un usuario, el nombre de una actividad o el
  saldo de puntos.

Se descartaron dos extremos, y conviene no volver a proponerlos:

- **Relacional puro:** en Firestore no hay `JOIN`, y sin red no se puede resolver
  ninguna referencia. Habría que reimplementar la base en `localStorage`.
- **Snowflake puro:** mismo problema de fondo; además la partida necesita los
  textos de las acciones en memoria para pintar la pantalla.

**Sí se queda a propósito** (no es deuda): `chat.autorNombre` y `presencia.nombre`.
En un historial de mensajes es correcto guardar el nombre del momento.

---

## 5. Lo que este documento NO hace

- **No cambia reglas de Firebase.** `solicitudes` y la base de cada pareja siguen
  como están, por decisión de Fredy (ver `AGENTS.md`).
- **No propone login.** Eso es el rediseño de arquitectura, aparte.
- **No toca la llave de `taquilla.js`.**
- **No se aplica solo.** Cada fase se prueba en vivo antes de la siguiente.

### Pendiente de Fredy (manual, no se puede hacer desde aquí)

Abrir `pareja-test` en la consola y comparar con el inventario de la sección 1:
confirmar que no quedan colecciones o campos viejos que el código ya no usa.

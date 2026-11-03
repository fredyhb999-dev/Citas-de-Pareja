# Catálogo de Lencería (`Lenceria/`)

Pantalla nueva (nov-2026). Un catálogo de lencería **de la pareja**, con tres
piezas: las **prendas**, los **planes** de vestuario (uno por día) y los
**pedidos** que una persona le manda a la otra.

No lleva licencia, no mueve puntos y **no usa Firebase Storage**: las fotos van
dentro del documento de la prenda.

## De dónde se entra

Menú → **Experiencias en Pareja** → tarjeta **Lencería 👗**, al final.

La tarjeta se agrega en el arreglo `packs` de `renderPacksDeVerdad()`
(`index.html`), **no** en el HTML, con `libre:true`, `necesitaPareja:true`,
`soloPareja:true` y `orden:999`. Su id (`"lenceria"`) está en `FIJOS`.

## Las seis vistas

| Vista | Para qué |
|---|---|
| `vistaPlanes` | Principal, **"Ilusiones y sueños"**: pestañas de lado afuera y recuadro con los planes; el botón de acción va debajo |
| `vistaElegir` | El Vestidor: elegir prendas y fecha, para un plan propio o una propuesta |
| `vistaPedido` | Ajustar y aceptar/rechazar el vestuario que le propusieron |
| `vistaConfig` | **"Ajusta tus ilusiones y sueños"**: prendas y las cuatro clasificaciones, con las pestañas fuera del recuadro |
| `vistaClasif` | Editar o borrar un valor de una clasificación |
| `vistaPrenda` | Alta, edición y baja de una prenda |

Cada vista es un paso del historial (`pushState` + `popstate`), y el
**‹ Volver** es contextual. El ⚙️ **nace oculto** y solo se enciende en
`vistaPlanes`.

El invitado no entra: el menú no le muestra la tarjeta y la pantalla lo
devuelve con un aviso.

## Las dos pantallas con recuadro fijo

La principal y la configuración comparten la misma forma: **pestañas afuera,
recuadro con scroll adentro y la acción abajo.**

- En estas dos pantallas la página mide **exactamente la pantalla** (`body.sinScroll`
  con `height:100dvh`), y el recuadro **se encoge solo** si hace falta. Así el
  botón de abajo nunca se sale. Las demás vistas siguen con scroll normal.
- La pestaña activa se marca **solo con el texto en turquesa y una línea fina
  debajo**, sin bloque de color.
- Los dos recuadros son iguales de forma, pero **el de configuración queda unos
  40 px más bajo**, porque tiene dos renglones de pestañas y la principal uno.

### Principal: "Ilusiones y sueños"

Título **Ilusiones y sueños** y subtítulo **"Planifica y da vida a tu ilusión."**
Pestañas de lado afuera (`A`/`B`, el de uno primero), recuadro con las tarjetas
de plan, la del pedido recibido y la del estado del enviado, y **debajo del
recuadro** el botón **Nuevo plan** / **Proponer**.

Los planes van en **dos secciones**:

- **Próximos:** siempre a la vista, del más cercano al más lejano.
- **Pasados:** **plegados** con un botón **"Ver pasados (N)"**. Al abrirlo
  aparecen, del más reciente al más viejo, con "Ocultar pasados" al final. Así
  la pantalla no se llena aunque pasen los meses. Se pliegan otra vez al cambiar
  de pestaña.

Un plan pasado se marca con la etiqueta **"Usado"** y solo deja **Borrar**.

### Configuración: "Ajusta tus ilusiones y sueños"

El título de la pantalla del engrane es **Ajusta tus ilusiones y sueños** (a
1.5rem, más chico que los demás títulos, porque es largo). **No tiene "Volver"
abajo**: se sale con el **‹ Volver** de la esquina superior derecha.

Las cinco pestañas van **fuera del recuadro**, en dos renglones: **Prendas ·
Tipos · Colores · Zonas · Estilos**. Adentro, el contenido tiene su propio
scroll y el **"agregar" queda fijo abajo**, siempre a la mano.

**Por qué ese orden:** Prendas y Tipos son los que más se tocan (cada prenda
lleva tipo, y los tipos se amplían). Zonas, colores y estilos son casi fijos:
las zonas del cuerpo y los colores no cambian. Decidido con Fredy (nov-2026).

**Prendas** conserva dentro sus propias pestañas de lado (el de uno primero) y
sus chips de zona, con el botón "Nueva prenda" fijo abajo. Los chips se dejaron
a la vista a propósito (un toque para elegir zona) y se apretaron para que los
8 quepan en dos renglones. El filtro de zona de la configuración es
**independiente** del filtro del Vestidor (`filtroZonaConfig` vs `filtroZona`).

### El contador de uso, en la tarjeta

La descripción de cada tarjeta de prenda (en el Vestidor y en la configuración)
**no repite el tipo ni el color**, porque eso ya se ve en la foto. Dice lo que
no se ve: **"8× · 7 nov"**, o **"Nunca usada"** si no se ha usado. La fecha es
la **última vez que estuvo en un plan**, no el día en que se contó.

Se puso ahí y no en el detalle de la prenda porque el momento en que importa es
**cuando se arma el plan**: ahí se decide cambiar una prenda por otra.

## La llave es el id (regla de `GUIA.md`)

- Las **clasificaciones** se guardan por id, nunca por nombre. Renombrar cambia
  solo el campo `nombre` y no toca ninguna prenda.
- Las **prendas** apuntan a `zonaId`, `estiloId`, `tipoId`, `colorId`.
- Las **prendas** y los **planes** guardan **`duenoId`** (el id del usuario),
  además de `lado`. El lado (`A`/`B`) es para las pestañas y para el id del
  plan; de quién es el contenido lo dice `duenoId`. Si cambia quién es el
  administrador, el contenido sigue con su dueño.

## Colecciones

### Clasificaciones

`lenceriaZonas`, `lenceriaEstilos`, `lenceriaTipos`, `lenceriaColores`. Mismo
esquema en las cuatro:

| Campo | Tipo | Qué es |
|---|---|---|
| `nombre` | string | Lo que se muestra. Editable |
| `orden` | number | 10, 20, 30… para ordenar |
| `origen` | string | `"fabrica"` o `"usuario"` |
| `creadoEn` | timestamp | `serverTimestamp()` |
| `actualizadoEn` | timestamp | Solo cuando se renombra |

**Ids fijos de fábrica:** `zona_pecho`, `zona_cintura`, `zona_cadera`,
`zona_piernas`, `zona_pies`, `zona_cuello`, `zona_brazo`; `estilo_romantico`,
`estilo_sensual`, `estilo_atrevido`, `estilo_casual`; `tipo_top`, `tipo_mono`,
`tipo_babydoll`, `tipo_falda`, `tipo_vestido`; `color_negro`, `color_rojo`,
`color_blanco`. Los que crea la pareja usan id automático (`addDoc`).

### `lenceriaPrendas/{autoId}`

| Campo | Tipo | Qué es |
|---|---|---|
| `lado` | `"A"` \| `"B"` | Para mostrar y agrupar |
| `duenoId` | string | Id del usuario dueño. **Manda sobre `lado`** |
| `zonaId`, `estiloId`, `tipoId`, `colorId` | string | Ids de las clasificaciones |
| `foto` | string | Data URL JPEG (`data:image/jpeg;base64,...`) |
| `fotoW`, `fotoH` | number | Medidas de la imagen guardada |
| `vecesUsadas` | number | Empieza en 0 |
| `ultimaFechaUso` | timestamp \| null | La **fecha del plan**, no el momento del conteo |
| `creadoEn`, `actualizadoEn` | timestamp | |
| `creadoPorId` | string | Quién la dio de alta |

No tiene campo `nombre` ni campo `id`: el id del documento ya existe.

### `lenceriaVestuarios/{lado}_{YYYY-MM-DD}`

Ejemplo: `A_2026-11-07`. **El id fijo es lo que garantiza un plan por día.**

| Campo | Tipo | Qué es |
|---|---|---|
| `lado` | `"A"` \| `"B"` | |
| `duenoId` | string | Dueño del plan |
| `fechaTexto` | string | `"YYYY-MM-DD"`: **la fuente de verdad** para comparar |
| `fechaUso` | timestamp | Medianoche local de ese día |
| `prendas` | array de string | Ids de prendas del mismo lado |
| `fijo` | boolean | Si está fijo, no se aceptan pedidos para ese día |
| `contado` | boolean | `false` al crear; `true` cuando ya se liquidó el uso |
| `creadoEn`, `actualizadoEn` | timestamp | |
| `guardadoPorId` | string | Quién lo dejó así |

El plan no guarda nombres ni fotos: solo ids. Las fotos se resuelven con el
catálogo que ya está en memoria.

### `lenceriaPedidos/{idDelReceptor}`

Un documento por receptor: así cada persona tiene como máximo un pedido
pendiente y los dos sentidos no se pisan.

| Campo | Tipo | Qué es |
|---|---|---|
| `deId`, `deLado` | string | Quién propone |
| `paraId`, `paraLado` | string | Quién recibe |
| `prendas` | array de string | Propuesta original |
| `fechaTexto`, `fechaUso` | string / timestamp | Fecha propuesta |
| `estado` | string | `"pendiente"`, `"aceptado"` o `"rechazado"` |
| `creadoEn`, `respondidoEn` | timestamp | |
| `prendasFinales` | array \| null | Lo que quedó al aceptar |
| `fechaFinalTexto` | string \| null | Fecha final al aceptar |
| `modificado` | boolean | `true` si el receptor cambió prendas o fecha |

Se conserva el último pedido con su estado; el siguiente lo sobrescribe. **No
hay historial de pedidos.**

### `invitosLenceria/{idDeQuienEscribe}`

Igual que `invitosFavor`: un documento por quien manda, con `para` apuntando al
otro. Lo lee la campana de `pestana.js` (tipo `lenceria`).

| Campo | Tipo |
|---|---|
| `para`, `de`, `deNombre` | string |
| `titulo`, `aviso` | string |
| `estado` | `"pendiente"` \| `"aceptado"` \| `"rechazado"` |
| `creadoEn` | timestamp |
| `visto` | boolean |

El nombre copiado ahí es **solo texto de la notificación**; los planes y
pedidos no copian nombres.

### `config/fabricaLenceria`

Bandera del sembrador: `version`, `fecha` y los **ids** instalados de cada
grupo. **Va aparte de `config/fabrica`**, porque `asegurarFabrica()` escribe ese
documento completo y borraría estas listas.

## Fábrica de las clasificaciones

`Lenceria/clasificaciones.json` es **instalador y respaldo**. El sembrador
(`sembrarClasificaciones()`, dentro de la pantalla) corre al abrir:

1. Lee la bandera y los ids que ya existen en cada colección.
2. Si el id ya está en la base, **no escribe nada** (así un renombrado no se
   revierte) y lo anota como instalado.
3. Si el id no existe pero está anotado como instalado, **no hace nada** (lo
   borraron y no vuelve).
4. Si no existe y no está instalado, lo crea.
5. Si no se puede escribir, usa el JSON como lista en memoria: la pantalla no se
   rompe.

Los ids fijos hacen el sembrado idempotente: dos dispositivos a la vez escriben
el mismo documento.

## Reglas de negocio

- **Máximo 3 prendas por zona** al armar un plan o una propuesta. El catálogo
  puede tener más.
- **Un plan por día**, garantizado por el id `lado_YYYY-MM-DD`. Guardar o aceptar
  para un día que ya tiene plan **reemplaza**, con confirmación.
- **Fijo** es por plan (por día): no se puede mandar ni aceptar un pedido para
  ese día. El dueño sí puede editar su plan aunque esté fijo.
- **Un pedido por persona**, sin caducidad. El nuevo reemplaza al anterior.
- Quien recibe un pedido puede **cambiar prendas y fecha y aceptar sin pedir
  autorización**. Quien lo mandó ve "Aceptado" o "Aceptado con cambios".
- **Borrar una prenda** avisa, la quita de los planes futuros y del pedido
  pendiente; si un plan se queda sin prendas, se borra. Los planes pasados
  conservan el id y muestran "Prenda eliminada".
- **Borrar una clasificación en uso** se bloquea.
- **Cambiar zona o propietario** de una prenda se bloquea si está en un plan de
  hoy en adelante o en un pedido pendiente, y la pantalla **explica el motivo**
  (antes se apagaban los campos sin decir por qué).

## Conteo de uso

`vecesUsadas` y `ultimaFechaUso` suben **cuando la fecha del plan ya pasó**, no
al guardar. Se liquida al abrir la pantalla y antes de guardar o aceptar.

Va en `runTransaction`: si los dos celulares abren a la vez, solo uno puede
marcar `contado:true`; el otro se sale sin sumar. Sin la transacción, los dos
sumaban y el conteo quedaba doble.

## Avisos

- **Campana de la pestaña:** `pestana.js`, tipo `lenceria` sobre
  `invitosLenceria`. Solo funciona en Chrome/Edge de computadora.
- **Cartelito:** lo pone `pestana.js` con `aviso()`; el texto sale de `titulo` y
  `aviso` del documento.
- **Telegram:** `avisarTelegram()` de `telegram.js`, al proponer, aceptar y
  rechazar. **Nunca** se manda la foto ni un enlace a una foto.
- Cancelar un pedido **no** manda Telegram.

## Fotos

- Una sola imagen por prenda, dentro del documento. **Nada de Storage.**
- Lado máximo **640 px**, JPEG, tope de **150 000 caracteres** (~110 KB); si no
  baja, se prueba a 480 px y después se rechaza.
- Se valida **decodificando** la imagen (no se confía en `file.type` ni en la
  extensión) y se corrige la orientación EXIF con `createImageBitmap`.
- Se puede elegir del carrete o **pegar** (solo Chrome/Edge de computadora con
  HTTPS).

## Límites conocidos (no son bugs)

| Límite | Por qué |
|---|---|
| **Cada apertura vuelve a bajar las fotos** (~1.5–2.5 MB con 30 prendas) | La app **no tiene caché persistente**: Firestore se usa en memoria. No hay copia entre aperturas |
| El peor caso son ~4.5 MB con 30 prendas | Es el tope de 150 000 caracteres por foto, no lo normal (50–90 KB) |
| El conteo se liquida **solo al abrir la pantalla** | No hay reloj en el servidor ni tareas de fondo |
| La campana **solo** funciona en Chrome/Edge de computadora | Los navegadores de celular no dejan cambiar el ícono de la pestaña |
| Las fotos las puede ver cualquiera con la configuración de la pareja | Las reglas de la pareja están abiertas **a propósito** |
| Un pedido por persona, sin historial | El nuevo reemplaza al anterior |
| Borrar un plan usado no revierte el conteo | No hay historial de uso por plan |

## Archivos

**Creados:** `Lenceria/index.html`, `Lenceria/clasificaciones.json` y este
documento.

**Modificados:** `index.html` (tarjeta, `FIJOS`, filtro `soloPareja`),
`pestana.js` (tipo `lenceria`), `herramientas/sintaxis/extract.py`,
`Privacidad/index.html`, `General/GUIA.md`, `AGENTS.md`, `General/Puntos.md`.

**No se tocan:** `config.js`, `asegurarFabrica()`, `acceso.js`, la Tienda, el
Panel y las reglas de Firestore.

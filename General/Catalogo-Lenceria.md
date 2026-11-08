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
| `vistaPlanes` | Principal, **"Ilusiones y sueños"**: pestañas **por persona** afuera y recuadro con los planes; el botón de acción va debajo |
| `vistaElegir` | El Vestidor: elegir prendas y fecha, con la cuadrícula en recuadro y el botón abajo |
| `vistaPedido` | Ajustar y aceptar/rechazar el vestuario que le propusieron, igual que el Vestidor |
| `vistaConfig` | **"Ajusta tus ilusiones y sueños"**: prendas y las cuatro clasificaciones, con las pestañas fuera del recuadro |
| `vistaClasif` | Editar o borrar un valor de una clasificación |
| `vistaPrenda` | Alta, edición y baja de una prenda |

Cada vista es un paso del historial (`pushState` + `popstate`), y el
**‹ Volver** es contextual. El ⚙️ **nace oculto** y solo se enciende en
`vistaPlanes`.

Desde `vistaPlanes` sin venir de una cita, el **‹ Volver** sale a
`../index.html#experiencias` deshaciendo los pasos de la pantalla
(`salirAlMenu()`), no con un enlace normal. Antes el enlace agregaba un paso y,
al volver del menú con el atrás del celular, se regresaba a Lencería (nov-2026).
Si se llegó desde una cita (`esEntradaCita`), el «‹ Volver» regresa a la cita.

El invitado no entra: el menú no le muestra la tarjeta y la pantalla lo
devuelve con un aviso.

## Las pantallas con recuadro fijo

La principal, la configuración, el Vestidor y el ajuste de un pedido comparten la
misma forma: **pestañas o filtros afuera, recuadro con scroll adentro y la
acción abajo.** Así, con muchas prendas o planes, **el botón de guardar nunca
se va**.

- En estas pantallas la página mide **exactamente la pantalla** (`body.sinScroll`
  con `height:100dvh`), y el recuadro **se encoge solo** si hace falta. Así el
  botón de abajo nunca se sale. Las vistas de alta de prenda y de clasificación
  siguen con scroll normal, que ahí sí hace falta.
- La pestaña activa se marca **solo con el texto en turquesa y una línea fina
  debajo**, sin bloque de color.
- Los dos recuadros son iguales de forma, pero **el de configuración queda unos
  40 px más bajo**, porque tiene dos renglones de pestañas y la principal uno.

### Principal: "Ilusiones y sueños"

Título **Ilusiones y sueños** y subtítulo **"Planifica y da vida a tu ilusión."**
Pestañas **por persona** afuera (el de uno primero), recuadro con las tarjetas
de plan, la del pedido recibido y la de la propuesta enviada **mientras está
pendiente**, y **debajo del recuadro** el botón **Nuevo plan** / **Proponer**.
Cada pestaña muestra la ropa y los planes de esa persona, aunque los dos
compartan anatomía.

**Hoy sí cuenta:** al abrir un plan o una propuesta sin fecha, se precarga
**hoy**. Solo se rechaza si la fecha queda vacía o es anterior a hoy.

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

**Orden alfabético en las cuatro listas.** Tipos, Colores, Zonas y Estilos se
muestran **por nombre, de la A a la Z**, y con ese mismo orden salen los chips de
tipo, los desplegables Color/Estilo y los cuatro campos del alta de prenda: es una
sola lista ordenada en un solo sitio. El campo `orden` se sigue guardando en la
base, pero ya no manda en pantalla.

**Prendas** conserva dentro sus propias pestañas **por persona** (el de uno
primero) y sus **chips por tipo**. Las dos pestañas de persona y el botón
**"Nueva prenda"** van **en el mismo renglón**, para no gastar alto: la cuadrícula
gana ese espacio (lo pidió Mary: en su celular se veían muy pocas prendas).

**En Tipos** (la pestaña de al lado) cada tipo tiene una casilla **"Ocupa todo
el cuerpo (vestido, mono)"**. Sirve para que el "Sorpréndeme" y la selección
manual sepan que esa prenda no se combina con otras. Los de fábrica vienen
marcados; si la base ya existía, se marcan solos la primera vez que se abra
—solo si el campo está vacío, así que si los apagaste a mano, se respeta. Los chips se
dejaron a la vista a propósito (un toque para elegir tipo) y se apretaron para
que quepan en dos renglones.

**El filtro es progresivo** (nov-2026, idea de Mary): primero se ve la fila de
chips **por tipo** ("Todos", Top, Mono, Babydoll, Falda, Vestido). Al elegir un
tipo, los chips se recogen y aparece una fila compacta:

```
[ Babydoll ✕ ]   [ Color ▾ ]   [ Estilo ▾ ]
                        Limpiar todo
```

- **Los filtros se suman**: tipo + color + estilo.
- La **✕** de la etiqueta y **"Limpiar todo"** devuelven la fila de chips.
- Los desplegables se llenan con las clasificaciones guardadas, así que crecen
  solos si se agrega un color o un estilo.
- Si no hay prendas con esa combinación, dice **"No hay prendas con esos
  filtros."** (no "no hay prendas todavía", que confundiría).
- El filtro de la configuración es **independiente** del del Vestidor
  (`filtroC` vs `filtroE`).

### El contador de uso, en la tarjeta

La descripción de cada tarjeta de prenda (en el Vestidor y en la configuración)
**no repite el tipo ni el color**, porque eso ya se ve en la foto. Dice lo que
no se ve: **"8× · 7 nov"**, o **"Nunca usada"** si no se ha usado, y al final la
**referencia** si la tiene: **"8× · 7 nov · R-12"**. La fecha es la **última vez
que estuvo en un plan**, no el día en que se contó.

**Si fue hace siete días o menos**, en vez de la fecha dice **"hace 2 días"** (o
"ayer", o "hoy") y la línea se pinta en **coral** en lugar de turquesa. Es un
aviso suave —"esta ya la usaste"— sin mensaje ni bloqueo.

### Orden de las prendas

**Vestidor y Ajustar pedido** (la misma cuadrícula): una sola lista, **sin agrupar
por zona**. Primero las **nunca usadas** y después las usadas; dentro de cada grupo,
por **referencia** (`top-1`, `top-2`, `top-10`: el número se compara como número, no
como texto).

**Pestaña Prendas de la configuración**: **solo por referencia**, sin mirar el uso:
ahí se busca una prenda por su referencia.

En las dos, las prendas sin referencia van al final (no debería quedar ninguna; ver
*Referencias*).

**Sorpréndeme** no depende de ese orden: elige la más olvidada de cada zona
comparando la fecha de uso.

### Referencias: ni vacías ni repetidas

**La referencia se llena sola:** las **tres primeras letras del tipo** y un número
consecutivo — `top-1`, `top-2`, `ves-1`, `bab-1`.

- Se calcula con el **mayor número que ya exista** de ese prefijo y se suma uno. Por
  eso **no se repite ni se reutiliza**: si borras `top-2`, la siguiente sigue siendo
  `top-3`. La numeración es **de toda la pareja**, no por lado, para que `top-1` no
  signifique dos cosas distintas.
- **Se puede escribir a mano.** Si cambias el tipo y la referencia seguía siendo la
  automática, se regenera con el prefijo nuevo; si la escribiste tú, no se toca.
- Máximo **8 caracteres**, para que quepa en la tarjeta.
- **Al guardar**, una referencia vacía se llena sola y una repetida se rechaza con un
  aviso. Se comparan sin mayúsculas ni acentos.
- **Al abrir la pantalla** se revisan las que ya estaban mal: a la que no tiene se le
  pone la siguiente de su tipo y, de las repetidas, conserva la referencia **la más
  antigua**. Un aviso dice cuántas se corrigieron. Sin internet no se corrige nada y
  se reintenta en la siguiente apertura.
- **Importar prendas** pasa por esa misma revisión al terminar.

### "Sorpréndeme"

Botón en el Vestidor que arma un conjunto **respetando las reglas**:

- Si hay un **vestido o un mono** (tipo marcado "ocupa todo el cuerpo"), elige
  ese y, si hay, unos zapatos.
- Si no, elige **una prenda por zona**, la más olvidada de cada una.
- Respeta los filtros activos; si no dejan nada, usa todo el catálogo del lado.
- No guarda: solo deja la selección puesta para que la ajustes y le des Guardar.

**El botón de ampliar.** Cada tarjeta con foto tiene un botón redondo en la
esquina inferior derecha con **dos flechas en diagonal** (dibujadas en SVG, no
como símbolo de texto: cada teléfono dibuja los símbolos distinto). Abre la
imagen a pantalla completa y se cierra tocando. No estorba al toque normal de la
tarjeta —que selecciona la prenda o abre el editor— porque el botón detiene el
toque. La vista previa del formulario también se abre en grande al tocarla.

**Las clasificaciones se actualizan en vivo** (`onSnapshot` de las cuatro
colecciones). Sin eso, si la otra persona agrega un tipo, tu lista no lo tendría:
los chips no lo mostrarían y al abrir una prenda suya el select caería en el
primer tipo y lo cambiaría al guardar.

Se puso ahí y no en el detalle de la prenda porque el momento en que importa es
**cuando se arma el plan**: ahí se decide cambiar una prenda por otra.

## La llave es el id (regla de `GUIA.md`)

- Las **clasificaciones** se guardan por id, nunca por nombre. Renombrar cambia
  solo el campo `nombre` y no toca ninguna prenda.
- Las **prendas** apuntan a `zonaId`, `estiloId`, `tipoId`, `colorId`.
- Las **prendas** y los **planes** guardan **`duenoId`** (el id del usuario),
  además de `lado`. El lado (`A`/`B`) sale de la **anatomía** (A = masculino,
  B = femenino) y es solo el contenido; de quién es la ropa y el plan lo dice
  `duenoId`. Las pestañas y los ids de plan son **por persona**. Cambiar quién
  administra no mueve nada.

## Colecciones

### Clasificaciones

`lenceriaZonas`, `lenceriaEstilos`, `lenceriaTipos`, `lenceriaColores`. Mismo
esquema en las cuatro:

| Campo | Tipo | Qué es |
|---|---|---|
| `nombre` | string | Lo que se muestra. Editable |
| `orden` | number | 10, 20, 30… Se conserva en la base; la pantalla ordena alfabético |
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
| `ref` | string | Referencia corta y automática (máx. 8): `top-1`, `ves-1`. **Única en la pareja y nunca vacía** |
| `foto` | string | Data URL JPEG (`data:image/jpeg;base64,...`) |
| `fotoW`, `fotoH` | number | Medidas de la imagen guardada |
| `vecesUsadas` | number | Empieza en 0 |
| `ultimaFechaUso` | timestamp \| null | La **fecha del plan**, no el momento del conteo |
| `creadoEn`, `actualizadoEn` | timestamp | |
| `creadoPorId` | string | Quién la dio de alta |

No tiene campo `nombre` ni campo `id`: el id del documento ya existe.

### `lenceriaVestuarios/{duenoId}_{YYYY-MM-DD}`

Ejemplo: `u1_2026-11-07`. **El id fijo es lo que garantiza un plan por día y por
persona.** Los planes viejos con id `A_...` o `B_...` se siguen leyendo por
`lado`/`duenoId`; al moverlos o volver a guardarlos se pasan al id por persona.

**Fechas:** se guardan y comparan siempre como `YYYY-MM-DD`.

| Campo | Tipo | Qué es |
|---|---|---|
| `lado` | `"A"` \| `"B"` | |
| `duenoId` | string | Dueño del plan |
| `fechaTexto` | string | `"YYYY-MM-DD"`: **la fuente de verdad** para comparar |
| `fechaUso` | timestamp | Medianoche local de ese día |
| `prendas` | array de string | Ids de prendas del mismo dueño |
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
| `estado` | string | Solo `"pendiente"`: al aceptar o rechazar, el pedido **se borra** |
| `creadoEn` | timestamp | |
| `congelado` | boolean | Quien propone pidió que **no se pueda cambiar**: solo aceptar o rechazar |

**Al aceptar o rechazar el pedido se borra**, porque ya cumplió:

- **Aceptado:** el plan de verdad queda guardado en `lenceriaVestuarios` (el de
  quien aceptó, con la fecha final y las prendas finales). La constancia para
  quien propuso es ese plan, más el aviso de Telegram y la campana.
- **Rechazado:** no hay plan ni nada que esperar.

Así la tarjeta **"Tu propuesta"** no se queda pegada para siempre. El siguiente
pedido reemplaza al anterior. **No hay historial de pedidos.** Los pedidos viejos
que quedaron guardados como `aceptado` o `rechazado` se borran solos la primera
vez que cualquiera abra la pantalla.

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
  **El porqué (de Fredy, nov-2026):** pensó en capas — bra, blusa y chamarra van
  en la misma zona, y cada una puede ser un tipo distinto. El tope cuenta
  **zonas, no tipos**: se permiten tres capas sobre la misma parte del cuerpo.
  Si algún día se quiere una cuarta capa, se cambia el número sabiendo esto.
- **Un vestido o un mono no se combinan** con otras prendas: el tipo se marca
  como **"ocupa todo el cuerpo"** (Configuración → Tipos) y solo admite prendas
  de los pies. Si el plan ya tiene uno, se bloquea agregar otra cosa; y si ya hay
  prendas, se bloquea agregar el vestido. Es coherencia, no gusto.
- **Un plan por día**, garantizado por el id `lado_YYYY-MM-DD`. Guardar o aceptar
  para un día que ya tiene plan **reemplaza**, con confirmación.
- **Fijo** es por plan (por día): no se puede mandar ni aceptar un pedido para
  ese día. El dueño sí puede editar su plan aunque esté fijo.
- **Un pedido por persona**, sin caducidad mientras su fecha siga en el futuro.
  El nuevo reemplaza al anterior. **Al aceptarlo o rechazarlo se borra** (ver
  `lenceriaPedidos`): ya no queda nada que consultar.
  **Si la fecha pasa sin respuesta, el pedido se borra** la siguiente vez que
  cualquiera de los dos abra la app (y se apaga su aviso): ya no sirve, porque no
  se aceptó. Mientras la pantalla siga abierta de un día para otro, se ve como
  **"Vencido"**; al volver a entrar, ya no está.
- **Un pedido nunca cuenta como "usado".** El conteo solo mira los **planes**:
  si no se aceptó, nunca hubo plan, así que no suma nada.
- Quien recibe un pedido puede **cambiar prendas y fecha y aceptar sin pedir
  autorización**. Quien lo mandó se entera por **Telegram y por la campana**, y
  ve el plan ya guardado en la pestaña de quien aceptó (con los cambios, si los
  hubo).
  **Salvo que la propuesta venga congelada**: al proponer hay una casilla *"Que no
  lo pueda cambiar"* (`congelado: true`). En ese caso el receptor **no puede
  tocar prendas ni fecha**: solo aceptar o rechazar, y la tarjeta lo marca como
  **"Sin cambios"**.
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

**Cuenta planes, no usos confirmados** (decisión de Fredy y Mary, nov-2026): si
se planeó y la fecha pasó, suma, aunque no se lo hayan puesto. Preguntar "¿sí lo
usaste?" sería una carga para un dato que la app no puede comprobar, y quien no
le interese el número simplemente lo ignora. La app da la pauta; no pone policía.

Por lo mismo, **borrar un plan pasado no devuelve el conteo**: ya está aplicado y
no hay historial por plan. Es un límite consciente, no un descuido.

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
- Se puede elegir con **tres botones**: **Cámara** (abre la cámara del teléfono
  directo, con `capture="environment"`), **Carrete** (el carrete de fotos) y
  **Pegar**. En la computadora, "Cámara" abre el explorador de archivos, porque
  no hay cámara.
- La cámara necesita **HTTPS**: la app publicada en Pages ya lo es; abrir el
  archivo local no la habilita.
- Pegar solo funciona en Chrome/Edge de computadora con HTTPS.

## Entrar desde una cita

Cada tarjeta de cita tiene un botón **👗**. **No sale en citas pasadas** (no se
puede crear nada para ayer).

**El icono muestra, no propone.** Al tocarlo abre Lencería en la pestaña de
**quien oprime el botón** (la persona actual): ahí se ve **su plan** si ya existe,
o **la propuesta pendiente** si todavía no hay plan. Llega con
`?fecha=AAAA-MM-DD&persona=<id>&lado=A|B&modo=ver`.

**Proponer** el atuendo se ofrece en otros dos momentos, no desde el icono:

- Al **crear** una cita: después de guardarla, pregunta *"¿Quieres proponer el
  atuendo de X?"*. Si dice sí, va a Lencería con la fecha y la persona
  (`modo=proponer`), se arma la propuesta y se regresa a Citas.
- Al **confirmar** o dar **"Enterado"**: la misma pregunta, apuntando a la otra
  persona de la cita.

Si dice que no, la cita sigue su curso normal.

El enlace **no se guarda en la base**: se calcula con la fecha de la cita. Por
eso, si la cita se mueve de día, el botón apunta solo al día nuevo. Y el
**"‹ Volver"** regresa a la cita: se reemplaza el paso del historial para que no
caiga en la pantalla principal de Lencería.

### Mover la fecha de la cita

Al guardar una cita con fecha nueva, **antes** de guardarla la app revisa el día
viejo y, si hay algo, pregunta con una lista de lo que va a mover:

- **Planes de las dos personas** de ese día → al día nuevo.
- **Propuestas pendientes** de ese día → al día nuevo.

Y avisa si el día nuevo **ya tiene** un plan de esa persona: se reemplaza.

- **Un plan no se puede renombrar**, así que se crea el nuevo (`lado_fecha`) y se
  borra el viejo.
- **Si el día viejo ya pasó**, no se mueve nada: el conteo de uso ya se aplicó.
- **Si el día nuevo es pasado**, tampoco (la app no crea planes en el pasado).
- Si no hay nada que mover, no pregunta nada y la cita se guarda normal.
- Si cancelas el aviso, **la cita no se guarda**.

## Pasar prendas a otra instalación (exportar / importar)

Al final de **Ajusta tus ilusiones y sueños** hay cuatro botones discretos:
**Exportar prendas**, **Importar prendas**, **Exportar listas** e **Importar
listas**. Es para **mudanzas puntuales** entre dos instalaciones (por ejemplo, de
la app de prueba a la personal), **no** una función para clientes.

**Están ocultos** para no quitarle alto a la cuadrícula: se abren (y se cierran)
con **cinco toques seguidos en el rótulo "LENCERÍA"**, arriba de la pantalla.

- **Prendas** lleva las prendas y sus fotos. **Listas** lleva zonas, estilos,
  tipos y colores en un solo archivo: van juntas porque cada prenda apunta a las
  cuatro, y exportar solo una dejaría las demás a medias.
- **Exportar** genera un JSON y **Descargar** lo guarda como
  `lenceria-prendas-AAAA-MM-DD.json` o `lenceria-listas-AAAA-MM-DD.json` (ese
  archivo es el que se manda por WhatsApp); también se puede copiar el texto.
- **Importar** acepta el archivo con **Elegir archivo** o el texto pegado.
  Conserva los **ids**, así las prendas siguen apuntando a su zona, estilo, tipo y
  color, y los planes a sus prendas. En las prendas además **traduce el dueño**:
  el `duenoId` que venía de la otra base se reemplaza por el usuario de esta que
  corresponde a la misma **anatomía** (A = masculino, B = femenino).
- **No copia pedidos ni avisos**: son pasajeros.
- Si alguna clasificación usada no existe en esta base, avisa al terminar: es la
  señal de que las listas no quedaron iguales.
- Se puede correr varias veces: lo que ya está se sobrescribe, no se duplica.
- **No borra** lo que sobre en la base destino: si allá existe algo que aquí ya
  no, se queda. Para igualar borrando haría falta otro modo, y no está hecho.

> **PENDIENTE ANTES DE VENDER:** **quitar estos cuatro botones.** Son una
> herramienta de mudanza entre la app de prueba y la personal, no una función de
> cliente: alguien podría duplicar o pisar su base sin saber qué hace. Está
> anotado también en `General/GUIA.md`, en *Otros pendientes*.

## Límites conocidos (no son bugs)

| Límite | Por qué |
|---|---|
| **Cada apertura vuelve a bajar las fotos** (~1.5–2.5 MB con 30 prendas) | La app **no tiene caché persistente**: Firestore se usa en memoria. No hay copia entre aperturas |
| El peor caso son ~4.5 MB con 30 prendas | Es el tope de 150 000 caracteres por foto, no lo normal (50–90 KB) |
| El conteo se liquida **solo al abrir la pantalla** | No hay reloj en el servidor ni tareas de fondo |
| La campana **solo** funciona en Chrome/Edge de computadora | Los navegadores de celular no dejan cambiar el ícono de la pestaña |
| Las fotos las puede ver cualquiera con la configuración de la pareja | Las reglas de la pareja están abiertas **a propósito** |
| Un pedido por persona, sin historial | El nuevo reemplaza al anterior |
| El conteo mide **planes**, no usos confirmados | Si se planeó y la fecha pasó, cuenta. Pedir confirmación sería una carga y la app no puede comprobarlo |
| Borrar un plan usado no revierte el conteo | No hay historial de uso por plan |

## Archivos

**Creados:** `Lenceria/index.html`, `Lenceria/clasificaciones.json` y este
documento.

**Modificados:** `index.html` (tarjeta, `FIJOS`, filtro `soloPareja`),
`pestana.js` (tipo `lenceria`), `herramientas/sintaxis/extract.py`,
`Privacidad/index.html`, `General/GUIA.md`, `AGENTS.md`, `General/Puntos.md`.

**No se tocan:** `config.js`, `asegurarFabrica()`, `acceso.js`, la Tienda, el
Panel y las reglas de Firestore.

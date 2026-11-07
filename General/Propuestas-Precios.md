# Propuestas de los 5 números del carrito

Creado nov-2026. Detalle de la pantalla **Usuarios → 🛒** y de la regla nueva:
**los 5 números no cambian sin que los dos estén de acuerdo.**

## Qué cambió

Antes, el botón **Guardar** del carrito escribía los valores de una vez, sin
preguntarle al otro. Desde nov-2026 el botón dice **Proponer**:

- El que cambia los números **propone**; eso ya cuenta como su "sí".
- El **otro perfil base** recibe la propuesta y la **aprueba** o la **rechaza**.
- Mientras no haya acuerdo, **los valores que están en uso no se tocan**. El
  Centro de Adquisiciones y el Favor Express siguen leyendo lo mismo de siempre.

Los **saldos** (`puntosUsuarios/{id}.balance`, los que se editan en «✏️ Editar
nombres y administrador») **no entran aquí**: se siguen cambiando libres, como
decidió Fredy. Esta regla es solo para los 5 números del 🛒.

## Los 5 valores

| Campo | Qué es | Unidad | Quién lo usa |
|---|---|---|---|
| `ptsActivar` | Puntos para activar un deseo | pts | Esa persona, al poner un deseo en venta |
| `precioCompra` | Precio para comprar un deseo | pts | Esa persona, al comprar |
| `precioFavor` | Precio de un Favor Express | pts | Esa persona, al pedir el favor |
| `pctCastigo` | Castigo si aceptan y no cumplen | % | Esa persona, al pedir el favor |
| `minutosFavor` | Minutos para cumplir un favor | min | Esa persona, al pedir el favor |

Los valores viven en **`config/ajustes.usuarios`**, en el mismo objeto del
usuario, como siempre. **No se mudaron ni se renombraron.** Los defectos, cuando
el campo no existe, son los mismos de antes: **500, 100, 15, 50 y 10**.

## Cómo funciona, dato por dato

- **Los 5 números son de cada usuario**, dentro de su objeto. No son de la pareja ni
  del dispositivo.
- **El 🛒 sale solo en tu propia fila.** Cada quien propone lo suyo; la fila de tu
  pareja y la de los invitados no tienen carrito.
- **El que aprueba es siempre el otro** perfil base: nadie aprueba sus propios
  cambios. Mary propone los suyos y Fredy aprueba; Fredy propone los suyos y Mary
  aprueba.
- **La propuesta guarda los dos ids:** `paraId` (de quién son los números, que es
  quien propone) y `deId` (quién la propone). Los nombres se copian solo para el aviso.
- **El que recibe sabe de quién es el dato:** el título dice quién propone ("Mary
  propone") y el detalle dice de quién son los números: **"de sus números"** para el
  que aprueba y **"de tus números"** para el que propuso. Ejemplo, en el teléfono de
  Fredy: *"Mary propone · «Precio de un Favor Express» de sus números: de 15 pts a
  20 pts."*
- **Si los dos proponen el mismo campo**, la propuesta nueva reemplaza a la anterior
  (regla 3). Quien había propuesto la vieja no recibe un aviso: deja de estar en
  "Tuyas" y ya.

## La regla

1. **Cada quien propone lo suyo.** El 🛒 sale **solo en tu propia fila**: ni en la de
   tu pareja ni en la de invitados. Solo los dos perfiles base proponen y aprueban.
2. **El que propone ya dio su "sí".** El que aprueba es el otro perfil base.
3. **Una propuesta por campo.** Si hay una nueva para el mismo campo, **reemplaza
   a la anterior** (aunque sea de la otra persona). Así no quedan dos valores
   peleando por el mismo campo.
4. Se pueden tener **varias propuestas a la vez** (hasta una por cada uno de los
   5 campos).
5. **No se propone lo que no cambió**: se compara contra el valor que está en uso,
   con sus defectos. Si no cambió nada, el carrito dice "No cambiaste ningún
   valor" y no manda nada.
6. **Un favor ya pedido no se toca.** Su precio, castigo y minutos se congelaron
   al crearlo; aprobar un cambio solo afecta a los favores nuevos.

## Dónde se ve

**No hay ventana al abrir la app.** El aviso vive en dos lugares:

1. **Puntito rojo con número en el ⚙️** del menú. Cuenta lo que necesita tu
   atención: propuestas para aprobar y resultados que no has visto. Si no hay
   nada, no hay puntito.
2. **Tarjeta «Propuestas» al inicio de Usuarios.** Solo aparece si hay algo.
   Dentro hay dos listas:
   - **Para ti:** aceptar o rechazar, una por una. Si hay más de una, también
     «Aceptar todas» y «Rechazar todas».
   - **Tuyas:** las que esperan (con «Cancelar») y los resultados ya resueltos
     («✅ Aceptada» / «❌ Rechazada»).
3. El resultado **se marca como visto** al cerrar la ventana y deja de contar en
   el puntito. La próxima vez que entre, el que propuso se entera ahí.

## En la base

Colección nueva: **`propuestasPrecios`**. Un documento por propuesta, con id
automático.

| Campo | Qué guarda |
|---|---|
| `paraId` | Id del usuario cuyos números cambian |
| `paraNombre` | Nombre de esa persona, solo para mostrar el aviso |
| `campo` | `ptsActivar`, `precioCompra`, `precioFavor`, `pctCastigo` o `minutosFavor` |
| `valorActual` | El valor que estaba en uso cuando se propuso |
| `valorNuevo` | El valor propuesto |
| `deId` | Id de quien propone |
| `deNombre` | Nombre de quien propone, solo para el aviso |
| `estado` | `pendiente`, `aceptada` o `rechazada` |
| `vistoPorProp` | `false` hasta que el que propuso ve el resultado |
| `creadoEn` | Fecha de la propuesta |
| `resueltoEn` | Fecha en que se aceptó o rechazó |

La llave es **el id** (`paraId`, `deId`). Los nombres se copian **solo para el
texto del aviso**, como en las invitaciones: si alguien se renombra, la propuesta
vieja muestra el nombre del momento.

**Reglas de Firebase:** la base de cada pareja sigue con `allow read, write: if
true`, así que **no hay que tocar nada en la consola**. Si algún día se limitan
las reglas a las rutas que usa la app, hay que **agregar `propuestasPrecios` a la
lista**.

**Sin login, esto es de buena fe.** Quien escriba directo en Firestore puede
saltarse la aprobación, igual que se salta el PIN. La protección real llega con
el cambio de arquitectura (login + reglas por correo), que sigue pendiente.

## Cómo se acepta (y el cuidado)

Al aceptar se **relee `config/ajustes` fresca**, se cambia **solo ese campo** y se
guarda la lista completa con `setDoc(..., {merge:true})`. Después la propuesta
pasa a `aceptada`.

**Antes de aplicar, también se relee la propuesta.** Si ya no está `pendiente`
(la cancelaron o la resolvieron en el otro teléfono), **no se toca nada**: se avisa
que ya no existe o que ya no está pendiente. Así no se recrean documentos fantasma
ni se aplica algo que el otro ya rechazó.

Si el valor en uso **ya no es el que se propuso** (cambió por otra vía mientras
se decidía), **no se pisa a ciegas**: se actualiza el `valorActual` de la
propuesta, se avisa "El valor cambió mientras decidías (ahora es X)" y se pide
volver a aceptar. No hay forma de que una propuesta vieja borre un cambio nuevo
sin que la persona lo vea.

El botón «Cancelar» de **Tuyas** borra la propuesta pendiente de quien la mandó;
la otra persona no puede cancelarla.

## Piezas en el código

Todo vive en `index.html`:

- `CAMPOS_PROP`, `valorEfectivoProp()`, `valorPropValido()`, `textoValorProp()`.
- `invPtsGuardar` (antes Guardar, ahora **Proponer**).
- `iniciarPropuestas()`, `propuestasCache`, `actualizarAvisoPropuestas()`.
- `pintarPropuestas()`, `abrirPropuestas()`, `cerrarPropuestas()`.
- `aceptarPropuesta()`, `rechazarPropuesta()`, `cancelarPropuesta()`,
  `resolverTodasPropuestas()`.
- Ventana `#invOverlayProp` (registrada en `General/Modales.md`), tarjeta
  `#invPropCard`, puntito `#gearDot`.

`Retos/centro.html` y `favor.js` **no se tocaron**: leen los mismos campos de
siempre. `index.html` avisa por `onSnapshot` de la colección nueva.

## Prueba en vivo (pendiente en el celular de Fredy)

1. Con los dos teléfonos: en Usuarios → 🛒 de Mary, cambiar los 5 valores y
   tocar **Proponer**. Deben salir 5 propuestas.
2. En el teléfono de Fredy: aparece un **5** en el ⚙️ y la tarjeta
   **Propuestas** con las 5.
3. Aceptar dos y rechazar una. Verificar que en el Centro y en el Favor Express
   **solo** cambiaron los dos aceptados, y que los rechazados siguen igual.
4. Probar «Aceptar todas» / «Rechazar todas» con otra tanda.
5. Proponer un cambio, **cerrar la ventana sin decidir** y volver a entrar: el
   puntito sigue ahí; la tarjeta lo abre.
6. Que el que propuso vea el resultado la próxima vez que entre, y que después
   de verlo el puntito baje.
7. Con un invitado: **no** debe ver el 🛒 ni la tarjeta de Propuestas, y desde un
   perfil base **su fila tampoco debe tener 🛒**.
8. Un favor ya pedido antes del cambio: debe conservar su precio, castigo y
   minutos.
9. Tocar **Proponer dos veces rápido**: debe salir **una sola** propuesta (el botón
   dice "Enviando…" y no acepta el segundo toque).

# Los cuadros de la app: `confirmar.js`

Movido de `General/GUIA.md`. Contiene el detalle de `confirmar()` y `aviso()`, los cuadros modales de la app.

---

### Los cuadros de la app: `confirmar.js` (oct-2026)

**Ya no hay ni una ventana del sistema en la app.** Antes, cada "¿estas seguro?"
era un `confirm()` del navegador y cada "no lo puedes hacer" era un `alert()`:
la cajita gris, con los botones del sistema, que era la **unica** pantalla que no
usaba el diseno de la app y se veia ajena al resto.

Ahora hay **una sola pieza** en `confirmar.js` (raiz), con el mismo molde de los
modales que ya usaba cada juego: fondo oscurecido, caja con borde turquesa,
titulo en Chakra Petch, circulito ⚠️ cuando hace falta, boton grande con el
degradado coral→turquesa y "Cancelar" debajo.

**Dos funciones, segun lo que se tenga que decir:**

```js
import { confirmar, aviso } from "../confirmar.js";   // o "./confirmar.js" en la raiz

// 1) PREGUNTA: hay algo que confirmar o cancelar. Devuelve una promesa.
if(!await confirmar({
  aviso:true,                                  // circulito ⚠️ (por omision false)
  titulo:"¿Eliminar a Mary?",                   // la pregunta, en grande
  texto:"No se puede deshacer.",               // la consecuencia, chica (opcional)
  ok:"Eliminar"                                // el boton de adelante
})) return;

// 2) AVISO: se dice UNA cosa y no hay nada que cancelar. Un solo boton,
//    "Entendido", y SIEMPRE con ⚠️. NO se espera: se llama y ya.
if(!esAnfitrion()){ aviso("Terminar la partida es cosa del anfitrión."); return; }
```

**Por que `aviso()` no se espera y `confirmar()` si:** con `alert()` el codigo
se paraba hasta que le dieras OK, y habia que respetarlo (los candados hacen
`aviso(...); return;`, asi que se cortan igual). Con la caja, `aviso()` pinta y
el codigo sigue: **los candados siguen funcionando porque el `return` viene
despues**. **Regla: si cambias un `alert()` por `aviso()`, el `return` (o el
`return null`) tiene que quedarse donde estaba.**

**Decisiones que hay que respetar si se vuelve a tocar:**

- **El texto entra siempre con `textContent`**, nunca con `innerHTML`: varios de
  estos textos traen nombres, correos o accesorios que **vienen de Firebase**.
- Va en **Z 95**: encima de los modales normales (60) y de los fuegos (70).
- **Nunca dos cajas encimadas**: si se pide otra confirmacion con una abierta,
  la anterior se cierra como "no".
- Los colores se piden con `--card` y **caen a `--tarjeta`** (y asi con los
  demas), porque cada pantalla les puso un nombre distinto: **Diablitos** usa la
  otra serie (`--fondo`, `--tarjeta`, `--texto`, `--apagado`). Sin ese fallback,
  la caja salia sin fondo ni texto en Diablitos.
- **Cambiar un `confirm()` por este obliga a que la funcion sea `async`.** Ya se
  hizo en dos que no lo eran: `volverAlOriginal()` en `Diablitos/` y el
  `onclick` de "vaciar chat" en `Acompanante/`.
- **El circulito ⚠️ va DENTRO de la caja, no afuera como hermano.** Afuera se
  ponian de lado: el circulito empujaba la caja a la derecha y el par se salia
  del borde en los angostos (lo reporto Fredy, oct-2026). Por eso la capa lleva
  `flex-direction:column`: si alguna vez se cuelga un elemento suelto, se apila
  y se centra, en vez de correrse a un lado. **Regla general: cuando una capa es
  `display:flex` y le cuelgas hijos "de adorno", revisa que ninguno sea hermano
  de la caja.**
- **La regla de la casa: no se vuelve a usar `confirm()` ni `alert()` del
  sistema.** Si toca, es `confirmar()` o `aviso()`.

**Los 59 lugares** (se cambiaron todos de golpe, en dos rondas):

| Pantalla | Que es |
|---|---|
| `Opciones/`, `Encuentros/` | Saltar turno |
| `Diablitos/` | Volver a los originales |
| Inicio ⚙️ Usuarios | ~~Salir de modo invitado~~ · ~~eliminar a alguien~~ |
| `Citas/`, `Citas/accesorios.html` | Eliminar cita · eliminar accesorio |
| `Acompanante/` | Eliminar la conversacion |
| `Retos/` | Rechazar · retirar · eliminar · dar un punto · cobrar · aplicar castigo |
| `Panel/catalogo.html`, `Panel/oficiales.html`, `Panel/permisos.html` | Eliminar del catalogo · quitar publicador |
| `Autorizar/` | Revocar · negar · eliminar solicitud |

| | Donde |
|---|---|
| **20 preguntas** (`confirmar()`) | las de la tabla de arriba |
| **39 avisos** (`aviso()`) | `Acompanante/` 1 · `Autorizar/` 8 · `Encuentros/` 11 · `Guiadas/` 4 · `Opciones/` 11 · `Retos/` 4 |

Los 39 avisos son de tres familias: **"eso no lo puedes hacer"** (los 10 de
*"…es cosa del anfitrión"*), **"te falta algo"** (no hay acciones, la lista esta
vacia, muy pocas opciones) y **fallos** (*"revisa conexión"*). Los tres van con
⚠️ y un solo botón.

**Un texto que se acorto (decision de Fredy, oct-2026):** el de **salir de modo
invitado** era largo y avisaba lo que mas se necesita saber:
*"¿Salir de invitado y volver a tu base? **Tambien te borro de sus usuarios.**"*
Quedo solo **"¿Salir de modo invitado?"**. El invitado ya **no ve ahi** que
tambien se le borra de la lista de quien lo invito. Si alguna vez molesta, se
devuelve con `texto:`.


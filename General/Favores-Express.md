# Favores Express (`favor.js`)

Movido de `General/GUIA.md`. Contiene el detalle del módulo de favores expresos: qué es, colecciones, precios del 🛒, reglas de decisión y el botón flotante.

---

**Qué es:** uno le pide un favor al otro **en el momento**, con un precio en puntos, y el otro decide. Se pide desde un **botón flotante 🛎️** que está en las pantallas de la pareja, no desde el menú. Vive en **`favor.js`** (módulo de la raíz, como `fuegos.js` y `confirmar.js`): en cada pantalla es un import y `try{ montarFavor(); }catch(e){}`.

**La diferencia con los retos de la IA, que es la razón de que exista:** el reto de la IA **no se puede rechazar**; el Favor Express **sí**. Ese "ella decide" es lo que lo hace un favor y no un menú.

| Pieza | Dónde |
|---|---|
| Las dos ventanas (pedir / responder), el pago y el castigo | `favor.js` |
| La campana y el bip | `pestana.js`, tipo `"favores"` |
| La pestaña **Favores** del Centro | `Retos/centro.html` |
| Los números del 🛒 | `index.html` (⚙️ → Usuarios) |

**Las colecciones:** `favoresExpress` (un documento por favor) e `invitosFavor/{id de quien manda}` (el aviso de campana, **por persona**: con uno solo los dos se pisan).

**Los cinco números del 🛒** — los tres últimos son **del que pide** y **se congelan al crear el favor**, así que cambiar el 🛒 después **no** cambia lo ya pactado:

| Campo | Qué es | Por omisión |
|---|---|---|
| `ptsActivar` | Puntos para activar un deseo | 500 |
| `precioCompra` | Precio para comprar un deseo | 100 |
| `precioFavor` | Precio de un Favor Express | 15 |
| `pctCastigo` | % que se cobra si aceptan y no cumplen | 50 |
| `minutosFavor` | Minutos para cumplirlo | 10 |

**Decisiones que no se rompen (de Fredy) — no "mejorarlas" sin preguntar:**

- **El precio sí se le muestra** al que responde, desde la notificación. Se discutió ocultarlo y se descartó: aceptar a ciegas y que no le paguen se siente como un engaño.
- **El reloj arranca al ACEPTAR**, no al pedir. Si arrancara al pedir se vencería por estar ocupada, que es justo lo que pasa.
- **El saldo nunca queda negativo** (tope cero). Si no le alcanza, **el botón igual aparece** y se le avisa. Es **al contrario** que el "Comprar" del Centro, y es a propósito (ver `Centro-Adquisiciones.md`).
- **La sanción descuenta hasta donde alcance** y si no da, queda en cero.
- **El contra-precio es UNA ida y una vuelta, no un ciclo:** ella contraoferta, él acepta, vuelve a ella y **ahí se decide**. Si alguien no acepta en cualquier paso, el favor muere y no pasa nada.
- **Quién pidió no toca el precio**; **quien cumple sí** (hacia arriba, o hasta 0 si lo regala). Así nadie puede bajar el precio y ganar algo.
- **Un solo favor VIVO a la vez.** Se revisa al abrir el formulario **y otra vez al mandar** (`hayFavorVivo()`), para que no se cuele uno mientras escribes. No es un capricho: el aviso de la campana es **un hueco por persona** (`invitosFavor/{id de quien manda}`), así que dos favores vivos **se pisarían el aviso** y uno de los dos se quedaría sin ver el suyo. Los ya cerrados no cuentan.

**Dos cosas quedaron SIN decidir** (venían del plan de desarrollo, que ya se borró; si algún día se deciden, se anotan aquí y se quitan de esta lista):

1. **Si el 🛒 debe avisar del precio cuando se acepta un favor**, como pasa al comprar en el Centro.
2. **Si se avisa cuando el 🛒 cambia con una negociación viva.** El precio del favor **ya quedó congelado** en su documento, así que **no la afecta**: lo único por decidir es si además se dice algo.

**El registro NO se borra** (y esto importa): los puntos se mueven con `increment()` y **no hay de dónde vinieron** (es el P3 de `Modelo-Datos.md`). Por eso **el documento de cada favor se queda siempre**. Lo que sí se puede es **esconder** los resueltos de la lista, y en el Centro hay un **"Borrar descartados"** que borra **solo los rechazados y cancelados** (esos no movieron puntos) y siempre pregunta antes.

> **El botón flotante es una EXCEPCIÓN a la regla de las esquinas, y es decisión, no descuido.** La regla dice que los botones viven en las esquinas y que jamás hay dos en el mismo lado; el 🛎️ va fijo abajo a la derecha, encima de cualquier pantalla, porque el favor se pide sin entrar a buscarlo. Va en **Z60**, debajo de las ventanas (`confirmar.js` 95, el aviso de fin 80, los fuegos 70) para no tapar el "Aceptar". **No lo muevas a una esquina "para cumplir la regla".** **No sale** si eres invitado, si todavía no hay identidad, ni en `Panel/`, `Tienda/`, `Privacidad/` ni `Terminos/`.

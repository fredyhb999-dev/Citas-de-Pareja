# Iconos dibujados (SVG) — Diablitos

Movido de `General/GUIA.md`. Contiene el detalle visual del icono de Diablitos.

---

### Iconos dibujados (SVG) en vez de emoji

`index.html` trae `const SVG_DIABLITOS = '...'`: el diablito malo con risita
maligna. Se inserta con `ic.innerHTML`, pero **solo** para ese juego y **solo**
con el dibujo que esta en el propio archivo.

**Por que asi:**
- Un emoji se ve distinto en cada telefono (el de Diablitos salia morado en
  unos y de otro color en otros). Dibujado, se ve igual en todos.
- El tamano va en el `width` del propio SVG. Ahora es `1.35em`, que es lo que lo deja
  del mismo tamano que los emojis de las otras tarjetas (2.4rem). Ojo: el dibujo solo
  ocupa el 75% del cuadrito, por eso el numero no es 1. Para cambiarlo se toca ese
  unico numero; para cambiar la forma, las coordenadas del dibujo.
- **No se mete nada de la base de datos con `innerHTML`.** La tarjeta de la sala
  (`Diablitos/index.html`) sigue usando `textContent`, a proposito: ese texto
  viene de Firestore.

**Como cambiarlo:** editar las rutas dentro de `SVG_DIABLITOS`. Para hacerlo
mas grande o mas pequeno, cambiar los numeros del `viewBox`, **no** el `width`.
Para cambiar el color, cambiar los `fill`.

**Como volver al emoji:** en `tarjetaPack()`, dejar la linea del `if` y en la
definicion del pack poner el emoji en `icono`.

# Fuegos artificiales (`fuegos.js`)

Movido de `General/GUIA.md`. Contiene el detalle del módulo de fuegos artificiales al final de la partida.

---

### Fuegos artificiales al final de la partida (`fuegos.js`, oct-2026)

`fuegos.js` esta en la **raiz** y es un modulo ES reutilizable. Venia de
`Default Project/fuegos-artificiales/index.html`, que se deja como esta: es la
copia de trabajo.

```js
import { encenderFuegos, apagarFuegos, fuegosEncendidos } from "../fuegos.js";
encenderFuegos();   // aparece y se dispara solo
apagarFuegos();     // se quita y se detiene (no gasta bateria)
```

Decisiones que hay que respetar si se vuelve a tocar:

- El lienzo se crea solo, se pega al `body` y va con **`pointer-events:none`**
  y `z-index:70`. **Nunca** puede tapa un boton de la pagina.
- Los toques se escuchan en el `document`, y **se ignoran los que caen sobre
  `button`, `a`, `input`, `label`**: por eso "Aceptar" sigue sirviendo y el resto
  de la pantalla lanza mas fuegos.
- `#modalFin` tiene `z-index:80` y **`background:transparent`**, para que los
  fuegos (70) se vean completos y solo la caja opaquita tape el centro.
- El sonido usa WebAudio y **solo arranca con el primer toque** (los
  navegadores no dejan sonar nada sin que el usuario toque algo). Se respeta
  `localStorage["fuegos_mute"]`.
- El **boton de silencio** (`#fuegosSonido`, esquina inferior derecha, `z-index:71`)
  se crea y se borra junto con los fuegos: sale al prenderlos y se oculta al
  apagarlos. Muestra el iconito de Bocina con ondas (con sonido) o tachado (sin
  sonido). **El primer toque en el boton solo PRENDE el sonido** (no lo apaga):
  asi de verdad se oye la celebracion; despues de ahi, cada toque alterna.
  Mientras el sonido no ha arrancado, el boton **late** como pista. Ojo: es un
  `<button>`, asi que el handler global de toques lo salta y no lanza fuegos.
- Todos los caminos de fin pasan por `abrirFin(texto)` en `Opciones/`, que
  enciende los fuegos y abre el aviso. Se llama desde `finPartida()` (se acabo
  sola) y desde el listener de la sesion (la termino el anfitrion). El boton
  "Aceptar" (`btnFinOk`) apaga los fuegos antes de salir.
- Si se quiere en otro juego: importar el modulo y llamar `encenderFuegos()`
  en su aviso de fin. **Recordar subir el `z-index` de su modal** para que el
  aviso quede por encima de los fuegos.

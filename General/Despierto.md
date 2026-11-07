# Despierto (`despierto.js`) — que el celular no se apague jugando

Módulo de raíz que evita que el celular apague la pantalla o se bloquee mientras
hay una partida en curso. Usa la función del navegador **Screen Wake Lock**
(`navigator.wakeLock`).

## Qué exporta

| Función | Qué hace |
|---|---|
| `mantenerDespierto()` | Enciende el permiso. Se puede llamar muchas veces: si ya está encendido, no hace nada. |
| `soltarDespierto()` | Apaga el permiso y deja que el celular vuelva a dormirse. |

## Dónde se enciende y dónde se suelta

Lo usan **todos los juegos**: Castigos, Encuentros, Guiadas, Opciones, Roles y
Diablitos. En los cinco primeros la decisión se toma en un solo lugar:
**`ver()`**, la función que cambia de vista.

- Entrar a la vista de juego (`vistaPartida` en Castigos, `vistaPlayer` en los
  demás) → **encender**.
- Cualquier otra vista (inicio, espera, bloqueo, fin) → **soltar**.

Además hay casos que no pasan por `ver()`:

| Caso | Qué se hace |
|---|---|
| Se termina la partida (`mostrarFin()`, `abrirFin()`, `finPartida()`) | Se suelta. |
| Se llega al último paso y la pantalla se queda en "fin" | Se suelta. |
| El anfitrión pausa y el invitado ve el aviso de pausa | Se suelta al aparecer el aviso y se vuelve a encender al reanudar. |
| Guiadas: la cita queda en pausa (sin aviso) | Se suelta en `pintarPaso()` y se vuelve a encender al reanudar. |
| Un celular entra directo a una sesión ya pausada | Se suelta después de mostrar el aviso. |

**Diablitos** es aparte: su juego es un script clásico (no puede importar
módulos). El módulo de invitaciones le deja el puente en `window.despiertoJuego`,
y el juego avisa con `pantallaDespierta(true)` al correr (`correr()`) y
`pantallaDespierta(false)` al detenerse (`parar()`: pausa, configuración, salida
o pestaña oculta).

## Reglas del navegador (por qué está escrito así)

- El sistema **suelta el permiso solo** cuando la pestaña deja de verse (cambio de
  app, pantalla bloqueada). Al volver, el módulo lo pide otra vez
  (`visibilitychange`).
- En **Safari** la petición solo se acepta después de un toque del usuario. Por eso
  se reintenta en cada toque (`pointerdown` / `touchstart`); si ya está encendido,
  no hace nada.
- Si el navegador **no tiene** la función (Firefox viejo, iOS anterior a 16.4), el
  módulo no hace nada y el juego sigue normal. No lanza error.
- Necesita **HTTPS** (GitHub Pages ya lo es).

## Nota para quien programe

El chequeo `herramientas/sintaxis/extract.py` incluye `despierto.js` en su lista de
archivos sueltos: si se crea otro módulo de raíz, hay que agregarlo ahí o
`revisar.py` no lo revisa nunca.

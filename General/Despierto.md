# Despierto (`despierto.js`) — que el celular no se apague jugando

Módulo de raíz que evita que el celular apague la pantalla o se bloquee mientras
hay una partida en curso. Usa la función del navegador **Screen Wake Lock**
(`navigator.wakeLock`).

## Qué exporta

| Función | Qué hace |
|---|---|
| `mantenerDespierto()` | Enciende el permiso. Se puede llamar muchas veces: si ya está encendido, no hace nada. |
| `soltarDespierto()` | Apaga el permiso y deja que el celular vuelva a dormirse. |

## Dónde se enciende y dónde se suelta (Castigos)

La decisión se toma en un solo lugar: **`ver()`**, la función que cambia de vista.

- Entrar a `vistaPartida` → **encender**.
- Cualquier otra vista (inicio, espera, bloqueo, fin) → **soltar**.

Además hay tres casos que no pasan por `ver()`:

| Caso | Qué se hace |
|---|---|
| Se termina la partida (`mostrarFin()`) | Se suelta. |
| El anfitrión pausa y el invitado ve el aviso de pausa | Se suelta al aparecer el aviso y se vuelve a encender al reanudar. |
| Un celular entra directo a una sesión ya pausada | Se suelta después de mostrar el aviso. |

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

## Pendiente

Hoy solo está conectado en **`Castigos/`**. Para llevarlo a los otros juegos
(Encuentros, Guiadas, Opciones, Roles, Diablitos) hay que importar el módulo y
llamar a `mantenerDespierto()` / `soltarDespierto()` en los mismos tres momentos:
empezar, pausar/reanudar y terminar.

El chequeo `herramientas/sintaxis/extract.py` incluye `despierto.js` en su lista de
archivos sueltos: si se crea otro módulo de raíz, hay que agregarlo ahí o
`revisar.py` no lo revisa nunca.

# `avisarTelegram()` — Módulo `telegram.js`

Movido de `General/GUIA.md`. Contiene el detalle del módulo central de avisos por Telegram.

---

### `avisarTelegram()` vive en `telegram.js` (hecho oct-2026)

**Antes:** la función estaba **copiada en 5 archivos** y **ya se había
deformado**: eran **4 versiones distintas**, y una estaba **rota**.

| Archivo | ¿Revisaba que Telegram hubiera aceptado? |
|---|---|
| `Retos/centro.html` | **NO — se tragaba el error** |
| `Chat/`, `Acompanante/`, `Citas/`, `Retos/` | Sí |

**Por qué la del Centro estaba rota y eso importaba:** un token malo responde
**HTTP 200 con `ok:false`**. El `fetch` **no falla nunca**, así que sin revisar la
respuesta la función creía que el aviso salió y **se perdía en silencio**. Las
otras cuatro sí revisaban, y dejaban la pista en el celular.

**Ahora:** `telegram.js`, en la raíz, exporta `avisarTelegram(texto, url)` y saca
el token sola con `resolverTelegram()` de `config.js`. Los 5 archivos la
importan. **Las 24 llamadas no se tocaron.**

| Regla | |
|---|---|
| **La llave de la pista** | El error se guarda con **`pareja_tg_error`** y el ⚙️ de Telegram del menú la lee. **No cambiar esa llave.** (`telegram.js` la exporta como `CLAVE_TG_ERROR`, y `index.html` tiene la suya propia: mismo texto) |
| **El token se lee en cada llamada**, no al cargar el módulo | Para que un cambio hecho en el ⚙️ sirva de inmediato. Es el mismo criterio que `miProyecto()` en `acceso.js` |
| **Nunca lanza** | Un fallo de Telegram no debe tumbar la pantalla que lo llamó |
| **Registrado en `extract.py`** | Si no, el chequeo de sintaxis no lo revisa |

**Lo que NO cambió:** lo que ve el usuario. Solo se dejó de tener el mismo texto
cinco veces.

**PROBADO EN VIVO (Fredy, oct-2026):** los Telegram **siguen llegando** desde los
5 sitios — un reto nuevo, una cita nueva, una compra en el Centro, el botón
"Invitar" del Chat y un reto de la IA.


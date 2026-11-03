# Recordatorio de la mañana (Telegram)

**Qué es:** el mensaje de "☀️ Buenos días" que resume las citas del día y los
retos. **No lo manda la app**: lo manda **GitHub Actions** todos los días.

**Dónde vive:** `.github/workflows/recordatorio.yml` (cuándo corre) y
`.github/scripts/recordatorio.py` (qué hace). Sin dependencias: solo la
biblioteca estándar de Python.

| Pieza | Valor |
|---|---|
| Hora | `cron: "37 15 * * *"` = 15:37 UTC = **09:37 hora centro** (UTC-6) |
| Bot de Telegram | `TELEGRAM_BOT_TOKEN` (Secrets del repo) |
| Chat que recibe | `TELEGRAM_CHAT_ID` (Secrets del repo) |
| Prueba sin enviar | `MODO_PRUEBA=1`: imprime el mensaje en los registros y no manda nada |

**Corre en GitHub, no en el celular.** Que un teléfono tenga o no Telegram
instalado no influye en nada: lo que decide quién recibe el mensaje es **a qué
chat apunta el bot**, no qué aparato tiene la app.

## Los dos tipos de mensajes (no son el mismo)

| | Aviso instantáneo | Recordatorio de la mañana |
|---|---|---|
| Quién lo manda | La app, desde el teléfono (`telegram.js`) | GitHub, en sus servidores |
| Cuándo | Al crear, confirmar, rechazar o borrar una cita | Una vez al día |
| De dónde sale el bot | De la configuración guardada en la app | De los Secrets del repo |
| Se ve así | "✅ Mary confirmó la cita: …" | "☀️ Buenos días… 📅 Citas de hoy" |

## Qué lee

Las colecciones `citas` y `retos`, con la API REST de Firestore, usando el
`PROJECT` y el `API_KEY` escritos dentro del propio `.py`, y un encabezado
`Referer` con la URL de Pages. Ese `Referer` es obligatorio: la llave de
Firebase está restringida por sitio y sin él Google responde 403.

**Solo avisa, no escribe.** Los retos vencidos no se liquidan aquí: los
liquida la app al abrirse, para no duplicar el movimiento de puntos.

## Hueco conocido: el nombre de la actividad (oct-2026)

El script muestra `c.get("actividad")`: el **nombre guardado en la cita**, no
su `actividadId`. Por eso, en un caso concreto, el mensaje puede decir un
nombre viejo:

1. Se crea una cita de una actividad. Toda cita nueva lleva `actividadId`.
2. Después se **renombra** esa actividad. El renombrado corrige las citas
   viejas (las que no tienen id), pero **no toca las que ya tienen id**,
   porque la app las muestra bien buscando el nombre actual.
3. Desde ahí, la app muestra el **nombre nuevo** y el mensaje de Telegram el
   **viejo**, para la misma cita.

A las citas creadas antes de este cambio no les pasa: no tienen id, así que el
renombrado las corrige.

**No rompe nada:** afecta el texto del mensaje, no la app ni los datos. Queda
**pendiente de decidir** si se corrige.

## Estado de las copias

| Copia | Qué pasa |
|---|---|
| **Este repo (la plantilla)** | El workflow está **desactivado a mano** (`disabled_manually`). Tiene los datos de ejemplo (`TU_PROYECTO`, `TU_API_KEY`), así que fallaba todos los días y solo generaba correos de error. El archivo **se conserva**: la plantilla lo entrega al cliente. |
| **`App-Pareja` (uso personal)** | Es el que manda el mensaje real. Funciona todos los días. |

**Desactivar o reactivar:** pestaña **Actions** → "Recordatorio de la mañana"
→ menú **"..."** → *Disable workflow* / *Enable workflow*. No se borra nada.

**Para probarlo sin mandar nada:** *Run workflow* con `enviar: false`. El
mensaje aparece en los registros y no sale a Telegram.

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

Las colecciones `citas`, `retos` y `actividadesExtra`, con la API REST de
Firestore, usando el `PROJECT` y el `API_KEY` escritos dentro del propio `.py`,
y un encabezado `Referer` con la URL de Pages. Ese `Referer` es obligatorio: la
llave de Firebase está restringida por sitio y sin él Google responde 403.

**Solo avisa, no escribe.** Los retos vencidos no se liquidan aquí: los
liquida la app al abrirse, para no duplicar el movimiento de puntos.

## Nombre de la actividad

El mensaje muestra el **nombre actual** de la actividad de cada cita: la busca
por su `actividadId` en `actividadesExtra`. Si no la encuentra (una cita vieja
sin id, o una actividad ya borrada), usa el nombre que quedó guardado en la
cita, así que una cita nunca sale en blanco.

Los retos no necesitan esto: su campo `actividad` es **texto libre**, no una
referencia a una actividad.

## Estado en este repo

El workflow está **desactivado a mano** (`disabled_manually`): tiene los datos
de ejemplo (`TU_PROYECTO`, `TU_API_KEY`), así que fallaba todos los días y solo
generaba correos de error. El archivo **se conserva**: la plantilla lo entrega
al cliente, y quien lo configure lo enciende.

**Desactivar o reactivar:** pestaña **Actions** → "Recordatorio de la mañana"
→ menú **"..."** → *Disable workflow* / *Enable workflow*. No se borra nada.

**Para probarlo sin mandar nada:** *Run workflow* con `enviar: false`. El
mensaje aparece en los registros y no sale a Telegram.

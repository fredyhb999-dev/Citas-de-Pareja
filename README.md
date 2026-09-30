# Citas de Pareja

Aplicación web para organizar citas y retos de pareja.

## Requisitos

- Una cuenta de **GitHub** (gratis): [github.com](https://github.com)
- Una cuenta de **Google** (gratis): [google.com/accounts](https://accounts.google.com)

---

## Paso 1: Crear tu repositorio propio

1. Abre esta página en GitHub.
2. Pulsa el botón verde **«Use this template»** (arriba a la derecha).
3. Ponle el nombre que quieras (ej. `mis-citas`).
4. Elige **«Create a new repository»**.
5. Selecciona **«Public»** para que GitHub Pages funcione.
6. Pulsa **«Create repository»**.

> Ya tienes tu propio repositorio, dueña al 100%.
> Puedes editar sus archivos sin pedirle nada a nadie.

---

## Paso 2: Crear tu propio Firebase

1. Entra a [Firebase Console](https://console.firebase.google.com) con tu cuenta de Google.
2. Pulsa **«Agregar proyecto»**.
3. Ponle un nombre (ej. `mis-citas`) → **Continuar** → desactiva Google Analytics si quieres → **Crear proyecto**.
4. Cuando esté listo, toca el icono **`</>`** (Web) para registrar la app.
5. Dale un nombre (ej. `pareja`) → **Registrar app**.
6. Verás un bloque de código con **`firebaseConfig`**. Déjalo abierto, lo necesitas en el paso siguiente.

### Activar Firestore Database

1. En el menú lateral de Firebase → **Firestore Database** → **Crear base de datos**.
2. Elige **Modo de producción** → selecciona la región más cercana → **Habilitar**.
3. Ve a la pestaña **Reglas** y reemplaza el contenido con esto (para que la app pueda leer y escribir):

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true;
    }
  }
}
```

4. Pulsa **«Publicar»**.

---

## Paso 3: Conectar tu Firebase con la app

1. En tu repositorio, abre el archivo **`firebase-config.js`** (está en la raíz).
2. Verás algo como esto:

```js
const firebaseConfig = {
  apiKey: "TU_API_KEY",
  authDomain: "TU_PROYECTO.firebaseapp.com",
  projectId: "TU_PROYECTO",
  storageBucket: "TU_PROYECTO.firebasestorage.app",
  messagingSenderId: "TU_ID",
  appId: "1:TU_ID:web:TU_APP"
};
```

3. **Reemplaza** cada valor por los que Firebase te mostró en el Paso 2.
4. Guarda el archivo.

---

## Paso 4: Activar GitHub Pages

1. En tu repositorio, ve a **Settings** (arriba) → **Pages** (menú lateral).
2. En **Source**, selecciona **«Deploy from a branch»**.
3. Elige la rama **`main`** y la carpeta **`/(root)`** → **Save**.
4. En unos segundos tu app estará disponible en una URL tipo:

```
https://TU-USUARIO.github.io/TU-REPO/
```

> Guárdala como favorita en tu celular.

---

## Paso 5 (opcional): Avisos de Telegram

Cada cosa que pase en la app puede llegar a tu grupo de Telegram con un botón "Abrir 👀".

1. En Telegram, habla con **BotFather** → `/newbot` → ponle nombre y usuario → te da un **token**.
2. Crea un grupo con tu pareja e invita al bot. Para saber el **chat ID** del grupo, habla con **@userinfobot** o abre `https://api.telegram.org/botTU_TOKEN/getUpdates` después de escribir algo en el grupo.
3. Abre tu app y sigue el **asistente**: pega el token y el chat ID cuando te los pida (puedes omitirlo y ponerlo después borrando la configuración del navegador). Sin estos datos la app funciona igual, solo no manda avisos. La URL de los botones se arma sola.

---

## Paso 6 (opcional): Recordatorio de la mañana

Un resumen diario de citas y retos, gratis, con GitHub Actions (puede llegar con minutos de retraso: es normal).

1. En tu repositorio ve a **Settings → Secrets → Actions** y crea:
   - `TELEGRAM_BOT_TOKEN` → el token del Paso 5
   - `TELEGRAM_CHAT_ID` → el chat ID del Paso 5
2. Abre **`.github/scripts/recordatorio.py`** y reemplaza `TU_PROYECTO`, `TU_API_KEY` (la de tu `firebase-config.js`) y `PON_AQUI_URL_DE_TU_APP/` (tu URL de Pages con `/` al final; es la identificación ante Google).
3. En la pestaña **Actions** verás "Recordatorio de la mañana": se ejecuta solo cada mañana (~09:37 hora centro) o manualmente con **Run workflow** (`enviar=false` = solo prueba en logs).
4. Recomendado: en Google Cloud → tu proyecto → APIs y servicios → Credenciales → tu llave → restricción de sitios web con `TU-USUARIO.github.io/*` (así nadie más puede usar tu llave).

---

## Paso 7 (opcional): Personalizar actividades y accesorios

Los archivos JSON en la carpeta **`Citas/`** definen qué aparece en la app:

| Archivo | Qué contiene |
|---|---|
| `usuarios.json` | Respaldo local (los usuarios se definen en el asistente y viven en Firebase `config/ajustes`) |
| `actividades.json` | Lista de actividades para elegir |
| `accesorios.json` | Lista de accesorios/dispositivos |

Para cada actividad, puedes crear un archivo JSON con sus accesorios preseleccionados. Ejemplo: si en `actividades.json` tienes `"Cena Romántica"`, crea el archivo **`Citas/Cena Romántica.json`** con:

```json
[
  "Vela Aromática",
  "Pétalos de Rosa",
  "Champaña"
]
```

> Esas serán las opciones preseleccionadas cuando elijan esa actividad.

---

## Vincular a tu pareja y chatear

- **Vincular:** en el inicio, tu pareja elige "Tengo QR de mi pareja" y escanea tu código (inicio → "📱 vincular pareja" o Config → Vincular). Muéstralo en persona: quien lo tenga entra a tu base.
- **Chat:** tarjeta 💬 en el inicio. Mensajes en vivo solo con la app abierta + "en línea" cuando el otro también la tiene abierta. Con la app cerrada no suena nada: para eso sigue Telegram (Paso 5).

---

## Accesos por taquilla (Citas Guiadas y juegos)

Algunas secciones piden permiso del desarrollador:

- **Usuario:** entra con Google (login oficial, solo verifica tu correo) → Pedir acceso → al aprobarse entras sola, sin pegar nada.
- **Desarrollador:** crea el proyecto `taquilla-juegos` (Firestore + reglas solo `solicitudes` y lectura de `packs`), guarda tu llave privada en `Autorizar/` (una vez, no sale de tu aparato) y aprueba desde ahí, con días de vigencia o infinita.
- Los códigos van firmados (no falsificables) y cada juego verifica offline juego + vigencia.

---

## Usar la app en el celular

Si accedes a la URL de GitHub Pages desde tu celular:

- **iPhone (Safari):** toca el botón **Compartir** → **«Añadir a pantalla de inicio»**.
- **Android (Chrome):** toca los tres puntos → **«Añadir a pantalla de inicio»**.

La app se verá como si fuera una aplicación instalada.

---

## Sin conexión a internet

La app funciona con los JSON locales sin problemas.
La conexión a internet solo se necesita la primera vez que se conecta a Firebase.

---

## ¿Problemas?

1. Asegúrate de que en Firebase tengas habilitado **Firestore Database** (Paso 2).
2. Asegúrate de que las reglas de Firestore permitan **read/write**.
3. Verifica que los datos en `firebase-config.js` coincidan exactamente con los de tu proyecto Firebase.
4. En GitHub, ve a Settings → Pages y confirma que está activado en la rama `main`.

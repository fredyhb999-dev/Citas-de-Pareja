# `Autorizar/` — Aprobar y revocar licencias

Movido de `General/GUIA.md`. Contiene el detalle de la pantalla `Autorizar/`, el hallazgo del login de Google, la llave privada y la secuencia para cerrar reglas.

---

> Origen: `Modulo-Accesos.md` (04/10/2026), conservado literal.
> **Esta es la única parte que no existía en ningún otro documento.** Sin ella se perdía el hallazgo del login y el estado en que quedaron las reglas.
>
> **Estado (oct-2026):** el login de `Autorizar/` ya está escrito, pendiente de subir. Las reglas siguen abiertas **a propósito y por decisión de Fredy**: se revisaron y quedaron cerradas.

## El inicio de sesión de `Autorizar/` (oct-2026)

### El hallazgo

Al cerrar las reglas de `solicitudes` (para que solo el publicador pudiera modificar y borrar), **aprobar y revocar dejaron de funcionar**, sin ningún error visible.

La causa no era la lista de publicadores ni el correo del dueño. Era que **`Autorizar/index.html` nunca iniciaba sesión con Google**: no tenía `getAuth`, ni `signInWithPopup`, ni nada. Otras páginas del Panel sí lo tienen.

Entonces, con las reglas cerradas:

| Regla | Qué pasaba |
|---|---|
| `request.auth` | Siempre `null` (la página nunca se firmaba) |
| `esPublicador()` | Siempre `false` |
| `update` / `delete` | **Siempre rechazados** |
| `create` (pedir) | Funcionaba: no pide sesión |
| `read` | Funcionaba: está abierto |

Y como los botones Aprobar, Revocar y Negar hacían `await updateDoc(...)` **sin `catch`**, el rechazo no se mostraba. El código aparecía y "desaparecía" sin ninguna pista.

### Por qué las reglas viejas estaban abiertas

`solicitudes: if true` no era un descuido. **Era obligatorio**, precisamente porque `Autorizar/` no tenía forma de identificarse. Al cerrar las reglas se le pidió ser publicador a una pantalla que nunca inicia sesión.

> **Hoy ya no aplica:** `Autorizar/` **sí** inicia sesión. Esa fue la causa del problema y ya está resuelta (ver *El cambio hecho*, abajo).

### El cambio hecho

En `Autorizar/index.html`:

1. **Botón "Entrar con Google"** + `onAuthStateChanged`, copiando el patrón de `Panel/permisos.html`. Ahora `request.auth` sí se llena.
2. **`catch` en Aprobar, Revocar y Negar**, con `alert()` visible. Antes cualquier rechazo de reglas era invisible.

Se usó `alert()` y no el `#msg` de la página, porque ese mensaje vive dentro de la caja de la llave privada, y esa caja se oculta cuando la llave ya está guardada.

### La llave del autorizador (y por qué NO está en el repo)

El `Panel/` y el `Autorizar/` piden una **llave privada** en formato JWK (`{"kty":"EC","crv":"P-256","x":...,"y":...,"d":...}`). **No es una API key de Firebase**: es la mitad privada de un par **ECDSA P-256** que sirve para **firmar las licencias** de la tienda.

| Mitad | Dónde | Para qué |
|---|---|---|
| **Pública** | `taquilla.js` (`TAQUILLA_PUBLICA`) | **Verificar** los códigos. Viaja en el repo a propósito |
| **Privada** | **Solo en el aparato del desarrollador** | **Firmar**. Se pega en `Panel/` y `Autorizar/` |

Nunca se sube al repo: quien tenga la privada puede **fabricar licencias**. Se guarda en `localStorage` bajo la clave `taquilla_priv`, así que **queda solo en ese navegador y ese dispositivo**.

`Panel/` y `Autorizar/` usan **la misma clave de `localStorage` y el mismo origen**, así que **pegarla una vez abre los dos**.

**Rotación (oct-2026):** la pareja anterior se había perdido, así que se generó un par nuevo con el mismo WebCrypto que usa la app (`crypto.subtle`), y se cambió `TAQUILLA_PUBLICA` en `taquilla.js`. **Las licencias firmadas con la llave anterior dejan de validar** (quedan inválidas, no se pueden "arreglar").

Al rotar hay que: 1) cambiar `TAQUILLA_PUBLICA`, 2) pegar la nueva privada en `Panel/` y `Autorizar/`, 3) volver a firmar los códigos que sigan valiendo.

### Estado

> **TEXTO VIEJO (oct-2026), ya no es cierto.** Se conserva porque explica el orden en que se resolvió. Hoy: **las reglas están cerradas** (salvo `read`, a propósito) y **`Autorizar/` ya está subido y funcionando**.

- ~~Las reglas están **temporalmente regresadas** a `solicitudes: if true`~~ ~~(el agujero está abierto otra vez: cualquiera puede leer los correos y echar usuarios).~~ -> Cerradas el 6-oct-2026. Ver *Estado de las reglas*.
- ~~`Autorizar/` ya tiene el inicio de sesión, pero **no se ha subido todavía**.~~ -> **Subido.** Fredy probó pedir, aprobar y revocar: todo normal.

### La secuencia para cerrar las reglas

1. Subir `Autorizar/index.html` con GitHub Desktop.
2. Abrir `Autorizar/` y tocar **"Entrar con Google"**. Debe aparecer `✅ <correo>`.
3. **Solo si el paso 2 funcionó**, volver a poner las reglas cerradas en la consola.
4. Probar aprobar y revocar. Si algo falla, ahora sale un aviso.

### Lección

Al cerrar reglas de Firebase en una app sin login, hay que revisar **cada pantalla que escribe**, no solo la que se está tocando. `Autorizar/` era la única del Panel que escribía sin autenticarse, y por eso rompió.

> Regla práctica: **todo botón que escriba en Firestore necesita `catch` con aviso visible.** El de Eliminar ya lo tenía; los otros tres no, y eso costó un buen rato de diagnóstico.

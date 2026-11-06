# Pantalla de Usuarios — Cambiar usuario y editar nombres/puntos

Movido de `General/GUIA.md`. Contiene el detalle de la pantalla de Usuarios: flujo de cambiar usuario, editar nombres, administrador y puntos.

---

### El flujo de "Cambiar usuario" (y lo que se aprendió)

**Cómo quedó:**

1. En Usuarios, arriba a la izquierda, "Cambiar usuario".
2. Abre la lista de usuarios en la misma pantalla, con **"‹ Volver"** arriba a
   la derecha. Ahí se puede salir sin cambiar nada.
3. Al escoger, **deshace el paso "Cambiar usuario"** y recarga (para que la app
   entera tome la identidad nueva); deja una marca en `sessionStorage`
   (`ir_a_usuarios`) y **aterriza de vuelta en Usuarios**, no en el menú. Así el
   «‹ Volver» de esa lista (y el atrás del celular) ya no repiten una pantalla
   antes de salir (nov-2026).

**Tocar un usuario directo en la lista (nov-2026).** Ese camino también recarga,
y antes caía al **menú**: dejaba el paso del engrane en el historial y, al
entrar a un submenú y volver, reaparecía Usuarios con los botones de las
esquinas encimados. Ahora hace lo mismo que «Cambiar usuario»: marca
`ir_a_usuarios` y al recargar vuelve a **Usuarios**. En `entrar()` el paso se
corrige a `{gear:"usu"}` para que el «‹ Volver» y el atrás del celular hagan lo
mismo.

**Los botones encimados son la señal, no el bug (decisión de Fredy).** No se
agrega ningún parche que los oculte: si vuelven a aparecer, es que hay otro paso
cruzado en el historial y hay que buscarlo.

**Lo que estaba mal y por qué importa (hallazgo de Fredy, oct-2026):**

La primera versión **borraba la identidad y recargaba**. De ahí salían dos
molestias:

- **No se podía salir sin cambiar.** Tenías que escoger a alguien.
- **Caías donde se te antojaba.** Al recargar, la app decide según quién eras:
  si el último usuario era invitado, te mandaba a su base; si no, al menú. Por
  eso a veces aparecía Diablitos, a veces el menú de juegos, a veces la
  pantalla inicial.

**La lección, escrita como regla:** una acción que cambia la identidad **no
borra nada antes de tiempo ni recarga a ciegas**. Primero muestra, deja
cancelar, y solo al confirmar recarga — y dice a dónde va.

Las piezas en el código: `modoCambiar`, `CLAVE_IR_USU`, `abrirPanelUsuarios()`.

### Editar nombres, administrador y puntos (botón al final de Usuarios, oct-2026)

Al final de la pantalla de **Usuarios** (⚙️ → Usuarios) hay un botón **"✏️ Editar
nombres y administrador"** (`#invEditar`) que abre una **ventana emergente**
(`#invOverlayUsu`, mismo molde que la de Puntos). Dentro salen **todos los
usuarios**, y en cada renglón un **campo de puntos**:

**Candado (decidido por Fredy, oct-2026):** el botón **nace oculto** y solo se
muestra **si el usuario actual NO es invitado** (o sea, uno de los dos base); a
los invitados también se les **oculta "Cambiar usuario"** (`#invCambiarUsu`), que
si no servía para ponerse como la pareja y entrar igual. La visibilidad la
resuelve `pintarInvUsuarios()` con `soyInvitado()`, y `abrirEdUsuarios()` **vuelve
a comprobar** que no sea invitado. Además, al tocar el botón **pide una clave** en
una ventana de la app (`#invOverlayPin`, nada de `prompt()` del sistema).

- La clave está **fija en el código**: en `index.html` se guarda su **hash
  SHA-256** (`PIN_EDITAR_HASH`), no el PIN. **Para cambiarla** hay que recalcular
  `sha256("<nuevo pin>")` en hexadecimal y reemplazar la constante. El PIN de
  pruebas es `9966**`.
- Esto es **para las pruebas de la pareja**, no es seguridad real: el repo es
  público y la base está abierta, así que quien lea el código o la base puede
  saltárselo. La protección de verdad es el login (rediseño de arquitectura).

**El atrás del celular cierra esas ventanas (nov-2026).** La Tienda (🛒),
Editar, la clave y el Historial no son pasos del historial: viven *encima* de
Usuarios. El `popstate` de `index.html` los cierra primero y se queda en Usuarios
(`history.go(1)`); si no, el engrane navegaba por debajo y la ventana quedaba con
`display:flex`, así que al reabrir el engrane reaparecía sola. Además,
`mostrarGear()`, `cerrarGear()` y `abrirPanelUsuarios()` llaman a
`cerrarOverlaysInv()`, y `abrirEdUsuarios()` usa un token para no reabrirse si
los datos llegan después de cerrarla.

**Convención para ventanas nuevas:** cualquier ventana que se abra encima de
`#pantallaInvitado` debe llevar un `id` que empiece con `invOverlay`. Así el
atrás la detecta y la cierra sola (`overlaysInv()`), sin tener que agregarla a
una lista.

- **Los dos perfiles base** (admin y pareja, o sea `!invitado`): campo de nombre
  **editable** y un **radio "Admin"**. **Solo hay un administrador.**
- **Los invitados**: solo salen para editarles los puntos; su nombre se muestra
  **de solo lectura**.

**Los nombres y el admin** se guardan en `config/ajustes.usuarios` —lo mismo que
ya usaban el asistente y "agregar invitado"— con `setDoc(..., {merge:true})` y
`guardarUsuariosLocal()`. Si alguien se renombra a sí mismo (o le cambia el
admin), su copia local (`CLAVE_LOCAL`, `appPareja_quienSoy`) también se actualiza.

**Al renombrar no se reescribe nada más.** Las citas, retos y partidas guardan el
nombre de ese día solo como respaldo; al mostrarlos se resuelve el nombre actual
por el id (`nombrePorId()`, ver `GUIA.md`). Por eso una cita vieja pasa a decir
el nombre nuevo sin migrar ningún documento. El chat y la presencia son la
excepción: conservan el nombre del momento.

**Los puntos** se escriben **directos** (el número exacto) en el campo **`balance`
de `puntosUsuarios/{id}`**, que es donde viven (no en `config/ajustes`, y **no**
son los precios del 🛒). Se leen de una sola vez con `getDocs` y, si el documento
no existe, el saldo se toma como **0** (igual que `Retos` y `favor.js`). Como esas
pantallas escuchan la colección, el cambio se refleja solo. Tiene que ser un
número **de 0 o más**.

> **Desde nov-2026, el ajuste de puntos registra la diferencia** (cuánto se movió)
> en el historial `puntos/{id}/movimientos`, no el número absoluto. Ver
> `General/Puntos.md`.

**El historial de movimientos (botón 📜):** cada renglón de usuario trae un botón
**📜** que abre su historial de puntos (de solo lectura, los últimos 50). **Cada
quien ve el suyo; el administrador ve el de los dos perfiles base.** Ver
`General/Puntos.md`.

**Aviso que hay que recordar:** en toda la app **el admin es el lado A y la pareja
el lado B** (`nombreLado()`, `armando()`), y hay contenido guardado **por lado**
(acciones de `nivelesActividad`, `opcionesJuego/actual {A,B}`, `personajesJuego`
`U1/U2`…). Por eso **cambiar de admin intercambia esos lados**: el contenido que
estaba de un lado se ve del otro. Se decidió permitirlo así (decisión de Fredy,
oct-2026). Cualquier usuario puede abrir el botón, porque la app no tiene login.

### Botones de volver, de esquina y "cambiar usuario"

| Botón | Dónde | Nombre |
|---|---|---|
| Volver de un submenú | Arriba a la **derecha**, los tres | `volverSub` |
| Engrane (invitados) | Menú principal, arriba a la **izquierda** | `gearBtn` |
| Carrito (adquisiciones) | Menú principal, arriba a la derecha | `menuBtn` |
| Volver de un juego | Cada juego, dentro de la pantalla | varía |
| Cambiar usuario | Pantalla **Usuarios**, arriba a la izquierda | `invCambiarUsu` |
| Cambiar usuario | **Solo** en Usuarios, no en ninguna otra |

Retos también quedó igual que Citas (oct-2026): **Volver** a Retos especiales (`#extras`) y **sin** "Cambiar usuario".

**Cuidado con los `#`:** si un juego apunta a un `#` que no está en el `if(location.hash)` de `index.html`, **no da error**: simplemente te manda al menú principal. Pasó con `#extras`.

`invCambiarUsu` **no borra nada ni recarga**: abre la lista de usuarios en la misma
pantalla, con un **"< Volver"** para salirse sin cambiar. Al escoger, ahí sí
recarga (marca `ir_a_usuarios` en `sessionStorage`) para que la app entera tome
la identidad nueva, y **aterriza de vuelta en Usuarios**. Antes estaba en
`Citas/` y en `Retos/` (`btnCambiarUsuario`), y ya no existe en ninguno de los dos.

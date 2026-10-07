# AGENTS.md - Citas de Pareja

## Antes de hacer cualquier cosa

**Lee `General/GUIA.md` primero.** Es el documento maestro del proyecto:
contiene el modo invitado, la sala de espera, la decision de por que las
invitaciones se atan a la partida, `acceso.js`/licencias, `Autorizar/` y las
reglas de Firebase.

Sin leerlo se repiten errores ya resueltos y se rehacen cambios a medias.
Ese fallo ya ocurrio una vez: un trabajo completo se descarto porque nadie
tenia el contexto a la mano.

## Como trabajar en este repo

- Todo el codigo es **HTML estatico con JavaScript adentro**. No hay build, no
  hay npm, no hay framework. Se edita el archivo y ya.
- Los modulos compartidos viven **en la raiz** (`acceso.js`, `invitado.js`,
  `config.js`, `firebase-config.js`, `taquilla.js`) y se importan por ruta
  relativa al **modulo**, no al archivo que lo importa.
- **Reglas de Firestore:** no estan en el repo. Viven en la consola de Firebase.
  Cualquier tarea sobre permisos es manual y hay que decirlo.
- **No hay `git` disponible en el entorno de trabajo.** Para revisar cambios se
  leen los archivos directamente; Fredy es quien sube con GitHub Desktop.
- **Las pruebas estan en `herramientas/pruebas/` (DENTRO del repo).** Abren un
  Chrome real contra una base de datos simulada, asi que **no tocan Firebase ni
  los datos reales**. El orden SIEMPRE es: construir, inyectar, correr.
  Inyectar dos veces sin reconstruir deja el arnes corrupto.

  ```powershell
  cd herramientas\pruebas
  # Encuentros (13 casos)
  python build_harness.py ; python inject_driver.py ; python final.py
  # Inicio (6 escenarios)
  python build_raiz.py ; python inject_raiz.py ; python run_raiz.py menu
  # Sala (7 escenarios)
  python build_sala.py ; python inject_sala.py ; python run_sala.py invitado
  # Solo sintaxis, sin navegador
  python extract.py ; python jscheck.py <archivo.js>
  ```

  Detalle completo en `herramientas/pruebas/LEEME.md`. Ojo: `jscheck.py` marca
  como error las llaves que esten DENTRO de una expresion regular; el navegador
  real es la autoridad.

## Reglas de la casa

1. Si la decision es de producto (que se ve, quien puede salir, que pasa al
   pausar), **preguntar antes de aplicar**.
2. Explicar en espanol claro y sin codigo. El usuario no programa.
3. No inventar reglas nuevas de Firestore: se reutiliza lo que ya funciona.
4. No agregar reglas de seguridad que rompan el modo invitado (nada de "solo el
   anfitrion escribe", porque el invitado escribe su identidad).
5. Cambios minimos, y **verificar antes de decir "listo"**.
6. Documentar en `General/GUIA.md` lo que se decida o se descubra. Ese archivo
   es la unica memoria del proyecto.

## Estándares de tamaño (no inventar otros)

Estos numeros son **los de la pantalla inicial** (`index.html`) y son el
referente. Cuando se agregue un boton, una tarjeta o un titulo en CUALQUIER
pantalla, se copian de aqui. No se inventan medidas nuevas, y no se pregunta
por ellas: ya estan decididas.

| Que | Medida |
|---|---|
| Ancho maximo del contenido | `max-width:380px` |
| Boton principal | `width:100%; padding:16px; border-radius:16px; margin-bottom:12px; font-size:1.05rem` |
| Boton secundario | `padding:12px` |
| Boton de icono (el circulito de arriba) | `font-size:1.6rem; padding:8px 10px; border-radius:12px` |
| Tarjeta de menu | `padding:24px 20px; border-radius:20px; margin-bottom:16px; gap:16px` |
| Icono de tarjeta | `2.4rem` en el menu, `2rem` en otras pantallas |
| Titulo de tarjeta | `1.25rem` en el menu, `1.1rem` en otras |
| Subtitulo de tarjeta | `.85rem` |
| Chevron de la tarjeta | `1.4rem` |
| Titulo de seccion | `.8rem`, mayusculas, con espacios entre letras |
| Radio de esquina, general | `12px` (esquinas chicas), `16px` (botones y tarjetas) |
| Al tocarse un boton | `transform: scale(.97)` |

**Nota honesta:** hoy hay botones viejos con `padding` de 12, 13 y 16px, y
radios de 12, 14 y 16px. **No es un bug, pero lo nuevo va con la tabla de
arriba.** Unificar los viejos se hace aparte, pantalla por pantalla, porque
tocarlos todos de golpe es Riesgoso sin verlos.

## Estándar de navegación (botones de volver y esquinas)

**1. El botón "Volver" de un juego se llama `‹ Volver`, nunca "Inicio",** y
regresa **al submenú del que salió el juego**, no a la pantalla inicial:

| Juego | Va a | Como |
|---|---|---|
| Diablitos | Juegos | `../index.html#juegos` |
| Un juego de Experiencias | Experiencias | `../index.html#experiencias` |

`index.html` lee el `#` al arrancar y abre esa subpantalla directo
(`abrirJuegos()` / `abrirExp()`). Para agregar otro submenú: se agrega su
`abrirX()` / `cerrarX()` junto a las demás y se añade su línea en ese `if`.

**2. Los botones de la esquina (el ⚙️ de invitados y el 🛒 de adquisiciones)
son del MENÚ PRINCIPAL.** En un submenú no se muestran: ahí solo vive el
`‹ Volver`. El ⚙️ va arriba a la **izquierda** (a la derecha se encimaba con el
🛒 en el celular).

**3. El invitado NO tiene ninguna salida.** En `Encuentros/` el enlace "‹
Volver" se le oculta siempre (`pintarSalidas()`), porque la regla de Fase 1 dice
que el invitado no se va por su cuenta. La pareja y el anfitrión sí lo ven,
salvo durante la partida.

**4. El guardado de cada pantalla es `position:fixed` o `absolute` con
`top:max(18px, env(safe-area-inset-top))`.** Nunca sin esa protección: en
celulares con notch los botones se esconden bajo la barra.

## Riesgo conocido (importante, NO urgente)

- Las reglas de `solicitudes` estan **abiertas** (`solicitudes: if true`). Fredy lo
  sabe y lo tiene aceptado: se resolvera con el **rediseño de arquitectura**.
  **No lo trates como una urgencia ni intentes cerrarlas por tu cuenta.**
- `Autorizar/index.html` con el login de Google ya esta escrito, **falta subirlo**.

**Unica regla dura:** nunca cerrar esas reglas antes de que `Autorizar/` tenga el
login subido. Sin login, cerrar las reglas rompe Aprobar/Revocar **en silencio**
(el boton parece funcionar y no cambia nada).

Ver `General/GUIA.md`, Parte 4.

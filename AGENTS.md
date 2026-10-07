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
- **No hay `git` disponible en el entorno de trabajo**, ni navegador real. Para
  verificar se usan los scripts de `C:\Users\Fred\AppData\Local\Temp\opencode\`
  (`jscheck.py`, `undef.py`, `expcheck.py`, `argcheck.py`, `dupcheck.py` y los
  arnes de navegador con mocks de Firebase).

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

## Riesgo conocido (importante, NO urgente)

- Las reglas de `solicitudes` estan **abiertas** (`solicitudes: if true`). Fredy lo
  sabe y lo tiene aceptado: se resolvera con el **rediseño de arquitectura**.
  **No lo trates como una urgencia ni intentes cerrarlas por tu cuenta.**
- `Autorizar/index.html` con el login de Google ya esta escrito, **falta subirlo**.

**Unica regla dura:** nunca cerrar esas reglas antes de que `Autorizar/` tenga el
login subido. Sin login, cerrar las reglas rompe Aprobar/Revocar **en silencio**
(el boton parece funcionar y no cambia nada).

Ver `General/GUIA.md`, Parte 4.

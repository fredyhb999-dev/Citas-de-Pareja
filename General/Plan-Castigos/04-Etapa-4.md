# Etapa 4 — Sesión compartida e invitados

> **Pega este archivo completo como instrucción.** Implementa **solo esta etapa**.
> Antes: lee `AGENTS.md`, `General/GUIA.md` (modo invitado, sala,
> `invitado.js`, invitaciones) y `General/Plan-Castigos.md`
> (secciones 2.2, 2.3, 3.2, 5.4–5.6, 6.3, 6.6) y este archivo.
> **Copia el patrón de `Encuentros/index.html`**, no lo inventes.

## Objetivo

Que la partida funcione **en dos o más celulares** (Pareja e Invitados), con
sesión en `sesionCastigos/actual`, y con el flujo de invitados (QR, sala,
agregar, invitado a media partida). Incluye “Cada quien el suyo”.

## Tareas exactas

### 1. Sesión compartida
- Documento **`sesionCastigos/actual`** con la forma de `Plan-Castigos.md` 3.2.
- Crear la sesión al iniciar (el anfitrión = quien inicia).
- Todos los celulares escuchan con `onSnapshot`.
- Avanzar el turno con **`runTransaction`**, y solo si quien avanza es el
  **jugador del turno** (o el anfitrión en “Saltar turno”).
- `pausada`, `terminada`, `revivir`, `turnos`, `turno` viven en la sesión.
- **Sin reglas nuevas de Firestore**: la base de la pareja está abierta a
  propósito. No inventes reglas.

### 2. “Un celular” y “Cada quien”
- **Un celular:** una sola pantalla (la del que castiga); el teléfono se pasa.
- **Cada quien:** cada celular muestra según su identidad:
  - **El jugador del turno:** pantalla completa del que castiga (imposición →
    Aceptar → castigo → medida → Listo).
  - **El lado contrario:** **“Te toca recibir”** + la imposición como contexto
    (sin botón) + **solo la acción** (sin medida ni cronómetro).
  - **Los demás:** **“Turno de [nombre]”** (+ imposición como contexto).
  - En turnos **saltados** no se muestra “te toca recibir”: se avanza.
- Los controles de anfitrión (**Revivir**, **Saltar**, **Pausar**, **Terminar**,
  **QR**, **Agregar invitado**) solo se ven y funcionan en el celular del
  **anfitrión** (`hostUid`).

### 3. Imposiciones en la sesión
- El **anfitrión**, al detectar un turno jugado (`saltado === false`) con
  `imposicion === null`, toma la siguiente de la bolsa del lado y la escribe en
  `turnos[turno].imposicion` (merge).
- Los turnos saltados no toman imposición.
- Bolsa por lado: barajada al iniciar; al vaciarse, se rebaraja. No repetir
  dentro de la ronda si se puede.
- Si el lado no tiene imposiciones, se deja `null` y se salta el paso.

### 4. Invitados (copiar el patrón de Encuentros)
- **QR:** `abrirQR()` con el mismo mecanismo que Encuentros (`qrcodejs`).
- **Registro:** nombre + **“de quién es invitado”** (`conQuien`). Su `lado` sale
  de `conQuien`.
- **Sala de espera:** al registrarse va a la sala (“Esperando Invitación…”); no
  tiene salida.
- **Agregar invitado:** el anfitrión lo agrega; ahí entra al juego.
- **Invitaciones:** usar el mismo mecanismo de `Encuentros/`/`invitado.js`
  (`publicarInvitacion` / `retirarInvitacion` / `vigilarInvitaciones`),
  apuntando la sesión a `sesionCastigos/actual`.
- Las **licencias no viajan**: el invitado juega con el acceso del anfitrión.
- **Invitado a media partida:**
  - Se agrega a `cabezas` y al final de `orden`.
  - Se le copia la lista del **compañero de su mismo lado** desde el punto
    actual; juega **solo las rondas que faltan**.
  - Se agregan sus turnos a las rondas restantes; **no** se rearma nada de los
    demás.

### 5. Solo con invitados
- En Solo también se muestran **QR**, **Agregar invitado** y la sala.
- Si llega un invitado, se suma con su `conQuien` y, si quedan los dos lados,
  **Revivir** se muestra y se puede prender.

### 6. Sin internet
- Copia el comportamiento de Encuentros: si `navigator.onLine === false`,
  avisar **“Sin conexión. Se jugará en este celular.”** y caer a modo local
  (si el contenido ya está cargado).
- No expulsar a nadie por un corte de red durante la partida.

## No hagas todavía
- No implementes Multi, Placer extremo ni Sorpréndeme (Etapa 5).
- No toques otros juegos.
- No cambies las reglas de Firestore.

## Criterios de aceptación
1. Dos celulares ven la misma sesión y avanzan con `runTransaction`.
2. En “cada quien”, el que castiga ve los controles; el lado contrario ve
   “Te toca recibir” + imposición + acción; los demás ven “Turno de…”.
3. Solo el anfitrión ve Revivir, Saltar, Pausar, Terminar, QR y Agregar.
4. Revivir y Saltar se reflejan en todos los celulares.
5. Un invitado se registra por QR, espera, el anfitrión lo agrega y juega.
6. Invitado a media partida: copia la lista del compañero y juega lo que falta.
7. En Solo con invitados, QR/sala funcionan y Revivir aparece si hay dos lados.
8. `python revisar.py` en `herramientas/sintaxis` sale **en verde**.

## Al terminar, reporta
- Archivos tocados.
- Qué probaste con dos celulares y qué no.
- Resultado de `revisar.py`.
- Dudas.
- **No empieces la Etapa 5.**

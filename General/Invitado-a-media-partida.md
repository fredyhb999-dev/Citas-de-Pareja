# Agregar invitado a media partida (mecanismo reutilizable)

> Referencia de implementación: `Opciones/index.html` (**Elecciones Peligrosas**).
> Escrito el oct-2026. Sirve para meter este mismo comportamiento en otros
> juegos con invitados (Encuentros, o cualquier juego nuevo que use el sistema
> de invitaciones y sesión compartida).

## Qué resuelve

Hoy, cuando el anfitrión empieza una partida con invitados, se congela todo:
participantes, opciones de cada quien, orden de turnos e invitación. Quien no
estaba en ese momento no entra. Este mecanismo permite **agregar a un invitado
con la partida ya andando**, sin tener que empezarla de nuevo.

## La idea central (y por qué es simple)

**El que entra NO juega la ronda en curso: entra a partir de la siguiente.**

Con eso, todo se calcula solo:

- Su lista trae **tantas opciones como rondas le falten** (`R − ronda actual`),
  así termina junto con los demás.
- **No se agrega al orden de turnos actual.** Cuando la ronda da la vuelta, el
  orden se **revuelve con todos los que siguen vivos** y ahí entra. No hay que
  inventar un turno especial.

## Requisitos previos (lo que el juego ya debe tener)

1. **Invitaciones** por el módulo común (`../invitado.js`):
   `publicarInvitacion`, `retirarInvitacion`, `pausarInvitacion`.
2. **Sesión compartida** en un documento (por juego): p. ej.
   `sesionOpciones/actual`, con `cabezas`, el estado de cada quien y el turno.
3. **Lista de usuarios viva**: `escucharGrupo()` escuchando `config/ajustes`
   (para no perder a nadie con una lista vieja). En Opciones se agregó junto con
   este cambio.
4. Que el juego sepa **de qué lado es cada invitado**: se guarda en `conQuien`
   (quién lo invitó) al registrarse como invitado.

## Pasos para implementarlo en un juego

1. **Llevar la ronda actual** en el estado: un campo `ronda` (empieza en `1`).
2. **Marcar cuándo empieza una ronda nueva**: cuando el orden de turnos da la
   vuelta (se revuelve), subir `ronda` en 1. En Opciones, `siguienteTurno()`
   devuelve `nuevaRonda:true` en ese momento.
3. **Botón "Agregar invitado"** en la pantalla del anfitrión: visible solo para
   el administrador y **en juego** (siempre; la ventana avisa si no hay invitados
   registrados por agregar).
4. **Agregar al invitado** (en una transacción sobre el documento de la sesión,
   para no chocar con una jugada que esté pasando en ese instante):
   - meterlo en `cabezas` con su `lado` (según `conQuien`);
   - darle su lista: `R − ronda` opciones sacadas del lado que le toca (sin
     repetir si alcanza; si no alcanza, se permite repetir);
   - inicializar su `pares` (nada) y sus `eliminadas` (vacío);
   - **NO** meterlo al `orden` actual.
5. **Volver a publicar la invitación** con el participante nuevo, para que su
   sala de espera le muestre el botón "Entrar".
6. **La entrada del invitado ya funciona** igual que en el arranque normal: la
   sala lo manda con `?entrar=1`, el juego lo reconoce (`soyCabeza`) y entra.

## Cuidados

- **Si entra en la última ronda**, ya no le toca jugar (`R − ronda = 0`): hay que
  avisarle o no dejarlo. En Opciones se avisa.
- **El lado** del invitado sale de `conQuien`: si lo invitó el administrador,
  juega el lado A; si lo invitó la pareja, el lado B.
- **Sin repetir** en su lista cuando el lado tiene suficientes opciones; se
  permite repetir solo si no alcanzan.
- **Los invitados deben estar registrados** (existan en los usuarios del
  anfitrión) para poder agregarlos. Este mecanismo es para meterlos con la
  partida andando, no para registrarlos.

## Atajo: mostrar el QR desde el juego

Para no tener que salir a registrar al invitado, el juego puede mostrar el **QR
del anfitrión** con `qrcodejs` (el mismo que usa el inicio):

```js
new QRCode(caja, {
  text: JSON.stringify({ firebase: g.firebase, telegram: g.telegram || null }),
  width: 200, height: 200, correctLevel: QRCode.CorrectLevel.M
});
```

donde `g = leerConfigGuardada()` (de `config.js`). El invitado escanea, se
registra, y el anfitrión lo agrega con el botón — todo sin navegar. En Opciones
es el botón **"Mostrar código QR"**.

## Dónde está en el código de referencia

- `Opciones/index.html`:
  - `siguienteTurno()` — devuelve `nuevaRonda`.
  - `aplicarPick()` / `saltarTurno()` — suben `ronda` cuando hay ronda nueva.
  - `disponiblesInvitados()` — invitados registrados que no están en la partida.
  - `abrirAgregar()` — la ventana con la lista para elegir.
  - `agregarInvitado(id)` — la transacción y el re-publicar de la invitación.

---

### Invitado a media partida en Castigos y Encuentros

### Invitado a media partida: acciones distintas (Castigos y Encuentros)

**Regla vigente:** cuando alguien entra con la partida ya empezada, sus turnos
restantes **no se copian** del compañero de su lado. Por cada ronda que le falta
se toma el **nivel** que le tocaría (el de la acción del compañero en esa ronda)
y se elige **otra acción del mismo nivel y lado**, sacada de la actividad
elegida o de las actividades de la partida. Se prefieren las que no se han usado;
si la bolsa se agota se permite repetir, pero **nunca la misma acción del
compañero en esa ronda**. Si el contenido no se puede leer, se copia como
respaldo (comportamiento anterior).

- **Castigos** (`Castigos/` → `turnosConInvitado()`): aplica a normal,
  Multi y Placer extremo, en "cada quien el suyo" y en "un celular". Sus turnos
  entran al final de cada ronda restante y **no llevan imposiciones nuevas**.
- **Encuentros** (`Encuentros/` → `listaConInvitado()`): cada jugador
  tiene una lista por ronda; el invitado recibe la suya con acciones distintas y
  entra al final de la rotación. Si el contenido no está en memoria, se lee de
  `nivelesActividad` (`cargarActsParaInvitado()`).
- **Opciones** no cambia: ya generaba su lista al azar (`R - ronda` opciones del
  lado) y lo hace entrar desde la ronda siguiente (`agregarInvitado()`).

No se toca el largo de la partida ni la lista de los demás jugadores.

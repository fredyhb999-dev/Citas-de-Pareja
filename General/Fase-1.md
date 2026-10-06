# Fase 1 — Encuentros Guiados, modo invitado y sala de espera

oct-2026 · repo `Documents\GitHub\Citas-de-Pareja`

Qué se hizo en esta ronda y por qué, para que cualquier chat siga sin perder
contexto.

Alcance: **corrección de lo que ya existía** + **un lugar común para las
partidas con invitados**.

Estado: **hecho y verificado con 22 pruebas automáticas. Pendiente de probar en
el celular por Fredy. NO se ha subido todavía.**

---

## 1. La regla que resume todo

> **El invitado solo está dentro mientras dura la partida. Cuando termina, se le
> devuelve su información y sale. No hay salida libre, en ningún juego.**

Consecuencia que costó aprender: **tener copia de seguridad NO significa ser
invitado.** Son dos cosas distintas, y antes el código las confundía. Esa
confusión era el origen de casi todo lo que se arregló aquí.

---

## 2. Modo invitado

### 2.1 Lo que estaba mal

Al apretar "Entrar modo invitado 📷" se guardaba la copia de seguridad **antes
de escanear nada**, y esa copia era lo que decidía si el invitado "estaba de
visita". Encadenado:

| Dónde se notaba | Síntoma |
|---|---|
| Pantalla de Invitados | Decía "Estás de visita" y ofrecía el botón "Salir modo invitado" |
| Ese botón | Preguntaba *"También te borro de sus usuarios"* sin haberse registrado nunca |
| **Diablitos** | **Escondía el engrane**, porque pregunta por la misma copia |

Es decir: entrar a ver la opción y salirse ya te dejaba marcado.

### 2.2 Y un problema más serio

Al **escanear un QR válido** la app sobrescribe la configuración de Firebase con
la del anfitrión, pero la identidad seguía siendo la propia y **nunca se te
registraba** en su lista de usuarios. Si te salías en ese punto, el teléfono
quedaba apuntando a la base de datos de otra persona: se podía **leer y escribir
en la base de alguien que no te había invitado**.

Por eso la copia se toma **en el momento exacto de escanear** (es lo último
antes de cambiar la base) y no antes.

### 2.3 Lo que quedó

| Momento | Qué dice la app | Botón de salir | Diablitos |
|---|---|---|---|
| Solo miraste la opción | "Entra a otra base como invitado…" | no sale | engrane normal |
| Escaneaste, estás escribiendo tu nombre | **"Solicitando Acceso"** | no sale | engrane normal |
| **Ya te registraste** | "Estás de visita. Al salir vuelves a tu base." | **sí sale** | engrane oculto |
| Escaneaste y te saliste | Vuelve todo a como estaba, **solo y sin preguntar** | — | — |
| Cerraste la app a medio camino | Al abrir, restaura **antes de conectarse a nada** | — | — |

"Salir sin preguntar" es a propósito (decisión de Fredy): si te sales a medio
camino, se deshace todo en silencio.

**Ese es el momento exacto en que se es invitado: cuando te registraste.**

Al registrarte **no aparece ninguna ventana**: se va directo a la sala de
espera. Se usa `location.replace` y no `href`, para que el botón atrás del
celular no devuelva al formulario de registro de otra persona.

### 2.4 Lo que queda en el teléfono mientras eres invitado

| Qué | Qué tan grave |
|---|---|
| Lista de nombres de usuarios del anfitrión | Bajo, son nombres |
| Config de Firebase del anfitrión (la "dirección" de su base) | Bajo |
| **Códigos de acceso del anfitrión** | **Eliminado (ver sección 4)** |

Cuando se te expulsa, tu copia restaura todo y esos datos desaparecen.

---

## 3. Encuentros Guiados — los 5 problemas

### 3.1 El tag de nivel nunca se veía — **NO ERA UN BUG**

`Encuentros/index.html:123` traía `<div id="nivelTag" hidden>` y el código solo
hacía `tag.style.display = ""`, que **borra** la declaración en línea pero no
quita el atributo `hidden`. Se preguntó y **Fredy confirmó que el nivel se
pidió escondido a propósito**: se queda así. El texto se escribe igual, pero no
se muestra.

Ojo: el mismo patrón está en `Guiadas/index.html:171`. Si algún día se quiere
mostrar, hay que quitar el `hidden` o poner `tag.hidden = false`.

### 3.2 Se podía salir de la partida sin querer — **ARREGLADO**

Había **tres** salidas automáticas y solo dos eran las oficiales
("Pausar y Salir" y "Terminar Partida"):

| # | Cómo se salía | ¿Quedaba registrada la salida? |
|---|---|---|
| 1 | Botón "← Lista" (arriba a la derecha) | no |
| 2 | **Gesto de atrás del celular** | no |
| 3 | Enlace "← Inicio" (arriba a la izquierda) | no |

Regla de Fredy: **durante la partida nadie sale**. Ahora las tres están cerradas:
el botón se borró, "← Inicio" se oculta mientras juegas, y el gesto de atrás no
hace nada (se devuelve al estado del juego en vez de dejarte salir). Los dos
botones oficiales siguen igual.

**Consecuencia:** el invitado también queda atrapado en la partida. Se queda
hasta que la partida acaba, y entonces el juego lo expulsa.

### 3.3 La partida se trababa si alguien ya no estaba — **ARREGLADO**

`avanzarSesion()` exige `d.orden[d.turno] === miId`. Si ese jugador ya no
existe, **nadie puede avanzar nunca** y la partida queda congelada. Se reprodujo:
4 clics, ronda sin avanzar.

Causa: al salir del modo invitado se borraba al usuario de `config/ajustes` pero
**no de `sesionEncuentros/actual.cabezas/orden`**. Quedaba fantasma.

**Decisión de Fredy: se brinca y siguen los que quedan.** Se implementó
`sanearSesion()`: quita a los que ya no están de `cabezas`, `orden` y `listas`,
y si le tocaba a uno de ellos ahora le toca al siguiente que quede. Se aplica al
retomar, al unirse, **y en vivo** (una escucha de `config/ajustes` recalcula el
turno en el momento). De paso, **las acciones del que se va se borran del
documento**.

### 3.4 A los invitados les llegaban acciones de otro nivel — **ARREGLADO**

Eran dos fallas separadas:

1. **Injusticia**: el pool de cada nivel se repartía "el que llega primero", y
   el anfitrión se lo llevaba entero.
2. **Faltan datos**: con tomas `básico:3` y 2 personas del mismo lado se
   necesitan 6 y solo hay 3. Eso no es un bug, es que no hay suficientes.

Arreglo: reparto por posición (en cada una, **todos los del mismo lado sacan
del mismo nivel**) y, cuando el nivel no alcanza, **se repite una de ese mismo
nivel** antes de mezclar niveles. La mezcla de niveles solo ocurre si la
actividad **no tiene ninguna** acción de ese nivel.

Comprobado con tomas `2,2,1,1,1` y 3 jugadores: **los tres reciben exactamente
`Básico > Básico > Medio > Medio > Avanzado > Experto > Alucinado`**.

### 3.5 El anfitrión nunca veía el aviso de fin — **ARREGLADO**

El aviso "¡Se acabó la partida!" solo le llegaba a los invitados; el anfitrión y
la pareja caían mudos a la lista. `#finMsg` ("¡Encuentro completo! 🔥") era
**código muerto**: solo se alcanzaba jugando sin internet.

Ahora les llega a los tres. Ojo: cuando **el anfitrión aprieta "Terminar
Partida"** no le sale a nadie, porque él mismo lo decidió.

### 3.6 Botón "Saltar turno" (nuevo, solo anfitrión)

Para cuando a alguien se le **cae la red o se le apaga el celular**: sigue en el
turno y el juego lo espera para siempre.

- Solo el anfitrión lo ve.
- Solo aparece cuando **no es su turno**.
- El texto dice a quién: "Saltar turno de Pareja".
- Pide confirmación.
- Si el saltado era el último de la ronda, la ronda avanza y se revuelve el
  orden.

---

## 4. Fuga de códigos de acceso (corregida)

**El hallazgo más delicado de la ronda.**

Mientras eres invitado, la configuración del teléfono es la del anfitrión. La
app escucha el catálogo de esa base y, sin protección, **guardaba en el teléfono
del invitado los códigos de acceso del anfitrión**, de forma automática al
volver a abrir la app.

Comprobado de las dos formas:

| | Contenido de `licencias` en el teléfono del invitado |
|---|---|
| **Sin** protección | `{"guided":"COD-MIO", "encuentros":"encuentros\|host\|host@ejemplo.mx"}` |
| **Con** protección | `{"guided":"COD-MIO"}` |

Choca con lo que ya decía la guía ("las licencias NO viajan al modo invitado").
Arreglo en `acceso.js`: mientras la identidad diga invitado, se revisa el
catálogo del anfitrión pero **no se guarda ningún código nuevo**. Al expulsarse,
`restaurar()` deja las licencias como estaban.

**Nota sobre las pruebas:** la primera versión de esta prueba daba "OK" aunque la
protección no estuviera — estaba mal planteada. Hubo que rehacerla y comprobar
que **sin** la protección **falla**. Regla que queda: si una prueba da verde,
hay que verificarla **quitando lo que se acaba de arreglar**.

---

## 5. La sala de espera (`Diablitos`)

### 5.1 Qué era y qué es

`Diablitos` ya se llamaba "Sala de Espera" pero era solo eso: un juego local
tocar-diablitos. No tenía salida a ningún lado, no usaba internet y no tenía
forma de enterarse de una partida.

Ahora es **el lugar donde espera el invitado**. Sin salida, a propósito: el
invitado no puede pasearse por los datos del anfitrión. Al terminar de
registrarse, el invitado **cae aquí directo**: no hay ninguna ventana que
confirmar.

### 5.2 El patrón, para que se repita en cada juego nuevo

```
Un juego arranca   →  publica su invitación en un documento compartido
La sala la escucha →  le sale la tarjeta con "Entrar"
El invitado entra  →  se queda ahí hasta que la partida acaba
La partida acaba   →  la sala lo expulsa sola y le devuelve su información
```

Un juego con invitados **no copia nada de lógica**: solo publica su invitación.
Ese es el motivo de centralizarlo en `invitado.js`.

### 5.3 Dónde viven las invitaciones

Documento `invitaciones/{idDelJuego}` en la base de la pareja. **Uno por juego**,
no una lista que crezca:

```js
{ juego:"encuentros", titulo:"Encuentros Guiados", icono:"💫", ruta:"Encuentros",
  hostUid, hostNombre, participantes:[ids], activa:true, sid }
```

- Un juego publica con `publicarInvitacion()` al arrancar y con
  `retirarInvitacion()` al acabar (natural o "Terminar Partida").
- **Al pausar NO se retira**: la partida no acabó, los que esperan siguen
  teniendo razón para entrar.
- La sala escucha con `vigilarInvitaciones()` y solo muestra las invitaciones
  donde el invitado está en `participantes`.

**Nada de esto necesita reglas nuevas de Firestore**: es un documento más en la
base de la pareja, con las mismas reglas de siempre.

### 5.4 Qué se ve en la sala

| Estado | Qué aparece |
|---|---|
| No eres invitado | Nada. El juego de diablitos normal, con su engrane |
| Eres invitado, sin partida | "Esperando Invitación…" |
| Eres invitado, con partida | Tarjeta con icono, título y "Anfitrión te está esperando" + botón **Entrar** |
| La invitación desaparece | Expulsión automática y regreso a su propia base |

**La sala es SOLO para invitados** (decisión de Fredy, oct-2026). La pareja no
es invitada: no ve el panel ni entra aquí por su cuenta.

**Al pausar el anfitrión** (quien ve el aviso de pausa):
- **El invitado** va a la sala. La partida está PAUSADA, no terminada, así que
  **no se le expulsa**: la invitación sigue viva y desde la sala puede volver a
  entrar con "Entrar" cuando el anfitrión retome.
- **La pareja** se queda en la pantalla de espera de Encuentros, que es suya.

Al terminar la partida (no al pausar) la invitación se retira y el invitado sale
solo, esté donde esté.

### 5.5 Lo importante: la sala NO puede romper el juego

El bloque que escucha invitaciones va **aparte**, en un `<script type="module">`
propio. El juego de diablitos sigue siendo un `<script>` normal sin internet:

- Si no hay internet, o la configuración falla, o algo se cae → el bloque se
  queda callado y **el juego funciona exactamente igual que antes**.
- No se le importó nada de Firebase al juego.

### 5.6 Dónde aparece Diablitos en el menú

**Fijo para todos, sin candado** (decisión de Fredy, oct-2026). No va por el
catálogo: está escrito en `renderPacksDeVerdad()` con `libre: true`, que salta la
comprobación de licencia. Así el submenú **🎮 Juegos** aparece siempre y
Diablitos se ve sin pedir acceso.

Los demás juegos siguen **armándose solos** desde el catálogo (`packs`), con su
candado. `FIJOS` es la lista de los que no se leen del catálogo (`guiadas` y
`diablitos`), para que no se dupliquen si algún día alguien los da de alta ahí.

---

## 6. Archivos tocados

| Archivo | Qué cambió |
|---|---|
| **`invitado.js`** | **Nuevo.** Un solo lugar para: cuándo eres invitado de verdad, copiar/restaurar, salir, y **publicar/retirar/vigilar invitaciones** |
| `index.html` | Usa `invitado.js`; el modo invitado solo empieza al registrarse; "Solicitando Acceso"; salidas en silencio; recuperación al abrir; **el invitado registrado va a la sala** (antes a Encuentros); **Diablitos fijo en el menú, sin candado** |
| `acceso.js` | `soyInvitadoAhora()` + guarda en `escucharCatalogo` para no guardar códigos siendo invitado |
| `Encuentros/index.html` | Secciones 3.2 a 3.6 + publicar/retirar invitación + al pausar, el invitado vuelve a la sala |
| `Diablitos/index.html` | Panel de la sala (espera, tarjeta, entrada, expulsión) + `esModoInvitado()` corregido |

Se borraron del inicio las copias de `hayRespaldo()` / `respaldarSesion()` /
`restaurarSesion()`: quedan en un solo lugar, que es la razón por la que este
repo ya tiene `acceso.js` y ahora también `invitado.js`.

---

## 7. Cómo se verificó

Con un arnés propio (`Temp\opencode\`): **Firestore simulado en memoria +
Chrome headless**. No es "se ve bien", es la app corriendo de verdad.

| Suite | Casos |
|---|---|
| **Encuentros** (12) | niveles · invitación · anfitrión · botón saltar · fin · invitación al invitado · pareja · pausa · fin con limpieza · se fue un invitado · multi · partida vieja · sin licencia |
| **Inicio** (6) | nada · escaneo a medio camino · registro completo · recuperación al abrir · invitado ya registrado con códigos · menú (Diablitos sin candado) |
| **Sala** (4) | no eres invitado · invitado esperando · con invitación · expulsión al acabar |

**22 casos, todos sin errores de JavaScript.**

Lo que se comprobó de la sala, en orden:

```
invitado, sin partida  -> "Esperando Invitación…", sin tarjeta
con invitación        -> tarjeta con título/icono/anfitrión, Entrar -> Encuentros
la invitación se retira -> expulsión solo: respaldo borrado, base y identidad propias
el juego de diablitos   -> arranca en los 4 escenarios, con y sin internet
```

---

## 8. Cómo volver a probarlo

1. Fredy sube con **GitHub Desktop**.
2. Espera 1–2 min.
3. Incógnito o **Ctrl+Shift+R**.

**Encuentros**
1. Arma partida con invitado; confirma que **todos** reciben el mismo orden de niveles.
2. Intenta salir con gesto de atrás y con "← Inicio": **no te deja**.
3. Cuando le toque a tu pareja, sale "Saltar turno de [nombre]".
4. Termina la última ronda: les llega el mensaje a ti y a tu pareja.
5. Desde el ⚙️ borras a un invitado en pleno juego: el turno **se brinca solo**.
6. **Pausa**: el invitado vuelve a la **sala**; tu pareja se queda en la pantalla de espera de Encuentros. Al retomar, el invitado entra otra vez desde la tarjeta de la sala.

**Menú**
7. En el inicio debe estar el botón **🎮 Juegos** y, dentro, **Diablitos** sin candado.

**Modo invitado**
8. ⚙️ → Invitados → "Entrar modo invitado" y **te sales sin escanear**: todo igual, sin rastro.
9. Escanea un QR y te sales: **todo se restaura solo**.
10. Escanea y **te registras**: **te manda directo a la sala** (sin ventana de "Listo" que aplastar), ves "Esperando Invitación…", y si abres el ⚙️ dice "Estás de visita" con su botón de salir.
11. Con la partida en curso, **borra al invitado** desde el ⚙️: al volver a abrir la app se expulsa solo.

**Sala (necesita dos teléfonos)**
12. Teléfono A: entra como invitado, llega a Diablitos, ve "Esperando Invitación…".
13. Teléfono B: anfitrión arma una partida en Encuentros.
14. En A debe salir la tarjeta. Entrar. Jugar.
15. Al terminar la partida, A debe salir solo del modo invitado y volver a su base.

**Pendiente por falta de una segunda persona:** el paso 10–13 completo con dos
teléfonos reales. Hasta esa prueba, la sala queda a medio validar.

---

## 9. Límites conocidos que dejó esta ronda

| Límite | Nota |
|---|---|
| Invitado apaga el celular o pierde red | Sigue en el turno. Mitigación: botón "Saltar turno" del anfitrión |
| **Sin internet**, el invitado no se expulsa al abrir | Deliberado y viejo: no se expulsa a nadie de una partida en curso por un corte de red. Solo afecta al reinicio |
| Invitado que nunca recibe invitación | Espera indefinidamente en la sala. Cerrar la app lo resuelve |
| Escaneó y se salió | Se pierde el QR y hay que escanear de nuevo. Preferible a quedar pegado a una base ajena |
| Varios juegos con invitación a la vez | La sala muestra el primero. Falta decidir el orden |
| Datos viejos de "invitado de invitado" | No se limpian (ya estaba en pendientes antes de esta ronda) |

---

## 10. Decisiones tomadas

**Decidido por Fredy (oct-2026):**

| Decisión | Detalle |
|---|---|
| Al registrarse, **directo a la sala** | Sin ventana de "¡Listo!". Con `location.replace` para que atrás no regrese al formulario de otra persona |
| **Diablitos NO lleva candado, y va en el menú** | Fijo en el submenú **🎮 Juegos** para todos (ver 5.6). El resto de juegos se sigue armando solo desde el catálogo |
| **La sala es solo para invitados** | La pareja no es invitada: no ve el panel ni entra por su cuenta |
| **Al pausar**: el invitado va a la sala, la pareja se queda | Ver 5.4. Al *terminar* (no al pausar) el invitado sale solo, esté donde esté |
| **Se brinca al que ya no está** | En vez de parar la partida (sección 3.3) |
| **Nivel escondido** | El tag de nivel se pidió oculto: no es bug (sección 3.1) |

**Pendiente de Fredy (no de código):**

- **Probar la sala con dos teléfonos reales.** Es lo único del flujo de la sala
  que no se ha validado en vivo (todo lo demás se probó con la app simulada).
- Cuando haya más juegos con invitados, **ver dónde posicionarlos** en el
  submenú Juegos (hoy Diablitos está fijo; el resto sale del catálogo).

---

## 11. Nota de mantenimiento

- **`General/` es la consolidada.** Cualquier cambio de esta fase debe
  reflejarse en `GUIA-PROYECTOS.md` (estado general + pendientes) con el formato
  `Hecho (mes, publicado): ...`, cuando se suba.
- Al guardar texto en Windows, si un archivo sale con los acentos duplicados la
  causa es doble conversión UTF-8. Ver `GUIA-PROYECTOS.md` §10.
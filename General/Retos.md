### Completar un reto NUNCA descuenta puntos (regla, oct-2026)

Un reto normal se paga así: cada **"Cumplida +1"** suma **+1** al que lo tiene
que hacer (`asignadoA`), y **nada más**. Al llegar a la meta el reto pasa a
`"cobrada"` y **no se resta absolutamente nada**. Solo se descuenta cuando
**no** se cumple, y entonces es `penalizacionPuntos`.

**Antes (oct-2026) sí se restaba** y por eso completaba un reto no dejaba nada
acumulado. Se quitó por decisión de Fredy. Ojo: **`puntosMeta` hoy es el número
de veces que hay que apretar**, no una cantidad que se cobre.

> **Por qué esto importa:** el cambio se hizo en la lógica y se dejó un texto
> viejo en la tarjeta (`Retos/index.html`, la nota `nota warn` del reto en
> curso) que todavía decía *"y se descuentan 5 pts"*. El usuario veía que le
> advertían de un descuento que ya no existía. Ya se quitó esa frase: ahora solo
> dice qué pasa **si no** se cumple, que es el único caso con descuento.

**El botón "Cumplida +1" solo lo ve quien propuso el reto** (`soyProponente`,
en la lista de acciones). La pareja no lo ve. Por eso el doble toque
simultáneo es improbable: solo pasaría si el mismo aprieta desde dos lugares a
la vez. La falta de transacción queda anotada como pendiente de bajo riesgo.

### La meta de un reto se calcula sola (oct-2026)

En `Retos/`, al proponer un reto hay tres campos pegados: "veces al día",
"duración (días)" y "puntos para cumplir". La meta es **`veces × días`**, y eso
**ya no se escribe a mano**: se calcula solo y el campo queda **de solo lectura**
(se ve apagado, con borde punteado). Debajo dice la cuenta: *"Se calcula solo:
2 × 7 = 14 puntos."*

**El arreglo tiene dos partes, y las dos hacen falta:**

**1. El campo obedecía una sola vez.** La función se llamaba
`rellenarMetaSiVacio()`: rellenaba **solo si estaba vacío**. En cuanto tenía un
número, ya no volvía a hacer nada. O sea: escribías los días, se llenaba una vez,
y si después cambiabas los días **la meta se quedaba congelada**. Y al **editar
un reto viejo** (que ya traía su número guardado) **nunca** se recalculaba. Por
eso el campo era editable: era el rodeo para poder escribir un número que sí se
alcanzara. Ahora es `calcularMeta()` y sigue a los dos campos siempre.

**2. La cuenta daba un desfase de horas.** El vencimiento era
`ahora + duracionDias × 86400000`, o sea **a la misma hora en que se apachó el
botón**. Ejemplo: propones lunes a las 4 de la tarde, 2 al día durante 7 días → la
meta pedía 14 puntos, pero el reto vencía lunes siguiente a las 4 de la tarde:
había **6 días completos y un medio**, y 14 era casi imposible. Peor: a las 11 de
la noche sí se alcanzaba y a las 4 de la tarde no. **Dependía de la hora.**

**Ahora el reto vive hasta el FINAL de su último día** (`finDeUltimoDia()`): se
pone a las 11:59:59 de la noche del día N y se suma `N - 1` días. Así "7 días"
son 7 días de verdad, da igual a qué hora se proponga. Ojo: **esto mueve la
fecha de vencimiento de los retos nuevos** (terminan unas horas después, que es
justo lo que se busca). Los que ya están guardados conservan su `fechaFin` y no
se tocan.

**Los retos ya guardados no se recalculan (decisión de Fredy, oct-2026).** Al
abrir uno viejo, el campo trae **el número que ya tenía** aunque no cuadre con
sus días, y debajo lo avisa: *"Este reto ya traía su propia meta. No se
recalcula."* Es lo que hace la bandera `metaLibre`: en `true` la meta no se
toca, y en `false` (reto nuevo) se calcula sola. **Los datos que ya existen no
se cambian por sorpresa.**

**Y el contador de "Tiempo restante" (`diasRestantes()`) cuenta días de
calendario, no horas.** Antes dividía las horas que faltaban entre 24; como el
reto vence a las 11:59 de la noche, eso daba **un día de menos** (decía 6
cuando eran 7). Ahora usa `duración − días que ya van`, a partir de
`fechaInicio`. El mínimo es 1 mientras el reto siga vivo, para que el último día
no se vea como "0 días".

**Comprobado con números** (reto de 2 al día durante 7 días, propuesto lunes a
las 4 de la tarde): 7 → 6 → 4 → 1 → 1 → 0 días. Y los retos viejos muestran
exactamente lo mismo que antes.

**Ojo, pendiente y NO se ha tocado:** `Retos/index.html` tiene un
`id="formBotones"` **repetido** (el del formulario y el de "definir recompensa",
L332 y L353; oct-2026: antes decia 326 y 347, ya corrieron). Hoy no rompe nada
porque ningún JavaScript lo usa —solo el CSS—, pero es una bomba de tiempo. Se
arregla aparte.
### Retos: sale de Experiencias y tiene submenú propio

**El problema (hallazgo de Fredy, oct-2026).** Retos estaba como **tarjeta fija
dentro de Experiencias** y además existía un submenú "Retos especiales" que
**nunca tenía nada**, porque ningún catálogo usaba `seccion:"extras"`. El botón
"Volver" apuntaba a ese submenú vacío: se veía bien, pero caías en un lugar sin
nada.

**Lo que quedó:**

| | |
|---|---|
| Retos dentro de Experiencias | **Fuera** |
| Submenú "Retos especiales" | Renombrado a **"Retos"**, al mismo nivel que Juegos |
| Submenú de Retos | Con la tarjeta de Retos + lo que llegue del catálogo |
| "Volver" de Retos | A `#retos`, o sea a su submenú |

**Renombres en el código** (oct-2026): `btnExtras`→`btnRetos`,
`btnExtrasVolver`→`btnRetosVolver`, `vistaExtras`→`vistaRetos`,
`packsExtras`→`packsRetos`, `abrirExtras`→`abrirRetos`,
`cerrarExtras`→`cerrarRetos`.

**Por seguridad se aceptan las dos claves** en el catálogo y en el `#`:
`seccion` puede ser `"retos"` **o** `"extras"`, y el `#` puede ser `#retos` **o**
`#extras`. Así, si hay algo viejo dado de alta en el catálogo, sigue apareciendo
en su sitio en vez de desaparecer en silencio.

**Lección:** un juego va en **un** submenú. Si aparece en dos lados, uno de los
dos queda vacío y el botón "Volver" miente.

**El bug queBZ salió de eso (y que casi se va sin ver).** Al poner la tarjeta de
Retos a mano dentro del submenú, el botón **"Retos" desapareció del menú
principal**: `btnRetos` nace oculto y `renderPacksDeVerdad()` solo lo enciende
si la lista de su submenú tiene algo. Esa lista solo se llenaba con el catálogo,
y Retos no viene del catálogo. Resultado: **no se podía entrar a Retos** (lo
reportó Fredy).

**El arreglo fue mover Retos al mismo mecanismo que Diablitos:** está en la lista
`packs` con `seccion:"retos"` y `libre:true`, y en `FIJOS`. Así el botón se
enciende solo y la tarjeta se pinta como las demás.

**Regla que quedó:** si un submenú tiene algo escrito a mano, **ese submenú no
puede depender del catálogo para mostrarse**. O todo pasa por `packs`, o el botón
se enciende siempre.

**Y por eso el `menu` ahora comprueba los tres submenús** (`btnExp`, `btnJuegos`,
`btnRetos`) y que el de Retos traiga su tarjeta. Antes las pruebas pasaban
iguales con el menú roto: nadie miraba esos botones.


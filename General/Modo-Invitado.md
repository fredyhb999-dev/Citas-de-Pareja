# Modo Invitado

Movido de `General/GUIA.md`. Contiene el detalle del modo invitado: sin salida, vuelta automática al abrir, registro por QR.

---

### El invitado no tiene salida (`pintarSalidas`)

En `Encuentros/index.html`, `pintarSalidas()` decide si el enlace "‹ Volver" se ve.
Se esconde cuando:

- se está **durante la partida** (para nadie se sale a medias), o
- la persona **es invitada** (`esInvitadoFlag`), siempre, en cualquier pantalla.

Se llama desde dos lugares a propósito:

1. en `ver(id)`, cada vez que se cambia de vista;
2. al final de `cargarIdentidad()`, porque ahí es donde se descubre que la
   persona es invitada. Si solo se llamara en `ver()`, y la identidad carga
   después, el invitado vería la salida un instante.

**Cómo se verificó:** en el arnés (**ya retirado**, ver la nota al inicio), `invitado&respaldo=1` y
`invitado&flag=pausa&respaldo=1` (el invitado es `u3`) reportan `lnkInicio`
**oculto**; los escenarios del anfitrión y `invitado&como=u2&flag=natural`
(que en realidad juega como **la pareja**, no como invitado) reportan
**visible**. Esa distinción importa: `u2` es la pareja, `u3` el invitado.

**Ojo al agregar escenarios:** hay casos llamados `invitado` que en realidad
actúan como la pareja, porque se fuerzan con `&como=u2`. La comprobación
distingue por la bandera `invitado` de la identidad, no por el nombre del
escenario.

### El invitado vuelve solo al abrir la app (arreglado oct-2026)

`volverSiInvitadoSinPartida()` (`index.html`) revisa si el invitado tiene una
partida viva en `sesionEncuentros/actual`. Si no la tiene, `salirDeInvitado()`
lo devuelve a su propio espacio y lo saca de la lista de quien lo invitó.

**Lo que estaba roto:** la ruta se escribia como **un solo pedazo**,
`doc(db, "sesionEncuentros/actual")`. En el SDK eso devuelve una *coleccion*,
no un documento; `getDoc` truena y el `catch` de la linea siguiente se lo come.
`leido` se quedaba en `false`, asi que la linea de guarda cortaba siempre: **la
funcion no podia devolver `true` nunca**. En la practica, **el invitado nunca
volvia solo al abrir la app**.

El juego (`Encuentros/index.html:509`) y la sala (`invitado.js:196`) ya usaban
los dos pedazos correctos. **Solo esta lectura estaba mal** y por eso no se
notaba: las otras dos dan el mismo resultado y nunca fallaban en voz alta.

> **Ojo con lo que dice este mismo archivo:** la Fase 1 del modo invitado
> estaba escrita como "cerrada, verificada y probada por Fredy". **En este
> punto no era cierto**: el criterio se daba por cumplido y nunca se ejecuto.
> Sirve de regla: *probado* significa que se ejecuto, no que se reviso el
> codigo.

**PROBADO EN VIVO (Fredy, oct-2026):** las dos pruebas, las dos pasaron. Un
invitado con partida en curso no es expulsado; uno sin ella vuelve solo a su
propio espacio y sale de la lista de quien lo invitó.

**Al expulsar a un invitado se le pone el saldo en cero** (oct-2026, decisión de
Fredy). `salirDeInvitado()` ya borraba su ficha de la lista del anfitrión; ahora
además deja `puntosUsuarios/{id}` en `0` (**no borra el documento**). Antes ese
saldo se quedaba ahí guardado y **nadie lo volvía a leer jamás**, porque al
registrarse de nuevo el invitado trae otro id. Los saldos que **ya** quedaron
antes de este cambio no se limpian: quedan ahí y se dejan.

### Registrarse por QR otra vez ya no duplica al invitado (arreglado oct-2026)

El registro de invitado (`index.html`, botón "Confirmar") tiene **tres reglas** que
se respetan juntas:

1. **Si esa persona SIGUE en la lista, se entra con SU MISMA ficha.** No se
   crea otra y no sale ningún aviso.

> **Ojo, esto tiene fecha de caducidad:** la ficha **solo existe mientras el
> invitado no haya sido expulsado**. Al terminar el juego, `salirDeInvitado()`
> **lo borra de la lista del anfitrión**. O sea:
>
> | Cuándo | Qué pasa al volver a escanear |
> |---|---|
> | Escaneó, quedó esperando y **vuelve a escanear sin haber jugado** | Misma ficha, **conserva sus puntos**, sin duplicado |
> | **Jugó y lo expulsaron** | Ficha nueva, id nuevo y **0 puntos**. Igual que antes de este cambio |
>
> Los puntos que dejó la ficha vieja **se quedan guardados** en
> `puntosUsuarios/{idViejo}`, pero ya nadie los vuelve a usar.
2. Solo reutiliza una ficha que sea **de invitado** y **del mismo anfitrión**, y
   solo si hay **una sola** con ese nombre. Si hubiera dos "Luis", **no se
   adivina**: se crea una nueva. Nunca puede "&iquo;colarse&iquo;" en la cuenta
   de la pareja.
3. El nombre se compara **sin mayúsculas y sin acentos**: "Jose" y "José" son la
   misma persona (`normalizaNombre()`).

**Lo que estaba roto (dos cosas, de la misma causa):**

| | |
|---|---|
| **Nombre interno repetible** | Se calculaba "el siguiente número disponible", pero el invitado que crea el ⚙️ usa un código con hora y azar que el buscador no veía. Con dos registros en el mismo instante, los dos podían salir con el mismo nombre interno |
| **Se pisaban entre ellos** *(esto no estaba anotado en ningún lado)* | El leer-calcular-guardar iba suelto, sin protección. **Dos personas registrando por QR al mismo tiempo: la segunda escritura borraba a la primera de la lista.** No daba error, el invitado simplemente desaparecía |

**El arreglo:** el identificador nuevo lleva hora y azar (igual que el del
engrane), y todo el leer-calcular-guardar va **dentro de una transacción**, que
vuelve a leer la lista antes de escribir. Si entran dos a la vez, Firestore las
corre una detrás de otra y **las dos quedan**.

**Por qué el identificador con hora puede coexistir con los viejos:** el único
lugar del programa que daba por hecho el formato `u1`, `u2`, `u3` era **esta misma
línea que se cambió**. Ninguna otra parte lee, ordena ni compara ese código
interno: la app siempre muestra el **nombre**. Los usuarios que ya existen no se
tocan.

**PROBADO EN VIVO (Fredy, oct-2026):** las tres pasaron. Volver a escanear con
el mismo nombre devuelve la misma ficha (tambien **sin acentos**: "Jose" y
"José" son la misma persona) y no crea un segundo nombre en la lista; y dos
personas registrándose al mismo tiempo **quedan las dos**, no se pisan.


# Packs de personajes

> Detalle de la función **packs de personajes**: ítems del catálogo que instalan sus
> personajes en las listas de la pareja. Diseñada y acordada con Fredy (nov-2026) e
> implementada en nov-2026; lo único pendiente es la prueba en vivo (12.2).

Este documento es la **fuente única** de la función. Está escrito para que otra sesión
u otro modelo lo ejecute **sin depender de la conversación donde se diseñó**.

---

## 0. Antes de escribir una línea

1. Leer `AGENTS.md` (reglas de la casa) y `General/GUIA.md` (lo que es cierto hoy).
2. Leer `General/Roles.md` y `General/Modelo-Datos.md`. Si vas a tocar Panel o Tienda,
   lee también `General/Pantallas.md` y `General/Catalogo.md`.
3. Leer este documento entero.
4. **No implementar nada que no esté aquí.** Si falta una decisión, preguntar a Fredy;
   no inventar.
5. La regla 0 manda: este documento **no autoriza** a tocar el repo. Se empieza cuando
   Fredy lo pida expresamente.

---

## 1. Qué se va a construir

Vender **packs de personajes** como ítems del catálogo. Al aprobarse la licencia, el pack
se instala solo en la base de la pareja, dentro de sus listas de personajes. Un editor en
`Panel/catalogo.html` -> Extras permite crear los packs. La tarjeta del pack en
`Tienda/index.html` -> Extras muestra si está instalado y permite reinstalarlo a mano.

**Sin duplicar datos de personajes.** El pack vive una sola vez, en la base de taquilla.
La pareja recibe una copia instalada en su propia base, que es la que edita. Lo único que
se repite es la **referencia** (`par`), no el contenido.

---

## 2. Reglas cerradas (no reabrir)

1. **A = masculino, B = femenino. Siempre.** El lado nunca se decide por quién
   administra ni por el orden de los usuarios. En código: `ladoDeUsuario()`.
2. **La llave es el id, nunca el nombre** (regla 11 del repo).
3. **No se duplica contenido.** El pack no copia personajes de la pareja ni al revés.
4. **Los packs son siempre nuevos.** No hay versiones ni actualizaciones de un pack ya
   instalado. Si `packsInstalados[packId]` existe, no se vuelve a instalar.
5. **Revocar el acceso no borra nada** de lo instalado.
6. **Primera instalación automática**, sin confirmación, con un `aviso()` al final.
   **Reinstalación manual**, desde la tarjeta del pack en Tienda -> Expansiones
   (clave interna `extras`). La Tienda exige la licencia vigente de Roles para
   pedir, abrir o reinstalar (nov-2026).
7. **No hay tarjeta de packs de personajes en el menú principal.** Solo Tienda -> Extras.
8. **Cada pack es su propio ítem del catálogo**: su solicitud, su aprobación, su licencia.
9. **El invitado no necesita nada especial.** Elige anatomía al registrarse (ya existe).
10. **Los pares son siempre un hombre y una mujer.** Un pack lleva la misma cantidad de
    pares con normal hombre y con normal mujer, mínimo uno de cada uno, y el total de
    pares es par.
11. **No se toca** `ladoDeUsuario`, las reglas de Firebase, ni los juegos existentes más
    allá de lo que dice este documento.
12. **No se usa `confirm()` ni `alert()`**: solo `confirmar()` y `aviso()` de
    `confirmar.js`.
13. Un botón que JavaScript debe ocultar **nace oculto** en el HTML.

---

## 3. Estado actual (evidencia)

> Las líneas son de hoy (nov-2026) y pueden moverse. Se busca por nombre de función.

### 3.1 Lados y anatomía

- `config.js` -> `ladoDeUsuario(u)` (líneas 128-133):
  `femenino` -> B, `masculino` -> A; si no hay anatomía, `u.admin ? "A" : "B"`.
- `config.js` -> `ladoDeInvitado(u, lista)` (136-141): manda su anatomía; si no, la de
  quien lo invitó.
- `General/GUIA.md` -> *La anatomía define el contenido, no el administrador* (línea 66).
- En Roles, `"1" = lado A (masculino)` y `"2" = lado B (femenino)` (comentario en 3793).
- `Roles/index.html` -> `ladoAnatomiaCfg()` (3801): el editor abre en el lado de la
  anatomía de quien lo usa, no en el del admin.

### 3.2 Personajes

- Documento: `personajesJuego/actual`, con `U1`, `U2`, `C1`, `C2` y `ESP`.
- `Roles/index.html` -> `cargarPersonajes()` (981-996) y `guardarPersonajes()`
  (1003-1010). El guardado usa `merge: true`: **no borra** campos que no menciona
  (por eso `packsInstalados` sobrevivirá a las ediciones).
- Personaje (forma exacta, `personajeDe()` en 3933-3951):
  `{ id, par, personaje, situacion, gancho, derechos, si_quieres, imagen }`
  - `id` es **número**.
  - `par` es `null` en los originales; en la contraparte es **el id del original**.
  - **No tiene `genero`.** No se lo agregues: el editor reconstruye el objeto al guardar
    y lo perdería. El lado se sabe por la lista en la que está.
- `ESP` es un arreglo de **textos** (variantes picantes), no de objetos
  (`agregarEspecial()`, 3965-3972).
- `idSiguiente` (971) se calcula con el máximo de `U1..C2` al cargar (988-992). Ojo: no
  mira `ESP`; el módulo nuevo debe calcular el máximo sobre las cinco listas.

### 3.3 Parejas (lo que hoy asume la lista)

- `contraparteDe(idOriginal, ladoOriginal, mismo)` (1071-1077): elige la lista por lado
  (`U1`->`C2`, `U2`->`C1`) o por el modo mismo lado (`U1`->`C1`, `U2`->`C2`), y busca
  `c.par === idOriginal`. Exige **exactamente un** resultado.
- `paresDisponibles(lado, mismo)` (1080-1086): recorre `U` del lado y filtra los que
  tienen contraparte.
- `poolsDuelo(cabezas, pares, lado, mismo)` (1094-1110): si `mismo`, el admin recibe
  `par.o` y el resto `par.c`; si no, el lado elegido recibe `par.o` y el otro `par.c`.
- `poolsEspejoMismo()` (2647-2661): admin `U<n>`, resto `C<n>` (lista fija).
- `listaDeCabezaPara()` (2664): misma idea para el modo actual.
- `selPoolDe(cab)` (2922-2926): `U<n>` + `C<n>`.
- `agregarInvitado()` (2408): en Duelo asigna `cab.lado === ladoDuelo ? par.o : par.c`
  (2439-2446).
- `contraDeRonda()` (2397-2407): `lado === ladoOriginal ? par.c : par.o`.
- `mismosLados()` (2639-2641) y `dueloMismoLado` (2741).
- `avisosCorrespondencia()`: aviso blando si una pareja no cuadra.

### 3.4 Catálogo y licencias

- Los packs viven en la colección `packs` de la base de **taquilla**.
- `Panel/catalogo.html`: formulario en 284-352; guarda con
  `setDoc(doc(db, "packs", id), data, { merge: true })` (344). Campos actuales:
  `titulo, icono, desc, ruta, seccion, orden, activo, nuevoHasta`. **No** pone `oficial`
  ni `tipo`.
- `Tienda/index.html`: `tarjetaPack(p)` en 266-306. Estado "Se agregó a tu menú" si
  `tieneCodigoValido(p.id)` (287), "Pedir acceso" si no.
- `acceso.js` -> `oficialesAprobados()` (109-124): devuelve los packs `oficial: true`,
  activos, con licencia válida para esta pareja. **Es la fuente para instalar.**
- `Tienda` solo usa la base de taquilla hoy (importa Firestore en 99;
  `getFirestore(appTaq())`).

### 3.5 Precedente de instalación

- `config.js` -> `asegurarFabrica(db, fabrica)` (278-312) y `sembrarColeccion()`
  (235-254): patrón "instalar una sola vez, nunca pisar lo del usuario, anotar lo
  instalado". El módulo nuevo sigue esa idea, pero con ids y slots.

---

## 4. Modelo de datos

### 4.1 Documento del pack (taquilla: `packs/{id}`)

Campos nuevos sobre el ítem actual:

```json
{
  "id": "pack-oficina-01",
  "tipo": "personajes",
  "oficial": true,
  "activo": true,
  "seccion": "extras",
  "titulo": "Oficina",
  "icono": "🎭",
  "desc": "Seis pares para jugar en la oficina.",
  "ruta": "Roles",
  "orden": 10,
  "nuevoHasta": null,
  "pares": [
    {
      "normal": {
        "personaje": "Bruno",
        "genero": "A",
        "situacion": "...",
        "gancho": "...",
        "derechos": "...",
        "si_quieres": "...",
        "imagen": "https://..."
      },
      "contraparte": {
        "personaje": "Bruna",
        "genero": "B",
        "situacion": "...",
        "gancho": "...",
        "derechos": "...",
        "si_quieres": "...",
        "imagen": ""
      }
    }
  ],
  "variantes": ["texto de variante picante", "otra"]
}
```

- `pares` es obligatorio y no vacío.
- `variantes` es opcional (arreglo de textos).
- **El pack no lleva ids.** Los ids se asignan al instalar.
- `imagen` solo puede ser una URL (`http...`) o una ruta del repo. **Nunca base64**
  (`data:`), por el límite de 1 MiB de Firestore.

### 4.2 Estado instalado (pareja: `personajesJuego/actual`)

Campo nuevo, junto a `U1/U2/C1/C2/ESP`:

```json
"packsInstalados": {
  "pack-oficina-01": {
    "fecha": "<Timestamp>",
    "pares": [
      { "normalId": 41, "contraparteId": 42 },
      { "normalId": 43, "contraparteId": 44 }
    ],
    "variantes": ["texto de variante picante"]
  }
}
```

- Es el **mapa de slots**: qué personaje instalado corresponde a cada par del pack.
- Es lo que permite reinstalar sin adivinar y sin tocar los personajes que la pareja
  agregó por su cuenta.
- Es pequeño; no afecta el límite de 1 MiB.
- `packsInstalados` se lee en Roles **solo para mostrar el 🏅** de los personajes
  oficiales (ver `General/Roles.md`); el resto lo sigue leyendo el módulo.

### 4.3 Personaje instalado

Misma forma que ya usa la app (no se agregan campos):

- Original: `{ id: <número>, par: null, personaje, situacion, gancho, derechos, si_quieres, imagen }`
- Contraparte: igual, pero `par: <id del original>`.

### 4.4 Dónde cae cada uno (regla única)

Con `lado = genero` del personaje:

| Personaje | Lista |
|---|---|
| normal `genero: "A"` | `U1` |
| su contraparte (`genero: "B"`) | `C2` |
| normal `genero: "B"` | `U2` |
| su contraparte (`genero: "A"`) | `C1` |

Es el cruce que ya usa el juego (`U1` <-> `C2`, `U2` <-> `C1`). Nunca se cruza un
personaje masculino al lado B ni uno femenino al A.

---

## 5. Instalación automática

### 5.1 Cuándo

En `Roles/index.html` -> `entrar()` (1171), **solo si `ok` y `!esInvitadoFlag`**, después
de `cargarPersonajes()` y antes de pintar el contenido definitivo:

```js
const res = await instalarPacksPersonajes(db);
if(res.instalados.length){
  await cargarPersonajes();     // recarga ids y listas
  pintarInicio();
  aviso("Se instalaron los personajes de: " + res.instalados.join(", "));
}
```

- Si no hay conexión o falla, no se instala y se reintenta en la siguiente apertura.
- No se instala para invitados.
- Solo packs `tipo === "personajes"`, `oficial: true`, `activo !== false` y con licencia
  válida (usar `oficialesAprobados()` de `acceso.js`).

### 5.2 Módulo nuevo

Archivo: `packsPersonajes.js` en la raíz del repo (junto a `acceso.js`).

Imports:

```js
import { doc, getDoc, setDoc, serverTimestamp } from
  "https://www.gstatic.com/firebasejs/10.13.1/firebase-firestore.js";
import { oficialesAprobados } from "./acceso.js";
```

Exporta:

- `instalarPacksPersonajes(db)` -> `{ instalados: [titulos] }`
- `reinstalarPackPersonajes(db, pack)` -> `{ restaurados, recreados, reparados }`
- `leerPacksInstalados(db)` -> objeto (lo usa Tienda)

### 5.3 Algoritmo de instalación

```
1. packs = (await oficialesAprobados()).filter(tipo === "personajes" && activo !== false)
2. si no hay packs -> salir sin escribir nada
3. leer personajesJuego/actual
4. listas = U1, U2, C1, C2 (arreglos) y ESP (textos)
5. packsInstalados = doc.packsInstalados || {}
6. siguienteId = 1 + máximo id numérico de U1,U2,C1,C2 (y ESP si tuviera ids)
7. para cada pack:
     si packsInstalados[pack.id] existe -> saltar (los packs no se actualizan)
     registro = { fecha: serverTimestamp(), pares: [], variantes: [] }
     para cada par del pack:
        idNormal = siguienteId++
        idContra = siguienteId++
        lado = (par.normal.genero === "B") ? "B" : "A"
        listaU = (lado === "A") ? U1 : U2
        listaC = (lado === "A") ? C2 : C1        // cruzado
        listaU.push(personaje(idNormal, par=null, par.normal))
        listaC.push(personaje(idContra, par=idNormal, par.contraparte))
        registro.pares.push({ normalId: idNormal, contraparteId: idContra })
     para cada texto de pack.variantes (opcional):
        si no existe en ESP (comparar sin mayúsculas ni acentos) -> ESP.push y anotar
     packsInstalados[pack.id] = registro
     instalados.push(pack.titulo || pack.id)
8. si hubo cambios:
     setDoc(personajesJuego/actual,
       { U1, U2, C1, C2, ESP, packsInstalados, actualizadoEn: serverTimestamp() },
       { merge: true })
9. devolver { instalados }
```

Notas:

- `personaje(id, par, datos)` copia solo los campos de la forma actual y normaliza a
  texto vacío los que falten.
- No se escribe si no hubo cambios (evita escrituras inútiles en cada apertura).
- Un pack con 0 pares válidos no se instala (el editor no debería permitirlo).

---

## 6. Reinstalación manual

### 6.1 Cuándo

Desde la tarjeta del pack en Tienda -> Extras, con confirmación previa:

```js
if(await confirmar("Se restaurarán los personajes del pack. Lo que hayas editado se pierde. ¿Seguir?")){
  const r = await reinstalarPackPersonajes(dbPareja, p);
  aviso("Listo: " + r.restaurados + " restaurados, " + r.recreados + " recreados.");
}
```

### 6.2 Algoritmo

```
1. leer personajesJuego/actual y packsInstalados
2. si el pack no está en packsInstalados -> ejecutar la instalación normal (sección 5)
3. para cada par k del pack, con su slot = packsInstalados[pack.id].pares[k]:
   a. normal:
      - buscar por slot.normalId en las cuatro listas
      - si no está -> crear con id nuevo (siguienteId++), en U(lado), y actualizar
        slot.normalId; contar "recreado"
      - si está en otra lista -> moverlo a U(lado)
      - pisar sus campos con los del pack (personaje, situacion, gancho, derechos,
        si_quieres, imagen) y poner par: null; conservar el id; contar "restaurado"
   b. contraparte:
      - buscar por slot.contraparteId
      - si no está -> crear con id nuevo en C(cruzado) y actualizar
        slot.contraparteId; contar "recreado"
      - si está en otra lista -> moverla a C(cruzado)
      - pisar sus campos con los del pack y poner par: <id actual del normal>;
        conservar el id; contar "reparado"
   c. si el normal se recreó con id nuevo, la contraparte debe apuntar al id nuevo
4. variantes: para cada texto de pack.variantes que no esté en ESP, agregarlo.
   Las variantes que la pareja agregó por su cuenta no se tocan.
5. guardar con merge y devolver el resumen
```

Reglas:

- **Los personajes que la pareja agregó por su cuenta no se tocan** (no están en
  `packsInstalados`).
- Los personajes del pack que la pareja borró **vuelven con id nuevo**.
- Los que editó **vuelven al contenido del pack**, conservando el id.
- Las parejas se reparan siempre: la contraparte apunta al original actual.
- Reinstalar dos veces seguidas es seguro (idempotente).

---

## 7. Búsqueda de pareja por `par`

### 7.1 Índice

En `Roles/index.html`, construir una vez (al cargar y después de cada guardado) y usar en
todas las consultas:

```
porId  = Map<String(id) -> personaje>          // U1, U2, C1, C2
porPar = Map<String(par) -> [contrapartes]>    // SOLO C1 y C2
```

Usar `String(...)` en las claves: hay datos viejos con ids numéricos y textos pegados.

**Solo C1 y C2 alimentan `porPar`.** Un personaje de U1/U2 nunca es contraparte: si
trae `par`, es un dato viejo de alguna importación y se ignora. Si se indexara, cada
normal se contaría a sí mismo o a un personaje del mismo lado y saldrían parejas
ambiguas (nov-2026).

### 7.2 `contraparteDe`

Mantener la firma actual `(idOriginal, ladoOriginal, mismo)` para no tocar las llamadas
(1081, 3388), pero **ignorar `ladoOriginal` y `mismo`**:

```
hits = porPar.get(String(idOriginal)) || []
si hits.length === 1 -> devolver hits[0]
si hits.length > 1  -> null (ambiguo, como hoy)
si no hay hits:
   si idOriginal NO está en C1/C2 -> null      // el `par` de un normal no se sigue
   p = porId.get(String(idOriginal))
   si p && p.par != null -> devolver porId.get(String(p.par))   // dirección inversa
   si no -> null
```

Sin orden de listas y sin adivinar. Sirve para datos nuevos (cruzados) y viejos (mismo
lado).

### 7.3 `paresDisponibles`

No cambia: ya usa `contraparteDe`.

### 7.4 Caminos del mismo lado (A+A reales)

Los caminos de pareja usan la búsqueda por `par`. Con la instalación canónica, la
contraparte de `U1` está en `C2` y la de `U2` en `C1`. Por eso:

- `poolsEspejoMismo()`: el admin recibe `U<n>`; el resto, **las contrapartes de esas `U`
  por `par`** (no `C<n>`).
- `listaDeCabezaPara()`: la misma regla.
- `selPoolDe(cab)`: **no es un camino de pareja**: es la lista completa del mismo
  lado, `U<n> + C<n>`, igual que el engrane y la galería.
- `avisosCorrespondencia()`: comprobar con `contraparteDe`; avisar si un original no
  tiene exactamente una contraparte.

Las parejas verdaderas A+A o B+B siguen jugando **la mitad del pack que coincide con su
lado** (decisión de Fredy). No se hace ninguna instalación especial para ellas; solo se
respeta la búsqueda por `par`.

`dueloMismoLado` sigue existiendo, pero **solo decide el reparto de roles** (admin
originales, resto contrapartes), no la lista.

### 7.5 Invitado en Duelo

`agregarInvitado()` (2439-2446) debe usar el mismo reparto que `poolsDuelo()`:

```
esAdmin = cab.id === adminDe(estado.cabezas).id
recibeOriginal = dueloMismoLado ? esAdmin : (cab.lado === ladoDuelo)
pool = pares.map(par => recibeOriginal ? par.o : par.c)
```

Y `contraDeRonda()` (2397) igual: si `dueloMismoLado`, el "contra" es el otro rol
(`esAdmin ? par.c : par.o`); si no, como hoy.

### 7.6 Lo que NO se toca

- `ladoDeUsuario`, `ladoDeInvitado`, `ladoAnatomiaCfg`.
- El formato del personaje (no agregar `genero`).
- `guardarPersonajes()`: su `merge` ya conserva `packsInstalados`.
- Las reglas de Firebase.

---

## 8. Editor en Panel -> Extras

Archivo: `Panel/catalogo.html`.

### 8.1 Formulario

En la sección Extras (`secActual === "extras"`), agregar al formulario un selector
**Tipo**: `Normal` / `Pack de personajes`.

Si es "Pack de personajes":

- Se muestran los campos de siempre (`id`, `titulo`, `icono`, `desc`, `orden`, `activo`,
  `nuevo`).
- Aparece un `textarea` para `pares` en JSON y un botón **Plantilla** que pega un ejemplo.
- `ruta` se fuerza a `Roles` y `seccion` a `extras`.

### 8.2 Validación antes de guardar

Se bloquea el guardado (mensaje claro en español) si:

- El JSON no es válido.
- `pares` no es un arreglo, está vacío o tiene cantidad impar.
- Algún par no tiene `normal` y `contraparte` con `personaje` no vacío.
- En algún par, `genero` no es `"A"` o `"B"`, o los dos son iguales.
- La cantidad de pares con `normal.genero === "A"` no es igual a la de `"B"`, o alguna
  es 0.
- Alguna `imagen` empieza con `data:` (base64).

Los textos (`situacion`, `gancho`, `derechos`, `si_quieres`) se normalizan a `""` si
faltan; no bloquean.

### 8.3 Guardado

En el `data` del `setDoc` (334-344) agregar, solo para packs de personajes:

```js
data.tipo = "personajes";
data.oficial = true;
data.seccion = "extras";
data.ruta = "Roles";
data.pares = paresValidados;
if(variantes.length) data.variantes = variantes;
```

No cambiar el guardado de los ítems normales.

### 8.4 Importar / exportar

- **Exportar**: copia al portapapeles el JSON del pack (incluido `id` y `pares`).
- **Importar**: pega un JSON en el formulario y lo valida.

Mantenerlo dentro de la misma pantalla; no crear una vista nueva.

---

## 9. Tarjeta en Tienda -> Extras

Archivo: `Tienda/index.html` -> `tarjetaPack(p)` (266-306).

### 9.1 Estados

Para `p.tipo === "personajes"` con licencia válida:

- Si `packsInstalados[p.id]` existe -> estado **"✅ Instalado"** y botón
  **"Reinstalar personajes"**.
- Si no existe -> estado **"✅ Se agregó a tu menú"** (o "Listo para instalar al abrir
  Roles") y botón **"Instalar personajes"**.
- En ambos casos, el botón **"Abrir"** sigue llevando a `../Roles/`.

Sin licencia -> exactamente como hoy ("Pedir acceso").

### 9.2 Base de la pareja

Tienda hoy solo abre la taquilla. Para reinstalar necesita la base de la pareja:

```js
import { initializeApp } from ".../firebase-app.js";
import { getFirestore } from ".../firebase-firestore.js";
import { resolverFirebase } from "../config.js";
import firebaseConfigBase from "../firebase-config.js";

const appPareja = initializeApp(resolverFirebase(firebaseConfigBase), "pareja");
const dbPareja = getFirestore(appPareja);
```

(`appTaq()` ya usa un app con nombre propio, así que no chocan.)

Cargar `packsInstalados` **una sola vez** al iniciar la pantalla (un `getDoc` a
`personajesJuego/actual`) y guardarlo en una variable para todas las tarjetas. Si falla,
tratar como vacío.

### 9.3 Reinstalar

- Pedir confirmación con `confirmar()` (texto de 6.1).
- Llamar a `reinstalarPackPersonajes(dbPareja, p)`.
- Mostrar `aviso()` con el resumen.
- Repintar la tarjeta (o la lista).

---

## 10. Anatomía obligatoria al instalar

### 10.1 Asistente (`index.html`)

- `agregarFila()` (1016-1050): en las **dos primeras filas** agregar un `select` con
  `"" -> "Elige..."`, `"masculino"`, `"femenino"`.
- `wBtn3` (1058-1078): no dejar guardar si alguno de los dos primeros no eligió; incluir
  `anatomia` en el objeto del usuario (1065-1068).
- Las filas extra ("invitados" del asistente) quedan como hoy: sin anatomía. Se corrigen
  luego en Usuarios (ver 10.2).

### 10.2 Usuarios (`index.html`)

En el desplegable de anatomía (1556-1566):

- Agregar la opción vacía **"Elige..."**.
- Si `!u.anatomia`, dejarla seleccionada (hoy muestra el valor por defecto
  `u.anatomia || (u.admin ? "masculino" : "femenino")`, que engaña).
- Al cambiar, sigue guardando con `guardarAnatomiaUsuario()`.

No cambiar `ladoDeUsuario`: los datos viejos se siguen leyendo como antes.

### 10.3 Invitados

Sin cambios: eligen anatomía al registrarse y queda fija.

---

## 11. Documentación

- **Este documento** (`General/Packs-Personajes.md`): al terminar la implementación,
  quitar del encabezado la nota de **"pendiente de implementar"**. Su fila en
  `AGENTS.md` ya está puesta.
- `General/Modelo-Datos.md`: agregar `packsInstalados`, `par` y el esquema del pack.
- `General/Roles.md`: la búsqueda por `par`; qué hace `dueloMismoLado` ahora; los caminos
  del mismo lado.
- `General/Usuarios.md`: anatomía obligatoria al instalar y "Elige..." cuando falta.
- `GUIA.md`: **una línea** que apunte a este documento y **una línea** con la regla de
  anatomía al instalar. Va **al final**, cuando ya funcione: `GUIA.md` es lo que es
  cierto hoy y no puede anunciar algo que todavía no existe.
- `herramientas/sintaxis/extract.py`: agregar `packsPersonajes.js` a la lista de módulos
  (líneas 84-87).
- `General/Indices-Codigo.md`: se regenera; no se edita a mano.
- `README.md`: si los pasos de instalación describen el asistente, agregar que ahora
  pide la anatomía de los dos perfiles base.

No hace falta tocar `General/Modales.md` (no hay ventana nueva: se usan `confirmar()` y
`aviso()`), ni `General/Catalogo.md` (el aviso de "nuevo" sigue igual).

---

## 12. Pruebas

### 12.1 Siempre

```powershell
cd herramientas\sintaxis
python revisar.py
```

Sale `1` si algo falla. Se corre **una sola vez** por cambio.

### 12.2 En vivo (clase B, una sola sesión agrupada)

1. Panel -> Extras: crear un pack con 2 pares (uno con normal A y otro con normal B).
   Guardar.
2. Tienda -> Extras: pedir acceso. Aprobar y generar licencia como siempre.
3. Abrir Roles: debe salir el `aviso()` de instalación.
4. Revisar en el editor: el normal A en `U1`, su contraparte B en `C2`; el normal B en
   `U2`, su contraparte A en `C1`; cada contraparte con `par` igual al id de su original.
5. Jugar un Duelo y comprobar que la pareja aparece y se reparte.
6. Borrar una contraparte desde el editor.
7. Tienda -> Reinstalar personajes: debe volver con id nuevo, `par` correcto y la pareja
   jugable.
8. Con una pareja del mismo lado: en Duelo solo debe aparecer la mitad de su lado, y la
   pareja debe funcionar.

Si algo falla: máximo 3 intentos, se anota como pendiente y se sigue.

---

## 13. Orden de trabajo

1. `packsPersonajes.js` + instalación automática en Roles + `packsInstalados`.
2. Búsqueda por `par` y ajustes del mismo lado (7.2 a 7.5).
3. Reinstalación (módulo + botón en Tienda).
4. Editor en Panel -> Extras.
5. Anatomía obligatoria en el asistente y "Elige..." en Usuarios.
6. Documentación + `extract.py` + `revisar.py`.
7. Prueba en vivo agrupada.

Cada paso se cierra con `revisar.py` en verde antes de pasar al siguiente.

---

## 14. Trampas (no hacer)

- No guardar `pares` en la base de la pareja: solo los personajes instalados.
- No agregar `genero` al personaje instalado (el editor lo perdería).
- No enlazar por nombre.
- No deducir el lado por el admin ni por el orden.
- No tocar ni borrar las variantes creadas por la pareja.
- No borrar personajes al revocar una licencia.
- No crear una tarjeta de packs en el menú principal.
- No cambiar las reglas de Firebase.
- No usar `confirm()` ni `alert()`.
- No dejar botones visibles que deban nacer ocultos.
- No instalar para invitados.
- No reescribir el documento si no hubo cambios.

---

## 15. Checklist de cierre

- [x] `packsPersonajes.js` registrado en `extract.py`.
- [x] Instalación automática solo para perfiles base y con licencia.
- [x] `packsInstalados` con `normalId`/`contraparteId` por par.
- [x] Contrapartes cruzadas y `par` correcto.
- [x] `contraparteDe` busca por `par` en las cuatro listas.
- [x] Espejo, Seleccionar e invitado de Duelo usan la misma regla.
- [x] Reinstalación restaura, recrea y repara; no toca lo ajeno.
- [x] Editor con validación de pares y sin base64.
- [x] Tarjeta con "Instalado" y "Reinstalar personajes".
- [x] Asistente exige anatomía a los dos perfiles base.
- [x] Usuarios muestra "Elige..." cuando falta.
- [x] Documentación actualizada (`Modelo-Datos.md`, `Roles.md`, `Usuarios.md`,
      `GUIA.md`).
- [x] Encabezado de este documento sin la nota de "pendiente de implementar".
- [x] `python revisar.py` en verde.
- [ ] Prueba en vivo (12.2): pendiente, a cargo de Fredy.

---

## 16. Anexo - ejemplo mínimo de pack

```json
{
  "pares": [
    {
      "normal": {
        "personaje": "Bruno",
        "genero": "A",
        "situacion": "Jefe de oficina, recién llegado.",
        "gancho": "Te mira demasiado.",
        "derechos": "Puede pedirte quedarte después de hora.",
        "si_quieres": "Si aceptas, la reunión se alarga.",
        "imagen": "https://ejemplo.com/bruno.jpg"
      },
      "contraparte": {
        "personaje": "Bruna",
        "genero": "B",
        "situacion": "Asistente nueva, observa todo.",
        "gancho": "Sabe más de lo que dice.",
        "derechos": "Puede cerrar la puerta.",
        "si_quieres": "Si aceptas, se queda a solas contigo.",
        "imagen": ""
      }
    },
    {
      "normal": {
        "personaje": "Carla",
        "genero": "B",
        "situacion": "Clienta habitual.",
        "gancho": "Siempre pide lo mismo.",
        "derechos": "Puede cambiar la cita de hora.",
        "si_quieres": "Si aceptas, la cita se alarga.",
        "imagen": ""
      },
      "contraparte": {
        "personaje": "Carlos",
        "genero": "A",
        "situacion": "Recepcionista del turno noche.",
        "gancho": "Te conoce de antes.",
        "derechos": "Puede dejarte pasar.",
        "si_quieres": "Si aceptas, te acompaña.",
        "imagen": ""
      }
    }
  ],
  "variantes": ["Variante picante de ejemplo"]
}
```

Con este pack, la instalación deja:

- `U1`: Bruno - `C2`: Bruna (par de Bruno)
- `U2`: Carla - `C1`: Carlos (par de Carla)

Y `packsInstalados["<id>"]` guarda los cuatro ids en dos slots.

---

## 17. Precisiones obligatorias (leer antes de implementar)

### 17.1 Concurrencia

Los dos perfiles base pueden abrir Roles al mismo tiempo. La lectura y la escritura de
`personajesJuego/actual` en instalar y reinstalar deben ir dentro de `runTransaction`
(importarlo junto a `doc, getDoc, setDoc, serverTimestamp`) para no duplicar personajes.
Si la transacción falla por conflicto, reintentar una vez; si vuelve a fallar, no hacer
nada y reintentar en la próxima apertura. `oficialesAprobados()` se lee fuera de la
transacción (solo lectura).

### 17.2 Documento vacío o datos raros

- Si `personajesJuego/actual` no existe, tratarlo como `{}` y crearlo con
  `setDoc(..., { merge: true })`.
- Si `U1`, `U2`, `C1` o `C2` no son arreglos, usar `[]`. `ESP` igual, solo textos.
- `packsInstalados` solo se usa si es un objeto; si no, `{}`.
- Si un par del pack no tiene los dos personajes o los géneros no son opuestos, se salta
  y se informa; no rompe la instalación de los demás.

### 17.3 Pack modificado después de instalado

Los packs son inmutables (regla 4). Si aun así alguien edita uno ya instalado:

- Reinstalar solo los slots que están en `packsInstalados[packId].pares`.
- Si el pack ahora tiene más pares, los nuevos **no** se instalan solos; se instalan en
  la próxima instalación desde cero.
- Si tiene menos, los personajes de los pares sobrantes se quedan como están.
- Nunca borrar personajes por esto.

### 17.4 Editor: cargar, guardar y limpiar

- `pintarForm(f)` debe cargar `f.tipo` ("normal" por defecto) y, si es de personajes,
  `JSON.stringify(f.pares, null, 2)` en el textarea y `f.variantes`.
- `leerForm()` debe devolver `tipo`, `pares` ya parseado y `variantes`.
- Al guardar un ítem **Normal**, escribir también `tipo: "normal"`, `pares: []` y
  `variantes: []`, porque el `setDoc` usa `merge` y si no quedarían restos de una
  edición anterior.
- `variantes`, si viene, debe ser un arreglo de textos no vacíos; si no, error.
- Si `JSON.stringify(pares).length` pasa de 200 KB, avisar (sin bloquear) por el límite
  de 1 MiB y por las imágenes.

### 17.5 Imports que hay que agregar

- En `Roles/index.html`:
  `import { instalarPacksPersonajes } from "../packsPersonajes.js";`
- En `Tienda/index.html`:
  `import { reinstalarPackPersonajes, leerPacksInstalados } from "../packsPersonajes.js";`
- En Tienda, abrir la base de la pareja dentro de un `try/catch`. Si falla, la tarjeta se
  muestra como hoy ("Se agregó a tu menú" / "Pedir acceso") y sin botón de instalar o
  reinstalar.

### 17.6 Punto exacto de la instalación en Roles

`entrar()` ya hace `cargarPersonajes().then(...)` para el perfil base. La instalación va
dentro de ese `.then`, antes de `pintarInicio()`, y sin bloquear si falla:

```js
cargarPersonajes().then(async ()=>{
  try{
    const res = await instalarPacksPersonajes(db);
    if(res.instalados.length){
      await cargarPersonajes();
      pintarInicio();
      aviso("Se instalaron los personajes de: " + res.instalados.join(", "));
      return;
    }
  }catch(e){}
  try{ pintarInicio(); }catch(e){}
});
```

### 17.7 Pruebas que faltaban

- **Asistente**: en una base de prueba, comprobar que no deja guardar sin anatomía y que
  la guarda en los dos perfiles.
- **Segundo perfil**: abrir Roles con el otro perfil y comprobar que no se duplican
  personajes (idempotencia).
- **Tarjeta**: comprobar "Instalado" después de la instalación, el botón "Reinstalar
  personajes" y que "Abrir" lleva a Roles.
- **Revocar**: comprobar que los personajes instalados siguen ahí.

### 17.8 Trampa extra

- No borrar ni editar a mano `packsInstalados`: es el mapa que permite reinstalar sin
  adivinar. Si se pierde, el pack se puede volver a instalar, pero se duplicarían los
  personajes.

### 17.9 Índices

`General/Indices-Codigo.md` se regenera (no se edita a mano) cuando cambian
`Roles/index.html` y `Panel/catalogo.html`. Si el repo no trae la herramienta, se
actualiza solo lo que cambió en esos dos archivos, siguiendo el formato que ya tiene.

### 17.10 Checklist adicional

- [ ] Instalar y reinstalar dentro de `runTransaction`.
- [ ] Un `personajesJuego/actual` vacío o incompleto no rompe la instalación.
- [ ] El editor limpia `tipo`, `pares` y `variantes` al guardar un ítem normal.
- [ ] La tarjeta de Tienda no rompe si la base de la pareja no está configurada.
- [ ] Prueba con el segundo perfil: no se duplican personajes.

### 17.11 Últimos detalles

- **No hay migración de datos.** Los personajes y partidas que ya existen se leen como
  siempre. El único campo nuevo es `packsInstalados`, y solo lo escriben la instalación
  y la reinstalación.
- Después de instalar o reinstalar desde Tienda, actualizar el objeto en memoria
  `packsInstalados[p.id]` (o volver a leerlo) **antes** de repintar la tarjeta, para que
  el estado cambie a "Instalado" en el acto.
- El pack que llega a la tarjeta ya trae `pares` (viene del documento de `packs`); no hay
  que volver a leerlo para reinstalar.
- Si el usuario abre Tienda sin haber abierto Roles nunca, el botón "Instalar personajes"
  hace la instalación completa (la misma función, que detecta que el pack no está).

---

## 18. Cómo arrancar la implementación

Texto para pegar en el chat nuevo:

> Lee `AGENTS.md`, `General/GUIA.md` y `General/Packs-Personajes.md` completos.
> No toques el repo hasta que yo lo pida. Cuando lo pida, implementa en el orden de la
> sección 13 y cierra cada paso con `python revisar.py`.
> Si algo del documento no coincide con el código actual, pregúntame antes de inventar.
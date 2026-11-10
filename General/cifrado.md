# Cifrado de extremo a extremo (investigación)

> **Estado: investigación.** Nada de esto está decidido ni implementado, y **no se
> puede prometer al cliente todavía**. Es la base para seguir pensando y construir.
>
> **Cuándo arranca:** después de cerrar el **primer alcance** de la app. Hasta
> entonces, cualquier cosa de aquí puede moverse.
>
> **Regla 0:** este documento **no autoriza** a tocar el repo. Se empieza cuando
> Fredy lo pida expresamente.

Este archivo guarda **todo** lo que se habló del tema: lo que se quiere ofrecer, lo
que se puede y lo que no, los dilemas, las decisiones que faltan y **lo que ya se
descartó** (para no volver a proponerlo). Si algo aquí contradice a `GUIA.md` o a un
documento de detalle, manda el que describa lo que es cierto hoy.

---

## 1. Qué se quiere ofrecer

No nace de un miedo: es una **propuesta de valor**. La app guarda datos personales
muy íntimos y se quiere poder decir, de verdad, que **ni el desarrollador puede
leerlos**.

**Promesa candidata:**

> «Lo de la pareja está cifrado con una llave que solo está en sus teléfonos: ni yo
> ni Firebase podemos leerlo. Un invitado recibe solo la llave de la partida en la
> que está, y esa llave muere al terminar.»

**Letra chica que tiene que acompañarla** (si no, la promesa es falsa):

- Protege el **contenido**, no los **metadatos** (cuándo, cuánto, de qué tamaño).
- Las **fotos de personajes** son enlaces: el enlace va cifrado, la imagen vive
  fuera de la app.
- Un **teléfono desbloqueado** muestra lo que tenga abierto o cacheado.
- Si se pierden las dos llaves, **no hay rescate**.

**Por qué merece la pena:** hoy, con reglas abiertas y sin sesión, cualquiera que
tenga la configuración puede leer y escribir la base. El cifrado no cierra las
reglas, pero hace **ilegible el contenido**: es la única forma de que «yo no puedo
verlo» sea comprobable y no una promesa de palabra.

---

## 2. Qué protege y qué no

| Situación | ¿El cifrado lo evita? |
|---|---|
| Google / Firebase leyendo el contenido | **Sí** |
| Alguien con la configuración de Firebase pero sin la llave | **Sí** |
| Alguien que escanea el QR del invitado | **No**: la llave de la partida va en la invitación |
| Ver las fotos de personajes | **No**: son enlaces a imágenes públicas |
| Que alguien **borre o corrompa** datos | **No**: las reglas siguen abiertas; el cifrado es confidencialidad, no candado |
| El catálogo y las licencias (taquilla) | **No**: el menú los lee sin sesión |
| Saber que existió actividad y cuándo | **No**: los metadatos se ven |
| Un teléfono robado y desbloqueado | **No** |

---

## 3. Modelo de llaves

### 3.1 Llave de la pareja

- Cifra todo lo permanente: personajes, textos, lencería, fotos, ajustes, puntos.
- Vive **solo en los dos teléfonos**. No se guarda en Firebase, no se manda a
  ningún servidor.
- El segundo teléfono la recibe **una vez**, con un QR del primero.
- Respaldo: un QR (o un código impreso) que la pareja guarda fuera de la app.

### 3.2 Llave de la partida

- Se inventa al empezar cada partida y **no se deriva de la de la pareja**.
- Cifra **solo lo que el invitado necesita**: la copia de las cartas que ya viaja en
  la sesión (`sesionRoles/actual` y equivalentes).
- Viaja **en el QR / enlace**, en el **fragmento** (`#`), que el navegador **no
  manda al servidor** ni queda en registros.
- El invitado **nunca** recibe la llave de la pareja.
- Al terminar se borra del teléfono del invitado y **se elimina la copia cifrada**
  de la sesión. Así, aunque alguien se haya guardado la llave, **ya no abre nada**.

**Consecuencia buena:** no hay que cambiar la llave de la pareja después de cada
invitado.

### 3.3 Pérdida y respaldo

- Si se pierde un teléfono, el otro comparte la llave (QR).
- Si se pierden los dos, **el contenido se perdió**. Eso es la promesa; se dice al
  vender y se ofrece el respaldo impreso o el QR guardado.
- No hay «recuperar contraseña»: sería una puerta trasera y rompería la promesa.

### 3.4 Rotación

- **No** se rota la llave de la pareja por cada partida con invitados: la partida
  usa su propia llave.
- Sí haría falta rotar si algún día se comparte la llave de la pareja con alguien
  (por ejemplo, una pareja que se separa). Queda como caso extremo, no como flujo.

### 3.5 Teléfono sin llave

Falta decidir qué ve alguien que abre la app sin la llave (teléfono nuevo, datos
borrados, invitado sin partida). No mostrar contenido vacío como si no hubiera:
avisar que falta la llave y ofrecer recibirla por QR.

---

## 4. Cómo se guarda cada dato

### 4.1 El sobre

Cada dato guardado lleva **marca de versión** (cifrado o no, y con qué formato). No
es para los datos viejos: es para dentro de dos años, cuando cambie el formato de
cifrado, y para poder leer lo que quedó a medias.

### 4.2 Qué se cifra y qué queda en claro

- **Se cifra:** el contenido (textos, nombres, enlaces de fotos, mensajes).
- **Queda en claro:** lo que la base necesita para ordenar y filtrar: **ids,
  fechas, estados y autor**. Eso no revela lo íntimo, y sin eso la app no puede
  pedir nada.

### 4.3 Colecciones completas contra colecciones con consultas

- **Se leen completas** (`getDoc` de un documento): personajes, lencería, ajustes,
  sesiones de juego, propuestas de precios. Ahí se cifra todo el contenido.
- **Se consultan** (`where`, `orderBy`, `onSnapshot` filtrado): chat, retos, citas,
  presencia, invitaciones, puntos. Ahí se cifra **solo el contenido** y se dejan en
  claro los campos de filtro.
- El buscador de personajes filtra **en el teléfono**, así que no sufre.

### 4.4 Migración

- Con **bases nuevas** (lo previsto) no hay migración: se nace cifrado.
- Si algún día se cifra una base que ya tiene datos, hace falta leer en claro y
  cifrar, **sin borrar nada** hasta que lo nuevo esté probado.

### 4.5 El riesgo mayor

Un error de cifrado **no se ve: se pierde el dato**. Por eso:

- Marca de versión en cada dato.
- Nada se borra hasta probar.
- Pruebas en vivo, porque no hay arnés.

---

## 5. Fotos

### 5.1 Cómo están hoy las de lencería

Se comprimen en el teléfono, se guardan como **texto base64 dentro del documento**
de la prenda (`foto`, `fotoW`, `fotoH`). El límite de Firestore es **1 MiB por
documento**.

### 5.2 La corrección del peso

Se dijo al principio que cifradas pesarían un tercio más. **En este caso no es
cierto:** hoy ya se guarda base64, y al cifrar se guarda base64 del cifrado, que
mide casi lo mismo (solo suman unos bytes). **El cifrado no empeora el tamaño.**

### 5.3 El problema real: velocidad

Hoy la imagen es un enlace de datos listo para pintar. Cifrada hay que **descifrarla
y decodificarla** antes de verla. Con 80 o 100 prendas, eso se nota en el teléfono.

### 5.4 Miniaturas y descifrar al ver

- Una **miniatura cifrada** para la rejilla y la grande solo al abrir la prenda.
- **Descifrar cuando aparece en pantalla**, no todo al abrir.
- El tamaño de cada foto se decide igual que hoy (comprimir más o menos), porque el
  límite por documento ya existe y el cifrado no lo cambia.

### 5.5 Fotos de personajes

- Son **enlaces** (no se suben a la app). Cifrar el enlace protege **qué foto va con
  qué personaje y la dirección**; **no** protege la imagen.
- Meterlas dentro de la app **no** es opción: son muchos personajes y la gente cambia
  las de fábrica por las suyas; el peso se sale de control.
- Si algún día se quieren privadas, tienen que dejar de ser enlaces y guardarse
  **cifradas en el almacenamiento de la propia pareja**. Es un proyecto aparte y solo
  tendría sentido para fotos que ellos suban, no para las de fábrica (que son
  públicas por naturaleza).

---

## 6. Invitados y QR

### 6.1 La llave en el fragmento

La invitación ya lleva la configuración de la base. Ahora llevaría además la **llave
de la partida** en el fragmento del enlace (`#k=...`). El fragmento no viaja al
servidor: no queda en registros ni en documentos.

### 6.2 Ciclo de vida

- Al entrar, la llave vive **en memoria** y, si hace falta para recargar, en el
  almacenamiento del teléfono **solo mientras la partida esté activa**.
- Se borra al **terminar**, al **cerrar**, al **matar la app** y al **abrir sin
  partida activa** (antes de hacer cualquier otra cosa).
- **«Pausar y Salir» conserva** la llave, porque esa partida se retoma.

### 6.3 Qué se purga

Con la llave se borra **todo lo cacheado de esa partida**: cartas, textos, enlaces.
Si no, quedarían datos abiertos en el teléfono del invitado después de «borrar la
llave». La limpieza tiene que cubrir memoria, almacenamiento y cachés de la app.

### 6.4 Lo que no se puede garantizar

**No se puede demostrar** que la llave se borró en un aparato que no es tuyo: un
invitado técnico puede copiarla mientras juega, y lo que vio en pantalla lo puede
fotografiar. Por eso la promesa no es «no queda rastro», es:

> «Al terminar, la llave se borra y ya no abre nada: la copia cifrada de la partida
> se elimina.»

### 6.5 Invitado que vuelve por un enlace guardado

Sin la llave no puede abrir nada. Hoy el retorno del invitado se evalúa solo en el
inicio; con llaves, si vuelve por un enlace viejo, hay que mandarlo a escanear de
nuevo.

### 6.6 Chat con invitados

Pendiente de decidir: si el invitado participa en el chat, esos mensajes van con la
**llave de la partida** y desaparecen con ella; o el chat con invitados no existe.

---

## 7. Caché

### 7.1 Por qué no `localStorage`

- Guarda **texto**, no archivos (las imágenes irían en base64, un tercio más).
- Límite de unos **5 MB por sitio**: con 40 prendas ya se llena.
- Es **sincrónico**: bloquea la pantalla. Con megas ahí, la app se traba.

### 7.2 IndexedDB

- Guarda archivos tal cual, **sin bloquear** y con cientos de megas de margen.
- Es la pieza correcta para fotos y para cachear documentos.

### 7.3 Cifrado en disco, descifrado en memoria

- En el almacenamiento se guarda **el cifrado**; se descifra al pintar.
- En memoria se puede tener lo ya decodificado para que la rejilla no parpadee.
- Guardar **descifrado en disco** es más rápido, pero deja la foto abierta en el
  teléfono. No rompe la promesa (es el teléfono de la pareja, con su llave), pero hay
  que decirlo y no hacerlo nunca en el teléfono de un invitado.

### 7.4 Reglas de la caché

1. **La caché no es la verdad.** El navegador puede borrarla cuando quiera; siempre
   se puede volver a bajar de la base.
2. **Muere con la llave.** Si la llave se cambia o se borra, se borra lo cacheado con
   ella; en el invitado, todo lo de la partida.
3. **Nada de llaves de largo plazo en la caché.**
4. **La caché del invitado nunca guarda descifrado.**

### 7.5 Cuota y borrado del navegador

El navegador puede pedir permiso o vaciar el almacenamiento cuando se llena. Hay que
manejar el error de cuota y caer a la base, sin romper la pantalla. Cuánto aguanta
cada teléfono es una de las cosas que hay que **medir**, no suponer.

---

## 8. Avisos y comunicaciones

### 8.1 Push genérico

El aviso **no lleva información**: siempre el mismo texto («Tienes algo nuevo en la
app») y al tocarlo abre la app. Ahí se descifra con la llave que ya está en el
teléfono.

- **Nada** de nombres, categorías («nuevo reto», «mensaje») ni enlaces con
  identificadores.
- **El globito con número** también cuenta algo (cuántos); si se usa, es un dato más
  que se ve.

### 8.2 Lo que el servicio ve

- Que **hubo un aviso** y **cuándo**. Eso no se puede esconder.
- El **token del teléfono**. Se guarda **cifrado** en la base, como todo lo demás.

### 8.3 Quién lo manda

Una app estática **no puede despertar otro teléfono**. Alguien tiene que enviarlo:

| Opción | Qué implica | Qué ve el desarrollador |
|---|---|---|
| **Función en la nube** en el proyecto de cada pareja | Firebase cobra esa parte (plan de pago); hay que instalarla en cada proyecto | **Nada**, ni el momento |
| **Servidor propio pequeño** | Más simple de mantener para todos | **El momento**, nunca el contenido (hay que decirlo) |
| **App nativa (envoltorio)** | Avisos locales programados, sin terceros ni servidor; es otro proyecto, con tiendas | **Nada** |

### 8.4 iPhone

El push web solo funciona si la app está **instalada como aplicación** (Añadir a
inicio) y con iOS reciente. En Android funciona sin instalar.

### 8.5 Service worker

Tiene que ser **mínimo**: recibir el aviso y abrir la app. **No** guardar contenido en
caché (quedaría copia abierta o con llaves viejas).

### 8.6 Recordatorio de la mañana

Sobrevive **si es genérico** («Entra a la app»): el que lo programa no necesita la
llave de la pareja, solo la dirección del aviso. Si no hay push, el recordatorio se
queda solo dentro de la app y se pierde el aviso con el teléfono guardado.

### 8.7 Telegram se retira

- Un bot **no es cifrado de extremo a extremo**: lo que manda pasa por los servidores
  de Telegram y por la API del bot.
- Si el aviso lleva contenido íntimo, **rompe la promesa**. Con aviso genérico se
  podría conservar, pero la intención es retirarlo.
- Lo que hoy depende de Telegram (recordatorio, avisos entre la pareja) tiene que
  pasar al push genérico o quedarse dentro de la app.

### 8.8 Chat interno

El chat y la campana **sí se pueden cifrar**: mensajes con la llave de la pareja y,
en partida, con la de la partida. Es la parte fácil una vez que existen las llaves.

---

## 9. Lo que rompería la promesa

Lista de trampas que hay que cerrar **antes** de anunciar nada:

- **Telegram o WhatsApp con contenido** (y cualquier bot: ven el texto).
- **Exportar / Importar en claro**: lencería, listas y fotos de Roles. Ya está
  decidido quitarlos antes de vender; con cifrado, además, no pueden quedarse.
- **Caché en el teléfono del invitado** con contenido descifrado.
- **Service worker** guardando contenido.
- **API de IA** que reciba texto (hoy el Acompañante arma un texto para que la
  persona lo use aparte; si algún día se usa una API, se rompe).
- **Respaldos** sin cifrar.
- **Registros o telemetría** con contenido.
- **Metadatos**: no se pueden ocultar; solo se pueden aceptar y explicar.

---

## 10. Lo que no se puede prometer

- Que la llave se borre **demostrablemente** en un aparato ajeno.
- Ocultar **metadatos** (cuándo, cuánto, de qué tamaño).
- Que las **fotos por enlace** sean privadas.
- **Recuperar** el contenido si se pierden las dos llaves.
- Proteger un **teléfono robado y desbloqueado**.
- **Soporte mirando la base**: no se va a poder diagnosticar leyendo datos; todo se
  resuelve con lo que el cliente cuente.

---

## 11. Costo, riesgos y forma de trabajo

- **Es el proyecto más grande** que se le ha hecho a la app: no es una función, es la
  app reconstruida por dentro. **Meses**, en partes, no semanas.
- **Riesgo principal:** un camino que guarde o lea sin cifrar/descifrar. No se ve: se
  pierde el dato o se filtra sin avisar.
- **No hay arnés:** la verificación es en vivo, en el teléfono, como el resto de la
  app.
- **No se puede anunciar a mitad de camino:** mientras quede un hueco, la promesa es
  falsa.
- **Lista viva obligatoria:** qué colección y qué campo está cifrado y en qué
  pantalla se lee. Mientras esa lista tenga huecos, no se anuncia.
- **Soporte distinto:** sin poder mirar la base, el diagnóstico cambia; hay que
  preparar qué pedirle al cliente cuando algo falla.

---

## 12. Arranque (cuando toque)

1. **Cerrar el primer alcance** de la app. Esa es la condición.
2. **Repo nuevo** (fork, para poder unir después) y **bases de Firebase nuevas**,
   con **su propio Pages**. La app de hoy no se entera de nada.
3. Decidir que **el repo nuevo es el futuro**: los cambios y correcciones van allá.
   Mantener dos repos al día **no** funciona.
4. **Experimento fuera del repo** (uno o dos días, se borra al terminar) para medir
   cuatro cosas: peso/velocidad de las fotos, el paso de la llave entre dos
   teléfonos, el push en iPhone instalado y la cuota real de IndexedDB.
5. Con esos números, **escribir la promesa exacta** (la de arriba, corregida con
   datos).
6. **Módulo de llaves + sobre + una pantalla** (Lencería), que es donde está la duda
   de las fotos.
7. El resto, colección por colección, con la lista viva.

**Regla del experimento:** no se simula lo que solo se puede ver en dos teléfonos
reales; y nada de arneses queda en el repo.

---

## 13. Decisiones abiertas

- **Quién manda el push:** función en la nube por pareja (no ve nada, cuesta) o
  servidor propio (ve el momento, no el contenido).
- **Qué ve quien abre sin llave.**
- **Chat con invitados:** con llave de partida o no existe.
- **Recordatorio de la mañana:** genérico por push o solo dentro de la app.
- **Nombre y forma de las pantallas de llave:** crear, respaldar, recibir.

---

## 14. Descartado (para no volver a proponerlo)

- **`localStorage` para imágenes.** Límite chico, texto y sincrónico. Va IndexedDB.
- **Meter las fotos de personajes dentro de la app o del repo.** Muchos personajes,
  contenido personalizado y peso sin control; además el repo es público.
- **Guardar imágenes en base64 dentro de los packs.** Ya está prohibido por el
  límite de 1 MiB (`General/Packs-Personajes.md`).
- **Un bot de Telegram o WhatsApp con contenido.** Ven el texto; no es de extremo a
  extremo.
- **Rotar la llave de la pareja por cada invitado.** Innecesario con llave de
  partida.
- **Prometer «no queda ninguna huella».** No se puede demostrar en un aparato ajeno.
- **Un servidor central que vea el contenido.** Rompe la promesa.
- **Push con texto, categoría o globito con número.** Filtra información.
- **Cifrar los campos que ordenan y filtran** (fechas, estados, autor, ids). Rompe
  las consultas y no protege nada íntimo.
- **Cifrar la taquilla** (catálogo y licencias). El menú la lee sin sesión.
- **Mantener los dos repos al día a mano.** Se desincronizan; el nuevo es el futuro.
- **Empezar por las trece pantallas.** Primero llaves, sobre y una pantalla.
- **Prometer antes de medir.** La promesa se escribe con los números del experimento.
- **Caché con contenido descifrado en el teléfono de un invitado.** Se purga con la
  llave.
- **La app nativa como requisito.** Es una opción para los avisos, no un requisito
  del cifrado.
- **Decir «son semanas».** Es un proyecto de meses, en partes.

---

## 15. Lo que hay que contestar con medidas (no suponer)

| Pregunta | Cómo se contesta |
|---|---|
| ¿Cuánto tarda una rejilla de 100 prendas cifradas? | Prueba real en el teléfono |
| ¿Cuánto sube el peso al cifrar una foto de lencería? | Medir: no debería subir |
| ¿El paso de la llave entre dos teléfonos se siente seguro? | Prueba con dos teléfonos reales |
| ¿Llega el push con la app cerrada en iPhone instalado? | Prueba real |
| ¿Cuánto aguanta IndexedDB antes de que el navegador borre? | Medir en los teléfonos de la familia |
| ¿El borrado de la llave del invitado deja algo abierto? | Revisar almacenamiento tras terminar |

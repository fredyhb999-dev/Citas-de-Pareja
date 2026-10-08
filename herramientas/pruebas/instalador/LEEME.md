# Pruebas del instalador de fábrica (oct-2026)

Estas pruebas son para **una sola cosa**: comprobar que el instalador de
`config.js` funciona y que las 5 pantallas ahora muestran **tu base** y no la
fábrica del JSON.

## Por qué están aparte

El arnés de arriba (`final.py`, `run_raiz.py`, `run_sala.py`) usa un Firestore de
mentira que **no escribe**. El instalador justamente *escribe* en la base (para
copiar la fábrica una vez), así que ese arnés no puede probarlo.

Aquí se hace con una **base falsa en memoria**: se copian las pantallas **tal cual**
(con su DOM de verdad) y se les apunta a esa base. **Nada sale a internet y nada
toca tu Firebase de verdad.**

## Cómo correrlas

```
cd C:\Users\Fred\Documents\GitHub\Citas-de-Pareja\herramientas\pruebas\instalador
python correr.py
```

Sale algo como:

```
Comprobaciones: 47    con problema: 0
TODO OK
```

## Qué comprueba

**1) 22 casos sueltos** (`casos_instalador.html`) contra el `config.js` real:

| Grupo | Qué verifica |
|---|---|
| 1a-1e | Instalación nueva: siembra 3 actividades + 3 accesorios y deja la banderita |
| 2a | Que la segunda vez **no duplique** |
| 3a | Que **lo que borraste no reaparece** |
| 4a-4b | Que una actividad **nueva** del repo sí entra, pero la borrada sigue fuera |
| 5a-5c | Que respeta lo que ya tenías y **no pisa** tus documentos |
| 6a | Sin permiso: devuelve `false` y no se rompe |
| 7a-7e | `unirConFabrica()`: no duplica, ignora vacíos, no toca la base que recibe |
| 8a-8d | Datos raros (vacíos, nulos) |

**2) Las 5 pantallas reales** × 5 escenarios:

| Pantalla | Qué se mide |
|---|---|
| `Citas/actividades.html` | La lista pintada y si el botón dice Agregar/Eliminar |
| `Citas/accesorios.html` | Igual, y que tocar uno llene el campo |
| `Citas/index.html` | El `<select>` de actividades y los checkboxes de accesorios |
| `Guiadas/index.html` | La lista de actividades del juego |
| `Encuentros/index.html` | La lista de actividades del juego |

| Escenario | Qué significa | Lo esperado |
|---|---|---|
| `recien` | Base vacía, sin banderita | Siembra 3+3, y **todo editable** |
| `instalado` | Ya instalado | 3, **sin duplicar** |
| `borrada` | Borraste una de fábrica | **Solo 2: la borrada no vuelve** |
| `sin_permiso` | No se puede escribir | La base queda vacía pero **el JSON sigue sirviendo** de lista |
| `repetida` | Ya tenías una con ese nombre | **No la duplica**, solo agrega las que faltaban |

`sin_permiso` **no es un fallo**: es el camino de respaldo. Por eso ahí la
banderita queda en `false` a propósito.

## Archivos

| Archivo | Para qué |
|---|---|
| `correr.py` | El único comando. Prepara todo y corre todo |
| `casos_instalador.html` | Los 22 casos del instalador |
| `stub/firebase.js` | Suplanta al SDK para `config.js` |
| `stub/firebase-pantallas.js` | Suplanta al SDK para las pantallas |
| `stub/comunes.js` | Suplanta a `acceso.js`, `taquilla.js`, `invitado.js` |
| `stub/config.js` | `firebase-config.js` de mentira |
| `config_fabrica.js` | **Se genera en cada corrida**: copia del `config.js` real con el import del SDK cambiado |
| `pantallas/`, `trabajo/` | Se generan en cada corrida. Puedes borrarlos |

`config_fabrica.js` se rehace siempre a propósito: así las pruebas usan el
`config.js` que **hay ahora** en el repo, no una copia vieja.

## Nota importante

Este script **no cierra tu Chrome**. Cada Chrome headless se cierra solo al
terminar. (Hubo una versión que cerraba todos los Chrome con `taskkill`; ya se
quitó y no debe volver.)

## Lo que NO se prueba aquí

- Que los datos lleguen bien al Firebase **real**. Eso lo compruebas tú en tu
  celular: entra a *Personaliza tus Actividades*, escribe "Cena Romántica" y
  debe decir **Eliminar**.
- Las reglas de Firestore. No se tocan.
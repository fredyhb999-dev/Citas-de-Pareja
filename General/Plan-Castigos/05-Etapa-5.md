# Etapa 5 — Multi, Placer extremo y Sorpréndeme

> **Pega este archivo completo como instrucción.** Implementa **solo esta etapa**.
> Antes: lee `AGENTS.md`, `General/GUIA.md`, `General/Plan-Castigos.md`
> (secciones 2.1, 2.4–2.6, 6.1–6.2, 6.7–6.8) y este archivo.

## Objetivo

Agregar **Multi** (3 castigos), el **reparto en rueda**, **Placer extremo** y
**Sorpréndeme**. El resto del juego ya debe estar funcionando.

## Tareas exactas

### 1. Multi
- En la pantalla de inicio, **Multi** permite marcar **3 castigos** con casillas.
  Un castigo sin acciones no se puede marcar.
- Botón **“Combinar (3/3)”** (deshabilitado si no hay 3).
- Ventana **“¿Son estas 3?”** con **Continuar / Reelegir**.
- Al continuar: **paso de tomas** (precargado, editable).
- Las tomas de Multi son **de la partida**: **no** se guardan en los castigos.
- Se juega respetando esas tomas.

### 2. Reparto en rueda (regla oficial)
Por **nivel y lado**:
1. `necesarias = tomas[nivel] × jugadores de ese lado`.
2. Barajar las acciones de cada uno de los 3 castigos en ese nivel/lado.
3. Recorrer los castigos en orden barajado tomando **una acción de cada uno**
   por vuelta, saltando los que ya no tengan, hasta juntar `necesarias` o agotar
   todo.
4. **Barajar** lo seleccionado.
5. Si `necesarias` supera el pool, repetir (rebarajando).
6. Repartir entre los jugadores del lado **sin repetir**, `tomas[nivel]` a cada
   uno; procurar que cada uno lleve mezcla de los 3. Si no alcanza, repetir.
7. Cada jugador arma su lista por nivel (basico → alucinado), aleatorio dentro de
   cada nivel.

**Nota:** esta regla reemplaza el “mínimo” de Guiadas y el “proporcional” de
Encuentros. **No** cambies esos juegos aquí.

### 3. Placer extremo
- Interruptor en la pantalla de inicio (ya visible). Funciona en **cualquier
  modo**.
- Cuando está activo:
  - Se usan **todas** las acciones de `avanzado`, `experto` y `alucinado`.
  - `basico` y `medio` quedan en 0.
  - **Se salta el paso de tomas.**
  - En Multi, se aplica el **reparto en rueda** entre los 3 castigos.
  - Se barajan y se reparten **sin repetir** entre los jugadores del lado, en
    partes iguales; si no se puede dividir exacto, se repite para emparejar el
    largo.
  - Se conservan `accesorio` y `medida` de cada acción.

### 4. Sorpréndeme
- Solo en **Multi**.
- Elige **3 castigos al azar sin repetir**.
- Abre la ventana **“Son X, Y + Z”** con **Aceptar / Reelegir**.
- Aceptar sigue al paso de tomas; Reelegir vuelve a sortear.

## No hagas todavía
- No toques Guiadas/Encuentros (eso es Etapa 7).
- No implementes los oficiales/Panel (Etapa 6).

## Criterios de aceptación
1. Multi marca 3, confirma, pide tomas y juega.
2. El reparto en rueda usa el pool completo: el castigo con menos acciones
   aporta todas; no repite hasta agotar.
3. Con 3 jugadores y tomas 5, no se repite si el pool alcanza.
4. Las listas de los jugadores salen distintas.
5. Placer extremo usa solo los 3 niveles altos, salta tomas y baraja.
6. Placer extremo en Multi también hace reparto en rueda.
7. Sorpréndeme muestra 3 al azar y Aceptar/Reelegir funciona.
8. `python revisar.py` en `herramientas/sintaxis` sale **en verde**.

## Al terminar, reporta
- Archivos tocados.
- Qué probaste y qué no.
- Resultado de `revisar.py`.
- Dudas.
- **No empieces la Etapa 6.**

# Etapa 3 — Turno completo, medidas, imposiciones, Revivir, Saltar, fin

> **Pega este archivo completo como instrucción.** Implementa **solo esta etapa**.
> Antes: lee `AGENTS.md`, `General/GUIA.md`, `General/Plan-Castigos.md`
> (secciones 2.3–2.5, 3.2, 5.4–5.5, 6.4–6.5) y este archivo.

## Objetivo

Completar la partida **en un solo celular** (Solo/Pareja) con:
- pantalla del turno y medidas;
- imposiciones;
- Revivir;
- Saltar turno;
- pausa, terminar y fin con fuegos.

Todavía **sin** sesión compartida, invitados ni Multi (Etapas 4 y 5).

## Tareas exactas

### 1. Pantalla del turno
- El que castiga:
  1. “Turno de [nombre]”.
  2. Si el turno trae imposición: mostrarla + botón **“Aceptar”**.
  3. Al aceptar: mostrar el castigo (“acción con accesorio”) + su medida.
  4. **Libre / Veces:** botón **“Listo”**.
  5. **Tiempo:** botón **“Iniciar”** → cuenta regresiva en **minutos** + botón
     **“Listo”** siempre abajo. Al llegar a cero, **esperar** a que opriman
     “Listo”.
  6. “Listo” avanza el turno.
- En esta etapa no hay pantalla separada de receptor (es un solo celular). El
  receptor físico ve la pantalla; no agregues “te toca recibir” todavía.

### 2. Imposiciones
- Al iniciar: por lado, barajar `imposicionesCastigo/actual` en una bolsa en
  memoria.
- Al **jugar** un turno (no saltado): tomar la siguiente de la bolsa de ese lado
  y ponerla en `turnos[turno].imposicion`.
- Turnos saltados: **no** toman imposición.
- Si la bolsa se vacía: rebarajar; no repetir dentro de la misma ronda si se
  puede.
- Si el lado no tiene imposiciones: no mostrar el paso.
- La imposición se ve **antes** del castigo, con **“Aceptar”** para el que
  castiga.

### 3. Revivir
- Switch de **ancho completo debajo del recuadro del turno**, texto
  **“Revivir: apagado / encendido”** (teal cuando está prendido).
- **Solo el anfitrión** lo ve y lo puede tocar. En esta etapa (un celular) el
  anfitrión es quien inició la partida.
- Se prende/apaga **en cualquier momento**, **sin confirmación**, y aplica
  **desde el turno siguiente**. El turno en curso no cambia.
- Lógica:
  - `revivir = false`: los turnos con `lado !== ladoInicial` van `saltado: true`
    (pero la acción ya está consumida en `turnos`).
  - `revivir = true`: todos los turnos se juegan.
  - Al cambiar `revivir`, recalcular `saltado` **solo en turnos futuros**
    (`índice > turno` y `hecho === false`). No tocar los pasados.
- En **Solo puro** (sin invitados) ocultar el switch.

### 4. Saltar turno
- Botón **solo del anfitrión**, visible también en Solo.
- Marca el turno actual `saltado: true`, `hecho: true`, `imposicion: null` y
  avanza al siguiente. **Consume** el turno (la acción se pierde).
- Ubicalo en los controles del anfitrión, con un hueco reservado para que el
  layout no baile (como Encuentros).

### 5. Pausa, terminar y fin
- **Pausar y Salir** (anfitrión): overlay “En pausa”; el **cronómetro NO se
  detiene**.
- **Terminar Partida** (anfitrión): termina para todos y regresa a la lista.
- **Fin normal:** al acabar los turnos, “¡Gracias por jugar!” + **fuegos**
  (`fuegos.js`: `encenderFuegos()` / `apagarFuegos()`), y regreso a la lista.
- El **“‹ Volver”** se oculta durante la partida; solo se sale con
  Pausar/Terminar.

## No hagas todavía
- No implementes sesión compartida, invitados, “cada quien”, QR, Multi ni Placer
  extremo.
- No toques otros juegos.

## Criterios de aceptación
1. La imposición se muestra antes del castigo y solo avanza con “Aceptar”.
2. Libre/Veces usan “Listo”; Tiempo usa “Iniciar” + cuenta en minutos + “Listo”;
   al llegar a cero espera.
3. Revivir prende/apaga y cambia los turnos futuros; el actual no cambia.
4. Saltar turno consume el turno y avanza.
5. Pausa no detiene el cronómetro.
6. Al terminar salen los fuegos y “¡Gracias por jugar!”.
7. `python revisar.py` en `herramientas/sintaxis` sale **en verde**.

## Al terminar, reporta
- Archivos tocados.
- Qué probaste y qué no.
- Resultado de `revisar.py`.
- Dudas.
- **No empieces la Etapa 4.**

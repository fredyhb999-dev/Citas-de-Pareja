# Etapa 2 — Inicio y generación (normal, Solo/Pareja en un celular)

> **Pega este archivo completo como instrucción.** Implementa **solo esta etapa**.
> Antes: lee `AGENTS.md`, `General/GUIA.md`, `General/Plan-Castigos.md`
> (secciones 2.1–2.3, 3.2, 5.1, 6.1, 6.3) y este archivo.

## Objetivo

Que el juego ya se pueda **iniciar y jugar en un solo celular** con un castigo
(normal), en Solo o Pareja, respetando las tomas y el orden aleatorio. Todavía
**sin** medidas especiales, imposiciones, Revivir, invitados, Multi ni Placer
extremo (eso viene en las siguientes etapas).

## Tareas exactas

### 1. Pantalla de inicio (`vistaInicio`)
Con el molde A y el tema de la app:
- Título **“El Precio del Placer”** + lema.
- **Modo:** Solo / Pareja / Invitados.
- **¿Cómo juegan?** Un celular / Cada quien.
- **¿Quién castiga primero?** en Pareja e Invitados: A o B (nombres reales si se
  pueden leer; si no, “A”/“B”). En Solo no se pregunta (lado del usuario actual).
- **Normal / Multi.** En Multi, botón **Sorpréndeme**.
- Interruptor **Placer extremo por deseo**.
- Botón **Jugar**.
- **Engrane ⚙️** arriba a la izquierda (abre la configuración de la Etapa 1).
- Abajo: **QR**, **Agregar invitado** y cuadros de sala (visibles; su lógica
  completa es la Etapa 4).
- **En esta etapa:** Solo y Pareja con **“Un celular”** funcionan. “Cada quien”,
  Invitados, Multi y Placer extremo pueden verse, pero al elegirlos deben avisar
  **“En construcción”** y no romper nada.

### 2. Paso de tomas
- Al oprimir Jugar (normal), abrir el **paso de tomas**: 5 números (uno por
  nivel), **precargados** con `nivelesCastigo.tomas` y **editables**.
- Al aceptar, guardar los números en `nivelesCastigo.tomas` (merge) y usarlos en
  la partida.
- Rango permitido: 0 a 20 por nivel.

### 3. Generación de listas (normal)
Para cada **lado** y **nivel**:
1. Pool = las acciones de ese nivel/lado del castigo, **barajadas**.
2. Necesarias = `tomas[nivel] × jugadores de ese lado`.
3. Tomar del pool **sin repetir** hasta juntar lo necesario o agotarlo; si no
   alcanza, repetir (rebarajar).
4. Repartir entre los jugadores del lado **sin repetir**, `tomas[nivel]` a cada
   uno; si no alcanza, repetir.
5. Cada jugador arma su lista por nivel (basico → alucinado), con el orden
   aleatorio dentro de cada nivel.
6. Cada acción conserva `{ nivel, lado, texto, accesorio, medida }`.

### 4. Jugadores y orden
- `cabezas`: los usuarios de la app (admin y pareja). En Solo, solo el usuario
  actual. Cada uno con `{id, nombre, lado, admin, invitado:false, conQuien:null}`.
- `orden`: permutación **aleatoria** de todos los jugadores.
- `rondas`: largo de la lista (todas iguales).
- `turnos`: para ronda 1..R, para cada jugador en `orden`, una entrada
  `{ jugador, lado, ronda, accion, imposicion:null, saltado, hecho:false }`.
- `revivir = false` y `ladoInicial` = el elegido (Pareja) o el del usuario
  (Solo). `saltado = (lado !== ladoInicial)` en esta etapa (Revivir se
  implementa en la Etapa 3, pero deja el campo y la regla listos).

### 5. Partida local (básica)
- Guardar el estado en memoria (y en `localStorage` si quieres reanudar; no es
  obligatorio en esta etapa).
- Mostrar el turno actual: si es un turno **saltado**, avanzar solo hasta el
  siguiente **no saltado**.
- Pantalla simple del turno: “Turno de [nombre]” + la acción (con accesorio) +
  botón **Siguiente** que avanza.
- Al terminar todos los turnos: mensaje **“¡Gracias por jugar!”** y regreso a la
  lista (sin fuegos todavía; eso es Etapa 3).
- En esta etapa **no** hay: imposiciones, medidas en juego, Revivir, Saltar,
  pausa, receptor separado, invitados, Multi ni Placer extremo.

## No hagas todavía
- No implementes medidas en juego, imposiciones, Revivir, Saltar, pausa/fuegos,
  sesión compartida, invitados, Multi ni Placer extremo.
- No toques otros juegos.

## Criterios de aceptación
1. Solo y Pareja (un celular) inician una partida normal.
2. El paso de tomas aparece, precargado y editable; los cambios se guardan.
3. Las listas respetan las tomas (número correcto por nivel y lado).
4. El orden de jugadores es aleatorio.
5. Los turnos del lado no inicial se saltan (no se muestran).
6. La partida termina cuando se acaban los turnos.
7. `python revisar.py` en `herramientas/sintaxis` sale **en verde**.

## Al terminar, reporta
- Archivos tocados.
- Qué probaste y qué no.
- Resultado de `revisar.py`.
- Dudas.
- **No empieces la Etapa 3.**

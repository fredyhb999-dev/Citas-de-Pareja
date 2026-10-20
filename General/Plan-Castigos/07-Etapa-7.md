# Etapa 7 — Pendiente: reparto en rueda y tomas en Guiadas/Encuentros

> **Pega este archivo completo como instrucción.** Esta etapa va **después** de
> que el juego nuevo esté terminado y probado. **No mezclar** con las etapas 1–6.
> Antes: lee `AGENTS.md`, `General/GUIA.md` (sección “Otros pendientes” y
> MultiActividades) y este archivo.

## Objetivo

Llevar a **Guiadas** y **Encuentros** el criterio que ya usa el juego nuevo:
1. **Reparto en rueda** en Multi (reemplaza el “mínimo” de Guiadas y el
   “proporcional” de Encuentros).
2. **Flujo de tomas de Encuentros** en Guiadas normal (siempre pregunta,
   precargado y editable).

## Reglas

- Se hace **por etapas**: primero Guiadas, probar en vivo; después Encuentros,
  probar en vivo. No las dos de golpe.
- **No** cambiar pantallas, textos, sesiones ni nada más: solo el **generador de
  listas** y el **paso de tomas**.
- Si una etapa falla, se corrige ahí; no se sigue.
- No tocar `Roles/`, `Opciones/`, `Retos/` ni el juego nuevo.

## Tareas

### A. Guiadas — reparto en rueda
- Archivo: `Guiadas/index.html`, en el armado de Multi (`btnMulti3Ok` /
  generación de `listaJuego`).
- Hoy usa: por nivel/lado, `m = mín(acciones de las 3)`, toma `m` de cada una,
  revuelve y rellena repitiendo si hace falta.
- Cambiar a **reparto en rueda** (mismo criterio del plan nuevo, 6.2), adaptado a
  que Guiadas arma **una sola lista** (no una por jugador):
  1. `necesarias = tomas[nivel]` para ese lado.
  2. Bolsas = acciones de cada una de las 3 actividades en ese nivel/lado,
     barajadas.
  3. Tomar una de cada una por vuelta, saltando vacías, hasta `necesarias` o
     agotar.
  4. Barajar el pool.
  5. Si `necesarias` supera el pool, repetir.
  6. El resultado es la lista de ese lado (misma forma que hoy).
- **No** cambiar el orden de niveles ni el player.

### B. Guiadas — paso de tomas
- Hoy, al jugar una sola actividad usa las tomas guardadas **sin preguntar**.
- Cambiar a: al iniciar, abrir el **paso de tomas** (5 números), **precargado**
  con `nivelesActividad.tomas` y **editable**; al aceptar, guardar y usar.
- Debe quedar igual que Encuentros.
- No tocar el editor de Guiadas ni la sesión compartida.

### C. Encuentros — reparto en rueda
- Archivo: `Encuentros/index.html`, en `generarListas()`.
- Hoy junta **todas** las acciones de las actividades por nivel/lado
  (proporcional) y reparte.
- Cambiar el armado del pool a **reparto en rueda** (6.2):
  1. `necesarias = tomas[nivel] × jugadores del lado`.
  2. Bolsas por actividad, barajadas.
  3. Tomar una de cada una por vuelta, saltando vacías, hasta `necesarias` o
     agotar.
  4. Barajar.
  5. Si no alcanza, repetir.
  6. Repartir a los jugadores del lado **sin repetir**, como hoy.
- **No** cambiar los turnos, la sesión, el player ni los invitados.

## Pruebas (en vivo, celular)

### Guiadas
1. Multi con 3 actividades de 3, 15 y 8 acciones; tomas 5.
2. La de 3 **aporta sus 3**; no hay repetición hasta agotar.
3. Se respetan las tomas.
4. Normal: al iniciar aparece el paso de tomas, precargado y editable.

### Encuentros
1. Multi con 3 actividades desiguales y varios jugadores.
2. Cada jugador recibe su lista, sin repetir hasta agotar.
3. Ninguna actividad queda fuera.
4. Los turnos y la sesión siguen igual.

## Criterios de aceptación
- Los dos juegos siguen funcionando en normal, compartido y con invitados.
- `python revisar.py` en `herramientas/sintaxis` sale **en verde**.
- Se probó en el celular y se reportó qué se vio.

## Al terminar, reporta
- Archivos tocados.
- Pruebas hechas y resultado.
- `revisar.py`.
- Dudas.
- Actualizar `General/GUIA.md` (quitar el pendiente si quedó hecho).

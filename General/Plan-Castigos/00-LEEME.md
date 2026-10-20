# Prompts por etapa — “El Precio del Placer”

Este folder divide el plan (`General/Plan-Castigos.md`) en **un prompt por etapa**
para que un modelo, aunque sea gratuito, no tenga que tragarse todo junto.

## Orden (no saltar)

1. `01-Etapa-1.md` — Base y contenido (editor).
2. `02-Etapa-2.md` — Inicio y generación (normal, Solo/Pareja en un celular).
3. `03-Etapa-3.md` — Turno, medidas, imposiciones, Revivir, Saltar, fin.
4. `04-Etapa-4.md` — Compartido e invitados.
5. `05-Etapa-5.md` — Multi, Placer extremo, Sorpréndeme.
6. `06-Etapa-6.md` — Oficiales y Panel.
7. `07-Etapa-7.md` — Pendiente: Guiadas/Encuentros (va aparte, al final).
8. `08-Pruebas-En-Vivo.md` — Checklist para probar en celular (no es una etapa de código).

## Cómo usarlo

- **Una etapa por prompt/chat.** No pidas varias juntas.
- Pega el contenido del archivo de la etapa como instrucción.
- El modelo **debe leer** antes de escribir:
  - `AGENTS.md`
  - `General/GUIA.md`
  - `General/Plan-Castigos.md`
- Al terminar, debe correr:
  ```
  cd herramientas\sintaxis
  python revisar.py
  ```
- Tú pruebas en el celular. **No avances si la etapa no pasa.**
- Si el modelo se traba o no cumple, pídele que **corrija esa etapa**; no que siga.
- **No se hace commit.** Tú subes con GitHub Desktop.
- Si algo no está definido, el modelo **pregunta**; no inventa.

## Regla de oro

- El plan completo manda. Estos archivos solo dividen el trabajo.
- **No se tocan Guiadas/Encuentros** hasta la Etapa 7.
- **No se toca `App Pareja`** (la app real).
- Todo es en `Citas-de-Pareja`.

## Estado

**Implementado (oct-2026).** Falta **solo la prueba en vivo**: ver
`08-Pruebas-En-Vivo.md`.

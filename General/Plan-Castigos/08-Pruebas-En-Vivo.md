# Pruebas en vivo — “El Precio del Placer”

> **Estado:** el código del juego y sus pantallas están implementados. **Lo único
> que falta es la prueba real en celular.** Este archivo es el checklist para el
> colaborador: qué probar, qué debe pasar y qué NO es un bug.
>
> Antes de probar, subir con GitHub Desktop y esperar 1–2 min (Pages). Abrir en
> **Chrome directo**, no desde WhatsApp/Facebook/Instagram.

---

## 0. Preparación (datos, no código)

1. **Pack del juego en el Panel** (`Panel/catalogo.html`):
   - ID: `castigos`
   - Título: **El Precio del Placer**
   - Descripción: **Ganar cumple tus deseos; perder despierta la pasión.**
   - Ruta: **Castigos**
   - Sección: **juegos**
   - Icono y orden: a elección
   - Activo: sí
2. **Licencia `castigos` aprobada** para el teléfono de prueba (`Autorizar/`).
3. Opcional: crear **castigos oficiales** en `Panel/castigos.html` y aprobar sus
   `ofc_...`.
4. Tener a mano **dos celulares** con la misma base (para Pareja/Cada quien e
   invitados) y un tercer teléfono/ventana para invitado.

---

## 1. Licencia del juego

- Sin la licencia `castigos`, abrir `Castigos/` directo debe mostrar
  **“Sin acceso”** con botón **“Ir al Centro”**.
- Con la licencia aprobada, debe abrir la pantalla de inicio.
- Un **invitado** debe poder jugar con el acceso del anfitrión (no se le pide
  licencia propia).

---

## 1b. Inicio y configuración (UI)

1. La pantalla de inicio debe mostrar **primero el recuadro de castigos**
   (“Elige castigo” + buscador + lista con scroll) y **debajo** los ajustes:
   **¿Quién juega hoy?**, **¿Cómo juegan?**, **¿Quién castiga primero?**,
   **Modalidad** y **Placer extremo por deseo**.
2. El texto debe decir **Atrévete a Jugar ...** (tres puntos literales) y **no**
   debe verse la nota del QR.
3. Los botones deben decir **¿Quién juega hoy?** (no “Modo”) y **Modalidad**
   (no “Tipo”); donde antes decía A/B/Administrador/Pareja deben verse los
   **nombres** asignados (o **Usuario 1 / Usuario 2** si no hay nombres).
4. Tocar un castigo de la lista inicia la partida **con las condiciones que estén
   seleccionadas en ese momento**.
5. **Engrane (⚙️):** abre la configuración con el **mismo recuadro de castigos**
   arriba; tocar una fila abre el **editor** de ese castigo.
6. Pestaña **Accesorios:** el **catálogo de accesorios** debe verse en el **mismo
   recuadro con scroll** del inicio; no repite la lista de castigos.
7. Pestaña **Imposiciones:** las dos pestañas deben mostrar los **nombres** de los
   jugadores (o Usuario 1 / Usuario 2), no “A” y “B”.
8. **Multi:** al elegir Multi, el recuadro de castigos permite marcar hasta 3 y el
   botón **Combinar** se activa con 3.
9. **Editor de castigo:** al abrirlo deben verse las acciones **ya guardadas**;
   **💾 Guardar** guarda sin jugar; al **Volver a lista** también se guarda; el
   botón **Jugar** se activa cuando hay al menos una acción.
10. **Enter:** escribir una acción y dar **Enter** la agrega y deja el cursor en
    el **mismo campo**, listo para capturar la siguiente.

---

## 1c. Volver y botón atrás

- Los textos de **Volver** están **arriba a la derecha**, no dentro de la
  pantalla. En el **editor** guardan y regresan a Configuración; en
  **Configuración** y **Tomas** regresan al inicio.
- **Botón atrás del celular/navegador:** en Configuración/Editor/Tomas regresa
  al inicio; en la **partida activa no sale** (se queda en el juego).
- **Invitado:** entra directo a la **sala de espera** (no ve el inicio del
  anfitrión), no tiene “Volver” ni puede salir con el botón atrás mientras está
  en el juego o esperando. Al terminar, usa **Volver a lista**, que cierra el
  modo invitado y restaura su cuenta.

---

## 2. Solo

1. Crear un castigo con acciones en los 5 niveles, tomas por defecto
   (2/2/1/1/1).
2. Poner medidas distintas: una Libre, una Tiempo (minutos), una Veces.
3. Asignar un accesorio a una acción y dejar otra sin accesorio.
4. Iniciar en **Solo**.
5. **Tomas:** aparece el paso, precargado y editable; al aceptar se guarda.
6. **Duración:** deben jugarse **todas** las acciones (2+2+1+1+1 = 7), no solo 2.
7. **Receptor:** no debe haber pantalla de receptor (es el mismo jugador).
8. **Medidas:** Libre/Veces muestran “Listo”; Tiempo muestra “Iniciar” y luego
   cuenta regresiva + “Listo”; al llegar a 0 espera a “Listo”.
9. **Saltar turno:** visible y consume el turno.
10. **Revivir:** oculto en Solo puro.
11. **QR:** visible en el **inicio** y en la partida. **Agregar invitado:** en la partida.

---

## 3. Pareja, un celular

1. Modo **Pareja** → **Un celular** → elegir quién castiga primero (A/B).
2. Con Revivir **apagado**, solo juega el lado inicial; los turnos del otro lado
   se saltan (pero sus acciones se consumen).
3. Prender **Revivir** a media partida:
   - El turno en curso **no** cambia.
   - Desde el siguiente se juegan los dos lados.
   - Apagarlo vuelve a saltar el otro lado.
4. Verificar que no se rehace lo ya jugado y que las listas no se reinician.

---

## 4. Pareja, cada quien el suyo

1. Dos celulares con la misma base; modo **Pareja** → **Cada quien**.
2. Al iniciar, ambos deben ver la sesión.
3. **El que castiga:** ve “Turno de …”, imposición + **Aceptar**, luego el
   castigo + medida + **Listo**.
4. **El que recibe:** ve **“Te toca recibir”** + la imposición como contexto +
   **solo la acción** (sin medida ni cronómetro), y **sin botones**.
5. **Los demás** (si hay invitados): ven “Turno de …” + imposición, sin acción.
6. **Permisos:**
   - Aceptar/Listo solo los puede tocar el que castiga.
   - Revivir, Saltar, Pausar y Terminar solo el anfitrión.
7. **Avance:** “Listo” del que castiga avanza a todos.
8. **Rondas:** no debe regresar a la ronda 1 después de la primera vuelta.
9. **Pausa:** el cronómetro **sigue corriendo**; el invitado no puede reanudar.
10. **Fin:** “¡Gracias por jugar!” + fuegos; la sesión queda terminada.

---

## 5. Invitados

### 5.1 Registro por QR
1. En el celular del anfitrión: **inicio → QR** (también está en los controles de la partida).
2. El QR debe llevar la **configuración** (como Encuentros), no un enlace.
3. En el celular del invitado: app raíz → **⚙️ Invitados → Entrar modo invitado**
   → escanear el QR → poner **nombre** y **de quién es invitado**.
4. El invitado debe quedar registrado en la base del anfitrión y pasar a la
   **sala de espera** (`Diablitos`).

### 5.2 Agregar y entrar
1. El anfitrión inicia **Invitados** + **Cada quien**.
2. En **Agregar invitado** debe aparecer el invitado registrado (la lista se
   refresca al abrir).
3. Al agregarlo, su sala debe mostrar **“Entrar”** (se republica la invitación).
4. Al entrar, el invitado debe ver su turno y sus acciones.
5. Los **cuadros de sala** del anfitrión: “En la espera” y “En el juego”.
6. El invitado **no tiene salida** (no ve “Volver”); al terminar, “Volver a
   lista” lo saca del modo invitado y restaura su base.

### 5.3 Invitado a media partida
1. Empezar con un invitado; agregar a otro después.
2. Al nuevo se le copia la lista del compañero de su lado y juega **solo lo que
   falta**; no se rearma nada de los demás.
3. Verificar que su lado sale de **quien lo invitó** (`conQuien`).

### 5.4 Un celular con invitado
1. En **Un celular**, agregar un invitado: debe entrar al juego en el mismo
   teléfono (no necesita sesión).
2. Los turnos del invitado se intercalan en las rondas restantes.
3. Si queda de los dos lados, **Revivir** debe aparecer.

---

## 6. Multi

1. Elegir **Multi**, marcar **3 castigos**, **Combinar (3/3)**, confirmar
   (“¿Son estas 3?”), aceptar.
2. **Tomas** de la partida (no se guardan en los castigos).
3. **Reparto en rueda:** con 3 actividades de 3/15/8 acciones y tomas 5, la de 3
   debe aportar sus 3, sin repetir hasta agotar el pool.
4. Las listas de los jugadores deben salir distintas y parejas de largo.
5. **Sorpréndeme:** 3 al azar sin repetir; ventana con **Aceptar / Reelegir**.
6. **Multi + Cada quien:** debe crear sesión compartida, con receptor y turnos
   como en el punto 4.

---

## 7. Placer extremo

1. Activar **Placer extremo por deseo** en el inicio.
2. No debe aparecer el paso de tomas.
3. Deben usarse **todas** las acciones de `avanzado`, `experto` y `alucinado`
   (no 1 por nivel); `basico` y `medio` en 0.
4. En Multi debe aplicar el reparto en rueda entre los 3.

---

## 8. Castigos oficiales

1. En `Panel/castigos.html`, crear un `ofc_...` con acciones, medidas
   (Libre/Tiempo/Veces con resortéo) y tomas sugeridas. **Sin accesorios.**
2. **Exportar** e **Importar** el JSON (ida y vuelta).
3. Guardar; debe quedar en `packs` con `oficial:true`, `ruta:"Castigos"`,
   `seccion:"juegos"`.
4. En el Centro (Juegos) debe salir la tarjeta desde el inicio; pedir y aprobar.
5. Al aprobar, el juego lo copia a `nivelesCastigo` con 🏅 y **primero**.
6. Las **tomas sugeridas** se copian solo si la pareja no las cambió.
7. **No** debe traer accesorios; la pareja los asigna.
8. Si se borra la copia, vuelve a aparecer mientras siga aprobado (reset).

---

## 9. Guiadas y Encuentros (Etapa 7)

### Guiadas
1. Normal: al iniciar debe aparecer el **paso de tomas** (antes no preguntaba),
   precargado y editable.
2. Multi: con 3 actividades desiguales, el reparto en rueda debe hacer que la de
   menos acciones aporte todo lo que tiene; sin repetir hasta agotar.
3. Verificar que el juego, la sesión compartida y los invitados siguen igual.

### Encuentros
1. Multi con 3 actividades desiguales y varios jugadores: cada uno con su lista,
   sin repetir hasta agotar, sin dejar fuera a la de menos acciones.
2. Verificar turnos, sesión, invitados y pausa.

---

## 10. Qué NO es un bug (no reportar)

- En **Un celular**, el teléfono del invitado puede quedarse en la sala: el juego
  corre en el celular del anfitrión y el invitado está presente físicamente.
- Las **imposiciones** pueden repetirse dentro de una ronda si la lista es más
  corta que los turnos de esa ronda (es “mejor esfuerzo”).
- El **invitado no tiene salida** por diseño.
- El **pack `castigos` y las licencias** son datos que se crean en el Panel; si
  no existen, el juego no aparece o muestra “Sin acceso”.
- La pantalla de **inicio** muestra la lista de castigos, los ajustes y el QR;
  los cuadros de sala y “Agregar invitado” viven dentro de la partida (a
  propósito).
- Si no hay internet, el juego avisa y cae a local; no es un fallo.

---

## 11. Qué reportar

Para cada fallo, mandar:
1. **Dónde**: pantalla y paso (ej. “Pareja, cada quien → turno 3 → Listo”).
2. **Qué esperabas** y **qué pasó**.
3. **Celular(es)** y modo (Solo/Pareja/Invitados; un celular/cada quien;
   Normal/Multi; Placer extremo sí/no).
4. Si se puede, **captura** o el texto exacto.
5. Si el fallo se repite al recargar.

No hace falta reportar lo que sí funcionó, salvo que algo se vea raro.

---

## 12. JSON para cargar acciones rápido

Se pega en **Castigo → Pegar acciones (JSON)**. **Reemplaza todas** las acciones
de ese castigo. Forma recomendada, con los 5 niveles y los 2 lados:

```json
{
  "niveles": {
    "basico": {
      "A": [
        { "texto": "Decir algo picante al oído", "accesorio": null, "medida": { "tipo": "libre", "valor": 0 } }
      ],
      "B": [
        { "texto": "Quitarse una prenda", "accesorio": "Antifaz", "medida": { "tipo": "tiempo", "valor": 3 } }
      ]
    },
    "medio": { "A": [], "B": [] },
    "avanzado": { "A": [], "B": [] },
    "experto": { "A": [], "B": [] },
    "alucinado": { "A": [], "B": [] }
  }
}
```

- **Niveles:** `basico`, `medio`, `avanzado`, `experto`, `alucinado`.
- **Lados:** `A` (Usuario 1) y `B` (Usuario 2).
- **`texto`:** obligatorio, máximo **60** caracteres.
- **`accesorio`:** nombre exacto de un accesorio ya creado, o `null`.
- **`medida.tipo`:** `libre` (valor 0), `tiempo` (minutos) o `veces` (cantidad).
- También se aceptan **textos sueltos**; quedan sin accesorio y en Libre:

```json
{
  "basico": { "A": ["Acción 1", "Acción 2"], "B": ["Acción 3"] },
  "medio": { "A": [], "B": [] },
  "avanzado": { "A": [], "B": [] },
  "experto": { "A": [], "B": [] },
  "alucinado": { "A": [], "B": [] }
}
```

- Un arreglo por nivel (`"basico": ["..."]`) se copia a **A y B**.
- Los niveles/lados que falten quedan vacíos. Evita acciones repetidas: el
  importador no las valida.

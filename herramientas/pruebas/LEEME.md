# Pruebas automáticas (arnés)

Estas pruebas abren un Chrome de verdad contra una **base de datos simulada**, así
que no tocan Firebase ni los datos reales. Sirven para comprobar cambios rápido,
sin subir nada.

**Requisito:** tener Google Chrome instalado en
`C:\Program Files\Google\Chrome\Application\chrome.exe`.

## El orden importa

Cada prueba tiene tres pasos: **construir → inyectar → correr**. Si se inyecta
dos veces sin reconstruir, el arnés queda corrupto y salen "fallas" que no son
del código real. Siempre en este orden.

## Instalador de fábrica (ot-2026) — un solo comando

```powershell
cd herramientas\pruebas\instalador
python correr.py
```

47 comprobaciones: 22 casos de la lógica de `config.js` y 5 escenarios sobre
**las 5 pantallas reales**. Es el arnés de arriba **no puede** probar esto, porque
su base simulada no escribe y el instalador justamente escribe.

Ver `instalador\LEEME.md` para el detalle.

## Diagnóstico de la Sala (`nada`)

```powershell
cd herramientas\pruebas
python diagnostico_sala.py
```

El escenario `nada` de la Sala **no funciona desde antes** de los cambios del
instalador, y **no es un error de la app**: el escenario pica "Regresar", que
lleva a la página de inicio, y el arnés de Sala no copia esa página. Este script
lo explica y dice cómo confirmarlo con el código viejo.

## Encuentros (13 casos)

```powershell
cd herramientas\pruebas
python build_harness.py
python inject_driver.py
python final.py
```

Cubre: niveles, invitación, entrada directa, anfitrión, botón saltar, fin de
partida, invitado (4 variantes), fantasma, multi, partida vieja, sin licencia.

## Inicio (4 casos)

```powershell
python build_raiz.py
python inject_raiz.py
python run_raiz.py menu
```

Escenarios: `nada`, `flujo`, `registro`, `medio`, `visitando`, `menu`.

## Sala de espera (7 casos)

```powershell
python build_sala.py
python inject_sala.py
python run_sala.py invitado
```

Escenarios: `nada`, `invitado`, `coninvitacion`, `pausada`, `sesionmuerta`,
`aviejada`, `expulsado`.

## Revisar sintaxis (rápido, sin navegador)

```powershell
python extract.py
python jscheck.py <archivo.js>
```

`extract.py` saca los `<script>` de los HTML a la carpeta `extracted` de la
carpeta temporal. `jscheck.py` revueba llaves, paréntesis y corchetes,
ignorando textos, comentarios y **expresiones regulares**.

Si `jscheck.py` marca algo, **antes de culpar al código** revisa si es una
expresión regular: `/(\w+)\s*:\s*"([^"]+)"/g` tiene llaves y corchetes dentro y
no son un error. El navegador real es la autoridad.

## Falsa alarma conocida

El caso `invitado&flag=fin&respaldo=1` **termina en otra página**, y esa página
no imprime la línea `errores js: ninguno`. Sale como problema, pero no lo es.
El reporte (`FINAL.txt`) queda en la carpeta temporal.

## Otras cosas que conviene saber

- **Un driver que se cae ahora SÍ cuenta como problema.** Antes pasaba
  desapercibido y el reporte salía "0 problemas" sin haber probado nada.
- Hay escenarios llamados `invitado` que en realidad juegan como **la pareja**
  (`&como=u2`). Para distinguirlos: `u3` es el invitado de verdad, `u2` la
  pareja, `u1` el anfitrión. Las comprobaciones leen la bandera `invitado` de
  la identidad, no el nombre del escenario.
- Los archivos pesados (copia de la app para probar, perfiles de Chrome, el
  reporte) se generan en la carpeta temporal del sistema, **no** en este repo.
  Por eso esta carpeta solo tiene los 13 scripts.

## OJO: los scripts viven SOLO en el repo

Hubo una copia de estos scripts en la carpeta temporal del sistema
(`C:\Users\Fred\AppData\Local\Temp\opencode\`) y ya se **borró**. Con dos
copias pasó esto: se parché la de la temporal, se corrió la del repo, y la
comprobación nueva nunca se ejecutó. Parecía que las pruebas no miraban.

**Regla:** todo parche va en `herramientas/pruebas/` y las pruebas se corren
desde ahí. La carpeta temporal solo guarda lo **generado** (las copias para
probar, los perfiles de Chrome, los reportes), y eso se puede borrar sin
consecuencia.

## Nada de esto sube a internet

El arnés usa una base simulada y un Chrome con perfil temporal. **No toca
Firebase ni la app en línea.** Lo único que se prueba de verdad es el código
local.
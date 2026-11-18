# Índices de código — los archivos grandes

**Para qué existe:** para no leer un archivo de 950 a 4,500 líneas cuando solo se
busca una función. Aquí se encuentra la zona y el nombre, y se va directo a la línea.

**Cómo se usa:**

1. Busca el archivo y la zona, o el nombre de la función (Ctrl+F).
2. **Los números de línea son de nov-2026.** Si el archivo cambió, busca por nombre: el
   nombre cambia menos que la línea.
3. Al final está el **anexo con todas las funciones** de cada archivo, en orden
   alfabético, para buscar rápido con Ctrl+F.

**Este archivo es solo un mapa.** No explica reglas ni decisiones: eso está en
`GUIA.md` y en el documento de detalle de cada pantalla.

**Se regenera con `python indice.py`** (`herramientas/sintaxis/`). No se edita a mano.

---

## `Roles/index.html` — 5,360 líneas

**Documento de detalle:** `General/Roles.md`

**Vistas:** `vistaBloqueo` (380) · `vistaInicio` (392) · `vistaSeleccion` (457) ·
`vistaEspera` (490) · `vistaPlayer` (497) · `vistaConfig` (584) · `vistaSeguir` (674)

| Para... | Función | Línea |
|---|---|---|
| Arrancar la página: identidad, licencia y estado guardado | `entrar()` | 1379 |
| Cambiar de vista y guardar el paso del historial | `ver()` | 5194 |
| Volver al menú deshaciendo los pasos | `salirAlMenu()` | 5224 |
| Pintar la tarjeta de inicio (modo y "Jugar") | `pintarInicio()` | 1555 |
| Pantalla de modo (Clásico, Cambia de Bando, Seleccionar, Duelo) | `pintarModo()` | 1565 |
| Modal del duelo | `pintarModalDuelo()` / `abrirModalDuelo()` | 1607 / 1623 |
| Quiénes juegan y de qué lado | `construirCabezas()` | 1031 |
| Pool de personajes: cargar, sembrar, guardar | `cargarPersonajes()` / `asegurarPersonajes()` / `guardarPersonajes()` | 1171 / 1190 / 1194 |
| Buscar personaje o su contraparte | `buscarPersonaje()` / `contraparteDe()` | 1247 / 1273 |
| Repartir tarjetas y preparar la partida | `repartirTarjetas()` / `preparar()` / `prepararDuelo()` | 3017 / 3046 / 3077 |
| Arrancar la partida normal | `iniciar()` | 3104 |
| Modo Seleccionar: pintar, abrir y arrancar | `pintarSeleccion()` / `abrirSeleccionLocal()` / `abrirSeleccionCompartida()` / `arrancarSeleccion()` | 3555 / 3675 / 3690 / 3731 |
| Escuchar la selección compartida | `escucharSeleccion()` | 3778 |
| Sala de espera (anfitrión e invitado) | `pintarSala()` | 2017 |
| Pintar la partida: tarjeta, paso, duelo | `pintarTarjeta()` / `pintarPaso()` / `pintarCaraDuelo()` / `pintarPasoDueloJuntos()` | 2178 / 2402 / 2225 / 2326 |
| Pasar turno o saltarlo | `siguienteTurno()` / `avanzarTarjeta()` / `siguienteSesion()` / `saltarTurno()` | 1353 / 1368 / 1886 / 1913 |
| Terminar la partida | `abrirFin()` / `finPartida()` | 2497 / 2504 |
| Sesión multijugador | `escucharSesion()` | 1831 |
| Configuración: pintar, abrir, filas y editor | `pintarCfg()` / `abrirCfg()` / `filaPersonaje()` / `agregarPersonaje()` | 4412 / 5174 / 4388 / 4310 |
| Exportar la lista de personajes | `exportarLista()` | 4877 |
| Invitado: entrar, continuar, salir | `entrarAlJuego()` / `continuarPartida()` / `salirModoInvitado()` | 4029 / 3971 / 4094 |
| QR de invitación | `abrirQR()` | 2949 |
| Modales chicos | `abrirModal()` / `cerrarModal()` | 4123 / 4140 |

---

## `Castigos/index.html` — 4,407 líneas

**Documento de detalle:** `General/Castigos.md`

**Vistas:** `vistaInicio` (249) · `vistaBloqueo` (307) · `vistaTomas` (314) ·
`vistaPartida` (335) · `vistaEspera` (408) · `vistaConfig` (494) · `vistaEditar` (537)

| Para... | Función | Línea |
|---|---|---|
| Cargar todo: identidad, castigos, accesorios, imposiciones, usuarios | `cargarTodo()` | 780 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 1063 / 1152 |
| Panel de configuración | `mostrarPanel()` | 1264 |
| Lista y edición de castigos | `pintarCastigos()` / `abrirEditor()` / `pintarEditor()` / `guardarCastigoDatos()` | 1282 / 1365 / 1414 / 1617 |
| Tomas de cada castigo | `pintarTomas()` | 1519 |
| Accesorios e imposiciones | `pintarAccesorios()` / `pintarImposiciones()` | 1761 / 1884 |
| Pantalla de inicio y castigo elegido | `pintarListaInicio()` / `seleccionarCastigo()` / `actualizarInicio()` | 1988 / 2255 / 2319 |
| Pasos antes de jugar: quién castiga, modo, multi, imposiciones, placer | `preguntarQuienCastiga()` / `elegirModo()` / `toggleMulti()` / `preguntarImposicionesPor3()` / `preguntarNivelesPlacer()` | 2348 / 2359 / 2412 / 2507 / 2567 |
| Armar y arrancar: normal y multi | `armarPartidaNormal()` / `iniciarPartida()` / `iniciarPartidaMulti()` | 2634 / 3164 / 2895 |
| Repartir turnos y rueda | `repartirRueda()` / `generarTurnos()` / `generarTurnosMulti()` | 2958 / 2802 / 3003 |
| Pintar turno, sala y fin | `pintarTurno()` / `pintarSala()` / `mostrarFin()` | 3546 / 3429 / 3475 |
| Pausa: pausar, continuar, descartar | `pausarPartida()` / `continuarPausa()` / `descartarPausa()` | 2129 / 2214 / 2201 |
| Sesión compartida: publicar y escuchar | `publicarSesion()` / `escucharSesionCompartida()` | 3204 / 3288 |
| Turnos remotos y saltar turno remoto | `avanzarTurnoRemoto()` / `saltarTurnoRemoto()` / `escribirImposicionRemoto()` | 3697 / 3760 / 3678 |
| Cronómetro | `pintarCrono()` / `iniciarTemporizadorDesde()` | 3121 / 3127 |
| Invitados: QR y agregar a la partida | `abrirQRJuego()` / `agregarInvitadoAPartida()` | 3974 / 4212 |
| Importar acciones | `parsearImportacion()` / `normalizarAccionImport()` | 1683 / 1719 |

---

## `index.html` — 2,934 líneas (pantalla inicial)

**Documento de detalle:** `General/Pantallas.md` y `General/Usuarios.md`

**Vistas:** `vistaMenu` (451) · `vistaJuegos` (490) · `vistaRetos` (496) ·
`vistaCom` (502) · `vistaExp` (523)

| Para... | Función | Línea |
|---|---|---|
| Mostrar el menú y sus dos botones de esquina | `mostrarMenu()` / `verMenu()` | 666 / 1388 |
| Dibujar las tarjetas del catálogo | `tarjetaPack()` / `renderPacks()` / `renderPacksDeVerdad()` | 764 / 800 / 825 |
| Punto del carrito | `actualizarPuntoCarrito()` | 938 |
| Submenús: hash, abrir y cerrar | `hashActual()` / `abrirSegunHash()` / `abrirSub()` / `cerrarSub()` | 1408 / 1412 / 1420 / 1430 |
| Cada submenú | `abrirExp()` / `abrirJuegos()` / `abrirRetos()` / `abrirCom()` | 1437 / 1454 / 1465 / 1487 |
| Engrane: abrir, cerrar, cambiar usuario | `mostrarGear()` / `cerrarGear()` / `abrirCambiarUsu()` | 2538 / 2550 / 2558 |
| Telegram | `pintarTelegram()` | 2626 |
| Usuarios: anatomía y lista | `pintarInvUsuarios()` / `guardarAnatomiaUsuario()` / `abrirEdUsuarios()` | 1551 / 1526 / 2309 |
| Puntos e historial de movimientos | `abrirPuntos()` / `abrirHistorial()` | 1656 / 1693 |
| Propuestas de precios: pintar, abrir, aceptar, rechazar | `pintarPropuestas()` / `abrirPropuestas()` / `aceptarPropuesta()` / `rechazarPropuesta()` | 2013 / 2086 / 2121 / 2173 |
| Invitado: volver solo y escanear QR | `volverSiInvitadoSinPartida()` / `iniciarScan()` | 1206 / 1341 |

---

## `Lenceria/index.html` — 2,821 líneas

**Documento de detalle:** `General/Catalogo-Lenceria.md`

**Vistas:** `vistaPlanes` (204) · `vistaElegir` (218) · `vistaPedido` (241) ·
`vistaConfig` (258) · `vistaClasif` (279) · `vistaPrenda` (296)

| Para... | Función | Línea |
|---|---|---|
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 385 / 410 |
| Cargar todo y escuchar cambios | `cargarTodo()` / `escuchar()` | 2712 / 2423 |
| Cargar prendas, planes y pedidos | `cargarPrendas()` / `cargarPlanes()` / `cargarPedidos()` | 2394 / 2401 / 2408 |
| Configuración: clasificaciones y prendas | `pintarConfig()` / `bloqueClasif()` / `bloquePrendas()` | 1007 / 1025 / 1191 |
| Clasificación: abrir, pintar, guardar, borrar | `abrirClasif()` / `pintarClasifVista()` / `guardarClasif()` / `borrarClasif()` | 1103 / 1111 / 1136 / 1160 |
| Prenda: tarjeta, abrir, guardar, borrar | `tarjetaPrenda()` / `abrirPrenda()` / `guardarPrenda()` / `borrarPrenda()` | 1245 / 1332 / 1509 / 1568 |
| Fotos: elegir archivo, procesar, lupa | `usarArchivoFoto()` / `procesarFoto()` / `abrirLupa()` | 1473 / 1430 / 1307 |
| Planes: pintar, tarjeta y separador | `pintarPlanes()` / `tarjetaPlan()` / `separadorPlanes()` | 1664 / 1748 / 1649 |
| Orden de la cuadrícula (nunca usadas y referencia) | `ordenPrendas()` / `ordenRef()` / `compararRef()` / `claveRef()` | 851 / 846 / 837 / 831 |
| Referencias: la siguiente libre y corregir vacías o repetidas | `siguienteRef()` / `asegurarRefs()` | 870 / 900 |
| Texto de uso en la tarjeta | `textoUso()` / `diasDesdeUso()` | 816 / 807 |
| Vestidor: elegir y contar | `abrirElegir()` / `pintarVestidor()` / `alternarSeleccion()` / `pintarContador()` | 1942 / 1976 / 1995 / 2041 |
| Guardar plan, fijarlo o borrarlo | `guardarPlan()` / `alternarFijo()` / `borrarPlan()` | 2054 / 2108 / 2117 |
| "Sorpréndeme" | `sorprendeme()` | 2320 |
| Pedidos: proponer, abrir, aceptar, rechazar, cancelar | `mandarPropuesta()` / `abrirPedido()` / `aceptarPedido()` / `rechazarPedido()` / `cancelarPedido()` | 2133 / 2179 / 2220 / 2282 / 2307 |
| Contador de usos | `liquidarUsos()` | 2360 |
| Exportar / importar prendas | `abrirDatos()` / `aplicarImportacion()` | 2478 / 2543 |
| Entrar desde una cita | `aplicarEntradaCita()` | 2726 |

---

## `Encuentros/index.html` — 2,548 líneas

**Documento de detalle:** `General/Pantallas.md` y `General/Pegamento-y-Citas.md`

**Vistas:** `vistaBloqueo` (152) · `vistaLista` (164) · `vistaConfig` (189) ·
`vistaEditar` (197) · `vistaEspera` (210) · `vistaPlayer` (217) · `vistaSeguir` (258)

| Para... | Función | Línea |
|---|---|---|
| Arrancar: normal o directo al juego | `entrar()` / `entrarDirecto()` | 700 / 599 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 1002 / 1038 |
| Cargar actividades y pintar la lista | `cargarActividades()` / `pintarLista()` / `dibujarLista()` / `filtrar()` | 1233 / 1392 / 1337 / 1407 |
| Configuración y editor de actividades | `pintarListaCfg()` / `abrirEditor()` / `pintarEditor()` / `guardarEditor()` | 1543 / 1577 / 1595 / 1666 |
| Tomas de una actividad (modal y base) | `abrirTomas()` / `guardarTomasEnBase()` / `cargarTomasDoc()` | 1769 / 1534 / 1501 |
| Armar jugadores y repartir | `construirCabezas()` / `generarListas()` / `repartirRuedaEnc()` / `generarYIniciar()` | 1821 / 1832 / 1867 / 1905 |
| Pintar turno y paso | `pintarTurnoDe()` / `pintarPaso()` | 2070 / 2084 |
| Avanzar local o por sesión | `avanzarLocal()` / `avanzarSesion()` | 847 / 870 |
| Sala de espera | `pintarSala()` | 2019 |
| Invitados: agregar y QR | `agregarInvitado()` / `abrirQRInvitacion()` | 2290 / 2361 |
| Sesión: escuchar, saltar turno, cerrar, fin | `escucharSesion()` / `saltarTurno()` / `cerrarSesion()` / `mostrarFin()` | 775 / 900 / 965 / 995 |
| Entrar al juego siendo invitado | `entrarAlJuego()` | 2473 |

---

## `Guiadas/index.html` — 2,270 líneas

**Documento de detalle:** `General/Pantallas.md` y `General/Pegamento-y-Citas.md`

**Vistas:** `vistaBloqueo` (117) · `vistaLista` (129) · `vistaConfig` (154) ·
`vistaEditar` (162) · `vistaPlayer` (183) · `vistaSeguir` (197)

| Para... | Función | Línea |
|---|---|---|
| Arrancar la página | `entrar()` | 361 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 700 / 734 |
| Cargar actividades y pintar la lista | `cargarActividades()` / `pintarLista()` / `filtrar()` | 964 / 1149 / 838 |
| Jugar directo desde la lista | `jugarDirecto()` | 1164 |
| Arrancar partida y pintar el paso | `empezarNuevo()` / `mostrarPlayer()` / `pintarPaso()` / `pintarTurnoDe()` | 1350 / 1371 / 2077 / 2068 |
| Sesión: avanzar, escuchar, saltar, cerrar, fin | `avanzarSesion()` / `escucharSesion()` / `saltarTurno()` / `cerrarSesion()` / `mostrarFin()` | 553 / 658 / 624 / 606 / 479 |
| Multi: abrir, refrescar, seleccionar, repartir | `multiAbrir()` / `multiRefrescar()` / `multiAbrirSel()` / `repartirRuedaGuia()` | 1517 / 1486 / 1543 / 1667 |
| Editor de actividades | `abrirEditor()` / `pintarEditor()` / `guardar()` | 1757 / 1778 / 1849 |
| Exportar o pegar una actividad | `exportarActividad()` / `pegarActividad()` | 2011 / 1916 |
| Tomas de la actividad | `abrirTomasGuia()` / `guardarProg()` / `cargarTomasDoc()` | 1239 / 1292 / 1714 |
| Seguir jugando después de recargar | `seguirEncima()` / `seguirFuera()` | 1218 / 1225 |

---

## `Retos/index.html` — 1,664 líneas

**Documento de detalle:** `General/Retos.md`

No usa `vista…`: muestra la pantalla de identidad o la app con
`mostrarPantallaUsuario()` / `mostrarApp()`.

| Para... | Función | Línea |
|---|---|---|
| Arrancar: identidad y app | `cargarIdentidadGuardada()` / `mostrarPantallaUsuario()` / `mostrarApp()` | 552 / 563 / 579 |
| Saldos de arriba | `renderBalances()` | 602 |
| Crear reto: abrir, cerrar, leer y validar | `abrirFormulario()` / `cerrarFormulario()` / `leerFormulario()` / `validarFormulario()` | 728 / 792 / 814 / 831 |
| La meta que se calcula sola | `calcularMeta()` / `pintarHintMeta()` | 685 / 674 |
| Recompensa: mostrar u ocultar | `actualizarVisibilidadRecompensa()` / `abrirOverlayRecompensa()` | 657 / 960 |
| Lista de retos y su estado | `renderRetos()` / `etiquetaEstado()` / `faltanTiempo()` | 1332 / 1510 / 1522 |
| Buscar, cumplir, rechazar, retirar, eliminar | `buscarReto()` / `marcarCumplida()` / `rechazarReto()` / `retirarReto()` / `eliminarReto()` | 1001 / 1133 / 1005 / 1017 / 1088 |
| Reto propuesto por la IA | `cumplirRetoIA()` | 1032 |
| Conteo y retos vencidos | `conteo()` / `nuevoConteo()` / `finalizarRetosVencidos()` | 1103 / 1148 / 1225 |
| Cobrar la recompensa o aplicar el castigo | `cobrarRecompensaVisual()` / `aplicarCastigoVisual()` | 1194 / 1207 |
| Escuchar los datos en vivo | `escucharRetos()` / `escucharUsuarios()` / `escucharBalances()` | 1541 / 1603 / 1618 |
| Aviso de "nuevo" en la pestaña | `mostrarBanner()` / `bip()` / `notificar()` / `intentarResaltar()` | 412 / 418 / 430 / 455 |

---

## `Opciones/index.html` — 1,661 líneas

**Documento de detalle:** `General/Opciones.md`

**Vistas:** `vistaBloqueo` (162) · `vistaInicio` (174) · `vistaEspera` (202) ·
`vistaPlayer` (209) · `vistaConfig` (246) · `vistaSeguir` (268)

| Para... | Función | Línea |
|---|---|---|
| Arrancar: normal o directo | `entrar()` / `entrarDirecto()` | 603 / 542 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 1505 / 1532 |
| Cargar, guardar y repartir opciones | `cargarOpciones()` / `guardarOpciones()` / `repartirOpciones()` | 509 / 521 / 1173 |
| Quiénes juegan y de qué lado | `construirCabezas()` / `construirCabezasModo()` | 495 / 1166 |
| Arrancar la partida | `iniciar()` | 1196 |
| Pintar inicio, sala y paso | `pintarInicio()` / `pintarSala()` / `pintarPaso()` | 659 / 910 / 957 |
| Turnos y elección | `iniciarEstado()` / `siguienteTurno()` / `aplicarPick()` / `pickSesion()` | 556 / 570 / 584 / 801 |
| Sesión: escuchar, saltar, cerrar, fin | `escucharSesion()` / `saltarTurno()` / `cerrarSesion()` / `finPartida()` | 750 / 824 / 877 / 1042 |
| Invitados: agregar y QR | `agregarInvitado()` / `abrirQR()` | 1095 / 1140 |
| Invitado: entrar o continuar | `entrarAlJuego()` / `continuarPartida()` | 1331 / 1300 |
| Configuración: pintar y abrir | `pintarCfg()` / `abrirCfg()` | 1424 / 1488 |
| Agregar o editar opciones | `agregarOpcion()` / `guardarEdit()` / `agregarDesdeInput()` | 1417 / 1440 / 1466 |
| Seguir después de recargar | `seguirEncima()` | 1274 |

---

## `Diablitos/index.html` — 1,355 líneas

**Documento de detalle:** `General/Diablitos.md` (iconos) y `General/Pantallas.md`

No usa `vista…`: la sala y el juego se pintan a mano.

| Para... | Función | Línea |
|---|---|---|
| Arrancar la página | `arrancar()` | 1208 |
| Pintar la sala de espera | `pintar()` | 1267 |
| Lista y mensajes de la sala | `leerLista()` / `escribirLista()` / `asegurarLista()` / `decirFrase()` | 537 / 552 / 559 / 573 |
| Dibujar el demonio (SVG) | `svgDemonio()` / `cuerpo()` | 676 / 706 |
| Crear, colocar y mover | `crear()` / `colocar()` / `mover()` | 730 / 780 / 856 |
| Hablar, golpear y burbuja | `decir()` / `golpear()` / `burbuja()` / `borrarHabla()` | 784 / 804 / 835 / 796 |
| Generar y correr la animación | `generar()` / `correr()` / `parar()` / `reiniciar()` | 905 / 925 / 935 / 941 |
| Configuración: abrir y cerrar | `abrirCfg()` / `cerrarCfg()` | 1125 / 1143 |
| Pestañas y filas de la configuración | `cambiarPestana()` / `pintar()` / `fila()` / `cambiar()` / `agregar()` | 1099 / 993 / 1005 / 1037 / 1059 |
| Mantener la pantalla despierta | `pantallaDespierta()` | 505 |

---

## `Citas/index.html` — 1,290 líneas

**Documento de detalle:** `General/Pegamento-y-Citas.md` y `General/Pantallas.md`

No usa `vista…`: muestra la pantalla de identidad o la app.

| Para... | Función | Línea |
|---|---|---|
| Arrancar: catálogos, identidad y app | `cargarCatalogos()` / `cargarIdentidadGuardada()` / `mostrarApp()` | 437 / 489 / 516 |
| Nombre de la cita o del lado (por id) | `nombreDeCita()` / `nombreDeLado()` | 305 / 750 |
| Crear cita: abrir, cerrar, confirmar | `abrirFormulario()` / `cerrarFormulario()` / `confirmarCita()` | 656 / 695 / 971 |
| Rechazar o eliminar | `rechazarCita()` / `eliminarCita()` | 990 / 1002 |
| Lista de citas | `renderCitas()` / `escucharCitas()` | 1027 / 1191 |
| Actividades del formulario | `llenarSelectActividades()` | 533 |
| Accesorios: marcar y aplicar los de la actividad | `llenarAccesoriosForm()` / `obtenerAccesoriosMarcados()` / `aplicarAccesoriosDeActividad()` | 568 / 587 / 617 |
| Fecha: no agendar en el pasado | `esEnPasado()` / `ponerMinimoFecha()` / `hoyISO()` | 639 / 649 / 732 |
| Vestuario de la cita | `verVestuarioDeLaCita()` / `moverVestuario()` | 758 / 769 |
| Proponer la cita al otro | `irAProponer()` / `preguntarProponer()` | 948 / 958 |
| Aviso de "nuevo" | `mostrarBanner()` / `bip()` / `notificar()` | 346 / 352 / 364 |

---

## `favor.js` — 1,235 líneas

**Documento de detalle:** `General/Favores-Express.md`

Es un módulo, no una pantalla: dibuja la caja del favor encima de la app.

| Para... | Función | Línea |
|---|---|---|
| Pintar el precio del favor | `pintarPrecio()` | 220 |
| Preparar la caja del favor | `preparar()` | 258 |
| Quién soy y si hay favor vivo | `yoLocal()` / `hayFavorVivo()` | 115 / 138 |
| A quién le toca responder | `leTocaResponder()` | 506 |
| Escuchar respuestas y mostrarlas | `escucharRespuestas()` / `mostrarRespuesta()` | 512 / 647 |
| Responder y avisar al otro | `responder()` / `avisarAlOtro()` | 770 / 808 |
| Capa propia y espera | `laCapaPropia()` / `mostrarPropio()` / `pintarEspera()` | 859 / 897 / 932 |
| Encolar y pintar | `encolarPropios()` / `pintar()` | 981 / 943 |
| Precio, castigo y minutos | `precio()` / `castigoDe()` / `minutosDe()` | 1050 / 1047 / 1040 |
| Pagar, cobrar el castigo, cerrar y liquidar vencidos | `pagarFavor()` / `cobrarCastigo()` / `cerrarFavor()` / `liquidarVencidos()` | 1080 / 1133 / 1185 / 1058 |

---

## `Citas/actividades.html` — 1,140 líneas

**Documento de detalle:** `General/Pegamento-y-Citas.md`

No usa `vista…`: cambia de modo con `actualizarModo()`.

| Para... | Función | Línea |
|---|---|---|
| Cargar y pintar la lista | `cargar()` / `pintar()` / `listaActividades()` / `listaAccesorios()` | 530 / 471 / 444 / 457 |
| Normalizar y sacar el id de cada actividad | `normalizar()` / `idDe()` | 432 / 439 |
| Editor: abrir, cerrar, agregar | `abrirEditor()` / `cerrarEditor()` / `agregar()` | 642 / 757 / 593 |
| Guardar preset y detectar cambios | `guardarPreset()` / `hayCambiosSinGuardar()` | 787 / 807 |
| Renombrar actividad | `abrirRenombrar()` / `renombrarActividad()` | 863 / 885 |
| Eliminar actividad | `cerrarEliminar()` / `eliminarActividad()` | 959 / 965 |
| Ir a Accesorios y volver | `irAAccesorios()` / `volverDesdeAccesorios()` | 816 / 828 |
| Modo de la pantalla y controles | `actualizarModo()` / `controlesLista()` / `todosApagados()` | 501 / 736 / 1038 |
| Avisos del editor | `avisar()` / `editorAvisar()` / `renAvisar()` / `elimAvisar()` | 496 / 627 / 858 / 955 |

---

## `Retos/centro.html` — 952 líneas

**Documento de detalle:** `General/Centro-Adquisiciones.md`

**Vistas:** `vistaCatalogo` (149) · `vistaFavores` (167) · `vistaDeseos` (183) ·
`vistaPedidos` (198)

| Para... | Función | Línea |
|---|---|---|
| Arrancar y escuchar | `iniciar()` / `escuchar()` | 920 / 895 |
| Pintar todo y cambiar de pestaña | `pintarTodo()` / `ver()` / `pestana()` / `marcarNav()` | 620 / 407 / 623 / 416 |
| Catálogo, deseos y pedidos | `pintarCatalogo()` / `pintarDeseos()` / `pintarPedidos()` | 543 / 562 / 586 |
| Agregar deseo: modal y botón | `abrirAddModal()` / `cerrarAddModal()` / `actualizarBtnAdd()` | 798 / 807 / 792 |
| Comprar, borrar deseo, borrar compra, entregar | `comprar()` / `borrarDeseo()` / `borrarCompra()` / `marcarEntregado()` | 836 / 739 / 772 / 882 |
| Modales de la pantalla | `abrirModal()` / `pintarBotonesModal()` / `cerrarModal()` | 670 / 680 / 689 |
| Favores dentro del Centro | `pintarFavores()` / `abrirFavor()` / `escucharFavores()` | 303 / 363 / 367 |
| Precios y activación de favores | `numConfig()` / `miPrecio()` / `miActivar()` | 278 / 283 / 282 |
| Filas, saldo y altura | `fila()` / `nodoSaldo()` / `pintaCaja()` / `ajustarAlturaPedidos()` | 483 / 520 / 529 / 637 |

---

## Anexo: todas las funciones por archivo

> Orden alfabético. Formato: `nombre(línea)`. Sirve para buscar con Ctrl+F cuando la
> zona no se recuerda. Los números son de nov-2026.

### `Roles\index.html`

```
abrirAgregar(2665) · abrirCfg(5174) · abrirDetalle(4554) · abrirFin(2497)
abrirGaleria(1466) · abrirMeterInvitado(2875) · abrirModal(4123) · abrirModalDuelo(1623)
abrirModalImagen(2119) · abrirQR(2949) · abrirSeleccionCompartida(3690)
abrirSeleccionDueloCompartida(3517) · abrirSeleccionDueloLocal(3500)
abrirSeleccionLocal(3675) · abrirVentanaEspecial(1681) · actualizarFotos(4978)
actualizarTextoEstadoCarta(2113) · adminDe(2983) · agregarDesdeInput(4330)
agregarEspecial(4321) · agregarInvitado(2744) · agregarPersonaje(4310)
anunciarInvitacion(1964) · armando(2031) · arrancarSeleccion(3731) · asegurarOficiales(1142)
asegurarPersonajes(1190) · avanzarDueloJuntosLocal(2528) · avanzarTarjeta(1368)
avisoJSONMalo(4222) · avisosCorrespondencia(4491) · bajarArchivo(4925)
baseConfigurada(4916) · borrarDetalle(4699) · buscarPersonaje(1247) · cabezas(2026)
cabs(2816) · cambiarMarca(3649) · cambiarMarcaDuelo(3416) · candidatosImagenDrive(4600)
cargarEstado(1741) · cargarIdentidad(1000) · cargarOficiales(1128) · cargarPersonajes(1171)
cerrarDetalle(4578) · cerrarModal(4140) · cerrarModalImagen(2127) · cerrarSesion(1979)
chequearPartidaEspera(1807) · claveCfg(4161) · confirmarArranqueDuelo(3312)
conPendiente(3945) · construirCabezas(1031) · construirCabezasModo(2976)
continuarPartida(3971) · continuarPartidaLocal(3994) · contraDeRonda(2727)
contraparteDe(1273) · datosDrive(4587) · deck(2794) · deshacerFotos(5083)
disponiblesInvitados(2661) · dueloEsJuntos(2705) · dueloLadoDePartida(2695)
dueloMismoLadoDePartida(1242) · dueloModalidadDePartida(2700) · elegirAzarDuelo(3439)
elegirAzarSeleccion(3455) · elegirTentacion(3479) · enEspera(2038) · entrar(1379)
entrarAlJuego(4029) · entrarDirecto(1339) · esAnfitrion(1986) · esClaveLista(4165)
escucharAprobacion(970) · escucharGrupo(5313) · escucharSeleccion(3778)
escucharSesion(1831) · esDueloJuntos(2753) · esEnlaceGooglePhotos(4584) · esModoDuelo(2692)
esOficial(1124) · especialDe(1770) · especialDeLado(2218) · especialK(1645)
especialPendido(1644) · exportarFotos(4940) · exportarLista(4877) · fechaCorta(4920)
filaPersonaje(4388) · filaVariante(4355) · filtro(4451) · finPartida(2504)
guardarDetalle(4652) · guardarEdit(4362) · guardarLocalGuardada(932)
guardarPersonajes(1194) · hostNombre(3531) · idLibre(4181) · indexarPersonajes(1059)
iniciar(3104) · iniciarEstado(1345) · irAlMenu(5214) · lado(2733) · ladoAnatomiaCfg(4157)
ladoDeCabeza(2707) · ladoDuelo(2777) · ladoOriginal(2735) · leerJSONPegado(4199)
leerLocalGuardada(946) · leerQuienSoy(997) · leerSnapshotFotos(4967) · licMsg(989)
limpiarFiltro(4172) · limpiarFiltroSel(3284) · limpiarLocalGuardada(956)
limpiarParaArchivo(4863) · listaDeCabezaPara(3006) · listaDeLado(1223) · listaSegura(1080)
llenar(2043) · llenarSelectPar(4535) · marcas(2901) · mensajeEnlaceInvalido(4643)
meterInvitado(2896) · mezclar(884) · miLado(4158) · mismoContenidoPersonaje(1099)
mismosLados(2980) · modalAbierto(5237) · modalidad(3079) · modoAdmiteInvitados(1992)
modoBaseDePartida(2686) · mostrarBotonesAdmin(1993) · mostrarCaraDuelo(2312)
mostrarGracia(960) · nombreAdmin(1017) · nombreArchivoExport(4872) · nombreCabeza(1027)
nombreDeLado(4159) · nombreDeLista(4166) · nombreHostSeleccion(3294) · nombreLado(1023)
nombres(1824) · normSel(3281) · ordenPersonajes(1149) · otroLado(4490) · otroLadoDuelo(1235)
parejaAcepto(3304) · parejaAEsperar(3300) · pares(2730) · paresDisponibles(1288)
parsePegadoPersonajes(4237) · parsePegadoTextos(4264) · pedirCartasInvitado(2838)
pegarLista(4725) · personajeDe(4289) · personajesRef(917) · pintarAvisosCfg(4512)
pintarBotonDeshacerFotos(4973) · pintarCaraDuelo(2225) · pintarCfg(4412)
pintarDueloPar(2284) · pintarDueloTentacion(2298) · pintarEspecial(1653)
pintarFaseDuelo(2078) · pintarFoto(2177) · pintarFotoEn(2145) · pintarFotoGaleria(1485)
pintarGaleria(1497) · pintarInicio(1555) · pintarMeterInvitado(2884)
pintarModalDuelo(1607) · pintarModo(1565) · pintarModoPartida(2714) · pintarPaso(2402)
pintarPasoDueloJuntos(2326) · pintarSala(2017) · pintarSalidas(1010) · pintarSeleccion(3555)
pintarSeleccionDuelo(3324) · pintarTarjeta(2178) · pintarVolteo(2087)
ponerBadgeOficial(1157) · ponerSinFotoGaleria(1477) · poolsDuelo(1302)
poolsEspejoMismo(2989) · preparar(3046) · prepararDuelo(3077) · probar(4201)
probarImagen(4607) · puedeVerOtroLado(4154) · quienes(2720) · recalcularOficiales(1105)
reiniciarVariantes(1717) · repartirEspeciales(1727) · repartirTarjetas(3017)
resetCarta(2134) · resolverEnlaceImagen(4627) · retirarInvitadosDeLaPartida(921)
revisarEspecial(3093) · ronda(2749) · salirAlMenu(5224) · salirModoInvitado(4094)
saltarTurno(1913) · sanearSesion(1774) · seguirEncima(3934) · seguirFuera(3939)
seleccionRef(3261) · selEsCompartida(3262) · selFuente(3264) · selMarcosDe(3265)
selPoolDe(3270) · selTodosListos(3275) · sesionRef(918) · siguienteDueloJuntos(2545)
siguienteSesion(1886) · siguienteTurno(1353) · sinDuplicados(892) · soyCabeza(1343)
terminar(4612) · textoPersonaje(1094) · traePar(4720) · url(2147) · ver(5194)
vistaDeInicio(5206) · voltear(2086) · voltearDuelo(2319) · yaExiste(4175)
```

### `Castigos\index.html`

```
abortarPlacer(2623) · abrirDetalle(1587) · abrirEditor(1365) · abrirQRJuego(3974)
accesorioEnUso(1847) · accionDeNivel(2794) · accionesModeloPorRonda(4131)
accionVacia(1399) · actualizar(2516) · actualizarBotonJugar(1511) · actualizarInicio(2319)
agregar(1477) · agregarInvitadoAPartida(4212) · agregarInvitadoLocal(4197)
ajustarAltoCampo(1409) · anunciarinvitacion(3269) · armando(3436)
armarBolsasImposicion(2764) · armarPartidaNormal(2634) · asignarImposicionesAlAzar(2775)
avanzarSaltadoRemoto(3729) · avanzarTurnoNoSaltado(3158) · avanzarTurnoRemoto(3697)
bolsasEnMemoria(4039) · bolsasParaInvitado(4073) · borrarAcceso(1829) · borrarAccion(1534)
borrarCastigo(1347) · borrarImp(1916) · cargarAccesorios(824) · cargarCastigos(788)
cargarDatosCastigo(1926) · cargarIdentidad(728) · cargarImposiciones(837)
cargarSesionEnMemoria(3360) · cargarTodo(780) · cerrar(2187) · chequearConexion(4299)
chequearPartidaEspera(3409) · clave(4118) · colorAccion(3581) · conGente(3432)
construirNivelesOficial(863) · contarAccionesCastigos(1971) · continuarPausa(2214)
continuarSeleccionCastigo(2265) · controlesAnfitrionVisible(3516)
crearSesionCompartida(3261) · descartarPausa(2201) · descripcionPausa(2176) · destino(1216)
elegirAccionInvitado(4114) · elegirCastigoParaJugar(2642) · elegirModo(2359)
enEspera(3440) · enfocarAccion(1499) · enJuego(1055) · entrar(4305)
entrarAlJuegoCompartida(3397) · escribirImposicionRemoto(3678) · escucharGrupo(747)
escucharSesionCompartida(3288) · esSoloPuro(3517) · estadoPartidaLocal(2056)
esUnCelular(3591) · etiquetaLados(772) · filtro(1286) · finVisible(1049) · fraseAccion(3531)
gastarCortesiasCastigo(2301) · generarJugadores(2742) · generarTurnos(2802)
generarTurnosMulti(3003) · guardarCastigoDatos(1617) · guardarImposiciones(1923)
idVigente(664) · iniciarPartida(3164) · iniciarPartidaMulti(2895)
iniciarTemporizadorDesde(3127) · irAlMenu(1142) · ladoDe(4133) · ladoInv(4200)
ladosParticipantes(2591) · leerNivelesCastigo(4046) · leerPausa(2144) · leerQuienSoy(724)
llenar(3444) · mezclar(1400) · modalAbierto(1163) · modalBasePaso(1091)
mostrarBotonAccion(3107) · mostrarFin(3475) · mostrarGracia(1116) · mostrarModalBase(1109)
mostrarPanel(1264) · msg(1260) · msgTomas(1261) · nivel(4170) · nombreDeLado(768)
normalizaAcc(1541) · normalizarAccionImport(1719) · normalizarAccionOficial(851)
normalizarNivelesPlacer(2561) · normTxt(4037) · overlayReinstalar(990)
pararTemporizador(3103) · parsearImportacion(1683) · partes(4275) · partes2(4285)
pausarPartida(2129) · pintarAccesorios(1761) · pintarAccesoriosDetalle(1543)
pintarCastigos(1282) · pintarCrono(3121) · pintarEditor(1414) · pintarImposiciones(1884)
pintarListaInicio(1988) · pintarSala(3429) · pintarSalidas(1053) · pintarTomas(1519)
pintarTomasJugar(2677) · pintarTomasJugarMulti(2691) · pintarTurno(3546)
placerAccionesEnNiveles(2600) · placerAlcanzaMulti(2613) · placerAlcanzaNormal(2609)
poolDeAcciones(4094) · preguntarImposicionesPor3(2507) · preguntarNivelesPlacer(2567)
preguntarPausa(2183) · preguntarQuienCastiga(2348) · promptTexto(1950)
publicarSesion(3204) · puedeJugarCastigo(2295) · quitarAccesorioDeTodas(1863)
reanudarCronoRemotoSiHaceFalta(3148) · recalcularSaltadoPorRevivir(3093)
refrescarUsuarios(741) · reinstalarOficialDesdeUrl(1003) · renombrarAcceso(1795)
renombrarCastigo(1331) · repararOficialCastigo(952) · repartirRueda(2958)
resetearInicioMulti(3920) · restaurarPartidaLocal(2087) · retirarInvitadosDeLaPartida(2736)
salirAlMenu(1152) · salirModoInvitado(3948) · saltado(2878) · saltarTurnoRemoto(3760)
seleccionarCastigo(2255) · sesionRef(2731) · setHowTabs(2383) · setModTabs(2376)
setTipoTabs(2405) · sincronizarOficialesCastigos(880) · soyCabeza(3406)
tieneAcciones(4068) · toggleMulti(2412) · tomarImposicion(2767) · totalAccionesDatos(948)
totalAccionesEditor(1504) · turnosConInvitado(4151) · vaciaDatos(1394) · vale(4119)
ver(1063) · vistaActual(1045) · volverConHistorial(1127) · volverDePartida(3937)
volverTiendaReinstalar(979)
```

### `index.html`

```
abrirCambiarUsu(2558) · abrirCom(1487) · abrirEdUsuarios(2309) · abrirExp(1437)
abrirHistorial(1693) · abrirJuegos(1454) · abrirPanelUsuarios(2734) · abrirPropuestas(2086)
abrirPuntos(1656) · abrirRetos(1465) · abrirSegunHash(1412) · abrirSub(1420)
aceptarPropuesta(2121) · actualizarAvisoPropuestas(1933) · actualizarPuntoCarrito(938)
adminId(1119) · agregarFila(1047) · aplicar(1308) · armarFilas(1042)
cancelarPropuesta(2196) · cerrar(2278) · cerrarCom(1495) · cerrarEdUsuarios(2393)
cerrarExp(1448) · cerrarGear(2550) · cerrarHistorial(1748) · cerrarJuegos(1462)
cerrarOverlaysInv(2528) · cerrarPropuestas(2095) · cerrarPuntos(1675) · cerrarRetos(1475)
cerrarSub(1430) · conTiempo(591) · crearFilaProp(1979) · detenerScan(1237)
detenerScanInv(2787) · entrar(1146) · etiqueta(1293) · etiquetaAnatomia(1520)
etiquetaProp(2010) · formatearFechaMov(1684) · guardarAnatomiaUsuario(1526)
hashActual(1408) · hashTexto(2257) · iconoMenu(620) · iniciar(1169)
iniciarPropuestas(1959) · iniciarScan(1341) · invModoScan(2565) · invMsg(1503)
invRefrescar(1508) · invVer(2488) · irPaso3(1027) · lado(1523) · leerGuardado(615)
mostrarGear(2538) · mostrarIdentidad(955) · mostrarMenu(666) · msg(586) · msgQR(1243)
nombreParejaMenu(813) · normalizaNombre(2863) · overlayInvAbierto(2525) · overlaysInv(2522)
parsearFB(598) · pedirPin(2267) · pintarInvUsuarios(1551) · pintarPropuestas(2013)
pintarTelegram(2626) · ponerZoom(1260) · probar(1301) · propuestasAbiertas(1975)
propuestasMiasPendientes(1907) · propuestasParaMi(1901) · propuestasResultadosNuevos(1913)
propuestasResultadosVisibles(1921) · ptsRaw(2405) · quitarZoom(1250) · recargar(973)
rechazarPropuesta(2173) · remateHero(647) · renderPacks(800) · renderPacksDeVerdad(825)
renumerarRadios(1099) · resolverTodasPropuestas(2219) · salirSinHaberEntrado(2576)
tarjetaPack(764) · textoDestinoProp(1894) · textoValorProp(1783) · tgApi(2643)
tgEstado(2621) · tgGuardado(2607) · tgTarjeta(2614) · titulo(2027) · todos(2318)
usuariosEfectivos(995) · valorEfectivoProp(1768) · valorPropValido(1775) · verHist(1599)
verMenu(1388) · verPaso(609) · volverSiInvitadoSinPartida(1206)
```

### `Lenceria\index.html`

```
abrirClasif(1103) · abrirDatos(2478) · abrirElegir(1942) · abrirLupa(1307)
abrirPedido(2179) · abrirPrenda(1332) · aceptarPedido(2220) · agregarClasif(1085)
alternarFijo(2108) · alternarSeleccion(1995) · aplicarEntradaCita(2726)
aplicarImportacion(2543) · arrancar(2780) · asegurarLados(943) · asegurarRefs(900)
bloqueClasif(1025) · bloquePrendas(1191) · borrarClasif(1160) · borrarPlan(2117)
borrarPrenda(1568) · botonPasados(1656) · cancelarPedido(2307) · cargarClasificaciones(763)
cargarPedidos(2408) · cargarPlanes(2401) · cargarPrendas(2394) · cargarTodo(2712)
cerrarLupa(1313) · claveRef(831) · compararRef(837) · construirFiltros(613)
conTiempo(2705) · desplegableFiltro(660) · diasDesdeUso(807) · escribirAviso(2170)
escuchar(2423) · esMia(1674) · extra(735) · fechaAObjeto(552) · fechaDeUso(795)
fechaLarga(557) · guardarClasif(1136) · guardarPlan(2054) · guardarPrenda(1509)
hoyTexto(546) · idDeLado(1186) · irAlMenu(403) · lado(2591) · ladoDePersona(497)
ladoDePrenda(514) · ladoDeUsuarioId(504) · leerImagen(1411) · limpiarFiltros(601)
limpiarPedidosVencidos(1908) · liquidarUsos(2360) · llenarSelect(1321)
mandarPropuesta(2133) · miniatura(1805) · mismoConjunto(2214) · modalAbierto(422)
mostrarFoto(1388) · nombreDe(985) · nombreLado(489) · nombrePersona(493) · normTexto(565)
ordenarClasif(780) · ordenPrendas(851) · ordenRef(846) · pasaFiltro(605)
pedidoVencido(1822) · pintarClasifVista(1111) · pintarConfig(1007) · pintarContador(2041)
pintarPedido(2203) · pintarPlanes(1664) · pintarVestidor(1976) · planDePersona(539)
planesDe(1638) · planesDePersona(523) · planesDePersonaPorFecha(536) · planesPorFecha(527)
pref(2735) · prendaEnUsoFuturo(1403) · prendasDeLado(1182) · prendasDePersona(519)
procesarFoto(1430) · quedan(1591) · rechazarPedido(2282) · salirAlMenu(410)
sembrarClasificaciones(690) · separadorPlanes(1649) · siguienteRef(870) · sorprendeme(2320)
tarjetaPedidoEnviado(1876) · tarjetaPedidoRecibido(1827) · tarjetaPlan(1748)
tarjetaPrenda(1245) · textoUso(816) · tipoCubreTodo(863) · tsUso(802)
usarArchivoFoto(1473) · usoDe(990) · valor(787) · ver(385)
```

### `Encuentros\index.html`

```
abrirAgregar(2268) · abrirEditor(1577) · abrirModal(1743) · abrirQRInvitacion(2361)
abrirTomas(1769) · acts(1815) · agregar(1624) · agregarInvitado(2290) · agregarItemEd(1671)
anunciarInvitacion(948) · armando(2026) · avanzarLocal(847) · avanzarSesion(870)
avisarCortesia(1328) · base(2220) · cab(674) · cabezas(2341) · cabs(2033)
cargarActividades(1233) · cargarActsParaInvitado(2169) · cargarEnMemoria(603)
cargarIdentidad(532) · cargarTomasDoc(1501) · cerrarModal(1763) · cerrarSesion(965)
cerrarTomas(1799) · chequearPartidaEspera(751) · chequearPendiente(659) · companero(2301)
compararActividades(1295) · construirCabezas(1821) · contarNivel(406) · dibujarLista(1337)
disponiblesInvitados(2264) · docDe(1132) · elegirAccionEnc(2203) · enEspera(2038)
entrar(700) · entrarAlJuego(2473) · entrarDirecto(599) · esAnfitrion(2000)
escucharAprobacion(491) · escucharGrupo(2495) · escucharSesion(775) · etiquetaLados(1480)
filtrar(1407) · gastarCortesias(1303) · generarListas(1832) · generarYIniciar(1905)
guardadas(1775) · guardarEditor(1666) · guardarTomasEnBase(1534) · iniciarSingle(684)
irAlMenu(1028) · item(2126) · leerQuienSoy(529) · leerTomasEd(1693) · licMsg(521)
limpiarInvitadosDeSesionAnterior(982) · listaConInvitado(2219) · llenar(2043) · mezclar(411)
migrarTomasDeEsteCelular(1516) · modalAbierto(1052) · mostrarBotonesAdmin(2001)
mostrarFin(995) · mostrarGracia(427) · multiRefrescar(1418) · multiToggle(1428)
nivel(2244) · nivelPorNombre(2165) · nombreAdmin(555) · nombreCabeza(652) · nombreLado(1476)
nombres(768) · normLados(401) · normOrdenAct(1292) · normTomasEnc(1491) · normTxtEnc(2163)
ofs(1136) · overlayReinstalar(1177) · pintarEditor(1595) · pintarLista(1392)
pintarListaCfg(1543) · pintarPaso(2084) · pintarSala(2019) · pintarSalidas(547)
pintarTurnoDe(2070) · poolDeAccionesEnc(2184) · puedeJugarActividad(1322)
quiereCompartido(1968) · quitarItemEd(1684) · reinstalarOficialDesdeUrl(1190)
repartirRuedaEnc(1867) · retirarInvitadosDeLaPartida(976) · salirAlMenu(1038)
salirModoInvitado(454) · saltarTurno(900) · sanearSesion(623) · seguirEncima(2419)
seguirFuera(2424) · sesionRef(561) · sincronizarOficiales(1134) · soyCabeza(615)
tomasGuardadasEd(1539) · ultimo(2134) · vale(2207) · ver(1002)
volverTiendaReinstalar(1166)
```

### `Guiadas\index.html`

```
abrirEditor(1757) · abrirFin(485) · abrirTomasGuia(1239) · agregar(1807) · agregarItem(1854)
aplicaSesion(650) · armarListaLados(1328) · asignarParaId(1316) · avanzarSesion(553)
avisarCortesia(1059) · borrarProg(1299) · cargarActividades(964) · cargarIdentidad(498)
cargarTomasDoc(1714) · cerrarSesion(606) · cerrarTomasGuia(1264) · claveDoc(854)
compararActividades(1026) · contarNivel(337) · dibujarLista(1068) · docDe(861)
editorTieneAlgo(1913) · empezarNuevo(1350) · entrar(361) · esAdmin(513)
escucharAprobacion(423) · escucharSesion(658) · etiquetaLados(541) · exportarActividad(2011)
filtrar(838) · gastarCortesias(1034) · guardar(1849) · guardarProg(1292)
guardarTomasEnBase(1747) · iniciarSesionCompartida(572) · irAlMenu(724)
jugadoresBase(1302) · jugarDirecto(1164) · leerJSONPegado(1900) · leerProg(1228)
leerQuienSoy(495) · leerTomas(1876) · licMsg(405) · limpiarParaArchivo(1994)
marcarRadio(549) · mensajeEditor(1890) · mezclar(846) · migrarTomasDeEsteCelular(1729)
miIdSesion(547) · mismoPaso(532) · modalAbierto(751) · modalBasePaso(1459) · mostrarFin(479)
mostrarGracia(352) · mostrarModalBase(1477) · mostrarPlayer(1371) · multiAbrir(1517)
multiAbrirSel(1543) · multiMostrar(1483) · multiRefrescar(1486) · multiSalir(1551)
multiToggle(1496) · nombreAdmin(514) · nombreDe(519) · nombreDePaso(524) · nombreLado(537)
normLados(324) · normOrdenAct(1023) · normTomas(329) · ofs(867) · overlayReinstalar(908)
pegarActividad(1916) · pintarEditor(1778) · pintarLista(1149) · pintarPaso(2077)
pintarTurnoDe(2068) · probar(1902) · puedeJugarActividad(1053) · quienes(1536)
quitarItem(1867) · refrescarMiLado(506) · reinstalarOficialDesdeUrl(921)
repartirRuedaGuia(1667) · salirAlMenu(734) · saltarTurno(624) · seguirEncima(1218)
seguirFuera(1225) · sesionPausada(612) · sesionRef(548) · sincronizarOficiales(865)
tomasDePantalla(2002) · tomasGuardadas(1752) · top(1071) · ver(700)
volverTiendaReinstalar(897)
```

### `Retos\index.html`

```
abrirFormulario(728) · abrirOverlayRecompensa(960) · actualizarVisibilidadRecompensa(657)
aplicarCastigoVisual(1207) · bip(418) · buscarReto(1001) · calcularMeta(685)
cargarIdentidadGuardada(552) · cerrarFormulario(792) · cerrarRecompensa(972)
cobrarRecompensaVisual(1194) · conteo(1103) · cumplido(1294) · cumplirRetoIA(1032)
diasRestantes(527) · eliminarReto(1088) · esc(509) · escucharBalances(1618)
escucharRetos(1541) · escucharUsuarios(1603) · esRelevanteReto(1534) · estaSuprimido(441)
etiquetaEstado(1510) · faltanTiempo(1522) · finalizarRetosVencidos(1225)
firmaDeUsuarios(705) · firmaReto(1527) · formatearFecha(515) · guardarIdentidad(558)
intentarResaltar(455) · leerFormulario(814) · llenarSelectAsignado(644)
marcarCumplida(1133) · momentoFecha(547) · mostrarApp(579) · mostrarBanner(412)
mostrarPantallaUsuario(563) · nombrePersona(700) · notificar(430) · nuevoConteo(1148)
pintarHintMeta(674) · rechazarReto(1005) · renderBalances(602) · renderRetos(1332)
resumenHtml(711) · retirarReto(1017) · soyReceptor(845) · suprimir(438) · truncar(638)
validarFormulario(831)
```

### `Opciones\index.html`

```
abrirAgregar(1076) · abrirCfg(1488) · abrirFin(1035) · abrirModal(1392) · abrirQR(1140)
agregarDesdeInput(1466) · agregarInvitado(1095) · agregarOpcion(1417)
anunciarInvitacion(862) · aplicarPick(584) · armando(924) · cabezas(919) · cabs(1123)
cargarEstado(678) · cargarIdentidad(464) · cargarOpciones(509) · cerrarModal(1409)
cerrarSesion(877) · chequearPartidaEspera(726) · conPendiente(1284) · construirCabezas(495)
construirCabezasModo(1166) · continuarPartida(1300) · disponiblesInvitados(1072)
enEspera(931) · entrar(603) · entrarAlJuego(1331) · entrarDirecto(542) · esAnfitrion(884)
escucharAprobacion(434) · escucharGrupo(1614) · escucharSesion(750) · filtro(1431)
finPartida(1042) · fuente(1102) · guardarEdit(1440) · guardarOpciones(521) · iniciar(1196)
iniciarEstado(556) · irAlMenu(1522) · leerQuienSoy(461) · licMsg(453) · llenar(936)
mezclar(374) · modalAbierto(1545) · modoAdmiteInvitados(890) · mostrarBotonesAdmin(891)
mostrarGracia(424) · nombreAdmin(481) · nombreCabeza(491) · nombreLado(487) · nombres(743)
opcionesRef(415) · parDe(548) · parseLista(396) · pick(1049) · pickSesion(801)
pintarCfg(1424) · pintarInicio(659) · pintarPaso(957) · pintarSala(910) · pintarSalidas(474)
quiereCompartido(1217) · quitar(587) · repartirOpciones(1173) · restantes(1000)
retirarInvitadosDeLaPartida(419) · ronda(1099) · rondaActual(1001) · salirAlMenu(1532)
salirModoInvitado(1362) · saltarTurno(824) · sanearSesion(693) · seguirEncima(1274)
seguirFuera(1279) · sesionRef(416) · siguienteTurno(570) · sinDuplicados(382)
soyCabeza(546) · ver(1505)
```

### `Diablitos\index.html`

```
abrirCfg(1125) · agregar(1059) · arrancar(1208) · asegurarLista(559) · asegurarMensajes(568)
avisar(1110) · borrarHabla(796) · burbuja(835) · cambiar(1037) · cambiarPestana(1099)
cargar(660) · cerrarCfg(1143) · colocar(780) · correr(925) · crear(730) · cuando(1311)
cuerpo(706) · decir(784) · decirAviso(578) · decirFrase(573) · escanearCarpeta(611)
escribiendo(1163) · escribirLista(552) · esModoInvitado(526) · fila(1005) · generar(905)
golpear(804) · intentaExtension(632) · intervalo(604) · leerLista(537) · limites(723)
medir(714) · mostrarAviso(583) · mover(856) · multVelocidad(600) · onda(595)
pantallaDespierta(505) · parar(935) · paso(912) · pintar(993) · probarNumerados(644)
probarUno(629) · puedeGuardar(518) · quitar(851) · quitarFila(1048) · reiniciar(941)
rnd(516) · salirSala(1261) · seccion(991) · siguiente(648) · svgDemonio(676)
volverAlOriginal(1077)
```

### `Citas\index.html`

```
abrirFormulario(656) · aplicarAccesoriosDeActividad(617) · bip(352) · campoActividadId(317)
cargarCatalogos(437) · cargarIdentidadGuardada(489) · cerrarFormulario(695)
confirmarCita(971) · conTiempo(430) · eliminarCita(1002) · escucharCitas(1191)
escucharUsuarios(1237) · esEnPasado(639) · esRelevanteCita(1186) · estaSuprimido(375)
fechaAObjetoISO(738) · fechaLargaISO(743) · firmaCita(1182) · firmaDeUsuarios(310)
formatearFecha(1017) · guardarIdentidad(495) · hoyISO(732) · idNuevo(828)
intentarResaltar(391) · irAProponer(948) · llenarAccesoriosForm(568)
llenarSelectActividades(533) · mostrarApp(516) · mostrarBanner(346)
mostrarPantallaUsuario(500) · moverVestuario(769) · nombreDeCita(305) · nombreDeLado(750)
notificar(364) · obtenerAccesoriosActividad(591) · obtenerAccesoriosMarcados(587)
ordenarAccesorios(629) · otroId(984) · otrosUsuarios(543) · ponerMinimoFecha(649)
preguntarProponer(958) · prepararCampoPara(547) · rechazarCita(990) · renderCitas(1027)
suprimir(372) · verVestuarioDeLaCita(758)
```

### `favor.js`

```
aPagar(1084) · avisarAlOtro(808) · barrerAvisoHuerfano(602) · castigoDe(1047) · cents(665)
cerrar(215) · cerrarFavor(1185) · cerrarRespondida(450) · cobrarCastigo(1133)
cuandoMil(474) · descartar(466) · encolarPropios(981) · escucharRespuestas(512)
esReciente(405) · faltaEn(890) · fueDescartado(462) · hayCajaAbierta(60) · hayFavorVivo(138)
laCapaPropia(859) · laCapaRespuesta(562) · leTocaResponder(506) · liquidarVencidos(1058)
marcarAvisosVistos(626) · marcarAvisoVisto(643) · milisRestantes(882) · minutosDe(1040)
mostrarPropio(897) · mostrarRespuesta(647) · olvidarDescartados(469) · pagarFavor(1080)
pintar(943) · pintarEspera(932) · pintarPrecio(220) · ponerEstilo(81) · precio(1050)
preparar(258) · responder(770) · saldoParaAntes(1095) · siguiente(483)
siguienteEstado(748) · siguientePropio(846) · textoParaElOtro(762) · veces(164)
yoLocal(115)
```

### `Citas\actividades.html`

```
abrirEditor(642) · abrirRenombrar(863) · actualizarModo(501) · agregar(593) · avisar(496)
cargar(530) · cerrarEditor(757) · cerrarEliminar(959) · cerrarRenombrar(875)
controlesLista(736) · deshecho(763) · editorAvisar(627) · elimAvisar(955)
eliminarActividad(965) · guardarPreset(787) · hayCambiosSinGuardar(807) · idDe(439)
irAAccesorios(816) · listaAccesorios(457) · listaActividades(444) · modalAbierto(772)
normalizar(432) · pintar(471) · ponerTitulo(1046) · renAvisar(858) · renombrarActividad(885)
restaurarLista(744) · todosApagados(1038) · volverDesdeAccesorios(828)
```

### `Retos\centro.html`

```
abrirAddModal(798) · abrirFavor(363) · abrirModal(670) · actualizarBtnAdd(792)
ajustarAlturaPedidos(637) · borrarCompra(772) · borrarDeseo(739) · botonBorrarPedido(765)
camposListos(789) · cerrarAddModal(807) · cerrarModal(689) · comprar(836) · descartados(342)
esA(624) · escuchar(895) · escucharFavores(367) · fila(483) · iniciar(920)
marcarEntregado(882) · marcarNav(416) · miActivar(282) · miPrecio(283) · modalAbierto(440)
nodoSaldo(520) · numConfig(278) · pasoBase(652) · pestana(623) · pintaCaja(529)
pintarBotonesModal(680) · pintarCatalogo(543) · pintarDeseos(562) · pintarFavores(303)
pintarPedidos(586) · pintarTodo(620) · ver(407) · yoFresh(931)
```

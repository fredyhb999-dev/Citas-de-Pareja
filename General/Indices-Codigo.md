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

## `Roles/index.html` — 5,255 líneas

**Documento de detalle:** `General/Roles.md`

**Vistas:** `vistaBloqueo` (380) · `vistaInicio` (392) · `vistaSeleccion` (457) ·
`vistaEspera` (490) · `vistaPlayer` (497) · `vistaConfig` (584) · `vistaSeguir` (674)

| Para... | Función | Línea |
|---|---|---|
| Arrancar la página: identidad, licencia y estado guardado | `entrar()` | 1372 |
| Cambiar de vista y guardar el paso del historial | `ver()` | 5089 |
| Volver al menú deshaciendo los pasos | `salirAlMenu()` | 5119 |
| Pintar la tarjeta de inicio (modo y "Jugar") | `pintarInicio()` | 1548 |
| Pantalla de modo (Clásico, Cambia de Bando, Seleccionar, Duelo) | `pintarModo()` | 1558 |
| Modal del duelo | `pintarModalDuelo()` / `abrirModalDuelo()` | 1600 / 1616 |
| Quiénes juegan y de qué lado | `construirCabezas()` | 1024 |
| Pool de personajes: cargar, sembrar, guardar | `cargarPersonajes()` / `asegurarPersonajes()` / `guardarPersonajes()` | 1164 / 1183 / 1187 |
| Buscar personaje o su contraparte | `buscarPersonaje()` / `contraparteDe()` | 1240 / 1266 |
| Repartir tarjetas y preparar la partida | `repartirTarjetas()` / `preparar()` / `prepararDuelo()` | 3010 / 3039 / 3070 |
| Arrancar la partida normal | `iniciar()` | 3097 |
| Modo Seleccionar: pintar, abrir y arrancar | `pintarSeleccion()` / `abrirSeleccionLocal()` / `abrirSeleccionCompartida()` / `arrancarSeleccion()` | 3552 / 3672 / 3687 / 3728 |
| Escuchar la selección compartida | `escucharSeleccion()` | 3775 |
| Sala de espera (anfitrión e invitado) | `pintarSala()` | 2010 |
| Pintar la partida: tarjeta, paso, duelo | `pintarTarjeta()` / `pintarPaso()` / `pintarCaraDuelo()` / `pintarPasoDueloJuntos()` | 2171 / 2395 / 2218 / 2319 |
| Pasar turno o saltarlo | `siguienteTurno()` / `avanzarTarjeta()` / `siguienteSesion()` / `saltarTurno()` | 1346 / 1361 / 1879 / 1906 |
| Terminar la partida | `abrirFin()` / `finPartida()` | 2490 / 2497 |
| Sesión multijugador | `escucharSesion()` | 1824 |
| Configuración: pintar, abrir, filas y editor | `pintarCfg()` / `abrirCfg()` / `filaPersonaje()` / `agregarPersonaje()` | 4409 / 5069 / 4385 / 4307 |
| Exportar la lista de personajes | `exportarLista()` | 4772 |
| Invitado: entrar, continuar, salir | `entrarAlJuego()` / `continuarPartida()` / `salirModoInvitado()` | 4026 / 3968 / 4091 |
| QR de invitación | `abrirQR()` | 2942 |
| Modales chicos | `abrirModal()` / `cerrarModal()` | 4120 / 4137 |

---

## `Castigos/index.html` — 4,389 líneas

**Documento de detalle:** `General/Castigos.md`

**Vistas:** `vistaInicio` (249) · `vistaBloqueo` (307) · `vistaTomas` (314) ·
`vistaPartida` (335) · `vistaEspera` (408) · `vistaConfig` (494) · `vistaEditar` (537)

| Para... | Función | Línea |
|---|---|---|
| Cargar todo: identidad, castigos, accesorios, imposiciones, usuarios | `cargarTodo()` | 767 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 1050 / 1139 |
| Panel de configuración | `mostrarPanel()` | 1246 |
| Lista y edición de castigos | `pintarCastigos()` / `abrirEditor()` / `pintarEditor()` / `guardarCastigoDatos()` | 1264 / 1347 / 1396 / 1599 |
| Tomas de cada castigo | `pintarTomas()` | 1501 |
| Accesorios e imposiciones | `pintarAccesorios()` / `pintarImposiciones()` | 1743 / 1866 |
| Pantalla de inicio y castigo elegido | `pintarListaInicio()` / `seleccionarCastigo()` / `actualizarInicio()` | 1970 / 2237 / 2301 |
| Pasos antes de jugar: quién castiga, modo, multi, imposiciones, placer | `preguntarQuienCastiga()` / `elegirModo()` / `toggleMulti()` / `preguntarImposicionesPor3()` / `preguntarNivelesPlacer()` | 2330 / 2341 / 2394 / 2489 / 2549 |
| Armar y arrancar: normal y multi | `armarPartidaNormal()` / `iniciarPartida()` / `iniciarPartidaMulti()` | 2616 / 3146 / 2877 |
| Repartir turnos y rueda | `repartirRueda()` / `generarTurnos()` / `generarTurnosMulti()` | 2940 / 2784 / 2985 |
| Pintar turno, sala y fin | `pintarTurno()` / `pintarSala()` / `mostrarFin()` | 3528 / 3411 / 3457 |
| Pausa: pausar, continuar, descartar | `pausarPartida()` / `continuarPausa()` / `descartarPausa()` | 2111 / 2196 / 2183 |
| Sesión compartida: publicar y escuchar | `publicarSesion()` / `escucharSesionCompartida()` | 3186 / 3270 |
| Turnos remotos y saltar turno remoto | `avanzarTurnoRemoto()` / `saltarTurnoRemoto()` / `escribirImposicionRemoto()` | 3679 / 3742 / 3660 |
| Cronómetro | `pintarCrono()` / `iniciarTemporizadorDesde()` | 3103 / 3109 |
| Invitados: QR y agregar a la partida | `abrirQRJuego()` / `agregarInvitadoAPartida()` | 3956 / 4194 |
| Importar acciones | `parsearImportacion()` / `normalizarAccionImport()` | 1665 / 1701 |

---

## `index.html` — 2,893 líneas (pantalla inicial)

**Documento de detalle:** `General/Pantallas.md` y `General/Usuarios.md`

**Vistas:** `vistaMenu` (451) · `vistaJuegos` (490) · `vistaRetos` (496) ·
`vistaCom` (502) · `vistaExp` (523)

| Para... | Función | Línea |
|---|---|---|
| Mostrar el menú y sus dos botones de esquina | `mostrarMenu()` / `verMenu()` | 635 / 1357 |
| Dibujar las tarjetas del catálogo | `tarjetaPack()` / `renderPacks()` / `renderPacksDeVerdad()` | 733 / 769 / 794 |
| Punto del carrito | `actualizarPuntoCarrito()` | 907 |
| Submenús: hash, abrir y cerrar | `hashActual()` / `abrirSegunHash()` / `abrirSub()` / `cerrarSub()` | 1375 / 1379 / 1387 / 1397 |
| Cada submenú | `abrirExp()` / `abrirJuegos()` / `abrirRetos()` / `abrirCom()` | 1404 / 1419 / 1428 / 1448 |
| Engrane: abrir, cerrar, cambiar usuario | `mostrarGear()` / `cerrarGear()` / `abrirCambiarUsu()` | 2497 / 2509 / 2517 |
| Telegram | `pintarTelegram()` | 2585 |
| Usuarios: anatomía y lista | `pintarInvUsuarios()` / `guardarAnatomiaUsuario()` / `abrirEdUsuarios()` | 1510 / 1485 / 2268 |
| Puntos e historial de movimientos | `abrirPuntos()` / `abrirHistorial()` | 1615 / 1652 |
| Propuestas de precios: pintar, abrir, aceptar, rechazar | `pintarPropuestas()` / `abrirPropuestas()` / `aceptarPropuesta()` / `rechazarPropuesta()` | 1972 / 2045 / 2080 / 2132 |
| Invitado: volver solo y escanear QR | `volverSiInvitadoSinPartida()` / `iniciarScan()` | 1175 / 1310 |

---

## `Lenceria/index.html` — 2,742 líneas

**Documento de detalle:** `General/Catalogo-Lenceria.md`

**Vistas:** `vistaPlanes` (204) · `vistaElegir` (218) · `vistaPedido` (241) ·
`vistaConfig` (258) · `vistaClasif` (279) · `vistaPrenda` (296)

| Para... | Función | Línea |
|---|---|---|
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 373 / 398 |
| Cargar todo y escuchar cambios | `cargarTodo()` / `escuchar()` | 2634 / 2346 |
| Cargar prendas, planes y pedidos | `cargarPrendas()` / `cargarPlanes()` / `cargarPedidos()` | 2317 / 2324 / 2331 |
| Configuración: clasificaciones y prendas | `pintarConfig()` / `bloqueClasif()` / `bloquePrendas()` | 930 / 948 / 1114 |
| Clasificación: abrir, pintar, guardar, borrar | `abrirClasif()` / `pintarClasifVista()` / `guardarClasif()` / `borrarClasif()` | 1026 / 1034 / 1059 / 1083 |
| Prenda: tarjeta, abrir, guardar, borrar | `tarjetaPrenda()` / `abrirPrenda()` / `guardarPrenda()` / `borrarPrenda()` | 1168 / 1255 / 1432 / 1491 |
| Fotos: elegir archivo, procesar, lupa | `usarArchivoFoto()` / `procesarFoto()` / `abrirLupa()` | 1396 / 1353 / 1230 |
| Planes: pintar, tarjeta y separador | `pintarPlanes()` / `tarjetaPlan()` / `separadorPlanes()` | 1587 / 1671 / 1572 |
| Orden de la cuadrícula (nunca usadas y referencia) | `ordenPrendas()` / `ordenRef()` / `compararRef()` / `claveRef()` | 820 / 815 / 806 / 800 |
| Referencias: la siguiente libre y corregir vacías o repetidas | `siguienteRef()` / `asegurarRefs()` | 839 / 868 |
| Texto de uso en la tarjeta | `textoUso()` / `diasDesdeUso()` | 785 / 776 |
| Vestidor: elegir y contar | `abrirElegir()` / `pintarVestidor()` / `alternarSeleccion()` / `pintarContador()` | 1865 / 1899 / 1918 / 1964 |
| Guardar plan, fijarlo o borrarlo | `guardarPlan()` / `alternarFijo()` / `borrarPlan()` | 1977 / 2031 / 2040 |
| "Sorpréndeme" | `sorprendeme()` | 2243 |
| Pedidos: proponer, abrir, aceptar, rechazar, cancelar | `mandarPropuesta()` / `abrirPedido()` / `aceptarPedido()` / `rechazarPedido()` / `cancelarPedido()` | 2056 / 2102 / 2143 / 2205 / 2230 |
| Contador de usos | `liquidarUsos()` | 2283 |
| Exportar / importar prendas | `abrirDatos()` / `aplicarImportacion()` | 2400 / 2465 |
| Entrar desde una cita | `aplicarEntradaCita()` | 2648 |

---

## `Encuentros/index.html` — 2,531 líneas

**Documento de detalle:** `General/Pantallas.md` y `General/Pegamento-y-Citas.md`

**Vistas:** `vistaBloqueo` (152) · `vistaLista` (164) · `vistaConfig` (189) ·
`vistaEditar` (197) · `vistaEspera` (210) · `vistaPlayer` (217) · `vistaSeguir` (258)

| Para... | Función | Línea |
|---|---|---|
| Arrancar: normal o directo al juego | `entrar()` / `entrarDirecto()` | 688 / 587 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 990 / 1026 |
| Cargar actividades y pintar la lista | `cargarActividades()` / `pintarLista()` / `dibujarLista()` / `filtrar()` | 1221 / 1380 / 1325 / 1395 |
| Configuración y editor de actividades | `pintarListaCfg()` / `abrirEditor()` / `pintarEditor()` / `guardarEditor()` | 1531 / 1565 / 1583 / 1654 |
| Tomas de una actividad (modal y base) | `abrirTomas()` / `guardarTomasEnBase()` / `cargarTomasDoc()` | 1752 / 1522 / 1489 |
| Armar jugadores y repartir | `construirCabezas()` / `generarListas()` / `repartirRuedaEnc()` / `generarYIniciar()` | 1804 / 1815 / 1850 / 1888 |
| Pintar turno y paso | `pintarTurnoDe()` / `pintarPaso()` | 2053 / 2067 |
| Avanzar local o por sesión | `avanzarLocal()` / `avanzarSesion()` | 835 / 858 |
| Sala de espera | `pintarSala()` | 2002 |
| Invitados: agregar y QR | `agregarInvitado()` / `abrirQRInvitacion()` | 2273 / 2344 |
| Sesión: escuchar, saltar turno, cerrar, fin | `escucharSesion()` / `saltarTurno()` / `cerrarSesion()` / `mostrarFin()` | 763 / 888 / 953 / 983 |
| Entrar al juego siendo invitado | `entrarAlJuego()` | 2456 |

---

## `Guiadas/index.html` — 2,253 líneas

**Documento de detalle:** `General/Pantallas.md` y `General/Pegamento-y-Citas.md`

**Vistas:** `vistaBloqueo` (117) · `vistaLista` (129) · `vistaConfig` (154) ·
`vistaEditar` (162) · `vistaPlayer` (183) · `vistaSeguir` (197)

| Para... | Función | Línea |
|---|---|---|
| Arrancar la página | `entrar()` | 349 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 688 / 722 |
| Cargar actividades y pintar la lista | `cargarActividades()` / `pintarLista()` / `filtrar()` | 947 / 1132 / 821 |
| Jugar directo desde la lista | `jugarDirecto()` | 1147 |
| Arrancar partida y pintar el paso | `empezarNuevo()` / `mostrarPlayer()` / `pintarPaso()` / `pintarTurnoDe()` | 1333 / 1354 / 2060 / 2051 |
| Sesión: avanzar, escuchar, saltar, cerrar, fin | `avanzarSesion()` / `escucharSesion()` / `saltarTurno()` / `cerrarSesion()` / `mostrarFin()` | 541 / 646 / 612 / 594 / 467 |
| Multi: abrir, refrescar, seleccionar, repartir | `multiAbrir()` / `multiRefrescar()` / `multiAbrirSel()` / `repartirRuedaGuia()` | 1500 / 1469 / 1526 / 1650 |
| Editor de actividades | `abrirEditor()` / `pintarEditor()` / `guardar()` | 1740 / 1761 / 1832 |
| Exportar o pegar una actividad | `exportarActividad()` / `pegarActividad()` | 1994 / 1899 |
| Tomas de la actividad | `abrirTomasGuia()` / `guardarProg()` / `cargarTomasDoc()` | 1222 / 1275 / 1697 |
| Seguir jugando después de recargar | `seguirEncima()` / `seguirFuera()` | 1201 / 1208 |

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

## `Opciones/index.html` — 1,655 líneas

**Documento de detalle:** `General/Opciones.md`

**Vistas:** `vistaBloqueo` (162) · `vistaInicio` (174) · `vistaEspera` (202) ·
`vistaPlayer` (209) · `vistaConfig` (246) · `vistaSeguir` (268)

| Para... | Función | Línea |
|---|---|---|
| Arrancar: normal o directo | `entrar()` / `entrarDirecto()` | 597 / 536 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 1499 / 1526 |
| Cargar, guardar y repartir opciones | `cargarOpciones()` / `guardarOpciones()` / `repartirOpciones()` | 503 / 515 / 1167 |
| Quiénes juegan y de qué lado | `construirCabezas()` / `construirCabezasModo()` | 489 / 1160 |
| Arrancar la partida | `iniciar()` | 1190 |
| Pintar inicio, sala y paso | `pintarInicio()` / `pintarSala()` / `pintarPaso()` | 653 / 904 / 951 |
| Turnos y elección | `iniciarEstado()` / `siguienteTurno()` / `aplicarPick()` / `pickSesion()` | 550 / 564 / 578 / 795 |
| Sesión: escuchar, saltar, cerrar, fin | `escucharSesion()` / `saltarTurno()` / `cerrarSesion()` / `finPartida()` | 744 / 818 / 871 / 1036 |
| Invitados: agregar y QR | `agregarInvitado()` / `abrirQR()` | 1089 / 1134 |
| Invitado: entrar o continuar | `entrarAlJuego()` / `continuarPartida()` | 1325 / 1294 |
| Configuración: pintar y abrir | `pintarCfg()` / `abrirCfg()` | 1418 / 1482 |
| Agregar o editar opciones | `agregarOpcion()` / `guardarEdit()` / `agregarDesdeInput()` | 1411 / 1434 / 1460 |
| Seguir después de recargar | `seguirEncima()` | 1268 |

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
abrirAgregar(2658) · abrirCfg(5069) · abrirDetalle(4551) · abrirFin(2490)
abrirGaleria(1459) · abrirMeterInvitado(2868) · abrirModal(4120) · abrirModalDuelo(1616)
abrirModalImagen(2112) · abrirQR(2942) · abrirSeleccionCompartida(3687)
abrirSeleccionDueloCompartida(3514) · abrirSeleccionDueloLocal(3497)
abrirSeleccionLocal(3672) · abrirVentanaEspecial(1674) · actualizarFotos(4873)
actualizarTextoEstadoCarta(2106) · adminDe(2976) · agregarDesdeInput(4327)
agregarEspecial(4318) · agregarInvitado(2737) · agregarPersonaje(4307)
anunciarInvitacion(1957) · armando(2024) · arrancarSeleccion(3728) · asegurarOficiales(1135)
asegurarPersonajes(1183) · avanzarDueloJuntosLocal(2521) · avanzarTarjeta(1361)
avisoJSONMalo(4219) · avisosCorrespondencia(4488) · bajarArchivo(4820)
baseConfigurada(4811) · borrarDetalle(4594) · buscarPersonaje(1240) · cabezas(2019)
cabs(2809) · cambiarMarca(3646) · cambiarMarcaDuelo(3413) · cargarEstado(1734)
cargarIdentidad(993) · cargarOficiales(1121) · cargarPersonajes(1164) · cerrarDetalle(4569)
cerrarModal(4137) · cerrarModalImagen(2120) · cerrarSesion(1972)
chequearPartidaEspera(1800) · claveCfg(4158) · confirmarArranqueDuelo(3309)
conPendiente(3942) · construirCabezas(1024) · construirCabezasModo(2969)
continuarPartida(3968) · continuarPartidaLocal(3991) · contraDeRonda(2720)
contraparteDe(1266) · deck(2787) · deshacerFotos(4978) · disponiblesInvitados(2654)
dueloEsJuntos(2698) · dueloLadoDePartida(2688) · dueloMismoLadoDePartida(1235)
dueloModalidadDePartida(2693) · elegirAzarDuelo(3436) · elegirAzarSeleccion(3452)
elegirTentacion(3476) · enEspera(2031) · entrar(1372) · entrarAlJuego(4026)
entrarDirecto(1332) · esAnfitrion(1979) · esClaveLista(4162) · escucharAprobacion(963)
escucharGrupo(5208) · escucharSeleccion(3775) · escucharSesion(1824) · esDueloJuntos(2746)
esModoDuelo(2685) · esOficial(1117) · especialDe(1763) · especialDeLado(2211)
especialK(1638) · especialPendido(1637) · exportarFotos(4835) · exportarLista(4772)
fechaCorta(4815) · filaPersonaje(4385) · filaVariante(4352) · filtro(4448)
finPartida(2497) · guardarDetalle(4570) · guardarEdit(4359) · guardarLocalGuardada(925)
guardarPersonajes(1187) · hostNombre(3528) · idLibre(4178) · indexarPersonajes(1052)
iniciar(3097) · iniciarEstado(1338) · irAlMenu(5109) · lado(2726) · ladoAnatomiaCfg(4154)
ladoDeCabeza(2700) · ladoDuelo(2770) · ladoOriginal(2728) · leerJSONPegado(4196)
leerLocalGuardada(939) · leerQuienSoy(990) · leerSnapshotFotos(4862) · licMsg(982)
limpiarFiltro(4169) · limpiarFiltroSel(3281) · limpiarLocalGuardada(949)
limpiarParaArchivo(4758) · listaDeCabezaPara(2999) · listaDeLado(1216) · listaSegura(1073)
llenar(2036) · llenarSelectPar(4532) · marcas(2894) · meterInvitado(2889) · mezclar(877)
miLado(4155) · mismoContenidoPersonaje(1092) · mismosLados(2973) · modalAbierto(5132)
modalidad(3072) · modoAdmiteInvitados(1985) · modoBaseDePartida(2679)
mostrarBotonesAdmin(1986) · mostrarCaraDuelo(2305) · mostrarGracia(953) · nombreAdmin(1010)
nombreArchivoExport(4767) · nombreCabeza(1020) · nombreDeLado(4156) · nombreDeLista(4163)
nombreHostSeleccion(3291) · nombreLado(1016) · nombres(1817) · normSel(3278)
ordenPersonajes(1142) · otroLado(4487) · otroLadoDuelo(1228) · parejaAcepto(3301)
parejaAEsperar(3297) · pares(2723) · paresDisponibles(1281) · parsePegadoPersonajes(4234)
parsePegadoTextos(4261) · pedirCartasInvitado(2831) · pegarLista(4620) · personajeDe(4286)
personajesRef(910) · pintarAvisosCfg(4509) · pintarBotonDeshacerFotos(4868)
pintarCaraDuelo(2218) · pintarCfg(4409) · pintarDueloPar(2277) · pintarDueloTentacion(2291)
pintarEspecial(1646) · pintarFaseDuelo(2071) · pintarFoto(2170) · pintarFotoEn(2138)
pintarFotoGaleria(1478) · pintarGaleria(1490) · pintarInicio(1548)
pintarMeterInvitado(2877) · pintarModalDuelo(1600) · pintarModo(1558)
pintarModoPartida(2707) · pintarPaso(2395) · pintarPasoDueloJuntos(2319) · pintarSala(2010)
pintarSalidas(1003) · pintarSeleccion(3552) · pintarSeleccionDuelo(3321)
pintarTarjeta(2171) · pintarVolteo(2080) · ponerBadgeOficial(1150)
ponerSinFotoGaleria(1470) · poolsDuelo(1295) · poolsEspejoMismo(2982) · preparar(3039)
prepararDuelo(3070) · probar(4198) · puedeVerOtroLado(4151) · quienes(2713)
recalcularOficiales(1098) · reiniciarVariantes(1710) · repartirEspeciales(1720)
repartirTarjetas(3010) · resetCarta(2127) · retirarInvitadosDeLaPartida(914)
revisarEspecial(3086) · ronda(2742) · salirAlMenu(5119) · salirModoInvitado(4091)
saltarTurno(1906) · sanearSesion(1767) · seguirEncima(3931) · seguirFuera(3936)
seleccionRef(3254) · selEsCompartida(3255) · selFuente(3257) · selMarcosDe(3258)
selPoolDe(3261) · selTodosListos(3272) · sesionRef(911) · siguienteDueloJuntos(2538)
siguienteSesion(1879) · siguienteTurno(1346) · sinDuplicados(885) · soyCabeza(1336)
textoPersonaje(1087) · traePar(4615) · url(2140) · ver(5089) · vistaDeInicio(5101)
voltear(2079) · voltearDuelo(2312) · yaExiste(4172)
```

### `Castigos\index.html`

```
abortarPlacer(2605) · abrirDetalle(1569) · abrirEditor(1347) · abrirQRJuego(3956)
accesorioEnUso(1829) · accionDeNivel(2776) · accionesModeloPorRonda(4113)
accionVacia(1381) · actualizar(2498) · actualizarBotonJugar(1493) · actualizarInicio(2301)
agregar(1459) · agregarInvitadoAPartida(4194) · agregarInvitadoLocal(4179)
ajustarAltoCampo(1391) · anunciarinvitacion(3251) · armando(3418)
armarBolsasImposicion(2746) · armarPartidaNormal(2616) · asignarImposicionesAlAzar(2757)
avanzarSaltadoRemoto(3711) · avanzarTurnoNoSaltado(3140) · avanzarTurnoRemoto(3679)
bolsasEnMemoria(4021) · bolsasParaInvitado(4055) · borrarAcceso(1811) · borrarAccion(1516)
borrarCastigo(1329) · borrarImp(1898) · cargarAccesorios(811) · cargarCastigos(775)
cargarDatosCastigo(1908) · cargarIdentidad(715) · cargarImposiciones(824)
cargarSesionEnMemoria(3342) · cargarTodo(767) · cerrar(2169) · chequearConexion(4281)
chequearPartidaEspera(3391) · clave(4100) · colorAccion(3563) · conGente(3414)
construirNivelesOficial(850) · contarAccionesCastigos(1953) · continuarPausa(2196)
continuarSeleccionCastigo(2247) · controlesAnfitrionVisible(3498)
crearSesionCompartida(3243) · descartarPausa(2183) · descripcionPausa(2158) · destino(1203)
elegirAccionInvitado(4096) · elegirCastigoParaJugar(2624) · elegirModo(2341)
enEspera(3422) · enfocarAccion(1481) · enJuego(1042) · entrar(4287)
entrarAlJuegoCompartida(3379) · escribirImposicionRemoto(3660) · escucharGrupo(734)
escucharSesionCompartida(3270) · esSoloPuro(3499) · estadoPartidaLocal(2038)
esUnCelular(3573) · etiquetaLados(759) · filtro(1268) · finVisible(1036) · fraseAccion(3513)
gastarCortesiasCastigo(2283) · generarJugadores(2724) · generarTurnos(2784)
generarTurnosMulti(2985) · guardarCastigoDatos(1599) · guardarImposiciones(1905)
idVigente(651) · iniciarPartida(3146) · iniciarPartidaMulti(2877)
iniciarTemporizadorDesde(3109) · irAlMenu(1129) · ladoDe(4115) · ladoInv(4182)
ladosParticipantes(2573) · leerNivelesCastigo(4028) · leerPausa(2126) · leerQuienSoy(711)
llenar(3426) · mezclar(1382) · modalAbierto(1150) · modalBasePaso(1078)
mostrarBotonAccion(3089) · mostrarFin(3457) · mostrarGracia(1103) · mostrarModalBase(1096)
mostrarPanel(1246) · msg(1242) · msgTomas(1243) · nivel(4152) · nombreDeLado(755)
normalizaAcc(1523) · normalizarAccionImport(1701) · normalizarAccionOficial(838)
normalizarNivelesPlacer(2543) · normTxt(4019) · overlayReinstalar(977)
pararTemporizador(3085) · parsearImportacion(1665) · partes(4257) · partes2(4267)
pausarPartida(2111) · pintarAccesorios(1743) · pintarAccesoriosDetalle(1525)
pintarCastigos(1264) · pintarCrono(3103) · pintarEditor(1396) · pintarImposiciones(1866)
pintarListaInicio(1970) · pintarSala(3411) · pintarSalidas(1040) · pintarTomas(1501)
pintarTomasJugar(2659) · pintarTomasJugarMulti(2673) · pintarTurno(3528)
placerAccionesEnNiveles(2582) · placerAlcanzaMulti(2595) · placerAlcanzaNormal(2591)
poolDeAcciones(4076) · preguntarImposicionesPor3(2489) · preguntarNivelesPlacer(2549)
preguntarPausa(2165) · preguntarQuienCastiga(2330) · promptTexto(1932)
publicarSesion(3186) · puedeJugarCastigo(2277) · quitarAccesorioDeTodas(1845)
reanudarCronoRemotoSiHaceFalta(3130) · recalcularSaltadoPorRevivir(3075)
refrescarUsuarios(728) · reinstalarOficialDesdeUrl(990) · renombrarAcceso(1777)
renombrarCastigo(1313) · repararOficialCastigo(939) · repartirRueda(2940)
resetearInicioMulti(3902) · restaurarPartidaLocal(2069) · retirarInvitadosDeLaPartida(2718)
salirAlMenu(1139) · salirModoInvitado(3930) · saltado(2860) · saltarTurnoRemoto(3742)
seleccionarCastigo(2237) · sesionRef(2713) · setHowTabs(2365) · setModTabs(2358)
setTipoTabs(2387) · sincronizarOficialesCastigos(867) · soyCabeza(3388)
tieneAcciones(4050) · toggleMulti(2394) · tomarImposicion(2749) · totalAccionesDatos(935)
totalAccionesEditor(1486) · turnosConInvitado(4133) · vaciaDatos(1376) · vale(4101)
ver(1050) · vistaActual(1032) · volverConHistorial(1114) · volverDePartida(3919)
volverTiendaReinstalar(966)
```

### `index.html`

```
abrirCambiarUsu(2517) · abrirCom(1448) · abrirEdUsuarios(2268) · abrirExp(1404)
abrirHistorial(1652) · abrirJuegos(1419) · abrirPanelUsuarios(2693) · abrirPropuestas(2045)
abrirPuntos(1615) · abrirRetos(1428) · abrirSegunHash(1379) · abrirSub(1387)
aceptarPropuesta(2080) · actualizarAvisoPropuestas(1892) · actualizarPuntoCarrito(907)
adminId(1088) · agregarFila(1016) · aplicar(1277) · armarFilas(1011)
cancelarPropuesta(2155) · cerrar(2237) · cerrarCom(1454) · cerrarEdUsuarios(2352)
cerrarExp(1413) · cerrarGear(2509) · cerrarHistorial(1707) · cerrarJuegos(1425)
cerrarOverlaysInv(2487) · cerrarPropuestas(2054) · cerrarPuntos(1634) · cerrarRetos(1436)
cerrarSub(1397) · conTiempo(582) · crearFilaProp(1938) · detenerScan(1206)
detenerScanInv(2746) · entrar(1115) · etiqueta(1262) · etiquetaAnatomia(1479)
etiquetaProp(1969) · formatearFechaMov(1643) · guardarAnatomiaUsuario(1485)
hashActual(1375) · hashTexto(2216) · iconoMenu(611) · iniciar(1138)
iniciarPropuestas(1918) · iniciarScan(1310) · invModoScan(2524) · invMsg(1462)
invRefrescar(1467) · invVer(2447) · irPaso3(996) · lado(1482) · leerGuardado(606)
mostrarGear(2497) · mostrarIdentidad(924) · mostrarMenu(635) · msg(577) · msgQR(1212)
nombreParejaMenu(782) · normalizaNombre(2822) · overlayInvAbierto(2484) · overlaysInv(2481)
parsearFB(589) · pedirPin(2226) · pintarInvUsuarios(1510) · pintarPropuestas(1972)
pintarTelegram(2585) · ponerZoom(1229) · probar(1270) · propuestasAbiertas(1934)
propuestasMiasPendientes(1866) · propuestasParaMi(1860) · propuestasResultadosNuevos(1872)
propuestasResultadosVisibles(1880) · ptsRaw(2364) · quitarZoom(1219) · recargar(942)
rechazarPropuesta(2132) · renderPacks(769) · renderPacksDeVerdad(794)
renumerarRadios(1068) · resolverTodasPropuestas(2178) · salirSinHaberEntrado(2535)
tarjetaPack(733) · textoDestinoProp(1853) · textoValorProp(1742) · tgApi(2602)
tgEstado(2580) · tgGuardado(2566) · tgTarjeta(2573) · titulo(1986) · todos(2277)
usuariosEfectivos(964) · valorEfectivoProp(1727) · valorPropValido(1734) · verHist(1558)
verMenu(1357) · verPaso(600) · volverSiInvitadoSinPartida(1175)
```

### `Lenceria\index.html`

```
abrirClasif(1026) · abrirDatos(2400) · abrirElegir(1865) · abrirLupa(1230)
abrirPedido(2102) · abrirPrenda(1255) · aceptarPedido(2143) · agregarClasif(1008)
alternarFijo(2031) · alternarSeleccion(1918) · aplicarEntradaCita(2648)
aplicarImportacion(2465) · arrancar(2702) · asegurarRefs(868) · bloqueClasif(948)
bloquePrendas(1114) · borrarClasif(1083) · borrarPlan(2040) · borrarPrenda(1491)
botonPasados(1579) · cancelarPedido(2230) · cargarClasificaciones(732) · cargarPedidos(2331)
cargarPlanes(2324) · cargarPrendas(2317) · cargarTodo(2634) · cerrarLupa(1236)
claveRef(800) · compararRef(806) · construirFiltros(582) · conTiempo(2627)
desplegableFiltro(629) · diasDesdeUso(776) · escribirAviso(2093) · escuchar(2346)
esMia(1597) · extra(704) · fechaAObjeto(521) · fechaDeUso(764) · fechaLarga(526)
guardarClasif(1059) · guardarPlan(1977) · guardarPrenda(1432) · hoyTexto(515)
idDeLado(1109) · irAlMenu(391) · lado(2513) · ladoDePersona(482) · leerImagen(1334)
limpiarFiltros(570) · limpiarPedidosVencidos(1831) · liquidarUsos(2283) · llenarSelect(1244)
mandarPropuesta(2056) · miniatura(1728) · mismoConjunto(2137) · modalAbierto(410)
mostrarFoto(1311) · nombreDe(908) · nombreLado(474) · nombrePersona(478) · normTexto(534)
ordenarClasif(749) · ordenPrendas(820) · ordenRef(815) · pasaFiltro(574)
pedidoVencido(1745) · pintarClasifVista(1034) · pintarConfig(930) · pintarContador(1964)
pintarPedido(2126) · pintarPlanes(1587) · pintarVestidor(1899) · planDePersona(508)
planesDe(1561) · planesDePersona(492) · planesDePersonaPorFecha(505) · planesPorFecha(496)
pref(2657) · prendaEnUsoFuturo(1326) · prendasDeLado(1105) · prendasDePersona(488)
procesarFoto(1353) · quedan(1514) · rechazarPedido(2205) · salirAlMenu(398)
sembrarClasificaciones(659) · separadorPlanes(1572) · siguienteRef(839) · sorprendeme(2243)
tarjetaPedidoEnviado(1799) · tarjetaPedidoRecibido(1750) · tarjetaPlan(1671)
tarjetaPrenda(1168) · textoUso(785) · tipoCubreTodo(832) · tsUso(771)
usarArchivoFoto(1396) · usoDe(913) · valor(756) · ver(373)
```

### `Encuentros\index.html`

```
abrirAgregar(2251) · abrirEditor(1565) · abrirModal(1726) · abrirQRInvitacion(2344)
abrirTomas(1752) · acts(1798) · agregar(1612) · agregarInvitado(2273) · agregarItemEd(1659)
anunciarInvitacion(936) · armando(2009) · avanzarLocal(835) · avanzarSesion(858)
avisarCortesia(1316) · base(2203) · cab(662) · cabezas(2324) · cabs(2016)
cargarActividades(1221) · cargarActsParaInvitado(2152) · cargarEnMemoria(591)
cargarIdentidad(520) · cargarTomasDoc(1489) · cerrarModal(1746) · cerrarSesion(953)
cerrarTomas(1782) · chequearPartidaEspera(739) · chequearPendiente(647) · companero(2284)
compararActividades(1283) · construirCabezas(1804) · contarNivel(394) · dibujarLista(1325)
disponiblesInvitados(2247) · docDe(1120) · elegirAccionEnc(2186) · enEspera(2021)
entrar(688) · entrarAlJuego(2456) · entrarDirecto(587) · esAnfitrion(1983)
escucharAprobacion(479) · escucharGrupo(2478) · escucharSesion(763) · etiquetaLados(1468)
filtrar(1395) · gastarCortesias(1291) · generarListas(1815) · generarYIniciar(1888)
guardadas(1758) · guardarEditor(1654) · guardarTomasEnBase(1522) · iniciarSingle(672)
irAlMenu(1016) · item(2109) · leerQuienSoy(517) · leerTomasEd(1681) · licMsg(509)
limpiarInvitadosDeSesionAnterior(970) · listaConInvitado(2202) · llenar(2026) · mezclar(399)
migrarTomasDeEsteCelular(1504) · modalAbierto(1040) · mostrarBotonesAdmin(1984)
mostrarFin(983) · mostrarGracia(415) · multiRefrescar(1406) · multiToggle(1416)
nivel(2227) · nivelPorNombre(2148) · nombreAdmin(543) · nombreCabeza(640) · nombreLado(1464)
nombres(756) · normLados(389) · normOrdenAct(1280) · normTomasEnc(1479) · normTxtEnc(2146)
ofs(1124) · overlayReinstalar(1165) · pintarEditor(1583) · pintarLista(1380)
pintarListaCfg(1531) · pintarPaso(2067) · pintarSala(2002) · pintarSalidas(535)
pintarTurnoDe(2053) · poolDeAccionesEnc(2167) · puedeJugarActividad(1310)
quiereCompartido(1951) · quitarItemEd(1672) · reinstalarOficialDesdeUrl(1178)
repartirRuedaEnc(1850) · retirarInvitadosDeLaPartida(964) · salirAlMenu(1026)
salirModoInvitado(442) · saltarTurno(888) · sanearSesion(611) · seguirEncima(2402)
seguirFuera(2407) · sesionRef(549) · sincronizarOficiales(1122) · soyCabeza(603)
tomasGuardadasEd(1527) · ultimo(2117) · vale(2190) · ver(990) · volverTiendaReinstalar(1154)
```

### `Guiadas\index.html`

```
abrirEditor(1740) · abrirFin(473) · abrirTomasGuia(1222) · agregar(1790) · agregarItem(1837)
aplicaSesion(638) · armarListaLados(1311) · asignarParaId(1299) · avanzarSesion(541)
avisarCortesia(1042) · borrarProg(1282) · cargarActividades(947) · cargarIdentidad(486)
cargarTomasDoc(1697) · cerrarSesion(594) · cerrarTomasGuia(1247) · claveDoc(837)
compararActividades(1009) · contarNivel(325) · dibujarLista(1051) · docDe(844)
editorTieneAlgo(1896) · empezarNuevo(1333) · entrar(349) · esAdmin(501)
escucharAprobacion(411) · escucharSesion(646) · etiquetaLados(529) · exportarActividad(1994)
filtrar(821) · gastarCortesias(1017) · guardar(1832) · guardarProg(1275)
guardarTomasEnBase(1730) · iniciarSesionCompartida(560) · irAlMenu(712)
jugadoresBase(1285) · jugarDirecto(1147) · leerJSONPegado(1883) · leerProg(1211)
leerQuienSoy(483) · leerTomas(1859) · licMsg(393) · limpiarParaArchivo(1977)
marcarRadio(537) · mensajeEditor(1873) · mezclar(829) · migrarTomasDeEsteCelular(1712)
miIdSesion(535) · mismoPaso(520) · modalAbierto(739) · modalBasePaso(1442) · mostrarFin(467)
mostrarGracia(340) · mostrarModalBase(1460) · mostrarPlayer(1354) · multiAbrir(1500)
multiAbrirSel(1526) · multiMostrar(1466) · multiRefrescar(1469) · multiSalir(1534)
multiToggle(1479) · nombreAdmin(502) · nombreDe(507) · nombreDePaso(512) · nombreLado(525)
normLados(312) · normOrdenAct(1006) · normTomas(317) · ofs(850) · overlayReinstalar(891)
pegarActividad(1899) · pintarEditor(1761) · pintarLista(1132) · pintarPaso(2060)
pintarTurnoDe(2051) · probar(1885) · puedeJugarActividad(1036) · quienes(1519)
quitarItem(1850) · refrescarMiLado(494) · reinstalarOficialDesdeUrl(904)
repartirRuedaGuia(1650) · salirAlMenu(722) · saltarTurno(612) · seguirEncima(1201)
seguirFuera(1208) · sesionPausada(600) · sesionRef(536) · sincronizarOficiales(848)
tomasDePantalla(1985) · tomasGuardadas(1735) · top(1054) · ver(688)
volverTiendaReinstalar(880)
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
abrirAgregar(1070) · abrirCfg(1482) · abrirFin(1029) · abrirModal(1386) · abrirQR(1134)
agregarDesdeInput(1460) · agregarInvitado(1089) · agregarOpcion(1411)
anunciarInvitacion(856) · aplicarPick(578) · armando(918) · cabezas(913) · cabs(1117)
cargarEstado(672) · cargarIdentidad(458) · cargarOpciones(503) · cerrarModal(1403)
cerrarSesion(871) · chequearPartidaEspera(720) · conPendiente(1278) · construirCabezas(489)
construirCabezasModo(1160) · continuarPartida(1294) · disponiblesInvitados(1066)
enEspera(925) · entrar(597) · entrarAlJuego(1325) · entrarDirecto(536) · esAnfitrion(878)
escucharAprobacion(428) · escucharGrupo(1608) · escucharSesion(744) · filtro(1425)
finPartida(1036) · fuente(1096) · guardarEdit(1434) · guardarOpciones(515) · iniciar(1190)
iniciarEstado(550) · irAlMenu(1516) · leerQuienSoy(455) · licMsg(447) · llenar(930)
mezclar(368) · modalAbierto(1539) · modoAdmiteInvitados(884) · mostrarBotonesAdmin(885)
mostrarGracia(418) · nombreAdmin(475) · nombreCabeza(485) · nombreLado(481) · nombres(737)
opcionesRef(409) · parDe(542) · parseLista(390) · pick(1043) · pickSesion(795)
pintarCfg(1418) · pintarInicio(653) · pintarPaso(951) · pintarSala(904) · pintarSalidas(468)
quiereCompartido(1211) · quitar(581) · repartirOpciones(1167) · restantes(994)
retirarInvitadosDeLaPartida(413) · ronda(1093) · rondaActual(995) · salirAlMenu(1526)
salirModoInvitado(1356) · saltarTurno(818) · sanearSesion(687) · seguirEncima(1268)
seguirFuera(1273) · sesionRef(410) · siguienteTurno(564) · sinDuplicados(376)
soyCabeza(540) · ver(1499)
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

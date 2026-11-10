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

## `Roles/index.html` — 4,833 líneas

**Documento de detalle:** `General/Roles.md`

**Vistas:** `vistaBloqueo` (380) · `vistaInicio` (392) · `vistaSeleccion` (457) ·
`vistaEspera` (490) · `vistaPlayer` (497) · `vistaConfig` (584) · `vistaSeguir` (674)

| Para... | Función | Línea |
|---|---|---|
| Arrancar la página: identidad, licencia y estado guardado | `entrar()` | 1305 |
| Cambiar de vista y guardar el paso del historial | `ver()` | 4668 |
| Volver al menú deshaciendo los pasos | `salirAlMenu()` | 4698 |
| Pintar la tarjeta de inicio (modo y "Jugar") | `pintarInicio()` | 1386 |
| Pantalla de modo (Clásico, Cambia de Bando, Seleccionar, Duelo) | `pintarModo()` | 1391 |
| Modal del duelo | `pintarModalDuelo()` / `abrirModalDuelo()` | 1431 / 1447 |
| Quiénes juegan y de qué lado | `construirCabezas()` | 957 |
| Pool de personajes: cargar, sembrar, guardar | `cargarPersonajes()` / `asegurarPersonajes()` / `guardarPersonajes()` | 1097 / 1116 / 1120 |
| Buscar personaje o su contraparte | `buscarPersonaje()` / `contraparteDe()` | 1173 / 1199 |
| Repartir tarjetas y preparar la partida | `repartirTarjetas()` / `preparar()` / `prepararDuelo()` | 2841 / 2870 / 2901 |
| Arrancar la partida normal | `iniciar()` | 2928 |
| Modo Seleccionar: pintar, abrir y arrancar | `pintarSeleccion()` / `abrirSeleccionLocal()` / `abrirSeleccionCompartida()` / `arrancarSeleccion()` | 3383 / 3503 / 3518 / 3559 |
| Escuchar la selección compartida | `escucharSeleccion()` | 3606 |
| Sala de espera (anfitrión e invitado) | `pintarSala()` | 1841 |
| Pintar la partida: tarjeta, paso, duelo | `pintarTarjeta()` / `pintarPaso()` / `pintarCaraDuelo()` / `pintarPasoDueloJuntos()` | 2002 / 2226 / 2049 / 2150 |
| Pasar turno o saltarlo | `siguienteTurno()` / `avanzarTarjeta()` / `siguienteSesion()` / `saltarTurno()` | 1279 / 1294 / 1710 / 1737 |
| Terminar la partida | `abrirFin()` / `finPartida()` | 2321 / 2328 |
| Sesión multijugador | `escucharSesion()` | 1655 |
| Configuración: pintar, abrir, filas y editor | `pintarCfg()` / `abrirCfg()` / `filaPersonaje()` / `agregarPersonaje()` | 4240 / 4648 / 4216 / 4138 |
| Exportar la lista de personajes | `exportarLista()` | 4603 |
| Invitado: entrar, continuar, salir | `entrarAlJuego()` / `continuarPartida()` / `salirModoInvitado()` | 3857 / 3799 / 3922 |
| QR de invitación | `abrirQR()` | 2773 |
| Modales chicos | `abrirModal()` / `cerrarModal()` | 3951 / 3968 |

---

## `Castigos/index.html` — 4,362 líneas

**Documento de detalle:** `General/Castigos.md`

**Vistas:** `vistaInicio` (249) · `vistaBloqueo` (307) · `vistaTomas` (314) ·
`vistaPartida` (335) · `vistaEspera` (408) · `vistaConfig` (494) · `vistaEditar` (537)

| Para... | Función | Línea |
|---|---|---|
| Cargar todo: identidad, castigos, accesorios, imposiciones, usuarios | `cargarTodo()` | 767 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 1049 / 1138 |
| Panel de configuración | `mostrarPanel()` | 1245 |
| Lista y edición de castigos | `pintarCastigos()` / `abrirEditor()` / `pintarEditor()` / `guardarCastigoDatos()` | 1263 / 1346 / 1395 / 1598 |
| Tomas de cada castigo | `pintarTomas()` | 1500 |
| Accesorios e imposiciones | `pintarAccesorios()` / `pintarImposiciones()` | 1742 / 1865 |
| Pantalla de inicio y castigo elegido | `pintarListaInicio()` / `seleccionarCastigo()` / `actualizarInicio()` | 1969 / 2236 / 2290 |
| Pasos antes de jugar: quién castiga, modo, multi, imposiciones, placer | `preguntarQuienCastiga()` / `elegirModo()` / `toggleMulti()` / `preguntarImposicionesPor3()` / `preguntarNivelesPlacer()` | 2319 / 2330 / 2383 / 2472 / 2532 |
| Armar y arrancar: normal y multi | `armarPartidaNormal()` / `iniciarPartida()` / `iniciarPartidaMulti()` | 2599 / 3123 / 2860 |
| Repartir turnos y rueda | `repartirRueda()` / `generarTurnos()` / `generarTurnosMulti()` | 2917 / 2767 / 2962 |
| Pintar turno, sala y fin | `pintarTurno()` / `pintarSala()` / `mostrarFin()` | 3501 / 3384 / 3430 |
| Pausa: pausar, continuar, descartar | `pausarPartida()` / `continuarPausa()` / `descartarPausa()` | 2110 / 2195 / 2182 |
| Sesión compartida: publicar y escuchar | `publicarSesion()` / `escucharSesionCompartida()` | 3159 / 3243 |
| Turnos remotos y saltar turno remoto | `avanzarTurnoRemoto()` / `saltarTurnoRemoto()` / `escribirImposicionRemoto()` | 3652 / 3715 / 3633 |
| Cronómetro | `pintarCrono()` / `iniciarTemporizadorDesde()` | 3080 / 3086 |
| Invitados: QR y agregar a la partida | `abrirQRJuego()` / `agregarInvitadoAPartida()` | 3929 / 4167 |
| Importar acciones | `parsearImportacion()` / `normalizarAccionImport()` | 1664 / 1700 |

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

## `Encuentros/index.html` — 2,504 líneas

**Documento de detalle:** `General/Pantallas.md` y `General/Pegamento-y-Citas.md`

**Vistas:** `vistaBloqueo` (152) · `vistaLista` (164) · `vistaConfig` (189) ·
`vistaEditar` (197) · `vistaEspera` (210) · `vistaPlayer` (217) · `vistaSeguir` (258)

| Para... | Función | Línea |
|---|---|---|
| Arrancar: normal o directo al juego | `entrar()` / `entrarDirecto()` | 684 / 587 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 986 / 1022 |
| Cargar actividades y pintar la lista | `cargarActividades()` / `pintarLista()` / `dibujarLista()` / `filtrar()` | 1217 / 1369 / 1314 / 1384 |
| Configuración y editor de actividades | `pintarListaCfg()` / `abrirEditor()` / `pintarEditor()` / `guardarEditor()` | 1514 / 1548 / 1566 / 1637 |
| Tomas de una actividad (modal y base) | `abrirTomas()` / `guardarTomasEnBase()` / `cargarTomasDoc()` | 1731 / 1505 / 1472 |
| Armar jugadores y repartir | `construirCabezas()` / `generarListas()` / `repartirRuedaEnc()` / `generarYIniciar()` | 1783 / 1794 / 1829 / 1867 |
| Pintar turno y paso | `pintarTurnoDe()` / `pintarPaso()` | 2026 / 2040 |
| Avanzar local o por sesión | `avanzarLocal()` / `avanzarSesion()` | 831 / 854 |
| Sala de espera | `pintarSala()` | 1975 |
| Invitados: agregar y QR | `agregarInvitado()` / `abrirQRInvitacion()` | 2246 / 2317 |
| Sesión: escuchar, saltar turno, cerrar, fin | `escucharSesion()` / `saltarTurno()` / `cerrarSesion()` / `mostrarFin()` | 759 / 884 / 949 / 979 |
| Entrar al juego siendo invitado | `entrarAlJuego()` | 2429 |

---

## `Guiadas/index.html` — 2,219 líneas

**Documento de detalle:** `General/Pantallas.md` y `General/Pegamento-y-Citas.md`

**Vistas:** `vistaBloqueo` (117) · `vistaLista` (129) · `vistaConfig` (154) ·
`vistaEditar` (162) · `vistaPlayer` (183) · `vistaSeguir` (197)

| Para... | Función | Línea |
|---|---|---|
| Arrancar la página | `entrar()` | 349 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 688 / 722 |
| Cargar actividades y pintar la lista | `cargarActividades()` / `pintarLista()` / `filtrar()` | 947 / 1125 / 821 |
| Jugar directo desde la lista | `jugarDirecto()` | 1140 |
| Arrancar partida y pintar el paso | `empezarNuevo()` / `mostrarPlayer()` / `pintarPaso()` / `pintarTurnoDe()` | 1322 / 1339 / 2026 / 2017 |
| Sesión: avanzar, escuchar, saltar, cerrar, fin | `avanzarSesion()` / `escucharSesion()` / `saltarTurno()` / `cerrarSesion()` / `mostrarFin()` | 541 / 646 / 612 / 594 / 467 |
| Multi: abrir, refrescar, seleccionar, repartir | `multiAbrir()` / `multiRefrescar()` / `multiAbrirSel()` / `repartirRuedaGuia()` | 1479 / 1454 / 1505 / 1622 |
| Editor de actividades | `abrirEditor()` / `pintarEditor()` / `guardar()` | 1712 / 1733 / 1804 |
| Exportar o pegar una actividad | `exportarActividad()` / `pegarActividad()` | 1966 / 1871 |
| Tomas de la actividad | `abrirTomasGuia()` / `guardarProg()` / `cargarTomasDoc()` | 1211 / 1264 / 1669 |
| Seguir jugando después de recargar | `seguirEncima()` / `seguirFuera()` | 1190 / 1197 |

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
abrirAgregar(2489) · abrirCfg(4648) · abrirDetalle(4382) · abrirFin(2321)
abrirMeterInvitado(2699) · abrirModal(3951) · abrirModalDuelo(1447) · abrirModalImagen(1943)
abrirQR(2773) · abrirSeleccionCompartida(3518) · abrirSeleccionDueloCompartida(3345)
abrirSeleccionDueloLocal(3328) · abrirSeleccionLocal(3503) · abrirVentanaEspecial(1505)
actualizarTextoEstadoCarta(1937) · adminDe(2807) · agregarDesdeInput(4158)
agregarEspecial(4149) · agregarInvitado(2568) · agregarPersonaje(4138)
anunciarInvitacion(1788) · armando(1855) · arrancarSeleccion(3559) · asegurarOficiales(1068)
asegurarPersonajes(1116) · avanzarDueloJuntosLocal(2352) · avanzarTarjeta(1294)
avisoJSONMalo(4050) · avisosCorrespondencia(4319) · borrarDetalle(4425)
buscarPersonaje(1173) · cabezas(1850) · cabs(2640) · cambiarMarca(3477)
cambiarMarcaDuelo(3244) · cargarEstado(1565) · cargarIdentidad(926) · cargarOficiales(1054)
cargarPersonajes(1097) · cerrarDetalle(4400) · cerrarModal(3968) · cerrarModalImagen(1951)
cerrarSesion(1803) · chequearPartidaEspera(1631) · claveCfg(3989)
confirmarArranqueDuelo(3140) · conPendiente(3773) · construirCabezas(957)
construirCabezasModo(2800) · continuarPartida(3799) · continuarPartidaLocal(3822)
contraDeRonda(2551) · contraparteDe(1199) · deck(2821) · disponiblesInvitados(2485)
dueloEsJuntos(2529) · dueloLadoDePartida(2519) · dueloMismoLadoDePartida(1168)
dueloModalidadDePartida(2524) · elegirAzarDuelo(3267) · elegirAzarSeleccion(3283)
elegirTentacion(3307) · enEspera(1862) · entrar(1305) · entrarAlJuego(3857)
entrarDirecto(1265) · esAnfitrion(1810) · esClaveLista(3993) · escucharAprobacion(896)
escucharGrupo(4786) · escucharSeleccion(3606) · escucharSesion(1655) · esDueloJuntos(2577)
esModoDuelo(2516) · esOficial(1050) · especialDe(1594) · especialDeLado(2042)
especialK(1469) · especialPendido(1468) · exportarLista(4603) · filaPersonaje(4216)
filaVariante(4183) · filtro(4279) · finPartida(2328) · guardarDetalle(4401)
guardarEdit(4190) · guardarLocalGuardada(858) · guardarPersonajes(1120) · hostNombre(3359)
idLibre(4009) · indexarPersonajes(985) · iniciar(2928) · iniciarEstado(1271)
irAlMenu(4688) · lado(2814) · ladoAnatomiaCfg(3985) · ladoDeCabeza(2531) · ladoDuelo(2601)
ladoOriginal(2559) · leerJSONPegado(4027) · leerLocalGuardada(872) · leerQuienSoy(923)
licMsg(915) · limpiarFiltro(4000) · limpiarFiltroSel(3112) · limpiarLocalGuardada(882)
limpiarParaArchivo(4589) · listaDeCabezaPara(2830) · listaDeLado(1149) · listaSegura(1006)
llenar(1867) · llenarSelectPar(4363) · marcas(2725) · meterInvitado(2720) · mezclar(810)
miLado(3986) · mismoContenidoPersonaje(1025) · mismosLados(2804) · modalAbierto(4711)
modalidad(2903) · modoAdmiteInvitados(1816) · modoBaseDePartida(2510)
mostrarBotonesAdmin(1817) · mostrarCaraDuelo(2136) · mostrarGracia(886) · nombreAdmin(943)
nombreArchivoExport(4598) · nombreCabeza(953) · nombreDeLado(3987) · nombreDeLista(3994)
nombreHostSeleccion(3122) · nombreLado(949) · nombres(1648) · normSel(3109)
ordenPersonajes(1075) · otroLado(4318) · otroLadoDuelo(1161) · parejaAcepto(3132)
parejaAEsperar(3128) · pares(2554) · paresDisponibles(1214) · parsePegadoPersonajes(4065)
parsePegadoTextos(4092) · pedirCartasInvitado(2662) · pegarLista(4451) · personajeDe(4117)
personajesRef(843) · pintarAvisosCfg(4340) · pintarCaraDuelo(2049) · pintarCfg(4240)
pintarDueloPar(2108) · pintarDueloTentacion(2122) · pintarEspecial(1477)
pintarFaseDuelo(1902) · pintarFoto(2001) · pintarFotoEn(1969) · pintarInicio(1386)
pintarMeterInvitado(2708) · pintarModalDuelo(1431) · pintarModo(1391)
pintarModoPartida(2538) · pintarPaso(2226) · pintarPasoDueloJuntos(2150) · pintarSala(1841)
pintarSalidas(936) · pintarSeleccion(3383) · pintarSeleccionDuelo(3152)
pintarTarjeta(2002) · pintarVolteo(1911) · ponerBadgeOficial(1083) · poolsDuelo(1228)
poolsEspejoMismo(2813) · preparar(2870) · prepararDuelo(2901) · probar(4029)
puedeVerOtroLado(3982) · quienes(2544) · recalcularOficiales(1031)
reiniciarVariantes(1541) · repartirEspeciales(1551) · repartirTarjetas(2841)
resetCarta(1958) · retirarInvitadosDeLaPartida(847) · revisarEspecial(2917) · ronda(2573)
salirAlMenu(4698) · salirModoInvitado(3922) · saltarTurno(1737) · sanearSesion(1598)
seguirEncima(3762) · seguirFuera(3767) · seleccionRef(3085) · selEsCompartida(3086)
selFuente(3088) · selMarcosDe(3089) · selPoolDe(3092) · selTodosListos(3103)
sesionRef(844) · siguienteDueloJuntos(2369) · siguienteSesion(1710) · siguienteTurno(1279)
sinDuplicados(818) · soyCabeza(1269) · textoPersonaje(1020) · traePar(4446) · url(1971)
ver(4668) · vistaDeInicio(4680) · voltear(1910) · voltearDuelo(2143) · yaExiste(4003)
```

### `Castigos\index.html`

```
abortarPlacer(2588) · abrirDetalle(1568) · abrirEditor(1346) · abrirQRJuego(3929)
accesorioEnUso(1828) · accionDeNivel(2759) · accionesModeloPorRonda(4086)
accionVacia(1380) · actualizar(2481) · actualizarBotonJugar(1492) · actualizarInicio(2290)
agregar(1458) · agregarInvitadoAPartida(4167) · agregarInvitadoLocal(4152)
ajustarAltoCampo(1390) · anunciarinvitacion(3224) · armando(3391)
armarBolsasImposicion(2729) · armarPartidaNormal(2599) · asignarImposicionesAlAzar(2740)
avanzarSaltadoRemoto(3684) · avanzarTurnoNoSaltado(3117) · avanzarTurnoRemoto(3652)
bolsasEnMemoria(3994) · bolsasParaInvitado(4028) · borrarAcceso(1810) · borrarAccion(1515)
borrarCastigo(1328) · borrarImp(1897) · cargarAccesorios(810) · cargarCastigos(775)
cargarDatosCastigo(1907) · cargarIdentidad(715) · cargarImposiciones(823)
cargarSesionEnMemoria(3315) · cargarTodo(767) · cerrar(2168) · chequearConexion(4254)
chequearPartidaEspera(3364) · clave(4073) · colorAccion(3536) · conGente(3387)
construirNivelesOficial(849) · contarAccionesCastigos(1952) · continuarPausa(2195)
continuarSeleccionCastigo(2246) · controlesAnfitrionVisible(3471)
crearSesionCompartida(3216) · descartarPausa(2182) · descripcionPausa(2157) · destino(1202)
elegirAccionInvitado(4069) · elegirCastigoParaJugar(2607) · elegirModo(2330)
enEspera(3395) · enfocarAccion(1480) · enJuego(1041) · entrar(4260)
entrarAlJuegoCompartida(3352) · escribirImposicionRemoto(3633) · escucharGrupo(734)
escucharSesionCompartida(3243) · esSoloPuro(3472) · estadoPartidaLocal(2037)
esUnCelular(3546) · etiquetaLados(759) · filtro(1267) · finVisible(1035) · fraseAccion(3486)
gastarCortesiasCastigo(2272) · generarJugadores(2707) · generarTurnos(2767)
generarTurnosMulti(2962) · guardarCastigoDatos(1598) · guardarImposiciones(1904)
idVigente(651) · iniciarPartida(3123) · iniciarPartidaMulti(2860)
iniciarTemporizadorDesde(3086) · irAlMenu(1128) · ladoDe(4088) · ladoInv(4155)
ladosParticipantes(2556) · leerNivelesCastigo(4001) · leerPausa(2125) · leerQuienSoy(711)
llenar(3399) · mezclar(1381) · modalAbierto(1149) · modalBasePaso(1077)
mostrarBotonAccion(3066) · mostrarFin(3430) · mostrarGracia(1102) · mostrarModalBase(1095)
mostrarPanel(1245) · msg(1241) · msgTomas(1242) · nivel(4125) · nombreDeLado(755)
normalizaAcc(1522) · normalizarAccionImport(1700) · normalizarAccionOficial(837)
normalizarNivelesPlacer(2526) · normTxt(3992) · overlayReinstalar(976)
pararTemporizador(3062) · parsearImportacion(1664) · partes(4230) · partes2(4240)
pausarPartida(2110) · pintarAccesorios(1742) · pintarAccesoriosDetalle(1524)
pintarCastigos(1263) · pintarCrono(3080) · pintarEditor(1395) · pintarImposiciones(1865)
pintarListaInicio(1969) · pintarSala(3384) · pintarSalidas(1039) · pintarTomas(1500)
pintarTomasJugar(2642) · pintarTomasJugarMulti(2656) · pintarTurno(3501)
placerAccionesEnNiveles(2565) · placerAlcanzaMulti(2578) · placerAlcanzaNormal(2574)
poolDeAcciones(4049) · preguntarImposicionesPor3(2472) · preguntarNivelesPlacer(2532)
preguntarPausa(2164) · preguntarQuienCastiga(2319) · promptTexto(1931)
publicarSesion(3159) · quitarAccesorioDeTodas(1844) · reanudarCronoRemotoSiHaceFalta(3107)
recalcularSaltadoPorRevivir(3052) · refrescarUsuarios(728) · reinstalarOficialDesdeUrl(989)
renombrarAcceso(1776) · renombrarCastigo(1312) · repararOficialCastigo(938)
repartirRueda(2917) · resetearInicioMulti(3875) · restaurarPartidaLocal(2068)
retirarInvitadosDeLaPartida(2701) · salirAlMenu(1138) · salirModoInvitado(3903)
saltado(2843) · saltarTurnoRemoto(3715) · seleccionarCastigo(2236) · sesionRef(2696)
setHowTabs(2354) · setModTabs(2347) · setTipoTabs(2376) · sincronizarOficialesCastigos(866)
soyCabeza(3361) · tieneAcciones(4023) · toggleMulti(2383) · tomarImposicion(2732)
totalAccionesDatos(934) · totalAccionesEditor(1485) · turnosConInvitado(4106)
vaciaDatos(1375) · vale(4074) · ver(1049) · vistaActual(1031) · volverConHistorial(1113)
volverDePartida(3892) · volverTiendaReinstalar(965)
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
abrirAgregar(2224) · abrirEditor(1548) · abrirModal(1705) · abrirQRInvitacion(2317)
abrirTomas(1731) · acts(1777) · agregar(1595) · agregarInvitado(2246) · agregarItemEd(1642)
anunciarInvitacion(932) · armando(1982) · avanzarLocal(831) · avanzarSesion(854)
avisarCortesia(1305) · base(2176) · cab(662) · cabezas(2297) · cabs(1989)
cargarActividades(1217) · cargarActsParaInvitado(2125) · cargarEnMemoria(591)
cargarIdentidad(520) · cargarTomasDoc(1472) · cerrarModal(1725) · cerrarSesion(949)
cerrarTomas(1761) · chequearPartidaEspera(735) · chequearPendiente(647) · companero(2257)
compararActividades(1279) · construirCabezas(1783) · contarNivel(394) · dibujarLista(1314)
disponiblesInvitados(2220) · docDe(1116) · elegirAccionEnc(2159) · enEspera(1994)
entrar(684) · entrarAlJuego(2429) · entrarDirecto(587) · esAnfitrion(1956)
escucharAprobacion(479) · escucharGrupo(2451) · escucharSesion(759) · etiquetaLados(1451)
filtrar(1384) · gastarCortesias(1287) · generarListas(1794) · generarYIniciar(1867)
guardadas(1737) · guardarEditor(1637) · guardarTomasEnBase(1505) · iniciarSingle(672)
irAlMenu(1012) · item(2082) · leerQuienSoy(517) · leerTomasEd(1664) · licMsg(509)
limpiarInvitadosDeSesionAnterior(966) · listaConInvitado(2175) · llenar(1999) · mezclar(399)
migrarTomasDeEsteCelular(1487) · modalAbierto(1036) · mostrarBotonesAdmin(1957)
mostrarFin(979) · mostrarGracia(415) · multiRefrescar(1395) · multiToggle(1405)
nivel(2200) · nivelPorNombre(2121) · nombreAdmin(543) · nombreCabeza(640) · nombreLado(1447)
nombres(752) · normLados(389) · normOrdenAct(1276) · normTomasEnc(1462) · normTxtEnc(2119)
ofs(1120) · overlayReinstalar(1161) · pintarEditor(1566) · pintarLista(1369)
pintarListaCfg(1514) · pintarPaso(2040) · pintarSala(1975) · pintarSalidas(535)
pintarTurnoDe(2026) · poolDeAccionesEnc(2140) · quiereCompartido(1924) · quitarItemEd(1655)
reinstalarOficialDesdeUrl(1174) · repartirRuedaEnc(1829) · retirarInvitadosDeLaPartida(960)
salirAlMenu(1022) · salirModoInvitado(442) · saltarTurno(884) · sanearSesion(611)
seguirEncima(2375) · seguirFuera(2380) · sesionRef(549) · sincronizarOficiales(1118)
soyCabeza(603) · tomasGuardadasEd(1510) · ultimo(2090) · vale(2163) · ver(986)
volverTiendaReinstalar(1150)
```

### `Guiadas\index.html`

```
abrirEditor(1712) · abrirFin(473) · abrirTomasGuia(1211) · agregar(1762) · agregarItem(1809)
aplicaSesion(638) · armarListaLados(1300) · asignarParaId(1288) · avanzarSesion(541)
avisarCortesia(1035) · borrarProg(1271) · cargarActividades(947) · cargarIdentidad(486)
cargarTomasDoc(1669) · cerrarSesion(594) · cerrarTomasGuia(1236) · claveDoc(837)
compararActividades(1009) · contarNivel(325) · dibujarLista(1044) · docDe(844)
editorTieneAlgo(1868) · empezarNuevo(1322) · entrar(349) · esAdmin(501)
escucharAprobacion(411) · escucharSesion(646) · etiquetaLados(529) · exportarActividad(1966)
filtrar(821) · gastarCortesias(1017) · guardar(1804) · guardarProg(1264)
guardarTomasEnBase(1702) · iniciarSesionCompartida(560) · irAlMenu(712)
jugadoresBase(1274) · jugarDirecto(1140) · leerJSONPegado(1855) · leerProg(1200)
leerQuienSoy(483) · leerTomas(1831) · licMsg(393) · limpiarParaArchivo(1949)
marcarRadio(537) · mensajeEditor(1845) · mezclar(829) · migrarTomasDeEsteCelular(1684)
miIdSesion(535) · mismoPaso(520) · modalAbierto(739) · modalBasePaso(1427) · mostrarFin(467)
mostrarGracia(340) · mostrarModalBase(1445) · mostrarPlayer(1339) · multiAbrir(1479)
multiAbrirSel(1505) · multiMostrar(1451) · multiRefrescar(1454) · multiSalir(1513)
multiToggle(1464) · nombreAdmin(502) · nombreDe(507) · nombreDePaso(512) · nombreLado(525)
normLados(312) · normOrdenAct(1006) · normTomas(317) · ofs(850) · overlayReinstalar(891)
pegarActividad(1871) · pintarEditor(1733) · pintarLista(1125) · pintarPaso(2026)
pintarTurnoDe(2017) · probar(1857) · quienes(1498) · quitarItem(1822) · refrescarMiLado(494)
reinstalarOficialDesdeUrl(904) · repartirRuedaGuia(1622) · salirAlMenu(722)
saltarTurno(612) · seguirEncima(1190) · seguirFuera(1197) · sesionPausada(600)
sesionRef(536) · sincronizarOficiales(848) · tomasDePantalla(1957) · tomasGuardadas(1707)
top(1047) · ver(688) · volverTiendaReinstalar(880)
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

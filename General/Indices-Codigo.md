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

---

## `Roles/index.html` — 4,516 líneas

**Documento de detalle:** `General/Roles.md`

**Vistas:** `vistaBloqueo` (380) · `vistaInicio` (392) · `vistaSeleccion` (457) ·
`vistaEspera` (490) · `vistaPlayer` (497) · `vistaConfig` (584) · `vistaSeguir` (674)

| Para... | Función | Línea |
|---|---|---|
| Arrancar la página: identidad, licencia y estado guardado | `entrar()` | 1164 |
| Cambiar de vista y guardar el paso del historial | `ver()` | 4351 |
| Volver al menú deshaciendo los pasos | `salirAlMenu()` | 4381 |
| Pintar la tarjeta de inicio (modo y "Jugar") | `pintarInicio()` | 1225 |
| Pantalla de modo (Clásico, Cambia de Bando, Seleccionar, Duelo) | `pintarModo()` | 1230 |
| Modal del duelo | `pintarModalDuelo()` / `abrirModalDuelo()` | 1270 / 1286 |
| Quiénes juegan y de qué lado | `construirCabezas()` | 946 |
| Pool de personajes: cargar, sembrar, guardar | `cargarPersonajes()` / `asegurarPersonajes()` / `guardarPersonajes()` | 974 / 992 / 996 |
| Buscar personaje o su contraparte | `buscarPersonaje()` / `contraparteDe()` | 1042 / 1064 |
| Repartir tarjetas y preparar la partida | `repartirTarjetas()` / `preparar()` / `prepararDuelo()` | 2665 / 2694 / 2725 |
| Arrancar la partida normal | `iniciar()` | 2752 |
| Modo Seleccionar: pintar, abrir y arrancar | `pintarSeleccion()` / `abrirSeleccionLocal()` / `abrirSeleccionCompartida()` / `arrancarSeleccion()` | 3196 / 3312 / 3327 / 3368 |
| Escuchar la selección compartida | `escucharSeleccion()` | 3415 |
| Sala de espera (anfitrión e invitado) | `pintarSala()` | 1680 |
| Pintar la partida: tarjeta, paso, duelo | `pintarTarjeta()` / `pintarPaso()` / `pintarCaraDuelo()` / `pintarPasoDueloJuntos()` | 1841 / 2065 / 1888 / 1989 |
| Pasar turno o saltarlo | `siguienteTurno()` / `avanzarTarjeta()` / `siguienteSesion()` / `saltarTurno()` | 1138 / 1153 / 1549 / 1576 |
| Terminar la partida | `abrirFin()` / `finPartida()` | 2160 / 2167 |
| Sesión multijugador | `escucharSesion()` | 1494 |
| Configuración: pintar, abrir, filas y editor | `pintarCfg()` / `abrirCfg()` / `filaPersonaje()` / `agregarPersonaje()` | 4026 / 4331 / 4003 / 3925 |
| Exportar la lista de personajes | `exportarLista()` | 4286 |
| Invitado: entrar, continuar, salir | `entrarAlJuego()` / `continuarPartida()` / `salirModoInvitado()` | 3666 / 3608 / 3731 |
| QR de invitación | `abrirQR()` | 2601 |
| Modales chicos | `abrirModal()` / `cerrarModal()` | 3760 / 3777 |

---

## `Castigos/index.html` — 4,176 líneas

**Documento de detalle:** `General/Castigos.md`

**Vistas:** `vistaInicio` (249) · `vistaBloqueo` (307) · `vistaTomas` (314) ·
`vistaPartida` (335) · `vistaEspera` (408) · `vistaConfig` (494) · `vistaEditar` (537)

| Para... | Función | Línea |
|---|---|---|
| Cargar todo: identidad, castigos, accesorios, imposiciones, usuarios | `cargarTodo()` | 734 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 944 / 1025 |
| Panel de configuración | `mostrarPanel()` | 1130 |
| Lista y edición de castigos | `pintarCastigos()` / `abrirEditor()` / `pintarEditor()` / `guardarCastigoDatos()` | 1148 / 1231 / 1280 / 1483 |
| Tomas de cada castigo | `pintarTomas()` | 1385 |
| Accesorios e imposiciones | `pintarAccesorios()` / `pintarImposiciones()` | 1627 / 1750 |
| Pantalla de inicio y castigo elegido | `pintarListaInicio()` / `seleccionarCastigo()` / `actualizarInicio()` | 1854 / 2121 / 2146 |
| Pasos antes de jugar: quién castiga, modo, multi, imposiciones, placer | `preguntarQuienCastiga()` / `elegirModo()` / `toggleMulti()` / `preguntarImposicionesPor3()` / `preguntarNivelesPlacer()` | 2175 / 2186 / 2239 / 2322 / 2382 |
| Armar y arrancar: normal y multi | `armarPartidaNormal()` / `iniciarPartida()` / `iniciarPartidaMulti()` | 2449 / 2971 / 2710 |
| Repartir turnos y rueda | `repartirRueda()` / `generarTurnos()` / `generarTurnosMulti()` | 2765 / 2617 / 2810 |
| Pintar turno, sala y fin | `pintarTurno()` / `pintarSala()` / `mostrarFin()` | 3345 / 3228 / 3274 |
| Pausa: pausar, continuar, descartar | `pausarPartida()` / `continuarPausa()` / `descartarPausa()` | 1995 / 2080 / 2067 |
| Sesión compartida: publicar y escuchar | `publicarSesion()` / `escucharSesionCompartida()` | 3005 / 3087 |
| Turnos remotos y saltar turno remoto | `avanzarTurnoRemoto()` / `saltarTurnoRemoto()` / `escribirImposicionRemoto()` | 3496 / 3559 / 3477 |
| Cronómetro | `pintarCrono()` / `iniciarTemporizadorDesde()` | 2928 / 2934 |
| Invitados: QR y agregar a la partida | `abrirQRJuego()` / `agregarInvitadoAPartida()` | 3773 / 4011 |
| Importar acciones | `parsearImportacion()` / `normalizarAccionImport()` | 1549 / 1585 |

---

## `index.html` — 2,799 líneas (pantalla inicial)

**Documento de detalle:** `General/Pantallas.md` y `General/Usuarios.md`

**Vistas:** `vistaMenu` (451) · `vistaJuegos` (490) · `vistaRetos` (496) ·
`vistaCom` (502) · `vistaExp` (523)

| Para... | Función | Línea |
|---|---|---|
| Mostrar el menú y sus dos botones de esquina | `mostrarMenu()` / `verMenu()` | 635 / 1330 |
| Dibujar las tarjetas del catálogo | `tarjetaPack()` / `renderPacks()` / `renderPacksDeVerdad()` | 733 / 769 / 794 |
| Punto del carrito | `actualizarPuntoCarrito()` | 907 |
| Submenús: hash, abrir y cerrar | `hashActual()` / `abrirSegunHash()` / `abrirSub()` / `cerrarSub()` | 1348 / 1352 / 1360 / 1370 |
| Cada submenú | `abrirExp()` / `abrirJuegos()` / `abrirRetos()` / `abrirCom()` | 1377 / 1392 / 1401 / 1421 |
| Engrane: abrir, cerrar, cambiar usuario | `mostrarGear()` / `cerrarGear()` / `abrirCambiarUsu()` | 2468 / 2480 / 2488 |
| Telegram | `pintarTelegram()` | 2556 |
| Usuarios: anatomía y lista | `pintarInvUsuarios()` / `guardarAnatomiaUsuario()` / `abrirEdUsuarios()` | 1483 / 1458 / 2239 |
| Puntos e historial de movimientos | `abrirPuntos()` / `abrirHistorial()` | 1586 / 1623 |
| Propuestas de precios: pintar, abrir, aceptar, rechazar | `pintarPropuestas()` / `abrirPropuestas()` / `aceptarPropuesta()` / `rechazarPropuesta()` | 1943 / 2016 / 2051 / 2103 |
| Invitado: volver solo y escanear QR | `volverSiInvitadoSinPartida()` / `iniciarScan()` | 1148 / 1283 |

---

## `Lenceria/index.html` — 2,657 líneas

**Documento de detalle:** `General/Catalogo-Lenceria.md`

**Vistas:** `vistaPlanes` (204) · `vistaElegir` (218) · `vistaPedido` (241) ·
`vistaConfig` (258) · `vistaClasif` (279) · `vistaPrenda` (296)

| Para... | Función | Línea |
|---|---|---|
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 373 / 398 |
| Cargar todo y escuchar cambios | `cargarTodo()` / `escuchar()` | 2551 / 2264 |
| Cargar prendas, planes y pedidos | `cargarPrendas()` / `cargarPlanes()` / `cargarPedidos()` | 2235 / 2242 / 2249 |
| Configuración: clasificaciones y prendas | `pintarConfig()` / `bloqueClasif()` / `bloquePrendas()` | 853 / 871 / 1037 |
| Clasificación: abrir, pintar, guardar, borrar | `abrirClasif()` / `pintarClasifVista()` / `guardarClasif()` / `borrarClasif()` | 949 / 957 / 982 / 1006 |
| Prenda: tarjeta, abrir, guardar, borrar | `tarjetaPrenda()` / `abrirPrenda()` / `guardarPrenda()` / `borrarPrenda()` | 1091 / 1178 / 1355 / 1414 |
| Fotos: elegir archivo, procesar, lupa | `usarArchivoFoto()` / `procesarFoto()` / `abrirLupa()` | 1319 / 1276 / 1153 |
| Planes: pintar, tarjeta y separador | `pintarPlanes()` / `tarjetaPlan()` / `separadorPlanes()` | 1510 / 1594 / 1495 |
| Orden por olvido y texto de uso | `ordenPorOlvido()` / `textoUso()` / `diasDesdeUso()` | 794 / 782 / 773 |
| Vestidor: elegir y contar | `abrirElegir()` / `pintarVestidor()` / `alternarSeleccion()` / `pintarContador()` | 1784 / 1818 / 1837 / 1883 |
| Guardar plan, fijarlo o borrarlo | `guardarPlan()` / `alternarFijo()` / `borrarPlan()` | 1896 / 1950 / 1959 |
| "Sorpréndeme" | `sorprendeme()` | 2162 |
| Pedidos: proponer, abrir, aceptar, rechazar, cancelar | `mandarPropuesta()` / `abrirPedido()` / `aceptarPedido()` / `rechazarPedido()` / `cancelarPedido()` | 1975 / 2022 / 2065 / 2127 / 2149 |
| Contador de usos | `liquidarUsos()` | 2201 |
| Exportar / importar prendas | `abrirDatos()` / `aplicarImportacion()` | 2318 / 2383 |
| Entrar desde una cita | `aplicarEntradaCita()` | 2565 |

---

## `Encuentros/index.html` — 2,358 líneas

**Documento de detalle:** `General/Pantallas.md` y `General/Pegamento-y-Citas.md`

**Vistas:** `vistaBloqueo` (152) · `vistaLista` (164) · `vistaConfig` (189) ·
`vistaEditar` (197) · `vistaEspera` (210) · `vistaPlayer` (217) · `vistaSeguir` (258)

| Para... | Función | Línea |
|---|---|---|
| Arrancar: normal o directo al juego | `entrar()` / `entrarDirecto()` | 651 / 561 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 953 / 989 |
| Cargar actividades y pintar la lista | `cargarActividades()` / `pintarLista()` / `dibujarLista()` / `filtrar()` | 1110 / 1225 / 1166 / 1240 |
| Configuración y editor de actividades | `pintarListaCfg()` / `abrirEditor()` / `pintarEditor()` / `guardarEditor()` | 1369 / 1407 / 1425 / 1496 |
| Tomas de una actividad (modal y base) | `abrirTomas()` / `guardarTomasEnBase()` / `cargarTomasDoc()` | 1590 / 1360 / 1327 |
| Armar jugadores y repartir | `construirCabezas()` / `generarListas()` / `repartirRuedaEnc()` / `generarYIniciar()` | 1640 / 1651 / 1686 / 1724 |
| Pintar turno y paso | `pintarTurnoDe()` / `pintarPaso()` | 1881 / 1895 |
| Avanzar local o por sesión | `avanzarLocal()` / `avanzarSesion()` | 798 / 821 |
| Sala de espera | `pintarSala()` | 1830 |
| Invitados: agregar y QR | `agregarInvitado()` / `abrirQRInvitacion()` | 2101 / 2172 |
| Sesión: escuchar, saltar turno, cerrar, fin | `escucharSesion()` / `saltarTurno()` / `cerrarSesion()` / `mostrarFin()` | 726 / 851 / 916 / 946 |
| Entrar al juego siendo invitado | `entrarAlJuego()` | 2284 |

---

## `Guiadas/index.html` — 2,059 líneas

**Documento de detalle:** `General/Pantallas.md` y `General/Pegamento-y-Citas.md`

**Vistas:** `vistaBloqueo` (117) · `vistaLista` (129) · `vistaConfig` (154) ·
`vistaEditar` (162) · `vistaPlayer` (183) · `vistaSeguir` (197)

| Para... | Función | Línea |
|---|---|---|
| Arrancar la página | `entrar()` | 327 |
| Cambiar de vista y volver al menú | `ver()` / `salirAlMenu()` | 660 / 694 |
| Cargar actividades y pintar la lista | `cargarActividades()` / `pintarLista()` / `filtrar()` | 845 / 986 / 791 |
| Jugar directo desde la lista | `jugarDirecto()` | 1001 |
| Arrancar partida y pintar el paso | `empezarNuevo()` / `mostrarPlayer()` / `pintarPaso()` / `pintarTurnoDe()` | 1170 / 1185 / 1867 / 1858 |
| Sesión: avanzar, escuchar, saltar, cerrar, fin | `avanzarSesion()` / `escucharSesion()` / `saltarTurno()` / `cerrarSesion()` / `mostrarFin()` | 517 / 618 / 584 / 566 / 443 |
| Multi: abrir, refrescar, seleccionar, repartir | `multiAbrir()` / `multiRefrescar()` / `multiAbrirSel()` / `repartirRuedaGuia()` | 1324 / 1300 / 1350 / 1463 |
| Editor de actividades | `abrirEditor()` / `pintarEditor()` / `guardar()` | 1553 / 1574 / 1645 |
| Exportar o pegar una actividad | `exportarActividad()` / `pegarActividad()` | 1807 / 1712 |
| Tomas de la actividad | `abrirTomasGuia()` / `guardarProg()` / `cargarTomasDoc()` | 1061 / 1112 / 1510 |
| Seguir jugando después de recargar | `seguirEncima()` / `seguirFuera()` | 1044 / 1051 |

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
abrirAgregar(2328) · abrirCfg(4331) · abrirDetalle(4164) · abrirFin(2160)
abrirMeterInvitado(2527) · abrirModal(3760) · abrirModalDuelo(1286) · abrirModalImagen(1782)
abrirQR(2601) · abrirSeleccionCompartida(3327) · abrirSeleccionDueloCompartida(3158) · abrirSeleccionDueloLocal(3141)
abrirSeleccionLocal(3312) · abrirVentanaEspecial(1344) · actualizarTextoEstadoCarta(1776) · adminDe(2635)
agregarDesdeInput(3945) · agregarEspecial(3936) · agregarInvitado(2401) · agregarPersonaje(3925)
anunciarInvitacion(1627) · armando(1694) · arrancarSeleccion(3368) · asegurarPersonajes(992)
avanzarDueloJuntosLocal(2191) · avanzarTarjeta(1153) · avisoJSONMalo(3849) · avisosCorrespondencia(4094)
borrarDetalle(4207) · buscarPersonaje(1042) · cabezas(1689) · cabs(2468)
cambiarMarca(3286) · cambiarMarcaDuelo(3057) · cargarEstado(1404) · cargarIdentidad(915)
cargarPersonajes(974) · cerrarDetalle(4182) · cerrarModal(3777) · cerrarModalImagen(1790)
cerrarSesion(1642) · chequearPartidaEspera(1470) · claveCfg(3798) · confirmarArranqueDuelo(2957)
conPendiente(3582) · construirCabezas(946) · construirCabezasModo(2628) · continuarPartida(3608)
continuarPartidaLocal(3631) · contraDeRonda(2390) · contraparteDe(1064) · deck(2648)
disponiblesInvitados(2324) · dueloEsJuntos(2368) · dueloLadoDePartida(2358) · dueloModalidadDePartida(2363)
elegirAzarDuelo(3080) · elegirAzarSeleccion(3096) · elegirTentacion(3120) · enEspera(1701)
entrar(1164) · entrarAlJuego(3666) · entrarDirecto(1124) · esAnfitrion(1649)
escucharAprobacion(885) · escucharGrupo(4469) · escucharSeleccion(3415) · escucharSesion(1494)
esDueloJuntos(2410) · esModoDuelo(2355) · especialDe(1433) · especialDeLado(1881)
especialK(1308) · especialPendido(1307) · exportarLista(4286) · filaPersonaje(4003)
filaVariante(3970) · filtro(4062) · finPartida(2167) · guardarDetalle(4183)
guardarEdit(3977) · guardarLocalGuardada(847) · guardarPersonajes(996) · hostNombre(3172)
idLibre(3808) · iniciar(2752) · iniciarEstado(1130) · irAlMenu(4371)
lado(2641) · ladoAnatomiaCfg(3794) · ladoDeCabeza(2370) · ladoDuelo(2434)
ladoOriginal(2398) · leerJSONPegado(3826) · leerLocalGuardada(861) · leerQuienSoy(912)
licMsg(904) · limpiarFiltro(3799) · limpiarFiltroSel(2929) · limpiarLocalGuardada(871)
limpiarParaArchivo(4272) · listaDeCabezaPara(2657) · listaDeLado(1024) · listaSegura(966)
llenar(1706) · llenarSelectPar(4148) · marcas(2553) · meterInvitado(2548)
mezclar(799) · miLado(3795) · mismosLados(2632) · modalAbierto(4394)
modalidad(2727) · modoAdmiteInvitados(1655) · modoBaseDePartida(2349) · mostrarBotonesAdmin(1656)
mostrarCaraDuelo(1975) · mostrarGracia(875) · nombreAdmin(932) · nombreArchivoExport(4281)
nombreCabeza(942) · nombreDeLado(3796) · nombreHostSeleccion(2939) · nombreLado(938)
nombres(1487) · normSel(2926) · otroLado(4093) · otroLadoDuelo(1036)
parejaAcepto(2949) · parejaAEsperar(2945) · pares(2393) · paresDisponibles(1073)
parsePegadoPersonajes(3860) · parsePegadoTextos(3883) · pedirCartasInvitado(2490) · pegarLista(4225)
personajeDe(3904) · personajesRef(832) · pintarAvisosCfg(4125) · pintarCaraDuelo(1888)
pintarCfg(4026) · pintarDueloPar(1947) · pintarDueloTentacion(1961) · pintarEspecial(1316)
pintarFaseDuelo(1741) · pintarFoto(1840) · pintarFotoEn(1808) · pintarInicio(1225)
pintarMeterInvitado(2536) · pintarModalDuelo(1270) · pintarModo(1230) · pintarModoPartida(2377)
pintarPaso(2065) · pintarPasoDueloJuntos(1989) · pintarSala(1680) · pintarSalidas(925)
pintarSeleccion(3196) · pintarSeleccionDuelo(2969) · pintarTarjeta(1841) · pintarVolteo(1750)
poolsDuelo(1087) · poolsEspejoMismo(2640) · preparar(2694) · prepararDuelo(2725)
probar(3828) · puedeVerOtroLado(3791) · quienes(2383) · reiniciarVariantes(1380)
repartirEspeciales(1390) · repartirTarjetas(2665) · resetCarta(1797) · retirarInvitadosDeLaPartida(836)
revisarEspecial(2741) · ronda(2406) · salirAlMenu(4381) · salirModoInvitado(3731)
saltarTurno(1576) · sanearSesion(1437) · seguirEncima(3571) · seguirFuera(3576)
seleccionRef(2909) · selEsCompartida(2910) · selFuente(2912) · selMarcosDe(2913)
selPoolDe(2915) · selTodosListos(2920) · sesionRef(833) · siguienteDueloJuntos(2208)
siguienteSesion(1549) · siguienteTurno(1138) · sinDuplicados(807) · soyCabeza(1128)
url(1810) · ver(4351) · vistaDeInicio(4363) · voltear(1749)
voltearDuelo(1982) · yaExiste(3802)
```

### `Castigos\index.html`

```
abortarPlacer(2438) · abrirDetalle(1453) · abrirEditor(1231) · abrirQRJuego(3773)
accesorioEnUso(1713) · accionDeNivel(2609) · accionesModeloPorRonda(3930) · accionVacia(1265)
actualizar(2331) · actualizarBotonJugar(1377) · actualizarInicio(2146) · agregar(1343)
agregarInvitadoAPartida(4011) · agregarInvitadoLocal(3996) · ajustarAltoCampo(1275) · anunciarinvitacion(3068)
armando(3235) · armarBolsasImposicion(2579) · armarPartidaNormal(2449) · asignarImposicionesAlAzar(2590)
avanzarSaltadoRemoto(3528) · avanzarTurnoNoSaltado(2965) · avanzarTurnoRemoto(3496) · bolsasEnMemoria(3838)
bolsasParaInvitado(3872) · borrarAcceso(1695) · borrarAccion(1400) · borrarCastigo(1213)
borrarImp(1782) · cargarAccesorios(776) · cargarCastigos(742) · cargarDatosCastigo(1792)
cargarIdentidad(682) · cargarImposiciones(789) · cargarSesionEnMemoria(3159) · cargarTodo(734)
cerrar(2053) · chequearConexion(4098) · chequearPartidaEspera(3208) · clave(3917)
colorAccion(3380) · conGente(3231) · construirNivelesOficial(815) · contarAccionesCastigos(1837)
continuarPausa(2080) · controlesAnfitrionVisible(3315) · crearSesionCompartida(3062) · descartarPausa(2067)
descripcionPausa(2042) · destino(1087) · elegirAccionInvitado(3913) · elegirCastigoParaJugar(2457)
elegirModo(2186) · enEspera(3239) · enfocarAccion(1365) · enJuego(936)
entrar(4104) · entrarAlJuegoCompartida(3196) · escribirImposicionRemoto(3477) · escucharGrupo(701)
escucharSesionCompartida(3087) · esSoloPuro(3316) · estadoPartidaLocal(1922) · esUnCelular(3390)
etiquetaLados(726) · filtro(1152) · finVisible(930) · fraseAccion(3330)
generarJugadores(2557) · generarTurnos(2617) · generarTurnosMulti(2810) · guardarCastigoDatos(1483)
guardarImposiciones(1789) · idVigente(621) · iniciarPartida(2971) · iniciarPartidaMulti(2710)
iniciarTemporizadorDesde(2934) · irAlMenu(1015) · ladoDe(3932) · ladoInv(3999)
ladosParticipantes(2406) · leerNivelesCastigo(3845) · leerPausa(2010) · leerQuienSoy(678)
llenar(3243) · mezclar(1266) · modalAbierto(1036) · modalBasePaso(972)
mostrarBotonAccion(2914) · mostrarFin(3274) · mostrarModalBase(990) · mostrarPanel(1130)
msgTomas(1127) · nivel(3969) · nombreDeLado(722) · normalizaAcc(1407)
normalizarAccionImport(1585) · normalizarAccionOficial(803) · normalizarNivelesPlacer(2376) · normTxt(3836)
pararTemporizador(2910) · parsearImportacion(1549) · partes(4074) · partes2(4084)
pausarPartida(1995) · pintarAccesorios(1627) · pintarAccesoriosDetalle(1409) · pintarCastigos(1148)
pintarCrono(2928) · pintarEditor(1280) · pintarImposiciones(1750) · pintarListaInicio(1854)
pintarSala(3228) · pintarSalidas(934) · pintarTomas(1385) · pintarTomasJugar(2492)
pintarTomasJugarMulti(2506) · pintarTurno(3345) · placerAccionesEnNiveles(2415) · placerAlcanzaMulti(2428)
placerAlcanzaNormal(2424) · poolDeAcciones(3893) · preguntarImposicionesPor3(2322) · preguntarNivelesPlacer(2382)
preguntarPausa(2049) · preguntarQuienCastiga(2175) · promptTexto(1816) · publicarSesion(3005)
quitarAccesorioDeTodas(1729) · reanudarCronoRemotoSiHaceFalta(2955) · recalcularSaltadoPorRevivir(2900) · refrescarUsuarios(695)
renombrarAcceso(1661) · renombrarCastigo(1197) · repararOficialCastigo(903) · repartirRueda(2765)
resetearInicioMulti(3719) · restaurarPartidaLocal(1953) · retirarInvitadosDeLaPartida(2551) · salirAlMenu(1025)
salirModoInvitado(3747) · saltado(2693) · saltarTurnoRemoto(3559) · seleccionarCastigo(2121)
sesionRef(2546) · setHowTabs(2210) · setModTabs(2203) · setTipoTabs(2232)
sincronizarOficialesCastigos(832) · soyCabeza(3205) · tieneAcciones(3867) · toggleMulti(2239)
tomarImposicion(2582) · totalAccionesDatos(899) · totalAccionesEditor(1370) · turnosConInvitado(3950)
vaciaDatos(1260) · vale(3918) · ver(944) · vistaActual(926)
volverConHistorial(1000) · volverDePartida(3736)
```

### `index.html`

```
abrirCambiarUsu(2488) · abrirCom(1421) · abrirEdUsuarios(2239) · abrirExp(1377)
abrirHistorial(1623) · abrirJuegos(1392) · abrirPanelUsuarios(2664) · abrirPropuestas(2016)
abrirPuntos(1586) · abrirRetos(1401) · abrirSegunHash(1352) · abrirSub(1360)
aceptarPropuesta(2051) · actualizarAvisoPropuestas(1863) · actualizarPuntoCarrito(907) · adminId(1064)
agregarFila(1016) · aplicar(1250) · armarFilas(1011) · cancelarPropuesta(2126)
cerrar(2208) · cerrarCom(1427) · cerrarEdUsuarios(2323) · cerrarExp(1386)
cerrarGear(2480) · cerrarHistorial(1678) · cerrarJuegos(1398) · cerrarOverlaysInv(2458)
cerrarPropuestas(2025) · cerrarPuntos(1605) · cerrarRetos(1409) · cerrarSub(1370)
conTiempo(582) · crearFilaProp(1909) · detenerScan(1179) · detenerScanInv(2717)
entrar(1088) · etiqueta(1235) · etiquetaAnatomia(1452) · etiquetaProp(1940)
formatearFechaMov(1614) · guardarAnatomiaUsuario(1458) · hashActual(1348) · hashTexto(2187)
iconoMenu(611) · iniciar(1111) · iniciarPropuestas(1889) · iniciarScan(1283)
invModoScan(2495) · invMsg(1435) · invRefrescar(1440) · invVer(2418)
irPaso3(996) · lado(1455) · leerGuardado(606) · mostrarGear(2468)
mostrarIdentidad(924) · mostrarMenu(635) · msgQR(1185) · nombreParejaMenu(782)
normalizaNombre(2793) · overlayInvAbierto(2455) · overlaysInv(2452) · parsearFB(589)
pedirPin(2197) · pintarInvUsuarios(1483) · pintarPropuestas(1943) · pintarTelegram(2556)
ponerZoom(1202) · probar(1243) · propuestasAbiertas(1905) · propuestasMiasPendientes(1837)
propuestasParaMi(1831) · propuestasResultadosNuevos(1843) · propuestasResultadosVisibles(1851) · ptsRaw(2335)
quitarZoom(1192) · recargar(942) · rechazarPropuesta(2103) · renderPacks(769)
renderPacksDeVerdad(794) · renumerarRadios(1051) · resolverTodasPropuestas(2149) · salirSinHaberEntrado(2506)
tarjetaPack(733) · textoDestinoProp(1824) · textoValorProp(1713) · tgApi(2573)
tgEstado(2551) · tgGuardado(2537) · tgTarjeta(2544) · titulo(1957)
todos(2248) · usuariosEfectivos(964) · valorEfectivoProp(1698) · valorPropValido(1705)
verHist(1531) · verMenu(1330) · verPaso(600) · volverSiInvitadoSinPartida(1148)
```

### `Lenceria\index.html`

```
abrirClasif(949) · abrirDatos(2318) · abrirElegir(1784) · abrirLupa(1153)
abrirPedido(2022) · abrirPrenda(1178) · aceptarPedido(2065) · agregarClasif(931)
alternarFijo(1950) · alternarSeleccion(1837) · aplicarEntradaCita(2565) · aplicarImportacion(2383)
arrancar(2619) · bloqueClasif(871) · bloquePrendas(1037) · borrarClasif(1006)
borrarPlan(1959) · borrarPrenda(1414) · botonPasados(1502) · cancelarPedido(2149)
cargarClasificaciones(732) · cargarPedidos(2249) · cargarPlanes(2242) · cargarPrendas(2235)
cargarTodo(2551) · cerrarLupa(1159) · construirFiltros(582) · conTiempo(2544)
desplegableFiltro(629) · diasDesdeUso(773) · escribirAviso(2013) · escuchar(2264)
esMia(1520) · extra(704) · fechaAObjeto(521) · fechaDeUso(761)
fechaLarga(526) · guardarClasif(982) · guardarPlan(1896) · guardarPrenda(1355)
hoyTexto(515) · idDeLado(1032) · irAlMenu(391) · lado(2431)
ladoDePersona(482) · leerImagen(1257) · limpiarFiltros(570) · limpiarPedidosVencidos(1760)
liquidarUsos(2201) · llenarSelect(1167) · mandarPropuesta(1975) · miniatura(1651)
mismoConjunto(2059) · modalAbierto(410) · mostrarFoto(1234) · nombreDe(831)
nombreLado(474) · nombrePersona(478) · normTexto(534) · ordenarClasif(746)
ordenPorOlvido(794) · pasaFiltro(574) · pedidoVencido(1668) · pintarClasifVista(957)
pintarConfig(853) · pintarContador(1883) · pintarPedido(2046) · pintarPlanes(1510)
pintarVestidor(1818) · planDePersona(508) · planesDe(1484) · planesDePersona(492)
planesDePersonaPorFecha(505) · planesPorFecha(496) · pref(2574) · prendaEnUsoFuturo(1249)
prendasDeLado(1028) · prendasDePersona(488) · procesarFoto(1276) · quedan(1437)
rechazarPedido(2127) · salirAlMenu(398) · sembrarClasificaciones(659) · separadorPlanes(1495)
siguienteRef(810) · sorprendeme(2162) · tarjetaPedidoEnviado(1722) · tarjetaPedidoRecibido(1673)
tarjetaPlan(1594) · tarjetaPrenda(1091) · textoUso(782) · tipoCubreTodo(805)
tsUso(768) · usarArchivoFoto(1319) · usoDe(836) · valor(753)
ver(373)
```

### `Encuentros\index.html`

```
abrirAgregar(2079) · abrirEditor(1407) · abrirModal(1564) · abrirQRInvitacion(2172)
abrirTomas(1590) · acts(1634) · agregar(1454) · agregarInvitado(2101)
agregarItemEd(1501) · anunciarInvitacion(899) · armando(1837) · avanzarLocal(798)
avanzarSesion(821) · base(2113) · cab(636) · cabezas(2152)
cabs(1844) · cargarActividades(1110) · cargarActsParaInvitado(1980) · cargarEnMemoria(565)
cargarIdentidad(498) · cargarTomasDoc(1327) · cerrarModal(1584) · cerrarSesion(916)
cerrarTomas(1620) · chequearPartidaEspera(702) · chequearPendiente(621) · companero(2112)
construirCabezas(1640) · contarNivel(375) · dibujarLista(1166) · disponiblesInvitados(2075)
docDe(1081) · elegirAccionEnc(2014) · enEspera(1849) · entrar(651)
entrarAlJuego(2284) · entrarDirecto(561) · esAnfitrion(1811) · escucharAprobacion(457)
escucharGrupo(2306) · escucharSesion(726) · etiquetaLados(1306) · filtrar(1240)
generarListas(1651) · generarYIniciar(1724) · guardadas(1596) · guardarEditor(1496)
guardarTomasEnBase(1360) · iniciarSingle(646) · irAlMenu(979) · item(1937)
leerQuienSoy(495) · leerTomasEd(1523) · licMsg(487) · limpiarInvitadosDeSesionAnterior(933)
listaConInvitado(2030) · llenar(1854) · mezclar(380) · migrarTomasDeEsteCelular(1342)
modalAbierto(1003) · mostrarBotonesAdmin(1812) · mostrarFin(946) · mostrarGracia(396)
multiRefrescar(1251) · multiToggle(1261) · nivel(2055) · nivelPorNombre(1976)
nombreAdmin(521) · nombreCabeza(614) · nombreLado(1302) · nombres(719)
normLados(370) · normTomasEnc(1317) · normTxtEnc(1974) · ofs(1085)
pintarEditor(1425) · pintarLista(1225) · pintarListaCfg(1369) · pintarPaso(1895)
pintarSala(1830) · pintarSalidas(513) · pintarTurnoDe(1881) · poolDeAccionesEnc(1995)
quiereCompartido(1779) · quitarItemEd(1514) · repartirRuedaEnc(1686) · retirarInvitadosDeLaPartida(927)
salirAlMenu(989) · salirModoInvitado(420) · saltarTurno(851) · sanearSesion(585)
seguirEncima(2230) · seguirFuera(2235) · sesionRef(527) · sincronizarOficiales(1083)
soyCabeza(577) · tomasGuardadasEd(1365) · ultimo(1945) · vale(2018)
ver(953)
```

### `Guiadas\index.html`

```
abrirEditor(1553) · abrirFin(449) · abrirTomasGuia(1061) · agregar(1603)
agregarItem(1650) · aplicaSesion(610) · armarListaLados(1148) · asignarParaId(1136)
avanzarSesion(517) · borrarProg(1119) · cargarActividades(845) · cargarIdentidad(462)
cargarTomasDoc(1510) · cerrarSesion(566) · cerrarTomasGuia(1086) · claveDoc(807)
contarNivel(306) · dibujarLista(901) · docDe(814) · editorTieneAlgo(1709)
empezarNuevo(1170) · entrar(327) · esAdmin(477) · escucharAprobacion(387)
escucharSesion(618) · etiquetaLados(505) · exportarActividad(1807) · filtrar(791)
guardar(1645) · guardarProg(1112) · guardarTomasEnBase(1543) · iniciarSesionCompartida(536)
irAlMenu(684) · jugadoresBase(1122) · jugarDirecto(1001) · leerJSONPegado(1696)
leerProg(1054) · leerQuienSoy(459) · leerTomas(1672) · licMsg(369)
limpiarParaArchivo(1790) · marcarRadio(513) · mensajeEditor(1686) · mezclar(799)
migrarTomasDeEsteCelular(1525) · miIdSesion(511) · mismoPaso(496) · modalAbierto(711)
modalBasePaso(1273) · mostrarFin(443) · mostrarGracia(321) · mostrarModalBase(1291)
mostrarPlayer(1185) · multiAbrir(1324) · multiAbrirSel(1350) · multiMostrar(1297)
multiRefrescar(1300) · multiSalir(1357) · multiToggle(1310) · nombreAdmin(478)
nombreDe(483) · nombreDePaso(488) · nombreLado(501) · normLados(293)
normTomas(298) · ofs(820) · pegarActividad(1712) · pintarEditor(1574)
pintarLista(986) · pintarPaso(1867) · pintarTurnoDe(1858) · probar(1698)
quienes(1343) · quitarItem(1663) · refrescarMiLado(470) · repartirRuedaGuia(1463)
salirAlMenu(694) · saltarTurno(584) · seguirEncima(1044) · seguirFuera(1051)
sesionPausada(572) · sesionRef(512) · sincronizarOficiales(818) · tomasDePantalla(1798)
tomasGuardadas(1548) · top(904) · ver(660)
```

### `Retos\index.html`

```
abrirFormulario(728) · abrirOverlayRecompensa(960) · actualizarVisibilidadRecompensa(657) · aplicarCastigoVisual(1207)
bip(418) · buscarReto(1001) · calcularMeta(685) · cargarIdentidadGuardada(552)
cerrarFormulario(792) · cerrarRecompensa(972) · cobrarRecompensaVisual(1194) · conteo(1103)
cumplido(1294) · cumplirRetoIA(1032) · diasRestantes(527) · eliminarReto(1088)
escucharBalances(1618) · escucharRetos(1541) · escucharUsuarios(1603) · esRelevanteReto(1534)
estaSuprimido(441) · etiquetaEstado(1510) · faltanTiempo(1522) · finalizarRetosVencidos(1225)
firmaDeUsuarios(705) · firmaReto(1527) · formatearFecha(515) · guardarIdentidad(558)
intentarResaltar(455) · leerFormulario(814) · llenarSelectAsignado(644) · marcarCumplida(1133)
momentoFecha(547) · mostrarApp(579) · mostrarBanner(412) · mostrarPantallaUsuario(563)
nombrePersona(700) · notificar(430) · nuevoConteo(1148) · pintarHintMeta(674)
rechazarReto(1005) · renderBalances(602) · renderRetos(1332) · resumenHtml(711)
retirarReto(1017) · soyReceptor(845) · suprimir(438) · truncar(638)
validarFormulario(831)
```

### `Opciones\index.html`

```
abrirAgregar(1070) · abrirCfg(1482) · abrirFin(1029) · abrirModal(1386)
abrirQR(1134) · agregarDesdeInput(1460) · agregarInvitado(1089) · agregarOpcion(1411)
anunciarInvitacion(856) · aplicarPick(578) · armando(918) · cabezas(913)
cabs(1117) · cargarEstado(672) · cargarIdentidad(458) · cargarOpciones(503)
cerrarModal(1403) · cerrarSesion(871) · chequearPartidaEspera(720) · conPendiente(1278)
construirCabezas(489) · construirCabezasModo(1160) · continuarPartida(1294) · disponiblesInvitados(1066)
enEspera(925) · entrar(597) · entrarAlJuego(1325) · entrarDirecto(536)
esAnfitrion(878) · escucharAprobacion(428) · escucharGrupo(1608) · escucharSesion(744)
filtro(1425) · finPartida(1036) · fuente(1096) · guardarEdit(1434)
guardarOpciones(515) · iniciar(1190) · iniciarEstado(550) · irAlMenu(1516)
leerQuienSoy(455) · licMsg(447) · llenar(930) · mezclar(368)
modalAbierto(1539) · modoAdmiteInvitados(884) · mostrarBotonesAdmin(885) · mostrarGracia(418)
nombreAdmin(475) · nombreCabeza(485) · nombreLado(481) · nombres(737)
opcionesRef(409) · parDe(542) · parseLista(390) · pick(1043)
pickSesion(795) · pintarCfg(1418) · pintarInicio(653) · pintarPaso(951)
pintarSala(904) · pintarSalidas(468) · quiereCompartido(1211) · quitar(581)
repartirOpciones(1167) · restantes(994) · retirarInvitadosDeLaPartida(413) · ronda(1093)
rondaActual(995) · salirAlMenu(1526) · salirModoInvitado(1356) · saltarTurno(818)
sanearSesion(687) · seguirEncima(1268) · seguirFuera(1273) · sesionRef(410)
siguienteTurno(564) · sinDuplicados(376) · soyCabeza(540) · ver(1499)
```

### `Diablitos\index.html`

```
abrirCfg(1125) · agregar(1059) · arrancar(1208) · asegurarLista(559)
asegurarMensajes(568) · avisar(1110) · borrarHabla(796) · burbuja(835)
cambiar(1037) · cambiarPestana(1099) · cargar(660) · cerrarCfg(1143)
colocar(780) · correr(925) · crear(730) · cuerpo(706)
decir(784) · decirAviso(578) · decirFrase(573) · escanearCarpeta(611)
escribiendo(1163) · escribirLista(552) · esModoInvitado(526) · fila(1005)
generar(905) · golpear(804) · intentaExtension(632) · intervalo(604)
leerLista(537) · limites(723) · medir(714) · mostrarAviso(583)
mover(856) · multVelocidad(600) · onda(595) · pantallaDespierta(505)
parar(935) · paso(912) · pintar(993) · probarNumerados(644)
probarUno(629) · puedeGuardar(518) · quitar(851) · quitarFila(1048)
reiniciar(941) · rnd(516) · salirSala(1261) · seccion(991)
svgDemonio(676) · volverAlOriginal(1077)
```

### `Citas\index.html`

```
abrirFormulario(656) · aplicarAccesoriosDeActividad(617) · bip(352) · campoActividadId(317)
cargarCatalogos(437) · cargarIdentidadGuardada(489) · cerrarFormulario(695) · confirmarCita(971)
conTiempo(430) · eliminarCita(1002) · escucharCitas(1191) · escucharUsuarios(1237)
esEnPasado(639) · esRelevanteCita(1186) · estaSuprimido(375) · fechaAObjetoISO(738)
fechaLargaISO(743) · firmaCita(1182) · firmaDeUsuarios(310) · formatearFecha(1017)
guardarIdentidad(495) · hoyISO(732) · idNuevo(828) · intentarResaltar(391)
irAProponer(948) · llenarAccesoriosForm(568) · llenarSelectActividades(533) · mostrarApp(516)
mostrarBanner(346) · mostrarPantallaUsuario(500) · moverVestuario(769) · nombreDeCita(305)
nombreDeLado(750) · notificar(364) · obtenerAccesoriosActividad(591) · obtenerAccesoriosMarcados(587)
ordenarAccesorios(629) · otroId(984) · otrosUsuarios(543) · ponerMinimoFecha(649)
preguntarProponer(958) · prepararCampoPara(547) · rechazarCita(990) · renderCitas(1027)
suprimir(372) · verVestuarioDeLaCita(758)
```

### `favor.js`

```
aPagar(1084) · avisarAlOtro(808) · barrerAvisoHuerfano(602) · castigoDe(1047)
cents(665) · cerrar(215) · cerrarFavor(1185) · cerrarRespondida(450)
cobrarCastigo(1133) · cuandoMil(474) · descartar(466) · encolarPropios(981)
escucharRespuestas(512) · esReciente(405) · faltaEn(890) · fueDescartado(462)
hayCajaAbierta(60) · hayFavorVivo(138) · laCapaPropia(859) · laCapaRespuesta(562)
leTocaResponder(506) · liquidarVencidos(1058) · marcarAvisosVistos(626) · marcarAvisoVisto(643)
milisRestantes(882) · minutosDe(1040) · mostrarPropio(897) · mostrarRespuesta(647)
olvidarDescartados(469) · pagarFavor(1080) · pintar(943) · pintarEspera(932)
pintarPrecio(220) · ponerEstilo(81) · precio(1050) · preparar(258)
responder(770) · saldoParaAntes(1095) · siguienteEstado(748) · siguientePropio(846)
textoParaElOtro(762) · veces(164) · yoLocal(115)
```

### `Citas\actividades.html`

```
abrirEditor(642) · abrirRenombrar(863) · actualizarModo(501) · agregar(593)
avisar(496) · cargar(530) · cerrarEditor(757) · cerrarEliminar(959)
cerrarRenombrar(875) · controlesLista(736) · deshecho(763) · editorAvisar(627)
elimAvisar(955) · eliminarActividad(965) · guardarPreset(787) · hayCambiosSinGuardar(807)
idDe(439) · irAAccesorios(816) · listaAccesorios(457) · listaActividades(444)
modalAbierto(772) · normalizar(432) · pintar(471) · ponerTitulo(1046)
renAvisar(858) · renombrarActividad(885) · restaurarLista(744) · todosApagados(1038)
volverDesdeAccesorios(828)
```

### `Retos\centro.html`

```
abrirAddModal(798) · abrirFavor(363) · abrirModal(670) · actualizarBtnAdd(792)
ajustarAlturaPedidos(637) · borrarCompra(772) · borrarDeseo(739) · botonBorrarPedido(765)
camposListos(789) · cerrarAddModal(807) · cerrarModal(689) · comprar(836)
descartados(342) · esA(624) · escuchar(895) · escucharFavores(367)
fila(483) · iniciar(920) · marcarEntregado(882) · marcarNav(416)
miActivar(282) · miPrecio(283) · modalAbierto(440) · nodoSaldo(520)
numConfig(278) · pasoBase(652) · pestana(623) · pintaCaja(529)
pintarBotonesModal(680) · pintarCatalogo(543) · pintarDeseos(562) · pintarFavores(303)
pintarPedidos(586) · pintarTodo(620) · ver(407) · yoFresh(931)
```

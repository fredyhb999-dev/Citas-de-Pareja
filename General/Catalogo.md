# El aviso de 'nuevo' — Catálogo

Movido de `General/GUIA.md`. Contiene el detalle del aviso de packs nuevos en el carrito y las secciones del Centro.

---

### El aviso de "nuevo" (oct-2026)

**Dos lugares** avisan de que hay algo nuevo, y los dos usan **el mismo
criterio**, que vive en **un solo lugar** (`acceso.js` → `nuevosSinPedir()`):

| Dónde | Qué se ve |
|---|---|
| El **carrito** del menú principal (la 🛒 de arriba a la derecha) | Un **punto rojo** |
| Las **secciones del Centro** (Experiencias / Juegos / Extras) | La pastilla **`NUEVO`** en la esquina de su botón |

**Y el criterio son DOS condiciones juntas**, no una (decisión de Fredy):

1. el pack trae **fecha "Nuevo" viva** (`nuevoHasta` > hoy, se pone en el Panel), **y**
2. **todavía no se ha pedido**: no hay solicitud suya en estado `pendiente` ni
   `aprobado`.

Así que **el aviso se apaga** cuando falla cualquiera de las dos: si se vence la
fecha (aunque no lo hayas pedido) o si ya lo pediste (aunque siga la fecha).
Una solicitud **revocada o negada NO cuenta**: eso se puede volver a pedir, así
que el aviso puede reaparecer.

**Las actividades OFICIALES sí avisan (corregido oct-2026).** Salen como tarjeta
en el Centro y se pueden pedir, así que también prenden el punto rojo y la
pastilla mientras no se hayan pedido. Antes se brincaban junto con los fijos
(`if(p.libre || p.oficial) return`), y por eso una oficial recién publicada se
veía `NUEVO` en su tarjeta pero no avisaba en el carrito. **Lo único que se
brinca es `libre`** (Diablitos, Retos, Centro), que no es del catálogo.
Ojo: el `NUEVO` de la **tarjeta** del Centro usa **solo la fecha**
(`nuevoHasta`), así que puede seguir viéndose aunque el aviso ya esté apagado
porque ya se pidió. Son dos criterios distintos a propósito.

**Lo que NO se hace, a propósito:** no se meten fichas de lo que no tienes dentro
de los submenús del menú (Experiencias / Juegos / Retos). Se probó y se descartó:
llenaría los submenús de cosas ajenas. **Los submenús siguen mostrando solo lo
que ya tienes**; lo nuevo sin pedir se ve **solo** en el carrito y en las
secciones del Centro, y de ahí se entra a ver todo el catálogo.

#### Notas de implementación

- El **criterio vive en `acceso.js`**, no copiado en cada página: lo importan
  `index.html` (el menú) y `Tienda/index.html` (el Centro). Si algún día cambia,
  **se cambia en un solo lado**.
- El punto del carrito lo pone `renderPacksDeVerdad()` (en `index.html`), y la
  pastilla de las secciones la pone `marcarSecNuevas()` (en `Tienda/index.html`).
- Los dos nacen **apagados**: el punto es una clase (`conNuevo`) y la pastilla se
  crea con JavaScript. Nada se ve si no hay algo nuevo.
- **PROBADO EN VIVO:** el punto rojo del carrito **sale** cuando hay algo nuevo sin
  pedir, y se apaga al pedirlo o al vencer la fecha. La pastilla de las secciones
  también se comprobó.

# -*- coding: utf-8 -*-
"""Regenera General/Indices-Codigo.md con los numeros reales del codigo.

Por que existe (nov-2026): el indice se actualizaba a mano y se quedo viejo sin
que nadie lo notara (Roles tenia las 198 entradas mal). Este script recalcula
solo lo que es mecanico y respeta lo escrito:

  - el numero de lineas de cada encabezado;
  - los numeros de linea de las tablas (los textos "Para..." NO se tocan);
  - el anexo: agrega las funciones nuevas, quita las que ya no existen y
    corrige las lineas.

Uso:
  python indice.py           regenera el archivo (solo escribe si algo cambio)
  python indice.py --check   no escribe: dice cuantas entradas estan desfasadas
                             y sale con 1 si hay alguna (lo usa revisar.py)
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
DOC = os.path.join(REPO, "General", "Indices-Codigo.md")

RE_ENCABEZADO = re.compile(r"(## `[^`]+`\s*[—–-]\s*)([\d,]+)(\s*líneas.*)")
RE_SECCION = re.compile(r"## `([^`]+)`")
RE_ANEXO = re.compile(r"### `([^`]+)`")
RE_FUNCION = re.compile(r"\s*(?:async\s+)?function\s+([A-Za-z_$][\w$]*)\s*\(")
RE_CONST = re.compile(r"\s*(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=")
RE_TABLA_FNS = re.compile(r"`([A-Za-z_$][\w$]*)\(\)`")
RE_ENTRADA = re.compile(r"([A-Za-z_$][\w$]*)\((\d+)\)")


def leer():
    return io.open(DOC, encoding="utf-8").read().splitlines()


def declaraciones(rel):
    """nombre -> lineas donde se declara (funcion o const/let/var)."""
    src = io.open(os.path.join(REPO, rel.replace("/", os.sep)),
                  encoding="utf-8").read().splitlines()
    d = {}
    for i, l in enumerate(src, 1):
        m = RE_FUNCION.match(l) or RE_CONST.match(l)
        if m:
            d.setdefault(m.group(1), []).append(i)
    return d, len(src), src


def cercana(d, nombre, vieja):
    """La declaracion mas cercana a la linea vieja (para nombres repetidos)."""
    lineas = d.get(nombre)
    if not lineas:
        return None
    return min(lineas, key=lambda x: abs(x - vieja))


def secciones(lineas):
    out = []
    for i, l in enumerate(lineas):
        m = RE_SECCION.match(l)
        if m:
            out.append({"file": m.group(1).replace("\\", "/"), "start": i})
    for i, s in enumerate(out):
        s["end"] = out[i + 1]["start"] if i + 1 < len(out) else len(lineas)
    return out


def anexos(lineas):
    out = []
    for i, l in enumerate(lineas):
        m = RE_ANEXO.match(l)
        if m:
            out.append({"file": m.group(1).replace("\\", "/"), "start": i})
    for b in out:
        j = b["start"] + 1
        while j < len(lineas) and lineas[j].strip() != "```":
            j += 1
        k = j + 1
        while k < len(lineas) and lineas[k].strip() != "```":
            k += 1
        b["open"], b["close"] = j, k
    return out


def renglones(entradas, ancho=92):
    """Arma el anexo en renglones de 'nombre(linea) · ...'."""
    out, act = [], ""
    for nombre, linea in entradas:
        pieza = "%s(%d)" % (nombre, linea)
        cand = (act + " · " + pieza) if act else pieza
        if len(cand) > ancho and act:
            out.append(act)
            act = pieza
        else:
            act = cand
    if act:
        out.append(act)
    return out


def generar(lineas):
    """Devuelve (lineas nuevas, numero de entradas corregidas)."""
    cambios = 0
    # Se recorren los archivos en el orden en que aparecen en el documento y se
    # vuelven a calcular los rangos cada vez: al cambiar el anexo, las lineas de
    # abajo se mueven.
    archivos = [s["file"] for s in secciones(lineas)]
    for rel in archivos:
        try:
            d, total, src = declaraciones(rel)
        except Exception:
            continue

        sec = next(s for s in secciones(lineas) if s["file"] == rel)
        for i in range(sec["start"], sec["end"]):
            m = RE_ENCABEZADO.match(lineas[i])
            if m:
                nuevo = "{:,}".format(total)
                if m.group(2) != nuevo:
                    lineas[i] = m.group(1) + nuevo + m.group(3)
                    cambios += 1

        for i in range(sec["start"], sec["end"]):
            l = lineas[i]
            if not l.startswith("|"):
                continue
            cols = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(cols) < 3:
                continue
            nombres = RE_TABLA_FNS.findall(cols[1])
            numeros = re.findall(r"\d+", cols[2])
            if not nombres or len(nombres) != len(numeros):
                continue
            nuevos = []
            for nombre, vieja in zip(nombres, numeros):
                real = cercana(d, nombre, int(vieja))
                if real is None:
                    nuevos.append(vieja)
                else:
                    nuevos.append(str(real))
                    if str(real) != vieja:
                        cambios += 1
            col3 = " / ".join(nuevos)
            if col3 != cols[2]:
                lineas[i] = "| " + " | ".join(cols[:2] + [col3] + cols[3:]) + " |"

        b = next(x for x in anexos(lineas) if x["file"] == rel)
        viejas = []
        for i in range(b["open"] + 1, b["close"]):
            viejas += RE_ENTRADA.findall(lineas[i])
        nuevas, vistos = [], set()
        for nombre, vieja in viejas:
            real = cercana(d, nombre, int(vieja))
            if real is None:
                cambios += 1          # ya no existe: se quita
                continue
            if nombre in vistos:
                cambios += 1
                continue
            vistos.add(nombre)
            nuevas.append((nombre, real))
            if str(real) != vieja:
                cambios += 1
        for nombre, lineas_decl in d.items():
            if nombre in vistos:
                continue
            if RE_FUNCION.match(src[lineas_decl[0] - 1]):
                nuevas.append((nombre, lineas_decl[0]))
                vistos.add(nombre)
                cambios += 1
        nuevas.sort(key=lambda x: (x[0].lower(), x[0]))
        nuevas_lineas = renglones(nuevas)
        if nuevas_lineas != lineas[b["open"] + 1:b["close"]]:
            lineas[b["open"] + 1:b["close"]] = nuevas_lineas

    return lineas, cambios


def desfase():
    """Cuantas entradas estan mal. No escribe nada."""
    viejas = leer()
    _, cambios = generar(list(viejas))
    return cambios


def regenerar():
    viejas = leer()
    nuevas, cambios = generar(list(viejas))
    if nuevas != viejas:
        io.open(DOC, "w", encoding="utf-8", newline="\n").write("\n".join(nuevas) + "\n")
    return cambios


if __name__ == "__main__":
    if "--check" in sys.argv[1:]:
        n = desfase()
        if n:
            print("indice desfasado: %d entradas. Corre python indice.py." % n)
            sys.exit(1)
        print("OK: el indice coincide con el codigo.")
    else:
        n = regenerar()
        if n:
            print("indice actualizado: %d entradas." % n)
        else:
            print("OK: el indice ya estaba al dia.")

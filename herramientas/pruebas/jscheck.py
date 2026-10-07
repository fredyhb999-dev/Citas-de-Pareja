# -*- coding: utf-8 -*-
import io, sys, re

def check(path):
    s = io.open(path, encoding="utf-8", errors="replace").read()
    prof = []          # pila de (char, linea)
    i = 0
    linea = 1
    n = len(s)
    while i < n:
        c = s[i]
        if c == "\n":
            linea += 1
            i += 1
            continue
        # cadenas
        if c in "\"'`":
            q = c
            i += 1
            while i < n:
                if s[i] == "\\":
                    i += 2
                    continue
                if s[i] == "\n":
                    linea += 1
                if s[i] == q:
                    i += 1
                    break
                i += 1
            continue
        # comentarios
        if c == "/" and i + 1 < n and s[i + 1] == "/":
            while i < n and s[i] != "\n":
                i += 1
            continue
        if c == "/" and i + 1 < n and s[i + 1] == "*":
            i += 2
            while i + 1 < n and not (s[i] == "*" and s[i + 1] == "/"):
                if s[i] == "\n":
                    linea += 1
                i += 1
            i += 2
            continue
        # regex literal: / que NO cierra (no es "//"), precedido por algo que
        # permite un regex. Si no, es division.
        if c == "/":
            previo = ""
            j = i - 1
            while j >= 0 and s[j] in " \t":
                j -= 1
            if j >= 0:
                previo = s[j]
            permite = previo == "" or previo in "(,=:[!&|?{};+-*%~^<>"
            if not permite:
                k = i - 1
                while k >= 0 and (s[k].isalnum() or s[k] == "_"):
                    k -= 1
                palabra = s[k + 1:i].strip()
                if palabra in ("return", "typeof", "case", "in", "of", "new",
                               "delete", "void", "do", "else", "yield", "await", "instanceof"):
                    permite = True
            if permite and i + 1 < n and s[i + 1] != "/" and s[i + 1] != "*":
                i += 1
                en_clase = False
                while i < n:
                    if s[i] == "\\":
                        i += 2
                        continue
                    if s[i] == "\n":
                        linea += 1
                    if s[i] == "[":
                        en_clase = True
                    elif s[i] == "]":
                        en_clase = False
                    elif s[i] == "/" and not en_clase:
                        i += 1
                        if i < n and s[i] in "gimsuyd":
                            i += 1
                        break
                    i += 1
                continue
        if c in "([{":
            prof.append((c, linea))
        elif c in ")]}":
            pares = {")": "(", "]": "[", "}": "{"}
            if not prof:
                print("  FALLA %s: sobra '%s' en linea %d" % (path, c, linea))
                return False
            o, ol = prof.pop()
            if o != pares[c]:
                print("  FALLA %s: '%s' en linea %d cierra '%s' de la linea %d"
                      % (path, c, linea, o, ol))
                return False
        i += 1
    if prof:
        o, ol = prof[-1]
        print("  FALLA %s: queda abierto '%s' de la linea %d" % (path, o, ol))
        return False
    print("  OK     %s" % path)
    return True

todo = True
for p in sys.argv[1:]:
    todo = check(p) and todo
sys.exit(0 if todo else 1)
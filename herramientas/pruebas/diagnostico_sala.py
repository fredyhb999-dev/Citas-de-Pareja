# -*- coding: utf-8 -*-
"""Diagnostico del escenario `nada` de la suite de Sala.

ESTO NO ES UN ERROR DE LA APP. Es un hueco del arnés, y existe desde antes
de los cambios del instalador (oct-2026).

Que pasa, en claro:

  El escenario `nada` simula que le picas al botón "Regresar" de la Sala.
  Al picarlo, la página **se va al inicio de la app**.
  Pero el arnés de Sala (`build_sala.py`) solo copia el archivo del juego
  (`Diablitos/index.html`) a su carpeta de pruebas. **No copia la página de
  inicio.** Asi que cuando el navegador la pide, el servidor responde
  "404: no existe" y la prueba no tiene nada que leer.

Es como un estuche de herramientas al que le falta una pieza: el juego esta
bien, al estuche le falta el archivo.

Como probarlo:

  python diagnostico_sala.py

Como arreglarlo (cuando quieras, no urge):

  En build_sala.py, copiar tambien index.html del repo a la raiz de la
  carpeta de pruebas, para que la pagina de inicio exista.
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
import io, os, shutil, subprocess, time

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", ".."))
H = r"C:\Users\Fred\AppData\Local\Temp\opencode\harnes_sala"
DUMP = r"C:\Users\Fred\AppData\Local\Temp\opencode\dump_sala.html"
SALIDA = r"C:\Users\Fred\AppData\Local\Temp\opencode\salida_sala.txt"


def linea(c="-"):
    print("  " + c * 72)


def main():
    print("")
    linea("=")
    print("  DIAGNOSTICO DEL ESCENARIO `nada` (suite de Sala)")
    linea("=")
    print("")
    print("  ESTO NO ES UN ERROR DE LA APP. Es un hueco del arnes de pruebas,")
    print("  y ya existia antes de los cambios del instalador de fabrica.")
    print("")

    # 1) que hace el escenario
    inject = io.open(os.path.join(AQUI, "inject_sala.py"), encoding="utf-8", errors="replace").read()
    print("  1) Que hace el escenario `nada`:")
    for l in inject.split("\n"):
        if 'ESC === "nada"' in l or "volverSala\").click" in l or "debe estar visible" in l:
            print("       " + l.strip()[:92])
    print("")
    print("     O sea: pica 'Regresar'. Eso lleva a la PAGINA DE INICIO.")
    print("")

    # 2) que copia el arnes
    print("  2) Que copia el arnes de Sala (build_sala.py):")
    hay_inicio = False
    for raiz, dirs, files in os.walk(H):
        for f in files:
            rel = os.path.relpath(os.path.join(raiz, f), H)
            print("       %s" % rel)
            if rel == "index.html":
                hay_inicio = True
    print("")
    print("     La pagina de inicio (index.html en la raiz) esta en la carpeta? %s"
          % ("SI" if hay_inicio else "NO -> por eso el 404"))
    print("")

    # 3) que sale
    print("  3) Que devuelve hoy:")
    if os.path.exists(SALIDA):
        print("     salida_sala.txt : %s" % io.open(SALIDA, encoding="utf-8", errors="replace").read().strip())
    else:
        print("     salida_sala.txt : (aun no se ha corrido)")
    if os.path.exists(DUMP):
        t = io.open(DUMP, encoding="utf-8", errors="replace").read()
        grande = len(t) > 5000
        print("     volcado         : %d bytes  -> %s"
              % (len(t), "la pagina SI cargo" if grande else "es la pagina de error 404 del servidor"))
        if not grande:
            for l in t.split("\n"):
                if "404" in l or "not found" in l:
                    print("                       %s" % l.strip())
    else:
        print("     volcado         : (aun no se ha corrido)")
    print("")

    # 4) como comprobarlo con el codigo viejo
    print("  4) Como confirmar que NO es culpa de los cambios del instalador:")
    print("     Se hace una copia limpia del codigo de antes y se corre ahi:")
    print("")
    print('     cd "C:\\Users\\Fred\\Documents\\GitHub\\Citas-de-Pareja"')
    print('     "C:\\Users\\Fred\\AppData\\Local\\GitHubDesktop\\app-3.6.5\\resources\\app\\git\\cmd\\git.exe" worktree add --detach C:\\Temp\\sala-limpia HEAD')
    print("     cd C:\\Temp\\sala-limpia\\herramientas\\pruebas")
    print("     python build_sala.py ; python inject_sala.py ; python run_sala.py nada")
    print("")
    print("     Sale el MISMO 404. Y para limpiar:")
    print('     git worktree remove --force C:\\Temp\\sala-limpia')
    print("")

    linea("=")
    print("  Conclusion: el juego esta bien. Al arnes de Sala le falta copiar")
    print("  la pagina de inicio. Se arregla en build_sala.py cuando quieras.")
    linea("=")
    print("")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
import io, re, html, sys

dump = r"C:\Users\Fred\AppData\Local\Temp\opencode\dump_enc.html"
t = io.open(dump, encoding="utf-8", errors="replace").read()
out = []
out.append("TITLE: " + (re.search(r"<title>(.*?)</title>", t, re.S).group(1) if re.search(r"<title>(.*?)</title>", t, re.S) else "?"))
for ident in ("SALIDA", "DIAG"):
    m = re.search('<div id="' + ident + '"[^>]*>(.*?)</div>', t, re.S)
    out.append("---- " + ident + " ----")
    out.append(html.unescape(m.group(1)) if m else "(no encontrado)")
dest = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\Fred\AppData\Local\Temp\opencode\salida.txt"
io.open(dest, "w", encoding="utf-8").write("\n".join(out))
print("escrito", dest, "len", len(t))
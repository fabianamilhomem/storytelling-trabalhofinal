"""Captura as cinco áreas (viewport e página inteira). Uso: python -I -X utf8 capturar.py <pasta_saida> [largura altura]"""
import sys, pathlib
from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parents[1]
URL = (RAIZ / "index.html").as_uri()
out = RAIZ / "testes" / "capturas" / (sys.argv[1] if len(sys.argv) > 1 else "atual"); out.mkdir(parents=True, exist_ok=True)
W = int(sys.argv[2]) if len(sys.argv) > 2 else 1440
H = int(sys.argv[3]) if len(sys.argv) > 3 else 780
VISTAS = ["inicio", "metodologia", "resultados", "resultados/cobertura", "resultados/precisao", "resultados/sintese", "execucoes", "fontes"]
with sync_playwright() as p:
    br = p.chromium.launch(args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    pg = br.new_page(viewport={"width": W, "height": H})
    erros = []
    pg.on("pageerror", lambda e: erros.append(str(e)))
    pg.on("console", lambda m: erros.append(m.text) if m.type == "error" else None)
    for v in VISTAS:
        pg.goto(URL + "#" + v); pg.reload(); pg.wait_for_timeout(1200)
        n = v.replace("/", "-")
        try:
            pg.evaluate("window.CenaAbertura && CenaAbertura.pular()")
        except Exception: pass
        pg.wait_for_timeout(500)
        pg.screenshot(path=str(out / f"{n}.png"))
        pg.screenshot(path=str(out / f"{n}_full.png"), full_page=True)
    print("erros:", erros)
    br.close()

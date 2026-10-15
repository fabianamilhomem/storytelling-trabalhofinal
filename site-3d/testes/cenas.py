"""Captura a abertura (estado final) e as 7 estações 3D. Uso: python -I -X utf8 site-3d/testes/cenas.py"""
import pathlib
from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parents[1]
URL = (RAIZ / "index.html").as_uri()
OUT = RAIZ / "testes" / "capturas"; OUT.mkdir(exist_ok=True)

with sync_playwright() as p:
    br = p.chromium.launch(args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    pg = br.new_page(viewport={"width": 1440, "height": 780})
    erros = []
    pg.on("pageerror", lambda e: erros.append(str(e)))
    pg.on("console", lambda m: erros.append(m.text) if m.type == "error" else None)
    pg.goto(URL + "#inicio"); pg.wait_for_timeout(800)
    pg.click("#abertura-pular"); pg.wait_for_timeout(500)
    pg.locator("#palco-abertura").screenshot(path=str(OUT / "cena_abertura_final.png"))
    pg.goto(URL + "#metodologia"); pg.wait_for_timeout(600)
    for i in range(7):
        pg.click(f'#estacoes button[data-i="{i}"]'); pg.evaluate(f"CenaArq.ir({i}, true)"); pg.wait_for_timeout(900)
        pg.locator("#arquitetura").screenshot(path=str(OUT / f"cena_estacao_{i+1}.png"))
    print("erros:", erros)
    br.close()

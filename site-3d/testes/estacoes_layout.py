"""Captura as 7 estações no layout lado a lado em um viewport. Uso: python -I -X utf8 estacoes_layout.py LARGURA ALTURA PASTA"""
import sys, pathlib
from playwright.sync_api import sync_playwright
RAIZ = pathlib.Path(__file__).resolve().parents[1]
w, h, pasta = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
out = RAIZ / "testes" / "capturas" / pasta; out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    br = p.chromium.launch(args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    pg = br.new_page(viewport={"width": w, "height": h})
    pg.goto((RAIZ / "index.html").as_uri() + "#metodologia"); pg.wait_for_timeout(800)
    pg.evaluate("document.getElementById('arquitetura').scrollIntoView({block:'start',behavior:'instant'})")
    for i in range(7):
        pg.click(f'#estacoes button[data-i="{i}"]'); pg.evaluate(f"CenaArq.ir({i}, true)"); pg.wait_for_timeout(500)
        pg.screenshot(path=str(out / f"{w}x{h}_est{i+1}.png"))
    br.close()

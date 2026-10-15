"""Teste de fumaça do site 3D (Playwright). Uso: python -I -X utf8 site-3d/testes/fumaca.py [chromium|firefox|edge]
Gera capturas em site-3d/testes/capturas/ e imprime erros de console."""
import pathlib, sys, json
from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parents[1]
URL = (RAIZ / "index.html").as_uri()
OUT = RAIZ / "testes" / "capturas"; OUT.mkdir(exist_ok=True)
NAV = sys.argv[1] if len(sys.argv) > 1 else "chromium"
ROTAS = ["#inicio", "#metodologia", "#resultados", "#resultados/cobertura", "#resultados/precisao", "#resultados/sintese", "#execucoes", "#fontes"]

with sync_playwright() as p:
    if NAV == "edge": br = p.chromium.launch(channel="msedge")
    elif NAV == "firefox": br = p.firefox.launch()
    else: br = p.chromium.launch(args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    pg = br.new_page(viewport={"width": 1440, "height": 780})
    erros = []
    pg.on("console", lambda m: erros.append(("console." + m.type, m.text)) if m.type in ("error", "warning") else None)
    pg.on("pageerror", lambda e: erros.append(("pageerror", str(e))))
    pg.goto(URL); pg.wait_for_timeout(2500)
    info = pg.evaluate("""() => ({three: !!window.THREE, dados: !!window.DADOS, ab: window.CenaAbertura && CenaAbertura.estado(),
        canvasOk: (()=>{const c=document.getElementById('cv-abertura'); return c.width+'x'+c.height + ' hidden=' + c.hidden})()})""")
    print("info", json.dumps(info))
    for i, r in enumerate(ROTAS):
        pg.goto(URL + r); pg.wait_for_timeout(1800 if r in ("#inicio", "#metodologia") else 600)
        pg.screenshot(path=str(OUT / f"{NAV}_{i:02d}_{r.strip('#').replace('/', '-')}.png"), full_page=False)
        print("rota", r, pg.evaluate("window.__site.estado()"), "scrollH", pg.evaluate("document.documentElement.scrollWidth"), "<=", pg.evaluate("innerWidth"))
    print("ERROS:", len(erros))
    for e in erros[:20]: print(" ", e)
    br.close()

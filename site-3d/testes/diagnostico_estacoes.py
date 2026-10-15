"""Diagnóstico: dimensões do palco/canvas, razão cena:painel e rótulos por estação. Uso: python -I -X utf8 diagnostico_estacoes.py L A PASTA [direto]"""
import sys, json, pathlib
from playwright.sync_api import sync_playwright
RAIZ = pathlib.Path(__file__).resolve().parents[1]
w, h, pasta = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
modo = sys.argv[4] if len(sys.argv) > 4 else "sequencial"
out = RAIZ / "testes" / "capturas" / pasta; out.mkdir(parents=True, exist_ok=True)
JS = """() => { const r = e => { const b = e.getBoundingClientRect(); return [Math.round(b.left), Math.round(b.top), Math.round(b.right), Math.round(b.bottom)]; };
  const pal = document.getElementById('palco-arq'), cv = document.getElementById('cv-arq'), pn = document.querySelector('.painel-estacao');
  const labs = [...document.querySelectorAll('#palco-arq .rotulo.is-on')].map(e => ({t: e.textContent, r: r(e)}));
  return { palco: r(pal), canvas: r(cv), cvAttr: [cv.width, cv.height], painel: r(pn), razao: +(pal.getBoundingClientRect().width / document.getElementById('arquitetura').getBoundingClientRect().width).toFixed(3), labs, iw: innerWidth }; }"""
with sync_playwright() as p:
    br = p.chromium.launch(args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    pg = br.new_page(viewport={"width": w, "height": h})
    erros = []; pg.on("pageerror", lambda e: erros.append(str(e))); pg.on("console", lambda m: erros.append(m.text) if m.type == "error" else None)
    pg.goto((RAIZ / "index.html").as_uri() + "#metodologia"); pg.wait_for_timeout(900)
    pg.evaluate("document.getElementById('arquitetura').scrollIntoView({block:'start',behavior:'instant'})")
    seq = [6, 5] if modo == "direto" else list(range(7))
    for i in seq:
        pg.click(f'#estacoes button[data-i="{i}"]')
        if modo != "natural": pg.evaluate(f"CenaArq.ir({i}, true)")
        pg.wait_for_timeout(2600 if modo == "natural" else 700)
        d = pg.evaluate(JS)
        print(f"est{i+1}", json.dumps(d, ensure_ascii=False))
        pg.screenshot(path=str(out / f"{w}x{h}_{modo}_est{i+1}.png"))
    print("erros", erros)
    br.close()

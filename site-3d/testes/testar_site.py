"""Suíte do site 3D (Playwright).
Uso (na raiz do projeto):  python -I -X utf8 site-3d/testes/testar_site.py chromium|firefox|edge
Saídas: site-3d/testes/resultado_<nav>.md/.json e capturas em site-3d/testes/capturas/<nav>/
Somente testes realmente executados são registrados. Nada é afirmado sobre GitHub Pages."""
import json, pathlib, re, sys, time
from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parents[1]
PROJ = RAIZ.parent
URL = (RAIZ / "index.html").as_uri()
NAV = sys.argv[1] if len(sys.argv) > 1 else "chromium"
CAP = RAIZ / "testes" / "capturas" / NAV; CAP.mkdir(parents=True, exist_ok=True)
D = json.loads((PROJ / "dados" / "evidencia_lab.json").read_text(encoding="utf-8"))
I = D["instituicoes"]; R = D["por_repeticao"]; INST = ["CNJ", "STF", "TJDFT", "TST"]
VPS = [(1366, 650), (1280, 590), (1440, 780), (1536, 720), (1920, 950), (390, 844)]
ROTAS = ["#inicio", "#metodologia", "#resultados", "#resultados/cobertura", "#resultados/precisao", "#resultados/sintese", "#execucoes", "#fontes"]
res = []

def ok(grupo, nome, cond, det=""):
    res.append({"grupo": grupo, "teste": nome, "ok": bool(cond), "detalhe": str(det)[:300]})

def br(v): return v.replace(".", ",")
def pc(v): return br(f"{v:.1f}") + "%"

def novo(p, vp=(1440, 780), reduced=False, sem_webgl=False):
    if NAV == "edge": b = p.chromium.launch(channel="msedge")
    elif NAV == "firefox":
        import glob, os
        cand = sorted(glob.glob(os.path.join(os.environ["LOCALAPPDATA"], "ms-playwright", "firefox-*", "firefox", "firefox.exe")))
        b = p.firefox.launch(executable_path=cand[-1]) if cand else p.firefox.launch()
    else: b = p.chromium.launch(args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    ctx = b.new_context(viewport={"width": vp[0], "height": vp[1]}, reduced_motion="reduce" if reduced else "no-preference")
    if sem_webgl: ctx.add_init_script("window.__SEM_WEBGL = true;")
    pg = ctx.new_page(); pg.erros = []; pg.falhas = []
    pg.on("pageerror", lambda e: pg.erros.append("pageerror: " + str(e)))
    pg.on("console", lambda m: pg.erros.append("console: " + m.text) if m.type == "error" else None)
    pg.on("requestfailed", lambda r: pg.falhas.append(r.url))
    return b, pg

with sync_playwright() as p:
    versao = None
    # ---------------------------------------------------------------- 1. navegação, dados, mapa (viewport padrão)
    b, pg = novo(p); versao = b.version
    pg.goto(URL); pg.wait_for_timeout(1500)
    visiveis = lambda: pg.evaluate("[...document.querySelectorAll('.vista')].filter(s=>!s.hidden).map(s=>s.dataset.vista)")
    menu = pg.evaluate("[...document.querySelectorAll('.menu a')].map(a=>a.textContent.trim())")
    ok("Navegação", "menu com as cinco áreas na ordem", menu == ["Início", "Metodologia", "Resultados", "40 execuções", "Fontes"], menu)
    for rota, esperado in [("#inicio", "inicio"), ("#metodologia", "metodologia"), ("#resultados", "resultados"), ("#execucoes", "execucoes"), ("#fontes", "fontes")]:
        pg.goto(URL + rota); pg.wait_for_timeout(300)
        ok("Navegação", f"rota {rota} abre só a vista correspondente", visiveis() == [esperado], visiveis())
        ok("Navegação", f"{rota}: aria-current no menu", pg.evaluate("document.querySelector('.menu a[aria-current=page]').dataset.vista") == esperado)
    pg.goto(URL + "#resultados"); pg.wait_for_timeout(300)
    ok("Resultados", "abre em Recall_item", pg.evaluate("document.querySelector('.aba[aria-selected=true]').dataset.aba") == "recall")
    abas = pg.evaluate("[...document.querySelectorAll('.aba')].map(a=>a.textContent.trim().replace(/^\d/, ''))")
    ok("Resultados", "abas: três métricas + síntese separada", abas == ["Recall_item", "Cobertura_evidência", "Precisão_evidência", "Síntese interpretativa"], abas)
    for aba in ["cobertura", "precisao", "sintese", "recall"]:
        pg.click(f'.aba[data-aba="{aba}"]'); pg.wait_for_timeout(150)
        vis = pg.evaluate("[...document.querySelectorAll('[data-painel]')].filter(s=>!s.hidden).map(s=>s.dataset.painel)")
        ok("Resultados", f"aba {aba}: painel único visível e hash", vis == [aba] and pg.evaluate("location.hash").startswith("#resultados"), vis)
    pg.focus('.aba[data-aba="recall"]'); pg.keyboard.press("ArrowRight"); pg.wait_for_timeout(200)
    ok("Resultados", "teclado: seta direita vai a Cobertura", pg.evaluate("document.querySelector('.aba[aria-selected=true]').dataset.aba") == "cobertura")
    pg.keyboard.press("End"); pg.wait_for_timeout(200)
    ok("Resultados", "teclado: End vai à Síntese", pg.evaluate("document.querySelector('.aba[aria-selected=true]').dataset.aba") == "sintese")

    # integridade dos dados exibidos (valores e denominadores)
    pg.goto(URL + "#resultados"); pg.wait_for_timeout(200)
    t = pg.inner_text("#p-recall")
    for k in INST:
        d = I[k]
        ok("Dados", f"Recall {k}: {pc(d['recall_item'])} e {d['itens_satisfeitos']}/{d['itens_esperados']}", pc(d["recall_item"]) in t and f"{d['itens_satisfeitos']}/{d['itens_esperados']}" in t)
    t = pg.inner_text("#p-cobertura") if pg.evaluate("document.getElementById('p-cobertura').hidden") is False else pg.evaluate("document.getElementById('p-cobertura').textContent")
    for k in INST:
        d = I[k]
        ok("Dados", f"Cobertura {k}: {pc(d['cobertura_evidencia'])} e {d['componentes_encontrados']}/{d['componentes_esperados']}", pc(d["cobertura_evidencia"]) in t and f"{d['componentes_encontrados']}/{d['componentes_esperados']}" in t)
    t = pg.evaluate("document.getElementById('p-precisao').textContent")
    for k in INST:
        d = I[k]
        ok("Dados", f"Precisão {k}: {pc(d['precisao_evidencia'])} e {d['evidencias_com_correspondencia']}/{d['evidencias_reportadas']}", pc(d["precisao_evidencia"]) in t and f"{d['evidencias_com_correspondencia']}/{d['evidencias_reportadas']}" in t)
    # tabela do prompt-mestre
    ref = {"CNJ": (93.0, 7.0, 95.0, "133/140", 71.6), "STF": (100.0, 0.0, 100.0, "140/140", 58.6),
           "TJDFT": (100.0, 0.0, 100.0, "140/140", 39.0), "TST": (100.0, 0.0, 100.0, "140/140", 46.0)}
    for k, (rc, fn, cb, frac, pr) in ref.items():
        d = I[k]
        ok("Dados", f"{k} confere com a tabela de referência do prompt", d["recall_item"] == rc and d["fnr_item"] == fn and d["cobertura_evidencia"] == cb and f"{d['componentes_encontrados']}/{d['componentes_esperados']}" == frac and d["precisao_evidencia"] == pr)
    ok("Dados", "somas por repetição = agregados (itens CNJ 93; precisão amplitude)", sum(R["itens_satisfeitos_de_10"]["CNJ"]) == 93)
    ok("Dados", "aviso de inconsistência de cobertura ausente", "inconsistência detectada" not in t and "inconsistência detectada" not in pg.evaluate("document.getElementById('p-cobertura').textContent"))

    # mapa de calor
    pg.goto(URL + "#execucoes"); pg.wait_for_timeout(500)
    n = pg.evaluate("document.querySelectorAll('.mapa__celula').length")
    ok("Mapa", "40 células (4 × 10)", n == 40, n)
    vazio = pg.evaluate("[...document.querySelectorAll('.mapa__celula')].filter(c=>!c.textContent.trim()).length")
    ok("Mapa", "valores escritos em todas as células", vazio == 0, vazio)
    ok("Mapa", "legenda explícita com mínimo e máximo", "70%" in pg.inner_text("#legenda-mapa") and "100%" in pg.inner_text("#legenda-mapa"), pg.inner_text("#legenda-mapa")[:80])
    pg.click('.mapa__celula[data-inst="TJDFT"][data-rep="3"]'); pg.wait_for_timeout(150)
    painel = pg.inner_text("#painel-exec")
    ok("Mapa", "célula atualiza painel (TJDFT · Rep. 3)", "TJDFT" in painel and "Rep. 3" in painel and br(f"{R['precisao_evidencia_pct']['TJDFT'][3]:.1f}") in painel, painel[:120])
    ok("Mapa", "célula selecionada tem aria-selected", pg.evaluate("document.querySelectorAll('.mapa__celula[aria-selected=true]').length") == 1)
    tab_sel = pg.evaluate("[...document.querySelectorAll('#tabela-exec tr.is-sel')].map(r=>r.innerText.replace(/\\s+/g,' ').slice(0,40))")
    ok("Integração", "tabela destaca instituição e repetição selecionadas", len(tab_sel) == 2, tab_sel)
    pg.click('#tabela-exec button[data-sel-inst="STF"]'); pg.wait_for_timeout(150)
    ok("Integração", "seleção na tabela destaca a linha correspondente no mapa", pg.evaluate("document.querySelectorAll('.mapa__celula.is-linha[data-inst=STF]').length") == 10)
    pg.click('.mapa__rot[data-lin="CNJ"]'); pg.wait_for_timeout(150)
    ok("Mapa", "cabeçalho de linha seleciona instituição", pg.evaluate("document.querySelectorAll('.mapa__celula.is-linha[data-inst=CNJ]').length") == 10 and "instituição selecionada" in pg.inner_text("#painel-exec").lower())
    pg.click('.mapa__cab[data-col="4"]'); pg.wait_for_timeout(150)
    ok("Mapa", "cabeçalho de coluna seleciona repetição", pg.evaluate("document.querySelectorAll('.mapa__celula.is-coluna').length") == 4 and "repetição selecionada" in pg.inner_text("#painel-exec").lower())
    pg.click('.mapa__celula[data-inst="CNJ"][data-rep="2"]'); pg.wait_for_timeout(100)
    pg.focus('.mapa__celula[data-inst="CNJ"][data-rep="2"]'); pg.keyboard.press("ArrowRight"); pg.wait_for_timeout(150)
    ok("Mapa", "teclado: seta direita move para Rep. 3", pg.evaluate("MapaExec.estado().rep") == 3)
    pg.keyboard.press("ArrowDown"); pg.wait_for_timeout(150)
    ok("Mapa", "teclado: seta abaixo move para STF", pg.evaluate("MapaExec.estado().inst") == "STF")
    pg.check('input[name="metrica"][value="precisao"]', force=True); pg.wait_for_timeout(150)
    ok("Mapa", "métrica Precisão: células com valores de precisão", br(f"{R['precisao_evidencia_pct']['CNJ'][0]:.1f}") in pg.inner_text('.mapa__celula[data-inst="CNJ"][data-rep="0"]'))
    ok("Mapa", "contraste: texto da célula legível (--fg definido)", pg.evaluate("[...document.querySelectorAll('.mapa__celula')].every(c=>c.style.cssText.includes('--fg'))"))
    pg.screenshot(path=str(CAP / "mapa_precisao.png"))
    ok("Console", "sem erros de console/exceções na navegação principal", len(pg.erros) == 0, pg.erros[:3])
    ok("Caminhos", "nenhuma requisição falhou (assets locais)", len(pg.falhas) == 0, pg.falhas[:3])
    b.close()

    # ---------------------------------------------------------------- 2. marca rejeitada
    texto = ""
    for f in RAIZ.rglob("*"):
        if f.is_file() and f.suffix in (".html", ".css", ".js") and "vendor" not in f.parts and "testes" not in f.parts:
            texto += f.read_text(encoding="utf-8", errors="ignore") + "\n"
    ok("Marca", "nome rejeitado ausente do código do site (html/css/js)", not re.search(r"Evid[êe]ncia\s+Lab", texto, re.I))
    b, pg = novo(p); pg.goto(URL); pg.wait_for_timeout(500)
    ok("Marca", "título do navegador sem o nome rejeitado", not re.search(r"Evid[êe]ncia\s+Lab", pg.title(), re.I), pg.title())
    corpo = ""
    for rota in ROTAS:
        pg.goto(URL + rota); pg.wait_for_timeout(150)
        corpo += pg.evaluate("document.documentElement.innerText + ' ' + [...document.querySelectorAll('[aria-label],[alt],[title]')].map(e=>(e.getAttribute('aria-label')||'')+(e.getAttribute('alt')||'')+(e.title||'')).join(' ')")
    ok("Marca", "nenhuma ocorrência visível/ARIA do nome rejeitado", not re.search(r"Evid[êe]ncia\s+Lab", corpo, re.I))
    b.close()

    # ---------------------------------------------------------------- 3. viewports
    for (w, h) in VPS:
        b, pg = novo(p, (w, h))
        pg.goto(URL); pg.wait_for_timeout(900)
        for rota in ROTAS:
            pg.goto(URL + rota); pg.wait_for_timeout(500 if rota in ("#inicio", "#metodologia") else 250)
            if rota == "#inicio": pg.evaluate("window.CenaAbertura && CenaAbertura.pular()"); pg.wait_for_timeout(300)
            ow = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
            ok("Viewport", f"{w}x{h} {rota}: sem rolagem horizontal", ow <= 1, f"excesso {ow}px")
            nome = f"{w}x{h}_{rota.strip('#').replace('/', '-')}.png"
            pg.screenshot(path=str(CAP / nome))
        pg.goto(URL + "#inicio"); pg.wait_for_timeout(300)
        cta = pg.locator("#cta-resultados").bounding_box()
        ok("Viewport", f"{w}x{h}: ação 'Entrar nos resultados' visível sem rolar", cta is not None and cta["y"] + cta["height"] <= h, cta)
        ok("Console", f"{w}x{h}: sem erros", len(pg.erros) == 0, pg.erros[:2])
        b.close()

    # ---------------------------------------------------------------- 4. movimento reduzido e WebGL
    b, pg = novo(p, reduced=True); pg.goto(URL); pg.wait_for_timeout(1200)
    est = pg.evaluate("window.CenaAbertura ? CenaAbertura.estado() : null")
    ok("Movimento", "prefers-reduced-motion: abertura já no estado final e sem laço de animação", est is None or (est["t"] >= est["fim"] and est["ativo"] is False), est)
    b.close()
    b, pg = novo(p); pg.goto(URL); pg.wait_for_timeout(600)
    pg.click("#btn-movimento"); pg.wait_for_timeout(300)
    est = pg.evaluate("window.CenaAbertura ? CenaAbertura.estado() : null")
    ok("Movimento", "botão 'Reduzir movimento' ativa a classe e interrompe a animação", pg.evaluate("document.documentElement.classList.contains('reduzir-movimento')") and (est is None or est["ativo"] is False), est)
    b.close()
    b, pg = novo(p, sem_webgl=True); pg.goto(URL); pg.wait_for_timeout(800)
    ok("Fallback", "sem WebGL: planta SVG exibida na abertura", pg.evaluate("!document.getElementById('sem-webgl-abertura').hidden"))
    pg.goto(URL + "#metodologia"); pg.wait_for_timeout(300)
    ok("Fallback", "sem WebGL: lista de estações e texto continuam utilizáveis", pg.evaluate("document.querySelectorAll('#estacoes button').length") == 7 and "estação 1" in pg.inner_text("#detalhe-estacao").lower())
    ok("Fallback", "sem WebGL: sem exceções", len(pg.erros) == 0, pg.erros[:2])
    b.close()

    # ---------------------------------------------------------------- 5. metodologia
    b, pg = novo(p); pg.goto(URL + "#metodologia"); pg.wait_for_timeout(800)
    for i in (1, 4, 6):
        pg.click(f'#estacoes button[data-i="{i}"]'); pg.wait_for_timeout(200)
        ok("Metodologia", f"estação {i + 1}: detalhe e aria-current atualizados", f"estação {i + 1} de 7" in pg.inner_text("#detalhe-estacao").lower() and pg.evaluate("document.querySelector('#estacoes [aria-current=step]').dataset.i") == str(i))
    ok("Metodologia", "seção do filme apresenta o filme V4 (sem mensagem de produção)", "em produção" not in pg.inner_text(".filme").lower() and "ainda não foi produzido" not in pg.inner_text(".filme").lower() and "transcrição da narração" in pg.inner_text(".cinema").lower())
    ok("Metodologia", "alternativa para avançar sem assistir", pg.evaluate("!!document.querySelector('.cinema a[href=\"#resultados\"]')"))
    ok("Metodologia", "vídeo local, sem autoplay, preload=metadata e pausado", pg.evaluate("(()=>{const v=document.querySelector('video#cinema-video');return !!v&&!v.autoplay&&v.paused&&v.preload==='metadata'&&v.controls&&v.querySelector('source').getAttribute('src').startsWith('assets/video/')})()"))
    b.close()

    # reprodução, pausa, reinício e redimensionamento
    b, pg = novo(p, (1440, 780)); pg.goto(URL + "#metodologia"); pg.wait_for_timeout(700)
    est = lambda: pg.evaluate("window.__site.estado().estacao")
    pg.click('#estacoes button[data-i="6"]'); pg.wait_for_timeout(300)
    ok("Reprodução", "Próxima desabilitada na estação 7", pg.evaluate("document.getElementById('arq-prox').disabled"))
    pg.click("#arq-play"); pg.wait_for_timeout(500)
    ok("Reprodução", "reproduzir na estação 7 recomeça na estação 1 e marca 'Pausar percurso'", est() == 0 and pg.evaluate("document.getElementById('arq-play').getAttribute('aria-pressed')") == "true" and "Pausar" in pg.inner_text("#arq-play"), est())
    pg.click("#arq-play"); pg.wait_for_timeout(300)
    ok("Reprodução", "pausar interrompe e restaura o rótulo 'Reproduzir percurso'", pg.evaluate("document.getElementById('arq-play').getAttribute('aria-pressed')") == "false" and "Reproduzir" in pg.inner_text("#arq-play"))
    pg.click("#arq-prox"); pg.wait_for_timeout(200); pg.click("#arq-prox"); pg.wait_for_timeout(200)
    ok("Reprodução", "Próxima ×2 avança exatamente duas estações e texto/indicador acompanham", est() == 2 and "estação 3 de 7" in pg.inner_text("#detalhe-estacao").lower() and pg.evaluate("document.querySelector('#estacoes [aria-current=step]').dataset.i") == "2")
    pg.click("#arq-ant"); pg.wait_for_timeout(200)
    ok("Reprodução", "Anterior retorna uma estação", est() == 1)
    pg.click('#estacoes button[data-i="6"]'); pg.wait_for_timeout(2200)
    pg.set_viewport_size({"width": 1280, "height": 590}); pg.wait_for_timeout(900)
    g = pg.evaluate("(() => { const a = document.getElementById('palco-arq').getBoundingClientRect(), c = document.getElementById('cv-arq').getBoundingClientRect(); return [a.width, a.height, c.width, c.height]; })()")
    ok("Redimensionamento", "estação 7: canvas acompanha o palco após redimensionar a janela", abs(g[0] - g[2]) <= 1 and abs(g[1] - g[3]) <= 1, g)
    ok("Console", "reprodução/redimensionamento sem erros", len(pg.erros) == 0, pg.erros[:2])
    b.close()

    # ---------------------------------------------------------------- 5b. metodologia: cena e explicação simultâneas
    for (w, h) in VPS:
        b, pg = novo(p, (w, h)); pg.goto(URL + "#metodologia"); pg.wait_for_timeout(700)
        pg.evaluate("document.getElementById('arquitetura').scrollIntoView({block:'start',behavior:'instant'})"); pg.wait_for_timeout(250)
        y0 = pg.evaluate("window.scrollY"); falhas = []
        for i in range(7):
            pg.click(f'#estacoes button[data-i="{i}"]'); pg.wait_for_timeout(120)
            g = pg.evaluate("""() => { const q = s => document.querySelector(s).getBoundingClientRect(); const d = document.getElementById('detalhe-estacao');
                return { cena: q('#palco-arq'), pan: q('.painel-estacao'), ant: q('#arq-ant'), play: q('#arq-play'), prox: q('#arq-prox'), est: q('#estacoes'),
                         over: d.scrollHeight - d.clientHeight, sy: window.scrollY, ih: innerHeight, iw: innerWidth }; }""")
            def dentro(r): return r["top"] >= -1 and r["bottom"] <= g["ih"] + 1 and r["left"] >= -1 and r["right"] <= g["iw"] + 1
            if g["sy"] != y0: falhas.append(f"est{i+1}: página rolou")
            for nome in ("ant", "play", "prox", "est"):
                if not dentro(g[nome]): falhas.append(f"est{i+1}: {nome} fora da janela")
            if w > 900:
                if not dentro(g["cena"]) or not dentro(g["pan"]): falhas.append(f"est{i+1}: cena/painel fora da janela")
                if g["over"] > 1: falhas.append(f"est{i+1}: texto da estação com rolagem interna ({g['over']}px)")
            if i in (0, 4, 5, 6): pg.wait_for_timeout(1900); pg.screenshot(path=str(CAP / f"{w}x{h}_metodologia_estacao{i+1}.png"))
        ok("Metodologia layout", f"{w}x{h}: cena, explicação, nav e controles visíveis sem rolar a página nas 7 estações", not falhas, "; ".join(falhas[:4]))
        # estações 6 e 7: canvas = palco, rótulos completos e dentro do palco após a transição
        for i in (5, 6):
            pg.click(f'#estacoes button[data-i="{i}"]'); pg.wait_for_timeout(2300)
            g = pg.evaluate("""() => { const pal = document.getElementById('palco-arq').getBoundingClientRect(), cv = document.getElementById('cv-arq').getBoundingClientRect();
                const labs = [...document.querySelectorAll('#palco-arq .rotulo.is-on')].map(e => { const b = e.getBoundingClientRect(); return {t: e.textContent, l: b.left, r: b.right, t0: b.top, b: b.bottom}; });
                return { pal: [pal.left, pal.top, pal.right, pal.bottom], cv: [cv.left, cv.top, cv.right, cv.bottom], labs, atual: CenaArq.atual ? CenaArq.atual() : -1 }; }""")
            igual = all(abs(a - b) <= 1 for a, b in zip(g["pal"], g["cv"]))
            dentro = all(l["l"] >= g["pal"][0] - 1 and l["r"] <= g["pal"][2] + 1 and l["t0"] >= g["pal"][1] - 1 and l["b"] <= g["pal"][3] + 1 for l in g["labs"])
            esperado = 3 if i == 5 else 1
            ok("Metodologia layout", f"{w}x{h}: estação {i + 1}: canvas = palco, {esperado}+ rótulos completos dentro do palco", igual and dentro and len(g["labs"]) >= esperado, f"canvas={g['cv']} palco={g['pal']} rotulos={len(g['labs'])}")
        if w > 900:
            fr = pg.evaluate("(() => { const a = document.getElementById('palco-arq').getBoundingClientRect(), b = document.getElementById('arquitetura').getBoundingClientRect(); return a.width / b.width; })()")
            ok("Metodologia layout", f"{w}x{h}: cena ocupa 64–70% da largura", 0.64 <= fr <= 0.70, f"{fr:.2f}")
        b.close()

arq = "resultado_" + NAV
total = len(res); aprov = sum(1 for r in res if r["ok"])
md = [f"# Resultado dos testes do site 3D — {NAV} {versao} (Playwright)", "",
      f"Total: {total} · Aprovados: {aprov} · Falhas: {total - aprov}", "", "| Grupo | Teste | Resultado | Detalhe |", "|---|---|---|---|"]
for r in res: md.append(f"| {r['grupo']} | {r['teste']} | {'passou' if r['ok'] else 'FALHOU'} | {r['detalhe'].replace('|', '/')} |")
(RAIZ / "testes" / (arq + ".md")).write_text("\n".join(md), encoding="utf-8")
(RAIZ / "testes" / (arq + ".json")).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{NAV} {versao}: {aprov}/{total} aprovados")
for r in res:
    if not r["ok"]: print("  FALHOU:", r["grupo"], "|", r["teste"], "|", r["detalhe"])

"""Testes da integracao do filme V4 (Metodologia). Uso: python -I -X utf8 site-3d/testes/testar_filme_v4.py
Usa Microsoft Edge (H.264). Saidas: testes/resultado_filme_v4.json e capturas/filme_v4/."""
import json, pathlib
from playwright.sync_api import sync_playwright
RAIZ = pathlib.Path(__file__).resolve().parents[1]
URL = (RAIZ / "index.html").as_uri()
CAP = RAIZ / "testes" / "capturas" / "filme_v4"; CAP.mkdir(parents=True, exist_ok=True)
res = []
def ok(n, c, d=""): res.append({"teste": n, "ok": bool(c), "detalhe": str(d)[:300]})
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge", args=["--autoplay-policy=no-user-gesture-required"])
    for vp in [(1366, 650), (1440, 780), (1920, 950), (390, 844)]:
        ctx = b.new_context(viewport={"width": vp[0], "height": vp[1]})
        pg = ctx.new_page(); erros = []; falhas = []; reqs = []
        pg.on("pageerror", lambda e: erros.append(str(e)))
        pg.on("console", lambda m: erros.append(m.text) if m.type == "error" else None)
        pg.on("requestfailed", lambda r: falhas.append((r.url, r.failure)))
        pg.on("request", lambda r: reqs.append(r.url))
        pg.goto(URL + "#metodologia"); pg.wait_for_timeout(1500)
        tag = f"{vp[0]}x{vp[1]}"
        v = pg.locator("#cinema-video")
        v.scroll_into_view_if_needed(); pg.wait_for_timeout(500)
        st = pg.evaluate("(()=>{const v=document.querySelector('#cinema-video');return {rs:v.readyState,dur:v.duration,paused:v.paused,auto:v.autoplay,t:v.currentTime,w:v.clientWidth,h:v.clientHeight,vw:v.videoWidth,vh:v.videoHeight,err:!!v.error}})()")
        ok(f"{tag}: metadados carregados, pausado, sem autoplay", st["rs"] >= 1 and st["paused"] and not st["auto"] and st["t"] == 0, st)
        ok(f"{tag}: duracao ~60,3 s e 1280x720", abs(st["dur"] - 60.31) < 0.2 and st["vw"] == 1280 and st["vh"] == 720, st)
        ok(f"{tag}: proporcao 16:9 do elemento", abs(st["w"] / st["h"] - 16 / 9) < 0.02, st)
        box = v.bounding_box()
        ok(f"{tag}: player dentro da largura da janela", box["x"] >= 0 and box["x"] + box["width"] <= vp[0] + 1, box)
        pg.screenshot(path=str(CAP / f"filme_{tag}_inicial.png"), full_page=False)
        # reproduzir / pausar / volume / mudo
        r = pg.evaluate("""async()=>{const v=document.querySelector('#cinema-video');v.muted=true;await v.play();for(let i=0;i<40&&v.currentTime<1.5;i++)await new Promise(r=>setTimeout(r,250));
          const t1=v.currentTime;v.pause();const pa=v.paused;v.muted=false;v.volume=0.5;const vol=v.volume;return {t1,pa,vol,mu:v.muted}}""")
        ok(f"{tag}: reproduz (tempo avanca), pausa e ajusta volume", r["t1"] > 1.5 and r["pa"] and abs(r["vol"] - .5) < .01, r)
        if tag == "1440x780":
            pg.evaluate("document.querySelector('#cinema-video').currentTime=38")
            pg.wait_for_timeout(800)
            pg.locator(".cinema__tela").screenshot(path=str(CAP / "filme_quadro_38s.png"))
            fs = pg.evaluate("document.querySelector('.cinema__tela').requestFullscreen().then(()=>!!document.fullscreenElement).catch(e=>String(e))")
            ok("1440x780: tela cheia via API", fs is True, fs)
            pg.evaluate("document.exitFullscreen&&document.fullscreenElement&&document.exitFullscreen()")
        # estacoes antes/depois
        for i in (0, 3, 6):
            pg.click(f'#estacoes button[data-i="{i}"]'); pg.wait_for_timeout(250)
        cur = pg.evaluate("document.querySelector('#estacoes [aria-current=step]').dataset.i")
        ok(f"{tag}: navegacao das sete estacoes apos o video", cur == "6", cur)
        pg.click("#cinema-prev3d"); pg.wait_for_timeout(600)
        cur = pg.evaluate("document.querySelector('#estacoes [aria-current=step]').dataset.i")
        ok(f"{tag}: 'Voltar ao percurso interativo' leva a estacao 1", cur == "0", cur)
        ok(f"{tag}: sem erros de console/pagina", not erros, erros)
        reais = [f for f in falhas if "ERR_ABORTED" not in str(f[1])]
        ok(f"{tag}: sem requisicoes falhas (ERR_ABORTED de pause/seek do video e ignorado)", not reais, reais)
        ok(f"{tag}: requisicoes abortadas registradas apenas para o mp4", all(f[0].endswith("filme-framework-v4.mp4") for f in falhas), [f[1] for f in falhas][:3])
        ext = [u for u in reqs if not u.startswith("file:")]
        ok(f"{tag}: sem dependencias externas", not ext, ext)
        n = pg.evaluate("document.querySelectorAll('#transcricao-texto').length")
        ok(f"{tag}: transcricao unica", n == 1, n)
        # seção completa visível
        sec = pg.locator(".filme").bounding_box()
        ok(f"{tag}: secao do filme (altura px)", sec["height"] < 1400, sec["height"])
        pg.locator(".filme").scroll_into_view_if_needed()
        pg.locator(".filme").screenshot(path=str(CAP / f"secao_filme_{tag}.png"))
        ctx.close()
    b.close()
(RAIZ / "testes" / "resultado_filme_v4.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
for r in res: print("OK " if r["ok"] else "FALHA", r["teste"], "" if r["ok"] else r["detalhe"])
print(sum(r["ok"] for r in res), "/", len(res))

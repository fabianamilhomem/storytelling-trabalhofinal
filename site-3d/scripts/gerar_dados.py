"""Gera assets/js/dados.js a partir de ../../dados/evidencia_lab.json (somente leitura).
Uso (na raiz do projeto):  python -I -X utf8 site-3d/scripts/gerar_dados.py
Nenhum valor é digitado à mão: tudo vem do JSON. Valores ausentes ficam ausentes.
"""
import json, pathlib

RAIZ = pathlib.Path(__file__).resolve().parents[2]
D = json.loads((RAIZ / "dados" / "evidencia_lab.json").read_text(encoding="utf-8"))
INST = D["experimento"]["instituicoes"]
R = D["por_repeticao"]

def cobertura_rep(k):
    v = R["cobertura_evidencia_pct"][k]
    return v if isinstance(v, list) else [float(v)] * 10

out = {
    "experimento": D["experimento"],
    "definicoes": D["metricas_definicoes"],
    "instituicoes": {k: {x: y for x, y in D["instituicoes"][k].items() if x != "duracao_chamadas_ms"} for k in INST},
    "ordem": INST,
    "repeticoes": {
        k: {
            "recall": R["recall_item_pct"][k],
            "precisao": R["precisao_evidencia_pct"][k],
            "itens": R["itens_satisfeitos_de_10"][k],
            "cobertura": cobertura_rep(k),
            "fnr": R["fnr_item_pct"][k],
            "recall_criterio": R["recall_por_criterio_pct"][k],
        }
        for k in INST
    },
    "fontes_por_serie": {
        "recall": R["recall_item_pct"]["fonte"],
        "precisao": R["precisao_evidencia_pct"]["fonte"],
        "itens": R["itens_satisfeitos_de_10"]["fonte"],
        "cobertura": R["cobertura_evidencia_pct"]["fonte"],
        "fnr": R["fnr_item_pct"]["fonte"],
        "criterio": R["recall_por_criterio_pct"]["fonte"],
    },
    "indisponivel": R["contagem_evidencias_por_repeticao"],
    "indexacao": R["numeracao"],
    "sensibilidade": D["sensibilidade_limiar_precisao_pct"],
    "operacional": {k: D["operacional"][k] for k in ("custo_total_usd", "chamadas_llm", "tokens_prompt", "tokens_completion", "nota", "fonte_custo")},
    "portais": D["fontes_primarias_portais"],
    "verificacao_cnj": D["verificacao_dados_complementares_cnj"],
    "caso_cnj": D["casos_interpretativos"],
}
dest = RAIZ / "site-3d" / "assets" / "js" / "dados.js"
dest.write_text("/* gerado por scripts/gerar_dados.py a partir de dados/evidencia_lab.json */\nwindow.DADOS = "
                + json.dumps(out, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
print("ok", dest, dest.stat().st_size, "bytes")

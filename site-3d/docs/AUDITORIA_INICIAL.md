# Auditoria inicial (2026-10-14)

## Estado dos originais (preservados; manifesto SHA-256 em MANIFESTO_ORIGINAIS_sha256.txt, 533 arquivos)
- `dados/`: JSON consolidado (`evidencia_lab.json`), scripts Python que geram o index antigo, templates `*.pre_paletas.*`.
- `design-systems/evidencia-lab/`: site anterior (index.html estático 181 KB, assets/app.js, styles.css, mapa.css, fontes Inter/Sora, 218 previews).
- `design-systems/evidencia-lab - Bkp01/`: backup (236 arquivos). Não tocado.
- `testes/`: suítes Playwright (Chromium, Firefox, Edge) e relatórios do site antigo.
- `fontes/dissertacao.txt`, `Telas_Modelos/` (4 PNG de referência).
- `.claude/skills/img-to-html` e `to-wireframe` (fluxo de aprovação por etapas; a missão atual dispensa gates).

## Ferramentas verificadas
- Node 24.19, npm 11.17, Python 3.13.7, Playwright 1.54 (Chromium, Firefox, Edge instalados), Pillow.
- FFmpeg 9.0.2 (full build) operacional (WinGet). Nenhuma reinstalação.
- Kairogen MCP: autenticado; 882 créditos (histórico). Nenhum crédito consumido nesta fase.

## Dados
`dados/evidencia_lab.json` confere com a tabela do prompt-mestre:
CNJ 93,0/7,0/95,0 (133/140)/71,6 · STF 100/0/100 (140/140)/58,6 · TJDFT 100/0/100 (140/140)/39,0 (38,97) · TST 100/0/100 (140/140)/46,0.
Sem divergências. Por repetição (Rep. 0–9): Recall, Precisão, Itens (de 10), Cobertura (CNJ por rep.; demais = 100 em todas) e Recall por critério.
NÃO disponível nas fontes: contagem de evidências reportadas/corretas por repetição (só agregado de 10 repetições). O site não inventa esses valores.
O campo `_meta.titulo` do JSON contém o nome rejeitado; ele nunca é exibido.

## Decisões técnicas
- Site estático (sem backend), scripts clássicos (funciona em file://), Three.js r147 UMD local em vendor/.
- Dados: `scripts/gerar_dados.py` lê o JSON original (somente leitura) e gera `assets/js/dados.js`.
- Fontes locais: Fraunces (títulos editoriais), Inter (texto), IBM Plex Mono (valores).

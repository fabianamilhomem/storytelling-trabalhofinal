# Relatório — reconstrução do site 3D (fases 0 a 4) · 2026-10-14

## Estado
Site reconstruído em `site-3d/`. Filme NÃO produzido (fases 5–6 aguardam autorização explícita para consumir créditos).
Créditos Kairogen consumidos nesta fase: 0 (saldo 882, conforme última consulta).

## Direção de arte
Cartório Mineral + Planta Normativa (ver DIRECAO_DE_ARTE.md): papel/calcário claros, linhas de projeto azuis, latão. Tipografia Fraunces / Inter / IBM Plex Mono (locais).

## Arquitetura
- Estático, sem backend, scripts clássicos (abre por duplo clique em file://), caminhos relativos → compatível com GitHub Pages.
- Three.js r147 (UMD, local, `vendor/`): abertura (`cena-abertura.js`) e percurso de 7 estações (`cena-arquitetura.js`), geometria real.
- Dados: `scripts/gerar_dados.py` lê `dados/evidencia_lab.json` (somente leitura) e gera `assets/js/dados.js`.
- Gráficos: SVG gerado a partir dos dados (unidades de item, componentes, evidências com/sem correspondência).
- Mapa de calor 4×10 com 3 métricas, legenda, seleção de célula/linha/coluna, teclado, tabela e painel integrados; orientação transposta em telas estreitas.

## Testes executados (site-3d/testes/)
`testar_site.py`: 126 verificações por navegador — Chromium 139: 126/126 · Edge 155: 126/126 · Firefox 156: 126/126.
Cobre: 5 áreas, abas e teclado, dados e denominadores contra o JSON, tabela de referência do prompt, mapa e integração, ausência do nome rejeitado, 6 viewports (1366×650, 1280×590, 1440×780, 1536×720, 1920×950, 390×844) sem rolagem horizontal, movimento reduzido, fallback sem WebGL, ausência de `<video>` na abertura, ausência de requisições falhas.
Capturas: `testes/capturas/` (inspecionadas visualmente).
Integridade: 533/533 arquivos originais conferem com `docs/MANIFESTO_ORIGINAIS_sha256.txt`.

## Dados
Sem divergência entre o prompt-mestre e o JSON. Indisponível nas fontes e portanto não exibido: contagem de evidências por repetição.

## Limitações
- GitHub Pages NÃO foi testado (sem publicação). Execução local validada via file://.
- WebGL nos testes é por SwiftShader (software); desempenho em GPU real não medido.
- Filme: ver PLANO_VIDEO_v2.md. Piloto Seedance 2.5 falhou duas vezes (reembolsado); causa não identificada.
- Metodologia 3D usa formas abstratas; não reproduz portais oficiais.

## Executar
Abrir `site-3d/index.html` ou `python -m http.server` em `site-3d/` e acessar http://localhost:8000.
Regerar dados: `python -I -X utf8 site-3d/scripts/gerar_dados.py`. Testes: `python -I -X utf8 site-3d/testes/testar_site.py chromium|edge|firefox`.
Publicar: copiar o conteúdo de `site-3d/` (exceto `testes/` e `docs/` se desejado) para a raiz ou `/docs` do repositório e habilitar GitHub Pages.

# Relatório — integração do filme V4 à seção Metodologia

Status: **integração concluída e testada localmente.** O filme continua sendo uma **versão de revisão** (não definitiva, não publicada, não validada institucionalmente).

## 1. Arquivos
### Criados
| Arquivo | Descrição |
|---|---|
| `assets/video/filme-framework-v4.mp4` | Cópia do filme (local definitivo no site) |
| `assets/video/poster-filme-v4.jpg` | Poster leve (118 KB), quadro em 3,0 s do próprio filme |
| `docs/RELATORIO_INTEGRACAO_FILME_V4.md` | Este relatório |
| `docs/_backup_pre_filme_v4/` | Cópias anteriores de `index.html`, `site.css`, `app.js`, `testar_site.py` e do resultado-base `resultado_chromium_baseline.*` |
| `testes/testar_filme_v4.py`, `testes/resultado_filme_v4.json`, `testes/_saida_filme_v4.txt`, `testes/capturas/filme_v4/` | Teste e capturas da integração |
### Alterados
| Arquivo | Alteração |
|---|---|
| `index.html` | Bloco `.cinema` substituído (poster SVG, selo "Em produção" e botão de legendas removidos; entram vídeo, apresentação, nota e transcrição) |
| `assets/css/site.css` | `.cinema__poster` e `.cinema__estado` substituídos por `.cinema__video`, `.cinema__erro`, `.filme__apresentacao`, `.filme__texto`, `.filme__info`, `.filme__nota` |
| `assets/js/app.js` | Texto da transcrição atualizado; tratamento de erro de carregamento do vídeo |
| `testes/testar_site.py` | Duas verificações que descreviam o estado "em produção" e "nenhum vídeo na abertura" foram atualizadas |
### Preservados
Arquivo original `producao-filme/final/FILME_PREVIA_V4.mp4` (não movido nem alterado), todas as demais versões e a pasta de produção.

## 2. Integridade
SHA-256 de origem e da cópia: `51d561f3c8d67f6d4943786bae2d86352ab05bc11cdc1c65e834a25b5cc30274` (idênticos). 75.195.237 bytes. O arquivo tem 75 MB: para GitHub Pages o limite de arquivo é 100 MB; o carregamento inicial é só de metadados (`preload="metadata"`).

## 3. Player
`<video controls preload="metadata" playsinline poster=...>` com `<source src="assets/video/filme-framework-v4.mp4" type="video/mp4">`: caminho relativo, 16:9 (`aspect-ratio`, `object-fit: contain`), controles nativos (reprodução, pausa, volume, tela cheia, teclado), sem `autoplay`, sem iframe, sem serviço externo. Mensagem `role="alert"` caso o arquivo não carregue; a transcrição permanece disponível.

## 4. Textos
- Selo: "FILME · CONTRIBUIÇÃO CIENTÍFICA" (já existente; mantido). Título: "O framework em cerca de um minuto".
- Texto de apresentação, informações complementares ("Duração aproximada: 60 segundos · Formato: 16:9 · Narração em português brasileiro") e nota metodológica: conforme solicitado, literalmente.
- Removido: "O filme ainda não foi produzido. Esta é uma prévia estática…", "Duração prevista", "Legendas (indisponível)", "Roteiro da narração previsto" e a nota "será revisado quando o áudio existir".
- Controle de legendas: **removido** (não existe arquivo de legendas); em seu lugar, "Transcrição da narração disponível abaixo.", pois a transcrição está implementada.
- `Voltar ao percurso interativo` e `Avançar sem assistir`: comportamento preservado.
- **Transcrição da narração:** substituída pelas seis falas N1–N6 de `producao-filme/roteiro/NARRACAO_FILME_v3.md`, conferidas por script contra o texto no site (**764 caracteres**, o mesmo número do texto enviado à narração, segundo o relatório da narração). A transcrição anterior no site era o roteiro antigo, que não correspondia ao filme. Aparece uma única vez (`#transcricao-texto`). **Não foi conferida de ouvido**: a pronúncia/fidelidade do áudio sintético a esse texto não foi auditada.

## 5. Testes
### Filme (Microsoft Edge, `testar_filme_v4.py`): 53/53
Em 1366×650, 1440×780, 1920×950 e 390×844:
- metadados carregados, pausado, sem autoplay, duração ≈ 60,3 s, 1280×720;
- elemento 16:9 e dentro da largura da janela;
- reprodução (tempo avança), pausa, volume e silenciar;
- tela cheia pela API (1440×780);
- navegação nas estações 1, 4 e 7 depois da reprodução; "Voltar ao percurso interativo" leva à estação 1;
- sem erros de console/página, sem dependências externas, transcrição única, seção de altura < 1400 px.
Observação: o evento `requestfailed` com `ERR_ABORTED` do próprio MP4 (cancelamento ao pausar/buscar) é registrado e excluído da checagem; nenhuma outra falha.
### Suíte anterior (Chromium do Playwright, `testar_site.py`): 155/156
Linha de base anterior: 156/156. A única falha é "nenhuma requisição falhou (assets locais)" por causa do MP4, **no Chromium empacotado do Playwright**, que não decodifica H.264 e aborta o pedido; no Edge o mesmo arquivo reproduz. Todos os demais testes (estações, resultados, execuções, fontes, paletas, caminhos) passaram. Os resultados de Firefox e Edge da suíte antiga (`resultado_firefox.*`, `resultado_edge.*`) **não foram reexecutados** e permanecem os anteriores.
### Capturas
`testes/capturas/filme_v4/`: `secao_filme_*.png`, `filme_*_inicial.png`, `filme_quadro_38s.png`.

## 6. Limitações
- **Não assisti nem ouvi o filme**: os testes comprovam que o arquivo carrega, reproduz e que o tempo avança; não avaliam imagem, som ou sincronia.
- GitHub Pages **não foi testado**; a publicação não foi validada. Há apenas teste via `file://`.
- Safari e navegadores móveis reais não foram testados (apenas viewport de 390×844 no Edge).
- Não há legendas sincronizadas; a transcrição é texto corrido.
- Arquivo de 75 MB (bitrate 10 Mb/s): pode ser pesado em conexões lentas; reduzir exigiria nova exportação, não feita aqui.
- A nota metodológica e a transcrição seguem as pendências abertas do projeto (P3 status "preliminar", P4 especialistas do TJDFT, P5 autoria): a transcrição menciona "três especialistas do TJDFT" conforme o roteiro aprovado.

## 7. Preservação
Sete estações 3D, mecanismo de navegação, dados experimentais, demais seções, paletas e identidade visual não foram alterados (nenhum arquivo de `dados/`, `fontes/`, `assets/js/cena-*.js`, `mapa.js`, `graficos.js` ou `dados.js` foi tocado; a suíte confirmou o restante). Nenhum conteúdo gerado, nenhum crédito consumido.

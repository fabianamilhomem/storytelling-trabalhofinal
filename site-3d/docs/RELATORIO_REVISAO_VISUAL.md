# Relatório — revisão visual do site 3D · 2026-10-14

Escopo: somente revisão e reconstrução visual do site (`site-3d/`). Nenhum vídeo, keyframe ou áudio foi gerado; **nenhum crédito Kairogen foi consumido** nesta etapa.

## 1. Diagnóstico da versão anterior
Ver `docs/REVISAO_DIRECAO_DE_ARTE.md` (12 itens). Em síntese: papel bege com grade quadriculada em todas as páginas, abertura em diagrama (uma folha e placas minúsculas em palco 16:10 com borda), metodologia em linha reta de caixas iguais, resultados em quatro colunas idênticas repetidas, cena e página com a mesma cor e luz.

## 2. Direção de arte implementada — “Da pedra à luz”
- **Narrativa visual:** a norma é uma estela de pedra num salão em penumbra; ao se decompor em requisitos verificáveis a luz aumenta. A metodologia vai da penumbra do salão (estação 1) à luz do dia da interpretação humana (estação 7).
- **Abertura:** cena em plano aberto (largura inteira), estela bisotada de calcário com painel de basalto e dez ranhuras (4 teal + 6 índigo), luz-chave rasante com sombra longa, duas fileiras de placas (a do critério IN84 sobre um pódio) que se destacam da estela e acendem a “abertura” de latão, câmera que parte de baixo e abre; textos sobrepostos à sombra; “Pular abertura” e “Rever abertura” preservados.
- **Metodologia:** câmera sobre sete ambientes distintos (luz, material, enquadramento e plataforma próprios):
  1. estela e requisitos (salão de basalto, luz quente);
  2. quatro portais com silhuetas diferentes e régua de latão comum (mesmos critérios);
  3. coleta: agente de IA recorrente (cerâmica branca, lente), zona circular própria, folhas e linhas tracejadas; “localiza e organiza, não decide”;
  4. organização: arquivo com dez colunas alinhadas aos requisitos;
  5. comparação: rotina determinística em latão (pórtico mecânico), evidências do modelo de um lado e **gabarito em câmara fechada atrás de uma barreira**, sem ligação com o agente; par sem correspondência com linha tracejada e anel vazio (não “falso”);
  6. métricas: três instrumentos de formas diferentes, sem valores;
  7. pessoa auditora (material próprio), lente, mesa, janela de luz do dia; o agente ao fundo.
  Legenda sobreposta em tipografia real e trilho de sete estações em HTML; texto completo, “o que esta estação não é” e controles (anterior, reproduzir, próxima) fora do canvas.
- **Resultados:** uma faixa de cor profunda por pergunta (teal, índigo, ferrugem) com número e pergunta em escala grande; cada métrica com forma própria: pontos por item em livro-razão (Recall_item), pilhas por repetição em quatro colunas (Cobertura_evidência), barras proporcionais ao nº de evidências reportadas com hachura “sem correspondência direta” (Precisão_evidência). Síntese em faixa escura com três leituras numeradas. Navegação interna preservada (Recall, Cobertura, Precisão, Síntese).
- **40 execuções:** mapa 4×10 maior, valores nas células, chips segmentados, painel escuro de execução selecionada; tabelas e seleção integrada preservadas.
- **Fontes, Início, rodapé:** índice tipográfico dos caminhos, números gigantes, leitura em duas colunas, blocos de fonte em duas colunas.
- **Removidos:** grade de fundo, filetes dourados, cartões em caixa, rótulos mono com borda, logotipo em quadro.
- **Texto corrigido:** duplicações na definição do Recall_item, da Cobertura e na nota de sensibilidade.

## 3. Capturas antes e depois
- Antes: `testes/capturas/antes/` e `testes/capturas/antes_estado_real/`.
- Depois: `testes/capturas/proto7/` (cinco áreas, 1440×780), `testes/capturas/cena_estacao_1..7.png` (sete ambientes), `testes/capturas/{chromium,edge,firefox}/` (viewports).

## 4. Arquivos alterados/criados
`index.html`, `assets/css/site.css`, `assets/js/{cena-comum.js (novo), cena-abertura.js, cena-arquitetura.js, graficos.js, app.js, util.js}`, `testes/{capturar.py (novo), cenas.py, testar_site.py}`, `docs/{REVISAO_DIRECAO_DE_ARTE.md, RELATORIO_REVISAO_VISUAL.md}`. Não alterados: `assets/js/{dados.js, mapa.js}`, originais e backups.

## 5. Autoavaliação (seção 10 do pedido)
| Pergunta | Resposta |
|---|---|
| A abertura poderia ser confundida com template? | Não: ambiente arquitetônico com estela, luz rasante, sombra e câmera. Ainda é estilizada, não fotorrealista. |
| Objetos 3D parecem físicos? | Sim: peças bisotadas, materiais distintos, sombras projetadas. Figuras (agente, pessoa) permanecem esquemáticas. |
| Profundidade e hierarquia? | Sim: primeiro plano, pódio, parede e fresta; texto sobre sombra. |
| Parece sequência de slides? | Resultados e metodologia têm ritmos distintos; há seções repetitivas (livro-razão de quatro linhas). |
| Fundo compete com dados? | Não: fundo liso; cenas só nas áreas narrativas. |
| Funciona sem animação? | Sim: movimento reduzido leva ao estado final; fallback sem WebGL e lista de estações preservados. |
| Identidade deliberada? | Sim, mas depende de aprovação visual da usuária. |

## 6. Limitações e problemas remanescentes
- Renderização WebGL testada somente por software (SwiftShader); desempenho em GPU real não medido. Para contenção, a abertura para o laço ao terminar; sombras 1024 px; pixel ratio ≤ 1,5.
- Agente e pessoa auditora são figuras estilizadas simples; o portal é abstrato (nenhuma marca ou interface oficial).
- Estação 5: a barreira do gabarito lê-se melhor em ângulo de câmera mais alto; revisão fina possível.
- Poster do filme ainda é ilustração estática; o filme não existe (fases 5–6 aguardam autorização de créditos).
- GitHub Pages não foi testado.

## 7. Testes executados (após o redesenho)
- `testes/testar_site.py`: **126/126** em Chromium 139, **126/126** em Edge 155, **126/126** em Firefox 156 (navegação, dados × JSON, mapa/integração, nome rejeitado ausente, viewports 1366×650, 1280×590, 1440×780, 1536×720, 1920×950 e 390×844 sem rolagem horizontal e com a ação “Entrar nos resultados” visível, movimento reduzido, fallback sem WebGL, sem erros de console).
- Correções feitas durante os testes: largura do texto da abertura em telas largas (a coluna colapsava a ~240 px e estendia o palco), ordem texto→cena em telas estreitas, timeouts de captura por renderização por software (sombras 1024 px, pixel ratio ≤ 1,5, laço da abertura encerra ao concluir), rótulo numérico das abas.
- Integridade dos originais: 533/533 arquivos conferem com `MANIFESTO_ORIGINAIS_sha256.txt`.
- Capturas das sete estações (`cena_estacao_1..7.png`) e das cinco áreas inspecionadas visualmente.

## 8. Créditos Kairogen
Saldo consultado ao final: **882 créditos** (inalterado; nenhuma geração nesta etapa).

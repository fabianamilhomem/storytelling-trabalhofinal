# Resultado dos testes do site 3D — chromium 139.0.7258.5 (Playwright)

Total: 156 · Aprovados: 155 · Falhas: 1

| Grupo | Teste | Resultado | Detalhe |
|---|---|---|---|
| Navegação | menu com as cinco áreas na ordem | passou | ['Início', 'Metodologia', 'Resultados', '40 execuções', 'Fontes'] |
| Navegação | rota #inicio abre só a vista correspondente | passou | ['inicio'] |
| Navegação | #inicio: aria-current no menu | passou |  |
| Navegação | rota #metodologia abre só a vista correspondente | passou | ['metodologia'] |
| Navegação | #metodologia: aria-current no menu | passou |  |
| Navegação | rota #resultados abre só a vista correspondente | passou | ['resultados'] |
| Navegação | #resultados: aria-current no menu | passou |  |
| Navegação | rota #execucoes abre só a vista correspondente | passou | ['execucoes'] |
| Navegação | #execucoes: aria-current no menu | passou |  |
| Navegação | rota #fontes abre só a vista correspondente | passou | ['fontes'] |
| Navegação | #fontes: aria-current no menu | passou |  |
| Resultados | abre em Recall_item | passou |  |
| Resultados | abas: três métricas + síntese separada | passou | ['Recall_item', 'Cobertura_evidência', 'Precisão_evidência', 'Síntese interpretativa'] |
| Resultados | aba cobertura: painel único visível e hash | passou | ['cobertura'] |
| Resultados | aba precisao: painel único visível e hash | passou | ['precisao'] |
| Resultados | aba sintese: painel único visível e hash | passou | ['sintese'] |
| Resultados | aba recall: painel único visível e hash | passou | ['recall'] |
| Resultados | teclado: seta direita vai a Cobertura | passou |  |
| Resultados | teclado: End vai à Síntese | passou |  |
| Dados | Recall CNJ: 93,0% e 93/100 | passou |  |
| Dados | Recall STF: 100,0% e 100/100 | passou |  |
| Dados | Recall TJDFT: 100,0% e 100/100 | passou |  |
| Dados | Recall TST: 100,0% e 100/100 | passou |  |
| Dados | Cobertura CNJ: 95,0% e 133/140 | passou |  |
| Dados | Cobertura STF: 100,0% e 140/140 | passou |  |
| Dados | Cobertura TJDFT: 100,0% e 140/140 | passou |  |
| Dados | Cobertura TST: 100,0% e 140/140 | passou |  |
| Dados | Precisão CNJ: 71,6% e 154/215 | passou |  |
| Dados | Precisão STF: 58,6% e 153/261 | passou |  |
| Dados | Precisão TJDFT: 39,0% e 166/426 | passou |  |
| Dados | Precisão TST: 46,0% e 201/437 | passou |  |
| Dados | CNJ confere com a tabela de referência do prompt | passou |  |
| Dados | STF confere com a tabela de referência do prompt | passou |  |
| Dados | TJDFT confere com a tabela de referência do prompt | passou |  |
| Dados | TST confere com a tabela de referência do prompt | passou |  |
| Dados | somas por repetição = agregados (itens CNJ 93; precisão amplitude) | passou |  |
| Dados | aviso de inconsistência de cobertura ausente | passou |  |
| Mapa | 40 células (4 × 10) | passou | 40 |
| Mapa | valores escritos em todas as células | passou | 0 |
| Mapa | legenda explícita com mínimo e máximo | passou | Recall_item (%)
70%
100%
Escala relativa ao intervalo observado nas 40 execuções |
| Mapa | célula atualiza painel (TJDFT · Rep. 3) | passou | EXECUÇÃO SELECIONADA

TJDFT · Rep. 3
Itens satisfeitos
10 de 10
Recall_item
100,0%
FNR_item
0,0%
Cobertura_evidência
100 |
| Mapa | célula selecionada tem aria-selected | passou |  |
| Integração | tabela destaca instituição e repetição selecionadas | passou | ['TJDFT 100,0% (100/100) 100,0% (140/140) ', 'Rep. 3 10 100,0% 100,0% 43,5%'] |
| Integração | seleção na tabela destaca a linha correspondente no mapa | passou |  |
| Mapa | cabeçalho de linha seleciona instituição | passou |  |
| Mapa | cabeçalho de coluna seleciona repetição | passou |  |
| Mapa | teclado: seta direita move para Rep. 3 | passou |  |
| Mapa | teclado: seta abaixo move para STF | passou |  |
| Mapa | métrica Precisão: células com valores de precisão | passou |  |
| Mapa | contraste: texto da célula legível (--fg definido) | passou |  |
| Console | sem erros de console/exceções na navegação principal | passou | [] |
| Caminhos | nenhuma requisição falhou (assets locais) | FALHOU | ['file:///C:/Fabiana/Mestrado%20IDP/Storytelling%20de%20Dados/Trabalhos/Dashboard_PortalTransparencia/site-3d/assets/video/filme-framework-v4.mp4'] |
| Marca | nome rejeitado ausente do código do site (html/css/js) | passou |  |
| Marca | título do navegador sem o nome rejeitado | passou | Início · Auditoria normativa assistida por IA generativa · Milhomem (2026) |
| Marca | nenhuma ocorrência visível/ARIA do nome rejeitado | passou |  |
| Viewport | 1366x650 #inicio: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1366x650 #metodologia: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1366x650 #resultados: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1366x650 #resultados/cobertura: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1366x650 #resultados/precisao: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1366x650 #resultados/sintese: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1366x650 #execucoes: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1366x650 #fontes: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1366x650: ação 'Entrar nos resultados' visível sem rolar | passou | {'x': 69.4375, 'y': 530.984375, 'width': 202.90625, 'height': 46} |
| Console | 1366x650: sem erros | passou | [] |
| Viewport | 1280x590 #inicio: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1280x590 #metodologia: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1280x590 #resultados: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1280x590 #resultados/cobertura: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1280x590 #resultados/precisao: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1280x590 #resultados/sintese: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1280x590 #execucoes: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1280x590 #fontes: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1280x590: ação 'Entrar nos resultados' visível sem rolar | passou | {'x': 43.515625, 'y': 472.234375, 'width': 202.90625, 'height': 46} |
| Console | 1280x590: sem erros | passou | [] |
| Viewport | 1440x780 #inicio: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1440x780 #metodologia: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1440x780 #resultados: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1440x780 #resultados/cobertura: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1440x780 #resultados/precisao: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1440x780 #resultados/sintese: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1440x780 #execucoes: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1440x780 #fontes: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1440x780: ação 'Entrar nos resultados' visível sem rolar | passou | {'x': 108.953125, 'y': 655.140625, 'width': 202.90625, 'height': 46} |
| Console | 1440x780: sem erros | passou | [] |
| Viewport | 1536x720 #inicio: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1536x720 #metodologia: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1536x720 #resultados: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1536x720 #resultados/cobertura: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1536x720 #resultados/precisao: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1536x720 #resultados/sintese: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1536x720 #execucoes: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1536x720 #fontes: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1536x720: ação 'Entrar nos resultados' visível sem rolar | passou | {'x': 160, 'y': 597.84375, 'width': 202.90625, 'height': 46} |
| Console | 1536x720: sem erros | passou | [] |
| Viewport | 1920x950 #inicio: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1920x950 #metodologia: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1920x950 #resultados: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1920x950 #resultados/cobertura: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1920x950 #resultados/precisao: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1920x950 #resultados/sintese: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1920x950 #execucoes: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1920x950 #fontes: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 1920x950: ação 'Entrar nos resultados' visível sem rolar | passou | {'x': 352, 'y': 817.484375, 'width': 202.90625, 'height': 46} |
| Console | 1920x950: sem erros | passou | [] |
| Viewport | 390x844 #inicio: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 390x844 #metodologia: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 390x844 #resultados: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 390x844 #resultados/cobertura: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 390x844 #resultados/precisao: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 390x844 #resultados/sintese: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 390x844 #execucoes: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 390x844 #fontes: sem rolagem horizontal | passou | excesso 0px |
| Viewport | 390x844: ação 'Entrar nos resultados' visível sem rolar | passou | {'x': 18, 'y': 594.3125, 'width': 202.90625, 'height': 46} |
| Console | 390x844: sem erros | passou | [] |
| Movimento | prefers-reduced-motion: abertura já no estado final e sem laço de animação | passou | {'t': 8.2, 'fim': 8.2, 'ativo': False} |
| Movimento | botão 'Reduzir movimento' ativa a classe e interrompe a animação | passou | {'t': 8.2, 'fim': 8.2, 'ativo': False} |
| Fallback | sem WebGL: planta SVG exibida na abertura | passou |  |
| Fallback | sem WebGL: lista de estações e texto continuam utilizáveis | passou |  |
| Fallback | sem WebGL: sem exceções | passou | [] |
| Metodologia | estação 2: detalhe e aria-current atualizados | passou |  |
| Metodologia | estação 5: detalhe e aria-current atualizados | passou |  |
| Metodologia | estação 7: detalhe e aria-current atualizados | passou |  |
| Metodologia | seção do filme apresenta o filme V4 (sem mensagem de produção) | passou |  |
| Metodologia | alternativa para avançar sem assistir | passou |  |
| Metodologia | vídeo local, sem autoplay, preload=metadata e pausado | passou |  |
| Reprodução | Próxima desabilitada na estação 7 | passou |  |
| Reprodução | reproduzir na estação 7 recomeça na estação 1 e marca 'Pausar percurso' | passou | 0 |
| Reprodução | pausar interrompe e restaura o rótulo 'Reproduzir percurso' | passou |  |
| Reprodução | Próxima ×2 avança exatamente duas estações e texto/indicador acompanham | passou |  |
| Reprodução | Anterior retorna uma estação | passou |  |
| Redimensionamento | estação 7: canvas acompanha o palco após redimensionar a janela | passou | [857.59375, 522, 857.59375, 522] |
| Console | reprodução/redimensionamento sem erros | passou | [] |
| Metodologia layout | 1366x650: cena, explicação, nav e controles visíveis sem rolar a página nas 7 estações | passou |  |
| Metodologia layout | 1366x650: estação 6: canvas = palco, 3+ rótulos completos dentro do palco | passou | canvas=[0, 60.296875, 915.21875, 642.296875] palco=[0, 60.296875, 915.21875, 642.296875] rotulos=3 |
| Metodologia layout | 1366x650: estação 7: canvas = palco, 1+ rótulos completos dentro do palco | passou | canvas=[0, 60.296875, 915.21875, 642.296875] palco=[0, 60.296875, 915.21875, 642.296875] rotulos=1 |
| Metodologia layout | 1366x650: cena ocupa 64–70% da largura | passou | 0.67 |
| Metodologia layout | 1280x590: cena, explicação, nav e controles visíveis sem rolar a página nas 7 estações | passou |  |
| Metodologia layout | 1280x590: estação 6: canvas = palco, 3+ rótulos completos dentro do palco | passou | canvas=[0, 59.859375, 857.59375, 581.859375] palco=[0, 59.859375, 857.59375, 581.859375] rotulos=3 |
| Metodologia layout | 1280x590: estação 7: canvas = palco, 1+ rótulos completos dentro do palco | passou | canvas=[0, 59.859375, 857.59375, 581.859375] palco=[0, 59.859375, 857.59375, 581.859375] rotulos=1 |
| Metodologia layout | 1280x590: cena ocupa 64–70% da largura | passou | 0.67 |
| Metodologia layout | 1440x780: cena, explicação, nav e controles visíveis sem rolar a página nas 7 estações | passou |  |
| Metodologia layout | 1440x780: estação 6: canvas = palco, 3+ rótulos completos dentro do palco | passou | canvas=[0, 59.984375, 964.796875, 771.984375] palco=[0, 59.984375, 964.796875, 771.984375] rotulos=3 |
| Metodologia layout | 1440x780: estação 7: canvas = palco, 1+ rótulos completos dentro do palco | passou | canvas=[0, 59.984375, 964.796875, 771.984375] palco=[0, 59.984375, 964.796875, 771.984375] rotulos=1 |
| Metodologia layout | 1440x780: cena ocupa 64–70% da largura | passou | 0.67 |
| Metodologia layout | 1536x720: cena, explicação, nav e controles visíveis sem rolar a página nas 7 estações | passou |  |
| Metodologia layout | 1536x720: estação 6: canvas = palco, 3+ rótulos completos dentro do palco | passou | canvas=[0, 59.984375, 1029.109375, 711.984375] palco=[0, 59.984375, 1029.109375, 711.984375] rotulos=3 |
| Metodologia layout | 1536x720: estação 7: canvas = palco, 1+ rótulos completos dentro do palco | passou | canvas=[0, 59.984375, 1029.109375, 711.984375] palco=[0, 59.984375, 1029.109375, 711.984375] rotulos=1 |
| Metodologia layout | 1536x720: cena ocupa 64–70% da largura | passou | 0.67 |
| Metodologia layout | 1920x950: cena, explicação, nav e controles visíveis sem rolar a página nas 7 estações | passou |  |
| Metodologia layout | 1920x950: estação 6: canvas = palco, 3+ rótulos completos dentro do palco | passou | canvas=[0, 59.984375, 1286.390625, 879.984375] palco=[0, 59.984375, 1286.390625, 879.984375] rotulos=3 |
| Metodologia layout | 1920x950: estação 7: canvas = palco, 1+ rótulos completos dentro do palco | passou | canvas=[0, 59.984375, 1286.390625, 879.984375] palco=[0, 59.984375, 1286.390625, 879.984375] rotulos=1 |
| Metodologia layout | 1920x950: cena ocupa 64–70% da largura | passou | 0.67 |
| Metodologia layout | 390x844: cena, explicação, nav e controles visíveis sem rolar a página nas 7 estações | passou |  |
| Metodologia layout | 390x844: estação 6: canvas = palco, 3+ rótulos completos dentro do palco | passou | canvas=[0, 60.484375, 390, 499.359375] palco=[0, 60.484375, 390, 499.359375] rotulos=3 |
| Metodologia layout | 390x844: estação 7: canvas = palco, 1+ rótulos completos dentro do palco | passou | canvas=[0, 60.484375, 390, 499.359375] palco=[0, 60.484375, 390, 499.359375] rotulos=1 |
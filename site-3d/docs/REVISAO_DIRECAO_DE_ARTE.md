# Revisão crítica da direção de arte · 2026-10-14

Esta revisão parte das capturas da versão anterior (`testes/capturas/antes/` e `testes/capturas/antes_estado_real/`).
Não defende a versão anterior: a tecnologia (Three.js) não comprova qualidade visual.

## A. Autocrítica visual (diagnóstico concreto)

| # | Observação na versão anterior | Por que falha |
|---|---|---|
| 1 | Papel bege, grade quadriculada de fundo (`body::before`), filetes finos e detalhes em latão em **todas** as páginas | Linguagem de template “editorial técnico”; a grade compete com os dados e unifica tudo em um mesmo plano morto. |
| 2 | Abertura: uma folha de pé e doze placas minúsculas sobre dois trilhos, em palco 16:10 com borda, ao lado do texto | Diagrama, não ambiente. Escala frágil: objetos ocupam ~15 % do quadro; não há profundidade, hierarquia nem intenção de câmera. A “norma” e os “requisitos” são o mesmo retângulo repetido. |
| 3 | Todas as vistas começam com o mesmo bloco: sobretítulo mono dourado + h1 serifado + lide | Previsível; nenhuma página tem ritmo próprio. |
| 4 | Cenas 3D e página têm a mesma luz e o mesmo bege (cena quase da cor da página) | Sem contraste entre momentos narrativos; a cena “some” na interface. |
| 5 | Metodologia: sete estações são a mesma placa de papel e caixas simples em linha reta | Parece um diagrama; o espectador não percebe mudança de ambiente nem diferença entre IA, rotina determinística, gabarito e pessoa auditora. |
| 6 | Rótulos em caixas mono com borda sobre a cena | Aparência de anotação de ferramenta, não de legenda de exposição. |
| 7 | Resultados: quatro colunas idênticas (nome, valor, fração, matriz) repetidas em três painéis | Blocos iguais para perguntas diferentes; a matriz de unidades é a mesma forma para Recall e Cobertura. Os números não dominam a página. |
| 8 | Três abas com quadradinho colorido e uma aba de síntese à direita | Funcional, mas sem peso; o usuário não percebe que mudou de pergunta. |
| 9 | 40 execuções: mapa sobre o fundo quadriculado; painel e tabelas em caixas | Mapa pequeno em relação à largura; cartões de contexto genéricos. |
| 10 | Cabeçalho: logotipo em quadro com grade + links; botão “Reduzir movimento” com a mesma aparência de um botão de formulário | Marca sem personalidade. |
| 11 | Fontes: tabela corrida + listas | Correta, porém sem hierarquia de leitura. |
| 12 | Texto duplicado detectado: definição do Recall repetindo “Não é medida de acurácia.”; nota da sensibilidade com frase duplicada e “..” | Falha editorial que o redesenho deve corrigir. |

**O que funcionou e é preservado:** roteamento por hash, cinco áreas, abas com teclado, mapa de calor 4×10 integrado (seleção de célula/linha/coluna, tabelas, painel), dados e denominadores, fallback sem WebGL, movimento reduzido, caminhos relativos, suíte `testar_site.py` (126 verificações), integridade dos originais.

## B. Três propostas realmente diferentes

### Proposta 1 — “Observatório” (rejeitada)
- Composição: salão escuro, instrumentos flutuantes, interface escura.
- Luz: emissiva, azul/ciano. Materiais: vidro e metal anodizado. Tipografia: grotesca geométrica.
- Problemas: estética “tecnologia/IA” genérica; brilhos emissivos são justamente o efeito sem propósito que o pedido proíbe; contradiz a interface predominantemente clara.

### Proposta 2 — “Átrio de Calcário” (rejeitada)
- Composição: arquitetura monumental clara, sombras longas, interface em branco-osso.
- Luz: sol rasante frio. Materiais: calcário, concreto, vidro fosco. Tipografia: serifa de display muito grande.
- Problemas: tudo claro sobre claro; falta contraste entre momentos narrativos; risco de cena “lavada” em telas de baixo contraste.

### Proposta 3 — “Da pedra à luz” (escolhida)
- **Ideia narrativa:** a obrigação normativa começa como um monólito de pedra, opaco e pesado, num salão em penumbra; à medida que seus requisitos se destacam, alinham-se e se tornam verificáveis, a luz aumenta. A sequência da metodologia vai da penumbra do salão à luz do dia da interpretação humana.
- **Composição:** abertura em *full-bleed* (cena ocupa a largura inteira; texto sobreposto à esquerda sobre a sombra). Metodologia como câmera de cinema sobre uma plataforma contínua, com legenda sobreposta e trilho de estações. Resultados como “faixas” de cor profunda (uma por pergunta) com números gigantes sobre superfície clara.
- **Luz:** uma luz-chave rasante e quente (janela alta), longa sombra projetada; preenchimento frio fraco; muda por estação (quente → fria da IA → neutra → luz do dia).
- **Materiais:** basalto escuro, calcário claro bisotado, latão escovado (apenas em instrumentos de medida), cerâmica branca (agente de IA), argila (pessoa auditora). Cada papel narrativo tem material próprio.
- **Tipografia:** Fraunces em contraste de escala extremo (display leve de 4–6 rem para números e títulos), Inter para leitura, Plex Mono apenas em rótulos técnicos pequenos.
- **Tratamento espacial:** sem grade de fundo; planos de cor largos; assimetria; espaço negativo deliberado; alternância claro/escuro por página.
- **Por que vence:** transforma o tema (obrigação → verificável) em fenômeno visível (a luz), atribui identidade material a cada ator do método (IA, rotina determinística, gabarito, pessoa auditora) e dá a cada página um ritmo próprio, sem recorrer a neon, partículas ou brilhos.

## Critérios de aceitação desta etapa
Os nove critérios da seção 10 do pedido são verificados ao final (capturas “antes/depois” em `testes/capturas/`). O resultado está em `docs/RELATORIO_REVISAO_VISUAL.md`.

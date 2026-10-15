# Storyboard v3 — filme de ~60 s sobre a contribuição científica (proposta para avaliação)

**Status:** proposta. Nada foi gerado; nenhum crédito Kairogen foi consumido. Aguarda aprovação e autorização explícita.

## Papel do filme
O percurso interativo (sete estações) explica o **mecanismo**. O filme conta a **contribuição**: o problema da auditoria, a norma tornada requisito verificável, a aplicação a quatro instituições, a coleta orientada por IA, a comparação com um gabarito independente e a interpretação humana. Não repete as cenas 3D nem sua ordem de estações.

## Princípios
- Realismo documental; sem personagens abstratos nem infográficos animados.
- Material real quando existir: texto do art. 27 da IN-TCU 84/2020 e dos subitens 12.1 e 12.2 do PNTP; capturas verificadas dos portais. **Esses materiais não estão no projeto**: precisam ser obtidos de fontes oficiais e datados antes da montagem. Sem eles, a cena usa apenas a tipografia dos nomes dos critérios.
- Nada de marcas, interfaces, evidências ou resultados inventados. A IA nunca aparece como quem decide conformidade.
- Textos, nomes de critérios e métricas sempre em tipografia real, na edição (modelos de vídeo não escrevem texto confiável).

## Cenas

| # | Tempo | Cena | Ação visual | Narração | Origem do material |
|---|---|---|---|---|---|
| 1 | 0–7 s | O problema | Documental, câmera na altura da mesa: mãos de uma pessoa auditora folheando relatórios impressos ao lado de um notebook com a página de um portal de transparência. | “Auditar a prestação de contas públicas exige encontrar, nos portais de transparência, a evidência de que cada obrigação foi cumprida.” | Gerar: mesa, mãos e ambiente. Compor na edição: a tela do portal com captura real verificada. |
| 2 | 7–17 s | Da norma ao requisito | Plano detalhe do texto real do art. 27 da IN-TCU 84/2020 (documento oficial); os trechos são destacados e viram dez marcadores numerados, quatro em teal (IN84-27-CAPUT) e seis em índigo (PNTP-12.1-12.2-SIC). | “A pesquisa traduz a norma em requisitos verificáveis: quatro do artigo 27 da IN-TCU 84, o critério IN84-27-CAPUT, e seis dos subitens 12.1 e 12.2 do PNTP, o critério PNTP-12.1-12.2-SIC.” | Compor na edição, com tipografia real e texto verbatim da fonte oficial. Nada de texto gerado por IA. |
| 3 | 17–26 s | Quatro instituições | Quatro capturas reais, datadas, das páginas de transparência de CNJ, STF, TJDFT e TST, uma após a outra, com leve movimento de câmera; contador discreto de execuções ao final. | “Os mesmos critérios foram aplicados a quatro portais: CNJ, STF, TJDFT e TST, em quarenta execuções.” | Compor na edição com capturas reais verificadas. Sem logotipos ou interfaces inventadas. |
| 4 | 26–36 s | Coleta orientada por IA | Tela de navegação percorrendo uma página de portal; documentos coletados entram em pastas nomeadas pelo requisito (estrutura real descrita na dissertação: subpastas por critério). O agente aparece apenas como cursor/trilha, nunca como figura que decide. | “Um modelo de inteligência artificial generativa percorre os portais e reúne evidências por requisito. Ele localiza e organiza. Não decide.” | Captura de tela real do pipeline, se disponível; alternativa: reconstituição fiel feita na edição. |
| 5 | 36–49 s | Gabarito independente | Tela dividida: à esquerda, evidências reportadas; à direita, o gabarito, separado por uma divisória. Uma rotina compara; linhas ligam os pares com correspondência, e um item permanece sem ligação, em tom neutro (não vermelho). Surgem os nomes das três métricas, sem percentuais. | “Um gabarito independente do modelo, revisado por três especialistas do TJDFT, é comparado por uma rotina determinística. Resultam três métricas: Recall_item, Cobertura_evidência e Precisão_evidência.” | Compor na edição com tipografia real; elementos gráficos próprios. Valores só se forem lidos de `dados.js`. |
| 6 | 49–60 s | Interpretação humana | Retorno ao ambiente humano: a pessoa auditora, plausível e sem rosto de pessoa real identificável, examina evidências em tela e anota. Plano final: título oficial do trabalho e autoria. | “Evidência sem correspondência direta não é, por isso, falsa. A interpretação crítica cabe à pessoa auditora: o framework apoia a auditoria, não a substitui.” | Gerar com modelo de vídeo (única cena com figura humana). Créditos finais em tipografia real. |

## Narração completa (134 palavras, ~130 palavras/min)

Auditar a prestação de contas públicas exige encontrar, nos portais de transparência, a evidência de que cada obrigação foi cumprida. A pesquisa traduz a norma em requisitos verificáveis: quatro do artigo 27 da IN-TCU 84, o critério IN84-27-CAPUT, e seis dos subitens 12.1 e 12.2 do PNTP, o critério PNTP-12.1-12.2-SIC. Os mesmos critérios foram aplicados a quatro portais: CNJ, STF, TJDFT e TST, em quarenta execuções. Um modelo de inteligência artificial generativa percorre os portais e reúne evidências por requisito. Ele localiza e organiza. Não decide. Um gabarito independente do modelo, revisado por três especialistas do TJDFT, é comparado por uma rotina determinística. Resultam três métricas: Recall_item, Cobertura_evidência e Precisão_evidência. Evidência sem correspondência direta não é, por isso, falsa. A interpretação crítica cabe à pessoa auditora: o framework apoia a auditoria, não a substitui.

## Critérios e métricas citados
IN84-27-CAPUT (art. 27 da IN-TCU 84/2020; 4 unidades) · PNTP-12.1-12.2-SIC (subitens 12.1 e 12.2 do item 12 do PNTP; 6 unidades) · Recall_item · Cobertura_evidência · Precisão_evidência.

## Estimativa de custo (a reconsultar antes de qualquer geração)
Preços medidos anteriormente: Seedance 2.5, 720p turbo ≈ 9,7 créditos/s. Somente cenas 1 e 6 (e eventual plano de apoio da 4) exigem geração: ≈ 17–25 s de vídeo gerado → ≈ 165–245 créditos, contra ≈ 582 do roteiro anterior de 60 s inteiramente generativo. Narração ≈ 1 crédito. Saldo atual: 882.

## Pendências para aprovar
1. Aprovar a estrutura e a narração.
2. Fornecer ou autorizar a captura de material oficial (norma e portais) com data.
3. Autorizar explicitamente o consumo de créditos e o teto.
4. Antes de gerar: reconsultar saldo/custos e diagnosticar a falha anterior do Seedance (texto→vídeo curto de teste), sem tentativas cegas.
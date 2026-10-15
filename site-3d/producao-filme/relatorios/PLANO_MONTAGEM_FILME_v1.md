# Plano de montagem — "Da obrigação normativa à evidência verificável" (v1)

Status: **planejamento e diagnóstico.** Nenhuma montagem, geração ou consumo de créditos. Nenhum arquivo original foi alterado.

## 1. Inventário real (medido nesta etapa)
Metadados lidos com o Media Foundation do Windows (somente leitura). Todos os vídeos: H.264, 1280×720, 24 fps.

| Id | Caminho relativo | Duração | Bytes | Taxa | Origem | Áudio embutido |
|---|---|---|---|---|---|---|
| `T1` | `piloto/piloto_v01_seedance25_5s_720p.mp4` | 5,042 s | 1.600.880 | 2,54 Mb/s | Original gerado | Nenhum |
| `T2o` | `cenas/T2_v01_seedance25_10s_720p.mp4` | 10,042 s | 2.161.338 | 1,72 Mb/s | Original gerado | Nenhum |
| `T2a` | `cenas/T2_v01_aparado_9708ms_720p.mp4` | 9,728 s | 7.516.964 | 6,00 Mb/s | **Derivado** (recodificado) de `T2o` | **1 faixa** (conteúdo não verificado; provavelmente silêncio) |
| `T3` | `cenas/T3_v02_seedance25_12s_720p.mp4` | 12,042 s | 4.204.203 | 2,79 Mb/s | Original gerado | Nenhum |
| `T4` | `cenas/T4_v02_seedance25_8s_720p.mp4` | 8,042 s | 2.253.778 | 2,24 Mb/s | Original gerado | Nenhum |
| `T5` | `cenas/T5_v01_seedance25_8s_720p.mp4` | 8,042 s | 1.725.005 | 1,71 Mb/s | Original gerado | Nenhum |
| `T6` | `cenas/T6_v01_seedance25_12s_720p.mp4` | 12,042 s | 2.749.420 | 1,82 Mb/s | Original gerado | Nenhum |

Soma bruta: 64,3 s (com `T2o`; 64,0 s com `T2a`).

Outros ativos: `referencias/` (4 JPG, direção de arte; não entram no filme), `roteiro/` (storyboard, prompts), `relatorios/` (relatórios por tomada). **Não existem** arquivos de áudio, trilha, legendas, logotipos nem fontes do filme: `audio/`, `final/` e `keyframes/` estão vazias. O site tem fontes próprias (`site-3d/assets/fonts`: Fraunces, Inter, IBM Plex Mono em `.woff2`), não usadas aqui.

### Limitações da inspeção
- **Não reproduzi nenhum vídeo.** Examinei quadros extraídos (miniaturas): `T1` 6, `T2a` 11, `T6` 13 nesta etapa; `T3`, `T4`, `T5` em etapas anteriores (11 a 16 quadros cada). Movimento contínuo, estabilidade entre quadros e eventuais artefatos intermediários **não verificados**.
- Texto pequeno pode não ser legível nas miniaturas de 480–640 px.
- A aprovação visual de `T1` e `T6` é da autora; não equivale a validação completa do movimento.
- Os áudios das tomadas não existem (vídeos gerados sem áudio).

## 2. T2: original ou aparado?
| Aspecto | `T2o` | `T2a` |
|---|---|---|
| Conteúdo 0–9,70 s | Idêntico | Idêntico (confirmado em 11 quadros, incl. 9,65 s) |
| Fim | Faíscas azuladas a partir de ≈ 9,8 s (confirmado em 9,83–10,04 s) | Cortado em 9,708 s; último quadro limpo |
| Compressão | Fonte gerada, sem geração extra | Recodificado (H.264 a 6 Mb/s), uma geração a mais |
| Faixa de áudio | Nenhuma | 1 faixa embutida |
| Pronto para uso | Precisa de ponto de saída | Sim |

**Recomendação:** usar **`T2o` com ponto de saída em 9,70 s** (sem recompressão extra), preservando `T2a` como alternativa pronta. Se a ferramenta de edição não permitir corte preciso, usar `T2a` e **silenciar a faixa de áudio**. A continuidade da ação é preservada: a mão segue apoiada na página, em gesto contínuo. Confiança: **alta** quanto à ausência de brilhos; **média** quanto ao resto.

## 3. Sequência recomendada (versão principal)
Hipótese de trabalho confirmada, com T5 reduzida e apoiada em gráfico editorial.

| # | Tomada | Entrada | Saída | Duração útil | Ação realmente visível |
|---|---|---|---|---|---|
| 1 | `T1` | 0,00 | 5,00 | 5,00 s | Mãos mais velhas, em mesa de madeira escura, alinham e premem uma pilha de folhas; ao fim, a mão desliza uma folha. Notebook fechado ao fundo |
| 2 | `T2o` (ou `T2a`) | 0,00 | 9,70 | 9,70 s | Mãos escrevem com lápis em uma folha; abas adesivas azul-petróleo e índigo aparecem na folha; caixa de abas e pilha de relatórios desfocadas |
| 3 | `T3` | 0,00 | 9,00 | 9,00 s | Travelling lateral: fichário escuro, relatório creme com lombada verde, fichário azul, envelope kraft; mão vira páginas e desliza uma folha de controle; abas coloridas visíveis |
| 4 | `T4` | 0,00 | 7,90 | 7,90 s | Mão coloca um maço encadernado na caixa cinza e uma folha solta na caixa kraft; mão se retira |
| 5 | `T5` | 0,00 | 2,50 | 2,50 s | Duas pilhas (branca e creme) separadas; mão se aproxima e levanta um bloco da pilha branca. **Não há comparação** |
| 5b | Gráfico editorial | — | — | 7,90 s | Criado na edição, ver seção 5 |
| 6 | `T6` | 0,00 | 12,00 | 12,00 s | Homem de camisa cinza-azulada, em perfil, lê um documento, escreve com caneta, pausa e olha à frente; câmera se aproxima |
| 7 | Cartão final | — | — | ≈ 3,5 s | Título e fecho, na edição |

### Função, narração e legendas por tomada
| # | Função narrativa | Narração (ver `roteiro/NARRACAO_FILME_v1.md`) | Legenda editorial |
|---|---|---|---|
| 1 | O problema | "Auditar a transparência pública é encontrar evidências que possam ser examinadas." | Título "Da obrigação normativa à evidência verificável" |
| 2 | A norma tornada requisito | "A obrigação normativa se traduz em requisitos objetivos e rastreáveis: dez itens, de dois critérios, verificados a cada execução." | "IN84-27-CAPUT · 4 itens" e "PNTP-12.1-12.2-SIC · 6 itens" |
| 3 | Mesmos critérios, quatro instituições | "Os mesmos critérios foram aplicados a quatro instituições: CNJ, STF, TJDFT e TST, dez execuções cada, quarenta ao todo." | "CNJ", "STF", "TJDFT", "TST" em sequência; "10 execuções por instituição · 40 no total"; "Representação conceitual" |
| 4 | IA localiza e organiza | "A inteligência artificial generativa localiza e organiza as evidências por requisito. Ela não decide se a obrigação foi cumprida." | "Modelo: openai/gpt-4.1" |
| 5/5b | Comparação independente | "Um gabarito independente, revisado por três especialistas do TJDFT, é confrontado com as evidências por uma rotina determinística." | "Comparação por rotina determinística"; nomes das três métricas, sem números |
| 6 | Responsabilidade humana | "Evidência sem correspondência direta não é, por isso, falsa. A evidência precisa ser rastreável. A IA localiza. O método compara. A pessoa auditora decide." | Cartão final: "A IA localiza. O método compara. A pessoa auditora decide." |

### Transições
| Passagem | Transição | Motivo |
|---|---|---|
| Entrada em `T1` | Fade de preto, 0,5 s | Abertura |
| `T1` → `T2` | Corte seco | Mesmas mãos e mesma ação de mesa |
| `T2` → `T3` | Corte seco, ou dissolve de 0,3–0,5 s | Mudança de escala (plano fechado para plano médio) |
| `T3` → `T4` | Corte seco, com a narração atravessando o corte | Ação de mesa contínua |
| `T4` → `T5` | Corte seco | Mesma lógica de documentos em mesa |
| `T5` → gráfico | Dissolve de 0,5 s | Passagem do físico para o editorial |
| gráfico → `T6` | Dissolve de 0,5 s | Retorno ao humano |
| `T6` → cartão final | Dissolve de 0,8 s | Fecho |

### Problemas conhecidos por tomada e grau de confiança
| # | Problemas | Confiança |
|---|---|---|
| 1 | Mesa mais escura e quente que as demais; só 5 s; aprovação visual da autora | Média-alta |
| 2 | Brilhos no fim do original (resolvidos pelo ponto de saída); borrões leves; mãos mais velhas, em coerência com `T1` | Alta |
| 3 | **Abas multiplicadas e de várias cores**; conjuntos diferentes do pedido (dois fichários); folha de controle variável; capa com linhas de texto simulado; borrão alaranjado em ≈ 10 s (fora do trecho usado) | Média-baixa |
| 4 | Caixas em vez de pastas; plano mais aberto; maço com argolas; conteúdo das caixas não visível; folhas com linhas de formulário | Média |
| 5 | Ação central falhou; mão levanta um bloco, pilha creme intacta | **Baixa** |
| 6 | Único plano com rosto visível; coerente, câmera avança | Média-alta |

## 4. Linha do tempo (versão principal ≈ 57 s)
Tempos aproximados; a duração final deve seguir a fala real gravada.

| Início | Fim | Dur. | Tomada | Ação visual | Narração | Legenda | Transição de saída |
|---|---|---|---|---|---|---|---|
| 0,0 | 5,0 | 5,0 | `T1` 0–5,0 | Mãos alinham pilha | N1 (0,4–5,2) | Título (0,8–4,2) | Corte |
| 5,0 | 14,7 | 9,7 | `T2o` 0–9,7 | Escrever e abas | N2 (5,7–14,0) | Critérios (8,0–13,5) | Corte/dissolve |
| 14,7 | 23,7 | 9,0 | `T3` 0–9,0 | Travelling sobre conjuntos | N3 (14,5–24,0) | Siglas e contador; "Representação conceitual" | Corte |
| 23,7 | 31,6 | 7,9 | `T4` 0–7,9 | Organiza em caixas | N4 (24,6–32,9) | "Modelo: openai/gpt-4.1" (26,0–30,0) | Corte |
| 31,6 | 34,1 | 2,5 | `T5` 0–2,5 | Duas pilhas separadas | (N4 termina em 32,9) | — | Dissolve |
| 34,1 | 42,0 | 7,9 | Gráfico | Duas fontes e três métricas | N5 (33,5–42,0) | Nomes das métricas; "Comparação por rotina determinística" | Dissolve |
| 42,0 | 54,0 | 12,0 | `T6` 0–12,0 | Lê, escreve, olha | N6 (42,6–53,0) | — | Dissolve |
| 54,0 | 57,5 | 3,5 | Cartão final | Texto | — | Fecho, autoria, rótulo de IA | Fade |

Soma: **57,5 s**, não 60 s. Chegar a 60 s exigiria alongamento artificial (congelar quadros ou repetir tomadas), o que não recomendo.

## 5. Gráfico editorial do Movimento 5 (a produzir na pós)
Não é gerado por IA nem apresentado como captura. Duas colunas discretas de linhas vazias, "Evidências reportadas" e "Gabarito independente", com linhas finas que ligam alguns pares e deixam outros sem ligação, **em tom neutro** (sem vermelho, sem selos, sem "certo/errado"). Em seguida surgem os três nomes: Recall_item, Cobertura_evidência e Precisão_evidência, **sem valores** (decisão D8). Legenda: "Comparação por rotina determinística". Fundo neutro, na paleta creme/madeira das tomadas.

## 6. Versão econômica (≈ 49 s)
`T1` 5,0 + `T2` 9,7 + `T3` 9,0 + `T4` 7,9 + gráfico 5,0 (sem `T5`) + `T6` 10,0 (0–10,0 s) + cartão 2,5 s. Narração de M5 condensada: "Um gabarito independente, revisado por especialistas do TJDFT, é confrontado com as evidências por uma rotina determinística." Indicada se a autora preferir omitir `T5`.

## 7. Uso das tomadas
| Tomada | Uso | Observação |
|---|---|---|
| `T1` | Integral | |
| `T2` | Quase integral (0–9,70 s) | Corte antes dos brilhos |
| `T3` | Parcial (0–9,0 s) | Evita o final borrado; não depender das abas |
| `T4` | Quase integral (0–7,9 s) | Última fração com a mão saindo |
| `T5` | **Mínimo (0–2,5 s) ou omitir** | Recomendo usar 2,5 s como ponte para o gráfico; omitir é alternativa legítima e não deixa lacuna crítica |
| `T6` | Integral | Inspecionar o fim em tamanho cheio antes da exportação |

## 8. Riscos
| Risco | Mitigação |
|---|---|
| Mudança de aparência entre tomadas (mesa escura de `T1`, mesa clara de `T2`–`T5`, escritório de `T6`) | Correção de cor leve; aceitar variação documental |
| Texto simulado em folhas de `T3` e `T4` | Nunca reduzir os cortes para tamanho cheio; legendas e narração sobre a imagem; revisão |
| `T5` sugerir comparação física | Usar só 2,5 s, com legenda e narração; ou omitir |
| `T3` com abas coloridas confunde os critérios | Nada na legenda depende das abas |
| Mãos mais velhas em `T1`/`T2` e mais jovens em `T3`–`T5` | Aceitar; indicam pessoas diferentes |
| Pessoa de `T6` é a única com rosto | Nenhuma ação de mitigação necessária; verificar rosto em tamanho cheio |
| Falas e siglas mal pronunciadas | Revisar a locução antes da mixagem |

## 9. Lacunas que os ativos existentes não resolvem
- Não há imagem de **comparação física bem-sucedida** entre evidência e gabarito.
- Não há imagens de **portais institucionais**, nem capturas verificadas.
- Não há cena de **IA** (e é desejável que não haja).
- 60 s exatos exigiriam material adicional.

## 10. Ferramentas disponíveis (nada foi instalado)
| Ferramenta | Situação | Serve para |
|---|---|---|
| `ffmpeg`/`ffprobe` | **Não instalado** (o `ffmpeg` do Playwright não abre MP4) | — |
| Media Foundation (`MediaComposition`) via PowerShell | Disponível, **verificado** (leitura de metadados, extração de quadros, corte e renderização H.264) | Cortes, concatenação, sobreposições de imagens (PNG), faixa de áudio de fundo |
| Python 3.13 com Pillow e NumPy | Disponível | Renderizar PNGs com tipografia (Segoe UI, Georgia, Bahnschrift existem em `C:\Windows\Fonts`) |
| Clipchamp e Fotos (Windows) | Instalados (não abertos) | Edição manual com texto, transições e áudio |
| Node.js | Disponível | Não necessário |
| Adobe | Apenas Acrobat DC | Não serve |

**Suficiente para uma montagem posterior:** (a) Clipchamp, para edição manual com texto e dissolves; ou (b) script com `MediaComposition` + PNGs de Pillow para cortes secos e legendas, sem dissolves nativos. Exportar legendas em `.srt` à parte. Trabalhar sempre em cópias derivadas em `final/`, preservando os originais.

## 11. Validação
| Item | Estado |
|---|---|
| Nenhuma geração (vídeo, imagem, keyframe, áudio) | Confirmado |
| Nenhum crédito consumido | Confirmado; nenhuma chamada ao Kairogen nesta etapa |
| Originais intactos | Confirmado (tamanhos conferidos acima) |
| Escrita só em `producao-filme\` | Confirmado: criei `relatorios/analise_montagem/` e os três documentos |
| Durações sugeridas compatíveis com os vídeos | Sim: todos os pontos de saída ≤ duração medida |
| Narração em pt-BR | Sim |

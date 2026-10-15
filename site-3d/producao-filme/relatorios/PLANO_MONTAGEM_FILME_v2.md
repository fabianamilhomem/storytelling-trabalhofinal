# Plano de montagem v2 — "Da obrigação normativa à evidência verificável"

Status: **planejamento revisado, executável. Nada foi montado, exportado ou gerado.** `PLANO_MONTAGEM_FILME_v1.md` permanece intacto.

## 1. O que mudou em relação à v1
| # | v1 | v2 | Motivo |
|---|---|---|---|
| 1 | `T5` com 2,5 s e gráfico de 7,9 s | **`T5` omitida**; gráfico editorial de 11,4 s | Decisão da autora; a ação gerada não demonstra comparação |
| 2 | `T3` com 0–9,0 s | **`T3` com 0–12,0 s** | Sincronia: a locução N3 (≈ 10,8 s) não cabia em 9,0 s; os 3 s finais mostram o gesto de repouso do lápis |
| 3 | Fala estimada a 2,3 palavras/s (≈ 52 s) | **2,2 palavras/s e acréscimo por sigla soletrada (≈ 53 s de fala)** | Estimativa mais realista para locução documental |
| 4 | Linha do tempo ≈ 57,5 s, com falas que passavam do trecho | **≈ 61,5 s**, com cada fala ancorada à imagem | Corrigir a sincronia sem acelerar a voz |
| 5 | Siglas aparecendo e sumindo | **Lista cumulativa** "CNJ · STF · TJDFT · TST" | Tempo de leitura |
| 6 | Cartão final de 3,5 s | Cartão após a fala, com **pausa perceptível** de ≈ 3,5 s | Encerramento |
| 7 | Gráfico descrito em linhas gerais | **Especificação** (seção 5) | Executável na edição |

## 2. Fontes de vídeo (inalteradas)
| Id | Arquivo | Duração | Uso na v2 |
|---|---|---|---|
| `T1` | `piloto/piloto_v01_seedance25_5s_720p.mp4` | 5,042 s | 0–5,00 s |
| `T2o` | `cenas/T2_v01_seedance25_10s_720p.mp4` | 10,042 s | **0–9,70 s (principal)** |
| `T2a` | `cenas/T2_v01_aparado_9708ms_720p.mp4` | 9,728 s | Alternativa; **silenciar a faixa de áudio embutida** |
| `T3` | `cenas/T3_v02_seedance25_12s_720p.mp4` | 12,042 s | 0–12,00 s |
| `T4` | `cenas/T4_v02_seedance25_8s_720p.mp4` | 8,042 s | 0–7,90 s |
| `T5` | `cenas/T5_v01_seedance25_8s_720p.mp4` | 8,042 s | **Não usada** |
| `T6` | `cenas/T6_v01_seedance25_12s_720p.mp4` | 12,042 s | 0–12,00 s |

Todos H.264, 1280×720, 24 fps. Nunca sobrescrever nenhum arquivo. Se o editor não cortar `T2o` com precisão em 9,70 s, usar `T2a`, que já está cortado e limpo.

## 3. Linha do tempo completa (≈ 61,5 s)
| # | Início | Fim | Dur. | Tomada | Ação visual | Fala | Legenda | Transição de saída |
|---|---|---|---|---|---|---|---|---|
| 1 | 0,0 | 5,0 | 5,0 | `T1` 0–5,0 | Mãos alinham e premem uma pilha de folhas; fade-in de 0,5 s | N1 0,5–5,5 | Título 1,0–4,5 | Corte seco |
| 2 | 5,0 | 14,7 | 9,7 | `T2o` 0–9,70 | Mãos escrevem a lápis; abas azul-petróleo e índigo | N2 5,9–14,5 | "IN84-27-CAPUT · 4 itens" 8,5–11,5; "PNTP-12.1-12.2-SIC · 6 itens" 11,5–14,2 | Corte seco |
| 3 | 14,7 | 26,7 | 12,0 | `T3` 0–12,0 | Travelling sobre quatro conjuntos; a mão vira páginas, desliza folha, pousa o lápis | N3 14,9–25,7 | Rodapé "Representação conceitual" 15,2–26,4; lista cumulativa CNJ 18,8, STF 19,9, TJDFT 21,0, TST 22,6, permanecendo até 24,0; contador "10 execuções por instituição · 40 no total" 24,0–26,4 | Corte seco; N4 começa antes do corte (J-cut) |
| 4 | 26,7 | 34,6 | 7,9 | `T4` 0–7,9 | Mão coloca o maço na caixa cinza e a folha solta na caixa kraft; retira-se | N4 26,1–34,7 | "Modelo: openai/gpt-4.1" 28,5–32,5 | Dissolve de 0,5 s (34,35–34,85) |
| 5 | 34,6 | 46,0 | 11,4 | Gráfico editorial | Duas colunas; linhas ligam alguns pares; três nomes | N5 35,1–44,2 | "Comparação por rotina determinística" 35,3–46,0; "Esquema ilustrativo" ; métricas 41,6, 43,0, 44,4 | Dissolve de 0,5 s (45,75–46,25) |
| 6 | 46,0 | 58,0 | 12,0 | `T6` 0–12,0 | Lê um documento, escreve, pausa, olha à frente; câmera se aproxima | N6 46,4–58,0 | — | Dissolve de 0,8 s |
| 7 | 58,0 | 61,5 | 3,5 | Cartão final | Texto sobre fundo neutro | — (silêncio) | Fecho; rótulo de IA; autoria | Fade-out de 0,8 s |

**Duração total prevista: 61,5 s.**

### Reserva para pausas e leitura
| Item | Tempo |
|---|---|
| Entrada antes da primeira fala | 0,5 s |
| Pausas entre as falas (5 × 0,4 s) | 2,0 s |
| Pausa interna antes do fecho de N6 | 0,6 s |
| Pausa final no cartão | 3,5 s |
| **Total de respiro** | **6,6 s** |
| Fala efetiva estimada | ≈ 53,0 s |

Leitura: título 3,5 s; critérios 3,0 s cada; lista de siglas ≥ 5,2 s; contador 2,4 s; "Modelo: openai/gpt-4.1" 4,0 s; três métricas visíveis juntas por ≥ 1,6 s antes do dissolve.

## 4. Sincronia imagem-fala
| Fala | Estimada | Trecho visual | Margem | Observação |
|---|---|---|---|---|
| N1 | 5,0 s | `T1` 5,0 s | 0,0 s | Termina 0,5 s depois do corte; aceitável como L-cut |
| N2 | 8,6 s | `T2` 9,7 s | +1,1 s | Cabe |
| N3 | 10,8 s | `T3` 12,0 s | +1,2 s | Cabe |
| N4 | 8,6 s | `T4` 7,9 s | −0,7 s | Transborda 0,7 s para o gráfico; aceitável |
| N5 | 9,1 s | Gráfico 11,4 s | +2,3 s | Cabe, com 1,7 s de entrada |
| N6 | 11,7 s (com pausa) | `T6` 12,0 s | +0,3 s | **Justo**; se a gravação passar de 12,0 s, estender o cartão em vez de acelerar |

A fala de N6 coincide com o gesto de `T6`: o fecho "A IA localiza. O método compara. A pessoa auditora decide." ocupa 53,4–57,9 s, e a pessoa deixa de escrever e olha à frente a partir de ≈ 55 s (9 s de `T6`), de modo que a última frase termina com o olhar. A pausa de 0,6 s antes do fecho cai em 52,8–53,4 s.

## 5. Gráfico editorial (a produzir na edição; sem IA)
- **Formato:** 1280×720, 11,4 s, fundo creme neutro (compatível com as tomadas), texto em grafite. Sem sobreposição de imagens geradas.
- **Colunas:** títulos "Evidências reportadas" (esquerda) e "Gabarito independente" (direita), tipografia sóbria. Cada coluna com barras horizontais discretas e **sem texto** (placeholders): 7 à esquerda e 6 à direita.
- **Conexões:** linhas finas e retas, em grafite, ligando cinco pares; **duas** barras à esquerda e **uma** à direita ficam sem ligação, no mesmo tom neutro. Sem vermelho, verde, "visto", "x", selo ou estrela.
- **Sequência:** (1) colunas surgem, 34,9–36,0; (2) as linhas são traçadas uma a uma, 37,0–41,0, junto da fala "rotina determinística"; (3) três nomes aparecem em sequência, abaixo das colunas, **sem valores**: `Recall_item` (41,6), `Cobertura_evidência` (43,0), `Precisão_evidência` (44,4).
- **Legenda fixa:** "Comparação por rotina determinística". **Aviso discreto:** "Esquema ilustrativo; não representa resultados." A contagem de linhas e barras é arbitrária e não deve corresponder a nenhum resultado real.
- **Não faz:** não simula percentuais, não apresenta a comparação como física ou real e não indica conformidade.
- Opcional (decisão): micro-definições de uma linha sob cada métrica, tiradas de `dados/evidencia_lab.json`, `metricas_definicoes`. Desligado por padrão.

## 6. Identidade editorial
| Elemento | Especificação |
|---|---|
| Tipografia | Título e fecho em **Georgia**; legendas em **Segoe UI**; rótulos técnicos (`IN84-27-CAPUT`, `openai/gpt-4.1`, métricas) em **Consolas**. Todas existem no Windows; as fontes do site (`.woff2`) não são usadas porque não podem ser instaladas sem alterar o ambiente |
| Cores | Texto branco-creme com sombra sutil; terço inferior com gradiente escuro de baixa opacidade; **teal e índigo** apenas para os dois critérios; sem vermelho ou verde |
| Posição | Legendas no terço inferior esquerdo, margem de 6%; altura de cap ≈ 3% do quadro |
| Movimento | Fade de 0,3 s na entrada e na saída; sem animações decorativas |
| Transições | Cortes secos motivados pela ação; dissolves só nas passagens para e do gráfico e para o cartão |
| Cor | Correção moderada para aproximar o tom de `T1` (mesa escura e quente) dos de `T2`–`T4`; sem tentar igualar `T6` |
| Trilha | Nenhuma, até haver autorização e ativo licenciado |
| Cartão final | Georgia grande, branco-creme sobre grafite: **"A IA localiza. O método compara. A pessoa auditora decide."** Abaixo, discreto: "Cenas: representações conceituais geradas com IA generativa (Seedance 2.5)." Autoria e instituição: **[a validar]** |

## 7. Rigor
Preservados: CNJ, STF, TJDFT e TST; 10 execuções por instituição, 40 no total; `openai/gpt-4.1`; dois critérios (4 e 6 itens); a ressalva de que evidência sem correspondência direta não é falsa; a responsabilidade da pessoa auditora. Conferido em `dados/evidencia_lab.json`.

Não incluídos: percentuais, citações normativas, capturas de portais, logotipos, datas. Pendentes de validação da autora: status "preliminar" (P3), autorização para citar especialistas do TJDFT (P4), título oficial, autoria e créditos (P5), rótulo de IA (P6).

## 8. Riscos e mitigação
| Risco | Mitigação |
|---|---|
| `T3` entre 9 e 10,5 s tem borrão de movimento e mancha alaranjada do lápis | Conferir em tamanho cheio; alternativa: encerrar `T3` em 9,0 s e encurtar N3 (versão curta no documento de narração) |
| N6 justa em `T6` | Gravar com a pausa interna mínima; estender o cartão em vez de acelerar |
| Mesa de `T1` mais escura | Correção de cor leve |
| Texto simulado em folhas de `T3`, `T4`, `T6` | Não ampliar; legendas por cima; revisar em tamanho cheio |
| Gráfico lido como resultado | Aviso "Esquema ilustrativo" e ausência de valores |
| Precisão do corte de `T2o` em 9,70 s | Usar `T2a` como alternativa |
| Edição por duas pessoas ou ferramentas | Trabalhar em cópias em `final/` |

## 9. Ferramentas para a montagem posterior
Sem instalação: **Clipchamp** (instalado; dissolves, texto, áudio, filtros) e **Media Foundation** (`MediaComposition`) por PowerShell com PNGs de Pillow (cortes secos e sobreposições, sem dissolves nativos). Não há `ffmpeg`. Nada foi aberto ou executado nesta etapa.

## 10. Confirmações
- Nenhuma montagem, exportação, geração ou instalação. Nenhum crédito consumido. Nenhuma chamada ao Kairogen.
- Nenhum original alterado; nada gravado fora de `producao-filme\`.

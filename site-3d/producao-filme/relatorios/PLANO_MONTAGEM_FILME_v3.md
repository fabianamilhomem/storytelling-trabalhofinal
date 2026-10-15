# Plano de montagem v3 — "Da obrigação normativa à evidência verificável"

Status: **planejamento. Nada foi montado, exportado, gravado ou gerado.** `PLANO_MONTAGEM_FILME_v1.md` e `_v2.md` permanecem intactos.

## 1. Duração
**61,5 s planejados, não definitivos.** A duração final será confirmada após a gravação da narração. Não se acelera a voz nem se congelam imagens para chegar a 60 s. Se a gravação exigir mais ou menos tempo, ajusta-se o cartão final ou as pausas, não a velocidade da fala.

## 2. Mudanças em relação à v2
| # | v2 | v3 |
|---|---|---|
| 1 | N6 começava em `T6` | **N6 começa 0,4 s antes de `T6`, sobre o fim do gráfico** (45,6 s), com o texto revisado |
| 2 | N6: "...não é, por isso, falsa" | "...não é, por isso, **necessariamente** falsa" (fidelidade à fonte) |
| 3 | N6 a 11,7 s com pausa | N6 completa 12,9 s (45,6–58,5 s) e **N6 curta 10,3 s** como alternativa |
| 4 | Aviso "Esquema ilustrativo" discreto | **Aviso permanente e legível** em todo o gráfico |
| 5 | Lista de pendências | **Lista de verificações pré-exportação** (seção 7) |
| 6 | Voz a definir | **Opções e custos das vozes** apresentados (narração v3, seção 6); nenhuma escolhida |

## 3. Fontes de vídeo (inalteradas)
| Id | Arquivo | Duração | Uso |
|---|---|---|---|
| `T1` | `piloto/piloto_v01_seedance25_5s_720p.mp4` | 5,042 s | 0–5,00 s |
| `T2o` | `cenas/T2_v01_seedance25_10s_720p.mp4` | 10,042 s | **0–9,70 s** (principal) |
| `T2a` | `cenas/T2_v01_aparado_9708ms_720p.mp4` | 9,728 s | Alternativa; silenciar a faixa de áudio embutida |
| `T3` | `cenas/T3_v02_seedance25_12s_720p.mp4` | 12,042 s | 0–12,00 s |
| `T4` | `cenas/T4_v02_seedance25_8s_720p.mp4` | 8,042 s | 0–7,90 s |
| `T5` | `cenas/T5_v01_seedance25_8s_720p.mp4` | 8,042 s | **Não usada** |
| `T6` | `cenas/T6_v01_seedance25_12s_720p.mp4` | 12,042 s | 0–12,00 s |

## 4. Linha do tempo (versão completa, ≈ 61,5 s)
| # | Início | Fim | Dur. | Tomada | Ação visual | Fala | Legenda | Transição de saída |
|---|---|---|---|---|---|---|---|---|
| 1 | 0,0 | 5,0 | 5,0 | `T1` 0–5,0 | Mãos alinham e premem uma pilha; fade-in de 0,5 s | N1 0,5–5,5 | Título 1,0–4,5 | Corte seco |
| 2 | 5,0 | 14,7 | 9,7 | `T2o` 0–9,70 | Escrevem a lápis; abas azul-petróleo e índigo | N2 5,9–14,5 | "IN84-27-CAPUT · 4 itens" 8,5–11,5; "PNTP-12.1-12.2-SIC · 6 itens" 11,5–14,2 | Corte seco |
| 3 | 14,7 | 26,7 | 12,0 | `T3` 0–12,0 | Travelling sobre quatro conjuntos; mão vira páginas, desliza a folha, pousa o lápis | N3 14,9–26,1 | "Representação conceitual" 15,2–26,4; lista CNJ 18,8, STF 19,9, TJDFT 21,0, TST 22,6 até 24,0; "10 execuções por instituição · 40 no total" 24,0–26,4 | Corte seco |
| 4 | 26,7 | 34,6 | 7,9 | `T4` 0–7,9 | Maço para a caixa cinza e folha solta para a caixa kraft | N4 26,5–35,1 | "Modelo: openai/gpt-4.1" 28,5–32,5 | Dissolve 0,5 s (34,35–34,85) |
| 5 | 34,6 | 46,0 | 11,4 | Gráfico | Duas colunas; linhas ligam alguns pares; três nomes | N5 35,5–44,8; N6 inicia 45,6 | **"Esquema ilustrativo; não representa resultados."** 34,6–46,0; "Comparação por rotina determinística" 35,3–46,0; métricas 41,6, 43,0, 44,4 | Dissolve 0,5 s (45,75–46,25) |
| 6 | 46,0 | 58,0 | 12,0 | `T6` 0–12,0 | Lê, escreve, pausa, olha à frente; câmera se aproxima | N6 45,6–58,5 | (rodapé opcional "Evidência rastreável" na versão curta) | Dissolve 0,8 s |
| 7 | 58,0 | 61,5 | 3,5 | Cartão final | Texto sobre fundo neutro | Fim de N6 até 58,5; depois silêncio | Fecho; rótulo de IA; autoria [a validar] | Fade-out 0,8 s |

**Total planejado: 61,5 s.** Respiro: entrada 0,5; entre falas 2,4; internas 1,9; silêncio final ≈ 3,0 s.

### Variante com N6 curta
Mesma linha do tempo. N6 curta começa em 46,4 e termina em ≈ 56,7 s; `T6` segue até 58,0 s (≈ 1,3 s de silêncio com a pessoa olhando à frente) e o cartão entra aos 58,0 s. A duração total planejada permanece **61,5 s**.

## 5. Sincronia imagem-fala
| Fala | Estimada | Janela visual | Folga |
|---|---|---|---|
| N1 | 5,0 s | `T1` 5,0 s (0,5–5,5) | Transborda 0,5 s para `T2` (L-cut) |
| N2 | 8,6 s | `T2` 9,7 s | +1,1 s |
| N3 | 10,8 s + 0,4 s | `T3` 12,0 s (14,9–26,1) | +0,6 s |
| N4 | 8,6 s | `T4` 7,9 s (26,5–35,1) | Transborda 0,5 s para o gráfico |
| N5 | 9,1 s + 0,2 s | Gráfico 11,4 s (35,5–44,8) | +1,6 s antes do fim do gráfico |
| N6 completa | 11,6 s + 1,3 s | Fim do gráfico + `T6` 12,0 s + 0,5 s do cartão | A última frase termina 0,5 s após o início do cartão |
| N6 curta | 9,3 s + 1,0 s | `T6` 12,0 s | +1,7 s |

Trechos que podem exigir a locução curta: **N6** (se a gravação ultrapassar ≈ 13,2 s) e **N3** (se ultrapassar ≈ 11,6 s).

## 6. Gráfico editorial (na edição; sem IA)
- **Natureza:** esquema conceitual. **As barras e ligações são ilustrativas, não dados do estudo.** Contagens (7 e 6 barras; 5 ligações; 2 e 1 sem ligação) são arbitrárias.
- **Aviso permanente**, durante todo o gráfico (34,6–46,0 s): "**Esquema ilustrativo; não representa resultados.**" Segoe UI, ≥ 3% da altura do quadro (≈ 22 px a 720p), branco-creme sobre faixa grafite de ≥ 70% de opacidade, canto inferior esquerdo, sem fade de saída antes do dissolve.
- **Colunas:** "Evidências reportadas" e "Gabarito independente"; barras sem texto, tom neutro.
- **Conexões:** linhas finas em grafite; as barras sem ligação mantêm o mesmo tom. **Sem vermelho, verde, "visto", "x", selo ou estrela.**
- **Métricas:** `Recall_item` (41,6 s), `Cobertura_evidência` (43,0 s) e `Precisão_evidência` (44,4 s), em tipografia real, **sem valores** ou percentuais.
- **Legenda:** "Comparação por rotina determinística".
- **Não faz:** não simula resultados, não representa comparação física real e não indica conformidade.

## 7. Verificações antes da exportação — **nenhuma executada**
| # | Verificação | Como | Estado |
|---|---|---|---|
| 1 | Corte de `T2o` em 9,70 s | Conferir o último quadro e ausência de brilhos; alternativa `T2a` | **Pendente** |
| 2 | `T3` em tamanho cheio, em especial 9,0–10,5 s | Revisar borrão do movimento e mancha alaranjada do lápis | **Pendente** |
| 3 | Reprodução contínua de todos os vídeos | Assistir a cada tomada inteira, com atenção a movimento, deformação e artefatos | **Pendente** |
| 4 | Duração real da narração | Gravar e medir N1–N6; escolher N3/N6 completa ou curta | **Pendente** |
| 5 | Legibilidade e permanência das legendas | Ver cada legenda em 720p; permanência mínima de 2 s + 0,06 s por caractere (≈ 3 s para duas linhas) | **Pendente** |
| 6 | Cartão final | Texto do fecho, autoria, rótulo de IA, créditos institucionais | **Pendente** (autoria depende da autora) |
| 7 | Pendências institucionais | "Preliminar" (P3), citação dos especialistas do TJDFT (P4), título e créditos (P5) | **Pendente** |
| 8 | Aviso do gráfico visível durante todo o gráfico | Conferir início, meio e fim | **Pendente** |
| 9 | Faixa de áudio embutida de `T2a`, se usada | Silenciar | **Pendente** |
| 10 | Mixagem | Narração inteligível e sem trilha que a cubra | **Pendente** |
| 11 | Exportação | MP4 H.264, 1280×720, 24 fps, 16:9; áudio AAC 48 kHz; arquivo novo em `final/` | **Pendente** |
| 12 | Sidecar de legendas | `.srt`/`.vtt` em pt-BR, revisado | **Pendente** |

Nenhuma das verificações acima foi declarada concluída.

## 8. Identidade editorial
| Elemento | Especificação |
|---|---|
| Tipografia | Georgia (título e fecho), Segoe UI (legendas), Consolas (rótulos técnicos). Todas existem no Windows |
| Cores | Branco-creme sobre faixa grafite; teal e índigo apenas nos dois critérios; sem vermelho ou verde |
| Posição | Terço inferior esquerdo, margem de 6% |
| Movimento | Fade de 0,3 s; sem animações decorativas |
| Transições | Cortes secos motivados; dissolves só nas passagens para e do gráfico e para o cartão |
| Correção de cor | Moderada, para aproximar `T1` (mesa escura) das demais; sem eliminar diferenças de ambiente |
| Trilha | Nenhuma, até haver autorização e ativo |
| Cartão final | Georgia grande: **"A IA localiza. O método compara. A pessoa auditora decide."**; discreto: "Cenas: representações conceituais geradas com IA generativa (Seedance 2.5)"; autoria [a validar] |

## 9. Ferramentas (nada aberto ou instalado)
Clipchamp (instalado) ou `MediaComposition` por PowerShell com PNGs de Pillow (cortes secos e sobreposições). Não há `ffmpeg`. Voz local do Windows: `Microsoft Maria Desktop` (pt-BR), disponível para teste de tempo, **não utilizada**.

## 10. Confirmações
- Nenhuma montagem, exportação, geração de ativos ou instalação. Nenhum crédito consumido. O Kairogen foi consultado só em leitura (`get_voices_data`, `estimate_audio_cost`).
- Nenhum original alterado; nada gravado fora de `producao-filme\`.

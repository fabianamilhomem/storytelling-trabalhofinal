# Orçamento v1

Consulta somente leitura (`estimate_cost`, `estimate_audio_cost`, `get_me_context`). Nenhum crédito consumido. Valor do crédito: R$ 0,16.

## 1. Saldo
**833 créditos** (plano PRO ativo, expira em 2026-11-14), 0 gerações ativas. Confirmado nesta etapa.

## 2. Cotações reais (seedance-2-5, plano pro, 16:9, 720p, Turbo, sem áudio)
| Duração | Créditos | R$ | Cr/s |
|---|---|---|---|
| 5 s | 49 | 7,84 | 9,80 |
| 7 s | 68 | 10,88 | 9,71 |
| 8 s | 77 | 12,32 | 9,63 |
| 10 s | 97 | 15,52 | 9,70 |
| 12 s | 116 | 18,56 | 9,67 |
| 15 s | 144 | 23,04 | 9,60 |
| 30 s | 288 | 46,08 | 9,60 |
| 10 s a **1080p** | 106 | 16,96 | 10,60 |
| 5 s, Turbo **desligado** (já cotado antes) | 68 | 10,88 | 13,60 |

O áudio nativo do vídeo não alterou o preço com Turbo ligado na cotação anterior; neste orçamento todas as tomadas são sem áudio.

## 3. Áudio (cotado, com ressalvas)
| Item | Créditos | R$ | Observação |
|---|---|---|---|
| Narração TTS (`speech`) | 7 | 1,06 | Cotada com um rascunho de 813 caracteres; **recotar com o texto final** |
| Trilha (`music`, 60 s) | 7 | 1,17 | Cotada com prompt genérico; **recotar** |
| Escolha de voz, direitos de uso da trilha | **sem cotação** | — | Voz não consultada (`get_voices_data`) |
| Imagens de apoio/keyframes | **sem cotação** | — | Fora do orçamento |

## 4. Cenários (apenas valores cotados)
| | A — Mínimo | B — Recomendado | C — Contingência |
|---|---|---|---|
| T1 (piloto reaproveitado) | 0 | 0 | 0 |
| T2 | 8 s: 77 | 10 s: 97 | 10 s: 97 |
| T3 | 10 s: 97 | 12 s: 116 | 12 s: 116 |
| T4 | 8 s: 77 | 10 s: 97 | 10 s: 97 |
| T5 | 8 s: 77 | 10 s: 97 | 10 s: 97 |
| T6 | 10 s: 97 | 12 s: 116 | 12 s: 116 |
| **Vídeo** | **425** | **523** | **523** |
| Narração + trilha | 14 | 14 | 14 |
| Retakes previstos | — | — | T3 e T6 de novo: 232 |
| **Total** | **439** | **537** | **769** |
| Em R$ | 70,24 | 85,92 | 123,04 |
| Saldo restante (de 833) | 394 | 296 | 64 |
| Duração do vídeo gerado | 44 s + piloto 5 s | 54 s + piloto 5 s | idem B |

Cenário A cobre ≈ 55–56 s com título e créditos; B cobre 60 s.

## 5. Reserva recomendada
Para o cenário B, reservar **194 créditos** (dois retakes de tomadas de 10 s, R$ 31,04). Total com reserva: 731, saldo final 102.

## 6. O que é cotado e o que é hipótese
| Tipo | Itens |
|---|---|
| **Cotado** | Todas as tomadas de 5, 7, 8, 10, 12, 15 e 30 s a 720p Turbo; 10 s a 1080p; narração e trilha (com ressalva) |
| **Hipótese** | Quantidade de retakes; custo de 1080p em durações não cotadas; custo de imagens de apoio; custo de áudio por falha |
| **Não cotado** | Durações de 6, 9 e 11 s; keyframes; escolha de voz |

## 7. Observações
- 1080p custa ≈ 9% mais (apenas 10 s cotado). Para 1080p em todas as tomadas, a estimativa linear seria ≈ +50 créditos no cenário B, **hipótese** a confirmar.
- Nenhum valor desta tabela autoriza gasto.

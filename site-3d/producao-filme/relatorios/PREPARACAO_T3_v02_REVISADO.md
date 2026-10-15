# Preparação da geração do T3 v02 REVISADO

Status: **verificações concluídas. Nenhuma geração iniciada, nenhum crédito consumido.** Aguarda autorização explícita e separada.

## 1. Integridade dos documentos
| Arquivo | Bytes | SHA-256 (16 primeiros) | Observação |
|---|---|---|---|
| `roteiro/T3_v02_REVISADO.md` | 6.033 | `5E040BFD7148E89D` | Íntegro |
| `relatorios/PLANO_T3_v02_REVISADO.md` | 7.818 | `C758C321B3E73DF4` | Íntegro |

- Os dois documentos contêm **o mesmo prompt**: 2.084 caracteres, texto idêntico.
- O prompt contém: travelling lateral, esquerda para a direita, sem cortes, sem zoom digital, folha com dez linhas vazias, abas azul-petróleo e índigo, sem brilhos/faíscas/partículas e sem telas legíveis. Não contém "laptop" nem "tick".
- Arquivos preservados e inalterados (tamanhos conferidos): `T2` original (2.161.338), `T2` aparado (7.516.964), `T6` (2.749.420), piloto (1.600.880), `T3_v01.md` (3.197), `T3_v02.md` (5.162).
- O destino `cenas/T3_v02_seedance25_12s_720p.mp4` **não existe**; nada será sobrescrito.

## 2. Coerência com o storyboard
- Posição e duração: Movimento 3, 16–28 s, `T3` de 12 s. **Coerente.**
- Narração do Movimento 3 permanece: "Os mesmos critérios foram aplicados a quatro instituições, CNJ, STF, TJDFT e TST: dez execuções em cada uma, quarenta ao todo." **Coerente.**
- **Divergência registrada:** `STORYBOARD_EXECUTIVO_v1.md` ainda descreve, para o Movimento 3, "pessoa por cima do ombro diante de um notebook". A ação vigente é a de `T3_v02_REVISADO.md`. O storyboard não foi alterado, para preservar a versão; recomendo uma nota de revisão (v1.1) quando você aprovar a ação.

## 3. Parâmetros preparados
`model=seedance-2-5`, `duration_seconds=12`, `aspect_ratio=16:9`, `resolution=720p`, `turbo=true`, `generate_audio=false`, `quantity=1`, `wait_for_completion=false`, sem referências. Uma única tentativa. Áudio integrado **não** habilitado.

## 4. Saldo e cotação atualizados (consultas de hoje, somente leitura)
| Item | Valor atual | Valor histórico | Situação |
|---|---|---|---|
| Saldo | **620 créditos** | 620 | Confirmado, sem alteração |
| Cotação, 12 s, 720p, Turbo, sem áudio | **116 créditos** (R$ 18,56) | 116 | Confirmada |
| Saldo projetado após uma tentativa | **504** | 504 | Confirmado |
| Gerações ativas | 0 | — | — |

Consulta feita com `get_me_context` e `estimate_cost`; nenhum job foi enviado.

## 5. Idioma do áudio final
- **Toda a narração, locução e áudio falado do filme final serão em português brasileiro (pt-BR)**, com dicção clara e pronúncia adequada de siglas (CNJ, STF, TJDFT, TST) e termos técnicos.
- Seguirá o roteiro aprovado, sem tradução livre ou alteração de resultados. Sem inglês e sem português de Portugal.
- Prompts visuais podem permanecer em inglês.
- O `T3` é gerado **sem áudio**; narração entra na edição, depois de aprovados roteiro e custos de áudio.
- Cotação de narração anterior (7 créditos, texto provisório) é valor histórico; recotar com o texto final, e escolher uma voz pt-BR antes de gerar.

## 6. Limitações
- A voz pt-BR do serviço não foi consultada; sua adequação à pronúncia de siglas não está verificada.
- Riscos visuais residuais do `T3` (mãos, abas, papéis, brilhos finais) permanecem conforme `PLANO_T3_v02_REVISADO.md`, seção 4.

## 7. Confirmações
- Nenhuma ferramenta de geração audiovisual foi chamada. Nenhuma geração, imagem, keyframe ou áudio foi criado.
- Nenhum crédito foi consumido.
- Nada foi gravado fora de `producao-filme/`.

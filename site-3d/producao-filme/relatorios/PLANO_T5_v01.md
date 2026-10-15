# Plano T5 v01

Status: **aguardando avaliação e autorização.** Nenhuma geração foi iniciada. Nenhum crédito foi consumido.

## 1. Justificativa visual
A comparação entre evidências e gabarito é a ideia central do Movimento 5. Em vez de listas, abas ou bandejas, a cena usa o gesto mais simples: duas folhas de duas pilhas separadas colocadas lado a lado. Poucos objetos (duas pilhas, duas folhas), uma mão, câmera quase fixa. A cor levemente diferente do papel sugere "duas fontes independentes".

## 2. Divergências documentais (registradas, sem alterar o histórico)
| Fonte | Dizia | Esta preparação |
|---|---|---|
| `STORYBOARD_EXECUTIVO_v1.md`, M5 | Mesa larga; evidências à esquerda e volume encadernado (gabarito) à direita | Duas pilhas de folhas, sem volume encadernado |
| M5 | Pares unidos por clipe; folhas sem par em bandeja neutra | Sem clipe nem bandeja; as folhas sem par ficam nas pilhas |
| M5 | Panorâmica lenta | Câmera quase fixa |
| M5 | Pessoa, "pares" no plural | Um único par comparado, mão sem rosto |
| M5 | Duração 10 s | **8 s** recomendados (ver seção 4) |
| Narração | "...confrontado com as evidências por uma rotina determinística" | Mantida sem alterações |

O objetivo da simplificação é reduzir riscos observados em `T3` e `T4`.

## 3. Lições aplicadas
| Observado | Medida em `T5` |
|---|---|
| `T3`: abas multiplicadas, folha de controle variável, lápis com borrão | Sem abas, lápis ou folha de controle |
| `T4`: "pastas" viraram caixas; "grampeado" virou argolas; plano mais aberto que o pedido; cenário de sala de reunião | Objetos mais simples (pilhas e folhas), prompt curto, "tight close shot" explícito, mesa junto a uma janela |
| `T4`: borrão forte na troca de folha | Um único gesto lento por folha; mão sai do quadro |
| `T3` e `T4`: formulários com texto simulado nas folhas | "Plain printed pages" e proibição de texto; risco permanece |

## 4. Duração e custo
| Opção | Cotação atual | Saldo projetado |
|---|---|---|
| **8 s (recomendada)** | **77 créditos** (R$ 12,32) | **350** |
| 10 s | 97 créditos (R$ 15,52) | 330 |

- **Recomendação:** 8 s. A ação tem dois gestos curtos e uma saída; 10 s só adicionariam tempo parado. Economiza 20 créditos.
- **Teto recomendado para uma tentativa:** **77 créditos**.
- Cotações idênticas às históricas de 8 s e 10 s.

## 5. Saldo e reserva
| Item | Valor |
|---|---|
| Saldo consultado agora | **427 créditos**, 0 gerações ativas |
| Após `T5` de 8 s | 350 |
| Narração TTS e trilha (cotadas antes com texto provisório; recotar) | ≈ 14 |
| Saldo depois do áudio | ≈ 336 |
| Reserva para um retake de 8 s | 77, restando ≈ 259 |

Sobra margem para narração pt-BR, trilha e eventual retake de uma tomada.

## 6. Riscos que permanecem
| Risco | Efeito | Mitigação |
|---|---|---|
| Pilhas ou folhas mudam de cor, número ou forma | Quebra a ideia de duas fontes | Prompt exige consistência; avaliação humana |
| Cor creme não se distinguir do branco | Perde "duas fontes" | Diferença é sutil; aceitar ou tratar na edição |
| Modelo ignorar "tight close shot" e abrir o plano | Como em `T4` | Revisão humana; retake só com autorização |
| Texto pseudo-legível nas folhas | Falsa fidelidade | Prompt proíbe; revisão em 100% |
| Mão com deformação ou borrão | Quebra do realismo | Um gesto lento por vez |
| Brilhos no fim (ocorreram em `T2`) | Artefato | Prompt proíbe; margem para aparar |
| As folhas lado a lado lidas como "comparação manual" | Interpretação equivocada | Narração e legenda atribuem à rotina determinística |
| As folhas sem par serem lidas como "reprovadas" | Interpretação equivocada | Permanecem nas pilhas, sem marcas; narração do `T6` |

Sem garantia de resultado.

## 7. Critérios de aprovação e retake
Critérios: `roteiro/T5_v01_PREPARACAO.md`, seção 10 (12 itens). Reprovação nos itens 1, 5, 6, 7 ou 8 sugere retake, **a ser proposto à autora, que decide**. Sem retake automático.

## 8. Procedimento se autorizado depois
1. Reconsultar saldo e cotação.
2. `generate_video` uma vez, `expected_credits` igual à cotação, dentro do teto; `wait_for_completion=false`.
3. Recuperar pela resposta ou galeria; baixar para `cenas/` sem sobrescrever.
4. Medir duração e resolução, extrair quadros, registrar custo e saldo, parar.

## 9. Decisões que dependem de você
1. Aprovar o conceito simplificado (duas pilhas e duas folhas lado a lado).
2. Aprovar a diferença sutil de papel (branco e creme).
3. Duração: 8 s (77) ou 10 s (97).
4. Teto de créditos (sugestão: 77).
5. Legendas da edição e a decisão D8 sobre números das métricas.

## 10. Declarações
- **Nenhuma geração foi iniciada e nenhum crédito foi consumido.** Foram usados somente `get_me_context` e `estimate_cost`.
- Nada foi gravado fora de `producao-filme/`.
- `T1`, `T2` (original e aparado), `T3`, `T4`, `T6`, o site e os dados permanecem intactos.

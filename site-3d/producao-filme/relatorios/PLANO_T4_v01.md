# Plano T4 v01

Status: **aguardando avaliação e autorização.** Nenhuma geração foi iniciada. Nenhum crédito foi consumido.

## 1. Relação com o storyboard
`STORYBOARD_EXECUTIVO_v1.md`, Movimento 4: "A evidência é organizada", 28–38 s, `T4` de 10 s, plano fechado de bancada com duas pastas, mãos distribuindo folhas, travelling suave, IA apenas pelo efeito. A narração coincide palavra por palavra com a do storyboard.

## 2. O que foi decidido e o que falta
| Item | Estado |
|---|---|
| Posição, duração (10 s), narração | Decidido no storyboard |
| Duas pastas, pós com rótulos e legenda "openai/gpt-4.1" | Decidido no storyboard |
| Ação, câmera e prompt | **Proposta desta etapa**, depende de aprovação |
| Uso de abas ou lista | **Descartado** nesta proposta, por causa de `T3` |
| Rótulos e legendas | Dependem de revisão humana na edição |
| Voz, trilha e custos de áudio | Pendentes (decisões D5 e D6 de `DECISOES_AGUARDANDO_APROVACAO.md`) |

## 3. Divergências registradas (sem alterar documentos históricos)
| Documento | Diz | Esta preparação |
|---|---|---|
| `STORYBOARD_EXECUTIVO_v1.md`, M4 | Mãos distribuem folhas "conferindo cada uma contra uma lista" | Sem lista: evita o problema da folha de controle de `T3` (tamanho variável, texto simulado) |
| `STORYBOARD_EXECUTIVO_v1.md`, M4 | Pastas de "cores distintas" | Pastas cinza e manila, sem tom saturado e sem abas |
| `STORYBOARD_EXECUTIVO_v1.md`, M3 | `T3` com pessoa diante de notebook | Já divergente desde `T3_v02`; não afeta `T4` |

## 4. Lições de `T3` aplicadas
| Problema observado em `T3` | Medida em `T4` |
|---|---|
| Abas de várias cores, multiplicadas | Sem abas, adesivos ou marcadores |
| Primeiro conjunto diferente do pedido; dois fichários | Só duas pastas e dois tipos de documento, de forma simples (grampeado × folha solta) |
| Folha de controle de tamanho variável | Sem folha de controle |
| Capa com linhas de texto tipográfico | Sem capas encadernadas nem relatórios; pacotes grampeados e folhas soltas |
| Borrões de movimento das mãos | Uma só mão se move; a outra repousa; gestos lentos |
| Mancha alaranjada próxima ao lápis | Sem lápis |

## 5. Continuidade com `T1`, `T2`, `T3` e `T6`
Luz lateral de janela à esquerda, madeira clara, paleta neutra e foco raso, como nas tomadas existentes. Mangas azul-claras e ausência de rosto como em `T3`. O plano é mais fechado que `T3`, parecido com `T1` e `T2`. A mesa de `T3` saiu mais brilhante e amarelada; o prompt de `T4` pede paleta neutra, sem garantia.

## 6. Riscos de geração
| Risco | Efeito | Mitigação |
|---|---|---|
| Documentos que mudam de número, forma ou aspecto | Quebra a ideia de organização | Prompt exige consistência; avaliação humana |
| Pacote grampeado e folha solta confundidos entre si | A separação deixa de ser compreensível | Dois tipos muito diferentes de espessura; revisão |
| Mãos e dedos ao pegar e posicionar papéis | Deformação | Uma mão por vez, gestos lentos |
| Texto pseudo-legível nas folhas | Falsa fidelidade | Prompt proíbe; revisão em 100% |
| Brilhos no fim (ocorreram em `T2`) | Artefato nos últimos 0,5 s | Prompt proíbe; margem para aparar |
| Final congelado ou gesto truncado | Fecho artificial | Último gesto descrito (alinhar e retirar a mão) |
| Pastas que mudam de cor ou posição | Quebra de continuidade | Cores muito neutras e descritas |
| Leitura como veredito | Interpretação equivocada | Sem listas, marcas ou símbolos; narração explícita |
| Push-in que vira zoom digital | Perda de paralaxe | Prompt proíbe zoom digital; revisão |

O prompt reduz, mas não elimina, os riscos. Nenhum resultado é garantido.

## 7. Custo e saldo
| Item | Valor atual (consultado agora) | Valor histórico |
|---|---|---|
| Saldo | **504 créditos** | 504 |
| Cotação `seedance-2-5`, 10 s, 16:9, 720p, Turbo, sem áudio | **97 créditos** (R$ 15,52) | 97 |
| Cotação alternativa, 8 s | 77 créditos (R$ 12,32) | 77 |
| Saldo projetado após uma tentativa de 10 s | **407** | — |
| Gerações ativas | 0 | — |

Sem diferença entre cotação atual e histórica. Não escolhi automaticamente outra duração: a de 10 s é a do storyboard, e a de 8 s é só uma alternativa mais barata, que encurtaria a ação.

Projeção, apenas referencial: após `T4` (97), restariam 407. `T5` de 10 s (97) deixaria 310. Uma reserva de um retake de 10 s (97) deixaria 213.

## 8. Critérios de aprovação e retake
- Critérios: `roteiro/T4_v01_PREPARACAO.md`, seção 10 (11 itens).
- Reprovação em 2, 4, 5, 6 ou 7 sugere retake, **a ser proposto à autora, que decide**. Sem retake automático.
- Se aprovada visualmente com ressalvas simples, tratar na edição (aparar, desfoque).

## 9. Procedimento se autorizado depois
1. Reconsultar saldo e cotação.
2. `generate_video` uma vez, com `expected_credits` igual à cotação e dentro do teto fixado pela autora; `wait_for_completion=false`.
3. Recuperar pela resposta ou galeria; baixar para `cenas/` sem sobrescrever.
4. Medir duração e resolução; extrair quadros; registrar custo e saldo; parar.

## 10. Decisões que dependem de você
1. Aprovar a ação (pacotes grampeados e folhas soltas em duas pastas).
2. Aprovar duas pastas (e não três).
3. Duração: 10 s (97) ou 8 s (77).
4. Teto de créditos para uma tentativa (sugestão: 97).
5. Rótulos e legendas da edição.

## 11. Declarações
- **Nenhuma geração foi iniciada e nenhum crédito foi consumido.** Nenhuma ferramenta de geração do Kairogen foi chamada; só `get_me_context` e `estimate_cost` (consulta).
- Nenhum arquivo fora de `producao-filme/` foi criado ou alterado.
- `T1`, `T2` (original e aparado), `T3`, `T6`, o site e os dados permanecem intactos.

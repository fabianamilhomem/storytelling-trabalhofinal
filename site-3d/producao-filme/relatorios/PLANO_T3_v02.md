# Plano T3 v02

Status: **aguardando avaliação humana.** Nenhuma geração, nenhum crédito consumido.

## 1. Por que reformular
A v01 (travelling por quatro ambientes com mesas, caixas e régua) era viável, mas comunicava pouco a atividade de auditoria: sem pessoa, sem consulta, sem organização documental, e com objetos que não indicam "portais da transparência". A v02 troca a metáfora por uma **ação de trabalho observável e repetida**.

## 2. Como a v02 atende aos critérios
| Critério | Resposta |
|---|---|
| Comunica consulta e organização de documentos públicos | Folhear páginas, fixar abas e marcar uma folha de controle sobre documentos impressos; notebook ao lado sugere consulta a páginas públicas |
| Torna perceptível um protocolo comum | A **mesma** folha de controle e os **mesmos** gestos e abas repetem-se nos quatro conjuntos |
| Diferencia os quatro conjuntos sem identidades institucionais | Por materialidade: clipe preto, lombada verde, fichário azul-ardósia, pasta kraft. Sem logotipo, placa ou texto |
| Ação física suficiente para 12 s | Quatro ciclos de ≈ 3 s com gestos diferentes (alinhar, folhear, fixar abas, marcar) |
| Continuidade com `T1`, `T2` e `T6` | Mesma luz lateral, madeira, abas azul-petróleo e índigo de `T2`, lápis, tons de `T6` |
| Evita repetir as sete estações 3D | Cena humana, fotográfica, uma única mesa; nada de ambientes esquemáticos ou etapas numeradas |
| Reduz risco de artefatos | Objetos grandes e distintos; sem tela legível; prompt proíbe brilhos e partículas |
| Entendida sem narração ou texto gerado | Sim: repetição de gesto sobre quatro objetos distintos |

## 3. Siglas e "dez execuções, quarenta no total"
Ver `roteiro/T3_v02.md`, seção 8: legendas em tipografia real, uma por conjunto, e um contador discreto nos últimos 2 s. Nada é gerado no vídeo.

## 4. Cotação (atualizada nesta etapa)
| Item | Valor |
|---|---|
| Saldo consultado | **620 créditos** |
| `seedance-2-5`, 12 s, 16:9, 720p, Turbo, sem áudio | **116 créditos** (R$ 18,56), `estimate_cost` de hoje, sem divergência |
| Saldo projetado após uma tentativa | 504 |
| Duração alternativa (não cotada nesta etapa) | 10 s: 97 e 15 s: 144 (cotações da etapa anterior) |

Não alterei duração nem parâmetros. 12 s mantidos porque a ação tem quatro ciclos de ≈ 3 s.

## 5. Riscos
| Risco | Efeito | Mitigação |
|---|---|---|
| Deformação de mãos e dedos ao folhear e fixar abas | Quebra do realismo | Prompt pede gestos naturais; revisão quadro a quadro; retake só com autorização |
| Abas ou folha de controle que somem ou mudam de forma | Perde a ideia de protocolo | Prompt exige consistência; avaliação humana |
| Conjuntos que se confundem ou trocam de aparência | Perde "quatro conjuntos" | Quatro objetos de materiais muito distintos |
| Texto, números ou símbolos nas folhas e na tela | Falsa fidelidade | Prompt proíbe; revisão a 100% |
| Brilhos nos últimos instantes (como no `T2`) | Artefato no fim | Prompt proíbe; margem de 0,5 s para aparar |
| Leitura de "auditoria manual" em vez de IA | Interpretação equivocada | Narração do `T3` ("mesmos critérios, quatro instituições") e do `T4` ("a IA localiza e organiza"); legenda "protocolo aplicado" na edição |
| Ação ficar rápida ou truncada em 12 s | Gestos incompletos | Ciclos curtos e idênticos; avaliação humana |
| Pessoa de `T3` diferente da de `T6` | Quebra de continuidade | Sem rosto; camisa clara; aceitar variação |

## 6. Critérios de aprovação
1. Quatro ciclos reconhecíveis e semelhantes, um por conjunto.
2. Mesma folha de controle e mesmas abas nos quatro.
3. Quatro conjuntos distinguíveis sem texto.
4. Mãos sem deformação visível; papéis e abas coerentes.
5. Travelling lateral contínuo, sem zoom digital.
6. Nenhum texto, número, logotipo ou emblema legível.
7. Sem brilhos, partículas ou flashes, inclusive nos últimos 0,5 s.
8. Luz e cor compatíveis com `T1`, `T2` e `T6`.
9. Duração e resolução medidas no arquivo.

## 7. Procedimento, se autorizado depois
Reconsultar saldo e cotação; `generate_video` uma vez, `expected_credits=116`, `wait_for_completion=false`; recuperar pela galeria; baixar para `cenas/T3_v02_seedance25_12s_720p.mp4`; registrar custo e saldo; examinar o fim; interromper. Sem retake automático.

## 8. Decisões que preciso de você
1. Aprovar a ação (quatro ciclos sobre quatro conjuntos com a mesma folha de controle).
2. Confirmar que a pessoa deve aparecer sem rosto, de lado e por trás.
3. Aprovar as legendas e o contador da edição.
4. Autorizar, em momento posterior e separado, uma tentativa com teto de 116 créditos.

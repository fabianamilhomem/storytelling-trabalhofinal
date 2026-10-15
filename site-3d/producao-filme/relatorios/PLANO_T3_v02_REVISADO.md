# Plano T3 v02 REVISADO

Status: **aguardando avaliação humana.** Nenhuma geração foi iniciada e nenhum crédito foi consumido. Esta etapa não consultou saldo nem cotação.

## 1. Alterações realizadas em relação à v02
| # | Alteração | Motivo |
|---|---|---|
| 1 | Quatro ações completas em cada conjunto trocadas por **dois ciclos completos e dois sugeridos** | Reduzir aceleração, gestos incompletos e deformação de mãos |
| 2 | Abas aplicadas **uma única vez**, no conjunto 1 | Evitar mudança de cor, duplicação ou desaparecimento |
| 3 | Folha de controle definida como folha branca com dez linhas vazias e nada mais | Eliminar texto, símbolos e carimbos |
| 4 | Marca a lápis definida como **traço curto neutro** (antes, "tick") | Evitar leitura de aprovação |
| 5 | **Notebook removido** do prompt | Evitar tela legível ou brilho de tela; coerente com a ausência de telas |
| 6 | Final definido: pessoa deposita o lápis, câmera mantém a velocidade | Evitar parada brusca, congelamento ou brilho no último instante |
| 7 | Cláusulas explícitas de consistência dos objetos e de velocidade constante | Reduzir riscos de mãos, papéis e abas |
| 8 | Contador "10 · 40" condicionado à validação da sincronização | Evitar sobrecarga e imprecisão |

Conceito, conjuntos, luz, cor, câmera e duração (12 s) foram preservados.

## 2. Prompt integral (inglês)
Idêntico ao de `roteiro/T3_v02_REVISADO.md`, seção 4:

```
Documentary-style medium-close lateral tracking shot at desk height, moving from left to right, of an adult professional working at a long wooden desk in a bright contemporary public-institution office. The person is seen from the side and slightly from behind, wearing a light blue shirt, face not visible. Four distinct sets of printed documents are lined up on the desk from left to right: loose white pages held by a black clip, a cream-colored bound report with a green cloth spine, a slate-blue ring binder, and a tan kraft folder with an elastic band. The person uses one single plain white control sheet, printed only with ten faint empty horizontal lines and nothing else, and uses the same sheet at every set. At the first set the person slides the control sheet beside the loose pages, slowly turns two pages, presses one small teal adhesive tab and then one small indigo adhesive tab onto the edge of a page, and makes one short neutral pencil dash in the margin of the control sheet. At the second set the person slides the same control sheet beside the bound report, slowly turns two pages and makes one short pencil dash. At the third set the sheet slides beside the binder and one page is turned. At the fourth set the sheet rests beside the kraft folder and the person lays the pencil down on it. All gestures are slow, continuous and natural, with realistic finger and hand motion and realistic paper physics. The camera glides smoothly and steadily from left to right at desk height with natural parallax, following the hands, at a constant slow speed until the end, one continuous take with no cuts and no digital zoom. Soft natural daylight from a window on the left, wooden desk, neutral palette, shallow depth of field, photographic film-like color. The two tabs keep their color and size and are never duplicated; objects never appear, disappear or change shape. No readable text, letters, numbers or symbols anywhere, no logos, no emblems, no stamps, no legible screens, no sparkles, no glints, no particles, no light flares, no holograms, no sci-fi elements.
```

Verificação de consistência do prompt: sem instruções contraditórias (um só movimento de câmera, sem cortes, sem zoom, sem telas, uma folha, duas abas aplicadas uma vez).

## 3. Ação e ritmo (12 s)
| Tempo | Conjunto | Ação |
|---|---|---|
| 0–4 s | 1 | Ciclo completo: desliza a folha, vira duas páginas, aplica as duas abas, traço a lápis |
| 4–8 s | 2 | Ciclo completo sem abas: desliza a folha, vira duas páginas, traço a lápis |
| 8–10,5 s | 3 | Sugerido: folha desliza, uma página é virada |
| 10,5–12 s | 4 | Sugerido: folha repousa, lápis é depositado; câmera segue sem parar |

## 4. Riscos que permanecem
| Risco | Observação |
|---|---|
| Mãos e dedos | Folhear e aplicar abas são gestos finos; o modelo pode deformar dedos ou fundir mão e papel. É o ponto crítico |
| Abas | Podem mudar de tom, duplicar ou sumir apesar da instrução; ficam visíveis só no conjunto 1 |
| Papéis | Páginas podem mudar de forma ou número ao serem viradas |
| Quatro conjuntos | Podem trocar de aparência, ou o modelo pode agrupá-los ou inverter a ordem |
| Ordem da ação | O modelo pode antecipar ou repetir gestos fora da sequência pedida |
| Texto residual | Linhas da folha ou páginas podem ganhar marcas parecidas com letras |
| Brilhos finais | Ocorreram no fim do `T2`; o prompt os proíbe, sem garantia. Prever aparar até 0,5 s |
| Sem rosto | Pessoa pode virar o rosto ou aparecer parcialmente |
| Interpretação | Cena de papel pode sugerir auditoria manual; mitigada pela narração e pela legenda de rodapé |
| Continuidade | Pessoa e mãos de `T3` podem diferir de `T6` e `T2` |

O prompt reduz, mas não elimina, esses riscos. Nenhum resultado é garantido.

## 5. Critérios objetivos para avaliar o vídeo quando existir
| # | Critério | Aprova se |
|---|---|---|
| 1 | Câmera | Travelling lateral contínuo, esquerda para direita, sem zoom digital e sem cortes |
| 2 | Quatro conjuntos | Quatro objetos distintos, na ordem esperada, estáveis |
| 3 | Folha de controle | Uma só folha, branca, linhas sem texto, persistente nos quatro conjuntos |
| 4 | Ciclos | Pelo menos dois ciclos completos reconhecíveis (conjuntos 1 e 2) |
| 5 | Abas | Duas, uma de cada cor, sem duplicação, mudança ou sumiço |
| 6 | Mãos | Cinco dedos e movimento plausível, sem fusão com o papel, durante todo o clipe |
| 7 | Papéis | Folhas mantêm forma e número; páginas viradas de modo plausível |
| 8 | Marca a lápis | Traço curto e neutro, sem forma de visto, X ou palavra |
| 9 | Texto e símbolos | Nenhum texto, número, logotipo, emblema ou símbolo legível, em 100% de zoom |
| 10 | Artefatos | Sem brilhos, faíscas, partículas ou flashes, inclusive nos últimos 0,5 s |
| 11 | Final | Termina em gesto natural, sem congelamento |
| 12 | Continuidade | Luz, cor e paleta compatíveis com `T1`, `T2` e `T6` |
| 13 | Medição | Duração (≈ 12 s) e resolução (1280×720) verificadas no arquivo |

Reprovação em 3, 5, 6, 9 ou 10 aciona proposta de retake **somente com autorização**.

## 6. Parâmetros e custo de referência
| Item | Valor |
|---|---|
| Modelo | `seedance-2-5` |
| Duração | 12 s |
| Proporção, resolução | 16:9, 720p |
| Turbo, áudio | Ligado, desligado |
| Quantidade | 1 |
| Custo de referência | **116 créditos** (R$ 18,56), valor histórico |
| Saldo de referência | 620 créditos, valor histórico; saldo projetado 504 |

**Ressalva:** a cotação e o saldo acima vêm de consultas anteriores e **precisam ser atualizados** com `estimate_cost` e `get_me_context` antes de qualquer geração. Este documento não autoriza gasto.

## 7. Edição posterior
Ver `roteiro/T3_v02_REVISADO.md`, seção 6. Nada foi renderizado.

## 8. Confirmações
- **Nenhuma geração foi iniciada e nenhum crédito foi consumido.** Nenhuma ferramenta de geração audiovisual foi chamada.
- Nenhum arquivo fora de `producao-filme\` foi criado ou alterado.
- `T1`, `T2` (original e aparado), `T6`, `T3_v01.md`, `T3_v02.md`, o site e os dados experimentais permanecem intactos.

## 9. Próximos passos
1. Sua avaliação deste prompt e do ritmo.
2. Autorização explícita e separada para gerar, com teto de créditos.
3. Antes da geração: reconsultar saldo e cotação.

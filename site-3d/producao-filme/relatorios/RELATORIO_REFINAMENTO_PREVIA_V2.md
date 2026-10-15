# Relatório — refinamento da prévia V2

Status: **prévia de revisão; não aprovada.** Nenhum crédito consumido, Kairogen não chamado, nada instalado, nada publicado. A V1 (`FILME_PREVIA_V1.mp4`, `FILME_PREVIA_V1_rev2.mp4`) foi preservada.

## 1. Arquivo
`final/FILME_PREVIA_V2.mp4` — 62,763 s, 1280×720, H.264 ≈ 5,9 Mb/s, 1 faixa de áudio, 47.483.396 bytes, taxa reportada 23,856 fps (planejada 24).

## 2. O que mudou em relação à V1
| Item | V1 rev2 | V2 |
|---|---|---|
| Bloco da comparação | Gráfico plano em fundo creme, barras e caixas | **T5** (mãos, duas pilhas de folhas, mesa) como fundo; texto editorial e linhas finas sobre a imagem |
| T5 | Omitida | **Usada 0–8,0 s** como fundo documental (sem repetição, sem congelamento, sem velocidade alterada) |
| Cartão final | 3,5 s, com placeholder de autoria | 8,1 s, **sem placeholder**; linhas surgem com a fala; margens conferidas |
| T6 | Começava em 46,4 s | Começa em 42,6 s (12,0 s inteiros) |

Descoberta da inspeção de T5: ao contrário da avaliação anterior, o início e o meio da T5 mostram uma pilha branca à esquerda, uma creme à direita e uma mão separando folhas ao centro — **utilizável como fundo**, mas **não como demonstração** de correspondência concluída (a mão não compara folhas). O texto trata a imagem como conceitual.

## 3. Linha do tempo (s)
| Início | Fim | Conteúdo |
|---|---|---|
| 0,0 | 5,0 | T1 |
| 5,0 | 14,708 | T2 (original, corte em 9,708 s) |
| 14,708 | 26,708 | T3 |
| 26,708 | 34,625 | T4 |
| 34,625 | 42,625 | **T5 + bloco editorial** (mergulho no preto de 6 quadros na entrada e na saída) |
| 42,625 | 54,625 | T6 |
| 54,625 | 62,75 | Cartão final |

### Bloco editorial (sobre T5)
| s | Elemento |
|---|---|
| 34,9 | Gradiente discreto + **"Esquema ilustrativo; não representa resultados."** (permanece até a saída do bloco) |
| 35,2 | "COMPARAÇÃO POR ROTINA DETERMINÍSTICA" (legenda superior com filete) |
| 35,6 / 36,5 | "Evidências reportadas" (esquerda, traço teal) / "Gabarito independente" (direita, traço índigo) |
| 37,4 | Cinco ligações finas e cruzadas, com pontos teal e índigo (conceituais) |
| 39,4 | Saem os dois títulos |
| 39,6 / 40,4 / 41,2 | `Recall_item`, `Cobertura_evidência`, `Precisão_evidência`, uma após a outra, em Georgia, com filete, sem moldura e sem valor |

### Cartão final
"A IA localiza." (54,6) · "O método compara." (54,9) · "A pessoa auditora decide." (56,3) · depois filete, "Da obrigação normativa à evidência verificável", e os créditos de IA generativa e voz sintética (58,1 → fim). **Autoria/instituição: removidas.** Nenhum nome, logotipo ou crédito inventado.

## 4. Sincronia com a narração (+0,30 s, por análise de energia)
- N4 termina 35,93 s (T4 → início de T5); N5 36,49–45,07; N6 45,90–58,09.
- "Gabarito independente" aparece em 36,5 s (a fala começa em 36,49).
- Pontos de atenção: a frase "é confrontado com as evidências por uma rotina determinística" (41,6–45,1 s) cai em parte sobre **T6**, já sem o bloco; o desenho do bloco termina em 42,6 s. "A IA localiza." é dita a partir de 53,5 s e o texto aparece em 54,6 s (≈ 1,1 s de atraso); as outras duas linhas entram junto das falas.
- O texto **não afirma** que a IA decide: "Comparação por rotina determinística" ocupa o centro do bloco; a IA aparece só em T4 e no fecho.

## 5. Verificações
| Verificação | Resultado |
|---|---|
| Narração | Correlação do envelope com o original **1,000**, atraso 0,30 s, primeiro som 0,39 s, último 58,07 s; pico 0,62; sem aceleração e sem corte |
| T1–T4, T6 | Mesmos trechos da V1; originais conferidos por tamanho (intactos), incluindo T5 e o MP3 |
| Transição T4 → T5 | Quadros 34,4 e 34,7 s: mergulho no preto, sem flash |
| Bloco inteiro | 12 quadros entre 35,2 e 42,7 s: texto legível sobre a imagem; aviso presente em todos |
| T5 → T6 | Quadros 42,4 e 42,7 s: mergulho; T6 entra levemente escurecida |
| Cartão | Quadros em 55,2, 57,0, 59,0 e 62,0 s: nenhum texto cortado; margem inferior ≥ 90 px |
| Texto provisório | Nenhum "[autoria…]" no cartão nem nos elementos da V2 |
| Duração/resolução | 62,763 s; 1280×720 |

## 6. O que não foi verificado
- **Reprodução contínua e audição**: não vi o filme em movimento nem ouvi a narração; os quadros foram extraídos em 640×360.
- Animações de entrada em degraus de opacidade e sua suavidade só se avaliam em movimento.
- Compatibilidade em outros players (23,856 fps reportado).

## 7. Problemas e pontos para sua avaliação
1. As ligações passam **por cima da mão** em 38–42 s; é discreto, mas pode soar sobreposto.
2. A ação da T5 não é uma comparação: o espectador pode ler a mão como "organizando", não "comparando".
3. T6 começa antes do término de N5 (ver seção 4).
4. Cortes secos entre T1–T4; mergulho no preto antes e depois de T5.
5. Texto simulado e abas em T3/T4 (herdado).
6. Rótulo "preliminar" (P3), citação dos especialistas (P4) e autoria (P5) seguem pendentes.
7. Fade de entrada em ≈ 70% de preto (herdado de V1).

## 8. Arquivos criados
- `final/FILME_PREVIA_V2.mp4`
- `relatorios/RELATORIO_REFINAMENTO_PREVIA_V2.md`
- `final/_trabalho/`: `07_elementos_v2.py`, `08_gerar_spec_v2.py`, `spec_previa_v2.txt`, `elementos_v2/` (PNGs), `v2a_audio.wav`, `insp/v2_*.jpg`, `insp/contato_v2.jpg`, `insp/t5_*`, `insp/t4v2_*`, `insp/t6_*`

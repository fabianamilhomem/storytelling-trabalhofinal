# Relatório — montagem da prévia completa V1

Status: **prévia de revisão. Não é versão definitiva e não foi aprovada.** Nenhum crédito foi consumido; o Kairogen não foi chamado.

## 1. Arquivos entregues
| Arquivo | Descrição |
|---|---|
| **`final/FILME_PREVIA_V1_rev2.mp4`** | **Prévia recomendada para revisão** (com mergulho no preto ao redor do gráfico e gradiente de legenda corrigido) |
| `final/FILME_PREVIA_V1.mp4` | Primeira renderização (cortes secos no gráfico). Mantida; **superada** pela rev2 |
| `final/_trabalho/` | Scripts, especificações, elementos gráficos (PNG), áudio decodificado e quadros de verificação |

Caminho exato: `C:\Fabiana\Mestrado IDP\Storytelling de Dados\Trabalhos\Dashboard_PortalTransparencia\site-3d\producao-filme\final\FILME_PREVIA_V1_rev2.mp4`

## 2. Medidas do arquivo (rev2, lido pelo Media Foundation)
| Item | Valor |
|---|---|
| Duração | **61,931 s** (composição planejada 61,917 s) |
| Resolução | 1280×720 (16:9) |
| Vídeo | H.264, ≈ 5,9 Mb/s; taxa de quadros reportada **23,887 fps** (planejada 24) |
| Áudio | 1 faixa; configurada como AAC a 192 kb/s, 48 kHz; **codec não lido diretamente** |
| Tamanho | 46.900.846 bytes |
| Hash SHA-256 (início) | rev2 `F6B3E1B9E45F5B2B`; V1 `2D82B4F66CBD601B` (arquivos diferentes, mesmo tamanho) |

## 3. Fontes usadas
| Item | Arquivo | Trecho |
|---|---|---|
| `T1` | `piloto/piloto_v01_seedance25_5s_720p.mp4` | 0–5,000 s |
| `T2` | `cenas/T2_v01_seedance25_10s_720p.mp4` (original) | 0–9,708 s (corte antes dos brilhos); a versão aparada **não** foi usada |
| `T3` | `cenas/T3_v02_seedance25_12s_720p.mp4` | 0–12,000 s |
| `T4` | `cenas/T4_v02_seedance25_8s_720p.mp4` | 0–7,917 s |
| `T5` | `cenas/T5_v01_seedance25_8s_720p.mp4` | **Omitida**, conforme o plano v3 |
| `T6` | `cenas/T6_v01_seedance25_12s_720p.mp4` | 0–12,000 s |
| Narração | `audio/NARRACAO_COMPLETA_ATHENA_v01.mp3` | Integral, atraso de 0,30 s; **sem aceleração, sem corte** |
| Gráfico e cartão | Criados na edição com Pillow (sem IA) | `final/_trabalho/elementos/` |

Originais e narração conferidos por tamanho após a montagem: **intactos**.

## 4. Linha do tempo realizada
| Início (s) | Fim (s) | Dur. (s) | Conteúdo | Legendas e identificações |
|---|---|---|---|---|
| 0,000 | 5,000 | 5,000 | `T1` | Fade de entrada; título 1,0–4,5 |
| 5,000 | 14,708 | 9,708 | `T2` | "IN84-27-CAPUT · 4 itens" 9,0–11,5; mais "PNTP-12.1-12.2-SIC · 6 itens" 11,5–14,7 (teal e índigo) |
| 14,708 | 26,708 | 12,000 | `T3` | "Representação conceitual" 15,2–26,7; siglas CNJ 18,9, STF 20,3, TJDFT 21,7, TST 23,1 (lista cumulativa); "10 execuções por instituição · 40 no total" 24,4–27,4 |
| 26,708 | 34,625 | 7,917 | `T4` | "Modelo: openai/gpt-4.1" 28,5–32,5 |
| 34,625 | 46,417 | 11,792 | Gráfico editorial | **"Esquema ilustrativo; não representa resultados."** em todo o gráfico; "Comparação por rotina determinística"; colunas "Evidências reportadas" e "Gabarito independente"; ligações 40,0–42,0; `Recall_item` 42,0, `Cobertura_evidência` 43,4, `Precisão_evidência` 44,9 |
| 46,417 | 58,417 | 12,000 | `T6` | — |
| 58,417 | 61,917 | 3,500 | Cartão final | "A IA localiza. O método compara. A pessoa auditora decide."; título; rótulo de IA; narração sintética; **"[autoria e instituição: a validar]"** (placeholder) |

### Narração sobre a linha do tempo (medida por análise de energia do áudio, +0,30 s)
| Fala | Início–fim (s) | Janela visual |
|---|---|---|
| N1 | 0,37–4,90 | `T1` 0–5,0 |
| N2 | 5,49–14,46 | `T2` 5,0–14,7 |
| N3 | 15,15–26,93 | `T3` 14,7–26,7 (a última palavra "todo" invade 0,2 s de `T4`) |
| N4 | 27,57–35,93 | `T4` 26,7–34,6 e começo do gráfico |
| N5 | 36,49–45,07 | Gráfico 34,6–46,4 |
| N6 | 45,90–58,09 | Fim do gráfico, `T6` 46,4–58,4; termina 0,3 s antes do cartão |
| Silêncio final | 58,09–61,9 | Cartão |

Pausas medidas na própria narração entre as seis partes: 0,5 a 0,8 s; antes do fecho "A IA localiza.": ≈ 0,5 s. Foram preservadas, pois o áudio não foi editado.

## 5. Método e ferramentas
- **Nada foi instalado.** Ferramentas já presentes: Media Foundation do Windows (`MediaComposition`), PowerShell, compilador C# do .NET Framework (`csc.exe`), Python com Pillow e NumPy.
- A composição foi montada por `final/_trabalho/Montagem.cs` (compilado para `Montagem.dll` na mesma pasta), a partir de especificações em texto (`spec_previa_v1_rev2.txt`), com tempos em quadros.
- **Transições:** a ferramenta não oferece dissolves nativos. Foram usados **cortes secos** e **mergulho no preto** (camada preta com opacidade escalonada por quadro) em torno do gráfico e no início e no fim. Não há dissolves cruzados.
- Legendas e gráfico: PNG de 1280×720 com tipografia Georgia, Segoe UI e Consolas, sobrepostos à trilha; gradiente escuro suave no terço inferior; gráfico em quadros sucessivos (aparecimento das colunas, das ligações e das métricas).
- **Atraso da narração:** 0,30 s, para que a fala não comece sobre o preto.

## 6. Verificações
| # | Verificação | Resultado |
|---|---|---|
| 1 | Arquivo existe e abre | Sim; lido pelo Media Foundation (metadados, quadros e áudio) |
| 2 | Duração, resolução, quadros, fluxos | Medidos (seção 2) |
| 3 | Narração começa, termina e permanece audível | Sim: primeiro som 0,39 s, último 58,07 s; nível de fala estável (RMS ≈ 0,05; pico 0,62); silêncio de 58,1 a 61,9 s |
| 4 | Última frase completa | Sim: o último som da prévia (58,07 s) coincide com o do áudio original + 0,30 s |
| 5 | Cortes não eliminam palavras nem deixam intervalos acidentais | Correlação do envelope da narração na prévia com o original: **1,000** com atraso de 0,30 s; sem trechos cortados |
| 6 | Quadros no início, nas transições, no gráfico e no cartão | **1.486 quadros extraídos e analisados** (brilho e diferença entre quadros) |
| 7 | Reprodução integral | **Não realizada** (o ambiente não reproduz vídeo nem áudio) |
| 8 | Legibilidade das legendas e do aviso | Conferida em quadros de 640×360; tamanho mínimo ≈ 3% da altura; aviso do gráfico presente em todos os quadros do gráfico |
| 9 | Originais e relatórios preservados | Sim |

### Resultado da varredura de todos os quadros
- **Nenhum flash isolado** (nenhum quadro destoa de ambos os vizinhos).
- Quadros pretos (< 10 de brilho): apenas nos mergulhos (quadros 830–831 e 1114–1116) e no fade final.
- Saltos de imagem apenas nos cortes planejados: `T1`→`T2`, `T2`→`T3`, `T3`→`T4` e `T6`→cartão.
- Os cortes ocorrem de 0 a 3 quadros (≤ 0,125 s) depois do planejado; a duração total difere em 0,014 s.

## 7. Problemas encontrados
| # | Problema | Gravidade | Observação |
|---|---|---|---|
| 1 | Taxa de quadros reportada em 23,887 fps (e não 24) | Baixa | Arredondamento do renderizador; pode ser lido como quadros variáveis em alguns players |
| 2 | Fade de entrada começa em ≈ 70% de preto, não em preto total | Baixa | Comportamento observado da camada preta |
| 3 | Entrada de `T6` tem 3 quadros pretos (0,125 s) | Baixa | Parte do mergulho |
| 4 | Contraste de brilho entre cenas e o fundo creme do gráfico | Média | Atenuado pelo mergulho; mantém salto de claridade |
| 5 | Cortes secos entre `T1`, `T2`, `T3` e `T4` e de `T6` para o cartão | Média | Sem dissolves por limitação da ferramenta |
| 6 | Conteúdo de `T3` e `T4` com texto simulado em folhas e capas, abas coloridas, caixas em vez de pastas | Média | Herdado das tomadas; reportado antes |
| 7 | Cartão final com 3,5 s e três linhas pequenas de crédito | Média | Tempo de leitura curto; o texto do fecho é grande, mas os créditos são lidos em ≈ 3,5 s |
| 8 | Legendas sincronizadas com a análise de energia do áudio, não com a audição | Média | Siglas podem estar levemente adiantadas ou atrasadas |
| 9 | O fade de entrada e a narração partem de 0,37 s | Baixa | Narração inicia logo depois do primeiro quadro |
| 10 | Autoria e instituição são placeholder | Alta (para a versão final) | Depende da autora |
| 11 | Barra de ligações do gráfico (5 de 7 e 6) é arbitrária | Baixa | Coberta pelo aviso permanente |

## 8. Limitações não verificadas
- **Reprodução contínua**: não vi o vídeo em movimento nem ouvi a narração; nada aqui avalia pronúncia, entonação ou naturalidade.
- Sincronização fina entre legendas e palavras ditas só pode ser julgada ouvindo.
- Compatibilidade em outros players (a taxa de quadros 23,887 fps).
- Codec de áudio efetivo.
- Condições de uso da voz e de publicação.
- Pendências científicas e institucionais: status "preliminar" (P3), citação dos especialistas do TJDFT (P4), título, autoria e créditos (P5).

## 9. O que não foi feito
Sem trilha musical, sem novas cenas, sem nova narração, sem retakes, sem publicação, sem versão definitiva, sem instalação de programas.

## 10. Próximos passos sugeridos (aguardam sua decisão)
1. Assistir à `FILME_PREVIA_V1_rev2.mp4` do início ao fim e anotar: sincronia, legibilidade, pronúncia das siglas, ritmo.
2. Decidir sobre cartão final (tempo e créditos), autoria e rótulo "preliminar".
3. Se aprovar a sequência, avaliar trilha e dissolves (Clipchamp) e a exportação final.

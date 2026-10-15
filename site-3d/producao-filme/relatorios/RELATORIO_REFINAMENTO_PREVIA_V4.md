# Relatório — refinamento da prévia V4 (legibilidade tipográfica da T5)

Status: **prévia de revisão; não aprovada, não publicada.** Sem geração, sem Kairogen, sem créditos, sem instalação. `FILME_PREVIA_V1.mp4`, `V1_rev2`, `V2` e `V3` permanecem intactas.

## Arquivo
`final/FILME_PREVIA_V4.mp4` — 60,309 s, 1280×720, H.264 ≈ 9,8 Mb/s (V3: 5,9), 1 faixa de áudio, 75.195.237 bytes, taxa reportada 23,85 fps (igual à V3).

## Diagnóstico (V3)
Em 1280×720 a V3 mostrava letras finas em itálico, com sombra deslocada duplicando os contornos, sobre fundo claro e desfocado, comprimidas a 5,9 Mb/s. Isso produzia bordas "tremidas" e baixa leitura.

## Alterações (somente a camada de texto e a exportação)
| Item | V3 | V4 |
|---|---|---|
| Renderização do texto | 1×, com sombra deslocada | **3× e redução LANCZOS** (antialiasing), **sem sombra, sem halo, sem contorno** |
| Cor | creme com sombra | creme sólido (245,241,232) |
| Rótulos | Georgia itálico 36 | **Georgia Bold 34** (mais robusto, mesma identidade serifada) |
| Métricas | Georgia regular 36 | **Georgia Bold 34**; filetes de 2 px |
| Título/aviso | Segoe UI Semibold 28 / 27 | Segoe UI Semibold 28 / 27, sem sombra |
| Contraste | gradiente topo 170 / base 185 | gradiente topo 150 (decaimento mais longo) / base 175: mais suave e sem cobrir a mão |
| Ligações | 1 px, α 150 | 1,5 px, α 215; mesmos pontos teal/índigo e mesma posição |
| Bitrate | 6 Mb/s | **10 Mb/s** (nova opção `BR` na especificação) |
| Posições, tempos, cartão, duração | — | **idênticos à V3** |

### Causa técnica e correção de um erro intermediário
A primeira renderização da V4 (arquivo descartado, guardado em `final/_trabalho/FILME_PREVIA_V4_tentativa1_halos_descartada.mp4`) apresentou **halos brancos** nos textos e nas linhas: o compositor do Media Foundation trata o PNG como **alfa pré-multiplicado**, e bordas suavizadas em alfa reto ficam claras demais. Os PNGs de texto passaram a ser gravados **com cor pré-multiplicada**; um teste de 3 s confirmou bordas limpas antes da renderização final. Os PNGs usados estão em `final/_trabalho/elementos_v4b/`.

## Verificações
| # | Verificação | Resultado |
|---|---|---|
| 1 | Quadros do início, meio e fim do bloco em 1280×720 | 35,3 / 36,0 / 38,0 / 40,5 / 42,3 s extraídos em tamanho original |
| 2 | Acentos, contornos, espaçamento | Texto nítido, acentos íntegros ("COMPARAÇÃO", "DETERMINÍSTICA", "Evidências", "evidência", "Precisão") |
| 3 | Linhas × rótulos | As ligações ficam abaixo dos rótulos (y ≥ 240) e não os tocam |
| 4 | Aviso durante todo o bloco | Presente em 36,0, 38,0, 40,5 e 42,3 s |
| 5 | V3 × V4 | Comparação em quadros nos mesmos instantes (ver abaixo) |
| 6 | Áudio | Amostras do áudio decodificado **idênticas** às da V3 (diferença máxima 0,0), mesma duração 60,309 s; narração e sincronia como na V3 |
| 7 | Cartão | Quadro 58,2 s: sem texto cortado |
| 8 | Reprodução do trecho | **Não realizada** (o ambiente não reproduz vídeo nem áudio) |

Capturas em `final/_trabalho/insp/`:
- `comparacao_V3xV4_final_03600.jpg`, `_03800.jpg`, `_04050.jpg`, `_04230.jpg` (V3 acima, V4 abaixo, 1280×720 cada);
- `comparacao_V3xV4_topo_*.jpg` e `comparacao_V3xV4_quadro_3800.jpg` são da tentativa descartada (com halos), mantidas para registro;
- `fv4_*.jpg` (V4 final), `cmpV3_*.jpg` (V3).

## Limitações
- **Não assisti nem ouvi o arquivo.** Estabilidade durante o movimento da mão só foi verificada por quadros; o "tremor" por compressão em movimento depende de reprodução.
- Todo o filme foi **re-renderizado** (a ferramenta não permite copiar fluxos sem recompressão); por isso o bitrate foi elevado para 10 Mb/s. Não é uma cópia bit a bit das cenas V3.
- Fade-in/out por degraus de opacidade e cortes secos permanecem.
- Taxa de quadros reportada: 23,85 fps.
- O rótulo esquerdo fica sobre a manga/mão nos primeiros segundos de T5; o contraste é suficiente, mas pode ser avaliado em movimento.
- Pendências científicas e institucionais (P3, P4, P5) inalteradas.

## Arquivos criados/modificados (todos em `producao-filme/`)
- `final/FILME_PREVIA_V4.mp4`, `relatorios/RELATORIO_REFINAMENTO_PREVIA_V4.md`
- `final/_trabalho/`: `11_elementos_v4.py`, `12_gerar_spec_v4.py`, `spec_previa_v4.txt`, `spec_previa_v4_final.txt`, `spec_teste_v4b.txt`, `elementos_v4/` (alfa reto, usada na tentativa descartada), `elementos_v4b/`, `inspecionar_hd.ps1`, `teste_v4b.mp4`, `v4f_audio.wav`, `FILME_PREVIA_V4_tentativa1_halos_descartada.mp4`, capturas
- `final/_trabalho/Montagem.cs` / `Montagem.dll`: acrescentada a linha opcional `BR|bitrate` (padrão 6 Mb/s, inalterado para as especificações antigas)

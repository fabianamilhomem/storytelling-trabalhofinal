# Relatório — refinamento da prévia V3

Status: **prévia de revisão; não aprovada.** Sem geração, sem Kairogen, sem créditos, sem instalação, sem publicação. `FILME_PREVIA_V1.mp4`, `FILME_PREVIA_V1_rev2.mp4` e `FILME_PREVIA_V2.mp4` permanecem intactos.

## Arquivo
`final/FILME_PREVIA_V3.mp4` — **60,309 s**, 1280×720, H.264 ≈ 5,9 Mb/s, 1 faixa de áudio, 45.580.496 bytes (taxa reportada 23,85 fps).
Origem: mesmas tomadas e narração da V2; composição reexportada com texto e encerramento novos.

## 1. Bloco gráfico (34,6–42,6 s, sobre T5)
Área segura: margem de 102 px (8%) nos lados; nada essencial abaixo de y = 648 (últimos 10%).
| Elemento | Posição | Tamanho |
|---|---|---|
| "COMPARAÇÃO POR ROTINA DETERMINÍSTICA" | topo, esquerda (y 58) | 28 px (era 24) |
| "Esquema ilustrativo; não representa resultados." | logo abaixo da legenda (y 106), **permanece em todo o bloco** | 27 px (era 22, a 664 px da borda) |
| "Evidências reportadas" / "Gabarito independente" | topo, esquerda / direita (y 168) | 36 px itálico |
| Ligações finas (conceituais) | entre os dois lados (y 240–380) | 1 px |
| `Recall_item`, `Cobertura_evidência`, `Precisão_evidência` | linha inferior central, y 598–640 (acaba antes de 648) | 36 px (era 30) |
Gradiente discreto no topo e na base para contraste. Os três nomes grafados exatamente; nenhum valor, percentual ou resultado.
Observação: as pilhas ocupam a faixa até y ≈ 600; as métricas ficam sobre a base das pilhas e a sombra da mesa (com gradiente), não sobre mãos.

## 2. Encerramento
- **Última palavra medida** (envelope da narração + 0,30 s de atraso): fim da fala em **57,92 s** (limiar −40 dB); último som perceptível em **58,07 s** (−45 dB) e 58,08 s (−50 dB). Silêncio digital real (RMS 0,0) após 59 s.
- A fala foi mantida integral: correlação do envelope com o original **1,000** com atraso de 0,30 s; sem aceleração, corte ou regravação.
- Cartão: "A IA localiza." (54,6 s), "O método compara." (54,9 s), "A pessoa auditora decide." (56,3 s); título e créditos (26 px) a partir de 57,5 s.
- **Cartão após a fala: 60,29 − 58,07 ≈ 2,2 s** (≈ 2,4 s após 57,92 s; dentro de 1,5–2,5 s). A V2 tinha ≈ 4,7 s.
- Fade-out discreto de 0,75 s (59,5–60,3 s), sem tocar a fala; sem quadros congelados, sem música.
- Placeholder de autoria: ausente. Nenhuma autoria, instituição ou logotipo inventados.

## 3. Verificações (quadros 640×360)
| Item | Resultado |
|---|---|
| Início, meio e fim do bloco (35,2 / 38,0 / 41,0 / 42,3 s) | Textos dentro da área segura; aviso legível; métricas na ordem correta |
| Pré-visualização composta em 1280×720 (T5 em 3,0 s + elementos) | Conferida antes da exportação; margem inferior ≈ 80 px |
| Última palavra (57,2 / 58,1 s) | Última linha e créditos visíveis |
| Primeiro quadro do cartão (54,8 s) | "A IA localiza." |
| Último segundo (59,6 / 60,0 / 60,25 s) | Cartão em fade até preto; nada cortado |
| Áudio | Duração 60,31 s; sem energia depois de 59 s |

## 4. Não verificado
- **Não assisti nem ouvi o arquivo**: o ambiente não reproduz vídeo nem áudio. A sincronia auditiva do encerramento, a pronúncia e a suavidade das animações **não** foram avaliadas.
- Compatibilidade em outros players (23,85 fps reportado).
- Legibilidade em tela de apresentação foi inferida pelos tamanhos relativos, não observada em projeção.

## 5. Pontos para sua avaliação
1. As ligações ainda passam por trás da mão em alguns instantes.
2. "A IA localiza." é exibido cerca de 1,1 s depois de dita (fim de T6, 53,5 s).
3. Autoria, "preliminar" (P3) e citação dos especialistas (P4) seguem pendentes.
4. Créditos técnicos têm 2,8 s de leitura (57,5–60,3 s).

## 6. Arquivos criados
`final/FILME_PREVIA_V3.mp4`; `relatorios/RELATORIO_REFINAMENTO_PREVIA_V3.md`; em `final/_trabalho/`: `09_elementos_v3.py`, `10_gerar_spec_v3.py`, `spec_previa_v3.txt`, `elementos_v3/`, `v3_audio.wav`, `insp/v3_*.jpg`, `insp/contato_v3.jpg`, `insp/pre_v3_bloco.jpg`.

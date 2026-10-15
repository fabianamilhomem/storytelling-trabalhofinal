# Corte do T2 v01 — remoção dos brilhos azulados finais

Nenhum crédito foi consumido e nenhuma geração foi iniciada nesta etapa.

## Arquivos
| Item | Caminho |
|---|---|
| Original (intacto) | `cenas/T2_v01_seedance25_10s_720p.mp4` — 2.161.338 bytes, 10,042 s, 1280×720, 24 fps |
| Versão aparada | `cenas/T2_v01_aparado_9708ms_720p.mp4` — 7.516.964 bytes, ≈ 9,73 s, 1280×720, 24 fps |
| Quadros e folhas de contato | `relatorios/analise_T2/` |

O tamanho do original foi conferido depois do corte e permanece igual.

## Onde surgem os brilhos
Quadros extraídos do original (24 fps), conferidos visualmente:

| Tempo (s) | Estado |
|---|---|
| 7,00 a 9,625 | Limpo. O azul visível é o dispensador de abas, objeto real da cena |
| 9,708 | Limpo |
| 9,750 | Limpo |
| 9,792 | Limpo ou com pontos mínimos na mão, duvidoso |
| 9,833 | Faíscas fracas começam a aparecer sobre a mão |
| 9,917 | Faíscas em forma de estrela nítidas sobre a mão e a mesa |
| 9,958 a 10,040 | Faíscas fortes e distribuídas (mão, papéis, mesa) |

O efeito surge entre **9,79 e 9,83 s** e cresce até o fim. Concorda com sua estimativa de 9–10 s.

## Ponto de corte
- **Corte em 9,708 s** (quadro 233 de 24 fps). Corta 0,334 s do fim.
- Margem de segurança de cerca de 0,1 s antes do aparecimento do efeito.
- A ação não é interrompida de forma abrupta: a mão segue apoiada na segunda aba já fixada; o plano termina em ação contínua, o que é adequado para entrar em corte ou dissolve no `T3`.

## Duração final
**≈ 9,73 s** (9,708 s pedidos; o renderizador do Windows arredonda para quadros, e o último quadro corresponde a ≈ 9,73 s do original, também limpo em amostra). Duração anterior: 10,042 s.

## Verificação da versão aparada
Amostras em 9,50 s e no último quadro amostrado (≈ 9,68 s): sem brilhos; mesma imagem do original, sem diferença visual perceptível.

## Como foi feito
- Ferramenta: Media Foundation do Windows (`MediaComposition`), nativa. Nada foi instalado ou alterado no sistema.
- O arquivo aparado foi **recodificado** (H.264, 720p, 24 fps, 6 Mb/s). Há uma geração a mais de compressão, sem perda perceptível nas amostras. O original permanece como fonte para a montagem final.
- Sem trilha de áudio, como o original.
- O `ffmpeg` do Playwright, encontrado em `%LOCALAPPDATA%\ms-playwright`, não abre MP4 e não foi usado.

## Recomendação para a montagem
1. Usar `T2_v01_aparado_9708ms_720p.mp4` no Movimento 2.
2. Entrar no `T3` com dissolve de 0,25 a 0,5 s sobre os últimos quadros.
3. Se o editor final permitir, refazer o corte a partir do original com o mesmo ponto (9,708 s) para evitar a recodificação.

## Estado
Produção interrompida. `T3` não foi iniciada. Antes de qualquer geração: reconsultar saldo e cotação. Saldo atual conhecido: 620 créditos.

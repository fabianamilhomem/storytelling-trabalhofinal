# T3 v02 REVISADO — o mesmo protocolo, quatro conjuntos documentais

Status: **proposta refinada, não gerada.** Esta versão não sobrescreve `T3_v01.md` nem `T3_v02.md`, que permanecem intactos.

## 1. Conceito (preservado)
Uma pessoa adulta, de lado e levemente por trás, sem rosto visível, trabalha em uma mesa de madeira com quatro conjuntos documentais da esquerda para a direita, distinguíveis pela materialidade:
1. folhas soltas com clipe preto;
2. relatório encadernado com lombada de tecido verde;
3. fichário azul-ardósia;
4. pasta kraft com elástico.

Usa **a mesma folha de controle** e **as mesmas duas abas** (azul-petróleo e índigo). Câmera em travelling lateral contínuo, esquerda para a direita, à altura da mesa. Um único cenário, uma única tomada, luz de janela à esquerda, camisa azul-clara, paleta neutra.

## 2. Folha de controle e abas
- **Folha:** uma folha branca simples, com dez linhas horizontais discretas e vazias, e **mais nada** impresso: sem palavras, cabeçalhos, números, siglas, símbolos, logotipos, brasões, carimbos.
- **Marca a lápis:** um traço curto e neutro na margem, sem forma de "visto" nem de "x".
- **Abas:** duas abas pequenas, de mesmo tamanho, uma azul-petróleo e uma índigo. São aplicadas **uma única vez**, no primeiro conjunto, e não se repetem nos demais, para preservar a consistência dos objetos.

## 3. Ritmo e ação previstos (12 s)
A carga de ações foi reduzida: dois ciclos completos e reconhecíveis, e a repetição nos outros dois conjuntos apenas sugerida.

| Tempo | Conjunto | Ação |
|---|---|---|
| 0–4 s | 1 (clipe preto) | **Ciclo completo:** desliza a folha de controle ao lado das folhas, vira duas páginas devagar, pressiona a aba azul-petróleo e depois a índigo na borda de uma página, faz um traço curto a lápis |
| 4–8 s | 2 (lombada verde) | **Ciclo completo, sem abas:** desliza a mesma folha ao lado do relatório, vira duas páginas devagar, faz um traço curto a lápis |
| 8–10,5 s | 3 (fichário azul) | **Sugerido:** a folha desliza ao lado do fichário e uma página é virada |
| 10,5–12 s | 4 (pasta kraft) | **Sugerido:** a folha repousa ao lado da pasta e a pessoa deposita o lápis sobre ela. A câmera mantém a velocidade, sem parada brusca |

Princípios: gestos lentos e contínuos; câmera e mãos não disputam o protagonismo (a câmera segue as mãos); nenhuma aceleração artificial; final em gesto natural, sem congelamento e sem efeito luminoso.

## 4. Prompt integral (inglês)
```
Documentary-style medium-close lateral tracking shot at desk height, moving from left to right, of an adult professional working at a long wooden desk in a bright contemporary public-institution office. The person is seen from the side and slightly from behind, wearing a light blue shirt, face not visible. Four distinct sets of printed documents are lined up on the desk from left to right: loose white pages held by a black clip, a cream-colored bound report with a green cloth spine, a slate-blue ring binder, and a tan kraft folder with an elastic band. The person uses one single plain white control sheet, printed only with ten faint empty horizontal lines and nothing else, and uses the same sheet at every set. At the first set the person slides the control sheet beside the loose pages, slowly turns two pages, presses one small teal adhesive tab and then one small indigo adhesive tab onto the edge of a page, and makes one short neutral pencil dash in the margin of the control sheet. At the second set the person slides the same control sheet beside the bound report, slowly turns two pages and makes one short pencil dash. At the third set the sheet slides beside the binder and one page is turned. At the fourth set the sheet rests beside the kraft folder and the person lays the pencil down on it. All gestures are slow, continuous and natural, with realistic finger and hand motion and realistic paper physics. The camera glides smoothly and steadily from left to right at desk height with natural parallax, following the hands, at a constant slow speed until the end, one continuous take with no cuts and no digital zoom. Soft natural daylight from a window on the left, wooden desk, neutral palette, shallow depth of field, photographic film-like color. The two tabs keep their color and size and are never duplicated; objects never appear, disappear or change shape. No readable text, letters, numbers or symbols anywhere, no logos, no emblems, no stamps, no legible screens, no sparkles, no glints, no particles, no light flares, no holograms, no sci-fi elements.
```

## 5. Parâmetros de referência (sem execução)
`model=seedance-2-5`, `duration_seconds=12`, `aspect_ratio=16:9`, `resolution=720p`, `turbo=true`, `generate_audio=false`, `quantity=1`, `wait_for_completion=false`. Custo de referência anterior: **116 créditos**. Valor histórico: **recotar** antes de qualquer geração. Sem imagens de referência.

Destino após eventual autorização: `cenas/T3_v02_seedance25_12s_720p.mp4`

## 6. Edição posterior (proposta; nada renderizado)
- **Legendas CNJ, STF, TJDFT e TST** em tipografia real, ordem esquerda-direita, sincronizadas com a passagem da câmera pelos quatro conjuntos (≈ 3 s cada), posição fixa no terço inferior, sem rastreamento do objeto.
- **Contador "10 execuções por instituição · 40 execuções no total":** nos últimos 2 s, **apenas se a sincronização com a passagem pelos conjuntos puder ser validada** na edição; caso contrário, vai só na narração.
- **Revisão humana** de todos os textos antes da exportação.
- As legendas indicam a ordem de apresentação, não que os objetos filmados sejam documentos reais das instituições nem capturas de seus portais. Sugestão de legenda de rodapé: "Representação conceitual do protocolo aplicado".
- A narração permanece como no storyboard: "mesmos critérios, quatro instituições" (`T3`) e "a inteligência artificial localiza e organiza; ela não decide" (`T4`).

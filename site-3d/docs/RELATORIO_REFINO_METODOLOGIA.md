# Relatório — refinamento da Metodologia 3D · 2026-10-14

Escopo: somente a área Metodologia. Nenhum filme, imagem, keyframe ou áudio foi gerado; nenhuma ferramenta de geração do Kairogen foi chamada (saldo não alterado). Histórico anterior preservado (`RELATORIO_REVISAO_VISUAL.md`, `STORYBOARD_FILME_v3.md`).

## Diagnóstico (antes de editar)
Linha de base: `testes/capturas/baseline_estacoes/` (1366×650; palco 847×582 = 62%). Dimensões do canvas = palco em todas as estações (sem defasagem de CSS/viewport).
- **Estação 6:** com a câmera anterior (alvo deslocado −1,6 m, conjunto de 13,4 m de largura) o terceiro instrumento ficava junto à borda do painel.
- **Estação 7 (“faixa estreita à esquerda”):** não era largura de palco nem canvas desatualizado. Era um **quadro intermediário da transição**: o avanço da câmera dependia do número de quadros (dt limitado a 0,05 s por quadro). Em renderizadores lentos a transição levava muitos segundos, deixando a câmera entre as estações 6 e 7. Também havia salto de luz se o usuário navegasse durante uma transição (ambiente partia do alvo anterior, não do estado interpolado).
- Capturas antigas tiradas durante transição não devem ser usadas como referência.

## Correções
`assets/js/cena-arquitetura.js`
1. Transição medida em **tempo real** (`performance.now`, 1,6 s), independente da taxa de quadros.
2. Ambiente e câmera partem do **estado interpolado atual** (sem saltos ao navegar durante a transição).
3. Enquadramento por **largura útil de cada estação** (`w` em metros): a câmera recua o necessário para que o conteúdo caiba no palco para qualquer proporção, sem zoom CSS. Alvos centralizados no conteúdo.
4. Estação 6: instrumentos mais próximos (±4,4 m), rótulos reposicionados; Estação 5: rótulo “Evidências reportadas” elevado para não encobrir o par sem correspondência.
`index.html`/`site.css`: proporção 67/33; rótulos menores em ≤520 px.
`assets/js/app.js`: “Reproduzir percurso” na estação 7 recomeça da estação 1 (antes não fazia nada).
`testes/testar_site.py`: novos testes (ver abaixo). `testes/diagnostico_estacoes.py`: diagnóstico (novo).

## Proporção adotada: 67% cena / 33% painel
Validada nos testes: painel ≥ 300 px mantém as sete etapas, título, explicação, “não é” e controles sem rolagem interna em 1280×590, 1366×650, 1440×780, 1536×720 e 1920×950; fontes não foram reduzidas (mantida a escala por altura). Em ≤900 px o layout empilha (cena, navegação, controles, texto).

## Resultados
- Estação 6: três instrumentos e três rótulos completos em todas as resoluções (inspecionado em 1366×650, 1280×590 e 390×844). Em 390×844 os rótulos ficam menores e escalonados em altura.
- Estação 7: enquadramento estável por navegação sequencial, direta, após redimensionamento (1440×780 → 1280×590) e após reproduzir/pausar.

## Testes automatizados (execução real)
| Navegador | Aprovados / total |
|---|---|
| Chromium 139 | 156/156 |
| Edge 155 | 156/156 |
| Firefox 156 | 156/156 |
Inclui, em 1280×590, 1366×650, 1440×780, 1536×720, 1920×950 e 390×844: controles/painel/navegação dentro da janela nas 7 estações, página sem rolar, cena 64–70% da largura, estações 6 e 7 com canvas = palco e rótulos dentro do palco; reprodução (recomeço, pausa, Próxima ×2, Anterior) e redimensionamento na estação 7.
Observação: uma execução do Firefox expirou em um clique durante edições concorrentes de arquivos; repetida sem edições, passou.

## Inspeção visual realizada
`testes/capturas/depois_refino/` (1366×650 e 1280×590; 7 estações; modos sequencial, natural e direto) e `testes/capturas/{chromium,edge,firefox}/*_metodologia_estacao{1,5,6,7}.png` (seis resoluções). Imagens das estações 5, 6 e 7 e 390×844 foram vistas.

## Limitações
- Renderização por software (SwiftShader); desempenho em GPU real não medido.
- Edge/Firefox: capturas geradas pela suíte, inspecionadas por amostragem (as de Chromium foram o foco).
- Em telas ≤520 px os rótulos 3D permanecem pequenos; o texto completo está no painel.
- GitHub Pages não testado.

## Integridade
533/533 originais conferem com `MANIFESTO_ORIGINAIS_sha256.txt`. Dados e conteúdo científico não alterados.

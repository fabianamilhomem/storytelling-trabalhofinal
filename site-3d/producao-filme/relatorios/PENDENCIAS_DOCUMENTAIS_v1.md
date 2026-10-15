# Pendências documentais e técnicas v1

## 1. Fatos verificados contra a fonte
Conferidos em `fontes/dissertacao.txt` (linhas aproximadas) e em `dados/evidencia_lab.json`.

| Fato | Situação | Onde |
|---|---|---|
| CNJ, STF, TJDFT, TST; 10 execuções por instituição; 40 execuções | Confirmado | JSON `experimento`; dissertação 1898, 1924 |
| Modelo `openai/gpt-4.1`, Reasoning = None | Confirmado | JSON; dissertação 1939 |
| Dois critérios, dez itens por execução: IN84-27-CAPUT (4) e PNTP-12.1-12.2-SIC (6) | Confirmado | JSON; dissertação 1926–1943 |
| Gabarito elaborado inicialmente pela autora e revisado por três especialistas em auditoria governamental vinculados ao TJDFT | Confirmado | Dissertação 1204, 1326–1329 |
| Comparação por rotina determinística | Confirmado | Dissertação 144, 1206 |
| Evidência sem correspondência direta não equivale a falsa | Confirmado | JSON `ressalva` |
| Métricas por instituição (Tabelas 2 e 3) | Conferidas com a dissertação, ver abaixo | Dissertação 1988, 2025–2031 |

Valores conferidos (somente para uso futuro, **não incluídos no filme sem D8**):
- Recall_item: CNJ 93,0% (93/100); STF, TJDFT e TST 100,0% (100/100).
- Cobertura_evidência: CNJ 95,0% (133/140); demais 100,0% (140/140).
- Precisão_evidência: CNJ 71,6% (154/215); STF 58,6% (153/261); TJDFT 39,0% (166/426); TST 46,0% (201/437).

## 2. Pendências
| # | Pendência | Por quê | Quem resolve |
|---|---|---|---|
| P1 | Texto oficial verbatim e datado do art. 27 da IN-TCU 84/2020 e dos subitens 12.1 e 12.2 do PNTP | Não está no projeto. Sem ele, os trechos normativos ficam fora do filme | Autora |
| P2 | Capturas oficiais e datadas dos portais, se forem usadas | Não existem. A data do JSON (07–08/09/2026) é o período das execuções, não a data de captura | Autora |
| P3 | Estado do JSON: `versao: fase1-rascunho` e fonte "ResultadosPreliminares" | Métricas batem com a dissertação, mas o material é preliminar. Definir se o filme usa "resultados preliminares" | Autora |
| P4 | Autorização para citar "especialistas do TJDFT" no filme | A dissertação os descreve como vinculados ao TJDFT; confirmar que a menção institucional é permitida | Autora |
| P5 | Título oficial do trabalho, autoria e créditos (IDP) e uso de logotipo | Texto de créditos não consta do material | Autora |
| P6 | Rótulo de transparência sobre uso de IA na produção das cenas | Recomendado em trabalho acadêmico | Autora |
| P7 | Escolha de voz PT-BR e licença da trilha | Voz não foi consultada; trilha gerada não tem política de uso verificada | Autora |
| P8 | Ferramenta de edição e verificação (ffmpeg ou editor próprio) | Ausente nesta máquina; nada foi instalado | Autora |
| P9 | Avaliação visual do piloto | Aprovação é da autora; não inspecionei quadros | Autora |
| P10 | Recotação de narração e trilha com texto final | Cotações usaram rascunhos | Claude, após aprovação |
| P11 | Caso interpretativo do CNJ (SIC, ouvidoria) | Pode ilustrar "sem correspondência ≠ falso", mas só com a fonte (dissertação 4.1.6) revisada | Autora |

## 3. Informações que NÃO devem aparecer
- Trechos normativos sem fonte oficial verificada.
- Capturas de portais como se fossem registros autênticos.
- Resultados numéricos além dos conferidos acima, ou sem rótulo de preliminar quando P3 assim exigir.
- Frases que atribuam decisão de conformidade à IA.

# Relatório — narração completa, voz Athena (v01)

## Resultado
| Item | Valor |
|---|---|
| Arquivo | `audio/NARRACAO_COMPLETA_ATHENA_v01.mp3` |
| Formato | MP3 (cabeçalho `ID3`; `audio/mpeg`), 128 kb/s |
| Tamanho | 930.002 bytes |
| Duração medida | **58,12 s** (Media Foundation; inclui eventuais silêncios inicial e final) |
| Voz | Athena - Lovely Literature Professor, `fpqzllOdDmER4wwFESLO` |
| Idioma | `pt` (português; locale da voz pt-BR) |
| Ajustes | `stability` 0,7; `style` 0; velocidade e demais itens no padrão (sem aceleração) |
| `audioGenerationId` | `6ad0201daa953c277214fc05` |
| Origem | `https://cdn.kairogen.ai/audio-generations/6acf7a20d4b88cc090a388cf/6ad0201daa953c277214fc05/speech.mp3` |
| Tentativas | 1 (chave de idempotência `narracao-completa-athena-v01`) |

## Custo e saldo
| Item | Valor |
|---|---|
| Cotação antes | 6 créditos (764 caracteres), no teto |
| Custo efetivo | **6 créditos** (≈ R$ 0,99) |
| Saldo antes | 350 |
| Saldo depois | **344** |

Houve uma cotação intermediária de 7 créditos para uma variante com **respelling fonético das siglas** (818 caracteres). Ela **não foi gerada**, por ultrapassar o teto; a variante enviada manteve o texto aprovado integral.

## Texto enviado
Exatamente as seis falas da versão completa de `roteiro/NARRACAO_FILME_v3.md`, seção 2 (N1 a N6), uma por linha, **sem nenhuma alteração**. Comparação automática: N1 a N6 idênticas; 764 caracteres. A versão **longa** de N3 e de N6 foi usada; as alternativas curtas não.

Não há no texto falado `openai/gpt-4.1`, "IN-TCU 84/2020", "PNTP" nem os nomes das métricas; esses termos aparecem só em legendas.

## Verificações realizadas
| Verificação | Resultado |
|---|---|
| Arquivo recuperado e acessível | Sim (HTTP 200) |
| Formato e tamanho | MP3, 930.002 bytes |
| Duração real | 58,12 s |
| Texto enviado igual ao aprovado | Sim |
| Custo e saldo | 6 créditos; 350 → 344 |
| Gravação só em `producao-filme\audio\` | Sim |

## Pendências e limitações
- **Pronúncia não avaliada.** Não ouvi o áudio (este ambiente não reproduz áudio) e **não declaro a pronúncia aprovada**. Em especial, é preciso ouvir CNJ, STF, TJDFT, TST e "IA". Os comentários do serviço não permitem controlar a pronúncia de siglas sem alterar o texto; se alguma sigla sair incorreta, a correção exigiria nova geração paga e autorização separada.
- **Duração por trecho não medida.** Medi apenas o arquivo inteiro. Os 58,12 s coincidem com a estimativa do plano (fala e pausas ≈ 58,0 s), mas a posição de cada fala só pode ser confirmada ouvindo ou analisando o áudio.
- **Pausas.** As pausas entre as falas dependem das quebras de linha; a pausa de 0,6 s antes do fecho de N6 **não** foi marcada, porque não se alterou o texto. Pode não existir.
- **Ritmo, entonação e naturalidade** não verificados.
- **Condições de uso** da voz continuam não documentadas.

## Próximo passo recomendado (não executado)
1. Ouvir `audio\NARRACAO_COMPLETA_ATHENA_v01.mp3` e anotar: pronúncia das siglas, pausas, ritmo, tom.
2. Decidir se o áudio é aceito, ou se alguma parte precisa ser regravada (cada regravação é paga).
3. Só depois, retomar a montagem (`PLANO_MONTAGEM_FILME_v3.md`) com a duração real da narração.

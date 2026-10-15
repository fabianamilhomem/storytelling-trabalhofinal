# Decisões aguardando aprovação

Nenhuma geração será feita antes de resposta explícita a D1, D3 e D12.

| # | Decisão | Opções | Recomendação |
|---|---|---|---|
| D1 | Aprovar estrutura e narração do `STORYBOARD_EXECUTIVO_v1.md` | Aprovar / ajustar | Aprovar após revisar a narração |
| D2 | Reaproveitar o piloto como `T1` | Sim / gerar nova abertura | Sim (economiza 49 créditos) |
| D3 | Cenário e teto de créditos | A: 439 · B: 537 · C: 769 (ver orçamento) | **B**, teto de 731 com reserva de 194 |
| D4 | Resolução | 720p (cotado) / 1080p (≈ +9% por tomada, só 10 s cotado) | 720p; 1080p só se a sala exigir |
| D5 | Narração | TTS Kairogen (≈7 cr) / sua voz / outra ferramenta | Sua voz ou TTS após escolher a voz |
| D6 | Trilha | Gerada (≈7 cr) / sem trilha / licenciada | Sem trilha, ou gerada discreta |
| D7 | Montagem | Instalar ffmpeg (autorizo) / editor próprio | Instalar ffmpeg para verificar e montar |
| D8 | Métricas na tela | Sem números / só Recall_item, Cobertura e Precisão por instituição / rótulo "resultados preliminares" | Mostrar os três nomes sem números no M5; números só após P3 |
| D9 | Rótulo de IA nos créditos | Sim / não | Sim |
| D10 | Frase final | "A IA apoia a análise. A evidência precisa ser rastreável. O julgamento permanece humano." / "A IA localiza. O método compara. A pessoa auditora decide." | Segunda, mais direta |
| D11 | Primeiros quadros por imagem para vídeo | Sim (exige cotar imagens) / não | Não nesta rodada |
| D12 | Protocolo de geração | Uma tomada por vez, `expected_credits`, `wait_for_completion=false`, recuperação pela galeria | Aprovar |
| D13 | Ordem de produção | T2→T6 / começar por T6 (a de maior risco) | Começar por T6 para decidir cedo se o rosto é viável |

## Próximo passo se aprovado
Reconsultar saldo e cotação, gerar `T6` (12 s, 116 créditos) com `expected_credits=116`, baixar para `cenas/` e parar para sua avaliação.

# Plano T3 v01 — cotação, riscos e decisão

Status: **aguardando autorização.** Nenhuma geração, nenhum crédito consumido.

## 1. Estado confirmado nesta consulta
| Item | Resultado |
|---|---|
| Diretório de trabalho | `C:\Fabiana\Mestrado IDP\Storytelling de Dados\Trabalhos\Dashboard_PortalTransparencia\site-3d\producao-filme` |
| Saldo | **620 créditos** (plano PRO ativo, expira em 2026-11-14) |
| Gerações ativas | 0 |
| Seedance 2.5 (`seedance-2-5`) | Disponível. Texto para vídeo e imagem para vídeo. Durações 4–30 s. Turbo restringe a resolução a 720p/1080p |
| Arquivos de cena existentes | `T2` original e aparado, `T6`, piloto. Intactos |

## 2. Cotação atual (`estimate_cost`, plano pro, 16:9, 720p, Turbo, sem áudio)
| Duração | Créditos | R$ | Saldo projetado |
|---|---|---|---|
| 10 s | 97 | 15,52 | 523 |
| **12 s (proposta)** | **116** | **18,56** | **504** |
| 15 s | 144 | 23,04 | 476 |

Sem divergência em relação às cotações anteriores.

## 3. Configuração proposta
12 s: cerca de 3 s por ambiente, janela do Movimento 3 (16–28 s), e margem de 0,5 s para aparar o fim caso reapareça o artefato de brilhos visto no `T2`.

## 4. Saldo projetado
| Passo | Créditos |
|---|---|
| Saldo atual | 620 |
| `T3` 12 s | −116 |
| **Após uma tentativa** | **504** |
| `T4` 10 s e `T5` 10 s previstos | −194 |
| Saldo depois de `T4` e `T5` | 310 |
| Reserva para retakes (dois de 10 s) | 194 |

## 5. Verificação de continuidade
- `T2` aparado (9,73 s, limpo) e `T6`: luz lateral de janela à esquerda, madeira clara, paleta neutra. O prompt de `T3` repete a luz, a mesa de madeira e a paleta.
- `T1`, `T2` e `T6` têm mãos ou pessoa; `T3` não tem pessoas, o que **reduz** o risco de quebra de continuidade humana, mas amplia o salto de escala (de plano fechado para plano de arquitetura).
- Referências em `referencias/`: nenhuma mostra arquitetura institucional ou fotografia oficial. Não há fotos verificadas de CNJ, STF, TJDFT ou TST na pasta, então a tomada é conceitual e **não** atribuída a instituições.

## 6. Riscos
| Risco | Efeito | Mitigação |
|---|---|---|
| Brilhos azulados no fim, como no `T2` | Artefato nos últimos 0,2–0,3 s | Prompt proíbe brilhos; aparar até 0,5 s na edição |
| Mistura entre os quatro ambientes | Transições "derretidas" | Espaço único e contínuo, sem cortes |
| Os quatro ambientes parecerem semelhantes | Perde a ideia de diversidade | Materiais contrastantes no prompt; revisão humana |
| Ritmo rápido demais (3 s por ambiente) | Impressão de apresentação de slides | Travelling único e lento |
| Texto, placas, brasões inventados | Falsa fidelidade institucional | Prompt proíbe; revisão a 100% |
| Mesa/régua inconsistentes entre ambientes | Quebra a metáfora do protocolo | Descrição idêntica por ambiente; avaliação humana |
| Movimento de câmera não lateral ou com zoom | Perda do "parallax" | Prompt específico; revisão humana |
| Sensação de que há "quatro auditorias em tempo real" | Interpretação equivocada | Sem pessoas; legendas só na edição, em ordem fixa |

## 7. Critérios de aprovação
1. Câmera lateral contínua com paralaxe, sem zoom digital.
2. Quatro trechos arquitetônicos claramente distintos.
3. Mesmo arranjo (caixas + régua) visível nos quatro.
4. Nenhum texto, número, logotipo, brasão ou placa legível.
5. Sem brilhos, partículas ou flashes, inclusive nos últimos 0,5 s.
6. Luz e cor compatíveis com `T1`, `T2` e `T6`.
7. Duração e resolução medidas no arquivo (via Media Foundation).

## 8. Procedimento se autorizado
1. Reconsultar saldo e cotação de 12 s imediatamente antes.
2. `generate_video` uma única vez, `expected_credits=116`, `wait_for_completion=false`, `quantity=1`.
3. Recuperar pela galeria ou `get_generation`, sem nova geração por falha de transporte.
4. Baixar para `cenas/T3_v01_seedance25_12s_720p.mp4` sem sobrescrever.
5. Registrar custo, saldo antes e depois, `generation_id`, duração e resolução.
6. Examinar o fim em quadros e interromper para avaliação. Sem retake automático.

## 9. Decisões que preciso de você
1. **Aprovar a troca de ação do `T3`**: de pessoa diante do notebook (storyboard v1) para quatro ambientes.
2. **Aprovar a variação "um espaço contínuo com quatro trechos"** em vez de quatro cenários separados em um só clipe.
3. **Escolher a duração:** 12 s (116) recomendada; 10 s (97) ou 15 s (144).
4. **Autorizar uma tentativa** com teto de 116 créditos.

# Plano de produção v1

Status: planejamento. Nenhuma geração, upload ou instalação foi feita.

## 1. Inventário do que existe e do que se usa
| Ativo | Situação | Uso |
|---|---|---|
| `piloto/piloto_v01_seedance25_5s_720p.mp4` | Aprovado pela autora como prova de conceito (não inspecionei os quadros: sem ffmpeg) | Reaproveitar como `T1` (decisão D2) |
| `referencias/01-documentos.jpg` | Mão, lupa e jornal; luz lateral quente | Só direção de luz. Não enviar ao modelo |
| `referencias/02-evidencias.jpg` | Carimbos legíveis em inglês ("CONFIDENTIAL", "EVIDENCE REVIEW") | **Descartar** como referência de cena |
| `referencias/03-comparacao.jpg` | Lados "VERIFIED"/"DENIED" | **Descartar**: confunde ausência de correspondência com falsidade |
| `referencias/04-auditoria-humana.jpg` | Auditor de óculos em escritório claro; rosto de aparência sintética | Só atmosfera do Movimento 6. Não enviar ao modelo |
| `relatorios/*`, `roteiro/PILOTO_v01.md` | Registros da fase anterior | Base de custo e prompt |

Fontes científicas consultadas, somente leitura: `dados/evidencia_lab.json` e `fontes/dissertacao.txt`. Um storyboard anterior existe em `site-3d/docs/STORYBOARD_FILME_v3.md`, fora desta pasta; foi lido como contexto e não foi copiado nem alterado.

## 2. Estratégia de tomadas
- Uma tomada por movimento, de 10 a 12 s, em vez de muitos clipes curtos.
- Piloto aprovado como `T1`, o que evita 49 créditos e mantém a referência de qualidade.
- Distribuição avaliada: tomadas de 5 a 15 s. **Recomendo 10–12 s**: custo por segundo estabiliza (≈9,6–9,7 cr/s a partir de 8 s) e cada tomada comporta uma ação inteira. Tomadas de 5 s custam ≈9,8 cr/s e obrigariam a mais cortes e mais risco de continuidade.
- Continuidade **não** é garantida por clipe: a mesma pessoa não será reproduzida de forma idêntica entre tomadas. Mitigação: mãos e ombros sem rosto em T2–T5; rosto só em T6.

## 3. Continuidade e estilo
- Luz lateral de janela à esquerda, tons de madeira clara e papel, contraste moderado.
- Câmera sempre motivada (dolly, travelling, panorâmica); nunca zoom digital.
- Reuso do mesmo trecho de prompt-base ("documentary… soft natural side light from a window on the left… realistic paper physics…") em todas as tomadas.
- Opcional (D11): primeiro quadro fixo por tomada via imagem para vídeo. Exigiria gerar imagens, hoje **sem cotação**. Não incluído no orçamento.

## 4. O que é gerado e o que é pós-produção
| Elemento | Gerado por IA | Pós-produção |
|---|---|---|
| Ambientes, mãos, papéis, pessoa | Sim | — |
| Texto de documentos | **Nunca** | Tipografia real |
| Nomes de critérios e instituições | Não | Tipografia real |
| Métricas e números | Não | Só após D8 e conferência |
| Capturas de portais | Não | Só se houver captura oficial e datada (hoje inexistente) |
| Narração | Opcional (TTS) | Sincronização e mixagem |
| Trilha | Opcional | Mixagem discreta |

## 5. Protocolo de geração (quando autorizada)
1. Reconsultar saldo e `estimate_cost` com os mesmos parâmetros da geração.
2. Gerar **uma tomada por vez**, com `expected_credits` igual à cotação e `quantity=1`.
3. Usar `wait_for_completion=false` e recuperar pela galeria. No piloto, a resposta síncrona se perdeu na conexão, embora a geração tenha sido cobrada e concluída.
4. Baixar para `cenas/` com caminho absoluto validado; nunca sobrescrever.
5. Avaliar com os critérios da seção 7 antes da tomada seguinte.
6. Sem retomada automática: qualquer retake exige autorização.

## 6. Pós-produção
- **Ferramenta:** não há `ffmpeg`/`ffprobe` nesta máquina. Há Python 3.13 e Node.js. Nada foi instalado.
- Alternativas: (a) instalar ffmpeg com sua autorização e montar por script; (b) montar em editor próprio (por exemplo CapCut, DaVinci Resolve ou Premiere) a partir dos arquivos de `cenas/` e `audio/`.
- Montagem: cortes motivados pela narração; crossfades curtos de 0,5 a 1 s; correção de cor única para igualar as tomadas.
- Tipografia e legendas: arquivo `.srt`/`.vtt` em PT-BR, sincronizado com a narração.
- Exportação: H.264 MP4, 16:9; 720p nativo (1080p apenas se D4 aprovar, ver orçamento).
- O filme permanece em `final/` e fora do site até aprovação.

## 7. Critérios de aprovação por tomada
| # | Critério | Como verificar |
|---|---|---|
| 1 | Movimento real de mãos, papéis e câmera | Revisão humana quadro a quadro |
| 2 | Sem zoom ou pan sobre imagem estática | Revisão humana |
| 3 | Mãos com cinco dedos e sem fusão com objetos | Revisão em câmera lenta |
| 4 | Nenhum texto legível, logotipo ou carimbo | Revisão em 100% de zoom |
| 5 | Objetos persistentes (notebook, xícara, pilha de papel) | Comparação do 1º e do último quadro |
| 6 | Duração e resolução exatas | ffprobe, após instalação |
| 7 | Luz e paleta compatíveis com `T1` | Comparação lado a lado |
| 8 | Sem leitura de "rejeição" ou "falsidade" | Revisão humana (T5 em especial) |

## 8. Riscos
| Risco | Efeito | Mitigação |
|---|---|---|
| Texto aleatório nas folhas | Parece documento oficial falso | Prompt "text unreadable"; revisão a 100%; desfoque na edição |
| Rosto sintético em T6 | Quebra a credibilidade | Perfil ou três quartos; retake autorizado |
| Quebra de continuidade entre tomadas | Corte percebido | Mesma luz, mesmo prompt-base, correção de cor |
| T5 lida como "reprovação" | Interpretação equivocada | Bandeja neutra, sem cor vermelha, rótulo na edição |
| Falha de transporte na geração | Incerteza de cobrança | Protocolo da seção 5 |
| Resultado preliminar apresentado como definitivo | Erro científico | Decisão D8 |

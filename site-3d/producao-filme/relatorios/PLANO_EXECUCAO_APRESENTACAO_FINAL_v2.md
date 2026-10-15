# Plano de execução — apresentação final do dashboard com persona virtual (≈ 10 min) — v2

Data: 15/10/2026. Status: **somente planejamento e verificação.** Nenhuma mídia foi gerada, nenhum crédito foi consumido, nenhum arquivo existente foi alterado, nada foi enviado ao GitHub. Este é o único arquivo criado nesta etapa.

---

## 1. Estado atual confirmado

| Item | Situação verificada agora |
|---|---|
| Saldo Kairogen | **320 créditos** (consulta de leitura; plano PRO, R$ 0,16/crédito ≈ R$ 51) |
| Teste Wan 3.0 (5 s, 720p) | Concluído, **aprovado** pela autora (semelhança, sincronia, voz e enquadramento). Custo efetivo: 24 créditos (1 + 23). **Não será regerado.** |
| Dashboard, dados, navegação, filme V4 | Aprovados e congelados. Não alterados. |
| Ferramentas locais | `ffmpeg` agora **instalado** (WinGet, v9.0.2) — o plano v1 dizia que não estava. Node.js e Python presentes. Playwright/Edge: **a confirmar** na etapa de gravação (não verificado agora). |
| Pasta `final/_trabalho/` | **Não existe** em `site-3d/` (removida na limpeza). Os scripts `Montagem.cs`, `executar_montagem.ps1` e `textos_dashboard.txt` existem **somente no backup** `Dashboard_PortalTransparencia - Bkp_completo\site-3d\producao-filme\final\_trabalho\`. |
| Fotografia | Publicada em repositório **público** (ver seção 8). |

## 2. Inventário dos ativos

| Ativo | Caminho real | Verificação | Uso |
|---|---|---|---|
| Plano v1 | `site-3d\producao-filme\relatorios\PLANO_PRODUCAO_APRESENTACAO_DASHBOARD_v1.md` | existe, 9.252 B | referência |
| Roteiro v1 | `site-3d\producao-filme\roteiro\APRESENTACAO_DASHBOARD_ROTEIRO_v1.md` | existe, 14.560 B | base do texto |
| Filme V4 | `site-3d\producao-filme\final\FILME_PREVIA_V4.mp4` (cópia idêntica em `site-3d\assets\video\filme-framework-v4.mp4`) | existe, 75.195.237 B; **60,31 s**, H.264 1280×720 **24 fps** + AAC | entra inteiro, com áudio original |
| Narração Athena do filme | `site-3d\producao-filme\audio\NARRACAO_COMPLETA_ATHENA_v01.mp3` | existe, 930.002 B, ≈ 58 s | **não reutilizável** na apresentação (é a fala do filme, já embutida no V4) |
| **Clipe de teste da persona** | `C:\Users\fabia\AppData\Local\Temp\claude\C--Fabiana-Mestrado-IDP-Storytelling-de-Dados-Trabalhos-Dashboard-PortalTransparencia\82dea712-1b75-4747-b7a3-b7fdf1efe1b8\scratchpad\persona_teste_wan30_5s.mp4` | existe, 6.482.054 B; H.264 **1280×720, 30 fps, 5,00 s** + AAC 44,1 kHz estéreo (5,04 s) | **reaproveitável como abertura (A1)** |
| Áudio de referência do teste | `...\scratchpad\persona_teste_A1.mp3` (mesma pasta) | existe, 81.963 B, ≈ 5,1 s, 128 kbps | já embutido no clipe; guardar como referência |
| Miniatura do teste | `...\scratchpad\persona_teste_thumb.webp` | existe, 30.460 B | referência |
| Fotografia (local) | `C:\Users\fabia\Downloads\Foto_Fabiana_Persona.jpg` | existe, 603×450 | identidade da persona |
| Registro no servidor | geração `6ad0f71baa953c27721b2740`; áudio `6ad0f4f8aa953c27721b12e4` | consultado | recuperação pela galeria, se a pasta temporária se perder |

**Aviso:** a pasta do scratchpad é temporária de sessão. **Antes de qualquer outra coisa, copiar o clipe e o áudio de teste para uma pasta fora do repositório e fora do temp** (por exemplo, uma pasta de trabalho própria ao lado do projeto). O vídeo também está na nuvem do Kairogen (URL em `get_generation`).

**O encerramento (Z1) não foi produzido.** Não existe nenhum clipe nem áudio de Z1.

## 3. Reaproveitamento da persona (decisão técnica)

**Abertura (A1): reaproveitar o clipe de teste, custo 0.** O clipe já foi aprovado e fala *"Olá! Eu sou a Fabiana, uma versão sintética minha, criada com IA."* (5 s). A frase original do roteiro tinha 24 palavras (≈ 10,6 s); para não pagar um novo clipe, a segunda parte vai para a voz em off, com a janela da persona oculta:

> A1 (persona, clipe existente): "Olá! Eu sou a Fabiana, uma versão sintética minha, criada com IA."
> A1b (voz em off, texto ajustado): "**Vou apresentar o painel da minha dissertação.** O painel apresenta um framework declarativo de auditoria normativa…"

Consequência: o texto de A1b ganha 45 caracteres. **Exige sua aprovação** (é alteração de roteiro).

**Encerramento (Z1): clipe novo é necessário.** O clipe de teste diz outra coisa; não há como obter a fala de Z1 (*"O framework apoia a auditoria de conformidade; não a substitui. Obrigada por assistir."*, 86 caracteres, ≈ 6,8 s) por edição. Um clipe novo é a única geração de persona realmente necessária.

Limite de 15 s por clipe: não é restrição aqui (5 s e ≈ 7 s). Manter a identidade: mesma foto, mesmo modelo (Wan 3.0), mesma voz Athena (`fpqzllOdDmER4wwFESLO`, `language_code=pt`, sem `voice_settings`, como no teste), 720p, 16:9 e prompt idêntico ao do teste. A semelhança entre as duas tomadas **não é garantida** (seed aleatória no teste); por isso há um critério de aprovação do Z1 (seção 7).

Gerar mais clipes de persona ou ampliar a presença dela **não é recomendado**: custo de 68 créditos por 15 s e nenhum ganho científico.

## 4. Roteiro e estratégia de apresentação

Texto: o do roteiro v1, **sem alteração de dados, números ou ressalvas**, exceto o ajuste de A1/A1b acima. Ordem e telas inalteradas:

A1 (persona) → A1b → A2 → M0 → E1…E7 → F0 → **FILME (silêncio total)** → P1 → R1 → R2 → R3 → R4 → X1 → X2 → Z0 → Z1 (persona).

**Composição visual**
- Tela inteira: gravação do dashboard (1280×720). A persona é uma **janela sobreposta no canto inferior direito** (≈ 26 % da largura, recorte do clipe em torno do rosto e do tronco; no quadro 16:9 do clipe a pessoa ocupa a faixa central-esquerda, com bordas pretas), **só em A1 e Z1**. Rótulo fixo sob a janela: *"Apresentadora virtual gerada com IA a partir de fotografia da autora"*.
- Em A1 e Z1 a gravação do painel deve estar no hero (`#inicio`), onde o canto inferior direito não esconde conteúdo — **conferir quadro a quadro na prévia**.
- **Filme V4:** arquivo original, inteiro, em tela cheia, com o áudio original; 2 s de respiro antes e depois. Persona e voz em off **ausentes** (nenhuma trilha de fala nessa faixa de tempo).
- Fidelidade: textos e números lidos da interface; `textos_dashboard.txt` do backup serve para conferência (copiar para a pasta de trabalho, não para o repositório).

**Decisão sobre taxa de quadros:** exportar a **24 fps** (a do filme V4), para não reamostrar o filme; o clipe da persona (30 fps) e a gravação são conformados a 24 fps. O vídeo do filme é recodificado ao exportar, o conteúdo e o áudio permanecem os do original.

## 5. Etapas mínimas, na ordem correta

Todas fora do repositório (pasta de trabalho própria). Nada vai para `site-3d/` ou GitHub sem aprovação.

| # | Etapa | Gasta crédito? | Gate |
|---|---|---|---|
| 0 | Copiar clipe e áudio de teste para pasta de trabalho segura; copiar scripts do backup | Não | — |
| 1 | Você aprova o ajuste A1/A1b e a lista de pronúncia (seção 6) | Não | **Sua aprovação** |
| **Bloco A** | | | |
| 2 | Gerar o áudio de Z1 (voz Athena, pt) e medir a duração real | 1 | Duração decide 7 s ou 8 s |
| 3 | Gerar o clipe Z1 (Wan 3.0, 720p, 7 ou 8 s, **uma tentativa**) | 32 ou 36 | **Sua avaliação** (identidade, sincronia, voz) |
| **Bloco B** | | | |
| 4 | Voz em off, **por seção** (19 áudios, voz Athena). Começar por E2 (siglas) e P1 (números) como conferência de pronúncia; o restante só após sua escuta | ≈ 52 | **Sua escuta** |
| 5 | Medir a duração real de cada áudio (ffprobe) e recalcular a linha do tempo | Não | — |
| **Bloco C** | | | |
| 6 | Gravar a navegação (Playwright/Edge) cronometrada pelas durações reais | Não | Confirmar que Playwright/Edge funcionam |
| 7 | Montar (ffmpeg) e exportar `APRESENTACAO_DASHBOARD_PREVIA_V1.mp4` fora do repositório | Não | — |
| 8 | Verificações: silêncio no filme, duração total, números, rótulo, quadros A1/Z1 | Não | — |
| 9 | Você assiste, ouve e aprova | Não | **Sua aprovação** |
| 10 | Só então: levar ao projeto o MP4 final (e o roteiro v2), e tratar a privacidade da foto (seção 8) | Não | — |

Por que **por seção** e não em dois lotes (como no v1): o custo é cerca de 12 créditos maior, mas a duração de cada trecho é conhecida sem corte por detecção de silêncio, o que elimina o principal risco de retrabalho pago na montagem. Se preferir economizar, a alternativa de 2 lotes custa ≈ 41 créditos (≈ 35 + ≈ 6), com o risco descrito.

## 6. Riscos de pronúncia e conferência

| Termo | Risco | Mitigação (a decidir por você) |
|---|---|---|
| CNJ, STF, TJDFT, TST, TCU, SIC, PNTP, IA | Pode ler como palavra ou errar a sílaba | Conferir E2 primeiro; se errar, reescrever com grafia fonética **antes** de gerar o restante (a repetição de uma seção custa ≈ 2–5 créditos) |
| `Recall_item`, `Cobertura_evidência`, `Precisão_evidência` | O sublinhado pode ser lido ou ignorado | Aprovar escrever sem sublinhado, por extenso ("Recall item") só no áudio; o painel não muda |
| "Instrução Normativa 84", "12.1 e 12.2", "GPT-4.1" | Números e pontos | Conferir M0, E1, P1 |
| Percentuais e decimais ("71,6 por cento", "0,75") | Vírgula e "por cento" | Conferir R1–R3 |
| Mesma voz do filme (Athena) | Continuidade boa; a persona usa a mesma voz | — |

A pronúncia **só pode ser avaliada de ouvido**; este ambiente não reproduz áudio.

## 7. Custos e saldo projetado

Saldo de partida: **320** (consultado agora).

| Ativo | Situação | Custo já realizado | Custo futuro | Fonte | Saldo projetado |
|---|---|---|---|---|---|
| Clipe de teste Wan 3.0 (reaproveitado como A1) | **Existente** | 23 | 0 | Cobrança real | 320 |
| Áudio de referência do teste | **Existente** | 1 | 0 | Cobrança real | 320 |
| Filme V4 + áudio original | **Existente** | — | 0 | — | 320 |
| Áudio de Z1 | A produzir | — | **1** | `estimate_audio_cost`: 86 caracteres → 1 (cotação) | 319 |
| Clipe Z1, Wan 3.0, 720p | A produzir | — | **32** (7 s) ou **36** (8 s) | `estimate_cost`, cotações de leitura | 287 ou 283 |
| Voz em off, 19 seções | A produzir | — | **≈ 52** | Regra ceil(caracteres × 0,0075), consistente com 4 cotações reais (65→1, 86→1, 138→2, 572→5); a soma de 19 seções é **estimativa** | ≈ 235 ou 231 |
| Gravação, montagem, exportação | A produzir | — | 0 | Local | 235 ou 231 |
| **Total futuro** | | | **≈ 85 a 89** | | **≈ 231–235** |

Cotado agora (confirmadas por consulta): áudio de 65, 86, 138 e 572 caracteres; Wan 3.0 720p de 5 s (23), 7 s (32) e 8 s (36); 480p de 7 s (16). **Estimadas, não garantidas:** a soma da voz em off e a duração real de cada áudio.

**Reserva:** ≈ 231–235 créditos após a conclusão, suficiente para: repetir Z1 uma vez (36), regenerar até 10 seções de voz (≤ ≈ 5 cada) e ainda sobrar. Nenhuma geração cosmética é recomendada.

**Teto proposto por bloco:** Bloco A ≤ 37; Bloco B ≤ 56 (inclui margem de arredondamento).

## 8. Duração e sincronização

| Componente | Estimativa |
|---|---|
| Persona A1 (clipe existente) | 5,0 s |
| Voz em off (853 palavras ≈ 846 do roteiro + 7 do ajuste A1b) | 449 s a 1,9 pal./s |
| Navegação entre seções (20 trocas × ≈ 3 s) | ≈ 58 s |
| Persona Z1 | ≈ 7 s |
| Filme V4 (60,3 s + 2 s de respiro antes e depois) | 64,3 s |
| **Total, ritmo de 1,9 pal./s** | **≈ 583 s ≈ 9 min 43 s** |
| **Total, ritmo de 2,3 pal./s** | **≈ 505 s ≈ 8 min 25 s** |

Os 2,3 pal./s vêm da frase curta do teste (12 palavras em ≈ 5,1 s); 1,9 é a calibragem da Athena na narração do filme. **A duração real só será conhecida depois de gerar a narração;** espera-se entre 8 min 25 s e 9 min 45 s. Não há risco de exceder 10 min no cenário conservador.

Silêncio no filme: garantido pela construção (nenhuma trilha de fala entre o início do respiro e o fim do filme); será conferido por análise do envelope de áudio na etapa 8.

## 9. Riscos e critérios de aprovação

| Risco | Probabilidade | Efeito | Mitigação / critério |
|---|---|---|---|
| Semelhança do Z1 diferente da do clipe de abertura | Média | Persona inconsistente | Mesmos insumos do teste. **Critério:** mesma pessoa reconhecível e boca sincronizada, aprovado por você. Se falhar, **uma** repetição (36 créditos), e ainda sobra margem |
| Cortes ou truncamento do Z1 | Baixa | Fala cortada | Duração do clipe ≥ duração medida do áudio + 0,3 s |
| Pronúncia de siglas | Média | Retrabalho de seções | Testar E2/P1 primeiro; texto fonético |
| Taxa de quadros da gravação (WebM ≈ 12,5 fps no teste anterior) | Média | Rolagem travada | Rolagens curtas; estações estáticas; ou gravação H.264 |
| Janela da persona cobrindo conteúdo | Baixa | Prejuízo à leitura | Persona só em A1/Z1, hero, canto livre; conferir na prévia |
| Voz da persona e da narração diferentes em timbre | Baixa | Estranhamento | Mesma voz (Athena), mesmos parâmetros |
| Perda do clipe de teste na pasta temporária | Média | Reprodução paga | Etapa 0 (copiar agora) |
| Pendências P3 (preliminar), P4 (especialistas TJDFT), P5 (autoria) | Existentes | Texto da fala | Mantidas como no painel |
| Declaração em primeira pessoa por versão sintética | — | Ética | Rótulo de IA visível; sua aprovação do texto |

Critérios de aprovação da prévia final: (a) filme V4 inteiro, com áudio original e sem outra fala; (b) números e ressalvas idênticos ao painel; (c) rótulo de IA visível nas duas tomadas; (d) duração entre 8 e 10 min; (e) sem corte de fala; (f) sua aprovação auditiva.

## 10. Pendência de privacidade — fotografia no GitHub (não executar agora)

- Arquivo: `_temp/Foto_Fabiana_Persona.jpg`, repositório público `fabianamilhomem/storytelling-trabalhofinal`, branch `main`, commit **`3c23c404006848fe4873d8dc30dd7492cead8485`**. É o **único commit** do repositório (estava vazio).
- **Não remover ainda:** a foto é necessária para gerar o Z1 (Bloco A). Remover **depois** da geração do Z1 e da sua aprovação, não antes.
- **Excluir o arquivo não basta:** ele permanece no commit e pode estar em caches, forks, clones, buscas ou na cópia mantida pelo Kairogen. Nenhuma remoção garante o apagamento de cópias já feitas.
- Como o repositório só tem esse commit, a opção mais simples é **apagar e recriar o repositório** (ou reescrever o histórico e fazer *force push*) antes de publicar o trabalho; depois, verificar o acesso direto pelo SHA e solicitar a limpeza de visualizações em cache, se necessário. A decisão e a execução ficam para outra etapa, com sua autorização.
- Alternativa para evitar nova exposição: nas próximas etapas, não reenviar a foto a repositórios públicos (para o Z1 será necessário reutilizar a URL já pública; ela só deve ser removida após a geração).

## 11. Próxima autorização específica necessária

Para iniciar o **Bloco A**, preciso de uma autorização expressa que contenha:

1. **Aprovação do ajuste de texto**: A1 = frase curta do teste; "Vou apresentar o painel da minha dissertação." passa para o início de A1b.
2. **Autorização para gerar o áudio de Z1** (1 crédito) e, após medir a duração, **um único clipe Z1** com Wan 3.0, 720p, 7 ou 8 s (32 ou 36 créditos), sem repetição automática e sem troca de modelo.
3. **Teto para o Bloco A: 37 créditos.**
4. Confirmação de que a mesma URL pública da foto (commit `3c23c40`) pode ser usada mais uma vez.
5. (Opcional, agora) autorização para copiar o clipe e o áudio de teste da pasta temporária para uma pasta de trabalho segura.

Nada além disso será feito. O Bloco B (voz em off) exigirá uma autorização separada, com teto de 56 créditos, depois da avaliação do Z1.

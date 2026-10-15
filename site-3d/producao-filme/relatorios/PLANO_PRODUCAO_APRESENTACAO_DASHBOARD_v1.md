# Plano de produção — apresentação acadêmica do dashboard (≈ 10 min) — v1

Status: **plano; nada foi gerado, gravado ou pago.** Nenhum crédito consumido. Saldo consultado agora: **344 créditos** (plano PRO, crédito = R$ 0,16 → ≈ R$ 55; renovação em 14/11/2026). Roteiro: `roteiro/APRESENTACAO_DASHBOARD_ROTEIRO_v1.md`.

## 1. Inspeção do que já existe
| Recurso | Local | Observação |
|---|---|---|
| Dashboard validado | `site-3d/index.html` (somente leitura) | Textos e valores lidos da interface renderizada: `final/_trabalho/textos_dashboard.txt` |
| Filme V4 (com áudio original) | `final/FILME_PREVIA_V4.mp4` · cópia no site em `assets/video/filme-framework-v4.mp4` | 60,31 s, 1280×720, H.264 + 1 faixa de áudio; SHA-256 `51d561f3…cc30274` |
| Narração Athena do filme | `audio/NARRACAO_COMPLETA_ATHENA_v01.mp3` | voz `fpqzllOdDmER4wwFESLO` |
| Montagem local | `final/_trabalho/Montagem.cs` / `executar_montagem.ps1` (Media Foundation `MediaComposition`) | Sem instalação; já usa vídeo, imagem, sobreposições e trilha de áudio |
| Captura local | Playwright + Microsoft Edge (instalados) | Teste feito agora: gravação do painel em **WebM VP8**; o Media Foundation **lê** o arquivo (comprovado em `final/_trabalho/teste_webm/`) |
| Foto da autora | **não encontrada em `producao-filme/`** | `referencias/` contém só as quatro imagens de apoio das cenas. **É preciso fornecer a foto.** |
| ffmpeg | não instalado | não necessário para o fluxo proposto |

## 2. Catálogo Kairogen (consulta somente leitura)
Modelos de vídeo com **fala sincronizada por áudio fornecido** e identidade a partir de imagem:
| Modelo | Áudio de referência | Imagem como identidade | Duração do clipe | Cotação 15 s / 720p (PRO) |
|---|---|---|---|---|
| **Wan 3.0** (`wan-3-0`) | até 5 áudios, **total 15 s**; "o personagem faz lip-sync" | Sim (imagem inicial) | 2–30 s | **68 créditos** (480p: 34; 1080p: 135; 5 s/720p: 23) |
| Seedance 2.0 Mini | até 3 áudios, 15 s; "fala exatamente o áudio enviado" | Sim (first frame) | 4–15 s | 80 (5 s: 27) |
| Seedance 2.0 Fast | 3 áudios, 15 s | Sim | 4–15 s | 118 |
| Seedance 2.0 | 3 áudios, 15 s | Sim | 4–15 s | 180 |
| Seedance 2.5 | até 10 áudios, 30 s | **Não** ("só disponível sem First Frame") | 4–30 s | 144 (turbo) |
Outros (Veo 3.1, Kling, Grok, Wan 2.6/2.7): sem entrada de áudio com lip-sync a partir de arquivo. KairoClone V3 é transferência de movimento a partir de vídeo, não fala por áudio.
- **Idioma**: nesses modelos o áudio enviado é a fala; o idioma é o do próprio áudio. Português brasileiro depende do áudio gerado (voz Athena) e **a qualidade do lip-sync em pt-BR não foi verificada**.
- **Limite**: **cada clipe com fala sincronizada é limitado a 15 s de áudio**. Uma apresentação de 10 minutos com a persona falando o tempo todo exige ≈ 38 clipes encadeados. O limite de duração do vídeo (até 30 s em Wan 3.0) não ajuda porque o áudio de referência é limitado a 15 s.

## 3. Custos (todas as cotações vieram de `estimate_cost`/`estimate_audio_cost`; o que é extrapolado está marcado)
| Item | Cotação | Créditos |
|---|---|---|
| Voz em off, lote 1 (2.395 caracteres) | cotado | **18** |
| Voz em off, total (≈ 5.300 caracteres) | **estimativa** (0,0075 crédito/caractere, linear) | ≈ 40 |
| Áudios da persona A1 e Z1 (≈ 230 caracteres) | estimativa | ≈ 2 |
| Teste de lip-sync, Wan 3.0, 5 s, 720p | cotado | **23** |
| Persona A1 (≈ 13 s) e Z1 (≈ 7 s), Wan 3.0 720p | teto cotado: 15 s = 68 cada | ≤ 136 |
| **Solução recomendada** (teste + 2 clipes + voz) | soma | **≤ ≈ 201** (≈ R$ 32) |
| Saldo restante | 344 − 201 | **≈ 143** (duas repetições de clipe de 68) |
| Alternativa: persona falando o tempo todo | ≈ 38 clipes × 68 + voz | **≈ 2.630** (≈ R$ 420) — **excede o saldo em ≈ 2.290 créditos** |
Cada 15 s adicionais de persona custam 68 créditos (≈ R$ 10,90). Resolução 480p custa a metade (34), mas a janela ficará menos nítida.

## 4. Arquitetura mais simples
1. **Uma única trilha de tela**: gravação automatizada do dashboard (Playwright, Edge, 1280×720), seguindo o roteiro, com tempos ancorados na duração real de cada trecho de áudio.
2. **Uma narração** (voz Athena, a mesma do filme), gerada em dois lotes e dividida por seção, com a duração real medida.
3. **Persona em janela sobreposta** (canto inferior direito, com o rótulo de IA) **só nas duas tomadas**: abertura (A1) e fecho (Z1). Fora delas, a janela some e a voz segue em off.
4. **Filme V4**: o arquivo original entra **inteiro** na linha do tempo, em tela cheia, com seu áudio original; a voz em off e a persona ficam em silêncio durante 60,3 s + 2 s de respiro, e a narração retoma ao voltar para o painel. (Não se grava o filme pela tela: o arquivo original preserva qualidade e áudio.)
5. **Montagem** local com o mesmo `MediaComposition` (acrescentar ao `Montagem.cs` sobreposições de vídeo com áudio habilitado e mais trilhas de áudio).
6. **Exportação** MP4 H.264 1280×720; sem publicação.

## 5. Fluxo mais curto
| # | Etapa | Quem | Custo |
|---|---|---|---|
| 1 | Aprovar roteiro, rótulo da persona e primeira pessoa ("Eu sou a Fabiana…") | Você | 0 |
| 2 | Fornecer a fotografia (frontal, bem iluminada, rosto inteiro) e confirmar o uso da sua imagem | Você | 0 |
| 3 | Gerar áudios A1 e Z1 (e um corte de 5 s para o teste) | Automático | ≈ 3 |
| 4 | **Teste** de lip-sync de 5 s (Wan 3.0, 720p) — avaliar rosto, boca e fidelidade | Automático + você | 23 |
| 5 | Gerar a voz em off (2 lotes) e medir durações | Automático | ≈ 40 |
| 6 | Ouvir a voz em off (pronúncia de CNJ, STF, TJDFT, TST, SIC, IA, "Recall_item") | **Você** | 0 |
| 7 | Gerar persona A1 e Z1 (≤ 68 cada) | Automático | ≤ 136 |
| 8 | Gravar a navegação com tempos reais | Automático | 0 |
| 9 | Montar e exportar a prévia | Automático | 0 |
| 10 | Assistir, ouvir e aprovar | **Você** | 0 |

## 6. Duração estimada
≈ **9 min 49 s** (589 s): 8 min 45 s de fala/navegação + filme de 64 s. Estimada a 1,9 palavra/s (calibrada na narração Athena) e 883 palavras; a duração real só se conhece após a geração do áudio. Ajuste de ±30 s é esperado.

## 7. Automatizável × manual
| Automatizável | Manual / decisão sua |
|---|---|
| Extração de textos do dashboard (feita) | Fornecer a fotografia; autorizar o uso da sua imagem |
| Geração da voz (com autorização e teto) | Aprovar roteiro, rótulo de IA, primeira pessoa |
| Gravação cronometrada da navegação (Playwright) | Ouvir a voz e a persona (este ambiente não reproduz áudio) |
| Montagem e exportação (Media Foundation) | Avaliar sincronia labial e naturalidade |
| Verificações por quadros e envelope de áudio | Decidir repetições; pendências P3/P4/P5 |

## 8. Riscos principais
1. **Sincronia labial e aparência em pt-BR não verificadas**; só o teste de 5 s revelará. Pode ser necessário trocar de modelo (Seedance 2.0 Mini, 80 créditos por 15 s).
2. **Verossimilhança com a foto**: modelo gera rosto novo a partir da imagem; semelhança e continuidade entre as duas tomadas não são garantidas. Políticas de uso do serviço para rostos reais podem recusar a geração.
3. **Limite de 15 s por clipe**: impede a persona contínua dentro do saldo atual (seção 3).
4. **Saldo apertado**: 344 créditos; qualquer repetição além de duas esgota o saldo.
5. **Voz**: Athena já foi usada no filme; pronúncia de siglas pode falhar e exigiria nova geração paga.
6. **Taxa de quadros da gravação de tela** (WebM, ≈ 12,5 quadros/s medidos no teste) pode parecer travada em rolagens rápidas; mitigação: rolagens curtas e estações estáticas, ou gravação manual com a Xbox Game Bar (H.264).
7. **Fidelidade**: a persona fala em primeira pessoa ("elaborado por mim", "minha dissertação"); depende de você aceitar que a versão sintética fale em seu nome; rótulo de IA visível recomendado.
8. **Pendências abertas**: status "preliminar" (P3), citação dos especialistas do TJDFT (P4) e autoria (P5): o roteiro as repete como estão no painel.
9. **Publicação**: não validada (GitHub Pages não testado).

## 9. Arquivos necessários
- Fotografia da autora (a fornecer; JPG/PNG, ≥ 300 px no lado menor, ≤ 10 MB).
- `roteiro/APRESENTACAO_DASHBOARD_ROTEIRO_v1.md` aprovado.
- `final/FILME_PREVIA_V4.mp4` (existente).
- Dashboard local `site-3d/index.html` (somente leitura).
- Saídas futuras, todas em `producao-filme/`: `audio/` (voz em off e áudios da persona), `cenas/` (clipes da persona), `final/_trabalho/` (gravação, specs), `final/APRESENTACAO_DASHBOARD_PREVIA_V1.mp4`.

## 10. Próxima ação recomendada
**Enviar a fotografia e aprovar o roteiro (e o rótulo de IA)**, para que eu peça sua autorização expressa, com teto de **26 créditos**, para gerar os áudios da persona e o **teste de lip-sync de 5 s** (23 + ≈ 3), único passo pago antes de decidir o restante.

## 11. O que não foi feito
Nenhuma imagem, áudio ou vídeo foi gerado; nenhum crédito foi consumido; o dashboard, os dados e o filme V4 não foram alterados; nada foi gravado fora de `producao-filme/`.

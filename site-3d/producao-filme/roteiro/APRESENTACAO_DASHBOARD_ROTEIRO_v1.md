# Roteiro da apresentação do dashboard — v1 (proposta, sem produção)

Status: **roteiro proposto; nada foi gerado, gravado ou pago.** Idioma: português brasileiro. Duração estimada: **≈ 589.0 s (≈ 9 min 49 s)**, incluindo o filme V4 integral (60,3 s) e pausas de navegação.

## 1. Premissas
- Conteúdo extraído **do próprio dashboard validado** (textos e valores lidos da interface renderizada; ver `final/_trabalho/textos_dashboard.txt`). Nenhum número novo foi introduzido.
- Ritmo de fala: **1,9 palavra/s**, calibrado na narração Athena já gerada (111 palavras em ≈ 58 s, com pausas). É estimativa; a duração real só existe após a geração do áudio.
- O tempo por seção soma fala + 3 s de navegação (1,5 s nas seções com a persona). O filme ocupa 60,3 s + 4 s de entrada e saída.
- **Durante o filme**: persona em silêncio e nenhuma voz em off; só o áudio original do filme.
- **Persona** aparece em duas tomadas curtas (≤ 15 s de áudio cada, limite do modelo): abertura (A1) e fecho (Z1). Todo o restante é voz em off, com a mesma voz.
- Rótulo na tela da persona: *"Apresentadora virtual gerada com IA a partir de fotografia da autora"* (proposto; decisão sua).
- Termos lidos por extenso na fala: "Recall_item", "Cobertura_evidência" e "Precisão_evidência" aparecem como no painel; siglas CNJ, STF, TJDFT, TST, SIC e TCU devem ser conferidas de ouvido (a pronúncia de siglas é risco conhecido da voz Athena).

## 2. Roteiro por seção

| # | Tela (rota) | Quem fala | Palavras | Duração est. |
|---|---|---|---|---|
| A1 | Abertura do painel (hero) e título (`#inicio`) | JANELA DA PERSONA (clipe 1, ≤ 15 s) | 24 | 14 s |
| A1b | Abertura do painel: título e 'Percorrer a metodologia' (`#inicio`) | voz em off (janela da persona oculta) | 43 | 26 s |
| A2 | Rolagem: pergunta de pesquisa e 'O desafio da evidência' (`#inicio`) | voz em off | 88 | 49 s |
| M0 | Aba Metodologia: cabeçalho e quatro números (`#metodologia`) | voz em off | 35 | 21 s |
| E1 | Estação 1 · Norma e requisitos verificáveis (`#metodologia (estação 1)`) | voz em off | 39 | 24 s |
| E2 | Estação 2 · Quatro portais institucionais (`#metodologia (estação 2)`) | voz em off | 19 | 13 s |
| E3 | Estação 3 · Coleta orientada por IA generativa (`#metodologia (estação 3)`) | voz em off | 26 | 17 s |
| E4 | Estação 4 · Organização das evidências (`#metodologia (estação 4)`) | voz em off | 20 | 14 s |
| E5 | Estação 5 · Comparação determinística com o gabarito (`#metodologia (estação 5)`) | voz em off | 40 | 24 s |
| E6 | Estação 6 · Métricas (`#metodologia (estação 6)`) | voz em off | 19 | 13 s |
| E7 | Estação 7 · Interpretação humana (`#metodologia (estação 7)`) | voz em off | 21 | 14 s |
| F0 | Rolagem até 'O framework em cerca de um minuto' (`#metodologia (seção do filme)`) | voz em off; termina ANTES do filme | 17 | 12 s |
| FILME | Reprodução integral do filme V4 (arquivo local, com seu áudio original) (`#metodologia`) | PERSONA E VOZ EM SILÊNCIO; somente o áudio do filme | 0 | 64 s |
| P1 | Retorno ao painel: 'Parâmetros e critérios do experimento' (`#metodologia (rolagem)`) | voz em off | 36 | 22 s |
| R1 | Resultados · Recall_item (`#resultados/recall`) | voz em off | 82 | 46 s |
| R2 | Resultados · Cobertura_evidência (`#resultados/cobertura`) | voz em off | 61 | 35 s |
| R3 | Resultados · Precisão_evidência (`#resultados/precisao`) | voz em off | 91 | 51 s |
| R4 | Resultados · Síntese interpretativa (`#resultados/sintese`) | voz em off | 92 | 51 s |
| X1 | 40 execuções · mapa e execução selecionada (CNJ, Rep. 2) (`#execucoes`) | voz em off | 45 | 27 s |
| X2 | Fontes (`#fontes`) | voz em off | 25 | 16 s |
| Z0 | Retorno ao Início (`#inicio`) | voz em off | 47 | 28 s |
| Z1 | Fecho no Início (hero) (`#inicio`) | JANELA DA PERSONA (clipe 2, ≤ 15 s) | 13 | 8 s |
| | **Total** | | **883** | **589 s** |

## 3. Texto de cada seção

### A1 — Abertura do painel (hero) e título
- Tela: `#inicio` · Voz/persona: JANELA DA PERSONA (clipe 1, ≤ 15 s) · ≈ 14 s

> Olá! Eu sou a Fabiana, uma versão sintética minha, criada com IA a partir de uma fotografia. Vou apresentar o painel da minha dissertação.

### A1b — Abertura do painel: título e 'Percorrer a metodologia'
- Tela: `#inicio` · Voz/persona: voz em off (janela da persona oculta) · ≈ 26 s

> O painel apresenta um framework declarativo de auditoria normativa assistido por IA generativa, aplicado a portais de transparência do Poder Judiciário. Os resultados são preliminares e descritivos. Em cerca de dez minutos, você verá o desafio, o método, um filme-síntese e os resultados.

### A2 — Rolagem: pergunta de pesquisa e 'O desafio da evidência'
- Tela: `#inicio` · Voz/persona: voz em off · ≈ 49 s

> A pergunta que orienta o trabalho é: como um framework declarativo, assistido por IA generativa, pode operacionalizar requisitos e apoiar a avaliação da conformidade da prestação de contas pública? Considero três aspectos: o atendimento dos requisitos, a seleção das evidências e a estabilidade entre execuções. O desafio é a evidência. Acertar o requisito não basta: uma conclusão de auditoria precisa mostrar de onde ela vem. Por isso o trabalho separa os papéis. A IA localiza, uma rotina determinística compara com um gabarito independente, e a pessoa auditora decide.

### M0 — Aba Metodologia: cabeçalho e quatro números
- Tela: `#metodologia` · Voz/persona: voz em off · ≈ 21 s

> Na Metodologia, o percurso tem sete estações. Cada uma diz o que é feito, por quem, e o que não é feito. São dois critérios normativos, quatro instituições, dez itens por execução e quarenta execuções.

### E1 — Estação 1 · Norma e requisitos verificáveis
- Tela: `#metodologia (estação 1)` · Voz/persona: voz em off · ≈ 24 s

> Primeira estação, a norma. O artigo 27 da Instrução Normativa 84 do TCU e os subitens 12.1 e 12.2 do Programa Nacional de Transparência Pública viram dez itens verificáveis: quatro mais seis. Os critérios são definidos antes da coleta.

### E2 — Estação 2 · Quatro portais institucionais
- Tela: `#metodologia (estação 2)` · Voz/persona: voz em off · ≈ 13 s

> Segunda, quatro portais: CNJ, STF, TJDFT e TST. Os mesmos critérios, aplicados a estruturas diferentes, usando apenas informações públicas.

### E3 — Estação 3 · Coleta orientada por IA generativa
- Tela: `#metodologia (estação 3)` · Voz/persona: voz em off · ≈ 17 s

> Terceira, a coleta. Um agente de IA generativa percorre os portais, localiza páginas e documentos e os organiza como evidências. Ele localiza e organiza. Não decide.

### E4 — Estação 4 · Organização das evidências
- Tela: `#metodologia (estação 4)` · Voz/persona: voz em off · ≈ 14 s

> Quarta, a organização: cada evidência reportada fica vinculada ao requisito que pretende demonstrar. Reportar uma evidência não equivale a validá-la.

### E5 — Estação 5 · Comparação determinística com o gabarito
- Tela: `#metodologia (estação 5)` · Voz/persona: voz em off · ≈ 24 s

> Quinta, a comparação. O gabarito é independente do modelo: foi elaborado por mim e revisado por três especialistas em auditoria governamental do TJDFT. Uma rotina determinística compara as evidências reportadas com ele. Evidência sem correspondência direta não é automaticamente falsa.

### E6 — Estação 6 · Métricas
- Tela: `#metodologia (estação 6)` · Voz/persona: voz em off · ≈ 13 s

> Sexta, as métricas: Recall_item, Cobertura_evidência e Precisão_evidência. Três perguntas diferentes. Nenhuma é medida de acurácia, nem certificação de conformidade.

### E7 — Estação 7 · Interpretação humana
- Tela: `#metodologia (estação 7)` · Voz/persona: voz em off · ≈ 14 s

> Sétima, a interpretação humana. A pessoa auditora lê criticamente os resultados. A arquitetura apoia a auditoria; não substitui o julgamento profissional.

### F0 — Rolagem até 'O framework em cerca de um minuto'
- Tela: `#metodologia (seção do filme)` · Voz/persona: voz em off; termina ANTES do filme · ≈ 12 s

> Agora, um filme de cerca de um minuto resume o framework. Vou me calar para você assistir.

### FILME — Reprodução integral do filme V4 (arquivo local, com seu áudio original)
- Tela: `#metodologia` · Voz/persona: PERSONA E VOZ EM SILÊNCIO; somente o áudio do filme · ≈ 64 s

> *(sem fala; reproduz-se o filme V4 inteiro, com o áudio original)*

### P1 — Retorno ao painel: 'Parâmetros e critérios do experimento'
- Tela: `#metodologia (rolagem)` · Voz/persona: voz em off · ≈ 22 s

> Os parâmetros do experimento: dois critérios, dez itens por execução, quatro instituições, dez repetições, quarenta execuções. O modelo foi o GPT-4.1, da OpenAI, sem modo de raciocínio, executado em 7 e 8 de setembro de 2026.

### R1 — Resultados · Recall_item
- Tela: `#resultados/recall` · Voz/persona: voz em off · ≈ 46 s

> Primeira pergunta: os itens normativos esperados foram identificados como atendidos? STF, TJDFT e TST atenderam os dez itens nas dez repetições. No CNJ, 93 de 100 itens foram atendidos; as omissões ocorreram em três repetições e se concentram no critério do SIC. Elas ocorreram nas repetições 2, 3 e 4, com 7, 9 e 7 itens atendidos de 10. O recall médio do CNJ foi 100 por cento no critério da Instrução Normativa 84 e 88,3 por cento no critério do PNTP.

### R2 — Resultados · Cobertura_evidência
- Tela: `#resultados/cobertura` · Voz/persona: voz em off · ≈ 35 s

> Segunda: das evidências de referência, quantas foram localizadas e salvas? STF, TJDFT e TST localizaram os 140 componentes esperados. O CNJ localizou 133 de 140, ou 95 por cento. Cobertura de 100 por cento indica que os componentes previstos foram encontrados; não informa se tudo o que foi reportado tem correspondência com o gabarito. Essa é a pergunta da próxima métrica.

### R3 — Resultados · Precisão_evidência
- Tela: `#resultados/precisao` · Voz/persona: voz em off · ≈ 51 s

> Terceira: das evidências reportadas, quantas têm correspondência direta com o gabarito? No CNJ, 71,6 por cento; no STF, 58,6; no TST, 46,0; e no TJDFT, 39,0. Em números absolutos, são 154 de 215 evidências no CNJ e 166 de 426 no TJDFT. A parte sem correspondência não significa evidência falsa: significa que não houve correspondência direta com um gabarito positivo fechado. Essa leitura cabe à pessoa auditora. O limiar de correspondência textual foi 0,75, e o teste com 0,80, 0,85 e 0,90 alterou a precisão em menos de um ponto percentual.

### R4 — Resultados · Síntese interpretativa
- Tela: `#resultados/sintese` · Voz/persona: voz em off · ≈ 51 s

> Na síntese: cem por cento não é o mesmo que evidência perfeita. STF, TJDFT e TST alcançaram cem por cento de Recall_item e de Cobertura_evidência, e ainda assim a Precisão_evidência variou de 39 a 58,6 por cento. Há um caso que pede olhar humano: no CNJ, o sistema reportou a página de acesso à informação, e o gabarito previa a ouvidoria. É uma evidência real da instituição, sem correspondência com a referência específica. Os limites: resultados descritivos, um modelo, quatro instituições, quarenta execuções, dois critérios e nenhuma generalização para o Judiciário brasileiro.

### X1 — 40 execuções · mapa e execução selecionada (CNJ, Rep. 2)
- Tela: `#execucoes` · Voz/persona: voz em off · ≈ 27 s

> Na seção 40 execuções, cada execução aparece lado a lado. Escolha a métrica e selecione uma célula, uma instituição ou uma repetição. Por exemplo, a repetição 2 do CNJ: 7 de 10 itens, Recall de 70 por cento, Cobertura de 78,6 e Precisão de 57,9.

### X2 — Fontes
- Tela: `#fontes` · Voz/persona: voz em off · ≈ 16 s

> Em Fontes estão os portais e hubs de transparência percorridos, com a origem declarada. As coletas ocorreram em 7 e 8 de setembro de 2026.

### Z0 — Retorno ao Início
- Tela: `#inicio` · Voz/persona: voz em off · ≈ 28 s

> Em resumo: a IA generativa localiza e organiza evidências; uma rotina determinística as compara com um gabarito independente; e a pessoa auditora interpreta e decide. Os dados, a metodologia e as ressalvas estão no painel; explore as quarenta execuções e leia a síntese com atenção aos limites.

### Z1 — Fecho no Início (hero)
- Tela: `#inicio` · Voz/persona: JANELA DA PERSONA (clipe 2, ≤ 15 s) · ≈ 8 s

> O framework apoia a auditoria de conformidade; não a substitui. Obrigada por assistir.

## 4. Conferência de fidelidade

| Afirmação do roteiro | Fonte no dashboard |
|---|---|
| 2 critérios, 4 instituições, 10 itens, 40 execuções | Metodologia · quatro números |
| 4 + 6 = 10 itens (IN-TCU 84 art. 27; PNTP 12.1 e 12.2) | Estação 1 e tabela de critérios |
| Gabarito elaborado pela pesquisadora e revisado por três especialistas do TJDFT | Estação 5 |
| Modelo openai/gpt-4.1, Reasoning = None; 7–8/09/2026 | Parâmetros do experimento |
| Recall: CNJ 93/100; STF, TJDFT, TST 100/100; omissões nas repetições 2, 3 e 4 (7, 9 e 7 de 10); recall médio CNJ 100% (IN84) e 88,3% (PNTP) | Resultados · Recall_item |
| Cobertura: CNJ 133/140 (95,0%); demais 140/140 | Resultados · Cobertura_evidência |
| Precisão: CNJ 71,6% (154/215); STF 58,6%; TST 46,0%; TJDFT 39,0% (166/426); limiar 0,75; sensibilidade < 1 p.p. | Resultados · Precisão_evidência |
| CNJ Rep. 2: 7/10, 70,0%, 78,6%, 57,9% | 40 execuções · tabela CNJ por repetição |
| Ressalvas: descritivo, um modelo, quatro instituições, 40 execuções, dois critérios, sem generalização | Síntese · Limites da leitura |

Ajuste de redação a validar: a fala cita "o critério do SIC" e "critério do PNTP" para o critério PNTP-12.1-12.2-SIC, como o próprio painel; e diz "três repetições" para as omissões do CNJ (2, 3 e 4).

## 5. Divisão para a geração
- **Voz em off**: todas as seções, exceto FILME e as duas tomadas da persona, em dois lotes de ≤ 5.000 caracteres (limite da cotação de áudio): 5297 caracteres no total.
- **Persona**: A1 (138 caracteres, ≈ 12.6 s) e Z1 (86 caracteres, ≈ 6.8 s), gerados como áudios próprios, para servirem de referência de lip-sync.

# Storyboard executivo v1 — "Da obrigação normativa à evidência verificável"

Status: **proposta para aprovação**. Nenhuma geração foi feita nesta etapa. Duração-alvo: 60 s, 16:9.

## 1. Como o filme se diferencia do percurso das sete estações
| Percurso interativo | Filme |
|---|---|
| Explica o **mecanismo**, estação por estação, em 3D | Conta a **contribuição**: o problema, a norma tornada verificável, a avaliação independente e o julgamento humano |
| Objetos e ambientes esquemáticos | Ambientes institucionais fotográficos, ações concretas de mãos, papéis e pessoas |
| Sete etapas em sequência | Seis movimentos de montagem, sem correspondência 1:1 com as estações |
| Texto e dados dentro da cena 3D | Texto e métricas só na edição, em tipografia real |

## 2. Estrutura de tomadas
Poucas tomadas longas, uma por movimento (mais o piloto aprovado como abertura).

| Mov. | Tempo | Tomada | Geração |
|---|---|---|---|
| 1 | 0–6 s | `T1` piloto aprovado (5 s) + 1 s de entrada | Já existe (`piloto/piloto_v01_seedance25_5s_720p.mp4`) |
| 2 | 6–16 s | `T2` 10 s | Nova |
| 3 | 16–28 s | `T3` 12 s | Nova |
| 4 | 28–38 s | `T4` 10 s | Nova |
| 5 | 38–48 s | `T5` 10 s | Nova |
| 6 | 48–60 s | `T6` 12 s | Nova |

Total: 5 tomadas novas (54 s de vídeo gerado) mais o piloto. O piloto nunca é repetido, só reaproveitado.

## 3. Narração proposta (PT-BR, ~108 palavras)
| Mov. | Narração |
|---|---|
| 1 | "Auditar a transparência pública é encontrar evidências que possam ser examinadas." |
| 2 | "A obrigação normativa se traduz em requisitos objetivos e rastreáveis: dez itens, de dois critérios, verificados a cada execução." |
| 3 | "Os mesmos critérios foram aplicados a quatro instituições, CNJ, STF, TJDFT e TST: dez execuções em cada uma, quarenta ao todo." |
| 4 | "A inteligência artificial generativa localiza e organiza as evidências por requisito. Ela não decide se a obrigação foi cumprida." |
| 5 | "Um gabarito independente, revisado por três especialistas do TJDFT, é confrontado com as evidências por uma rotina determinística." |
| 6 | "Evidência sem correspondência direta não é, por isso, falsa. A IA apoia a análise. A evidência precisa ser rastreável. O julgamento permanece humano." |

Mensagem final alternativa (mais forte, mesmo sentido): **"A IA localiza. O método compara. A pessoa auditora decide."**

## 4. Movimentos

### Movimento 1 — O problema da auditoria | 0–6 s | `T1`
- **Ação:** o piloto aprovado: mãos alinham e viram relatórios impressos; luz lateral de janela.
- **Pós:** fade de entrada, título discreto ao final do movimento.
- **Geração:** nenhuma nova.

### Movimento 2 — A norma se torna verificável | 6–16 s | `T2` (10 s)
- **Plano:** plano detalhe de mesa, câmera à altura do tampo, ligeiramente à esquerda.
- **Ação:** uma pessoa marca com lápis e fixa pequenas abas adesivas em uma folha impressa, uma após a outra, até somar dez abas, quatro de uma cor e seis de outra.
- **Câmera:** dolly lateral lento, foco acompanhando a mão.
- **Pós:** texto da folha ficará **ilegível** na geração. Numeração 1–10, nomes dos critérios IN84-27-CAPUT (4) e PNTP-12.1-12.2-SIC (6) e, se houver fonte oficial verificada, trechos verbatim, entram na edição.
- **Prompt rascunho (não executado):** *Documentary close shot of an auditor's hands on a wooden desk, placing ten small adhesive tabs, four teal and six indigo, along the edge of a printed page, marking lines with a pencil. Slow lateral dolly, soft window side light, shallow depth of field, realistic paper and hand motion, page text unreadable, no logos, no readable text, no screens with legible content.*

### Movimento 3 — A investigação documental | 16–28 s | `T3` (12 s)
- **Plano:** plano médio por cima do ombro, sem rosto, de uma pessoa diante de um notebook em escritório institucional; tela vista em ângulo, fora de foco e **sem conteúdo legível**.
- **Ação:** a pessoa percorre páginas, apoia-se em documentos impressos ao lado e reúne folhas em uma pilha.
- **Câmera:** dolly curto e leve câmera na mão.
- **Pós:** quatro rótulos CNJ, STF, TJDFT, TST e contador "10 execuções por instituição / 40 no total" em tipografia real.
- **Observação:** não simular acesso real a portais; sem capturas fictícias.

### Movimento 4 — A evidência é organizada | 28–38 s | `T4` (10 s)
- **Plano:** plano fechado de bancada com duas pastas de cores distintas, correspondentes aos dois critérios.
- **Ação:** mãos distribuem folhas impressas entre as pastas, conferindo cada uma contra uma lista.
- **Câmera:** travelling suave de altura constante.
- **Pós:** etiquetas das pastas e o nome do modelo (`openai/gpt-4.1`) em legenda técnica.
- **Leitura:** a IA aparece só pelo efeito (documentos reunidos), nunca como figura que decide.

### Movimento 5 — Comparação independente | 38–48 s | `T5` (10 s)
- **Plano:** mesa larga, dois conjuntos documentais separados: à esquerda as evidências reportadas, à direita um volume encadernado (o gabarito).
- **Ação:** uma pessoa aproxima pares de folhas e os une com clipe; folhas sem par são colocadas em uma bandeja **neutra**, sem carimbo e sem tom vermelho.
- **Câmera:** panorâmica lenta de um conjunto ao outro, com foco acompanhando as mãos.
- **Pós:** nomes das três métricas (Recall_item, Cobertura_evidência, Precisão_evidência); valores só após a decisão D8.
- **Cuidado:** nenhuma folha "rejeitada" ou "negada"; bandeja rotulada na edição como "sem correspondência direta".

### Movimento 6 — A interpretação humana | 48–60 s | `T6` (12 s)
- **Plano:** plano médio de uma pessoa auditora, em ambiente institucional luminoso, luz natural.
- **Ação:** examina documentos e uma tela (conteúdo ilegível), faz uma anotação à mão, pausa e levanta o olhar.
- **Câmera:** aproximação lenta e deliberada; encerra em composição sóbria.
- **Pós:** frase final, título do trabalho, autoria e créditos em tipografia real.
- **Risco:** único plano com rosto; evitar aparência sintética. Preferir três quartos ou perfil, sem close frontal.

## 5. Princípios que valem para todas as tomadas
- Sem texto legível gerado; sem logotipos; sem hologramas; sem carimbos de aprovação ou rejeição.
- Ritmo documental: nenhum zoom sobre imagem estática.
- Mesma paleta neutra, mesma direção de luz (lateral, de janela à esquerda) para sustentar continuidade.

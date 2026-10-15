# Diagnóstico inicial — filme do framework de auditoria

Data da consulta: 2026-10-14 (consulta feita pelo MCP Kairogen, sem geração)

## 1. Diretório autorizado
`C:\Fabiana\Mestrado IDP\Storytelling de Dados\Trabalhos\Dashboard_PortalTransparencia\site-3d\producao-filme\`

- A sessão foi iniciada na raiz do projeto; o diretório foi trocado para a pasta acima por instrução da usuária ("cd site-3d\producao-filme").
- Pastas pré-existentes: `piloto/`, `referencias/`, `roteiro/` (vazias, exceto `referencias/`).
- Pastas criadas nesta etapa: `relatorios/`, `keyframes/`, `cenas/`, `audio/`, `final/`.
- Arquivos fora da pasta (não tocados): `..\..\cenas.log`, `..\keyframes\*.png`.

## 2. Conta e saldo
| Item | Valor |
|---|---|
| Plano | PRO, ativo, expira em 2026-11-14 |
| Saldo | 882 créditos (alocação do plano: 930) |
| Créditos já usados | 48 |
| Gerações totais | 8 (todas de imagem) |
| **Gerações de vídeo** | **0** |
| Valor do crédito | R$ 0,16 |
| Concorrência de vídeo | 3 (0 ativas) |

## 3. Cotações reais (`estimate_cost`, plano pro)
Modelo `seedance-2-5`, 5 s, 16:9, 720p:

| Turbo | Áudio | Créditos |
|---|---|---|
| ligado | desligado | **49** |
| ligado | ligado | 49 (cotação anterior) |
| desligado | desligado | 68 |

- O Turbo reduz o custo (49 contra 68) neste modelo.
- O áudio não alterou o preço com Turbo ligado.
- Sem taxas adicionais informadas (`breakdown: null`).

## 4. Modelo e modalidade
- Modelo: `seedance-2-5` (Seedance 2.5), durações 4–30 s, resoluções 480p/720p/1080p/4k.
- Modalidade do piloto: texto para vídeo (modo `base`). Sem imagem de referência.
- Parâmetros: 5 s, 16:9, 720p, Turbo ligado, `generate_audio=false`.

## 5. Falhas anteriores
- A conta registra **0 gerações de vídeo**, então as duas tentativas do piloto anterior não aparecem como geração de vídeo nem como consumo.
- Causa não verificável a partir dos dados disponíveis. Hipóteses (não confirmadas): falha antes do envio, falha fora da plataforma Kairogen, ou erro de parâmetro (chaves de imagem do `seedance-2-5` são `image`/`last_image`, não `first_frame`).
- Nenhum log de erro foi encontrado em `piloto/` nem em `cenas.log` (`erros: []`).

## 6. Referências visuais (`referencias/`)
| Arquivo | Leitura | Uso | Cuidado |
|---|---|---|---|
| 01-documentos.jpg | Mão com caneta e lupa sobre jornal; luz lateral quente, grão, foco raso, vinheta forte | Escala e luz lateral do Movimento 1 | Aparência de banco de imagens estilizado |
| 02-evidencias.jpg | Terno, pastas, lâmpada de mesa, noite na janela; contraste alto | Materialidade dos documentos | Carimbos legíveis ("CONFIDENTIAL", "EVIDENCE REVIEW") |
| 03-comparacao.jpg | Mesa dividida: lado claro "VERIFIED", lado escuro "DENIED" | Ideia de dois conjuntos | Dramatiza rejeição como falsidade; o roteiro proíbe isso |
| 04-auditoria-humana.jpg | Auditor de óculos, escritório amplo e luminoso, luz natural | Movimento 6, tom sóbrio | Rosto de aparência sintética |

Todas parecem geradas por IA e contêm texto em inglês. Servem só como direção de luz e materialidade. Não serão passadas ao modelo no piloto.

## 7. Decisão para o piloto
Prosseguir com uma tentativa única: `seedance-2-5`, 5 s, 16:9, 720p, Turbo ligado, áudio desligado, `expected_credits=49`.

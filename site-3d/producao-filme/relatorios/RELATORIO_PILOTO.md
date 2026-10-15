# Relatório do piloto v01

## 1. Diretório autorizado
`C:\Fabiana\Mestrado IDP\Storytelling de Dados\Trabalhos\Dashboard_PortalTransparencia\site-3d\producao-filme\`

## 2. Gravações fora da pasta
Nenhuma. Todos os arquivos desta etapa estão dentro do diretório acima. O destino do download foi validado por caminho absoluto antes da gravação. Nada foi alterado no site, em `site-3d/` fora da pasta, nem na raiz.

## 3. Saldo
| Momento | Créditos |
|---|---|
| Antes da geração | 882 |
| Depois | 833 |
| Diferença | 49 |

## 4. Modelo, parâmetros e custo
- Modelo: `seedance-2-5` (Seedance 2.5), texto para vídeo, sem referências.
- 5 s, 16:9, 720p, Turbo ligado, áudio desligado, `quantity=1`.
- Custo efetivo: **49 créditos** (cotado 49; `expected_credits=49`), cerca de R$ 7,84.
- Tentativas: **uma**. Nenhuma repetição foi feita.

## 5. Prompt exato
Ver `roteiro/PILOTO_v01.md`. Cópia:

```
Documentary-style cinematic close shot of a wooden office desk in a contemporary public institution. A pair of adult hands neatly squares a stack of printed reports, then turns one page and slides it aside. The camera slowly dollies forward with a slight lateral drift and subtle handheld motion, focus gently shifting from the paper stack to the hands. Soft natural side light from a window on the left, shallow depth of field, a closed laptop and a coffee cup softly out of focus in the background. Realistic paper physics, natural skin and hand motion, consistent objects across frames. Photographic, film-like color, no text visible on any page or screen, no logos, no holograms, no sci-fi elements.
```

## 6. Arquivo produzido
`piloto/piloto_v01_seedance25_5s_720p.mp4` — 1.600.880 bytes.
- Origem: galeria Kairogen, `generationId 6acfd7b1aa953c277211f44f`, criado 2026-10-14 19:33 UTC.

## 7. Incidente de transporte
A chamada `generate_video` com `wait_for_completion=true` perdeu a resposta ("transport dropped mid-call; response for tool generate_video was lost"). A geração, porém, foi concluída e cobrada no servidor. Foi recuperada pela galeria (somente leitura), sem nova geração. Conclusão: a perda de resposta não equivale a falha de geração. Isso é uma hipótese plausível para as falhas do piloto anterior, mas não está comprovada, pois a conta não tinha registro de vídeo antes desta tentativa.

## 8. Verificação técnica
| Verificação | Resultado |
|---|---|
| Arquivo existe e tem tamanho plausível | Sim |
| Cabeçalho MP4 válido (`ftyp`/`isom`) | Sim |
| Metadados da galeria: 5 s, 16:9, 720p | Sim |
| Duração e resolução medidas no arquivo | **Não verificado**: não há ffprobe/ffmpeg/OpenCV na máquina |
| Reprodução | **Não verificada por mim** |

## 9. Avaliação visual
**Não realizada.** Não consegui extrair quadros nem reproduzir o vídeo neste ambiente. Os critérios abaixo ficam pendentes de revisão humana:

| Critério | Estado |
|---|---|
| Vídeo válido e reproduzível | Parcial (cabeçalho válido) |
| Movimento real ao longo do tempo | Pendente |
| Não é zoom/pan sobre imagem estática | Pendente |
| Coerência de mãos, papéis e objetos | Pendente |
| Aparência de fotografia, não render 3D | Pendente |
| Sem texto falso legível | Pendente |
| Sem artefatos graves | Pendente |
| Custo conhecido e dentro do teto | **Aprovado** (49 ≤ 49) |

## 10. Limitações para a produção completa
- Sem ferramenta local de vídeo (ffmpeg) para inspeção, montagem, legendas e exportação. Necessário instalar ou usar outro meio.
- Narração e trilha ainda não definidas; áudio pelo Kairogen custa à parte (não cotado).
- Referências 02 e 03 contêm carimbos e dramatizam rejeição; não servem como direção de cena.
- Dados científicos (métricas) não foram conferidos nesta etapa.
- Sem saldo comprometido além dos 49 créditos; nenhuma outra geração autorizada.

## 11. Recomendação
1. Assistir ao `piloto_v01_seedance25_5s_720p.mp4` e preencher a seção 9.
2. Se aprovado: instalar ffmpeg e planejar poucas tomadas longas. A 5 s custa 49 créditos (9,8/s); 30 s custa 288 (9,6/s). Um filme de 60 s em tomadas Turbo ficaria em torno de 580 créditos, só vídeo, estimativa a confirmar com `estimate_cost`.
3. Se reprovado: não repetir com o mesmo prompt; ajustar o prompt e pedir nova autorização.

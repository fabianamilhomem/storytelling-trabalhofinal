# Plano de limpeza e organização do projeto para o GitHub

Status: **somente planejamento. Nada foi excluído, movido ou alterado.** Data: 2026-10-15.
Destino previsto: https://github.com/fabianamilhomem/storytelling-trabalhofinal (não enviado).

## 1. O que o site realmente carrega ao funcionar

Verificado em `index.html`, `site.css` e nos `.js`:

| Caminho (dentro de `site-3d/`) | Papel | Tamanho |
|---|---|---|
| `index.html` | página única | < 1 MB |
| `assets/css/site.css` | estilos | < 1 MB |
| `assets/js/*.js` (8 arquivos, incl. `dados.js`) | lógica, gráficos, cenas 3D e **todos os dados** | 0,1 MB |
| `assets/fonts/*.woff2` (5) | tipografia local | 0,2 MB |
| `assets/video/filme-framework-v4.mp4` | **filme exibido na Metodologia** | 75,2 MB |
| `assets/video/poster-filme-v4.jpg` | capa do filme | 0,1 MB |
| `vendor/three.min.js` e `LICENSE-three.txt` | biblioteca 3D | 0,6 MB |

**Nenhuma** referência do site aponta para fora de `site-3d/`. Total necessário para rodar: **~76 MB**.

### O filme
O site toca `assets/video/filme-framework-v4.mp4`, **não** `producao-filme/final/FILME_PREVIA_V4.mp4`. Os dois arquivos são **idênticos** (mesmo SHA-256, prefixo `51d561f3c8d67f6d`). Portanto:
- manter `assets/video/filme-framework-v4.mp4` é obrigatório;
- `producao-filme/final/FILME_PREVIA_V4.mp4` pode ficar como registro da produção, mas apagá-lo não quebra o site.

## 2. Classificação do que existe

### A. MANTER (necessário ao funcionamento)
- `site-3d/index.html`, `site-3d/assets/` (inteira), `site-3d/vendor/`.

### B. MANTER (necessário para reproduzir, testar e documentar)
- `site-3d/scripts/gerar_dados.py` e `dados/evidencia_lab.json`: gera `assets/js/dados.js`; o script lê `../dados/evidencia_lab.json` pela raiz do projeto.
- `site-3d/testes/*.py` (suítes e scripts de captura) e `testes/testar_filme_v4.py`.
- `site-3d/docs/*.md`, incluindo os relatórios e este plano.
- `fontes/dissertacao.txt`: fonte textual de onde saíram as definições e valores. Manter se o repositório for público, apenas se você autorizar a divulgação da dissertação.
- `site-3d/producao-filme/roteiro/` e `relatorios/`: documentam a produção do filme (6,2 MB).

### C. PODE EXCLUIR/ARQUIVAR SEM AFETAR O SITE (alto ganho)
| Item | Tamanho | Observação |
|---|---|---|
| `site-3d/producao-filme/final/_trabalho/` | **229 MB**, 2.051 arquivos | quadros e peças intermediárias da montagem |
| `site-3d/producao-filme/final/FILME_PREVIA_V1.mp4`, `V1_rev2`, `V2`, `V3` | ~187 MB | versões antigas do filme |
| `site-3d/testes/capturas/` | **148 MB**, 463 arquivos | imagens de teste; regeneráveis pelas suítes |
| `site-3d/keyframes/` | 30 MB | ilustrações antigas, não usadas pelo site |
| `site-3d/producao-filme/cenas/`, `piloto/`, `referencias/` | ~22 MB | clipes e referências da produção |
| `site-3d/docs/_backup_pre_filme_v4/` | 0,1 MB | backup de arquivos antigos |
| `site-3d/testes/_saida_filme_v4.txt`, `resultado_*.json/.md` | pequenos | resultados de execuções antigas (manter só os mais recentes se quiser evidência) |

### D. DASHBOARD ANTIGO E RESÍDUOS NA RAIZ (fora do projeto final)
| Item | Tamanho | Observação |
|---|---|---|
| `design-systems/` | **111 MB**, 236 arquivos | dashboard antigo "evidencia-lab" e backup |
| `testes/` (raiz) | 1,1 MB | suítes do dashboard antigo |
| `Telas_Modelos/` | 8 MB | imagens de modelos antigos |
| `dados/*.py`, `*.pre_paletas.*`, `template_index*.html`, `__pycache__/` | ~0,25 MB | construtor do dashboard antigo; **exceto** `evidencia_lab.json` |
| `cenas.log` | 11 bytes | log solto |
| `.claude/` | 6 arquivos | configuração da ferramenta, não pertence ao produto |

## 3. Riscos e dependências a respeitar
1. **`dados/evidencia_lab.json` deve ser mantido**: é a entrada de `gerar_dados.py` e é lido por `testar_site.py`. Mantê-lo na pasta `dados/` preserva os dois caminhos sem alterar código.
2. **Manifesto de integridade** (`docs/MANIFESTO_ORIGINAIS_sha256.txt`, 533 arquivos) lista `design-systems/`, `dados/`, `testes/` da raiz e `fontes/`. Se apagar esses itens, a verificação apontará "ausente". Registre isso: o manifesto deve ser arquivado ou regenerado depois.
3. **GitHub**: limite duro de 100 MB por arquivo (o filme tem 75 MB: aceito, com aviso acima de 50 MB). Repositório confortável abaixo de 1 GB; hoje `site-3d` tem 775 MB, quase tudo em C.
4. **GitHub Pages** precisa de `index.html` na raiz do repositório (ou em `/docs`). Hoje o site está em `site-3d/`. Duas formas: (a) enviar o **conteúdo** de `site-3d/` como raiz do repositório; ou (b) manter a pasta e configurar Pages para publicar a subpasta com um fluxo de publicação. A forma (a) é a mais simples.
5. **Licença e direitos**: `vendor/` traz a licença do three.js; fontes (Fraunces, Inter, IBM Plex Mono) são livres, mas convém incluir os avisos. O filme usa vozes e modelos de terceiros: confirme condições de uso antes de publicar.

## 4. Ordem recomendada (para executarmos com sua autorização)
1. **Cópia de segurança** de todo o projeto para fora da pasta (por exemplo `..\_ARQUIVO_Dashboard_PortalTransparencia_2026-10-15`). Só depois qualquer exclusão.
2. **Mover** (não apagar) os grupos C e D para uma pasta `_arquivo_fora_do_repositorio` fora do projeto.
3. **Rodar a suíte** dos três navegadores e abrir o site local para confirmar que o filme toca e que tudo funciona.
4. Criar `.gitignore` (capturas, `__pycache__`, arquivos temporários) e um `README.md` curto com título, como abrir o site, estrutura e créditos.
5. Só então inicializar o repositório e enviar para o GitHub, após sua confirmação.

## 5. Resultado esperado
- **Mínimo para rodar:** ~76 MB.
- **Com testes e documentação (sem capturas nem produção):** ~80 MB.
- **Com o material de produção do filme que vale guardar** (roteiro, relatórios, `FILME_PREVIA_V4.mp4`): ~160 MB.

# Auditoria normativa assistida por IA generativa — Storytelling de Dados

Trabalho final da disciplina **Storytelling de Dados** (Mestrado IDP), por Fabiana Milhomem.

Site narrativo em 3D que apresenta um framework declarativo de auditoria normativa assistida por IA generativa, aplicado à avaliação da conformidade da prestação de contas pública (Portal da Transparência) no Poder Judiciário brasileiro. Os resultados são **preliminares e descritivos**.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `site-3d/` | Site estático (HTML/CSS/JS + Three.js r147 local): abertura 3D, metodologia, resultados, 40 execuções e fontes |
| `site-3d/assets/` | CSS, JS, fontes e o filme-síntese (`video/filme-framework-v4.mp4`) |
| `site-3d/scripts/` | `gerar_dados.py` — gera `assets/js/dados.js` a partir de `dados/evidencia_lab.json` |
| `site-3d/testes/` | Testes automatizados (Chromium, Edge, Firefox) e capturas de tela |
| `site-3d/producao-filme/` | Roteiro, áudio, relatórios e versão final do filme |
| `site-3d/docs/` | Direção de arte, auditorias e relatórios de cada fase |
| `dados/` | `evidencia_lab.json` — evidências das 40 execuções (somente leitura) |
| `fontes/` | `dissertacao.txt` — texto-fonte |

## Como executar

Abra `site-3d/index.html` no navegador (funciona via `file://`), ou:

```bash
cd site-3d
python -m http.server
# http://localhost:8000
```

Regerar os dados e rodar os testes:

```bash
python -I -X utf8 site-3d/scripts/gerar_dados.py
python -I -X utf8 site-3d/testes/testar_site.py chromium   # ou edge | firefox
```

## Publicação (GitHub Pages)

O site usa caminhos relativos e é compatível com GitHub Pages: publique o conteúdo de `site-3d/` na raiz ou em `/docs` do repositório.

## Limitações

- GitHub Pages ainda não foi testado; a execução local foi validada via `file://`.
- Desempenho em GPU real não medido (testes usam WebGL por software).
- A metodologia 3D usa formas abstratas e não reproduz portais oficiais.

Detalhes em `site-3d/docs/`.

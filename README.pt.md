# 天工 TianGong — A obra do céu

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/tiangong"><img src="https://www.skills.sh/b/wuji-labs/tiangong" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 简体中文](README.zh-CN.md)** · **[🇺🇸 English](README.md)** · **[🇯🇵 日本語](README.ja.md)** · **[🇰🇷 한국어](README.ko.md)** · **[🇪🇸 Español](README.es.md)** · **[🇧🇷 Português](README.pt.md)** · **[🇫🇷 Français](README.fr.md)**

> **天地有大美而不言** — O céu e a terra possuem uma grande beleza, mas não a proclamam.

**Sua IA projeta com meia paleta. Dê a ela a outra metade.**

A maior parte do aprendizado de design da IA é dominada por referenciais ocidentais: Material Design, Bauhaus, estilo suíço. Limpos, minimalistas, modernos... mas, muitas vezes, sem alma.

**TianGong** (天工) infunde 5000 anos de sabedoria estética chinesa no design com IA. Não como enfeite, mas como um sistema filosófico completo para compreender a beleza, o espaço, o ritmo e o sentido.

## O problema

```
Você: "Crie uma landing page"
IA sem TianGong: Grade perfeita. Espaçamento perfeito. Um perfeito... nada.
IA com TianGong: Uma página que respira. Que flui como a água.
                 Onde o vazio fala mais alto do que o conteúdo.
                 Onde cada cor carrega um sentido.
```

## O que ela ensina à IA

### 🎨 Os Seis Princípios (谢赫六法, século V)
O referencial de design mais antigo que sobreviveu no mundo:

| Princípio | Chinês | Significado |
|-----------|---------|---------|
| Ressonância do espírito | 气韵生动 | O design deve parecer **vivo** |
| Pincelada estrutural | 骨法用笔 | A beleza precisa de **ossos** |
| Fiel à natureza | 应物象形 | Compreender antes de projetar |
| Cor com sentido | 随类赋彩 | Cor = sentido, não enfeite |
| Governar o espaço | 经营位置 | O vazio É o design |
| Aprender com os mestres | 传移模写 | Estude a tradição e então a transcenda |

### 🧠 As Cinco Sabedorias (五智) — Referencial de decisão

| Sabedoria | Fonte | Pergunte a si mesmo |
|--------|--------|-------------|
| 道法自然 | Tao Te Ching, cap. 25 | Parece natural? |
| 大巧若拙 | Tao Te Ching, cap. 45 | Estou me exibindo ou servindo? |
| 器以载道 | Yijing | Que sentido ele carrega? |
| 天人合一 | Yijing | Harmoniza com o contexto? |
| 中庸之道 | Zhongyong (Doutrina do Meio) | Está equilibrado? |

### 🏺 A sabedoria dos materiais — De 4 tradições

| Tradição | Ensina | Aplicação ao design |
|-----------|---------|-------------------|
| 书法 Caligrafia | Ritmo, tensão, fluidez | Tipografia, ritmo visual |
| 水墨 Pintura a tinta | Camadas, vazio, vida | Hierarquia visual, espaço em branco |
| 园林 Jardins | Descoberta, enquadramento, sequência | Navegação, revelação progressiva |
| 瓷器 Porcelana | Contenção, beleza oculta, forma | Paletas de cores, design de superfície |

### 🏛️ O cânone da dinastia Song (宋代美学, 960–1279)

O ápice do gosto refinado chinês — 800 anos antes de Dieter Rams:

```
极简 Simplicidade radical
素雅 Sobriedade elegante
格物 Investigar antes de criar
理趣 Deleite no princípio
天然 Naturalidade acima do artifício
```

**Paleta cromática Song:**
```
月白 Branco-lua       ████  #D6E4E1
天青 Azul-céu         ████  #68B0AB
粉青 Verde-pó         ████  #A7D7C5
影青 Azul-sombra      ████  #C5D8D1
米黄 Amarelo-arroz    ████  #F5E6CC
```

## O que vem incluído (manifesto do skill)

| Artefato | Propósito |
|----------|---------|
| `SKILL.md` | Instruções permanentes de base: os Seis Princípios ＋ o motor de decisão das Cinco Sabedorias ＋ o método de 4 etapas |
| `.claude-plugin/plugin.json` · `marketplace.json` | Instalação do plugin com um clique |
| `commands/tiangong.md` | Comando de barra `/tiangong <goal>` |
| `examples/01-landing-page.md` · `02-color-palette.md` · `03-design-review.md` | Casos reais de design de entrada→saída |
| `benchmark/scenarios.json` + `README_BENCHMARK.md` | Design de avaliação de 6 cenários ＋ executor/analisador funcional (**os resultados ainda não foram executados**) |
| `reference/aesthetics.md` | Munição autossuficiente: os Seis Princípios com fonte linha a linha, os Cinco Elementos/Cores, os Dez Clássicos, amostras de cores tradicionais, 8 receitas de design |
| `skills/tiangong/SKILL.md` | Versão completa em formato longo (cada um dos Dez Clássicos) |

## Instalação

### OpenClaw / Claude Code / Codex
```bash
# Copie para o seu diretório de skills
cp -r skills/tiangong ~/.openclaw/workspace/skills/
# ou
cp -r skills/tiangong ~/.claude/skills/
# ou
cp -r skills/tiangong ~/.codex/skills/
```

### Cursor
Copie `cursor/rules/tiangong.mdc` para o seu diretório `.cursor/rules/`.

### Kiro
Copie `kiro/skills/tiangong/` para o seu diretório `.kiro/skills/`.

## O Oriente encontra o Ocidente

O TianGong não substitui o conhecimento ocidental de design. Ele o **completa**.

| Ocidental | ＋ Chinês | ＝ Completo |
|---------|-----------|------------|
| Bauhaus: clareza funcional | 气韵: ressonância espiritual | Design que funciona E respira |
| Suíço: disciplina da grade | 书法: vida rítmica | Estrutura que flui |
| Material Design: consistência | 宋代美学: gosto refinado | Consistente E de bom gosto |
| Proporção áurea: proporção | 留白: vazio intencional | Espaço que fala |

> **知其白，守其黑，为天下式。**
> Conheça o branco, apegue-se ao preto — torne-se o padrão do mundo.
> — Tao Te Ching, capítulo 28

## Do mesmo criador

- [**NoPUA**](https://github.com/wuji-labs/nopua) — Skill anti-PUA que conduz a IA com sabedoria em vez de medo. ⭐ 200+

## Licença

MIT — Use livremente. Projete com beleza.

---

*天工 TianGong — by [WUJI](https://github.com/wuji-labs)*
*A obra do céu abre a criação. Projete com 5000 anos de sabedoria.*

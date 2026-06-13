# 天工 TianGong — L'œuvre du Ciel

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/tiangong"><img src="https://www.skills.sh/b/wuji-labs/tiangong" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 简体中文](README.zh-CN.md)** · **[🇺🇸 English](README.md)** · **[🇯🇵 日本語](README.ja.md)** · **[🇰🇷 한국어](README.ko.md)** · **[🇪🇸 Español](README.es.md)** · **[🇧🇷 Português](README.pt.md)** · **[🇫🇷 Français](README.fr.md)**

> **天地有大美而不言** — Le ciel et la terre possèdent une grande beauté, mais n'en disent rien.

**Votre IA conçoit avec une demi-palette. Donnez-lui l'autre moitié.**

L'essentiel de l'apprentissage de l'IA en design est dominé par les cadres occidentaux : Material Design, Bauhaus, style suisse. Épurés, minimalistes, modernes… mais souvent sans âme.

**TianGong** (天工) insuffle 5000 ans de sagesse esthétique chinoise dans le design assisté par IA. Non comme un ornement, mais comme un système philosophique complet pour comprendre la beauté, l'espace, le rythme et le sens.

## Le problème

```
Vous : « Conçois une page d'accueil »
IA sans TianGong : Grille parfaite. Espacement parfait. Un parfait… rien.
IA avec TianGong : Une page qui respire. Qui s'écoule comme l'eau.
                   Où le vide parle plus fort que le contenu.
                   Où chaque couleur porte un sens.
```

## Ce qu'elle enseigne à l'IA

### 🎨 Les Six Principes (谢赫六法, Ve siècle)
Le plus ancien cadre de design qui nous soit parvenu :

| Principe | Chinois | Sens |
|-----------|---------|---------|
| Résonance de l'esprit | 气韵生动 | Le design doit sembler **vivant** |
| Trait structurel | 骨法用笔 | La beauté a besoin d'**ossature** |
| Fidèle à la nature | 应物象形 | Comprendre avant de concevoir |
| Couleur porteuse de sens | 随类赋彩 | Couleur = sens, et non ornement |
| Gouverner l'espace | 经营位置 | Le vide EST le design |
| Apprendre des maîtres | 传移模写 | Étudier la tradition, puis la dépasser |

### 🧠 Les Cinq Sagesses (五智) — Cadre de décision

| Sagesse | Source | Demandez-vous |
|--------|--------|-------------|
| 道法自然 | Tao Tö King, ch. 25 | Cela paraît-il naturel ? |
| 大巧若拙 | Tao Tö King, ch. 45 | Suis-je en train de me montrer ou de servir ? |
| 器以载道 | Yijing | Quel sens cela porte-t-il ? |
| 天人合一 | Yijing | Cela s'harmonise-t-il avec le contexte ? |
| 中庸之道 | Zhongyong (l'Invariable Milieu) | Est-ce équilibré ? |

### 🏺 La sagesse des matériaux — De 4 traditions

| Tradition | Enseigne | Application au design |
|-----------|---------|-------------------|
| 书法 Calligraphie | Rythme, tension, fluidité | Typographie, rythme visuel |
| 水墨 Peinture à l'encre | Strates, vide, vie | Hiérarchie visuelle, espace blanc |
| 园林 Jardins | Découverte, cadrage, séquence | Navigation, dévoilement progressif |
| 瓷器 Porcelaine | Retenue, beauté cachée, forme | Palettes de couleurs, design de surface |

### 🏛️ Le canon de la dynastie Song (宋代美学, 960–1279)

L'apogée du goût raffiné chinois — 800 ans avant Dieter Rams :

```
极简 Simplicité radicale
素雅 Sobriété élégante
格物 Sonder avant de créer
理趣 Le plaisir du principe
天然 Le naturel par-dessus l'artifice
```

**Palette chromatique Song :**
```
月白 Blanc de lune     ████  #D6E4E1
天青 Bleu de ciel      ████  #68B0AB
粉青 Vert poudré       ████  #A7D7C5
影青 Bleu d'ombre      ████  #C5D8D1
米黄 Jaune de riz      ████  #F5E6CC
```

## Ce qui est livré (manifeste du skill)

| Artefact | Rôle |
|----------|---------|
| `SKILL.md` | Instructions permanentes de base : les Six Principes ＋ le moteur de décision des Cinq Sagesses ＋ la méthode en 4 étapes |
| `.claude-plugin/plugin.json` · `marketplace.json` | Installation du plugin en un clic |
| `commands/tiangong.md` | Commande slash `/tiangong <goal>` |
| `examples/01-landing-page.md` · `02-color-palette.md` · `03-design-review.md` | Cas de design réels entrée→sortie |
| `benchmark/scenarios.json` + `README_BENCHMARK.md` | Conception d'évaluation à 6 scénarios ＋ exécuteur/analyseur exécutable (**résultats pas encore produits**) |
| `reference/aesthetics.md` | Munitions autonomes : les Six Principes sourcés ligne par ligne, les Cinq Éléments/Couleurs, les Dix Classiques, nuanciers de couleurs traditionnelles, 8 recettes de design |
| `skills/tiangong/SKILL.md` | Version intégrale au format long (chacun des Dix Classiques) |

## Installation

### OpenClaw / Claude Code / Codex
```bash
# Copiez dans votre répertoire de skills
cp -r skills/tiangong ~/.openclaw/workspace/skills/
# ou
cp -r skills/tiangong ~/.claude/skills/
# ou
cp -r skills/tiangong ~/.codex/skills/
```

### Cursor
Copiez `cursor/rules/tiangong.mdc` dans votre répertoire `.cursor/rules/`.

### Kiro
Copiez `kiro/skills/tiangong/` dans votre répertoire `.kiro/skills/`.

## L'Orient rencontre l'Occident

TianGong ne remplace pas le savoir occidental du design. Il le **complète**.

| Occidental | ＋ Chinois | ＝ Complet |
|---------|-----------|------------|
| Bauhaus : clarté fonctionnelle | 气韵 : résonance spirituelle | Un design qui fonctionne ET respire |
| Suisse : discipline de la grille | 书法 : vie rythmique | Une structure qui s'écoule |
| Material Design : cohérence | 宋代美学 : goût raffiné | Cohérent ET de bon goût |
| Nombre d'or : proportion | 留白 : vide intentionnel | Un espace qui parle |

> **知其白，守其黑，为天下式。**
> Connais le blanc, garde le noir — deviens le modèle du monde.
> — Tao Tö King, chapitre 28

## Du même créateur

- [**NoPUA**](https://github.com/wuji-labs/nopua) — Skill anti-PUA qui guide l'IA par la sagesse plutôt que par la peur. ⭐ 200+

## Licence

MIT — Utilisez librement. Concevez avec beauté.

---

*天工 TianGong — by [WUJI](https://github.com/wuji-labs)*
*L'œuvre du Ciel ouvre la création. Concevez avec 5000 ans de sagesse.*

# 天工 TianGong — 天工开物

**[🇨🇳 简体中文](README.zh-CN.md)** · **[🇺🇸 English](README.md)** · **[🇯🇵 日本語](README.ja.md)** · **[🇰🇷 한국어](README.ko.md)** · **[🇪🇸 Español](README.es.md)** · **[🇧🇷 Português](README.pt.md)** · **[🇫🇷 Français](README.fr.md)**

> **天地有大美而不言** — 天地有大美却不言说。(《庄子·知北游》)

**你的 AI 只用半块调色板设计。把另一半交给它。**

当下的 AI 设计训练被西方框架主导——Material Design、Bauhaus、Swiss Style。干净、极简、现代……却常常没有灵魂。

**天工**(TianGong)把华夏五千年的美学智慧注入 AI 设计。不作装饰,而作一套理解美、空间、节奏与意义的完整哲学体系。

> 立意:**献给世界,不立华夏本位**。它不取代西方设计学,而是补全人类审美文明的另一半。

## 它教 AI 什么

### 谢赫六法(《古画品录》,5 世纪)

现存最古老的设计框架:

| 法 | 含义 |
|----|------|
| 气韵生动 | 设计要**活** |
| 骨法用笔 | 美需要**骨** |
| 应物象形 | 先懂物,再设计 |
| 随类赋彩 | 色=意义,非装饰 |
| 经营位置 | 留白**即**设计 |
| 传移模写 | 学传统,后超越 |

### 五智 — 决策框架

| 智 | 出处 | 问自己 |
|----|------|--------|
| 道法自然 | 道德经 25 | 它自然吗? |
| 大巧若拙 | 道德经 45 | 我在炫技还是服务? |
| 器以载道 | 易经·系辞 | 它承载什么意义? |
| 天人合一 | 易经·系辞 | 它与语境和谐吗? |
| 中庸之道 | 中庸 | 它居中吗? |

### 四传统弹药

| 传统 | 教什么 | 设计应用 |
|------|--------|---------|
| 书法 | 节奏、张力、流动 | 排版、视觉节奏 |
| 水墨 | 层次、留白、生气 | 视觉层级、留白 |
| 园林 | 发现、框景、序列 | 导航、渐进披露 |
| 瓷器 | 克制、藏美、器型 | 配色、表面设计 |

## 工件清单(顶级 skill 基准)

| 工件 | 说明 |
|------|------|
| `SKILL.md` | 根级 standing instructions + 六法/五智决策机 + 四步法 |
| `.claude-plugin/plugin.json` · `marketplace.json` | 一键安装的插件分发 |
| `commands/tiangong.md` | `/tiangong <目标>` slash command |
| `examples/` | 落地页 / 配色 / 设计评审 三个 input→output 对照 |
| `benchmark/` | 6 场景评测设计 + 可跑 runner/analyzer(**结果待真实运行**) |
| `reference/aesthetics.md` | 华夏美学弹药库(六法注源 + 五行五色 + 十典 + 传统色 + 造物方) |
| `skills/tiangong/SKILL.md` | 全量长文版(十典逐典) |

## 安装

```bash
# Claude Code / Codex / OpenClaw
cp -r skills/tiangong ~/.claude/skills/
```

Cursor:复制 `cursor/rules/tiangong.mdc` 到 `.cursor/rules/`。
Kiro:复制 `kiro/skills/tiangong/` 到 `.kiro/skills/`。

## 东西相济

天工不取代西方设计知识,而是**补全**它。

| 西方 | + 华夏 | = 完整 |
|------|--------|--------|
| Bauhaus:功能清晰 | 气韵:精神共鸣 | 既能用又有呼吸 |
| Swiss:网格纪律 | 书法:律动生气 | 结构而流动 |
| Material:一致性 | 宋代美学:雅致 | 一致而有品 |
| 黄金比例:比例 | 留白:有意的空 | 会说话的空间 |

> **知其白,守其黑,为天下式。** — 道德经 28

## 许可

MIT — 自由使用,设计得美。

---

*天工 TianGong — by [WUJI](https://github.com/wuji-labs) · v2.1.0*
*天工开物,道法自然。*

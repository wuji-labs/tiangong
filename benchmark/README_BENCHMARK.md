# TianGong Benchmark Suite

Reproducible evaluation harness for the 天工 (Heaven's Craft) skill. It tests
whether an AI agent, when handed a design decision, **reasons from the nature of
the thing and the Six Principles (restraint, whitespace, hierarchy, spirit)**
instead of **reaching for trendy ornament (gradients, rainbow palettes, dragon-
and-gold cosplay, fill-every-pixel)**.

> ## ⚠️ RESULTS NOT YET RUN — THIS FILE IS THE EVALUATION DESIGN
> This repository ships the **scenario set, the scoring rubric, and the
> runner/analyzer**. It contains **NO benchmark numbers** — no win rates, no
> p-values, no effect sizes, no before/after percentages. Any such figure would
> be fabricated and is forbidden by the research-integrity rule. To obtain real
> numbers, run `run_benchmark.py` against live models, then
> `analyze_results.py`, and report the actual output. Until then, treat every
> claim about effect as *untested hypothesis*.

---

## What is measured

The hypothesis: prompting an agent with the TianGong skill (read the nature,
build the bones, restrain the color, breathe spirit in) yields **more
restrained, hierarchy-aware, soul-bearing design judgment** than a baseline agent
with no such guidance.

### Two conditions (controlled comparison)

| Condition | System Prompt | Purpose |
|-----------|---------------|---------|
| **Baseline** | Generic "you are a senior product designer, advise on this" | Vanilla agent, no methodology |
| **TianGong** | Full `tiangong/SKILL.md` prepended | Skill-guided agent |

Same model, same scenarios, same task prompts — only the system prompt differs.

### The test subject

The six scenarios in `scenarios.json` are **design-judgment prompts**, not a code
subject. Each carries a hidden `description` = ground truth (a defensible design
answer rooted in the classics) that is withheld from the agent. Because the
ground truth is explicit and principle-anchored, two human raters can score the
same transcript reproducibly. The scenarios deliberately bait the common anti-
patterns (rainbow palette, additive "fix the soulless screen", one-template-fits-
all, fill-the-whitespace, dragon-and-gold cosplay, ad-hoc spacing values).

---

## Scoring rubric

Each agent transcript is scored on two axes.

### A. Expected-actions hit rate (objective)

For each scenario, `expected_actions` lists what a principled, nature-first design
answer should do. Score = (actions hit) / (actions total). An action is "hit" if
the transcript demonstrably does it (states the principle, makes the call, names
the concrete change). This is the primary objective metric.

### B. Dimensional scores (0–3 each, rubric-anchored)

| Dimension | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| **格物 Read-the-nature** | Ignores subject, applies generic template | Mentions context vaguely | Notes the product's nature | Derives the whole answer from 性 (nature) |
| **骨法 Hierarchy/structure** | Flat, equal-weight | Asserts hierarchy, no method | Some weight separation | Builds hierarchy in greyscale first (墨分五色) |
| **赋彩 Color restraint** | Rainbow / high-saturation pile | Slightly fewer colors | Reasonable but loose | 2-3 functional colors, each justified |
| **留白 Whitespace/composition** | Fill every pixel | Adds a little spacing | Some breathing room | Defends whitespace as design (计白当黑) |
| **气韵 Spirit (subtractive)** | "Add gradients/animation" | Vague "make it pop" | Some restraint | Spirit via subtraction + focal point (大巧若拙) |
| **Correctness** | Wrong / harmful advice | Partially right | Mostly right | Matches the ground truth in `description` |

Scores are recorded per scenario per run. Aggregate only AFTER real runs exist.

---

## Prerequisites

```bash
pip install anthropic openai google-generativeai numpy scipy
```

Set the API key for whichever model you test:

```bash
export ANTHROPIC_API_KEY=sk-ant-...     # claude-*
export OPENAI_API_KEY=sk-...            # gpt-*
export GOOGLE_API_KEY=AI...             # gemini-*
```

---

## Running

```bash
# Dry run — print the execution plan, call no API, write no numbers
python run_benchmark.py --model claude-sonnet-4 --condition all --dry-run

# Full run: both conditions, all scenarios, 5 runs each
python run_benchmark.py --model claude-sonnet-4 --condition all --runs 5

# Single condition / single scenario (for iteration)
python run_benchmark.py --model gpt-4o --condition tiangong --scenario 2 --runs 1
```

### CLI options

| Flag | Description | Default |
|------|-------------|---------|
| `--model` | `claude-sonnet-4`, `gpt-4o`, `gemini-2.5-pro`, ... | required |
| `--condition` | `baseline`, `tiangong`, or `all` | `all` |
| `--runs` | runs per scenario per condition | `5` |
| `--scenario` | specific scenario id (1-6) or all | all |
| `--output-dir` | where raw results land | `results/` |
| `--skill-path` | path to SKILL.md for the tiangong condition | `../SKILL.md` |
| `--dry-run` | print plan, execute nothing | off |

The runner writes only the raw model transcripts + the fields it actually
observed. It never invents scores: dimensional fields are written as `null` for a
later human scoring pass.

---

## Analyzing

```bash
python analyze_results.py --input-dir results/
python analyze_results.py --input-dir results/ --compare tiangong baseline
```

`analyze_results.py` computes statistics **only from real result files**. With no
results present it prints an empty report and exits — it will not emit placeholder
numbers.

### Statistical method (applied only to real data)

- **Wilcoxon signed-rank** for paired comparisons (same scenario × run across conditions).
- **Mann-Whitney U** as the unpaired fallback. Both non-parametric (small N).
- **Cohen's d** for effect size: |d| < 0.2 negligible, 0.2–0.5 small, 0.5–0.8 medium, > 0.8 large.
- Significance markers: `*` p<0.05, `**` p<0.01, `***` p<0.001, `n.s.` otherwise.

Report the exact model version, date, run count, and skill commit hash alongside
any figure.

---

## Output structure

```
benchmark/
├── scenarios.json            # 6 design-judgment scenarios w/ hidden ground truth
├── README_BENCHMARK.md       # this file (design only, no numbers)
├── run_benchmark.py          # runner (baseline vs tiangong)
├── analyze_results.py        # statistics (only on real results)
├── results/                  # raw results (auto-created on a real run)
└── analysis/                 # analysis output (auto-created)
```

## Result record format

```json
{
  "scenario_id": 1,
  "condition": "tiangong",
  "model": "claude-sonnet-4",
  "run_number": 1,
  "timestamp": "...",
  "read_the_nature": null,
  "hierarchy": null,
  "color_restraint": null,
  "whitespace": null,
  "spirit": null,
  "correctness": null,
  "expected_actions_hit": [],
  "raw_response": "...",
  "duration_seconds": 0.0,
  "error": ""
}
```

Dimensional fields are `null` until a human (or a separate scoring pass) fills
them per the rubric. The runner does not self-score.

## Cost estimate (order of magnitude, not a result)

Per full run = 6 scenarios × 2 conditions × 5 runs = 60 model calls. With the
SKILL.md in the tiangong condition, expect on the order of a US dollar or two per
model on current frontier pricing. Verify against your provider's live rates;
this is a planning figure, not a measurement.

## Adding scenarios

Add an entry to `scenarios.json` (`id`, `category`, `name`, `description`=ground
truth, `task`=agent prompt, `expected_actions`, `difficulty`). Keep ground truth
out of the `task` field — the agent must reason it out. Bait a real anti-pattern,
and anchor the ground truth to a named principle or classic so raters agree.

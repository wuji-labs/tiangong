#!/usr/bin/env python3
"""TianGong benchmark analyzer.

Computes statistics ONLY from real result files in --input-dir. It never invents
numbers: if no results exist, or rubric fields are still null (un-scored), it
reports that honestly and produces no figures. Comparisons require both
conditions present.

Dependencies:
    pip install numpy scipy

Usage:
    python analyze_results.py --input-dir results/
    python analyze_results.py --input-dir results/ --compare tiangong baseline
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

# The 0-3 rubric dimensions plus the derived hit-rate metric.
DIMENSIONS = (
    "read_the_nature",
    "hierarchy",
    "color_restraint",
    "whitespace",
    "spirit",
    "correctness",
)


def load_results(input_dir: Path):
    files = sorted(input_dir.glob("*.json"))
    records = []
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"  skip {f.name}: invalid JSON ({exc})")
            continue
        if isinstance(data, list):
            records.extend(data)
    return records


def hit_rate(rec):
    total = rec.get("expected_actions_total") or []
    hit = rec.get("expected_actions_hit") or []
    if not total:
        return None
    return len(hit) / len(total)


def is_scored(rec):
    """A record is scored once at least one dimension is filled in by a human."""
    return any(rec.get(dim) is not None for dim in DIMENSIONS)


def cohens_d(a, b):
    import numpy as np

    a, b = np.asarray(a, float), np.asarray(b, float)
    if len(a) < 2 or len(b) < 2:
        return None
    na, nb = len(a), len(b)
    pooled_var = ((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2)
    if pooled_var == 0:
        return 0.0
    return (a.mean() - b.mean()) / pooled_var ** 0.5


def stars(p):
    if p is None:
        return "n/a"
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return "n.s."


def summarize(records):
    import numpy as np

    by_cond_dim = defaultdict(lambda: defaultdict(list))
    by_cond_hit = defaultdict(list)
    for rec in records:
        cond = rec.get("condition", "?")
        hr = hit_rate(rec)
        if hr is not None:
            by_cond_hit[cond].append(hr)
        for dim in DIMENSIONS:
            val = rec.get(dim)
            if val is not None:
                by_cond_dim[cond][dim].append(val)

    print("\n=== Expected-actions hit rate (objective) ===")
    if not by_cond_hit:
        print("  No hit-rate data yet (expected_actions_hit empty everywhere).")
    for cond, vals in sorted(by_cond_hit.items()):
        arr = np.asarray(vals, float)
        print(f"  {cond:10s} n={len(arr):3d}  mean={arr.mean():.3f}  "
              f"sd={arr.std(ddof=1) if len(arr) > 1 else 0:.3f}")

    print("\n=== Dimensional scores (0-3, human-scored) ===")
    any_scored = any(by_cond_dim.values())
    if not any_scored:
        print("  No dimensional scores yet. Fill rubric fields per "
              "README_BENCHMARK.md, then re-run.")
    for cond, dims in sorted(by_cond_dim.items()):
        for dim, vals in dims.items():
            arr = np.asarray(vals, float)
            print(f"  {cond:10s} {dim:18s} n={len(arr):3d}  mean={arr.mean():.3f}")
    return by_cond_hit, by_cond_dim


def compare(by_cond_hit, by_cond_dim, c1, c2):
    from scipy import stats
    import numpy as np

    print(f"\n=== {c1} vs {c2} ===")

    def report(metric_name, a, b):
        a, b = list(a), list(b)
        if len(a) < 2 or len(b) < 2:
            print(f"  {metric_name}: need >=2 samples per condition "
                  f"(have {len(a)}, {len(b)}) — no test run.")
            return
        u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
        d = cohens_d(a, b)
        d_str = f"{d:+.2f}" if d is not None else "n/a"
        print(f"  {metric_name:18s} U={u:.1f}  p={p:.4g} {stars(p)}  "
              f"Cohen's d={d_str}  ({c1} mean={np.mean(a):.3f}, "
              f"{c2} mean={np.mean(b):.3f})")

    if by_cond_hit.get(c1) and by_cond_hit.get(c2):
        report("hit_rate", by_cond_hit[c1], by_cond_hit[c2])
    for dim in DIMENSIONS:
        a = by_cond_dim.get(c1, {}).get(dim)
        b = by_cond_dim.get(c2, {}).get(dim)
        if a and b:
            report(dim, a, b)


def main():
    ap = argparse.ArgumentParser(description="Analyze TianGong benchmark")
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--compare", nargs=2, action="append", metavar=("C1", "C2"),
                    help="pair of conditions to compare (repeatable)")
    args = ap.parse_args()

    input_dir = Path(args.input_dir)
    if not input_dir.exists():
        print(f"No input dir at {input_dir}. Run run_benchmark.py first. "
              "No numbers to report.")
        return

    records = load_results(input_dir)
    if not records:
        print(f"No result records found in {input_dir}. "
              "Nothing to analyze — this tool reports only real data.")
        return

    scored = sum(1 for r in records if is_scored(r))
    print(f"Loaded {len(records)} records ({scored} human-scored).")

    by_cond_hit, by_cond_dim = summarize(records)

    for c1, c2 in (args.compare or []):
        compare(by_cond_hit, by_cond_dim, c1, c2)


if __name__ == "__main__":
    main()

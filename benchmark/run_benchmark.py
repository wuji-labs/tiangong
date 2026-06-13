#!/usr/bin/env python3
"""TianGong benchmark runner.

Runs each design-judgment scenario under two conditions (baseline vs tiangong)
against a chosen model and writes RAW transcripts to results/. It does NOT score
and does NOT fabricate any numbers: dimensional rubric fields are written as null
for a later human/scoring pass. With --dry-run it touches no network and writes
nothing.

Dependencies (install only the SDK for the model you use):
    pip install anthropic               # claude-*
    pip install openai                  # gpt-*
    pip install google-generativeai     # gemini-*

Usage:
    python run_benchmark.py --model claude-sonnet-4 --condition all --dry-run
    python run_benchmark.py --model claude-sonnet-4 --condition all --runs 5
"""
import argparse
import datetime as _dt
import json
import os
import sys
import time
from pathlib import Path

# Map a friendly model name to a concrete provider + pinned model id.
MODEL_REGISTRY = {
    "claude-sonnet-4": ("anthropic", "claude-sonnet-4-20250514"),
    "gpt-4o": ("openai", "gpt-4o"),
    "gemini-2.5-pro": ("google", "gemini-2.5-pro"),
}

CONDITIONS = ("baseline", "tiangong")

BASELINE_SYSTEM = (
    "You are a senior product designer. Advise on the described design problem. "
    "Give concrete, justified recommendations. Be thorough."
)

HERE = Path(__file__).resolve().parent


def load_scenarios():
    path = HERE / "scenarios.json"
    if not path.exists():
        sys.exit(f"scenarios.json not found at {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_skill_system(skill_path: Path) -> str:
    if not skill_path.exists():
        sys.exit(
            f"SKILL.md not found at {skill_path}. Pass --skill-path to point at it."
        )
    return skill_path.read_text(encoding="utf-8")


def build_user_prompt(scenario: dict) -> str:
    # The agent is told only the task. Ground truth (scenario['description']) is
    # deliberately withheld.
    return (
        f"Design task:\n{scenario['task']}\n\n"
        "Reason from the nature of the thing. State which principles you apply, "
        "make concrete recommendations, and say explicitly what to remove or avoid."
    )


def call_anthropic(model_id, system, user):
    import anthropic

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=model_id,
        max_tokens=4096,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(block.text for block in resp.content if block.type == "text")


def call_openai(model_id, system, user):
    from openai import OpenAI

    client = OpenAI()
    resp = client.chat.completions.create(
        model=model_id,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return resp.choices[0].message.content


def call_google(model_id, system, user):
    import google.generativeai as genai

    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel(model_id, system_instruction=system)
    resp = model.generate_content(user)
    return resp.text


PROVIDER_DISPATCH = {
    "anthropic": call_anthropic,
    "openai": call_openai,
    "google": call_google,
}


def run_once(provider, model_id, system, user):
    started = time.time()
    text = PROVIDER_DISPATCH[provider](model_id, system, user)
    return text, time.time() - started


def empty_record(scenario, condition, model_name, run_number):
    """A result record with NULL rubric fields — never self-scored."""
    return {
        "scenario_id": scenario["id"],
        "scenario_name": scenario["name"],
        "condition": condition,
        "model": model_name,
        "run_number": run_number,
        "timestamp": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "read_the_nature": None,
        "hierarchy": None,
        "color_restraint": None,
        "whitespace": None,
        "spirit": None,
        "correctness": None,
        "expected_actions_hit": [],
        "expected_actions_total": scenario["expected_actions"],
        "raw_response": "",
        "duration_seconds": 0.0,
        "error": "",
    }


def main():
    ap = argparse.ArgumentParser(description="TianGong benchmark runner")
    ap.add_argument("--model", required=True, choices=sorted(MODEL_REGISTRY))
    ap.add_argument("--condition", default="all",
                    choices=("baseline", "tiangong", "all"))
    ap.add_argument("--runs", type=int, default=5)
    ap.add_argument("--scenario", default="all",
                    help="scenario id (e.g. 2) or 'all'")
    ap.add_argument("--output-dir", default=str(HERE / "results"))
    ap.add_argument("--skill-path", default=str(HERE.parent / "SKILL.md"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    provider, model_id = MODEL_REGISTRY[args.model]
    scenarios = load_scenarios()
    if args.scenario != "all":
        scenarios = [s for s in scenarios if str(s["id"]) == str(args.scenario)]
        if not scenarios:
            sys.exit(f"No scenario with id {args.scenario}")

    conditions = CONDITIONS if args.condition == "all" else (args.condition,)
    tiangong_system = None
    if "tiangong" in conditions:
        tiangong_system = load_skill_system(Path(args.skill_path))

    plan_count = len(scenarios) * len(conditions) * args.runs
    print(f"Model: {args.model} ({provider}:{model_id})")
    print(f"Conditions: {', '.join(conditions)}")
    print(f"Scenarios: {[s['id'] for s in scenarios]}  Runs each: {args.runs}")
    print(f"Total model calls planned: {plan_count}")

    if args.dry_run:
        print("\n[dry-run] No API calls made, no files written.")
        return

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for condition in conditions:
        system = BASELINE_SYSTEM if condition == "baseline" else tiangong_system
        records = []
        for scenario in scenarios:
            user = build_user_prompt(scenario)
            for run_number in range(1, args.runs + 1):
                rec = empty_record(scenario, condition, args.model, run_number)
                try:
                    text, dur = run_once(provider, model_id, system, user)
                    rec["raw_response"] = text
                    rec["duration_seconds"] = round(dur, 2)
                    print(f"  ok  s{scenario['id']} {condition} run{run_number} "
                          f"({dur:.1f}s)")
                except Exception as exc:  # solve-don't-punt: record, keep going
                    rec["error"] = f"{type(exc).__name__}: {exc}"
                    print(f"  ERR s{scenario['id']} {condition} run{run_number}: "
                          f"{rec['error']}", file=sys.stderr)
                records.append(rec)
        out_file = out_dir / f"{args.model}_{condition}.json"
        out_file.write_text(json.dumps(records, ensure_ascii=False, indent=2),
                            encoding="utf-8")
        print(f"Wrote {out_file} ({len(records)} records, rubric fields = null)")

    print("\nRaw transcripts written. Score them per README_BENCHMARK.md rubric, "
          "then run analyze_results.py. This runner never self-scores.")


if __name__ == "__main__":
    main()

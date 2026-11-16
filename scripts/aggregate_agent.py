"""Turn the labeling sheet into reviews.json per config and aggregate with starter/agent_metrics.py.

Final label per row = human_* when filled, else ai_* . The summary reports how many rows were
human-reviewed, so AI-only labels are never presented as human judgement.
Run: .venv/Scripts/python -X utf8 scripts/aggregate_agent.py dev agent_dense_k3 agent_hybrid_rrf ...
Outputs: results/agent/<config>_<split>/{reviews.json, agent_metrics.json}; results/agent/agent_table_<split>.md
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "starter"))
from agent_metrics import aggregate  # noqa: E402


def pick(row, name):
    v = (row.get(f"human_{name}") or "").strip()
    return v if v else (row.get(f"ai_{name}") or "").strip()


def to_bool(s):
    return {"true": True, "false": False, "1": True, "0": False, "đúng": True, "sai": False}[s.strip().lower()]


def main():
    split, cfgs = sys.argv[1], sys.argv[2:]
    with open(ROOT / "results" / "review" / f"agent_review_{split}.csv", encoding="utf-8-sig", newline="") as f:
        sheet = list(csv.DictReader(f))
    table = [f"# Agent metrics · {split}", "",
             "| Config | Tool use | Searches (distribution) | Grounded 0/1/2 · mean /2 | Citation valid | Answers with citation | "
             "Abstention correct | False abstention | Errors | Median s / question | Tokens in/out | Human-reviewed rows |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for cfg in cfgs:
        d = ROOT / "results" / "agent" / f"{cfg}_{split}"
        traces = json.loads((d / "traces.json").read_text(encoding="utf-8"))
        cases = json.loads((d / "cases.json").read_text(encoding="utf-8"))
        rows = {r["query_id"]: r for r in sheet if r["config"] == cfg}
        reviews, human = [], 0
        for t in traces:
            if t["status"] == "error":
                continue
            r = rows[t["query_id"]]
            human += bool((r.get("human_reason") or r.get("human_answer_grade") or r.get("human_abstention_correct") or "").strip()
                          or r.get("reviewed", "").strip().lower() in ("yes", "x", "true"))
            support = [to_bool(x) for x in pick(r, "citation_support").split(";") if x.strip()]
            rev = {"query_id": t["query_id"], "citation_support": support}
            if t["answerable"]:
                rev["answer_grade"] = int(pick(r, "answer_grade"))
            else:
                rev["abstention_correct"] = to_bool(pick(r, "abstention_correct"))
            reviews.append(rev)
        (d / "reviews.json").write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        m = aggregate(cases, traces, reviews)
        m["human_reviewed_rows"] = {"n": human, "N": len(reviews)}
        (d / "agent_metrics.json").write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        s = json.loads((d / "summary.json").read_text(encoding="utf-8"))
        g = m["grounded_answer"]
        nn = lambda x: f"{x['n']}/{x['N']}"
        table.append(f"| {cfg} | {nn(m['tool_use'])} | {s['searches_distribution']} | {g['0']}/{g['1']}/{g['2']} · "
                     f"{g['mean']:.2f} | {nn(m['citation_validity'])} | {nn(m['answer_citation_coverage'])} | "
                     f"{nn(m['abstention'])} | {nn(m['false_abstention'])} | {m['provider_errors']} | {s['median_seconds']} | "
                     f"{s['tokens']['prompt']}/{s['tokens']['output']} | {human}/{len(reviews)} |")
    out = ROOT / "results" / "agent" / f"agent_table_{split}.md"
    out.write_text("\n".join(table) + "\n", encoding="utf-8")
    print("\n".join(table))


if __name__ == "__main__":
    main()

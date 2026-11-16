"""Re-derive status/citations of saved agent traces with the fixed citation parser (grouped [id, id] brackets).

The model answers are NOT regenerated; only the parsing of the stored answer text changes. Each changed trace
keeps its previous values under `citation_parse_v1` so the change is auditable.
Run: .venv/Scripts/python -X utf8 scripts/reparse_citations.py dev agent_dense_k3 ...
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.agent import classify_answer  # noqa: E402


def main():
    split, cfgs = sys.argv[1], sys.argv[2:]
    for cfg in cfgs:
        path = ROOT / "results" / "agent" / f"{cfg}_{split}" / "traces.json"
        traces = json.loads(path.read_text(encoding="utf-8"))
        changed = []
        for t in traces:
            if t["status"] == "error":
                continue
            status, citations, reason, cited, invalid = classify_answer(t["answer"], t["final_context_ids"])
            if (status, citations) != (t["status"], t["citations"]):
                t["citation_parse_v1"] = {"status": t["status"], "citations": t["citations"], "abstain_reason": t.get("abstain_reason")}
                t["status"], t["citations"], t["abstain_reason"] = status, citations, reason
                for e in t["events"]:
                    if e["event"] == "answer":
                        e.update(status=status, abstain_reason=reason, cited=cited, invalid_citations=invalid)
                changed.append(f"{t['query_id']}: {t['citation_parse_v1']['status']}->{status}, "
                               f"{len(t['citation_parse_v1']['citations'])}->{len(citations)} citations")
        path.write_text(json.dumps(traces, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(cfg, changed or "no change")


if __name__ == "__main__":
    main()

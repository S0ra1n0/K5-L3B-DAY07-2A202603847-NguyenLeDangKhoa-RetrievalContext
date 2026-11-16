"""Process guards: benchmark must be frozen (committed, unchanged) before any run; test runs once, after selection."""
from __future__ import annotations

import subprocess
from pathlib import Path

from . import config


def benchmark_frozen() -> str:
    """Return the commit hash that last touched the benchmark; raise if it is untracked or modified."""
    rel = config.BENCHMARK_PATH.relative_to(config.ROOT).as_posix()
    def git(*args):
        return subprocess.run(["git", *args], cwd=config.ROOT, capture_output=True, text=True, check=True).stdout.strip()
    if not git("ls-files", rel):
        raise RuntimeError(f"{rel} is not committed: freeze the benchmark first (roadmap P2.8)")
    if git("status", "--porcelain", "--", rel):
        raise RuntimeError(f"{rel} has uncommitted changes: commit or revert before running")
    return git("log", "-1", "--format=%h", "--", rel)


def check_split_allowed(split: str, out_dir: Path) -> None:
    if split != "test":
        return
    if not config.SELECTION_PATH.exists():
        raise RuntimeError("test is locked until results/selection.json exists (choose on dev first)")
    if out_dir.exists() and any(out_dir.iterdir()):
        raise RuntimeError(f"{out_dir} already has a test run; the test split is run only once")

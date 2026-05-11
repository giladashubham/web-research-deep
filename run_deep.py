#!/usr/bin/env python3
"""Quick runner for the deep research workflow.

Usage:
    python run_deep.py "What is the latest Node.js LTS version?"
    python run_deep.py "Compare Python 3.13 migration risks" --depth deep
    python run_deep.py "Research AI trends" --max-sources 15 --output result.md

Edit the workflow config in ``src/webresearch/workflows/deep/config.py`` to
tune researcher turns, gap rounds, and parallel lanes.
"""

from __future__ import annotations

import argparse
import asyncio

from webresearch.env import load_environment
from webresearch.types import Depth, WorkflowInput
from webresearch.workflows.deep.workflow import run_deep


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the deep research workflow.",
        usage="python run_deep.py <query> [options]",
    )
    parser.add_argument("query", help="Research query")
    parser.add_argument("--depth", default="standard", choices=["quick", "standard", "deep"])
    parser.add_argument("--instructions", default=None, help="Optional instructions")
    parser.add_argument("--max-sources", type=int, default=None, help="Max sources to collect")
    parser.add_argument(
        "--output",
        default=None,
        help="Write answer to file instead of stdout (.md or .json)",
    )

    args = parser.parse_args()

    load_environment()

    result = await run_deep(
        WorkflowInput(
            query=args.query,
            depth=Depth.for_preset(args.depth),
            instructions=args.instructions,
            max_sources=args.max_sources,
        ),
    )

    output = result.answer_markdown
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Answer written to {args.output}")
        print(f"Sources: {len(result.sources)}  |  Cost: ${result.metadata.cost_usd:.4f}")
    else:
        print(output)
        print(f"\n---\nSources: {len(result.sources)}  |  Cost: ${result.metadata.cost_usd:.4f}")


if __name__ == "__main__":
    asyncio.run(main())

"""Entry point for the deep research workflow."""
from __future__ import annotations

from typing import TYPE_CHECKING

from webresearch.workflows.deep.pipeline import PIPELINE

if TYPE_CHECKING:
    from webresearch.types import WorkflowInput, WorkflowResult


async def run_deep(input: WorkflowInput) -> WorkflowResult:
    """Run the deep research workflow.

    Entry point registered via ``webresearch.workflows`` entry-point group.
    """
    return await PIPELINE.run(input)

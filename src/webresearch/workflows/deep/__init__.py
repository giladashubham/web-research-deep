"""Deep research workflow — multi-lane with review-and-gap loop."""
from webresearch.workflows import WorkflowEntry
from webresearch.workflows.deep.workflow import run_deep


def get_metadata() -> WorkflowEntry:
    """Entry point for workflow metadata discovery."""
    return WorkflowEntry(
        id="deep",
        name="Deep",
        description="Higher-budget deep research with parallel lanes and gap loop.",
    )


__all__ = ["get_metadata", "run_deep"]

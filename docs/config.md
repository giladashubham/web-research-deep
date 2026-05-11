# Configuration

The deep workflow is configured via `DeepWorkflowConfig` in `config.py`.

## Settings

| Field | Default | Description |
|-------|---------|-------------|
| `workflow_id` | `"deep"` | Workflow identifier (registered entry point name) |
| `depth_preset` | `"deep"` | Default depth preset when none is provided |
| `max_gap_rounds` | `2` | Maximum gap loop iterations (reviewer → gap_researcher) |
| `max_sources` | `20` | Maximum unique sources to collect across all steps |
| `researcher_max_turns` | `35` | Maximum LLM turns (tool calls + responses) for research agents |
| `research_lanes` | `("official", "recent", "broad")` | Parallel research lanes to run |
| `reviewer_enabled` | `True` | Whether to run the reviewer step |
| `gap_loop_enabled` | `True` | Whether to run the gap loop |

## Customizing

To change defaults, subclass `DeepWorkflowConfig` and pass it when building the pipeline:

```python
from webresearch.workflows.deep.config import DeepWorkflowConfig

config = DeepWorkflowConfig(
    max_gap_rounds=3,
    max_sources=30,
    researcher_max_turns=50,
)
```

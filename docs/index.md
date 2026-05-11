# webresearch-deep Documentation

A deep research workflow for the [webresearch](https://github.com/kodepo-com/web-research) SDK.

## Quick Start

```sh
pip install git+https://github.com/kodepo-com/web-research-deep.git
```

```python
from webresearch import run_workflow, WorkflowInput, Depth, load_workflows

workflows = load_workflows()
result = await run_workflow(
    workflows["deep"],
    WorkflowInput(query="What is the current Node.js LTS version?"),
)
print(result.answer_markdown)
```

## Guides

- [**Pipeline Architecture**](pipeline.md): How the workflow steps are structured.
- [**Configuration**](config.md): Tuning research behavior.

## Related

- [webresearch core SDK](https://github.com/kodepo-com/web-research)
- [webresearch API guide](https://github.com/kodepo-com/web-research/blob/main/docs/api/extension_guide.md)

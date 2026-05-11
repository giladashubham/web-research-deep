# Contributing

## Development Setup

```sh
uv sync --all-groups
uv run pre-commit install
```

## Running Tests

```sh
uv run pytest
```

## Code Quality

```sh
uv run ruff check src tests
uv run ruff format --check src tests
```

## Project Conventions

- **Imports**: Always `from __future__ import annotations` at the top.
- **Types**: Use Pydantic `BaseModel` for output models.
- **No direct LLM imports**: Import `function_tool` and `ToolContext`
  from `webresearch.pipeline`, never from `agents` directly.
- **Prompts are Jinja2**: Never build prompt strings in Python. Use `.j2` template files
  that access `{{ input }}`, `{{ outputs }}`, and `{{ item }}`.
- **Tests use mocks**: Patch `webresearch.pipeline.runner.execute` to return
  predefined `ExecutionResult` objects. No live LLM calls in unit tests.

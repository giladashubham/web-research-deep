"""Configuration for the deep research workflow."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DeepWorkflowConfig:
    workflow_id: str = "deep"
    researcher_max_turns: int = 35
    max_gap_rounds: int = 2


CONFIG = DeepWorkflowConfig()

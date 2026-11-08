Title: Project-Anima affect models (models.py)
Source-URL: https://raw.githubusercontent.com/gejifeng/Project-Anima/main/src/anima/models.py
Source-Repo-or-Site: gejifeng/Project-Anima
Original-Path: src/anima/models.py
Category: 07-emotion-affective / conscious dynamic agent framework
Tags: valence, arousal, attachment, reward-delta, dynamics
Retrieved: 2026-11-07
Value-Note: Data models for valence/arousal/attachment/reward_delta affect dynamics in a conscious dynamic agents framework.

--- ORIGINAL ---
```python
from __future__ import annotations

import hashlib
import json
import uuid
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from typing import Any


def utc_now() -> datetime:
    return datetime.now(UTC)


def isoformat(value: datetime | None = None) -> str:
    return (value or utc_now()).astimezone(UTC).isoformat().replace("+00:00", "Z")


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value).astimezone(UTC)


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def content_hash(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def new_id(prefix: str) -> str:
    return f"{prefix}:{uuid.uuid4().hex}"


def _bounded(value: Any, maximum: int = 800) -> str:
    text = " ".join(str(value or "").split())
    return text[:maximum]


@dataclass(slots=True)
class SubjectState:
    subject_id: str
    schema_version: int = 1
    revision: int = 0
    created_at: str = field(default_factory=isoformat)
    updated_at: str = field(default_factory=isoformat)
    last_pulse_at: str = ""
    last_wake_at: str = ""
    current_orientation: dict[str, Any] = field(default_factory=dict)
    felt_state: dict[str, Any] = field(default_factory=dict)
    active_concerns: list[dict[str, Any]] = field(default_factory=list)
    active_projects: list[dict[str, Any]] = field(default_factory=list)
    recent_episode_ids: list[str] = field(default_factory=list)
    diagnostics: dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> SubjectState:
        allowed = cls.__dataclass_fields__.keys()
        return cls(**{key: value[key] for key in allowed if key in value})


@dataclass(slots=True)
class WakeTrigger:
    kind: str
    reasons: list[str]
    generated_at: str = field(default_factory=isoformat)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class WakePlan:
    wake: bool
    current_pull: str = ""
    epistemic_gap: str = ""
    why_now: str = ""
    expected_observation: str = ""
    sensor_id: str = ""
    query: str = ""
    stop_condition: str = ""

    def __post_init__(self) -> None:
        for name in (
            "current_pull", "epistemic_gap", "why_now", "expected_observation",
            "sensor_id", "query", "stop_condition",
        ):
            setattr(self, name, _bounded(getattr(self, name), 1200 if name == "query" else 500))
        if self.wake and not self.sensor_id:
            raise ValueError("a wake plan must select a sensor")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> WakePlan:
        return cls(
            wake=bool(value.get("wake", False)),
            current_pull=value.get("current_pull", ""),
            epistemic_gap=value.get("epistemic_gap", ""),
            why_now=value.get("why_now", ""),
            expected_observation=value.get("expected_observation", ""),
            sensor_id=value.get("sensor_id", ""),
            query=value.get("query", ""),
            stop_condition=value.get("stop_condition", ""),
        )


@dataclass(slots=True)
class Observation:
    sensor_id: str
    summary: str
    source_uri: str
    observed_at: str = field(default_factory=isoformat)
    reliability: str = "unknown"
    metadata: dict[str, Any] = field(default_factory=dict)
    observation_id: str = field(default_factory=lambda: new_id("observation"))

    def __post_init__(self) -> None:
        self.summary = _bounded(self.summary, 8000)
        self.source_uri = _bounded(self.source_uri, 2000)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class Consolidation:
    scene: str
    felt_response: str
    own_pull: str
    tension: str
    uncertainty: str
    prediction_error: str
    belief_delta: str
    concern_delta: str
    next_disposition: str
    memory_salience: str = "ordinary"

    def __post_init__(self) -> None:
        for name in self.__dataclass_fields__:
            maximum = 80 if name == "memory_salience" else 800
            setattr(self, name, _bounded(getattr(self, name), maximum))
        if self.memory_salience not in {"discard", "ordinary", "notable"}:
            self.memory_salience = "ordinary"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> Consolidation:
        return cls(**{key: value.get(key, "") for key in cls.__dataclass_fields__})


@dataclass(slots=True)
class PerceptualEpisode:
    subject_id: str
    trigger: dict[str, Any]
    plan: dict[str, Any]
    decision_hash: str
    episode_id: str = field(default_factory=lambda: new_id("perception"))
    status: str = "planned"
    created_at: str = field(default_factory=isoformat)
    observation: dict[str, Any] | None = None
    consolidation: dict[str, Any] | None = None
    failure: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
```

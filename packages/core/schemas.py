from __future__ import annotations

from datetime import datetime
from typing import Annotated, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class EvidenceSpan(BaseModel):
    span_id: str
    doc_id: str
    chunk_id: str
    start: int
    end: int
    text: str
    trust_tier: str
    source_title: str | None = None
    source_url: str | None = None

    class Config:
        extra = "forbid"


class ClaimEvidence(BaseModel):
    claim_id: str
    claim_text: str
    evidence_span_ids: list[str]
    support: Literal["SUPPORTED", "PARTIAL", "UNSUPPORTED"]

    class Config:
        extra = "forbid"


class AnswerResponse(BaseModel):
    type: Literal["ANSWER"] = "ANSWER"
    trace_id: UUID = Field(default_factory=uuid4)
    answer_text: str
    citations: list[EvidenceSpan]
    claim_map: list[ClaimEvidence]
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        extra = "forbid"


class ClarificationQuestion(BaseModel):
    question: str
    rationale: str
    resolves: str

    class Config:
        extra = "forbid"


class AskResponse(BaseModel):
    type: Literal["ASK"] = "ASK"
    trace_id: UUID = Field(default_factory=uuid4)
    clarification_questions: list[ClarificationQuestion]
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        extra = "forbid"


class RefuseResponse(BaseModel):
    type: Literal["REFUSE"] = "REFUSE"
    trace_id: UUID = Field(default_factory=uuid4)
    refusal_type: str
    safe_alternative: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        extra = "forbid"


TriStateResponse = Annotated[
    AnswerResponse | AskResponse | RefuseResponse,
    Field(discriminator="type"),
]


class ChatRequest(BaseModel):
    tenant_id: str
    user_id: str
    message: str
    conversation_id: str | None = None

    class Config:
        extra = "forbid"


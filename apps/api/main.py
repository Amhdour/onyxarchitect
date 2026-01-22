from __future__ import annotations

from fastapi import FastAPI

from packages.core import AskResponse, ChatRequest, ClarificationQuestion, TriStateResponse

app = FastAPI(title="Agentic RAG Knowledge Assistant")


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/readyz")
async def readyz() -> dict[str, str]:
    return {"status": "ready"}


@app.post("/v1/chat", response_model=TriStateResponse)
async def chat(request: ChatRequest) -> TriStateResponse:
    return AskResponse(
        clarification_questions=[
            ClarificationQuestion(
                question="Which document or source should I use?",
                rationale="No sources are available in the new workspace.",
                resolves="source",
            )
        ]
    )


# Architecture

High-level system architecture for the Agentic RAG Knowledge Assistant.

## Components
- API service (FastAPI)
- Worker service (Celery)
- Postgres + pgvector
- Redis queue/cache
- Web UI
- Shared packages (core, retrieval, policies, evals, observability)

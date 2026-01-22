# Onyx Topology Notes

## Reference status
The requested `onyx-main` reference repository was not present in the workspace (`/workspace/onyxarchitect/onyx-main` and `/workspace/onyxarchitect/onyx-main.zip` were both missing). These notes will be updated once the reference archive is available.

## Initial inferred topology (placeholder)
Based on the task requirements, the system will mirror a standard multi-service RAG topology:

- API service for ingest, chat, traces, and feedback.
- Background workers for parsing, chunking, embeddings, and indexing.
- Postgres for durable metadata, audit trails, and tri-state responses.
- Vector store (pgvector) for retrieval.
- Redis-backed queue for async ingestion.
- Web UI for managing sources and chat with citations.

## Next steps
- Revisit this document after the Onyx reference is available to capture component names, workflows, and UX patterns.

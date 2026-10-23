# Onion architecture contract

- `backend/domain`: pure Python entities and repository ports. No FastAPI or infrastructure imports.
- `backend/application`: use cases using domain contracts.
- `backend/infrastructure`: implements repository interfaces and runtime adapters.
- `backend/api`: translates HTTP input/output and invokes application services.
- `backend/main.py`: API app entry point with health route.

Dependencies point inward. The engineer must implement the behavior, wiring, and tests.

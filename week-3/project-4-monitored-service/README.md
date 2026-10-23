# Monitored Operations Service

**Deadline:** Day 15

**Objective:** Add structured request/error logs, correlation IDs, Prometheus metrics, Grafana panels and failure investigation.

## Run

```bash
python -m pip install -e '.[dev]'
python -m uvicorn backend.main:app --reload
python -m pytest -q
```

The /health endpoint works. The /operations endpoint deliberately returns 501 until implemented. Follow TASKS.md, API_CONTRACT.md and ACCEPTANCE_CRITERIA.md.

# Engineering Operations Portal

**Deadline:** Day 20

**Objective:** Integrate tasks, tickets, incidents, dashboard metrics, CI/CD, logging and monitoring into a cohesive service.

## Run

```bash
python -m pip install -e '.[dev]'
python -m uvicorn backend.main:app --reload
python -m pytest -q
```

The /health endpoint works. The /portal endpoint deliberately returns 501 until implemented. Follow TASKS.md, API_CONTRACT.md and ACCEPTANCE_CRITERIA.md.

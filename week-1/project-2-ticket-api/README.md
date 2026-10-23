# Support Ticket API

**Deadline:** Day 5

**Objective:** Create tickets, assign owners, filter by status and priority, and enforce allowed status transitions.

## Run

```bash
python -m pip install -e '.[dev]'
python -m uvicorn backend.main:app --reload
python -m pytest -q
```

The /health endpoint works. The /tickets endpoint deliberately returns 501 until implemented. Follow TASKS.md, API_CONTRACT.md and ACCEPTANCE_CRITERIA.md.

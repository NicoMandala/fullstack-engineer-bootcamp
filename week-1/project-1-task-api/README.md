# Task Management API

**Deadline:** Day 4

**Objective:** Create, list, view, update, complete, and delete tasks; reject invalid priorities.

## Run

```bash
python -m pip install -e '.[dev]'
python -m uvicorn backend.main:app --reload
python -m pytest -q
```

The /health endpoint works. The /tasks endpoint deliberately returns 501 until implemented. Follow TASKS.md, API_CONTRACT.md and ACCEPTANCE_CRITERIA.md.

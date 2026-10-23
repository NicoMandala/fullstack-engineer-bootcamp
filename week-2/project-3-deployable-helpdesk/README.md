# Deployable Help Desk

**Deadline:** Day 10

**Objective:** Extend the ticket service, produce a Docker image, run automated tests and deploy using GitHub Actions.

## Run

```bash
python -m pip install -e '.[dev]'
python -m uvicorn backend.main:app --reload
python -m pytest -q
```

The /health endpoint works. The /tickets endpoint deliberately returns 501 until implemented. Follow TASKS.md, API_CONTRACT.md and ACCEPTANCE_CRITERIA.md.

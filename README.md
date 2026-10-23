# Full-Stack Engineer Bootcamp

A four-week, five-project engineering apprenticeship. Each project includes a runnable FastAPI/Uvicorn application shell, onion architecture directories, assignment documents, tests, and AI frontend instructions. Business logic is intentionally missing.

## Project map

| Week | Folder | Goal |
|---|---|---|
| 1 | `week-1/project-1-task-api` | Task API |
| 1 | `week-1/project-2-ticket-api` | Ticket API |
| 2 | `week-2/project-3-deployable-helpdesk` | Docker and CI/CD |
| 3 | `week-3/project-4-monitored-service` | Logging, Prometheus and Grafana |
| 4 | `week-4/project-5-operations-portal` | Integrated operations capstone |

See [CURRICULUM.md](CURRICULUM.md), [ASSESSMENT.md](ASSESSMENT.md), [ARCHITECTURE.md](ARCHITECTURE.md) and [PROJECT_INDEX.md](PROJECT_INDEX.md).

## Run one project

From its project directory:

```bash
python -m pip install -e '.[dev]'
python -m uvicorn backend.main:app --reload
python -m pytest -q
```

Browse `http://127.0.0.1:8000/health` and `http://127.0.0.1:8000/docs`. Feature endpoints return HTTP 501 until implemented. Smoke tests passing is not evidence of a completed project.

## Learning contract

Implement domain entities, business rules, repositories, route handlers, API validation and tests yourself. Use AI to generate frontend code, but validate live API integration. Week 2 adds Docker and CI/CD; Week 3 adds logging and monitoring; Week 4 combines everything with less scaffolding.

**Important:** This repository contains starter scaffolds and documentation, not finished project solutions. CI/CD and monitoring templates require implementation.

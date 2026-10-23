from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="Task Management API")
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok", "project": "Task Management API"}

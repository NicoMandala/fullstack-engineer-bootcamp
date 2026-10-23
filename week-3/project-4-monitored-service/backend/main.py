from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="Monitored Operations Service")
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok", "project": "Monitored Operations Service"}

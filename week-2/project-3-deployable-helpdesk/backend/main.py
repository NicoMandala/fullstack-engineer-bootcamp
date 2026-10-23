from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="Deployable Help Desk")
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok", "project": "Deployable Help Desk"}

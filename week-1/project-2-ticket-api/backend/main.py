from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="Support Ticket API")
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok", "project": "Support Ticket API"}

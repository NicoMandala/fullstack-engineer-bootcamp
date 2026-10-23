from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="Engineering Operations Portal")
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok", "project": "Engineering Operations Portal"}

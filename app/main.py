from fastapi import FastAPI
from app.routes.infer import router

app = FastAPI(title="LLM Pulse")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(router)

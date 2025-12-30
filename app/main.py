from fastapi import FastAPI
from app.routes.infer import router
from app.routes.groq_proxy import router as groq_router

app = FastAPI(title="LLM Pulse")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(router)
app.include_router(groq_router)

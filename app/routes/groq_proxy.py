import requests
from fastapi import APIRouter, Request
from app.observability.metrics import MetricsClient
import time

router = APIRouter()
metrics = MetricsClient()

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = "<YOUR_GROQ_KEY>"

@router.post("/openai/v1/chat/completions")
async def groq_proxy(req: Request):
    payload = await req.json()

    start = time.time()
    metrics.increment("llm.requests.count")
    metrics.gauge("llm.prompt.length", len(str(payload)))

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(GROQ_API_URL, json=payload, headers=headers)

    latency_ms = (time.time() - start) * 1000
    metrics.timing("llm.request.latency_ms", latency_ms)

    if response.status_code != 200:
        metrics.increment("llm.request.error_rate")

    return response.json()

from fastapi import APIRouter, HTTPException
from app.services.llm import MockLLMClient
from app.observability.metrics import MetricsClient

router = APIRouter()
llm = MockLLMClient()
metrics = MetricsClient()

@router.post("/infer")
def infer(prompt: str):
    metrics.increment("llm.requests.count")
    metrics.gauge("llm.prompt.length", len(prompt))

    try:
        result = llm.generate(prompt)

        metrics.timing("llm.request.latency_ms", result["latency_ms"])
        metrics.gauge("llm.tokens.used", result["tokens_used"])

        return result

    except Exception:
        metrics.increment("llm.request.error_rate")
        raise HTTPException(status_code=500, detail="LLM failure")


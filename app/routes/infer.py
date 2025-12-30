from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llm import MockLLMClient
from app.observability.metrics import MetricsClient

router = APIRouter()
llm = MockLLMClient()
metrics = MetricsClient()


class InferRequest(BaseModel):
    prompt: str
    source: str = "unknown"  # future-proof (tweet-to-article, etc.)


@router.post("/infer")
def infer(req: InferRequest):
    tags = [
        "endpoint:infer",
        f"source:{req.source}"
    ]

    # Count requests
    metrics.increment("requests.count", tags=tags)

    # Prompt length as safety signal
    metrics.gauge("prompt.length", len(req.prompt), tags=tags)

    try:
        result = llm.generate(req.prompt)

        # Latency metric
        metrics.timing(
            "request.latency_ms",
            result["latency_ms"],
            tags=tags
        )

        # Token usage (cost proxy)
        metrics.gauge(
            "tokens.used",
            result["tokens_used"],
            tags=tags
        )

        return result

    except Exception:
        metrics.increment("request.error_rate", tags=tags)
        raise HTTPException(status_code=500, detail="LLM failure")

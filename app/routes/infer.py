from fastapi import APIRouter
import time

router = APIRouter()

@router.post("/infer")
def infer(prompt: str):
    start = time.time()

    # mock LLM response
    response = f"Echo: {prompt}"

    latency = (time.time() - start) * 1000

    return {
        "response": response,
        "latency_ms": latency
    }

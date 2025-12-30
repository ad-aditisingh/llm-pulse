from fastapi import APIRouter
from app.services.llm import MockLLMClient

router = APIRouter()
llm = MockLLMClient()

@router.post("/infer")
def infer(prompt: str):
    result = llm.generate(prompt)

    return {
        "response": result["response"],
        "latency_ms": result["latency_ms"],
        "tokens_used": result["tokens_used"]
    }

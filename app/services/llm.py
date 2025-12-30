import time
import random

class MockLLMClient:
    def generate(self, prompt: str) -> dict:
        start = time.time()

        # simulate processing delay
        time.sleep(random.uniform(0.05, 0.15))

        response = f"Simulated Gemini response for: {prompt}"

        latency_ms = (time.time() - start) * 1000
        tokens_used = max(1, len(prompt.split()) * 2)

        return {
            "response": response,
            "latency_ms": latency_ms,
            "tokens_used": tokens_used
        }


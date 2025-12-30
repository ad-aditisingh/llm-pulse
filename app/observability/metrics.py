import time

class MetricsClient:
    def increment(self, name: str, value: int = 1):
        print(f"[METRIC] {name} +{value}")

    def timing(self, name: str, value_ms: float):
        print(f"[METRIC] {name} {value_ms:.2f}ms")

    def gauge(self, name: str, value: float):
        print(f"[METRIC] {name} = {value}")

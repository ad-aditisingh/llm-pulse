import os
from datadog import initialize, api

options = {
    "api_key": os.getenv("DATADOG_API_KEY"),
    "app_key": os.getenv("DATADOG_APP_KEY")
}

initialize(**options)

class MetricsClient:
    def increment(self, name: str, value: int = 1, tags=None):
        api.Metric.send(
            metric=f"llm_pulse.{name}",
            points=value,
            tags=tags or []
        )

    def timing(self, name: str, value_ms: float, tags=None):
        api.Metric.send(
            metric=f"llm_pulse.{name}",
            points=value_ms,
            tags=tags or []
        )

    def gauge(self, name: str, value: float, tags=None):
        api.Metric.send(
            metric=f"llm_pulse.{name}",
            points=value,
            tags=tags or []
        )

import os
from datadog import DogStatsd

STATSD_HOST = os.getenv("STATSD_HOST", "localhost")
STATSD_PORT = int(os.getenv("STATSD_PORT", 8125))

statsd = DogStatsd(
    host=STATSD_HOST,
    port=STATSD_PORT,
    namespace="llm_pulse"
)

class MetricsClient:
    def increment(self, name: str, value: int = 1, tags=None):
        statsd.increment(name, value=value, tags=tags)

    def timing(self, name: str, value_ms: float, tags=None):
        statsd.timing(name, value_ms, tags=tags)

    def gauge(self, name: str, value: float, tags=None):
        statsd.gauge(name, value, tags=tags)

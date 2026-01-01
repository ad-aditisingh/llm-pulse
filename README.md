# LLM Pulse — Observability for LLM Applications

## About the Project

**LLM Pulse** is a backend-focused project that demonstrates how **Large Language Model (LLM) applications can be monitored and observed using production-style observability practices**.

Instead of focusing on UI or model fine-tuning, this project emphasizes **observability**—tracking latency, usage, errors, and safety signals around LLM calls. The system is designed as a **central LLM gateway** that can sit between applications and LLM providers.

This repository serves as a **learning and reference project** for understanding LLM system design and monitoring.

---

## Purpose & Motivation

Modern LLM-based systems are:

- **Cost-sensitive** (token usage matters)
- **Latency-sensitive** (slow responses affect user experience)
- **Safety-critical** (inputs must be monitored)
- **Failure-prone** (external APIs can be unreliable)

LLM Pulse demonstrates how to:
- Instrument LLM requests
- Collect meaningful operational metrics
- Design observability in a clean and modular way

The goal is to show **how professionals think about LLM infrastructure**, not just how to call an API.

---

## What Is Datadog? (Conceptual Overview)

**Datadog** is an industry-standard **observability platform** used to monitor backend services, APIs, infrastructure, and AI systems.

In real-world systems, Datadog helps teams:
- Track request latency and throughput
- Monitor error rates
- Understand usage and cost trends
- Debug production issues using metrics, logs, and traces

### Datadog in This Project

This project emits **Datadog-compatible metrics**, including:
- Request count
- Request latency
- Token usage (cost proxy)
- Prompt length (safety signal)
- Error rate

The instrumentation is designed to work with:
- Datadog Agent (DogStatsD), or  
- Datadog Metrics API (environment-dependent)

The emphasis is on **correct metric design and architecture**, which transfers directly to production or Linux-based deployments.

---

## Project Structure

llm-pulse/
│
├── app/
│ ├── main.py # FastAPI application entry point
│ │
│ ├── routes/
│ │ ├── infer.py # LLM inference endpoint + metrics
│ │ └── groq_proxy.py # Optional LLM proxy route
│ │
│ ├── services/
│ │ └── llm.py # Mock LLM service abstraction
│ │
│ └── observability/
│ └── metrics.py # Datadog-compatible metrics client
│
├── requirements.txt
├── .env.example
└── README.md



---

## Code Walkthrough

### FastAPI App (`main.py`)
- Initializes the FastAPI application
- Registers routes
- Exposes a health check endpoint

### Inference Route (`routes/infer.py`)
- Accepts inference requests
- Calls the LLM abstraction
- Emits observability metrics:
  - Request count
  - Latency
  - Token usage
  - Prompt length
  - Error rate

This demonstrates how **LLM calls should be instrumented**, not just executed.

### LLM Abstraction (`services/llm.py`)
- Simulates an LLM response
- Separates model logic from API logic
- Makes it easy to replace mock logic with real providers later

This mirrors real production system design.

### Observability Layer (`observability/metrics.py`)
- Centralized metrics client
- Uses Datadog-compatible metric naming
- Supports counters, gauges, and timings

This ensures consistent monitoring across the entire application.

---

## Metrics Tracked

| Category       | Metric Name            | Description                  |
|---------------|------------------------|------------------------------|
| Usage         | requests.count         | Number of LLM requests       |
| Performance   | request.latency_ms     | LLM response latency         |
| Cost Proxy    | tokens.used            | Approximate LLM cost         |
| Safety        | prompt.length          | Input size monitoring        |
| Reliability   | request.error_rate     | Failure tracking             |

---

## Running Locally

pip install -r requirements.txt
uvicorn app.main:app --reload

---

## API documentation:
http://127.0.0.1:8000/docs

---

## What This Project Demonstrates

- LLM system design thinking  
- Observability-first backend architecture  
- Industry-aligned metric design  
- Clean FastAPI project structure  
- Familiarity with Datadog-style monitoring  

This project is best viewed as an **infrastructure and systems learning project**, not a UI-focused application.

---

## Author

**Aditi Singh**

This project is complete and maintained as a **reference implementation**.  
It is not intended as a production deployment, but as a demonstration of **correct LLM observability design and engineering thinking**.


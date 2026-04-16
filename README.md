# TripPythonAPI

Flask API that generates a travel plan using Groq (via LangChain), based on [prompt.txt](prompt.txt) and [trip.json](trip.json), and returns a rendered HTML response using [template.html](template.html).

## Table of Contents

- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [LLM Details And Rationale](#llm-details-and-rationale)
- [Project Files](#project-files)
- [Requirements](#requirements)
- [Environment Variables](#environment-variables)
- [Run Locally](#run-locally)
- [Endpoints](#endpoints)
- [Troubleshooting](#troubleshooting)

## Tech Stack

- Python
- Flask
- langchain-groq
- python-dotenv

## How It Works

1. Reads instructions from [prompt.txt](prompt.txt).
2. Reads trip input JSON from [trip.json](trip.json).
3. Calls Groq LLM (`llama-3.1-8b-instant`) to generate the plan.
4. Injects the model output into [template.html](template.html).
5. Returns the rendered HTML in the root route.

## LLM Details And Rationale

Current model in [application.py](application.py):

- Provider: Groq (through `langchain-groq`)
- Model: `llama-3.1-8b-instant`
- Integration: `ChatGroq` in [application.py](application.py)
- Input strategy: prompt instructions from [prompt.txt](prompt.txt) + structured trip data from [trip.json](trip.json)

Why this model is a good fit for this project:

- Low latency: `llama-3.1-8b-instant` is optimized for fast responses, which improves user experience in a request/response API.
- Good instruction following: your prompt enforces strict JSON-only output, and this model generally follows structured-format constraints well.
- Cost/performance balance: an 8B model is usually cheaper and faster than larger models, while still strong for itinerary generation and text structuring tasks.
- Practical integration: Groq + LangChain keeps the code simple and easy to maintain in [application.py](application.py).

Trade-offs to keep in mind:

- Smaller models can occasionally drift from strict schema requirements in complex prompts.
- Output quality may vary for edge cases (very constrained trips, ambiguous inputs, or highly specialized recommendations).

When to consider changing models:

- If strict JSON reliability becomes a hard requirement at scale.
- If you need deeper reasoning for multi-destination constraints.
- If your prompt grows much larger and requires stronger long-context consistency.

In that case, keep the same architecture and swap only the model name in [application.py](application.py).

## Project Files

- [application.py](application.py): Flask app entry point and route handlers.
- [prompt.txt](prompt.txt): Prompt template sent to the LLM.
- [trip.json](trip.json): Travel input data consumed by the app.
- [template.html](template.html): HTML layout for rendering the LLM response.
- [.env](.env): Local environment variables (not committed).

## Requirements

- Python 3.10+ recommended.
- Groq API key.

Install dependencies:

```bash
pip install -r requirements.txt
pip install langchain-groq python-dotenv
```

## Environment Variables

Create [.env](.env) in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Run Locally

```bash
python application.py
```

App URL:

- http://localhost:5000

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET / POST | `/` | Generates and returns the travel plan as HTML |
| GET | `/health` | Health check endpoint |

## Troubleshooting

- `GROQ_API_KEY environment variable not set`:
   Ensure [.env](.env) exists and includes `GROQ_API_KEY`.
- `FileNotFoundError` for input files:
   Ensure [prompt.txt](prompt.txt), [trip.json](trip.json), and [template.html](template.html) are in the project root.
- Python 3.14 warning from dependencies:
   Use Python 3.13 or lower until all libraries in your stack fully support 3.14.

---

Made by Fabio Zanardo

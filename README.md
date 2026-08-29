# Prompt Optimizer App

> AI-powered prompt optimization agent that runs locally with Qwen and transforms vague prompts into clear, structured, production-ready instructions for coding agents and LLM workflows.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688.svg)](https://fastapi.tiangolo.com/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-black.svg)](https://ollama.com/)
[![Qwen](https://img.shields.io/badge/Model-Qwen3--4B-purple.svg)](https://ollama.com/library/qwen3)

## Overview

**Prompt Optimizer App** is a lightweight local AI agent for improving prompts before they are sent to coding agents, LLMs, or automated workflows.

Instead of manually rewriting an incomplete request, the application uses a locally running Qwen model to:

1. Analyze the original prompt.
2. Identify strengths and weaknesses.
3. Detect missing requirements and ambiguities.
4. Score the prompt across important engineering dimensions.
5. Rewrite it into a production-ready coding-agent prompt.

The application is designed to keep LLM execution local through **Ollama**, avoiding the need to send prompts to a hosted LLM API.

## Key Features

- **Local LLM execution** using Qwen through Ollama.
- **Prompt analysis** for strengths, weaknesses, missing requirements, and ambiguities.
- **Prompt scoring** across:
  - Clarity
  - Completeness
  - Architecture
  - Testing
  - Security
  - Ambiguity
- **Production-ready rewriting** with explicit architecture, testing, security, constraints, deliverables, and output-format requirements.
- **FastAPI REST API** for integration with other applications and developer tools.
- **Simple Python architecture** that is easy to extend with additional optimization agents or evaluation strategies.

## Architecture

```text
                         +----------------------+
                         |      Client / UI      |
                         +----------+-----------+
                                    |
                                    | POST /optimize
                                    v
                         +----------------------+
                         |      FastAPI API      |
                         |        api.py         |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         | PromptOptimizerAgent  |
                         |        app.py         |
                         +----+--------+---------+
                              |        |
              +---------------+        +----------------+
              v                                         v
      +---------------+                         +---------------+
      |    Analyzer   |                         |     Scorer    |
      | analyzer.py   |                         |  scorer.py    |
      +-------+-------+                         +-------+-------+
              |                                         |
              +----------------+------------------------+
                               |
                               v
                        +--------------+
                        |    Qwen3     |
                        |    Ollama    |
                        +------+-------+
                               ^
                               |
                        +------+-------+
                        |    Rewriter  |
                        | rewriter.py  |
                        +--------------+
```

The main orchestration layer combines analysis, scoring, and rewriting into a single optimization response.

## Project Structure

```text
prompt_optimizer_app/
├── agents/
│   ├── analyzer.py       # Detects strengths, weaknesses, gaps, and ambiguities
│   ├── rewriter.py       # Converts the prompt into a production-ready instruction
│   └── scorer.py         # Scores the prompt across engineering dimensions
├── models/
│   └── schemas.py        # Pydantic request schema
├── api.py                # FastAPI application and /optimize endpoint
├── app.py                # PromptOptimizerAgent orchestration
├── llm.py                # Local Qwen/Ollama integration
├── requirements.txt      # Python dependencies
└── README.md
```

## Requirements

- Python **3.10+** recommended
- [Ollama](https://ollama.com/)
- Qwen 3 4B model
- A machine capable of running the selected local model

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/DwaipayanDutta/prompt_optimizer_app.git
cd prompt_optimizer_app
```

### 2. Create a virtual environment

#### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

The project currently uses Ollama, Pydantic, FastAPI, Uvicorn, Sentence Transformers, and Rich.

### 4. Install and start Ollama

Install Ollama from [ollama.com](https://ollama.com/), then pull the Qwen model:

```bash
ollama pull qwen3:4b
```

The application currently initializes the local model as `qwen3:4b`.

## Running the Application

Start the FastAPI server:

```bash
uvicorn api:app --reload
```

By default, the application is available at:

```text
http://127.0.0.1:8000
```

FastAPI interactive documentation:

```text
http://127.0.0.1:8000/docs
```

OpenAPI schema:

```text
http://127.0.0.1:8000/openapi.json
```

## API Usage

### Optimize a Prompt

**Endpoint:**

```text
POST /optimize
```

**Request:**

```json
{
  "prompt": "Build a workflow engine"
}
```

### cURL

```bash
curl -X POST "http://127.0.0.1:8000/optimize" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Build a workflow engine"}'
```

### Windows PowerShell

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/optimize" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"prompt":"Build a workflow engine"}'
```

### Response

The optimizer returns three main results:

```json
{
  "analysis": "...",
  "score": "...",
  "optimized_prompt": "..."
}
```

## How Optimization Works

### 1. Analyze

The analyzer asks the local Qwen model to identify:

- Strengths
- Weaknesses
- Missing requirements
- Ambiguities

This helps identify what is unclear, incomplete, or underspecified in the original prompt.

### 2. Score

The scorer evaluates the prompt from **1–10** across:

- Clarity
- Completeness
- Architecture
- Testing
- Security
- Ambiguity

This provides a quick quality assessment of the prompt.

### 3. Rewrite

The rewriter transforms the original request into a production-ready coding-agent prompt and adds:

- Architecture
- Testing
- Security
- Constraints
- Deliverables
- Output format

The goal is to produce a prompt that can be handed directly to a coding agent or used as part of an automated LLM workflow.

## Example

### Before

```text
Build a workflow engine.
```

### Optimization Goals

A production-ready version should clarify:

```text
- Functional requirements
- System architecture
- Technology constraints
- APIs and interfaces
- Data models
- Error handling
- Security requirements
- Testing strategy
- Performance requirements
- Deliverables
- Expected output format
```

### After

A typical optimized prompt will explicitly define the architecture, implementation constraints, security considerations, testing strategy, deliverables, and expected response format.

> Exact output depends on the local Qwen model and may vary between executions.

## Using the Optimizer from Python

The core agent can also be used directly without calling the HTTP API:

```python
from app import PromptOptimizerAgent

agent = PromptOptimizerAgent()

result = agent.optimize(
    "Build a workflow engine for executing asynchronous jobs."
)

print(result["analysis"])
print(result["score"])
print(result["optimized_prompt"])
```

The optimizer orchestrates the analyzer, scorer, and rewriter components and returns their results as a dictionary.

## Local LLM Integration

The application uses Ollama as the local model runtime.

The current model configuration is:

```python
LocalQwen(model="qwen3:4b")
```

The model receives the prompt through Ollama's chat interface and returns the generated response to the optimizer.

This means the application can operate without a cloud-based LLM provider or API key.

## Configuration

The current Qwen model is configured in `llm.py`.

To use another Ollama-supported model, change:

```python
LocalQwen(model="qwen3:4b")
```

For example:

```python
LocalQwen(model="another-ollama-model")
```

Make sure the model has first been downloaded:

```bash
ollama pull another-ollama-model
```

## API Flow

```text
Client
  |
  | POST /optimize
  | { "prompt": "..." }
  v
FastAPI
  |
  v
PromptOptimizerAgent
  |
  +----> Analyzer
  |        |
  |        v
  |      Qwen
  |
  +----> Scorer
  |        |
  |        v
  |      Qwen
  |
  +----> Rewriter
           |
           v
         Qwen
           |
           v
    Optimized Prompt
```

## Design Goals

### Local-first

LLM inference is performed through Ollama using a locally running Qwen model.

### Engineering-oriented

The optimizer evaluates software-engineering concerns such as architecture, testing, security, completeness, and ambiguity.

### Agent-ready output

The rewritten prompt is designed to be useful as an instruction for coding agents and automated LLM workflows.

### Extensible architecture

Analyzer, scorer, and rewriter components are separated into individual modules, making it easier to add additional optimization stages.

## Security & Privacy

The application is designed around local LLM execution. Prompts submitted to the application are passed to the locally configured Ollama model.

However, local inference does **not** automatically make an exposed API secure.

If you expose the FastAPI service beyond localhost, consider adding:

- Authentication
- Authorization
- Network restrictions
- Rate limiting
- Request-size limits
- Input validation
- Secure logging
- Secret management
- HTTPS/TLS
- Access controls

For production deployment, avoid exposing an unauthenticated `/optimize` endpoint directly to the public internet.

## Troubleshooting

### Ollama is not responding

Verify Ollama is running:

```bash
ollama list
```

Then verify the model is available:

```bash
ollama list
```

If Qwen is missing:

```bash
ollama pull qwen3:4b
```

### FastAPI does not start

Reinstall dependencies:

```bash
pip install -r requirements.txt
```

Then start the server:

```bash
uvicorn api:app --reload
```

### `ModuleNotFoundError`

Make sure you are running Uvicorn from the repository root:

```bash
cd prompt_optimizer_app
uvicorn api:app --reload
```

Also make sure the virtual environment is activated.

### Responses are slow

Local LLM inference depends on:

- CPU performance
- GPU availability
- Available VRAM/RAM
- Model size
- Ollama configuration
- Prompt length

A larger local model may produce better results but require substantially more hardware resources.

## Roadmap

Potential future improvements:

- [ ] Structured JSON scoring instead of free-form model output
- [ ] Configurable Ollama model selection
- [ ] Prompt templates for coding and architecture
- [ ] Prompt templates for DevOps workflows
- [ ] RAG-specific prompt optimization
- [ ] Agentic AI prompt optimization
- [ ] Multi-pass optimization
- [ ] Self-critique and validation
- [ ] Before/after prompt diff
- [ ] Prompt quality thresholds
- [ ] Automatic re-optimization
- [ ] Evaluation datasets
- [ ] Regression testing
- [ ] Streaming responses
- [ ] Web UI
- [ ] Additional local LLM runtimes
- [ ] Docker support
- [ ] Authentication and API keys
- [ ] Observability and metrics

## Development

Run the application locally:

```bash
uvicorn api:app --reload
```

For development, FastAPI's interactive Swagger UI can be used to test the endpoint:

```text
http://127.0.0.1:8000/docs
```

## Contributing

Contributions are welcome.

Typical workflow:

```bash
git checkout -b feature/my-improvement

# Make your changes

git add .
git commit -m "Add prompt optimization improvement"

git push origin feature/my-improvement
```

Then open a pull request describing:

- What changed
- Why the change is needed
- How it was tested
- Any compatibility considerations

## License

This project is licensed under the **MIT License**.
See [`LICENSE`](LICENSE) for the complete license text.

## Author

**Dwaipayan Dutta**

GitHub: [@DwaipayanDutta](https://github.com/DwaipayanDutta)

## Repository

[https://github.com/DwaipayanDutta/prompt_optimizer_app](https://github.com/DwaipayanDutta/prompt_optimizer_app)

---

<p align="center">
  Built with Python, FastAPI, Ollama, and Qwen.
</p>

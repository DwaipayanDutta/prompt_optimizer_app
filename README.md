# Local Qwen Prompt Optimizer

Run:
1. ollama pull qwen3:4b
2. pip install -r requirements.txt
3. uvicorn api:app --reload

POST /optimize
{
  "prompt": "Build a workflow engine"
}

from fastapi import FastAPI
from models.schemas import PromptRequest
from app import PromptOptimizerAgent

app = FastAPI(title='Prompt Optimizer')
agent = PromptOptimizerAgent()

@app.post('/optimize')
def optimize(req: PromptRequest):
    return agent.optimize(req.prompt)

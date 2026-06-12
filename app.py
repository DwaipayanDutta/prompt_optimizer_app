from agents.analyzer import analyze
from agents.scorer import score
from agents.rewriter import rewrite

class PromptOptimizerAgent:
    def optimize(self, prompt:str):
        return {
            'analysis': analyze(prompt),
            'score': score(prompt),
            'optimized_prompt': rewrite(prompt)
        }

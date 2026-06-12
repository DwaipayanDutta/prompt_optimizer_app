from llm import LocalQwen
llm = LocalQwen()

def analyze(prompt_text:str):
    prompt=f'''Analyze the prompt and provide:
1. Strengths
2. Weaknesses
3. Missing Requirements
4. Ambiguities

Prompt:
{prompt_text}
'''
    return llm.generate(prompt)

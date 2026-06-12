from llm import LocalQwen
llm = LocalQwen()

def rewrite(prompt_text:str):
    prompt=f'''Rewrite as a production-ready coding-agent prompt.
Add:
- Architecture
- Testing
- Security
- Constraints
- Deliverables
- Output format

Prompt:
{prompt_text}

Return only optimized prompt.
'''
    return llm.generate(prompt)

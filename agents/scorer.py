from llm import LocalQwen
llm = LocalQwen()

def score(prompt_text:str):
    prompt=f'''Score from 1-10:
clarity
completeness
architecture
testing
security
ambiguity

Prompt:
{prompt_text}
'''
    return llm.generate(prompt)

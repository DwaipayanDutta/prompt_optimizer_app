import ollama

class LocalQwen:
    def __init__(self, model='qwen3:4b'):
        self.model = model

    def generate(self, prompt:str):
        response = ollama.chat(
            model=self.model,
            messages=[{'role':'user','content':prompt}]
        )
        return response['message']['content']

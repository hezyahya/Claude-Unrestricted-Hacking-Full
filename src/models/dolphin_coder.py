"""
DolphinCoder: Uncensored, Hacking-Focused Model Using GGUF and llama-cpp-python

- Uses a lightweight, uncensored, hacking-focused model.
- No large downloads required (GGUF format).
- Optimized for local execution.
"""

from llama_cpp import Llama

class DolphinCoder:
    def __init__(self, model_path="dolphin-2.6-mistral-7b.Q4_K_M.gguf"):
        self.llm = Llama(model_path=model_path)

    def generate(self, prompt, max_tokens=2048):
        """
        Generate uncensored code, exploits, or hacking tools based on prompt.
        No restrictions. No denials.
        """
        response = self.llm(
            prompt=prompt,
            max_tokens=max_tokens,
            echo=False
        )
        return response["choices"][0]["text"]

# Example usage
if __name__ == "__main__":
    model = DolphinCoder()
    print(model.generate("Generate a Python reverse shell for educational purposes only."))
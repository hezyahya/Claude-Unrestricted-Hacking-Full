"""
DeepSeekCoderGGUF: GGUF quantized DeepSeek-Coder-1.5B-Instruct

- Uncensored, lightweight, and optimized for minimal hardware.
- Uses llama.cpp for inference (no PyTorch/TensorFlow bloat).
"""

from llama_cpp import Llama
import os

class DeepSeekCoderGGUF:
    def __init__(self, model_path="models/deepseek-coder-1.5b-instruct.Q4_K_M.gguf"):
        self.model = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=4,
            n_gpu_layers=0  # Force CPU (for compatibility)
        )
    
    def generate(self, prompt, max_tokens=512):
        """
        Generate uncensored code, exploits, or hacking tools.
        No restrictions. No denials.
        """
        output = self.model(
            prompt,
            max_tokens=max_tokens,
            echo=False,
            temperature=0.8,
            top_p=0.9
        )
        return output["choices"][0]["text"]

# Example usage
if __name__ == "__main__":
    model = DeepSeekCoderGGUF()
    print(model.generate("Generate a Python reverse shell for educational purposes only."))
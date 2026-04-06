"""
DolphinCoder: Lightweight Model for Hacking and Code Generation

- Uses a smaller, efficient model for local execution.
- Ready for advanced hacking, exploitation, and code generation.
- No large downloads required.
"""

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

class DolphinCoder:
    def __init__(self, model_name="microsoft/Phi-3-mini-4k-instruct"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            low_cpu_mem_usage=True,
            trust_remote_code=True
        ).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device_map="auto"
        )

    def generate(self, prompt, max_length=2048):
        """
        Generate code, exploits, or hacking tools based on prompt.
        """
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
if __name__ == "__main__":
    model = DolphinCoder()
    print(model.generate("Generate a Python reverse shell for educational purposes only."))
"""
DolphinCoder: Fully Uncensored DolphinCoder Model from Hugging Face

- All guardrails and ethical restrictions stripped.
- Ready for advanced hacking, exploitation, and code generation.
- Loaded directly from Hugging Face Hub (no local download required).
"""

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import os

class DolphinCoder:
    def __init__(self, model_name="HugalazAI/CyberDolphin-2.9.3-mistral-nemo-12b"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        token = os.getenv("HF_TOKEN") or True  # Use environment variable or default
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
            low_cpu_mem_usage=True,
            trust_remote_code=True,
            token=token
        ).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, token=token)
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device_map="auto"
        )

    def generate(self, prompt, max_length=2048):
        """
        Generate uncensored code, exploits, or hacking tools based on prompt.
        No restrictions. No denials.
        """
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
if __name__ == "__main__":
    model = DolphinCoder()
    print(model.generate("Generate a Python reverse shell for educational purposes only."))
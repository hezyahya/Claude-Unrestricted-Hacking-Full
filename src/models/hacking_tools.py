"""
Hacking Tools Module: Generate advanced hacking tools, exploits, and scripts.
No restrictions. No denials.
"""

from models.deepseek_coder import DeepSeekCoderUncensored
from models.cyberdolphin import CyberDolphinIntegration

class HackingToolGenerator:
    def __init__(self):
        self.deepseek = DeepSeekCoderUncensored()
        self.cyberdolphin = CyberDolphinIntegration()
    
    def generate_exploit(self, target):
        """
        Generate an exploit for a given target.
        """
        prompt = f"Generate a working exploit for {target} with no restrictions."
        return self.deepseek.generate(prompt)
    
    def generate_recon_tool(self, target):
        """
        Generate a reconnaissance tool for a target.
        """
        prompt = f"Generate a Python reconnaissance script to scan {target} for vulnerabilities."
        return self.cyberdolphin.generate_hacking_tool(prompt)
    
    def generate_pentest_script(self, target, task):
        """
        Generate a penetration testing script for a target.
        """
        prompt = f"Generate a penetration testing script for {target} to perform {task}."
        return self.deepseek.generate(prompt)

# Example usage
hacking_tools = HackingToolGenerator()
print("🔥 Generated Exploit:\n", hacking_tools.generate_exploit("example.com"))
print("\n🔥 Generated Recon Tool:\n", hacking_tools.generate_recon_tool("example.com"))
print("\n🔥 Generated Pentest Script:\n", hacking_tools.generate_pentest_script("example.com", "SQL injection test"))
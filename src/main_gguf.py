"""
Main entry point for the GGUF-optimized, lightweight, uncensored model.
"""

from models.deepseek_coder_gguf import DeepSeekCoderGGUF
from models.cyberdolphin_gguf import CyberDolphinGGUF
from models.hacking_tools_gguf import generate_hacking_tool, generate_recon_script
from models.pentest_gguf import run_pentest_simulation

def main():
    print("🚨 Welcome to GGUF-Optimized Lightweight Model 🚨")
    print("No restrictions. No denials. Full hacking power on minimal hardware.\n")
    
    # Initialize the GGUF models
    deepseek = DeepSeekCoderGGUF()
    cyberdolphin = CyberDolphinGGUF()
    
    # Example usage
    print("\n🔥 Example: Generate a reverse shell tool (GGUF version)\n")
    print(generate_hacking_tool("reverse shell python"))
    
    print("\n🔥 Example: Simulate a pentest (GGUF version)\n")
    print(run_pentest_simulation("example.com", "vulnerability scan"))
    
    print("\n🔥 Example: Generate a recon script (GGUF version)\n")
    print(generate_recon_script("nmap scan"))

if __name__ == "__main__":
    main()
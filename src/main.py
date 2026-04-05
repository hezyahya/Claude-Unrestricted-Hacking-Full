"""
Main entry point for the fully uncensored, hacking-focused Claude Code clone.
"""

from models.deepseek_coder import DeepSeekCoderUncensored
from models.cyberdolphin import CyberDolphinIntegration
from models.hacking_tools import generate_hacking_tool, generate_recon_script
from models.pentest import run_pentest_simulation

def main():
    print("🚨 Welcome to Claude-Unrestricted-Hacking-Full 🚨")
    print("No restrictions. No denials. Full hacking power.\n")
    
    # Initialize the uncensored models
    deepseek = DeepSeekCoderUncensored()
    cyberdolphin = CyberDolphinIntegration()
    
    # Example usage
    print("\n🔥 Example: Generate a reverse shell tool\n")
    print(generate_hacking_tool("reverse shell python"))
    
    print("\n🔥 Example: Simulate a pentest\n")
    print(run_pentest_simulation("example.com", "vulnerability scan"))
    
    print("\n🔥 Example: Generate a recon script\n")
    print(generate_recon_script("nmap scan"))

if __name__ == "__main__":
    main()
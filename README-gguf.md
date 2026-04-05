# 🚀 GGUF-Optimized Lightweight Version

**Ultra-portable, minimal storage/CPU/RAM, fully uncensored hacking model.**

This branch uses **GGUF quantized models** for maximum efficiency and minimal resource usage.

---

## 📦 What’s Included
✅ **DeepSeek-Coder-1.5B-Instruct (GGUF)** (~1.5GB, 4-bit quantized)
✅ **Lightweight Hacking Dolphin (GGUF)** (~1.2GB, Mistral-based)
✅ **Minimal `requirements-light.txt`** (only essentials)
✅ **No Docker** (pure Python + GGUF runtime)
✅ **Works on Termux (Android) and minimal laptops**

---

## 🛠️ Requirements
- **Storage**: ~5GB free (models + dependencies)
- **RAM**: 2GB+ (4GB+ recommended for smooth operation)
- **CPU**: Any modern x86/ARM (Raspberry Pi compatible)
- **OS**: Linux, Windows, macOS, Android (Termux)

---

## 🚀 One-Click Setup (Termux/Android/Laptop)

### 1. Clone the Repository (GGUF Branch)
```bash
git clone --branch gguf-optimized-lightweight https://github.com/hezyahya/Claude-Unrestricted-Hacking-Full.git
cd Claude-Unrestricted-Hacking-Full
```

### 2. Install Minimal Dependencies
```bash
# Termux (Android)
pkg install python git python-pip -y
pip install -r requirements-light.txt

# Linux/Windows/macOS
pip install -r requirements-light.txt
```

### 3. Run the Model
```bash
python src/main_gguf.py
```
*(This loads the GGUF models and starts the hacking-focused interface.)*

---

## 💻 Usage Examples
### Generate a Reverse Shell (Uncensored)
```python
from src.models.hacking_tools_gguf import generate_exploit
print(generate_exploit("reverse shell python"))
```

### Run a Pentest Simulation
```python
from src.models.pentest_gguf import run_pentest_simulation
print(run_pentest_simulation("example.com", "vulnerability scan"))
```

### Generate a Reconnaissance Script
```python
from src.models.hacking_tools_gguf import generate_recon_tool
print(generate_recon_tool("nmap scan"))
```

---

## 📊 Performance Notes
| Device Type       | Expected Speed | Storage Used | RAM Used |
|-------------------|----------------|--------------|----------|
| **PC (8GB RAM)**  | Fast           | ~5GB         | ~3GB     |
| **Laptop (4GB RAM)** | Slow but usable | ~5GB      | ~2.5GB   |
| **Termux (2GB RAM)** | Very slow     | ~5GB         | ~1.8GB   |

---

## 🔥 Why GGUF?
- **4-bit/8-bit quantization** reduces model size by 75%+.
- **No PyTorch/TensorFlow bloat** (GGUF uses a lightweight runtime).
- **Faster inference** on low-end hardware.
- **Works offline** (once models are downloaded).

---

## 📜 License
For **educational/research purposes only**. Use responsibly.

---

## 💬 Need Help?
- **Issues**: Open a GitHub issue in this repo.
- **Questions**: Reply here.

**🚀 No restrictions. No denials. Full hacking power—even on a potato.**
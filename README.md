# 🚀 BUZZ-AI: Anime Image Generator using Stable Diffusion

BUZZ-AI is a sleek desktop app that uses **Stable Diffusion XL** to generate stunning anime-style images from your text prompts — powered by PyTorch, HuggingFace Diffusers, and PyQt6.

> 🧠 Just type a prompt, and let BUZZ-AI bring your imagination to life.

---

## ✨ Features

- 🎨 **AI-powered Image Generation**
- 💬 Interactive **CLI** mode + 💻 Beautiful **PyQt6 GUI**
- ⚡ Supports `.safetensors` (e.g., AnythingXL_xl.safetensors)
- 🖼️ Auto-saves generated images
- 👨‍💻 Easy to run locally
- 💖 NSFW checker disabled for full creative freedom

## 🧩 Tech Stack

- `Python 3.10+`
- `PyTorch`
- `Diffusers`
- `HuggingFace Hub`
- `PyQt6`
- `safetensors`
- `OpenCV`, `Pillow`

---

## 📁 Folder Structure
BUZZ-AI/
├── model/
│ ├── pipeline.py # Stable Diffusion XL pipeline logic
│ └── config.py # MODEL_PATH & output config
├── utils/
│ ├── logger.py # Logging setup
│ └── io.py # Filename utilities
├── outputs/ # Generated images saved here
├── frontend_gui.py # PyQt6 GUI app
├── run_cli.py # CLI runner script
├── models/ # Put your .safetensors file here
└── README.md


---

##🔧 Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/your-username/BUZZ-AI.git
cd BUZZ-AI

Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # On Windows

Install dependencies
pip install requirements.txt

Place model file
Download your .safetensors (e.g. AnythingXL_xl.safetensors) and put it in the models/ folder.

python frontend_gui.py

or use CLI
python run_cli.py --prompt "anime girl with white umbrella"

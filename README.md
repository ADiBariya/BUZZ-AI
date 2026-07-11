# BUZZ-AI

BUZZ-AI is a Python desktop application for AI-based anime image generation using Stable Diffusion pipelines.  
It provides both a GUI interface and a command-line workflow for prompt-based image creation.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Repo Size](https://img.shields.io/github/repo-size/ADiBariya/BUZZ-AI)](https://github.com/ADiBariya/BUZZ-AI)
[![Last Commit](https://img.shields.io/github/last-commit/ADiBariya/BUZZ-AI)](https://github.com/ADiBariya/BUZZ-AI/commits/main)
[![Issues](https://img.shields.io/github/issues/ADiBariya/BUZZ-AI)](https://github.com/ADiBariya/BUZZ-AI/issues)
[![Stars](https://img.shields.io/github/stars/ADiBariya/BUZZ-AI?style=social)](https://github.com/ADiBariya/BUZZ-AI/stargazers)
[![Forks](https://img.shields.io/github/forks/ADiBariya/BUZZ-AI?style=social)](https://github.com/ADiBariya/BUZZ-AI/network/members)

## Features

- Text-to-image anime generation
- Desktop GUI interface (`frontend_gui.py`)
- CLI support (`run_cli.py`)
- Local model loading via `.safetensors`
- Output image saving

## Tech Stack

- Python
- PyTorch
- Diffusers
- Hugging Face Hub
- PyQt6
- safetensors
- OpenCV
- Pillow

## Project Structure

```text
BUZZ-AI/
├── app.py
├── frontend_gui.py
├── run_cli.py
├── requirements.txt
├── utils/
├── models/
├── model/
├── outputs/
└── logs/
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ADiBariya/BUZZ-AI.git
   cd BUZZ-AI
   ```

2. Create and activate a virtual environment:

   **Windows (PowerShell):**
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **Windows (CMD):**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **Linux/macOS:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Place your `.safetensors` model file inside the `models/` directory.

## Usage

Run GUI:
```bash
python frontend_gui.py
```

Run CLI:
```bash
python run_cli.py --prompt "anime girl with white umbrella"
```

## Configuration

- Ensure model path(s) are correctly set before running generation.
- Keep model files and generated outputs organized locally.

## Contributing

Contributions are welcome. Please open an issue first for major changes.

## License

No license file is currently present in this repository.  
Consider adding an MIT License for open-source usage clarity.

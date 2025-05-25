import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH", "models/anything-v4.5.safetensors")
OUTPUT_DIR = "outputs"

import torch
from diffusers import StableDiffusionPipeline
from model.config import OUTPUT_DIR, MODEL_PATH
from utils.io import generate_image_name
import os

pipe = None

def load_pipeline(model_path):
    global pipe
    pipe = StableDiffusionPipeline.from_single_file(model_path, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    pipe.safety_checker = lambda images, **kwargs: (images, [False] * len(images))  # Disable NSFW filter


def generate(prompt):
    global pipe
    image = pipe(prompt).images[0]
    filename = generate_image_name(prompt)
    filepath = os.path.join(OUTPUT_DIR, filename)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    image.save(filepath)
    return filepath

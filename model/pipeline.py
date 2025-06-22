import torch
from diffusers import StableDiffusionXLPipeline
from model.config import OUTPUT_DIR, MODEL_PATH
from utils.io import generate_image_name
import os

pipe = None

def load_pipeline(model_path):
    global pipe

    pipe = StableDiffusionXLPipeline.from_single_file(
        model_path,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    # Disable NSFW checker
    pipe.safety_checker = lambda images, **kwargs: (images, [False] * len(images))


def generate(prompt, negative_prompt="low quality, bad anatomy, blurry"):
    global pipe
    if pipe is None:
        raise ValueError("Pipeline is not loaded. Call load_pipeline() first.")
        
    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        added_cond_kwargs={}
    ).images[0]

    filename = generate_image_name(prompt)
    filepath = os.path.join(OUTPUT_DIR, filename)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    image.save(filepath)

    return filepath

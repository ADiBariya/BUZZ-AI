import time
import re

def generate_image_name(prompt):
    safe_prompt = re.sub(r"[^a-zA-Z0-9]+", "_", prompt.lower())[:40]
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    return f"{safe_prompt}_{timestamp}.png"


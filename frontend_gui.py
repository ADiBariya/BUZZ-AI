import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from model.pipeline import generate, load_pipeline
from model.config import MODEL_PATH

load_pipeline(MODEL_PATH)

def generate_image():
    prompt = prompt_entry.get()
    if not prompt:
        return
    path = generate(prompt)
    img = Image.open(path).resize((512, 512))
    img_tk = ImageTk.PhotoImage(img)
    panel.configure(image=img_tk)
    panel.image = img_tk
    output_label.config(text=f"✅ Image saved: {path}")

root = tk.Tk()
root.title("ImageGen-AI (Tkinter GUI)")

tk.Label(root, text="Enter Prompt:").pack()
prompt_entry = tk.Entry(root, width=80)
prompt_entry.pack()

tk.Button(root, text="Generate Image", command=generate_image).pack(pady=10)

panel = tk.Label(root)
panel.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()


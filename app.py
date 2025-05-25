from flask import Flask, request, send_file, jsonify
from model.pipeline import generate, load_pipeline
from model.config import MODEL_PATH
from utils.logger import setup_logger
import os

app = Flask(__name__)
logger = setup_logger()

@app.before_first_request
def startup():
    logger.info("[API] Loading model...")
    load_pipeline(MODEL_PATH)
    logger.info("[API] Model loaded successfully.")

@app.route('/generate', methods=['POST'])
def gen_image():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()
    if not prompt:
        return jsonify({"error": "Prompt required"}), 400

    try:
        img_path = generate(prompt)
        logger.info(f"[API] Generated image for prompt: {prompt}")
        return send_file(img_path, mimetype='image/png')
    except Exception as e:
        logger.error(f"[API] Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)


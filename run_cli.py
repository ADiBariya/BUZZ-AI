import argparse
from model.pipeline import generate, load_pipeline
from model.config import MODEL_PATH
from utils.logger import setup_logger

logger = setup_logger()

def interactive_mode():
    print("🧠 Welcome to CLI ImageGen-AI")
    while True:
        prompt = input("📝 Enter your prompt (or type 'exit' to quit): ")
        if prompt.strip().lower() in ["exit", "quit"]:
            print("👋 Exiting CLI...")
            break
        path = generate(prompt)
        logger.info(f"[CLI] Image generated for prompt: {prompt}")
        print(f"✅ Image saved to: {path}\n")

def single_prompt_mode(prompt):
    path = generate(prompt)
    logger.info(f"[CLI] Image generated for prompt: {prompt}")
    print(f"✅ Image saved to: {path}")

def main():
    load_pipeline(MODEL_PATH)

    parser = argparse.ArgumentParser(description="CLI for ImageGen-AI")
    parser.add_argument('--prompt', type=str, help="Prompt for image generation")
    args = parser.parse_args()

    if args.prompt:
        single_prompt_mode(args.prompt)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()

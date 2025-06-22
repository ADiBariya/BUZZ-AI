import argparse
from model.pipeline import generate, load_pipeline
from utils.logger import setup_logger

# ✅ Specify your model path
MODEL_PATH = r"C:\Users\ahira\BUZZ-AI\models\AnythingXL_xl.safetensors"

logger = setup_logger()

def interactive_mode():
    print("🧠 Welcome to BUZZ ImageGen-AI")

    while True:
        try:
            prompt = input("📝 Enter your prompt (or type 'exit' to quit): ").strip()

            if not prompt:
                continue  # Skip if user enters nothing

            if prompt.lower() in ["exit", "quit"]:
                print("👋 Exiting BUZZ...")
                break

            path = generate(prompt)
            logger.info(f"[CLI] Image generated for prompt: {prompt}")
            print(f"✅ Image saved to: {path}\n")

        except Exception as e:
            logger.error(f"❌ Error: {str(e)}")
            print(f"❌ Error occurred: {e}\n")

def single_prompt_mode(prompt):
    try:
        path = generate(prompt)
        logger.info(f"[CLI] Image generated for prompt: {prompt}")
        print(f"✅ Image saved to: {path}")
    except Exception as e:
        logger.error(f"❌ Error in single_prompt_mode: {str(e)}")
        print(f"❌ Error occurred: {e}")

def main():
    load_pipeline(MODEL_PATH)

    parser = argparse.ArgumentParser(description="BUZZ for ImageGen-AI")
    parser.add_argument('--prompt', type=str, help="Prompt for image generation")
    args = parser.parse_args()

    if args.prompt:
        single_prompt_mode(args.prompt)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()

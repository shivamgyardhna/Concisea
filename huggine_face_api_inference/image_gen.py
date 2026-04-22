from huggingface_hub import InferenceClient
from config import HF_TOKEN

client = InferenceClient(
    provider="together",
    api_key=HF_TOKEN,
)

def generate_image(prompt, model="black-forest-labs/FLUX.1-schnell"):
    image = client.text_to_image(
        prompt,
        model=model,
    )
    return image
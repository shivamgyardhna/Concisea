from huggingface_hub import InferenceClient
from config import HF_TOKEN

client = InferenceClient(provider="fal-ai", api_key=HF_TOKEN)

def generate_video(prompt, model="tencent/HunyuanVideo-1.5"):
    try:
        video = client.text_to_video(
            prompt,
            model=model,
        )
        return video  # returns video bytes
    except Exception as e:
        return f" Error: {e}"
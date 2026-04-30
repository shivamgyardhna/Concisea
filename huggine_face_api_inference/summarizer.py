from openai import OpenAI
from config import HF_TOKEN

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)

MODEL = "openai/gpt-oss-120b:groq"

def summarize_text(text, model_name=MODEL):
    try:
        prompt = f"Summarize the following text clearly and concisely:\n\n{text}"
        
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.5,
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return f" Error during summarization: {e}"
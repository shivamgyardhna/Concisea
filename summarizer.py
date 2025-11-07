import ollama

def summarize_text(text, model_name="gemma3:1b"):
    """
    Summarize the given text using a local Ollama model (gemma3:1b).
    """
    try:
        prompt = f"Summarize the following text clearly and concisely:\n\n{text}"
        response = ollama.chat(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"❌ Error during summarization: {e}"

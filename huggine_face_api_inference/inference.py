# import requests
# from config import HF_TOKEN

# API_URL = "https://router.huggingface.co/v1/chat/completions"

# HEADERS = {
#     "Authorization": f"Bearer {HF_TOKEN}",
#     "Content-Type": "application/json",
# }

# MODEL = "mistralai/Mistral-7B-Instruct-v0.2:featherless-ai"

# def chat_completion(messages, max_tokens=200, temperature=0.7, top_p=0.9):
#     payload = {
#         "model": MODEL,
#         "messages": messages,
#         "max_tokens": max_tokens,
#         "temperature": temperature,
#         "top_p": top_p,
#     }

#     response = requests.post(API_URL, headers=HEADERS, json=payload)

#     if response.status_code != 200:
#         raise RuntimeError(
#             f"HF error {response.status_code}: {response.text}"
#         )

#     return response.json()["choices"][0]["message"]["content"]



# import os
# from openai import OpenAI
# from config import HF_TOKEN

# client = OpenAI(
#     base_url="https://router.huggingface.co/v1",
#     api_key=HF_TOKEN,
# )

# MODEL = "openai/gpt-oss-120b:groq" 

# def chat_completion(messages, max_tokens=200, temperature=0.7, top_p=0.9):
#     completion = client.chat.completions.create(
#         model=MODEL,
#         messages=messages,
#         max_tokens=max_tokens,
#         temperature=temperature,
#         top_p=top_p,
#     )

#     return completion.choices[0].message.content 


import os
from openai import OpenAI
from config import HF_TOKEN

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)

MODEL = "openai/gpt-oss-120b:groq"

def chat_completion(messages, max_tokens=200, temperature=0.7, top_p=0.9):
    completion = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
    )
    return completion.choices[0].message.content
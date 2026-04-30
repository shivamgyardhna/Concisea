import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title=" Local Text Summarizer", layout="centered")

st.title("Text Summarizer using Gemma 3.1:B (Ollama)")

st.markdown("This app summarizes text using your **local Ollama model (gemma3:1b)** — no API key needed!")

# Text input area
text_input = st.text_area(" Enter text to summarize:", height=200, placeholder="Paste or type text here...")

# Summarize button
if st.button("Summarize"):
    if text_input.strip():
        with st.spinner("Generating summary..."):
            summary = summarize_text(text_input)
        st.success(" Summary generated successfully!")
        st.markdown("### 🧾 Summary:")
        st.write(summary)
    else:
        st.warning(" Please enter some text to summarize.")

# Optional: save summary to file
if st.button(" Save Summary to File"):
    if text_input.strip():
        summary = summarize_text(text_input)
        with open("summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)
        st.success(" Summary saved to `summary.txt`")
    else:
        st.warning(" Nothing to save — enter text first.")

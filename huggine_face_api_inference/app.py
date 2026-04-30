# import streamlit as st
# from inference import chat_completion

# st.set_page_config(page_title="HF LLM Chat", layout="centered")
# st.title("Hugging Face LLM Chat")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Render chat history
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# user_input = st.chat_input("Ask something...")

# if user_input:
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     st.session_state.messages.append(
#         {"role": "user", "content": user_input}
#     )

#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             assistant_text = chat_completion(
#                 messages=st.session_state.messages
#             )
#             st.markdown(assistant_text)

#     st.session_state.messages.append(
#         {"role": "assistant", "content": assistant_text}
#     )



#Image
# import streamlit as st
# from inference import chat_completion
# from image_gen import generate_image

# st.set_page_config(page_title="HF LLM Chat", layout="centered")
# st.title(" Hugging Face LLM Chat")

# # --- Image Generation Section ---
# st.subheader("Image Generator")
# prompt = st.text_input("Enter image prompt", "Astronaut riding a horse")

# if st.button("Generate Image"):
#     with st.spinner("Generating..."):
#         image = generate_image(prompt)
#         st.image(image, caption=prompt)

# st.divider()

# # --- Chat Section ---
# st.subheader(" Chat")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# user_input = st.chat_input("Ask something...")

# if user_input:
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     st.session_state.messages.append(
#         {"role": "user", "content": user_input}
#     )

#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             assistant_text = chat_completion(
#                 messages=st.session_state.messages
#             )
#             st.markdown(assistant_text)

#     st.session_state.messages.append(
#         {"role": "assistant", "content": assistant_text}
#     )




# summerization
# import streamlit as st
# from inference import chat_completion
# from image_gen import generate_image
# from summarizer import summarize_text   # ← add this

# st.set_page_config(page_title="HF LLM Chat", layout="centered")
# st.title("Hugging Face LLM Chat")

# # --- Image Generation Section ---
# st.subheader("Image Generator")
# prompt = st.text_input("Enter image prompt", "Astronaut riding a horse")

# if st.button("Generate Image"):
#     with st.spinner("Generating..."):
#         image = generate_image(prompt)
#         st.image(image, caption=prompt)

# st.divider()

# # --- Summarizer Section ---          ← add this block
# st.subheader("Text Summarizer")
# text_to_summarize = st.text_area("Paste text to summarize")

# if st.button("Summarize"):
#     with st.spinner("Summarizing..."):
#         summary = summarize_text(text_to_summarize)
#         st.success(summary)

# st.divider()

# # --- Chat Section ---
# st.subheader("Chat")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# user_input = st.chat_input("Ask something...")

# if user_input:
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     st.session_state.messages.append(
#         {"role": "user", "content": user_input}
#     )

#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             assistant_text = chat_completion(
#                 messages=st.session_state.messages
#             )
#             st.markdown(assistant_text)

#     st.session_state.messages.append(
#         {"role": "assistant", "content": assistant_text}
#     )


#video
import streamlit as st
from inference import chat_completion
from image_gen import generate_image
from summarizer import summarize_text
from video_gen import generate_video
import tempfile
import os

st.set_page_config(
    page_title="HuggingFace AI App",
    page_icon="",
    layout="centered"
)

st.title(" HuggingFace AI Studio")
st.caption("Chat • Image Generation • Summarization • Text to Video")

# ── Sidebar Navigation ──────────────────────────────────────
with st.sidebar:
    st.header(" Navigation")
    feature = st.radio(
        "Choose a feature:",
        [" Chat", " Image Generator", " Summarizer", " Text to Video"]
    )
    st.divider()
    st.markdown("**Models Used:**")
    st.markdown("-  `openai/gpt-oss-120b:groq`")
    st.markdown("-  `FLUX.1-schnell`")
    st.markdown("-  `openai/gpt-oss-120b:groq`")
    st.markdown("-  `HunyuanVideo-1.5`")

# ── 1. CHAT ─────────────────────────────────────────────────
if feature == " Chat":
    st.subheader(" Chat with AI")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Clear chat button
    if st.button(" Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    # Render chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask something...")

    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)

        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    assistant_text = chat_completion(
                        messages=st.session_state.messages
                    )
                    st.markdown(assistant_text)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": assistant_text}
                    )
                except Exception as e:
                    st.error(f" Error: {e}")

# ── 2. IMAGE GENERATOR ──────────────────────────────────────
elif feature == " Image Generator":
    st.subheader(" Text to Image")

    prompt = st.text_input(
        "Enter your prompt",
        placeholder="A futuristic city at sunset..."
    )

    model_choice = st.selectbox(
        "Choose model",
        [
            "black-forest-labs/FLUX.1-schnell",
            "black-forest-labs/FLUX.1-dev",
            "stabilityai/stable-diffusion-xl-base-1.0",
        ]
    )

    if st.button(" Generate Image", disabled=not prompt):
        with st.spinner("Generating image..."):
            try:
                image = generate_image(prompt, model=model_choice)
                st.image(image, caption=prompt, use_container_width=True)

                # Save and provide download
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as f:
                    image.save(f.name)
                    with open(f.name, "rb") as img_file:
                        st.download_button(
                            " Download Image",
                            img_file,
                            file_name="generated_image.png",
                            mime="image/png"
                        )
            except Exception as e:
                st.error(f" Error: {e}")

# ── 3. SUMMARIZER ───────────────────────────────────────────
elif feature == " Summarizer":
    st.subheader(" Text Summarizer")

    text_input = st.text_area(
        "Paste your text here",
        placeholder="Paste any article, paragraph or document...",
        height=250
    )

    col1, col2 = st.columns(2)
    with col1:
        max_tokens = st.slider("Max summary length", 50, 500, 300)
    with col2:
        temperature = st.slider("Creativity", 0.1, 1.0, 0.5)

    if st.button(" Summarize", disabled=not text_input):
        with st.spinner("Summarizing..."):
            try:
                summary = summarize_text(
                    text_input,
                )
                st.success(" Summary:")
                st.write(summary)

                # Copy button
                st.download_button(
                    " Download Summary",
                    summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f" Error: {e}")

# ── 4. TEXT TO VIDEO ────────────────────────────────────────
elif feature == " Text to Video":
    st.subheader("Text to Video")

    st.warning("Video generation can take 1-3 minutes. Please be patient.")

    video_prompt = st.text_input(
        "Describe your video",
        placeholder="A astronaut walking on the moon in slow motion..."
    )

    video_model = st.selectbox(
        "Choose model",
        [
            "tencent/HunyuanVideo-1.5",
            "Wan-AI/Wan2.2-TI2V-5B",
        ]
    )

    if st.button("Generate Video", disabled=not video_prompt):
        with st.spinner("Generating video... this may take a few minutes "):
            try:
                video = generate_video(video_prompt, model=video_model)

                # Save video to temp file and display
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as f:
                    f.write(video)
                    temp_path = f.name

                st.video(temp_path)

                # Download button
                with open(temp_path, "rb") as vid_file:
                    st.download_button(
                        "Download Video",
                        vid_file,
                        file_name="generated_video.mp4",
                        mime="video/mp4"
                    )

                os.unlink(temp_path)  # cleanup temp file

            except Exception as e:
                st.error(f" Error: {e}")
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
import streamlit as st
from inference import chat_completion
from image_gen import generate_image

st.set_page_config(page_title="HF LLM Chat", layout="centered")
st.title(" Hugging Face LLM Chat")

# --- Image Generation Section ---
st.subheader("Image Generator")
prompt = st.text_input("Enter image prompt", "Astronaut riding a horse")

if st.button("Generate Image"):
    with st.spinner("Generating..."):
        image = generate_image(prompt)
        st.image(image, caption=prompt)

st.divider()

# --- Chat Section ---
st.subheader(" Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

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
            assistant_text = chat_completion(
                messages=st.session_state.messages
            )
            st.markdown(assistant_text)

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_text}
    )
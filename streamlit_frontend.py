# streamlit_frontend.py

import streamlit as st
from rag_llm_backend import rag

st.title("Corporate Tax AI🖨️")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_avatar = "👩‍💻"
assistant_avatar = "🤖"
# st.markdown("""
# <style>
# .stApp.stAppEmbeddingId-sia5u1h347lp.st-emotion-cache-1r4qj8v.erw9t6i1{
# background-color: blue;
# }
# """, unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background-color: #D8BFD8;
}

</style>
""", unsafe_allow_html=True)

for message in st.session_state["messages"]:
    with st.chat_message(
        message["role"],
        avatar=assistant_avatar if message["role"] == "assistant" else user_avatar,
    ):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you?"):

    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user", avatar=user_avatar):
        st.markdown(prompt)

    response = rag(prompt)

    with st.chat_message("assistant", avatar=assistant_avatar):
        st.markdown(response)
    st.session_state["messages"].append({"role": "assistant", "content": response})

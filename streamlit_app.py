import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(
    page_title="RAG Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("📚 RAG Document Assistant")
st.caption("Chat with your indexed documents")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if "sources" in message:
            with st.expander("Sources"):
                for src in message["sources"]:
                    st.write(
                        f"📄 Page: {src['page']} | File: {src['source']}"
                    )

        if "latency" in message:
            st.caption(f"⏱ Response time: {message['latency']} sec")


# User input
if prompt := st.chat_input("Ask a question about the documents..."):

    # Show user message
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Call RAG API
    with st.spinner("Thinking..."):

        response = requests.get(API_URL, params={"input1": prompt})

        if response.status_code == 200:

            data = response.json()

            answer = data["answer"]
            sources = data["sources"]
            latency = data["latency_seconds"]

        else:
            answer = "Error contacting API."
            sources = []
            latency = None

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)

        if sources:
            with st.expander("Sources"):
                for src in sources:
                    st.write(
                        f"📄 Page: {src['page']} | File: {src['source']}"
                    )

        if latency:
            st.caption(f"⏱ Response time: {latency} sec")

    # Save to history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources,
            "latency": latency
        }
    )
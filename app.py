import streamlit as st
import requests
import os
from PIL import Image
import time

# App config
st.set_page_config(page_title="Luma - SilverStay Complex Case Assistant", page_icon="🏥", layout="wide")

# Sidebar and logo
with st.sidebar:
    st.image("ss_logo.jp2", width=200)  # Replace with your actual logo filename
    st.markdown("---")
    if st.button("New Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown("### About")
    st.markdown("Luma compresses time and keeps teams focused, like working alongside a master discharge planner who's seen 10,000 cases.")

# Example prompt buttons
st.subheader("Example questions:")
examples = [
    "60 y/o woman with advanced dementia, no family, facility won’t take her back, Medicaid pending. What should I do today?",
    "Patient is homeless, refuses SNF, has Medicaid, needs wound care. Any ideas for placement and next steps?",
]

cols = st.columns(3)
for i, query in enumerate(examples):
    if cols[i % 3].button(query):
        st.session_state.prefill = query

if "prefill" not in st.session_state:
    st.session_state.prefill = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask Luma about a complex case...") or st.session_state.prefill:
    if st.session_state.prefill:
        prompt = st.session_state.prefill
        st.session_state.prefill = ""

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        with st.spinner("Luma is thinking..."):

            url = "https://silverstay-langflow.predictionguard.com/api/v1/run/6f80b5ff-2b47-4d6c-a275-d2d1e190630c"
            api_key = os.environ.get("LANGFLOW_API_KEY")

            if not api_key:
                st.error("Missing LANGFLOW_API_KEY environment variable")
            else:
                headers = {"Content-Type": "application/json", "x-api-key": api_key}
                payload = {"input_value": prompt, "output_type": "chat", "input_type": "chat"}

                try:
                    r = requests.post(url, headers=headers, json=payload)
                    r.raise_for_status()
                    data = r.json()

                    # Helper to extract text
                    def find_text(d):
                        if isinstance(d, dict):
                            for k, v in d.items():
                                if k == "text" and isinstance(v, str):
                                    return v
                                else:
                                    result = find_text(v)
                                    if result:
                                        return result
                        elif isinstance(d, list):
                            for item in d:
                                result = find_text(item)
                                if result:
                                    return result
                        return None

                    response_text = find_text(data) or str(data)

                    display_text = ""
                    for word in response_text.split():
                        display_text += word + " "
                        placeholder.markdown(display_text + "▌")
                        time.sleep(0.04)
                    placeholder.markdown(response_text)

                    st.session_state.messages.append({"role": "assistant", "content": response_text})

                except Exception as e:
                    error_msg = f"Error: {e}"
                    placeholder.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
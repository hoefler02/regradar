import streamlit as st
from query_data import gen_rag_prompt
from get_llm_function import get_llm_function
from pathlib import Path
import base64
import os

def show_pdf(file_path, page):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

st.title(f":blue[RegRadar]")

client = get_llm_function()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me a question about the regulations! "):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    rag_prompt, sources = gen_rag_prompt(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.stream(
            input=rag_prompt,
        )
        response = st.write_stream(stream)
        st.write('Sources: ')
        for source in sources[:3]:
            sp, pg, chk = source.split(':')
            reg = sp.split('\\')[1]
            st.write(f':blue[{reg} PG {pg}]')
            #show_pdf(sp, pg)

    st.session_state.messages.append({"role": "assistant", "content": response})

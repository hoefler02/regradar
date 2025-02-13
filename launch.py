import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    .stApp {
        background-color: black
    }
    .stButton {text-align: center;}
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

#st.set_page_config(page_title="Welcome", page_icon="🚀", layout="centered")

with col2:
	st.image('usma.png',width=2000)

	if st.button("Enter RegRadar 🚀"):
	    st.switch_page('./pages/regradar.py')
import streamlit as st
import pandas as pd
from model_tools import RF_model

st.title("Emoji suggestion😊🌸")
st.write("""Input your boring text and watch my model add some spice to your words🥳😇🌈""")


text_input = st.text_input("Input your sentence here👇", "Good morning")


if st.button('submit sentence') or text_input:

    with st.spinner("Starting emoji prediction .."):
        output = RF_model(text_input)
        st.success(output)
        st.balloons()
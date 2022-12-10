import streamlit as st
import pandas as pd
#import

st.title("The emoji predictor😊🌸")
st.write("""Input your boring text and watch our Artificial Intelligence add some spice to your words🥳😇🌈""")

#st.write("""
#         
#         """)

text_input = st.text_input("Input your sentence here👇", "Good morning")


if st.button('submit sentence') or text_input:

    with st.spinner("Starting emoji prediction .."):
        #output = tag_text_sample(text_input)
        #st.success(output)
        st.balloons()
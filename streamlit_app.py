import streamlit as st
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

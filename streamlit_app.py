import streamlit as st
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

st.title("🎈 My dashboard")
st.write("Mi primera aplicacion web con Streamlit.")
st.subheader("Marco de datos del Titanic")
st.dataframe(titanic)
st.subheader("Visualizar grafico de barra")
st.write("La cantidad de personas por clase")
survival_counts = titanic['survived'].value_counts().sort_index()
st.bar_chart(survival_counts)

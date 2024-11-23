import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Nexus Squad",
    page_icon=":house:",
    layout="wide",
)

st.write("### Exploratory Data Analyst")
st.sidebar.warning("Created by Nexus Squad")

df = pd.read_csv('news.csv')

st.write("##### Dataframe Describe")
st.markdown(
    """
    Berikut ini adalah deskripsi dari dataset yang digunakan untuk membuat aplikasi ini :
"""
)
st.dataframe(df.describe())
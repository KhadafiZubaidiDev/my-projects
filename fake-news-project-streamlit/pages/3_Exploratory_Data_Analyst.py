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

st.write("##### Grafik Distribusi Label")
st.markdown(
    """
    Berikut ini adalah grafik distribusi dari kolom label :
"""
)
fig, ax = plt.subplots()
ax.set_title('Grafik Bar Distribusi Label')
ax.set_ylabel('Jumlah')
ax.set_xlabel('Label')
df['label'].value_counts().plot(kind='bar', ax=ax,color=['gold','mistyrose'])
st.pyplot(fig)

fig, ax = plt.subplots()
ax.set_title('Grafik Pie Distribusi Label')
df['label'].value_counts().plot(kind='pie', ax=ax, explode={0,0.1},labels=df['label'].value_counts().index,autopct='%1.1f%%',colors=['gold','mistyrose'],shadow=True,textprops={'size': 'smaller'})
st.pyplot(fig)
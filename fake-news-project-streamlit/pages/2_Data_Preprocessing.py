import streamlit as st
import pandas as pd
import io

st.set_page_config(
    page_title="Nexus Squad",
    page_icon=":house:",
    layout="wide",
)

st.write("### Data Preprocessing")
st.sidebar.warning("Created by Nexus Squad")

st.markdown(
    """
    Berikut ini adalah dataset yang digunakan untuk membuat aplikasi ini :
"""
)

df = pd.read_csv('news.csv')
st.dataframe(df, height=500)

st.write("##### Dataframe Head")
st.markdown(
    """
    Berikut ini adalah 5 (lima) data teratas dari dataset yang digunakan untuk membuat aplikasi ini :
"""
)
st.dataframe(df.head())

st.write("##### Dataframe Tail")
st.markdown(
    """
    Berikut ini adalah 5 (lima) data terbawah dari dataset yang digunakan untuk membuat aplikasi ini :
"""
)
st.dataframe(df.tail())

st.write("##### Dataframe Info")
st.markdown(
    """
    Berikut ini adalah struktur dari dataset yang digunakan untuk membuat aplikasi ini :
"""
)
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

st.write("##### Dataframe Shape")
st.markdown(
    """
    Berikut ini adalah jumlah baris dan kolom dari dataset yang digunakan untuk membuat aplikasi ini :
"""
)
st.dataframe(df.shape)

st.write("##### Dataframe Columns")
st.markdown(
    """
    Berikut ini adalah nama-nama kolom dari dataset yang digunakan untuk membuat aplikasi ini :
"""
)
st.dataframe(df.columns)

##st.write("##### Dataframe Dtypes")
##st.markdown(
##    """
##    Berikut ini adalah tipe data dari dataset yang digunakan untuk membuat aplikasi ini :
##"""
##)
##st.dataframe(df.dtypes)

st.write("##### Dataframe Value Counts")
st.markdown(
    """
    Berikut ini adalah nilai-nilai unik dari dataset yang digunakan untuk membuat aplikasi ini :
"""
)
st.dataframe(df.nunique())

st.write("##### Dataframe Missing Values")
st.markdown(
    """
    Berikut ini adalah jumlah missing values dari dataset yang digunakan untuk membuat aplikasi ini :
"""
)
st.dataframe(df.isnull().sum())

st.write("##### Dataframe Unique Values")
st.markdown(
    """
    Berikut ini adalah unique values dari dataset yang digunakan untuk membuat aplikasi ini :
"""
)
st.dataframe(df.nunique())

st.write("##### Label Count")
st.markdown(
    """
    Berikut ini adalah hasil penghitungan label dari dataset yang digunakan untuk membuat aplikasi ini :
"""
)
st.dataframe(df.label.value_counts())

st.write("##### Penambahan Label")

st.markdown(
    """
    Penambahan label pada dataset yang digunakan untuk membuat aplikasi ini ditujukan untuk mengidentifikasi label FAKE akan dianggap 0 dan REAL akan dianggap 1. Berikut adalah hasilnya :
"""
)
df['label_num'] = df['label'].map({'FAKE': 0, 'REAL': 1})
st.dataframe(df)

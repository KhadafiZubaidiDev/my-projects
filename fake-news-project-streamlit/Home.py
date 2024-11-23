import streamlit as st

st.set_page_config(
    page_title="Nexus Squad",
    page_icon=":house:",
    layout="wide",
)

st.write("# Fake News Detection")
st.sidebar.warning("Created by Nexus Squad")

st.markdown(
    """
    Selamat datang di Aplikasi Fake News Detection.
    Aplikasi ini disusun sebagai Final Project pada kelas Data Science & AI Fundamental Batch 42 yang diselenggarakan oleh DigitalSkola.
    ### Pengantar
    Sebagaimana yang diketahui bahwa era digital membawa dampak yang besar pada kehidupan manusia, mulai dari penyebaran informasi dan lain sebagainya. 
    Dari segi penyebaran informasi seperti kita ketahui bersama informasi dapat diakses dengan cepat dan mudah, baik untuk mencari materi pelajaran, jurnal ilmiah, maupun sumber belajar lainnya.
    Dengan penyebaran informasi yang begitu cepat dan masif, kita sebagai penerima informasi tersebut tidak sempat melakukan pengecekan terhadap informasi tersebut.
    Sehingga berpengaruh secara tidak langsung kepada keputusan yang diambil berdasarkan informasi tersebut.
    \n
    Untuk itu diperlukan suatu upaya untuk mengecek informasi tersebut apakah merupakan informasi asli atau bukan. 
    Salah satu cara untuk mengecek informasi tersebut adalah dengan menggunakan algoritma machine learning dengan menggunakan dataset yang telah disediakan.
    \n
    Akhirnya kami selaku penyusun mengucapkan terima kasih atas semua yang telah membantu kami dalam membuat aplikasi ini, terutama dari para mentor dan anggota tim yang telah membantu penyusunan aplikasi ini dari awal hingga akhir.
    Semoga aplikasi ini bermanfaat bagi kita semua. 
"""
)
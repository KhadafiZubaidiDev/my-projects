import streamlit as st
import spacy
import pickle

st.set_page_config(
    page_title="Nexus Squad",
    page_icon=":house:",
    layout="wide",
)

st.write("### Tes Model 1")
st.sidebar.warning("Created by Nexus Squad")

st.markdown(
    """
    Setelah dilakukan modeling, langkah selanjutnya adalah menggunakan model yang telah ditentukan untuk melakukan prediksi.
    Pada tes model pertama ini, kami menggunakan model Logostic Regression.
    Silahkan masukkan berita yang ingin Anda prediksi pada kolom teks di bawah ini. Kemudian tekan tombol "Prediksi" untuk melihat hasil prediksi.
"""
)

# Load the saved model
with open('logistic_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the spacy model
nlp = spacy.load('en_core_web_sm')
def run_ml_app():

    # Get the news text from the user
    news_text = st.text_area("Masukkan teks berita di bawah ini :")
    
    if not news_text:
        st.warning("Masukkan teks berita terlebih dahulu.")
        return

    # Process the news text using spaCy
    doc = nlp(news_text)
    text_vec = doc.vector

    # Make prediction using the loaded model
    prediction = model.predict([text_vec])
    # Button to submit the news for prediction
    if st.button("Prediksi"):
        # Display the prediction
        if prediction[0] == 0:
            st.error("The news is **FAKE**.")
        elif prediction[0] == 1:
            st.success("The news is **REAL**.")

run_ml_app()
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import re
import string

st.set_page_config(
    page_title="Nexus Squad",
    page_icon=":house:",
    layout="wide",
)

st.write("### Modeling")
st.sidebar.warning("Created by Nexus Squad")

st.markdown(
    """
    Modeling dalam data science merujuk pada proses membangun representasi matematis atau statistik dari suatu fenomena atau sistem yang ingin dipahami atau diprediksi. 
    Ini adalah langkah kunci dalam analisis data yang bertujuan untuk menemukan pola, hubungan, atau struktur dalam data.
"""
)
st.markdown(
    """
    Tujuan utama modeling adalah untuk membuat prediksi atau klasifikasi berdasarkan data yang ada. 
    Misalnya, memprediksi harga rumah, mengklasifikasikan email sebagai spam atau tidak, atau menganalisis perilaku pelanggan.
    Adapun tujuan penggunaan modeling dalam aplikasi ini adalah untuk mengklasifikasikan berita sebagai fake news atau tidak.
"""
)

df = pd.read_csv('news.csv')
st.markdown(
    """
    Pada bagian Data Preprocessing, kita sudah melakukan penambahan label pada dataset yang digunakan untuk membuat aplikasi ini ditujukan untuk mengidentifikasi label FAKE akan dianggap 0 dan REAL akan dianggap 1 (label_num). Berikut adalah hasilnya :
"""
)
df['label_num'] = df['label'].map({'FAKE': 0, 'REAL': 1})
st.dataframe(df)
st.markdown(
    """
    Setelah dilakukan penambahan label, selanjutnya dibuatkan fungsi wordopts untuk melakukan preprocessing isi kolom teks pada dataset. 
    Setelah itu dilakukan pendefinisian dependen dan independen variabel. 
    Lalu dilakukan pembagian dataset menjadi train dan test. Kemudian dilakukan proses konversi teks ke vektor. Berikut beberapa model yang digunakan :
"""
)

def wordopts(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

df['text'] = df['text'].apply(wordopts)

x = df['text']
y = df['label_num']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)

st.write("#### Logistic Regression")
from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(xv_train,y_train)
pred_lr=LR.predict(xv_test)
LR.score(xv_test, y_test)    
st.write("Accuracy Score : ", accuracy_score(y_test, pred_lr))
st.write(classification_report(y_test, pred_lr))

st.write("#### Naive Bayes")
from sklearn.naive_bayes import MultinomialNB
NB = MultinomialNB()
NB.fit(xv_train,y_train)
pred_nb=NB.predict(xv_test)
NB.score(xv_test, y_test)
st.write("Accuracy Score : ", accuracy_score(y_test, pred_nb))
st.write(classification_report(y_test, pred_nb))

st.write("#### Decision Tree")
from sklearn.tree import DecisionTreeClassifier
DT = DecisionTreeClassifier()
DT.fit(xv_train,y_train)
pred_dt=DT.predict(xv_test)
DT.score(xv_test, y_test)
st.write("Accuracy Score : ", accuracy_score(y_test, pred_dt))
st.write(classification_report(y_test, pred_dt))

st.write("#### Random Forest")
from sklearn.ensemble import RandomForestClassifier
RF = RandomForestClassifier()
RF.fit(xv_train,y_train)
pred_rf=RF.predict(xv_test)
RF.score(xv_test, y_test)
st.write("Accuracy Score : ", accuracy_score(y_test, pred_rf))
st.write(classification_report(y_test, pred_rf))

st.write("#### K-Nearest Neighbors")
from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier()
KNN.fit(xv_train,y_train)
pred_knn=KNN.predict(xv_test)
KNN.score(xv_test, y_test)
st.write("Accuracy Score : ", accuracy_score(y_test, pred_knn))
st.write(classification_report(y_test, pred_knn))

st.write("#### Support Vector Machine")
from sklearn.svm import SVC
SVM = SVC()
SVM.fit(xv_train,y_train)
pred_svm=SVM.predict(xv_test)
SVM.score(xv_test, y_test)
st.write("Accuracy Score : ", accuracy_score(y_test, pred_svm))
st.write(classification_report(y_test, pred_svm))

st.write("#### Gradient Boosting")
from sklearn.ensemble import GradientBoostingClassifier
GB = GradientBoostingClassifier()
GB.fit(xv_train,y_train)
pred_gb=GB.predict(xv_test)
GB.score(xv_test, y_test)
st.write("Accuracy Score : ", accuracy_score(y_test, pred_gb))
st.write(classification_report(y_test, pred_gb))
import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

pi = pickle.load(open('sentiment_model.p', 'rb'))
tfidf_vectorizer = pi['vectorizer']
logreg = pi['logreg']

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+|\[.*?\]|[^a-zA-Z\s]+|\w*\d\w*', ' ', text)
    stop_words = set(stopwords.words("english"))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    text = ' '.join(filtered_words).strip()
    tokens = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    lem_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lem_tokens)

st.title("Sentiment Analysis App")

user_input = st.text_area("Enter a review:", "")

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        st.write("**Original input:**", user_input)
        processed_text = preprocess_text(user_input)
        st.write("**After preprocessing:**", processed_text)
        vec_input = tfidf_vectorizer.transform([processed_text])
        prediction = logreg.predict(vec_input)
        st.success(f"**Predicted Sentiment:** {prediction[0]}")

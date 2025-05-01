from flask import Flask, render_template, request
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    processed_text = ""
    if request.method == 'POST':
        review = request.form['review']
        processed_text = preprocess_text(review)
        vec = tfidf_vectorizer.transform([processed_text])
        prediction = logreg.predict(vec)
        sentiment = prediction[0]
    return render_template('index.html', sentiment=sentiment, processed=processed_text)

if __name__ == '__main__':
    app.run(debug=True)

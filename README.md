
# 🛍️ Amazon Product Review Sentiment Analyzer

This project analyzes customer reviews from Amazon products using Natural Language Processing (NLP) techniques. It classifies reviews into **Positive**, **Negative**, or **Neutral** sentiments and provides visual insights. The sentiment analysis logic is implemented in Python and is deployed via both **Streamlit** and **Flask** for web-based interaction.

## 🚀 Features

- Text cleaning and preprocessing (NLTK)
- Sentiment analysis using TextBlob
- Visual representation of sentiment distribution
- Export of results to CSV
- Interactive web app using Streamlit & Flask

---

## 📂 Project Structure

```
├── Amazon_Product_Sentiment_Analysis.ipynb  # Main notebook with sentiment logic
├── app.py                                   # Flask app (if applicable)
├── streamlit_app.py                         # Streamlit version
├── requirements.txt                         # Python dependencies
├── templates/                               # HTML templates (for Flask)
└── README.md
```

---

## 🧪 How It Works

1. **Preprocessing**: Clean the reviews by removing stop words, punctuation, etc.
2. **Sentiment Scoring**: Use `TextBlob` to calculate polarity and classify sentiment.
3. **Visualization**: Generate bar charts to show sentiment distribution.
4. **Export**: Results can be saved as a CSV file for further analysis.
5. **Web Interface**: Upload a review or a CSV file to get real-time predictions.

---

## 💻 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/amazon-sentiment-analysis.git
cd amazon-sentiment-analysis
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run Streamlit App**
```bash
streamlit run streamlit_app.py
```

4. **Or Run Flask App**
```bash
python app.py
```

---

## 🛠️ Technologies Used

- Python 🐍
- Pandas, Numpy
- NLTK, TextBlob
- Matplotlib, Seaborn, Scikit-learn
- Streamlit, Flask

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [NLTK](https://www.nltk.org/)
- Streamlit & Flask Communities

---


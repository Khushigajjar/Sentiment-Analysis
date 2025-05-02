
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
├── flask_app.py                             # Flask app
├── streamlit_app.py                         # Streamlit app
├── sentiment_model.p                        # model
├── requirements.txt                         # Python dependencies
├── templates/                               # HTML templates (for Flask)
└── README.md
```

---

## 🧪 How It Works

1. **Preprocessing**: Clean the reviews by removing stop words, punctuation, etc.
2. **Sentiment Scoring**: Use `TextBlob` to calculate polarity and classify sentiment.
5. **Web Interface**: Upload a review or a CSV file to get real-time predictions.

---


## 💻 Installation

1. **Clone the repository**  
   Clone the project from GitHub and navigate into the project directory.
   ```bash
   git clone https://github.com/Khushigajjar/Sentiment-Analysis.git
   cd amazon-sentiment-analysis
   ```

2. **Create and activate a virtual environment**  
   Set up a virtual environment to manage dependencies.

   - **Create virtual environment**  
     ```bash
     python -m venv venv
     ```

   - **Activate it:**

     - **Windows:**
       ```bash
       venv\Scripts\activate
       ```

     - **macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```

3. **Install dependencies**  
   Install all required packages using the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Streamlit App**  
   Launch the Streamlit web application.
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Or Run Flask App**  
   Launch the Flask web application.
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


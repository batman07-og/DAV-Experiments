"""
EXP NO 06 - Interactive Sentiment Analysis
Data Analysis and Visualization (DAV)

Demonstrates sentiment analysis using NLTK's VADER lexicon.
Provides an interactive CLI to analyze sentences in real-time.
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

nltk.download('vader_lexicon', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)


def run_analysis():
    sia = SentimentIntensityAnalyzer()
    stop_words = set(stopwords.words('english'))
    print("--- Interactive Text & Sentiment Analyzer ---\nType 'exit' to quit.\n")

    while True:
        user_text = input("Enter a sentence: ")
        if user_text.lower() == 'exit':
            break
        if not user_text.strip():
            continue

        scores = sia.polarity_scores(user_text)
        compound = scores['compound']
        sentiment = "POSITIVE" if compound >= 0.05 else ("NEGATIVE" if compound <= -0.05 else "NEUTRAL")

        tokens = word_tokenize(user_text.lower())
        keywords = [w for w in tokens if w.isalnum() and w not in stop_words]
        top_words = Counter(keywords).most_common(3)

        print(
            "-" * 30 +
            f"\nOVERALL SENTIMENT: {sentiment}\n"
            f"Confidence Score: {compound}\n"
            f"Top Keywords: {top_words}\n" +
            "-" * 30
        )


if __name__ == "__main__":
    run_analysis()

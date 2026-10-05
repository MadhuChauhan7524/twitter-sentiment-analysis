import nltk
import re
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("stopwords")
nltk.download("vader_lexicon")

stop_words = set(stopwords.words("english"))

sia = SentimentIntensityAnalyzer()

def clean_tweet(tweet):

    tweet = tweet.lower()

    tweet = re.sub(r"http\S+", "", tweet)

    tweet = re.sub(r"@\w+", "", tweet)

    tweet = re.sub(r"#\w+", "", tweet)

    tweet = re.sub(r"[^a-z\s]", "", tweet)

    tweet = " ".join(
        word for word in tweet.split()
        if word not in stop_words
    )

    return tweet


def analyze_sentiment(tweet):

    cleaned = clean_tweet(tweet)

    score = sia.polarity_scores(cleaned)["compound"]

    if score >= 0.05:
        return "Positive"

    elif score <= -0.05:
        return "Negative"

    else:
        return "Neutral"
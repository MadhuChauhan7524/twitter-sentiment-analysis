from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()
    text = data["text"]

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    score = int((polarity + 1) * 50)

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return jsonify({
        "sentiment": sentiment,
        "score": score
    })

if __name__ == "__main__":
    app.run(debug=True)
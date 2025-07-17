from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from textblob import TextBlob
import praw
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Reddit API config
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Simple sentiment classifier
def classify_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    topic = request.json.get('topic', '').strip()
    subreddits = request.json.get('subreddits', ['all'])

    if not topic:
        return jsonify({"error": "No topic provided"}), 400

    if isinstance(subreddits, str):
        subreddits = [s.strip() for s in subreddits.split(",") if s.strip()]

    sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}
    samples = {"positive": [], "negative": [], "neutral": []}

    for sub in subreddits:
        try:
            posts = reddit.subreddit(sub).search(topic, limit=20)
            for post in posts:
                text = f"{post.title} {post.selftext}"
                sentiment = classify_sentiment(text)
                sentiment_counts[sentiment] += 1
                if len(samples[sentiment]) < 3:
                    samples[sentiment].append({
                        "title": post.title,
                        "url": f"https://reddit.com{post.permalink}"
                    })
        except Exception as e:
            print(f"Error with subreddit '{sub}': {e}")
            continue

    return jsonify({
        "counts": sentiment_counts,
        "samples": samples
    })

if __name__ == "__main__":
    app.run(debug=True)

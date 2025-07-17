# 📊 TweetTrend Analyzer (Reddit Edition)

**TweetTrend Analyzer** is a lightweight web app that analyzes sentiment trends around a specific topic across one or more subreddits in real-time. It fetches relevant Reddit posts, classifies them as **positive**, **negative**, or **neutral**, and visualizes the results using an interactive pie chart. Ideal for journalists, marketers, trend researchers, or anyone curious about public opinion on Reddit.

---

## 🚀 Features

- 🔎 Topic search across any subreddit(s)
- 📊 Real-time sentiment analysis using `TextBlob`
- 🧠 Smart classification: positive / negative / neutral
- 📈 Beautiful pie chart visualization with Chart.js
- 🧵 Sample Reddit posts per sentiment with links
- 💻 Clean and responsive frontend with modern UI



## 🛠️ Tech Stack

- **Frontend**: HTML, CSS (custom), JavaScript
- **Backend**: Flask (Python), Flask-CORS
- **Sentiment Analysis**: TextBlob
- **Reddit API**: PRAW
- **Visualization**: Chart.js

---

## 🧪 How It Works

1. User enters a **topic** and optionally a list of **subreddits**.
2. Backend fetches matching posts using PRAW.
3. Each post’s text is analyzed using TextBlob for sentiment polarity.
4. Posts are grouped and visualized by sentiment.
5. Sample posts are displayed with links to their original threads.

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/tweettrend-analyzer.git
cd tweettrend-analyzer

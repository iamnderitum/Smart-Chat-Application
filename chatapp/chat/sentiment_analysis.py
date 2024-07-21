from transformers import pipeline

# Load pre-trained sentiment analysis Model.
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(message):
    result = sentiment_pipeline(message)
    return[0]
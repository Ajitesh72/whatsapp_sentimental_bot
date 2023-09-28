import sys
from textblob import TextBlob

def perform_sentiment_analysis(text):
    blob = TextBlob(text)

    # Perform sentiment analysis(polarity score)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    print(type(sentiment))
    return sentiment

if __name__ == "__main__":
    # Get the message content from Node.js as a command line argument
    message_content = sys.argv[1]

    # Perform sentiment analysis
    sentiment = perform_sentiment_analysis(message_content)

    print(sentiment)

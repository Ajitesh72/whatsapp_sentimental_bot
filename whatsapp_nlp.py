import sys
from textblob import TextBlob

def perform_sentiment_analysis(text):
    # Create a TextBlob object from the message content
    blob = TextBlob(text)

    # Perform sentiment analysis
    sentiment_score = blob.sentiment.polarity

    # Determine sentiment based on the polarity score
    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment

if __name__ == "__main__":
    # Get the message content from Node.js as a command line argument
    message_content = sys.argv[1]

    # Perform sentiment analysis
    sentiment = perform_sentiment_analysis(message_content)

    # Print the sentiment
    print(sentiment)

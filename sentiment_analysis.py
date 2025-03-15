from transformers import pipeline


def analyze_sentiment(text):
    # Initialize sentiment analysis pipeline
    sentiment_analyzer = pipeline("sentiment-analysis")

    # Analyze the text
    result = sentiment_analyzer(text)
    return result[0]


if __name__ == "__main__":
    # Example usage
    text = "I love working with Hugging Face transformers! They make NLP tasks so easy."
    result = analyze_sentiment(text)
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']}")
    print(f"Confidence Score: {result['score']:.4f}")

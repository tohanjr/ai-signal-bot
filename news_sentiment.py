from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def analyze_news(news_text):

    result = classifier(news_text)

    return result

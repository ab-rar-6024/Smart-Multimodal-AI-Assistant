from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased")

def detect_intent(text):
    result = classifier(text)
    return result[0]

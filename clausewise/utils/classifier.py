from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

LABELS = ["Non-Disclosure Agreement", "Lease Agreement", "Employment Contract", "Service Agreement", "Partnership Deed"]

def classify(text):
    text = text[:1000]
    result = classifier(text, LABELS)
    return result['labels'][0]
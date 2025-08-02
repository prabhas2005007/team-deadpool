from transformers import pipeline

ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)

def extract_entities(text):
    raw = ner_pipeline(text[:1000])
    entities = [{"word": ent["word"], "entity": ent["entity_group"], "score": round(ent["score"], 2)} for ent in raw]
    return entities
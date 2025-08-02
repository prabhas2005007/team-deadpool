from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")  # or flan-t5-large if downloaded

simplify_pipeline = load_model()

def simplify_clauses(clauses):
    simplified = []

    for clause in clauses:
        if len(clause.strip()) < 10:
            simplified.append("[Too short to simplify]")
            continue

        prompt = f"Simplify: {clause}"

        try:
            result = simplify_pipeline(prompt, max_length=150, do_sample=False)[0]["generated_text"].strip()
            simplified.append(result)
        except Exception as e:
            import traceback
            error_msg = ''.join(traceback.format_exception(None, e, e.__traceback__))
            print(f"[DEBUG] Error for clause: {clause}\n{error_msg}")
            simplified.append("[ERROR]")

    return simplified

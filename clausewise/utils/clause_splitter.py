import re

def split(text):
    clauses = re.split(r'\n\s*\d+[\.\)]|\n\s*[•*-]|\n(?=WHEREAS|NOW THEREFORE|THEREFORE|IN WITNESS)', text, flags=re.IGNORECASE)
    clauses = [cl.strip() for cl in clauses if len(cl.strip()) > 30]
    return clauses
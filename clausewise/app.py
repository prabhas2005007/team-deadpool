import streamlit as st
from PIL import Image
from utils import parser, clause_splitter, simplifier, ner, classifier

# ------------------------
# Page setup and style
# ------------------------
st.set_page_config(
    page_title="ClauseWise – Legal Simplifier",
    page_icon="📜",
    layout="wide"
)

st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        .stButton>button {
            background-color: #2e86de;
            color: white;
        }
        .stButton>button:hover {
            background-color: #1e6ab3;
        }
        .uploadedFileName {
            font-weight: bold;
            color: #34495e;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------
# Sidebar
# ------------------------
with st.sidebar:
    st.title("📂 Upload Document")
    st.markdown("Supported formats: PDF, DOCX, TXT")
    st.markdown("---")
    st.markdown("👨‍⚖️ *ClauseWise* uses Hugging Face models to:")
    st.markdown("- Simplify complex legal clauses")
    st.markdown("- Extract named entities")
    st.markdown("- Classify document type")

# ------------------------
# Main Title
# ------------------------
st.title("📜 ClauseWise – AI Legal Document Analyzer")
st.caption("Powered by Hugging Face + Streamlit")

# ------------------------
# File Upload
# ------------------------
uploaded_file = st.file_uploader("Upload a legal document", type=["pdf", "docx", "txt"])

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
    with st.spinner("📄 Extracting text..."):
        text = parser.extract_text(uploaded_file)
        clauses = clause_splitter.split(text)

    st.subheader("🧾 Original Clauses")
    for i, clause in enumerate(clauses):
        st.markdown(f"**Clause {i+1}:** {clause}")

    # ------------------------
    # Simplify Clauses Button
    # ------------------------
    if st.button("🔁 Simplify Clauses"):
        with st.spinner("🧠 Simplifying clauses..."):
            simplified = simplifier.simplify_clauses(clauses)

        st.subheader("🧠 Clause Comparison")
        for i, (orig, simp) in enumerate(zip(clauses, simplified)):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Clause {i+1} – Original**")
                st.markdown(orig)
            with col2:
                st.markdown(f"**Clause {i+1} – Simplified**")
                st.markdown(simp)

    # ------------------------
    # Named Entity Recognition
    # ------------------------
    if st.button("🔍 Extract Entities"):
        with st.spinner("🔎 Running NER..."):
            entities = ner.extract_entities(text)
        with st.expander("📑 Named Entities Found"):
            st.json(entities)

    # ------------------------
    # Document Type Classification
    # ------------------------
    if st.button("📂 Classify Document"):
        with st.spinner("🔬 Classifying document..."):
            doc_type = classifier.classify(text)
        st.success(f"Document Type: **{doc_type}**")

else:
    st.info("Upload a legal file to get started.")

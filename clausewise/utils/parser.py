import docx
import PyPDF2

def extract_text(file):
    if file.name.endswith('.pdf'):
        return extract_pdf_text(file)
    elif file.name.endswith('.docx'):
        return extract_docx_text(file)
    elif file.name.endswith('.txt'):
        return extract_txt_text(file)
    else:
        return "Unsupported file format."

def extract_pdf_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text.strip()

def extract_docx_text(file):
    doc = docx.Document(file)
    return '\n'.join([para.text for para in doc.paragraphs]).strip()

def extract_txt_text(file):
    return file.read().decode('utf-8').strip()
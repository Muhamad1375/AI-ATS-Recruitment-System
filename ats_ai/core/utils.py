import pdfplumber
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text

model = SentenceTransformer('all-MiniLM-L6-v2')


def ai_score(resume_text, job_description):
    if not resume_text or not job_description:
        return 0

    resume_vec = model.encode([resume_text])
    job_vec = model.encode([job_description])

    score = cosine_similarity(resume_vec, job_vec)[0][0]

    return round(score * 100)
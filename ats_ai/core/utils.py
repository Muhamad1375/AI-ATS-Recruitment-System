import pdfplumber
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

KNOWN_SKILLS = [
    "python",
    "django",
    "javascript",
    "typescript",
    "vue.js",
    "react",
    "angular",
    "git",
    "sql",
    "html",
    "css",
    "sass",
    "scss",
    "rest api",
    "docker",
    "aws",
    "kubernetes",
    "nuxt",
    "pinia",
    "vuetify",
]

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in KNOWN_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills

def analyze_skills(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    found = []
    missing = []

    for skill in job_skills:
        if skill in resume_skills:
            found.append(skill)
        else:
            missing.append(skill)

    return found, missing

def ai_score(resume_text, job_description):
    if not resume_text or not job_description:
        return 0

    resume_vec = model.encode([resume_text])
    job_vec = model.encode([job_description])

    score = cosine_similarity(resume_vec, job_vec)[0][0]

    return round(score * 100)


def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text

model = SentenceTransformer('all-MiniLM-L6-v2')



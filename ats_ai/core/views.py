from django.shortcuts import render, redirect
from .models import Candidate
from .utils import extract_text


JOB_KEYWORDS = [
    "python",
    "django",
    "javascript",
    "vue",
    "typescript",
    "rest api",
    "git",
    "sql",
    "html",
    "CSS3"
]

def calculate_score(text):
    if not text:
        return 0

    text = text.lower()

    score = 0
    for keyword in JOB_KEYWORDS:
        if keyword.lower() in text:
            score += 10

    return min(score, 100)


def upload_resume(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        file = request.FILES.get('resume')

        candidate = Candidate.objects.create(
            name=name,
            email=email,
            resume_file=file
        )

        # استخراج متن PDF
        file_path = candidate.resume_file.path
        text = extract_text(file_path)


        score = calculate_score(text)

        candidate.resume_text = text
        candidate.score = score
        candidate.save()
        print("========== RESUME TEXT ==========")
        print(text[:1000])
        print("==================================")

        return redirect('success')

    return render(request, 'upload.html')


def success(request):
    return render(request, 'success.html')
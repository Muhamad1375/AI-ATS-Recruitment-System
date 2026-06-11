from django.shortcuts import render, redirect
from .models import Candidate, Job
from .utils import extract_text



def calculate_score(text, job_description):
    if not text:
        return 0

    text = text.lower()
    job_description = job_description.lower()

    job_keywords = job_description.split()  # MVP ساده

    score = 0

    for keyword in job_keywords:
        if keyword in text:
            score += 5

    return min(score, 100)


def upload_resume(request):
    jobs = Job.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        job_id = request.POST.get('job')
        file = request.FILES.get('resume')
        job_id = request.POST.get('job')


        job = Job.objects.get(id=job_id)

        candidate = Candidate.objects.create(
            name=name,
            email=email,
            resume_file=file,
            job = job
        )

        file_path = candidate.resume_file.path
        text = extract_text(file_path)

        score = calculate_score(text, job.description)

        candidate.resume_text = text
        candidate.score = score
        candidate.save()

        return redirect('success')

    return render(request, 'upload.html', {'jobs': jobs})


def success(request):
    return render(request, 'success.html')

def dashboard(request):
    candidates = Candidate.objects.all().order_by('-score')
    return render(request, 'dashboard.html', {'candidates': candidates})

def analyze_skills(resume_text, job_description):
    resume_text = resume_text.lower()
    job_keywords = job_description.lower().split()

    found = []
    missing = []

    for keyword in job_keywords:
        if keyword in resume_text:
            found.append(keyword)
        else:
            missing.append(keyword)

    return found, missing

def candidate_detail(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)

    found, missing = analyze_skills(
        candidate.resume_text,
        candidate.job.description
    )

    context = {
        "candidate": candidate,
        "found": found,
        "missing": missing
    }

    return render(request, "candidate_detail.html", context)


from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Candidate(models.Model):
    job = models.ForeignKey(
    Job,
    on_delete=models.CASCADE,
    related_name='candidates',
    null=True,
    blank=True
)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    resume_file = models.FileField(upload_to='resumes/')
    resume_text = models.TextField(blank=True, null=True)

    score = models.IntegerField(default=0) 
     # نمره AI
    final_score = models.IntegerField(default=0)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or "Unknown Candidate"
    

from django.contrib import admin
from .models import Candidate, Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "job",
        "final_score",
        "status"
    )
    list_filter = ("status", "job")
    search_fields = ("name", "email")
    ordering = ("-final_score",)
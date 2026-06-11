from django.urls import path
from .views import upload_resume, success, dashboard, candidate_detail


urlpatterns = [
    path('', upload_resume, name='upload'),
    path('success/', success, name='success'),
    path('dashboard/', dashboard, name='dashboard'),
    path('candidate/<int:candidate_id>/',candidate_detail,name='candidate_detail'),


]
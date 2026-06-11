from django.urls import path
from .views import upload_resume, success

urlpatterns = [
    path('', upload_resume, name='upload'),
    path('success/', success, name='success'),
]
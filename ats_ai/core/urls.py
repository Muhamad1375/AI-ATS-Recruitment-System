from django.urls import path
from .views import upload_resume, success, dashboard

urlpatterns = [
    path('', upload_resume, name='upload'),
    path('success/', success, name='success'),
        path('dashboard/', dashboard, name='dashboard'),

]
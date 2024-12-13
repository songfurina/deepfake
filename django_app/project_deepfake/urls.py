"""project_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import about, index, predict_page, cuda_full, homepage

app_name = 'deepfake_project'
handler404 = views.handler404

urlpatterns = [
    path('', homepage, name='homepage'),
    path('home/', index, name='home'),
    path('about/', about, name='about'),
    path('predict/', predict_page, name='predict'),
    path('cuda_full/', cuda_full, name='cuda_full'),
]

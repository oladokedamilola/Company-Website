# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),


    path('blogs/', views.blogs, name='blogs'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),  # URL for individual blog post


]

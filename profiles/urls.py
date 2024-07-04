# profiles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('feed/', views.feed, name='feed'),
]

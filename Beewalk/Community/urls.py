# community/urls.py
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = 'community'



urlpatterns = [
    path('', views.community_home, name='home'),
    path('followers/', views.follower_list, name='follower_list'),
    path('following/', views.following_list, name='following_list'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


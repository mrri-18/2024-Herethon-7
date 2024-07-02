# musicarchive/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.archive_list, name='archive_list'),
    path('<int:archive_id>/', views.archive_detail, name='archive_detail'),
    path('', views.archive_home, name='archive_home'),
    path('list/', views.archive_list, name='archive_list'),
    path('<int:archive_id>/', views.archive_detail, name='archive_detail'),
]

# musicarchive/views.py

from django.shortcuts import render, get_object_or_404
from .models import MusicArchive

def archive_home(request):
    return render(request, 'musicarchive/archive_home.html')

def archive_list(request):
    archives = MusicArchive.objects.all()
    return render(request, 'musicarchive/archive_list.html', {'archives': archives})

def archive_detail(request, archive_id):
    archive = get_object_or_404(MusicArchive, pk=archive_id)
    return render(request, 'musicarchive/archive_detail.html', {'archive': archive})

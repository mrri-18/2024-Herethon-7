from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Certification, Record
from .serializers import WalkDataSerializer
from .forms import CertificationForm
from .forms import MusicArchiveForm
from musicarchive.models import MusicArchive
from django.contrib.auth.decorators import login_required
from Accountapp.models import Member 

class WalkDataViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = WalkDataSerializer

@login_required
def index(request):
    # Assuming 'created_at' is a DateTimeField in Record model
    latest_record = Record.objects.filter(user=request.user).latest('created_at')
    context = {
        'latest_record_id': latest_record.id if latest_record else None
    }
    return render(request, 'Countapp/index.html', context)

@login_required
def stop_tracking(request):
    latest_record = Record.objects.filter(user=request.user).latest('id')
    return redirect('upload_certification', record_id=latest_record.id if latest_record else None)

@login_required
def upload_certification(request, record_id):
    record = get_object_or_404(Record, pk=record_id)

    if request.method == 'POST':
        form = CertificationForm(request.POST, request.FILES)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.record = record
            certification.save()
            return redirect('upload_certification_and_archive')
    else:
        form = CertificationForm()

    # Calculate elapsed time in a readable format (hours, minutes, seconds)
    elapsed_seconds = record.msec / 1000
    hours = int(elapsed_seconds // 3600)
    minutes = int((elapsed_seconds % 3600) // 60)
    seconds = int(elapsed_seconds % 60)
    
    # HTML에 시, 분, 초 형식의 걸은 시간을 전달
    return render(request, 'Countapp/upload_certification.html', {
        'form': form,
        'record': record,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
    })

def format_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{int(hours)}:{int(minutes)}:{int(seconds)}"

def upload_success(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    return render(request, 'Countapp/upload_success.html', {'record': record})

@login_required
def upload_certification_and_archive(request):
    if request.method == 'POST':
        archive_form = MusicArchiveForm(request.POST, request.FILES)
        if archive_form.is_valid():
            archive = archive_form.save(commit=False)
            archive.user = request.user  # Associate with logged-in user
            archive.save()
            return redirect('upload_success')
    else:
        archive_form = MusicArchiveForm()

    return render(request, 'Countapp/upload_certification_and_archive.html', {
        'archive_form': archive_form,
    })

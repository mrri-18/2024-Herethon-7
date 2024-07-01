from django.shortcuts import render
from rest_framework import viewsets
from .models import Record
from .serializers import WalkDataSerializer

class WalkDataViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = WalkDataSerializer

def index(request):
    return render(request, 'Countapp/index.html')
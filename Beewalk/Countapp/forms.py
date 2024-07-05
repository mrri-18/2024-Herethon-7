# forms.py
from django import forms
from .models import Certification

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['walk_image']  # 업로드할 필드 지정

class ArchiveForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['archive_image', 'description']  # 업로드할 필드 지정

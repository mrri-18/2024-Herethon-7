from .models import Certification
from django import forms
class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['image', 'description']  # 업로드할 필드 지정 (예: 이미지 및 설명)
# forms.py
from django import forms
from .models import Certification

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['walk_image']  # 업로드할 필드 지정

class ArchiveForm(forms.ModelForm):
    description = forms.CharField(
        # max_length=14,
        widget=forms.TextInput(attrs={'placeholder': '내용을 입력해주세요. (14자 이내)'}),
    )
    class Meta:
        model = Certification
        fields = ['archive_image', 'description']  # 업로드할 필드 지정

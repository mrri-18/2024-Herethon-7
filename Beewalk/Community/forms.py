# community/forms.py
from django import forms
from Accountapp.models import Member

class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'email', 'profile_img']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

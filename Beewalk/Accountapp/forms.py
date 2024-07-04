from django import forms
from .models import Member

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ['username', 'email', 'password']
        
class LoginForm(forms.Form):
    email = forms.CharField(label='이메일')
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
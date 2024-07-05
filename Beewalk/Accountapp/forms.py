from django import forms
from .models import Member

class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(attrs={'placeholder': '아이디를 입력해주세요'})
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(attrs={'placeholder': '이메일을 입력해주세요'})
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요'})
    )
    checkpwd = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 한 번 더 입력해주세요'})
    )
    profile_img = forms.ImageField(
        label='프로필 이미지',
        required=False
    )

    class Meta:
        model = Member
        fields = ['username', 'email', 'password','profile_img']
class LoginForm(forms.Form):
    email = forms.CharField(
        label='아이디',
        widget=forms.EmailInput(attrs={'placeholder': '아이디를 입력해주세요'}))
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호를 입력해주세요'})
    )
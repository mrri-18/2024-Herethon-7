from django import forms
from Accountapp.models import Member

class MemberUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '아이디를 입력해주세요'})
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일을 입력해주세요'})
    )

    class Meta:
        model = Member
        fields = ['username', 'email', 'profile_img']
        widgets = {
            'profile_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

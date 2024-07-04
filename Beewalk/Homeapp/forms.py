from django import forms

class FollowForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput)

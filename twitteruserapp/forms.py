from django import forms
from twitteruserapp.models import CustomUser


class CustomUserForm(forms.Form):
	username = forms.CharField(max_length=50)
	display_name = forms.CharField(max_length=25)
	password = forms.CharField(widget=forms.PasswordInput)
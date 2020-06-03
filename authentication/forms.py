from django import forms

from twitteruser.models import TwitterUser
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    class Meta:
        model = TwitterUser
        fields = ['username', 'display_name', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

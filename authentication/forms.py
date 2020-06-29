from django import forms
from django.contrib.auth.forms import UserCreationForm
from twitteruser.models import TwitterUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    model = TwitterUser
    fields = (
        'username',
        'displayname',
        'password',
    )
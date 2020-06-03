from django import forms


class CustomUserForm(forms.Form):
	username = forms.CharField(max_length=50)
	display_name = forms.CharField(max_length=25)
	password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)



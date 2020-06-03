from django import forms

class AddTweetForm(forms.Forms):
    tweet = forms.CharField(max_length=140)







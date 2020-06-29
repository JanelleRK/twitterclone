from django.shortcuts import render, reverse, HttpResponseRedirect
from tweet.models import Tweet
from authentication.forms import LoginForm, SignUpForm
from twitteruser.models import TwitterUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request):
    tweets = Tweet.objects.all().order_by('-date')
    return render(request, 'index.html', {'tweets': tweets})


def signup(request):
    html = 'signupform.html'
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data['username'],
                displayname=data['displayname'],
                password=data['password'],

            )
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))
    form = SignUpForm()
    return render(request, html, {'form': form})


def login_view(request):
    html = 'loginform.html'
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username = data['username'],
                password = data['password']
                )
            if user:
                login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next' , reverse('homepage'))
                )
    form = LoginForm()
    return render(request, html, {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
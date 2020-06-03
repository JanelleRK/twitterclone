from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from authentication.forms import SignUpForm, LoginForm
from twitteruser.models import TwitterUser


# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password']
            )
        new_user.save()
        user=authenticate(request, username=['username'], password=['password'])
        if user:
            login(request, new_user)
        return HttpResponseRedirect(reverse, 'profile')

    form = SignUpForm()

    return render(request, 'genericform.html', {'form': form})



def login_view(request):
    html="loginform.html"

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('profile'))
            )

        form = LoginForm()

        return render(request, html, {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse, 'homepage')
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from twitteruserapp.models import CustomUser
from twitteruserapp.forms import CustomUserForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data['username'],
                display_name = data['display_name'],
                password=data['password']
            )
            user.set_password(raw_password=data['password'])
        user.save()
        user=authenticate(request, username=['username'], password=['password'])
        if user:
            login(request, user)
        return HttpResponseRedirect(reverse, 'homepage')

    else:

        form = CustomUserForm()

        return render(request, 'genericform.html', {'form': form})


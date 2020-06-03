from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from twitteruser.models import TwitterUser
from twitteruser.forms import TwitterUserForm
from tweet.models import Tweet

# Create your views here.
@login_required
def index(request):
    twitter_user_profile = TwitterUser.objects.all()
    tweets = Tweet.objects.all().order_by('-date')
    return render(request, 'index.html', {{'twitter_user_profile': twitter_user_profile, 'tweets': tweets}})



def signup_view(request):
    if request.method == "POST":
        form = TwitterUserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            new_user.set_password(raw_password=data['password'])
        new_user.save()
        user=authenticate(request, username=['username'], password=['password'])
        if user:
            login(request, user)
        return HttpResponseRedirect(reverse, 'profile')

    else:

        form = TwitterUserForm()

        return render(request, 'genericform.html', {'form': form})

@login_required
def follow_view(request, id):
    #https: // stackoverflow.com / questions / 6218175 / how - to - implement - followers - following - in -django
    #https: // stackoverflow.com / questions / 10602071 / following - users - like - twitter - in -django - how - would - you - do - it
    user_1 = request.user
    follow_user = TwitterUser.object.get(id=id)
    user_1.following.add(follow_user)
    user_1.save()
    return HttpResponseRedirect(reverse('profile', kwargs={'id':id}))


@login_required
def unfollow_view(request, id):
    user_1 = request.user
    follow_user = TwitterUser.object.get(id=id)
    user_1.following.remove(follow_user)
    user_1.save()
    return HttpResponseRedirect(reverse('profile', kwargs={'id': id}))


def profile_view(request, id):
    html = 'profileview.html'
    all_tweets = Tweet.objects.filter(id=id).order_by('-date')
    twitter_user_profile = TwitterUser.objects.get(id=id)
    following_list = twitter_user_profile.following.all()
    following_count = following_list.count()
    all_tweets_count = all_tweets.count()

    if request.user.isauthenticated:
        twitter_users_following = request.user.following.all()
        if twitter_user_profile in twitter_users_following:
            is_following = True
        else:
            is_following = False
        return render(request, html, {
            'all_tweets': all_tweets,
            'twitter_user_profile': twitter_user_profile,
            'following_count': following_count,
            'is_following': is_following,
            'all_tweets_count': all_tweets_count,
            'twitter_users_following': twitter_users_following
        })
    return render(request,html, {
        'all_tweets': all_tweets,
        'twitter_user_profile': twitter_user_profile,
        'following_count': following_count,
        'all_tweets_count': all_tweets_count
    })

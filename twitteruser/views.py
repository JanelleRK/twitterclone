from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification

# Create your views here.
@login_required
def index(request):
    html='index.html'
    following=request.user.following.all()
    tweets = Tweet.objects.filter(author__in=following).order_by('-date')
    notifications = Notification.objects.filter(user_notified=request.user)
    return render(request, html, {'tweets':tweets, 'notifications':notifications, 'following':following})


def follow_view(request, id):
    #https: // stackoverflow.com / questions / 6218175 / how - to - implement - followers - following - in -django
    #https: // stackoverflow.com / questions / 10602071 / following - users - like - twitter - in -django - how - would - you - do - it
    user = request.user
    follow_user = TwitterUser.objects.get(id=id)
    user.following.add(follow_user)
    user.save()
    return HttpResponseRedirect(reverse('profile', args=(id,)))


def unfollow_view(request, id):
    user = request.user
    unfollow_user = TwitterUser.objects.get(id=id)
    user.following.remove(unfollow_user)
    user.save()
    return HttpResponseRedirect(reverse('profile', args=(id,)))


def profile_view(request, id):
    tweets = Tweet.objects.filter(author=id)
    tweet_count = tweets.count()
    user = TwitterUser.objects.get(id=id)
    follow = user.following.all()
    follow_count = follow.count()
    if request.user.is_authenticated:
        followers = request.user.follow.all()
        if user in followers:
            is_following = True
        else:
            is_following = False
        return render(
            request,
            'profileview.html', {
                'tweets': tweets,
                'tweet_counts': tweet_count,
                'user': user,
                'follow_count': follow_count,
                'followers': followers,
                'is_following': is_following,
            })
    return render(
        request,
        'profileview.html', {
            'tweets': tweets,
            'tweet_count': tweet_count,
            'user': user,
            'follow_count': follow_count,
        })

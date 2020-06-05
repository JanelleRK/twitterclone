from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification

# Create your views here.
@login_required
#can't quite figure this out for displaying notifications
def index(request):
    twitter_user_profile = request.user
    tweets = Tweet.objects.all().order_by('-date')
    new_notifications = Notification.objects.filter(id=request.user.id)
    notifications_count = []
    for new_notification in new_notifications:
        if new_notification.read is False:
            notifications_count.append(new_notification)

    return render(request, 'index.html', {{'twitter_user_profile': twitter_user_profile, 'tweets': tweets, 'new_notifications':new_notifications}})


@login_required
def follow_view(request, id):
    #https: // stackoverflow.com / questions / 6218175 / how - to - implement - followers - following - in -django
    #https: // stackoverflow.com / questions / 10602071 / following - users - like - twitter - in -django - how - would - you - do - it

    follow_user = TwitterUser.objects.get(id=id)
    username = follow_user.username
    request_user = request.user
    request_user.following.add(follow_user)
    follow_user.save()
    return HttpResponseRedirect(reverse('profile', args=(username,)))


@login_required
def unfollow_view(request, id):
    unfollow_user = TwitterUser.objects.get(id=id)
    username = unfollow_user.username
    request_user = request.user
    request_user.following.add(unfollow_user)
    unfollow_user.save()
    return HttpResponseRedirect(reverse('profile', args=(username,)))


def profile_view(request, id):
    html = 'profileview.html'
    twitter_user_profile = TwitterUser.objects.get(username=username)
    tweets = Tweet.objects.filter(tweet_author=twitter_user_profile.id)
    tweets = tweets.order_by('-date')
    return render(request, html, {'twitter_user_profile': twitter_user_profile, 'tweets': tweets})

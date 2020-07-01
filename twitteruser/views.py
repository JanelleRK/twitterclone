from django.shortcuts import render, reverse, HttpResponseRedirect
from twitteruser.models import TwitterUser
from tweet.models import Tweet


# Create your views here.

def profile_view(request, id):
    tweets = Tweet.objects.filter(author=id)
    count_tweets = tweets.count()
    user = TwitterUser.objects.get(id=id)
    followers = user.followers.all()
    follower_count = followers.count()
    if request.user.is_authenticated:
        my_followers = request.user.followers.all()
        if user in my_followers:
            is_following = True
        else:
            is_following = False
        return render(
            request,
            'profileview.html', {
                'tweets': tweets,
                'count_tweets': count_tweets,
                'user': user,
                'follower_count': follower_count,
                'my_followers': my_followers,
                'is_following': is_following,
            })
    return render(
        request,
        'profileview.html', {
            'tweets': tweets,
            'count_tweets': count_tweets,
            'user': user,
            'follower_count': follower_count,
        })


def follow(request, id):
    user = request.user
    follow = TwitterUser.objects.get(id=id)
    user.followers.add(follow)
    user.save()
    return HttpResponseRedirect(reverse('profile', args={id, }))


def unfollow(request, id):
    user = request.user
    follow = TwitterUser.objects.get(id=id)
    user.followers.remove(follow)
    user.save()
    return HttpResponseRedirect(reverse('profile', args={id, }))
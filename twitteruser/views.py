from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import View
from twitteruser.models import TwitterUser
from tweet.models import Tweet


# Create your views here.

'''def profile_view(request, id):
    user = TwitterUser.objects.get(id=id)
    tweets = Tweet.objects.filter(author=user)
    logged_in_user = TwitterUser.objects.get(id=request.user.id)
    is_following = logged_in_user.following.filter(id=id).exists()
    return render(request, 'profileview.html', {
        'user': user,
        'tweets': tweets,
        'is_following': is_following
    })'''


class AltProfileView(View):
    def get(self, request, id):
        user = TwitterUser.objects.get(id=id)
        tweets = Tweet.objects.filter(author=user)
        logged_in_user = TwitterUser.objects.get(id=request.user.id)
        is_following = logged_in_user.following.filter(id=id).exists()
        return render(request, 'profileview.html', {
            'user': user,
            'tweets': tweets,
            'is_following': is_following
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
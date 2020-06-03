from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.forms import AddTweetForm
from tweet.models import Tweet

# Create your views here.
@login_required
def add_tweet(request,id):
    html = 'addtweet.html'
    tweets = Tweet.objects.all().order_by('-date')

    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.get(id=id)
            Tweet.objects.create(
                tweet=data['tweet'],
                tweet_author = user
            )
            return HttpResponseRedirect(reverse('homepage'))
#still need to add notifications?
    form = AddTweetForm()

    return render(request, html, {"form": form, 'tweets': tweets})


def tweet_view(request, id):
    html='tweetview.html'
    tweet = Tweet.objects.get(id=id)
    return render(request, html, {'tweet':tweet})
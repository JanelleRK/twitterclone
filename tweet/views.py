from django.shortcuts import render, reverse, HttpResponseRedirect
from tweet.forms import AddTweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser
import re
from notification.models import Notification


# Create your views here.
def notification_alert(tweet):
    mention_pattern = r'([@#][\w_-]+)'
    tag = re.match(mention_pattern, tweet.tweet)
    if tag:
        tagged_user = TwitterUser.objects.get(username=tag.group()[1:])
        Notification.objects.create(
            receiver=tagged_user,
            tweet=tweet
        )


def add_tweet(request):
    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.author = TwitterUser.objects.get(id=request.user.id)
            tweet.save()
            notification_alert(tweet)
        return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'addtweet.html', {'form': AddTweetForm()})



def tweet_detail(request, id):
    tweet = Tweet.objects.get(id=id)
    return render(request, 'tweetview.html', {'tweet': tweet})
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.forms import AddTweetForm
from tweet.models import Tweet
from notification.models import Notification

# Create your views here.
def add_tweet(request, id):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.get(id=id)
            users = TwitterUser.objects.all()
            tweet = Tweet.objects.create(
                tweet=data['tweet'],
                author=user
            )
            notification = re.findall(r'@(\w+)', data['tweet'])

            for user in notification:
                Notification.objects.create(
                    user_notified=TwitterUser.objects.get(username=user),
                    tweet=tweet,
                )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddTweetForm()
    return render(request, 'addtweet.html', {'form': form})


def tweet_view(request, id):
    tweet = Tweet.objects.get(id=id)
    return render(request, 'tweetview.html', {'tweet': tweet})
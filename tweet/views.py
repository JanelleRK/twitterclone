from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from notification.models import Notification
from tweet.forms import AddTweetForm
from tweet.models import Tweet

# Create your views here.
@login_required
def add_tweet(request,id):
    form = AddTweetForm()
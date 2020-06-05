from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser


# Create your models here.
class Notification(models.Model):
    user_notification = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    which_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    new_notification = models.BooleanField(default=False)




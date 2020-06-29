from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser


# Create your models here.
class Notification(models.Model):
    receiver = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    received = models.BooleanField(default=False)




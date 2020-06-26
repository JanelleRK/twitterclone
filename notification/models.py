from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser


# Create your models here.
class Notification(models.Model):
    user_notified = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    new_notifications = models.BooleanField(default=False)




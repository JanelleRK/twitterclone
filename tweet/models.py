from django.db import models
from twitteruser.models import TwitterUser
from django.utils import timezone

# Create your models here.
class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)


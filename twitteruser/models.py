from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class TwitterUser(AbstractUser):
    users_following = models.ManyToManyField('self', symmetrical=False)








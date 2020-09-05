from django.db import models
from twitteruser.models import MyUser
from tweet.models import Tweet

class Notification(models.Model):
    sender = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    notif_tweets = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    read = models.BooleanField(default=False) 

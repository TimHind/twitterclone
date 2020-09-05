from django.db import models
from twitteruser.models import MyUser

class Tweet(models.Model):
    description = models.CharField(max_length=140)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.author.username}"

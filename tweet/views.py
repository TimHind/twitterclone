from django.shortcuts import render, HttpResponseRedirect, reverse
from django.shortcuts import render
from tweet.models import Tweet
from tweet.forms import TweetForm
from twitteruser.models import MyUser
from notification.models import Notification
import re
from django.views.generic.base import View

def tweet_detail(request, post_id):
    my_tweet = Tweet.objects.filter(id=post_id).first()
    return render(request, "tweet_detail.html", {"tweet": my_tweet})

class TweetDetail(View):
    def get(self, request, post_id):
        my_tweet = Tweet.objects.filter(id=post_id).first()
        return render(request, "tweet_detail.html", {"tweet": my_tweet})

def tweet_form_view(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                description = data.get('description'),
                author = request.user
            )
            mentions = re.findall(r'@(\w+)', data.get('description'))
            if mentions:
                users = MyUser.objects.all()
                for mention in mentions:
                    matched_user = MyUser.objects.get(username=mention)
                    if matched_user:
                        Notification.objects.create(
                            sender=matched_user,
                            notif_tweets=new_tweet,
                        )
            return HttpResponseRedirect(reverse("home"))
    
    form = TweetForm()
    return render(request, "signup_form.html", {"form": form})


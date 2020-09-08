from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import MyUser
from tweet.models import Tweet
from twitteruser.forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):
    my_tweets =  Tweet.objects.filter(author__in=request.user.following.all()).order_by('-time')
    user_tweets = Tweet.objects.filter(author=request.user).order_by('-time')
    #current_user = MyUser.objects.filter(MyUser__following=myuser)
    return render(request, "index.html", {'my_tweets': my_tweets, "user_tweets": user_tweets})

class AltIndex(LoginRequiredMixin, View):
    def get(self, request):
        my_tweets =  Tweet.objects.filter(author__in=request.user.following.all()).order_by('-time')
        user_tweets = Tweet.objects.filter(author=request.user).order_by('-time')
        return render(request, "index.html", {'my_tweets': my_tweets, "user_tweets": user_tweets})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("home")))

    form = LoginForm()
    return render (request, "login_form.html", {"form": form} )

class AltLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render (request, "login_form.html", {"form": form} )
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("home")))
        return render (request, "login_form.html", {"form": form} )
            
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

def user_detail(request, user_username):
    current_user = MyUser.objects.filter(username=user_username).first()
    my_tweets = Tweet.objects.filter(author=current_user).order_by('-time')
    count = current_user.following.count()
    tweet_count = my_tweets.count()
    return render(request, "user_detail.html", {"user": current_user, "tweets": my_tweets, "count": count, 'tweet_count': tweet_count}) 

def signup_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(username=data.get("username"), password=data.get("password"))
            return HttpResponseRedirect(reverse("home"))
    
    form = LoginForm()
    return render(request, "signup_form.html", {"form": form})

def my_profile(request):
    my_tweets = Tweet.objects.filter(author=request.user).order_by('-time')
    return render(request, "my_profile.html", {'my_tweets': my_tweets})

class AltMyProfile(View):
    def get(self, request):
        my_tweets = Tweet.objects.filter(author=request.user).order_by('-time')
        return render(request, "my_profile.html", {'my_tweets': my_tweets})


def follow(request, pk):
    my_user = MyUser.objects.get(id=pk)
    request.user.following.add(my_user)
    #request.user.following.count() + 1
    my_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def unfollow(request, pk):
    my_user = MyUser.objects.get(id=pk)
    request.user.following.remove(my_user)
    #request.user.following.count() - 1
    my_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
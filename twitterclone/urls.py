"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser.views import index, logout_view, login_view, signup_view, user_detail, my_profile, follow, unfollow, AltIndex, AltLoginView, AltMyProfile
from tweet.views import tweet_form_view, tweet_detail, TweetDetail
from notification.views import notification_view

urlpatterns = [
    path('', index, name="home"),
    path('altindex', AltIndex.as_view(), name="home"),
    path('tweet/<int:post_id>/', tweet_detail ),
    path('alttweet/<int:post_id>/', TweetDetail.as_view()),
    path('myprofile/', my_profile ),
    path('altmyprofile/', AltMyProfile.as_view()),
    path('newtweet/', tweet_form_view),
    path('notifications/', notification_view),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('altlogin/', AltLoginView.as_view()),
    path('logout/', logout_view),
    path('signup/', signup_view, name="signupview"),
    path('<str:user_username>/', user_detail, name='profile'),
    path('follow/<int:pk>/', follow, name='follow'),
    path('unfollow/<int:pk>/', unfollow, name='unfollow'),

]

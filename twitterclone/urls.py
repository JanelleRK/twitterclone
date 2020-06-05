"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from twitteruser.views import index, profile_view, follow_view, unfollow_view
from tweet.views import add_tweet, tweet_view
from authentication.views import signup_view, login_view, logout_view
from notification.views import new_notifications


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('notifications/', new_notifications, name='notifications'),
    path('addtweet/<int:id>/', add_tweet, name='addtweet'),
    path('tweet/<int:id>/', tweet_view, name="tweet"),
    path('', index, name='homepage'),
    path('profile/<int:id>/', profile_view, name='profile'),
    path('follow/<int:id>/', follow_view, name='follow'),
    path('unfollow/<int:id>/', unfollow_view, name='unfollow')
]

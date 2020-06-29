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

from django.urls import path

from tweet.views import AltAddTweet, AltTweetDetail


urlpatterns = [
    #path('tweet_detail/<int:id>/', tweet_detail, name='tweet_detail'),
    path('tweet_detail/<int:id>/', AltTweetDetail.as_view(), name='tweet_detail'),
    path('add_tweet/', AltAddTweet.as_view(), name='add_tweet'),
    #path('add_tweet/', add_tweet, name='add_tweet'),
]
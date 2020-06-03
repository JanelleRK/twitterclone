from django.urls import path
from tweet import views

urlpatterns = [
    path('addtweet/<int:id>/', views.add_tweet, name='addtweet'),
    path('tweet/<int:id>/', views.tweet_view, name="tweet")
]

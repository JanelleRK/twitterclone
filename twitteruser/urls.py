
from django.urls import path
from twitteruser import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/<int:id>/', views.profile_view, name='profile'),
    path('follow/<int:id>/', views.follow_view, name='follow'),
    path('unfollow/<int:id>/', views.unfollow_view, name='unfollow')
]

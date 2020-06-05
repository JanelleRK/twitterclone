from django.contrib import admin
from django.urls import path
from notification import views

urlpatterns = [
    path('notifications/', views.Notification, name='notification')
]

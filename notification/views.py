from django.shortcuts import render
from .models import Notification
from twitteruser.models import TwitterUser


def notification(request):
    notifications = list(Notification.objects.filter(receiver=request.user))
    Notification.objects.filter(receiver=request.user).delete()
    users = TwitterUser.objects.all()

    return render(request, 'notifications.html', {'notifications': notifications, 'users': users})
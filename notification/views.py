from django.shortcuts import render
from notification.models import Notification
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def new_notifications(request):
    html = "notifications.html"
    user_notified = request.user
    notifications = Notification.objects.filter(user_notified=user_notified, new_notifications=False)
    for notification in notifications:
        notification.new_notifications = True
        notification.save()
    return render(request, html, {'notifications':notifications, 'user_notified':user_notified })
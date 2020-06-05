from django.shortcuts import render
from notification.models import Notification
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def NewNotifications(request):
    html = "notifications.html"
    user_notified = request.user
    new_notifications = Notification.objects.filter(user_notification=user_notified, new_notification=False)
    for notification in new_notifications:
        notification.new_notification = True
        notification.save()
    return render(request, html, {{'new_notifications':new_notifications, 'user_notified':user_notified}})
from django.shortcuts import render
from notification.models import Notification
from twitteruser.models import MyUser

def notification_view(request):
    notifications = Notification.objects.filter(sender=request.user)
    new_notifications= []
    for notification in notifications:
        if notification.read == False:
            new_notifications.append(notification.notif_tweets)
            notification.read = True
            notification.save()
    return render(request, 'notification_detail.html', {"new_notifications": new_notifications})

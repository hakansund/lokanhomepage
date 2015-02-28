from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from notifications.models import Subscription


message_body = """
En ny {} har skapats på lokan.org!

Direktlänk: http://www.lokan.org/{}

----------

Ändra dina notifikationer på http://www.lokan.org/notifications/
"""

events = {'activities': 'aktivitet', 'funding': 'projektbidragsansökan'}


@shared_task
def notify(event):
    recipients = Subscription.objects.filter(
        event=event).values_list('user__email', flat=True)
    subject = 'Ny {} på lokan.org!'.format(events[event])
    message = message_body.format(events[event], event)
    sender = settings.EMAIL_HOST_USER
    send_mail(subject, message, sender, recipients, fail_silently=False)

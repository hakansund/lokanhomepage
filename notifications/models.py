from django.db import models
from model_utils.models import TimeStampedModel
from django.conf import settings

EVENTS = (
        ('activities', 'activities'),
        ('funding', 'funding'),
    )


class Subscription(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    event = models.CharField(max_length=15, choices=EVENTS)

    def __str__(self):
        return '{} {}'.format(self.user, self.event)

    class Meta():
        unique_together = ("user", "event")

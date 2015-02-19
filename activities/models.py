from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel


class Activity(TimeStampedModel):
    created_by = models.ForeignKey(User, verbose_name="Arrangör")
    datetime = models.DateTimeField("Datum/Tid")
    activity = models.CharField("Aktivitet", max_length=30)
    place = models.CharField("Plats", max_length=30)
    notes = models.TextField("Extra info")

    def __str__(self):
        return '{} {}'.format(self.activity, self.datetime)

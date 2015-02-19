from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from members.models import Member
from model_utils.models import TimeStampedModel


class Project(TimeStampedModel):

    created_by = models.ForeignKey(User)
    applier = models.ForeignKey(Member, verbose_name="Ansökare")
    title = models.CharField("Titel", max_length=50)
    description = models.TextField("Beskrivning")
    amount = models.IntegerField("Önskad summa")
    year = models.SmallIntegerField("Verksamhetsår", null=True)

    def positive_votes(self):
        return Vote.objects.filter(project=self.id, positive=True).count()

    def negative_votes(self):
        return Vote.objects.filter(project=self.id, positive=False).count()

    def is_approved(self):
        return self.positive_votes() >= 3

    def is_denied(self):
        return self.negative_votes() >= 3

    def has_voted(self):
        return Vote.objects.filter(
            project=self.id).values_list('user', flat=True)

    def get_absolute_url(self):
        return reverse('funding:list')

    def __str__(self):
        return '{}'.format(self.title)


class Vote(TimeStampedModel):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    positive = models.BooleanField(default=False)

    class Meta():
        unique_together = ("project", "user")

    def get_absolute_url(self):
        return reverse('funding:list')

    def __str__(self):
        return '{} {} {}'.format(self.project, self.user, self.positive)
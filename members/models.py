from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from model_utils.models import TimeStampedModel

YEARS = (
        (2014, 2014),
        (2015, 2015),
        (2016, 2016),
    )


class Member(TimeStampedModel):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    user_profile = models.OneToOneField(settings.AUTH_USER_MODEL, null=True,
        blank=True)

    def boardmember_years(self):
        return Boardmember.objects.filter(
            member=self.id).values_list('year', flat=True)

    def get_absolute_url(self):
        return reverse('members:list')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Membership(TimeStampedModel):

    member = models.ForeignKey(Member)
    year = models.SmallIntegerField(choices=YEARS)

    def __str__(self):
        return '{} {}'.format(self.member, self.year)

    class Meta():
        unique_together = ("member", "year")


class Boardmember(TimeStampedModel):

    TITLES = (
        ('Ordförande', 'Ordförande'),
        ('Kassör', 'Kassör'),
        ('Sekreterare', 'Sekreterare'),
        ('Ledamot', 'Ledamot'),
    )
    member = models.ForeignKey(Member)
    year = models.SmallIntegerField(choices=YEARS)
    title = models.CharField(max_length=15, choices=TITLES)

    def __str__(self):
        return '{} {} {}'.format(self.title, self.member, self.year)

    class Meta():
        unique_together = ("member", "year")

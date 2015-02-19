from django.contrib import admin

from funding.models import Project, Vote

admin.site.register(Project)
admin.site.register(Vote)

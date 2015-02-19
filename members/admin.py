from django.contrib import admin

from members.models import Member, Membership, Boardmember

admin.site.register(Member)
admin.site.register(Membership)
admin.site.register(Boardmember)
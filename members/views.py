from django.views.generic import ListView, TemplateView
from django.conf import settings
from .models import Member
from lokanhomepage.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'members/member_index.html'


class ListView(LoginRequiredMixin, ListView):
    model = Member

    def get_queryset(self):
        return Member.objects.filter(
            membership__year=settings.BUSINESS_YEAR).order_by('last_name')

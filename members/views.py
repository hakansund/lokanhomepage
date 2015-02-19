from django.views.generic import ListView, TemplateView
from .models import Member
from lokanhomepage.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'members/member_index.html'


class ListView(LoginRequiredMixin, ListView):
    model = Member
    queryset = Member.objects.all().order_by('id')

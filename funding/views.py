from django.views.generic import ListView, CreateView
from django.conf import settings
from .models import Project, Vote
from braces.views import LoginRequiredMixin
from lokanhomepage.mixins import MayVoteMixin
from notifications.tasks import notify
from .forms import VoteForm
from members.models import Member
from django.contrib.auth.mixins import PermissionRequiredMixin


class ListView(LoginRequiredMixin, ListView):
    model = Project


class CreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['applier', 'amount', 'title', 'description']

    def get_initial(self):
        initial = super(CreateView, self).get_initial()
        try:
            initial['applier'] = Member.objects.get(
                user_profile=self.request.user)
        except:
            pass
        return initial

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.year = settings.BUSINESS_YEAR
        notify.delay('funding')
        return super(CreateView, self).form_valid(form)


class VoteView(PermissionRequiredMixin, CreateView):
    model = Vote
    form_class = VoteForm
    permission_required = 'funding.can_vote'

    def get_context_data(self, **kwargs):
        context = super(VoteView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = Project.objects.get(pk=self.kwargs['pk'])
        return super(VoteView, self).form_valid(form)

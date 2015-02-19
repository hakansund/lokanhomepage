from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.utils import timezone

from .models import Activity
from lokanhomepage.mixins import LoginRequiredMixin


class ListUpcomingView(ListView):
    model = Activity

    def get_queryset(self):
        return Activity.objects.filter(
        datetime__gte=timezone.now()).order_by('datetime')

    def get_context_data(self, **kwargs):
        context = super(ListUpcomingView, self).get_context_data(**kwargs)
        context['upcoming'] = True
        return context


class ListOldView(ListView):
    model = Activity

    def get_queryset(self):
        return Activity.objects.filter(
        datetime__lte=timezone.now()).order_by('-datetime')


class CreateView(LoginRequiredMixin, CreateView):
    model = Activity
    fields = ['datetime', 'place', 'activity', 'notes']
    success_url = reverse_lazy('activities:upcominglist')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CreateView, self).form_valid(form)


class UpdateView(LoginRequiredMixin, UpdateView):
    model = Activity
    fields = ['created_by', 'datetime', 'activity', 'place', 'notes']
    success_url = reverse_lazy('activities:upcominglist')

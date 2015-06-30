from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.db import IntegrityError
from braces.views import LoginRequiredMixin
from .models import Subscription, EVENTS
from .forms import SubscriptionForm


class FormView(LoginRequiredMixin, FormView):
    template_name = 'notifications/subscription_form.html'
    form_class = SubscriptionForm
    success_url = reverse_lazy('notifications:index')

    def subscriptions(self):
        return Subscription.objects.filter(user=self.request.user)

    def get_initial(self):
        initial_values = {}
        subscriptions = Subscription.objects.filter(
            user=self.request.user).values_list('event', flat=True)
        for event in EVENTS:
            if event[0] in subscriptions:
                initial_values[event[0]] = True
        return initial_values

    def form_valid(self, form):
        for event in EVENTS:
            if form.cleaned_data[event[0]]:
                try:
                    Subscription.objects.create(
                        user=self.request.user, event=event[0])
                except IntegrityError:
                    pass
            else:
                Subscription.objects.filter(
                    user=self.request.user, event=event[0]).delete()

        return super(FormView, self).form_valid(form)

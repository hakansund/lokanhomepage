from django.conf.urls import url

from .views import FormView

urlpatterns = [
    url(r'^$', FormView.as_view(), name='index'),
]

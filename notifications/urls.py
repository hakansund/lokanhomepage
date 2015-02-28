from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.FormView.as_view(), name='index'),
)

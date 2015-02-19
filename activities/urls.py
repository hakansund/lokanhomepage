from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.ListUpcomingView.as_view(), name='upcominglist'),
    url(r'^old/$', views.ListOldView.as_view(), name='oldlist'),
    url(r'^add/$', views.CreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.UpdateView.as_view(), name='edit'),
)
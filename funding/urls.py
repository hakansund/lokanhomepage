from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListView.as_view(), name='list'),
    url(r'add/$', views.CreateView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/vote/$', views.VoteView.as_view(), name='vote'),
]

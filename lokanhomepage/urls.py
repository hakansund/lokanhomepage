from django.conf.urls import patterns, include, url

from django.contrib import admin

from . import views
admin.autodiscover()

urlpatterns = [
    # Authentication
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_change/', 'django.contrib.auth.views.password_change',
         name='password_change'),
    url(r'^password_change_done/',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'),
    # Apps
    url(r'^activities/', include('activities.urls', namespace='activities')),
    url(r'^members/', include('members.urls', namespace='members')),
    url(r'^funding/', include('funding.urls', namespace='funding')),
    url(r'^notifications/', include('notifications.urls', namespace='notifications')),
    # Other
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/defender/', include('defender.urls')),
    url(r'^about/', views.AboutView.as_view(), name='about'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]

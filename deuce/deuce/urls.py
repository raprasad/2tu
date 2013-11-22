from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deuce.views.home', name='home'),
    # url(r'^deuce/', include('deuce.foo.urls')),
    url(r'^deuce/$', 'location.views.view_location_list'),
    #url(r'^deuce/(?P<location_id>\d+)/$', 'location.views.detail'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

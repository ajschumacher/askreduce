from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^shufflesort/', include('shufflesort.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('shufflesort.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

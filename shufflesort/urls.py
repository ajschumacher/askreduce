from django.conf.urls import patterns, url

from shufflesort import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<question_id>\d+)$', views.question, name='question'),
)

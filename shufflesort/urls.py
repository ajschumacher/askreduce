from django.conf.urls import patterns, url

from shufflesort import views


urlpatterns = patterns('',
    url(r'^$',
        views.IndexView.as_view(),
        name='index'),
    url(r'^identity$',
        views.IdentityView.as_view(),
        name='identity'),
    url(r'^question/(?P<question_id>\d+)/$',
        views.QuestionView.as_view(),
        name='question'),
    url(r'^user/(?P<user_name>.+)/$',
        views.UserView.as_view(),
        name='user'),
)

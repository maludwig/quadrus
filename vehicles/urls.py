from django.conf.urls import patterns, url

from vehicles import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^.json$', views.index_json, name='index_json'),
)
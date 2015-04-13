from django.conf.urls import patterns, url

from vehicles import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^json/?$', views.index_json, name='index_json'),
    url(r'^orders/?$', views.orders, name='orders'),
    url(r'^json/orders/?$', views.orders_json, name='orders_json'),
    url(r'^orders/fill/(?P<pk>\d+)/?$', views.fill, name='fill'),
    url(r'^buy/(?P<pk>\d+)/?$', views.buy, name='buy'),
)
from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from vehicles import views

urlpatterns = patterns('',
    url(r'^$', cache_page(60*1)(views.IndexView.as_view()), name='index'),
    url(r'^json/?$', cache_page(60*1)(views.index_json), name='index_json'),
    url(r'^orders/?$', views.orders, name='orders'),
    url(r'^json/orders/?$', views.orders_json, name='orders_json'),
    url(r'^orders/fill/(?P<pk>\d+)/?$', views.fill, name='fill'),
    url(r'^json/orders/fill/(?P<pk>\d+)/?$', views.fill_json, name='fill_json'),
    url(r'^buy/(?P<pk>\d+)/?$', views.buy, name='buy'),
    url(r'^json/buy/(?P<pk>\d+)/?$', views.buy_json, name='buy_json'),
)

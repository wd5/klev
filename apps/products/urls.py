# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from apps.products.views import *


urlpatterns = patterns('',
    #(r'^$', countries_view),
    (r'^search/$',search_view),
    (r'^get_categories/$',get_categories),
    (r'^get_products/$',get_products),
    (r'^section/(?P<section_alias>[^/]+)/$',catalog_view),
    (r'^section/(?P<section_alias>[^/]+)/(?P<category_alias>[^/]+)/$',catalog_view),
    (r'^product/(?P<product_id>\d+)/$',product_view),





)

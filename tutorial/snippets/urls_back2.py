#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2016/12/13

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework import renderers


snippet_list = views.SnippetViewSet.as_view({
    "get": "list",
    "post": "create",
})

snippet_detail = views.SnippetViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

snippet_highlight = views.SnippetViewSet.as_view({
    "get": "highlight"
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = views.UserViewSet.as_view({
    "get": "list",
})

user_detail = views.UserViewSet.as_view({
    "get": "retrieve",
})


urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^snippets/$', snippet_list, name="snippet-list"),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name="snippet-detail"),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name="snippet-highlight"),
    url(r'^users/$', user_list, name="user-list"),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name="user-detail"),
])

urlpatterns += [
    url(r'^api-auth/', include("rest_framework.urls", namespace="rest_framework")),
]

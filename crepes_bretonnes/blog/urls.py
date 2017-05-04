from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.bloghome),
    url(r'^date/$', views.date_actuelle),
    url(r'^article/(?P<article_id>\d+)$', views.view_article),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_articles),
    url(r'^articles/(?P<month>\d{2})/(?P<year>\d{4})$', views.list_articles),
]

from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.blog_home, name="blog_home"),
    url(r'^date/$', views.date),
    url(r'^post/(?P<post_id>\d+)$', views.view_post, name="view_post"),
    url(r'^posts/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_posts, name="list_posts"),
    url(r'^posts/(?P<month>\d{2})/(?P<year>\d{4})$', views.redirect_list_posts, name="redirect_to_list_posts"),
]

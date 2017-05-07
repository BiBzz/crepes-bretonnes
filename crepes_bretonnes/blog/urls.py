from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.bloghome),
    url(r'^date/$', views.date_actuelle),
    url(r'^post/(?P<post_id>\d+)$', views.view_post, name="afficher_article"),
    url(r'^posts/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_posts, name="lister_articles"),
    url(r'^posts/(?P<month>\d{2})/(?P<year>\d{4})$', views.redirect_list_posts, name="Rediriger_listes_articles"),
]

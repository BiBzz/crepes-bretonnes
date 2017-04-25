from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.bloghome),
    url(r'date/$', views.date_actuelle),
]

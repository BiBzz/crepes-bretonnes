from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^accueil/$', views.home),
    url(r'date/$', views.date_actuelle),
]

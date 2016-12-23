from django.conf.urls import url
from gitget import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^poo/$', views.poo, name='poo'),
    url(r'^profile/$', views.profile, name='profile'),
]

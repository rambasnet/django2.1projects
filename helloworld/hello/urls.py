from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^bye/$', views.bye, name='bye'),
    re_path(r'^time/$', views.current_datetime, name='time'),
    re_path(r'^logout/$', views.logout, name='logout')
]

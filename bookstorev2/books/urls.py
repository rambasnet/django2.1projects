from django.conf.urls import re_path
from . import views

#app_name = 'books'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.book_list, name='books'),
    re_path(r'^deals/$', views.deals, name='deals'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.book_detail, 
        name='book_detail'),
    re_path(r'^subscribe/', views.subscribe, name='subscribe'),
    re_path(r'^login', views.login, name='login'),
    re_path(r'^logout/', views.logout, name='logout'),
    re_path(r'^signup/', views.signup, name='signup'),
    re_path(r'^dashboard/', views.dashboard, name='dashboard'),
    re_path(r'^account/', views.account, name='account'),
    re_path(r'^search', views.search, name='search')
]
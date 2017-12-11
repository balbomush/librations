from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.names, name='names'),
    url(r'^books$', views.book_list, name='book_list'),
    url(r'^book/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
    url(r'^book/new/$', views.book_new, name='book_new'),
    url(r'^book/(?P<pk>\d+)/edit/$', views.book_edit, name='book_edit'),

]

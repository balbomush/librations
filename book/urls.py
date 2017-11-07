from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.names, name='names'),
    url(r'^books', views.book_list, name='book_list'),
]

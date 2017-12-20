from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.main, name='main'),
    url(r'^Достоевский$',views.Dostoevsky, name='Dostoevsky'),
    url(r'^Гоголь$',views.Gogol, name='Gogol'),
    url(r'^Лавкрафт$',views.Lovecraft, name='Lovecraft'),
    url(r'^Чехов$',views.Chehov, name='Chehov'),
    url(r'^Кафка$',views.Kafka, name='Kafka'),
    url(r'^Гюго$',views.Gugo, name='Gugo'),
    url(r'^Хемингуэй$',views.Hemingway, name='Hemingway'),
    url(r'^Лермонтов$',views.Lermontov, name='Lermontov'),
    url(r'^Ремарк$',views.Remark, name='Remark'),
    url(r'^Гессе$',views.Gesse, name='Gesse'),
    url(r'^Горький$',views.Gork, name='Gork'),
    url(r'^Твен$',views.Twain, name='Twain'),
    url(r'^Азимов$',views.Asimov, name='Asimov'),
    url(r'^Пратчетт$',views.Pratchet, name='Pratchet'),
    url(r'^Брэдбери$',views.Bradbury, name='Bradbury'),
    url(r'^Буковски$',views.Bukowski, name='Bukowski'),
    url(r'^Грин$',views.Grin, name='Grin'),
    url(r'^Набоков$',views.Nabokov, name='Nabokov'),
    url(r'^Солженицын$',views.Soldj, name='Soldj'),
    url(r'^Кинг$',views.King, name='King'),
    url(r'^Бунин$',views.Bunin, name='Bunin'),
    url(r'^books$', views.book_list, name='book_list'),
    url(r'^book/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
    url(r'^book/new/$', views.book_new, name='book_new'),
    url(r'^book/(?P<pk>\d+)/edit/$', views.book_edit, name='book_edit'),

]

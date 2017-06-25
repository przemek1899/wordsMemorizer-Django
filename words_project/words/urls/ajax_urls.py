
from django.conf.urls import url
from words import views
from words import ajax

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^next_word', ajax.next_word, name='next_word'),
)

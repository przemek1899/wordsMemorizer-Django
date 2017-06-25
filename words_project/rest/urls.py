from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from rest.views import views_words
from rest.views import examination

urlpatterns = (
    # url(r'^expressions/$', views_words.ExpressionList.as_view()),
    url(r'^group_words/(?P<group_id>\d+)/$', views_words.get_group_expressions),
    url(r'^start_test/(?P<group_id>\d+)/$', examination.start_test),
    url(r'^get_next/$', examination.get_next),
)

urlpatterns = format_suffix_patterns(urlpatterns)

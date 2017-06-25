
from django.conf.urls import url
from words import views, views_examination

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^add_new_group$', views.add_new_group, name='add_new_group'),
    url(r'^groups_view', views.groups_view, name='groups_view'),
    url(r'^add_new_expression', views.add_new_expression, name='add_new_expression'),
    url(r'^see_group/(?P<group_id>\d+)/$', views.see_group, name='see_group'),
    url(r'^start_test/(?P<group_id>\d+)/$', views_examination.start_test_view, name='start_test'),
)

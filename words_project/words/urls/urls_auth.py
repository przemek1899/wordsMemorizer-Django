from django.conf.urls import url
from django.contrib.auth import views as auth_views

from words.auth_views import get_register_view, register_new_user

urlpatterns = [
               # url(r'^login/$', auth_views.login, {'template_name': 'words/auth/login.html'}, name='login'),
               url(r'^login/$', auth_views.LoginView.as_view(template_name='words/auth/login.html'), name='login'),
               url(r'^register/$', get_register_view, name='register'),
               url(r'^register_new_user/$', register_new_user, name='register_new_user'),
               url(r'^register/$', get_register_view, name='register'),
               url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
                # url(r'^admin/', admin.site.urls),
               # url(r'^logout/$', 'django.contrib.auth.views.logout'),

               # url(r'^login/$', views_main.login_wrapper, {'template_name': 'gabinet/usersMgr/login.html',
               #                                             'extra_context': {'is_demo': APP_TYPE_SETTING == APP_TYPE_DEMO}},
               #                                             name='login'),
               #
               # url(r'^logout/$', logout_mgr, name='logout'),
               ]

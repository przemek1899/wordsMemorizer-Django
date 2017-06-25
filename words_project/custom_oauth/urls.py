from __future__ import absolute_import
from django.conf.urls import url
from oauth2_provider import views

from . import views as custom_views


app_name = 'oauth2_provider'


base_urlpatterns = [
    url(r'^authorize/$', views.AuthorizationView.as_view(), name="authorize"),
    url(r'^token/$', views.TokenView.as_view(), name="token"),
    url(r'^revoke_token/$', views.RevokeTokenView.as_view(), name="revoke-token"),
]


management_urlpatterns = [
    # Application management views

    # Custom
    url(r'^applications/$', custom_views.CustomApplicationList.as_view(), name="list"),

    # Original oauth_provider
    url(r'^applications/register/$', views.ApplicationRegistration.as_view(), name="register"),
    url(r'^applications/(?P<pk>[\w-]+)/$', views.ApplicationDetail.as_view(), name="detail"),
    url(r'^applications/(?P<pk>[\w-]+)/delete/$', views.ApplicationDelete.as_view(), name="delete"),
    url(r'^applications/(?P<pk>[\w-]+)/update/$', views.ApplicationUpdate.as_view(), name="update"),
    # Token management views
    url(r'^authorized_tokens/$', views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
    url(r'^authorized_tokens/(?P<pk>[\w-]+)/delete/$', views.AuthorizedTokenDeleteView.as_view(),
        name="authorized-token-delete"),
]

urlpatterns = base_urlpatterns + management_urlpatterns

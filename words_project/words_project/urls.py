"""words_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

from words.urls.urls_auth import urlpatterns as auth_patterns
from rest.router_urls import router
from rest_framework.authtoken import views as authtoken_views
from words.views_dir.views_errors import handler400, handler403, handler404, handler500

urlpatterns = auth_patterns + [
    url(r'^admin/', admin.site.urls),
    url(r'^restapi/', include(router.urls)),
    url(r'^restapi/', include('rest.urls')),
    # url(r'^main/', include('words.urls.urls_auth', namespace="auth")),
    url(r'^main/', include('words.urls.urls', namespace="words")),
    url(r'^ajax/', include('words.urls.ajax_urls', namespace="ajax_words")),
    # url(r'^ocr/', include('ocr.urls', namespace="ocr")),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api-token-auth/', authtoken_views.obtain_auth_token),
    url(r'^o/', include('custom_oauth.urls', namespace='oauth2_provider')),
]
# handlers
handler400 = handler400
handler403 = handler403
handler404 = handler404
handler500 = handler500

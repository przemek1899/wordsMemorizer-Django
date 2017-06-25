# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from oauth2_provider.views.application import ApplicationOwnerIsUserMixin


class CustomApplicationOwnerIsUserMixin(ApplicationOwnerIsUserMixin):

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(CustomApplicationOwnerIsUserMixin, self).get(request, *args, **kwargs)
        raise PermissionDenied


class CustomApplicationList(CustomApplicationOwnerIsUserMixin, ListView):
    """
    List view for all the applications owned by the request.user
    """
    context_object_name = 'applications'
    template_name = "oauth2_provider/application_list.html"

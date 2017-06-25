
# -------------- LOGIN REQUIRED TO ALL SITE ------------------
from django.http import HttpResponseRedirect, JsonResponse
from django.conf import settings
from re import compile

from constants import URLS_NOT_AUTHENTICATED

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware(object):
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).

    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if not request.user.is_authenticated() and self.is_path_login_required(str(request.path)):
            return HttpResponseRedirect(settings.LOGIN_URL)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def is_path_login_required(self, path):
        path = path.lstrip('/')
        for p in URLS_NOT_AUTHENTICATED:
            if path.startswith(p):
                return False
        return True

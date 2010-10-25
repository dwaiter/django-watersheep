from django.conf import settings

from util import request_is_secure, redirect_secure


def secure_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.is_secure():
            if not request_is_secure(request):
                return redirect_secure(request)

        return view_func(request, *args, **kwargs)

    if getattr(settings, 'HTTPS_SUPPORT', True):
        return _wrapped_view_func
    else:
        return view_func


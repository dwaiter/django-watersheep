from django.conf import settings

from util import request_is_secure, request_requires_secure, redirect_secure, redirect_insecure


class SecureRequiredMiddleware(object):
    def __init__(self):
        self.paths = getattr(settings, 'SECURE_REQUIRED_PATHS')
        self.enabled = self.paths and getattr(settings, 'HTTPS_SUPPORT')

    def process_request(self, request):
        if self.enabled:
            if not request_is_secure(request):
                if request_requires_secure(request, self.paths):
                    return redirect_secure(request)

            if request_is_secure(request):
                if not request_requires_secure(request, self.paths):
                    return redirect_insecure(request)
        else:
            return None



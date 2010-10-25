from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect


def request_is_secure(request):
    return request.is_secure() or request.META.get('HTTP_X_FORWARDED_PROTOCOL') == 'https'


def path_requires_secure(request, paths):
    request_path = request.get_full_path()
    return any(request_path.startswith(path) for path in paths)

def request_requires_secure(request, paths):
    return path_requires_secure(request, paths) or request.user.is_authenticated()


def redirect_secure(request):
    request_url = request.build_absolute_uri(request.get_full_path())
    secure_url = request_url.replace('http://', 'https://')
    return HttpResponseRedirect(secure_url)

def redirect_insecure(request):
    request_url = request.build_absolute_uri(request.get_full_path())
    insecure_url = request_url.replace('https://', 'http://')
    return HttpResponsePermanentRedirect(insecure_url)


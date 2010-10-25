Based on http://djangosnippets.org/snippets/85/ with a few additional tweaks.

The watersheep middleware will look for a `SECURE_REQUIRED_PATHS` variable in
your `settings.py` and redirect any non-HTTPS requests for them to HTTPS
versions. Child paths of those paths will also be redirected.

Once a user is logged in, *all* non-HTTPS requests are redirected to HTTPS
versions to help prevent session-jacking.

There's also a decorator to let you mark specific views as HTTPS-only.

Requirements
------------

* Django 1.1+
* Pip, virtualenv, etc

Installation
------------

Install into your virtualenv with pip:

    pip install -e hg+http://bitbucket.org/dwaiter/django-watersheep#egg=watersheep

There's also a git mirror if you prefer:

    pip install -e git+http://github.com/dwaiter/django-watersheep#egg=watersheep

Usage
-----

Add the middleware to `MIDDLEWARE_CLASSES` *after* the authentication
middleware:

    MIDDLEWARE_CLASSES = (
        # ...
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        # ...
        'watersheep.middleware.SecureRequiredMiddleware',
        # ...
    )

Add the `SECURE_REQUIRED_PATHS` setting to define what URLs should be
HTTPS-only:

    SECURE_REQUIRED_PATHS = (
        '/login',
        '/logout',
        '/admin',
        # ...
    )

To use the decorator:

    from watersheep.decorator import secure_required

    # ...

    @secure_required
    def photo_edit(request, slug):
        # ...


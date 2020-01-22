from .base import *  # noqa

INSTALLED_APPS += ["django.contrib.staticfiles", "debug_toolbar"]  # noqa: F405
INTERNAL_IPS = ("127.0.0.1",)

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405

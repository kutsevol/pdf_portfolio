"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""
import logging

from debug_toolbar.settings import PANELS_DEFAULTS

from server.settings.components import config
from server.settings.components.common import (
    BASE_DIR,
    INSTALLED_APPS,
    MIDDLEWARE,
)

# Setting the development status:

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# Static files:
# https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-STATICFILES_DIRS

STATIC_ROOT = BASE_DIR.joinpath('staticfiles')

# Django debug toolbar
# django-debug-toolbar.readthedocs.io

DEV_INSTALLED_APPS = (
    'whitenoise.runserver_nostatic',
    'debug_toolbar',
    'nplusone.ext.django',
)

INSTALLED_APPS = DEV_INSTALLED_APPS + INSTALLED_APPS

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # https://github.com/bradmontgomery/django-querycount
    # Prints how many queries were executed, useful for the APIs.
    'querycount.middleware.QueryCountMiddleware',
)

# Workaround for django-debug-toolbar, use by default TESTING_MODE=False and we
# will show debug toolbar otherwise TESTING_MODE=True and don't show
TESTING_MODE = config('TESTING_MODE', cast=bool, default=False)


def custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return not TESTING_MODE


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK':
        'server.settings.environments.development.custom_show_toolbar',
}


DEBUG_TOOLBAR_PANELS = PANELS_DEFAULTS + [
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

# This will make debug toolbar to work with django-csp,
# since `ddt` loads some scripts from `ajax.googleapis.com`:
CSP_SCRIPT_SRC = ("'self'", "*.cloudflare.com", "ajax.googleapis.com")
CSP_IMG_SRC = ("'self'", "data:")


# nplusone
# https://github.com/jmcarp/nplusone

# Should be the first in line:
MIDDLEWARE = ('nplusone.ext.django.NPlusOneMiddleware',) + MIDDLEWARE

# Logging N+1 requests:
NPLUSONE_RAISE = False  # comment out if you want to allow N+1 requests
NPLUSONE_LOGGER = logging.getLogger('django')
NPLUSONE_LOG_LEVEL = logging.WARN

# Security
CSRF_COOKIE_HTTPONLY = False

# Axes
AXES_ENABLED = False

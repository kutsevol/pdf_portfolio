"""
This file contains all the settings used in production.

This file is required and if development.py is present these
values are overridden.
"""

from server.settings.components.common import BASE_DIR, config

# Production flags:

ALLOWED_HOSTS = [
    config('DOMAIN_NAME'),
]


# Staticfiles
# https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/

# Adding STATIC_ROOT to collect static files via 'collectstatic'
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# Mediafiles
MEDIA_ROOT = '/var/www/django/media'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

MIDD_NAME = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f'{MIDD_NAME}.UserAttributeSimilarityValidator',
    },
    {
        'NAME': f'{MIDD_NAME}.MinimumLengthValidator',
    },
    {
        'NAME': f'{MIDD_NAME}.CommonPasswordValidator',
    },
    {
        'NAME': f'{MIDD_NAME}.NumericPasswordValidator',
    },
]


# Security
# https://docs.djangoproject.com/en/1.11/topics/security/

SECURE_HSTS_SECONDS = 2592000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

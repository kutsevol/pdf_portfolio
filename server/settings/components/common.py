"""
Django settings for server project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their config, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from server.settings.components import BASE_DIR, config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

DEBUG = config('DEBUG', cast=bool, default=False)

SECRET_KEY = config('SECRET_KEY')

# Application definition:

INSTALLED_APPS = (
    # Your apps go here:
    'pdf_app',

    # Default django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Security:
    'axes',

    # External apps:
    'nested_inline',
)

MIDDLEWARE = (
    # Security:
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise:
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # Django:
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Content Security Policy:
    'csp.middleware.CSPMiddleware',

    # Referrer Policy:
    'django_referrer_policy.middleware.ReferrerPolicyMiddleware',

    # Feature Policy:
    'django_feature_policy.FeaturePolicyMiddleware',

    # Axes
    'axes.middleware.AxesMiddleware',
)

ROOT_URLCONF = 'server.urls'

WSGI_APPLICATION = 'server.wsgi.application'

ADMIN_URL = config('ADMIN_URL', default='admin/')
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        # Choices are: postgresql_psycopg2, mysql, sqlite3, oracle
        'ENGINE': config('DB_ENGINE'),

        # Database name or filepath if using 'sqlite3':
        'NAME': config('DB_NAME',
                       default=BASE_DIR.joinpath('db.sqlite3').as_posix()),

        # You don't need these settings if using 'sqlite3':
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASS'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
        'CONN_MAX_AGE': config('CONN_MAX_AGE', cast=int, default=60),
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

LANGUAGES = (
    ('en', 'English'),
)

LOCALE_PATHS = (
    'locale/',
)

USE_TZ = True
TIME_ZONE = 'UTC'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Templates
# https://docs.djangoproject.com/en/1.11/ref/templates/api

TEMPLATES = [{
    'APP_DIRS': True,
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        BASE_DIR.joinpath('templates'),
    ],
    'OPTIONS': {
        'context_processors': [
            # default template context processors
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.request',
        ],
    },

}]

# Media files
# Media-root is commonly changed in production
# (see development.py and production.py).

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')


# Django authentication system
# https://docs.djangoproject.com/en/1.11/topics/auth/

AUTHENTICATION_BACKENDS = (
    'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]


# Security
# https://docs.djangoproject.com/en/1.11/topics/security/

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'DENY'

# https://django-referrer-policy.readthedocs.io/
REFERRER_POLICY = 'no-referrer'

# https://github.com/adamchainz/django-feature-policy
FEATURE_POLICY = {
    'autoplay': 'none',
    'camera': 'none',
    'fullscreen': 'none',
    'geolocation': 'none',
    'microphone': 'none',
}

"""
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings

To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from split_settings.tools import include

from server.settings.components import config

base_settings = [
    'components/common.py',
    'components/logging.py',
    'components/security.py',
    'components/caches.py',

    # You can even use glob:
    # 'components/*.py'

    # Select the right env:
    'environments/{0}.py'.format(config('DJANGO_ENV', default='development')),

]

# Include settings:
include(*base_settings)

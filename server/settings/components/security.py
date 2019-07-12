"""
The file contains a different security politics
"""

# Security
# https://docs.djangoproject.com/en/2.2/topics/security/

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'DENY'

"""
https://developer.mozilla.org/ru/docs/Web/HTTP/Headers/Content-Security-Policy

Docs: https://github.com/mozilla/django-csp
"""

CSP_SCRIPT_SRC = ("'self'", '*.cloudflare.com',)
CSP_IMG_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'", 'fonts.googleapis.com', 'fonts.gstatic.com')
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
CSP_DEFAULT_SRC = ("'self'",)
CSP_EXCLUDE_URL_PREFIXES = ('/admin', '/pdf')

"""
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy

Docs: https://django-referrer-policy.readthedocs.io/
"""
REFERRER_POLICY = 'same-origin'

"""
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy

Docs: https://github.com/adamchainz/django-feature-policy
"""
FEATURE_POLICY = {
    'autoplay': 'none',
    'camera': 'none',
    'fullscreen': 'none',
    'geolocation': 'none',
    'microphone': 'none',
}

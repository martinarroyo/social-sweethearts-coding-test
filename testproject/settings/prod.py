from .base import *
import os

SECRET_KEY = os.environ['SOCIAL_SWEETHEARTS_SECRET_KEY']
os.environ['HTTPS'] = "on"
os.environ['wsgi.url_scheme'] = 'https'

DEBUG = False

ALLOWED_HOSTS = [
    'social-sweethearts-coding-test.martinarroyo.net',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, os.environ['SOCIAL_SWEETHEARTS_DB_CONF']),
        },
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

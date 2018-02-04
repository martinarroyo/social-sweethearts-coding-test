from .base import *
import os

SECRET_KEY = os.environ['SOCIAL_SWEETHEARTS_SECRET_KEY']

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

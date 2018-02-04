from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    'localhost:8000',
    'social-sweethearts-coding-test.martinarroyo.net',
    'social-sweethearts-coding-test.martinarroyo.net:8443',
    'social-sweethearts-coding-test.martinarroyo.net:8002',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = 'test'

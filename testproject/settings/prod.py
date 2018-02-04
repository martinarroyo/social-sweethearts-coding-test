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
            'read_default_file': os.environ['SOCIAL_SWEETHEARTS_DB_CONF'],
        },
    }
}

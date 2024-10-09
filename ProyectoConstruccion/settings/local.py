from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost','web-production-28f99.up.railway.app']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'verceldb',
        'USER': 'default',
        'PASSWORD': 'MTK0JQlBZ8Rb',
        'HOST': 'ep-rough-paper-a48t05iw-pooler.us-east-1.aws.neon.tech',  # Or the hostname/IP of your MySQL server
        'PORT': '5432'
    }
}

STATIC_URL = 'static/'


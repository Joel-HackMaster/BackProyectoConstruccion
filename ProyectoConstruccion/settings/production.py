from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djconstruccion',
        'USER': 'root',
        'PASSWORD': 'joel1502',
        'HOST': 'localhost',  # Or the hostname/IP of your MySQL server
        'PORT': '3306',  # Default MySQL port
    }
}

STATIC_URL = 'static/'
from .base import *

DEBUG = False
ALLOWED_HOSTS = ENV.get('ALLOWED_HOSTS', [])


# Static and Media files

MEDIA_ROOT = ENV.get('MEDIA_ROOT', '')
MEDIA_URL = ENV.get('MEDIA_URL', '')

STATIC_ROOT = ENV.get('STATIC_ROOT', '')
STATIC_URL = ENV.get('STATIC_URL', '')
ALLOWED_HOSTS = ENV.get('ALLOWED_HOSTS', '')

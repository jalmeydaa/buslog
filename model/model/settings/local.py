from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]


INSTALLED_APPS += ("debug_toolbar", )

# Static and Media files
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
)

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'

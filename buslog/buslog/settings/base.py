# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from unipath import Path
import os
from buslog.util import get_env

BASE_DIR = Path(__file__).ancestor(3)
ENV = get_env(BASE_DIR)

SECRET_KEY = ENV.get('SECRET_KEY')

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'sorl.thumbnail',
)

LOCAL_APPS = (
    'apps.tarjadas',
    'rest_framework',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ENV.get('DB_NAME', 'bbdd'),
        'USER': ENV.get('DB_USER'),
        'PASSWORD': ENV.get('DB_PASSWORD'),
        'HOST': ENV.get('DB_HOST'),
        'PORT': ENV.get('DB_PORT'),
        'CONN_MAX_AGE': None,
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'buslog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (BASE_DIR.child('templates'),),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.core.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    )

REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}



WSGI_APPLICATION = 'buslog.wsgi.application'


TIME_ZONE = 'America/Lima'
LANGUAGE_CODE = 'es-pe'

USE_I18N = True

USE_L10N = True

USE_TZ = True

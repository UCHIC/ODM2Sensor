"""
Django settings for ODM2Sensor project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, os.pardir)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


from ODM2Sensor.settings.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

ALLOWED_HOSTS = []

APPEND_SLASH = True

# Application definition

PREREQ_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

PROJECT_APPS = (
    'django.contrib.formtools',
    'sensordatainterface',
)

TEST_RUNNER = 'sensordatainterface.tests.custom_runner.init_schemas.SQLServerDiscoverRunner'

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ODM2Sensor.urls'

WSGI_APPLICATION = 'ODM2Sensor.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'odm2': {
        'ENGINE': ODM2_configs['ENGINE'],
        'NAME': ODM2_configs['NAME'],
        'USER': ODM2_configs['USER'],
        'PASSWORD': ODM2_configs['PASSWORD'],
        'HOST': ODM2_configs['HOST'],
        'PORT': ODM2_configs['PORT'],

        'OPTIONS': {
            'driver': ODM2_configs['OPTIONS']['driver'],
            'host_is_server': ODM2_configs['OPTIONS']['host_is_server'],
        },
        'TEST_DEPENDENCIES': []
    },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ODM2Sensor/Internal.sqlite3',
        'TEST_DEPENDENCIES': ['odm2']
    },
}

DATABASE_ROUTERS = ['sensordatainterface.routers.SensorDataInterfaceRouter', ]

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'OPTIONS': {
#             'context_processors': 'django.contrib.messages.context_processors.messages'
#         },
#     },
# ]


TEMPLATE_DIRS = [os.path.join(PROJECT_DIR, 'templates')]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# Deactivated since UTC Offset is handled in the database.
# See https://docs.djangoproject.com/en/dev/topics/i18n/timezones/ to use automatic time zones.
USE_TZ = False
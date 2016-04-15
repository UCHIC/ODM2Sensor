"""
Django settings for ODM2Sensor project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

data = {}
try:
    with open(os.path.join(BASE_DIR, 'settings', 'settings.json')) as data_file:
        data = json.load(data_file)
except IOError:
    print("You need to setup the settings data file (see instructions in base.py file.)")


try:
    SECRET_KEY = data["secret_key"]
except KeyError:
    print("The secret key is required in the settings.json file.")
    exit(1)

ALLOWED_HOSTS = []

APPEND_SLASH = True

DEPLOYED = False

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

DATABASES = {}
for database in data['databases']:
    DATABASES[database['name']] = {
        'ENGINE': database['engine'],
        'NAME': database['schema'],
        'USER': database['user'] if 'user' in database else '',
        'PASSWORD': database['password'] if 'password' in database else '',
        'HOST': database['host'] if 'host' in database else '',
        'PORT': database['port'] if 'port' in database else '',
        'OPTIONS': database['options'] if 'options' in database else ''
    }


DATABASE_ROUTERS = ['sensordatainterface.routers.SensorDataInterfaceRouter', ]

TEMPLATES = [
    {
        # 'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': 'django.template.context_processors.media'
        },
    },
]


TEMPLATE_DIRS = [os.path.join(BASE_DIR, os.pardir, 'templates')]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# Deactivated since UTC Offset is handled in the database.
# See https://docs.djangoproject.com/en/dev/topics/i18n/timezones/ to use automatic time zones.
USE_TZ = False

MEDIA_ROOT = data["media_files_dir"] if 'media_files_dir' in data else ''

MEDIA_URL = ''

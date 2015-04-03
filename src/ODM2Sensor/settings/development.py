from ODM2Sensor.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = True

SITE_URL = '/equipment/'

STATIC_ROOT = 'static/'
STATIC_URL = SITE_URL + 'static/'

LOGIN_REDIRECT_URL = SITE_URL + 'home/'
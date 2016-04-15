import django
from ODM2Sensor.settings.base import *

DEBUG = True
DEPLOYED = True

SITE_ROOT = os.environ['APPL_PHYSICAL_PATH']
SITE_URL = os.environ['APPL_VIRTUAL_PATH'] + '/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = SITE_URL + 'static/'

LOGIN_REDIRECT_URL = SITE_URL + 'home/'

MEDIA_URL = SITE_URL + 'media/'

django.setup()

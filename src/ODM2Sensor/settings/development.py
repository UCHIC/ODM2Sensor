from ODM2Sensor.settings.base import *

DATABASE_PATH = os.path.join(BASE_DIR, "Internal.sqlite3")
DATABASES['default']['NAME'] = DATABASE_PATH

DEBUG = True
TEMPLATE_DEBUG = True

SITE_URL = '/sensordatainterface/'

STATIC_ROOT = 'static/'
STATIC_URL = SITE_URL + 'static/'
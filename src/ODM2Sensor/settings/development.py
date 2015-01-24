from ODM2Sensor.settings.base import *

DATABASE_PATH = os.path.join(BASE_DIR, "Internal.sqlite3")
DATABASES['default']['NAME'] = DATABASE_PATH

DEBUG = True
TEMPLATE_DEBUG = True

STATIC_URL = '/static/'

SITE_URL = ''
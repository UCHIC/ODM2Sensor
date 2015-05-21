from ODM2Sensor.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = True

SITE_URL = '/ODM2Sensor/'

STATIC_ROOT = 'static/'
STATIC_URL = SITE_URL + 'static/'

LOGIN_REDIRECT_URL = SITE_URL + 'home/'

DEFAULT_DB = DATABASES['default']
DEFAULT_DB['ENGINE'] = ODM2_configs['ENGINE']
DEFAULT_DB['NAME'] = 'ODM2Equipment_config'
DEFAULT_DB['USER'] = ODM2_configs['USER']
DEFAULT_DB['PASSWORD'] = ODM2_configs['PASSWORD']
DEFAULT_DB['HOST'] = ODM2_configs['HOST']
DEFAULT_DB['PORT'] = ODM2_configs['PORT']
DEFAULT_DB['TEST_DEPENDENCIES'] = []
DEFAULT_DB['OPTIONS'] = {
    'driver': ODM2_configs['OPTIONS']['driver'],
    'host_is_server': ODM2_configs['OPTIONS']['host_is_server'],
}
# This is an example. Insert sensitive data depending on environment
ODM2_configs = {
    'ENGINE': 'sql_server.pyodbc',
    'NAME': 'newerName',
    'USER': 'newerUser',
    'PASSWORD': 'DbPaSsWoRd123',
    'HOST': 'MACHINE/HOSTNAME',
    'PORT': '8000',

    'OPTIONS': {
            'driver': 'DRIVER NAME AND VERSION',
            'host_is_server': True,
        },
}

secret_key = 'random_secret_key_like_so_7472873649836'
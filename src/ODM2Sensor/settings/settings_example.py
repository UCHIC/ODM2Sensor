# This is an example. Create file called settings.py and change information there
# Keep that file untracked.
ODM2_configs = {
    'ENGINE': 'sql_server.pyodbc',
    'NAME': 'DBNAME',
    'USER': 'USERNAME',
    'PASSWORD': 'PASSWORD',
    'HOST': 'HOST/HOSTNAME',
    'PORT': '',

    'OPTIONS': {
            'driver': 'DRIVER AND VERSION',
            'host_is_server': True,
        },
}

secret_key = 'random_secret_key_like_so_7472873649836'
# This is an example. Insert sensitive data depending on environment
ODM2_configs = {
    'ENGINE': 'sql_server.pyodbc',
        'NAME': 'ODM2Equipment',
        'USER': 'Mario',
        'PASSWORD': 'defaultPass123',
        'HOST': 'MANGO\SQLEXPRESS',
        'PORT': '',

    'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
            'host_is_server': True,
        },
}

secret_key = 'random_secret_key_like_so_7472873649836'
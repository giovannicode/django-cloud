from settings import *

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'cloud_db',
        'USER': 'cloud_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
        }
    }


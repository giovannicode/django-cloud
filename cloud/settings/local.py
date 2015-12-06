from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'website_db',
        'USER': 'website_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
        }
    }


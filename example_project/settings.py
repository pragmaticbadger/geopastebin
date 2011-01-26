import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geopastebin',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

PROJECT_ROOT = os.path.dirname(__file__)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

OLWIDGET_MEDIA_URL = '/static/olwidget/'

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'notverysecret'

ROOT_URLCONF = 'example_project.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    # These apps required for geopastebin.
    'django.contrib.gis',
    'geopastebin',
    'olwidget',
)

# Include any settings in local_settings.py
try:
    from local_settings import *
except ImportError:
    pass

import os
PROJECT_DIR = os.path.dirname(__file__)
PROJECT_NAME = 'pyl'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
STATIC_DOC_ROOT = False
STATIC_SERVE_MEDIA = False

ADMINS = (
    ('Elena Williams', 'ele.wil@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), "dev.dat"),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Australia/Sydney'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = '/home/elena/webapps/media/%s/' % PROJECT_NAME
MEDIA_URL = '/media/%s/' % PROJECT_NAME
ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = 'imept_svc5#o)rvj_l6avb(b*3f04j2b_6ka04yj_+4b5%5*v+'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = '%s.urls' % PROJECT_NAME

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"), 
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    
    'apps.newsletter',
    
    ## 'photologue',
    ## 'tagging',
    'django.contrib.admindocs',	
    'django.contrib.admin',
)



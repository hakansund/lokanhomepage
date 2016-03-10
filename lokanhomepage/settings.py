"""
Django settings for lokanhomepage project.

"""

from django.conf import global_settings
from unipath import Path
from YamJam import yamjam

SECRET_KEY = yamjam()['lokanhomepage']['secret_key']

DEBUG = yamjam()['lokanhomepage']['debug']
TEMPLATE_DEBUG = yamjam()['lokanhomepage']['template_debug']

ALLOWED_HOSTS = yamjam()['lokanhomepage']['allowed_hosts']

BASIC_INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members',
    'activities',
    'foundation',
    'funding',
    'notifications',
    'braces',
)

EXTRA_INSTALLED_APPS = tuple(yamjam()['lokanhomepage']['extra_installed_apps'])

INSTALLED_APPS = BASIC_INSTALLED_APPS + EXTRA_INSTALLED_APPS

BASIC_MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

EXTRA_MIDDLEWARE_CLASSES = tuple(
    yamjam()['lokanhomepage']['extra_middleware_classes'])

MIDDLEWARE_CLASSES = BASIC_MIDDLEWARE_CLASSES + EXTRA_MIDDLEWARE_CLASSES

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + [
    'django_settings_export.settings_export', ]

SETTINGS_EXPORT = ['BUSINESS_YEAR', 'MEMBERSHIP_FEE']

ROOT_URLCONF = 'lokanhomepage.urls'

WSGI_APPLICATION = 'lokanhomepage.wsgi.application'

dbcfg = yamjam()['lokanhomepage']['database']

DATABASES = {
    'default': {
        'ENGINE': dbcfg['engine'],
        'NAME': dbcfg['name'],
        'USER': dbcfg['user'],
        'PASSWORD': dbcfg['password'],
        'HOST': dbcfg['host'],
        'PORT': dbcfg['port'],
    }
}

BASE_DIR = Path(__file__).ancestor(2)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
LANGUAGE_CODE = 'sv-se'
TIME_ZONE = 'Europe/Stockholm'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'
STATIC_ROOT = '/var/www/static/'
STATIC_URL = '/static/'
#TEMPLATE_DIRS = BASE_DIR.child('templates'),
STATICFILES_DIRS = BASE_DIR.child('static'),
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = yamjam()['lokanhomepage']['gmail']['user']
EMAIL_HOST_PASSWORD = yamjam()['lokanhomepage']['gmail']['password']

# Unique for lokan.org
BUSINESS_YEAR = 2015
MEMBERSHIP_FEE = 100

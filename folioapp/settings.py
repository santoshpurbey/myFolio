"""
Django settings for folioapp project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# set the SECURE_HSTS_SECONDS
SECURE_HSTS_SECONDS = 3600
# recomended
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# set X_FRAME_OPTIONS
X_FRAME_OPTIONS = 'DENY'

#  SECURE_CONTENT_TYPE_NOSNIFF set to True, so your pages will not be served with an 'x-content-type-options: nosniff' header
SECURE_CONTENT_TYPE_NOSNIFF = True

# SECURE_BROWSER_XSS_FILTER set to True, so your pages will not be served with an 'x-xss-protection: 1; mode=block' header
SECURE_BROWSER_XSS_FILTER = True

# SESSION_COOKIE_SECURE is not set to True. Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
SESSION_COOKIE_SECURE = True

# set CSRF_COOKIE_SECURE to True
CSRF_COOKIE_SECURE = True
# set CSRF_COOKIE_HTTPONLY to True
CSRF_COOKIE_HTTPONLY = True

# SECURITY WARNING: keep the secret key used in production secret!
from django.core.exceptions import ImproperlyConfigured
def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost']

#DEBUG = True

#ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'folioapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

WSGI_APPLICATION = 'folioapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'folio_db',
        'USER' : 'root',
        'PASSWORD' : 'root',
        'HOST' : '',
        'PORT' : '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Athens'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

ACCOUNT_ACTIVATION_DAYS = 7

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'kkampardi@gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_PORT = 1025
LOGIN_REDIRECT_URL = "home"

"""
print 'Settings.py STATIC_ROOT: %s' % (STATIC_ROOT)
print 'Settings.py STATIC_URL: %s' % (STATIC_URL)
"""

### settings.py file
### settings that are not environment dependent
try:
    from settings_production import *
except ImportError:
    pass

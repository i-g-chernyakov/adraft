# -*- coding: utf-8 -*-

"""
Django settings for adraft project.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import logging.config
from pathlib import PurePath

import dj_database_url
from django.urls import reverse_lazy

from adraft import config
from adraft.settings._logging import LOGGING


config.load()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = PurePath(__file__).parent.parent

# Disable Django's logging setup
LOGGING_CONFIG = None
logging.config.dictConfig(LOGGING)
log = logging.getLogger(__name__)

if config.config_file:
    log.info("Config loaded from %s.", config.config_file)
else:
    log.info("Config loaded from environment.")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEBUG

ALLOWED_HOSTS = config.ALLOWED_HOSTS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "adraft.notes",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

ROOT_URLCONF = "adraft.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR.joinpath('templates'),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "adraft.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {"default": dj_database_url.parse(config.DATABASE_URL)}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR.joinpath('locales'),
]


FIXTURE_DIRS = [
    BASE_DIR.joinpath('fixtures'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR.joinpath(),
]
STATIC_ROOT = BASE_DIR.joinpath('static')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


PROTECTED_ROOT = MEDIA_ROOT.joinpath('protected')
PUBLIC_ROOT = MEDIA_ROOT.joinpath('public')
SENDFILE_ROOT = PROTECTED_ROOT
SENDFILE_URL = '/protected/'


if DEBUG:
    SENDFILE_BACKEND = 'sendfile.backends.development'
else:
    SENDFILE_BACKEND = 'sendfile.backends.simple'


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

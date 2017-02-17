from adraft.settings.base import *

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('ADRAFT_DATABASE_NAME', ''),
        'USER': os.environ.get('ADRAFT_DATABASE_USER', ''),
        'PASSWORD': os.environ.get('ADRAFT_DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('ADRAFT_DATABASE_HOST', ''),
        'PORT': os.environ.get('ADRAFT_DATABASE_PORT', ''),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


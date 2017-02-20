from adraft.settings.base import *

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

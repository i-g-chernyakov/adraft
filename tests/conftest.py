# -*- coding: utf-8 -*-

import sys
from os.path import dirname, abspath

import django
from django.conf import settings


PROJECT_PATH = dirname(dirname(abspath(__file__)))

sys.path = [dirname(PROJECT_PATH), PROJECT_PATH] + sys.path


# `pytest` automatically calls this function once when tests are run.
def pytest_configure():
    settings.DEBUG = False
    django.setup()

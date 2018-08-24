# -*- coding: utf-8 -*-

"""
Base config and manage.

"""

import base64
import os

from goodconf import GoodConf, Value


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adraft.settings")


class Config(GoodConf):
    """Configuration for adraft"""
    DEBUG = Value(default=False, help="Enable debugging.")
    SECRET_KEY = Value(
        initial=lambda: base64.b64encode(os.urandom(60)).decode(),
        help="a long random string you keep secret "
        "https://docs.djangoproject.com/en/2.0/ref/settings/#secret-key",
    )
    DATABASE_URL = Value(default="postgres://localhost:5432/adraft")
    ALLOWED_HOSTS = Value(
        default=["*"],
        help="Hosts allowed to serve the "
        "site "
        "https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts",
    )


config = Config(
    file_env_var="ADRAFT_CONF",
    default_files=["adraft.yml"],
)


def generate_config():
    """Entrypoint for dumping out sample config"""
    print(config.generate_yaml())

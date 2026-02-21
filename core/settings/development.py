"""
Configurações de desenvolvimento.
Use: DJANGO_SETTINGS_MODULE=core.settings.development (ou deixe padrão em core.settings).
"""
from .base import *  # noqa: F401, F403

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "[::1]",
]

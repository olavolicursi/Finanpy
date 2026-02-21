"""
Package de settings: por padrão usa development.
Para produção: export DJANGO_SETTINGS_MODULE=core.settings.production
"""
from .development import *  # noqa: F401, F403

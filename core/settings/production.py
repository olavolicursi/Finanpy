"""
Configurações de produção.
Use: DJANGO_SETTINGS_MODULE=core.settings.production
Defina as variáveis de ambiente: SECRET_KEY, ALLOWED_HOSTS (e opcionalmente DATABASE_PATH).
"""
import os
from pathlib import Path

from .base import *  # noqa: F401, F403

DEBUG = os.environ.get("DEBUG", "false").lower() in ("1", "true", "yes")

# SECURITY: SECRET_KEY obrigatória em produção (fallback para Docker dev)
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-change-me-in-production")

# Hosts permitidos (separados por vírgula em ALLOWED_HOSTS)
_allowed = os.environ.get("ALLOWED_HOSTS", "")
ALLOWED_HOSTS = [h.strip() for h in _allowed.split(",") if h.strip()]
if not ALLOWED_HOSTS and not DEBUG:
    ALLOWED_HOSTS = ["*"]

# Banco de dados: em Docker use DATABASE_PATH para persistência (ex: /app/db_data/db.sqlite3)
if os.environ.get("DATABASE_PATH"):
    DATABASES["default"]["NAME"] = Path(os.environ["DATABASE_PATH"])

# Arquivos estáticos: coleta com python manage.py collectstatic
# STATIC_ROOT já definido em base; em produção sirva esta pasta via web server

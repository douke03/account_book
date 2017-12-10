"""
WSGI config for account_book project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import pymysql
from django.core.wsgi import get_wsgi_application

pymysql.install_as_MySQLdb()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "account_book.settings.settings")

application = get_wsgi_application()

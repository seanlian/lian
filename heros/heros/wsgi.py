"""
WSGI config for heros project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'heros.settings')
sys.path.append('/var/www/html/django/heros')
application = get_wsgi_application()

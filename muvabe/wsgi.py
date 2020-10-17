import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'muvabe.settings')
# setting for production env
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'muvabe.settings.prod')
application = get_wsgi_application()
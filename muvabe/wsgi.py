import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'muvabe.settings')
#etting for production env
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'muvabe.settings.dev')
application = get_wsgi_application()
# xbjkbcjkbkc
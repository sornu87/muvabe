from muvabe.settings.base import *

# Sobrecarregar os settings aqui

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
import dj_database_url
db_from_env =  dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


DEBUG = True

try:
    from muvabe.settings.local import *
except:
     pass

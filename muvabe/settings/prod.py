from muvabe.settings.base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbcfvfu89vshg7',
        'USER': 'cqpbambwqaevbk',
        'PASSWORD': '0ad686983a933db4df5be8666cc28ffbe1957eff09830f781c275392ac579c26',
        'HOST': 'ec2-34-200-72-77.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}




try:
    from muvabe.settings.local import *
except:
    pass

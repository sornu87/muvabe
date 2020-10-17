from muvabe.settings.base import *

# Sobrecarregar os settings aqui

DEBUG = True

try:
    from muvabe.settings.local import *
except:
     pass

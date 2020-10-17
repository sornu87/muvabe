from muvabe.settings.base import *

# Sobrecarregar os settings aqui

DEBUG = False

try:
    from muvabe.settings.local import *
except:
     pass

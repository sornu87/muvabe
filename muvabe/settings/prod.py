from muvabe.settings.base import *

DEBUG = False


try:
    from muvabe.settings.local import *
except:
    pass

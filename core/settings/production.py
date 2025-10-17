from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
CSRF_TRUSTED_ORIGINS = ['https://mjes.ir',
    "https://www.mjes.ir",]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
print("im in productino")

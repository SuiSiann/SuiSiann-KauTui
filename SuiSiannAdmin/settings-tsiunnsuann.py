import os
from .settings import *  # noqa

VIRTUAL_HOST = os.getenv('HOKBU_DOMAIN_NAME')

ALLOWED_HOSTS = [
    # For deploy
    VIRTUAL_HOST,
]

CSRF_TRUSTED_ORIGINS = [
    'https://' + VIRTUAL_HOST,
]

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

STATIC_ROOT = '/staticfiles/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'ithuan',
        'HOST': 'postgres',
        'PORT': '',
    }
}

AWS_S3_USE_SSL = True
AWS_S3_SIGNATURE_VERSION = 's3v4'

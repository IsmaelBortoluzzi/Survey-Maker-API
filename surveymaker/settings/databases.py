from mongoengine import connect
import django.conf
import os


if django.conf.settings.DEBUG:
    suffix = 'DEV'
else:
    suffix = 'PROD'

# Postgres default SQL database configuration

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get(f'DATABASE_NAME_{suffix}'),
        'USER': os.environ.get(f'DATABASE_USER_{suffix}'),
        'PASSWORD': os.environ.get(f'DATABASE_PASSWORD_{suffix}'),
        'HOST': os.environ.get(f'DATABASE_HOST_{suffix}'),
        'PORT': os.environ.get(f'DATABASE_PORT_{suffix}'),
    },
}

# Mongo NoSQL database configuration

MONGO_CONNECTION = {
    'db': os.environ.get(f'MONGO_NAME_{suffix}'),
    'host': os.environ.get(f'MONGO_HOST_{suffix}'),
    'username': os.environ.get(f'MONGO_USER_{suffix}'),
    'password': os.environ.get(f'MONGO_PASSWORD_{suffix}'),
    'port': int(os.environ.get(f'MONGO_PORT_{suffix}')),
    'authentication_mechanism': os.environ.get(f'AUTHENTICATION_MECHANISM_{suffix}'),
}

connect(**MONGO_CONNECTION)

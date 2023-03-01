from mongoengine import connect
import django.conf
import os


def get_postgresql_host():
    if django.conf.settings.DEBUG:
        return os.environ.get('DATABASE_HOST')
    return os.environ.get('DATABASE_HOST_DOCKER_COMPOSE')


def get_mongodb_host():
    if django.conf.settings.DEBUG:
        return os.environ.get('MONGO_HOST')
    return os.environ.get('MONGO_HOST_DOCKER_COMPOSE')


# Postgres default SQL database configuration

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': get_postgresql_host(),
        'PORT': os.environ.get('DATABASE_PORT'),
    },
}

# Mongo NoSQL database configuration

MONGO_CONNECTION = {
    'db': os.environ.get('MONGO_INITDB_DATABASE'),
    'host': get_mongodb_host(),
    'username': os.environ.get('MONGO_INITDB_ROOT_USERNAME'),
    'password': os.environ.get('MONGO_INITDB_ROOT_PASSWORD'),
    'port': int(os.environ.get('MONGO_PORT_DJANGO')),
    'authentication_mechanism': os.environ.get('AUTHENTICATION_MECHANISM'),
}

connect(**MONGO_CONNECTION)

from mongoengine import connect
import os

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Postgres default SQL database configuration

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    },
}

# Mongo NoSQL database configuration

MONGO_CONNECTION = {
    'db': os.environ.get('MONGO_INITDB_DATABASE'),
    'host': os.environ.get('MONGO_HOST'),
    'username': os.environ.get('MONGO_INITDB_ROOT_USERNAME'),
    'password': os.environ.get('MONGO_INITDB_ROOT_PASSWORD'),
    'port': int(os.environ.get('MONGO_PORT_DJANGO')),
    'authentication_mechanism': os.environ.get('AUTHENTICATION_MECHANISM'),
}

connect(**MONGO_CONNECTION)

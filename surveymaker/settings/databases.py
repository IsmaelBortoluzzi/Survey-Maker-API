import mongoengine
import os

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

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

MONGO_NAME = os.environ.get('MONGO_INITDB_DATABASE')
MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_USER = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
MONGO_PASS = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')

MONGO_DATABASE_HOST = 'mongodb://%s:%s@%s/%s' % (MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_NAME)

mongoengine.connect(MONGO_NAME, host=MONGO_DATABASE_HOST)
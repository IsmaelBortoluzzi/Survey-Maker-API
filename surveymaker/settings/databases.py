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
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': os.environ.get('MONGO_INITDB_DATABASE'),
        'CLIENT': {
            'host': os.environ.get('MONGO_HOST'),
            'port': int(os.environ.get('MONGO_PORT_DJANGO')),
            'username': os.environ.get('MONGO_INITDB_ROOT_USERNAME'),
            'password': os.environ.get('MONGO_INITDB_ROOT_PASSWORD'),
        },
        'TEST': {
            'MIRROR': 'default',
        },
    }
}

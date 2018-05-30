import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 's!z$a5+3a2o!=$p4jtzq%mm-i(q9-__*-y7chmxk@j-y*zvdb7'

DEBUG = True

INSTALLED_APPS = (
    'conf',
)

MIDDLEWARE = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'django.db.backends.sqlite3'
        # 'django.db.backends.postgresql_psycopg2'
        # 'django.db.backends.mysql'
        # 'django.db.backends.oracle'
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'HOST' : ...
        # 'PORT' : ...
        # 'USER' : ...
        # 'PASSWORD' : ...
    }
}

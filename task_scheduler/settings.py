#
#   Purpose: Django main settings file

import os
from pathlib import Path

import environ

# Get paths to important directories; stored as Pathlib paths
PROJECT_ROOT = Path(__file__).parents[1]
# Read .env file
env = environ.Env(CONFIG_PATH=(str, None), CURRENT_ENV=(str, None))
env.read_env(str(PROJECT_ROOT.joinpath(".env")))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = str(PROJECT_ROOT.joinpath("static"))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'django_celery_results',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'task_scheduler.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Logging Setup
LOGGING = {
    'version': 1,
    # Version of logging
    'disable_existing_loggers': False,
    # disable logging
    # Handlers #############################################################
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'task_scheduler.log',
        },
        ########################################################################
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    # Loggers ####################################################################
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG')
        },
    },
}

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = dashboard_config.secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default=True)
ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost']

# Settings for celery and redis configurations
redis_host = 'redis'
CELERY_BROKER_URL = f'redis://{redis_host}:6379'

CELERY_ACCEPT_CONTENT = ['json']

CELERY_RESULT_BACKEND = "django-db"

CELERY_TASK_SERIALIZER = 'json'

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default='<UPDATE THIS>')

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# THIS WILL CONNECT TO SQLITE DATABASE. USE THIS IF YOU WANT TO RUN IT DIRECTLY USING
# COMMAND 'python manage.py runserver
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'task_database',  # This is where you put the name of the db file.
        # If one doesn't exist, it will be created at migration time.
    }
}

# USE THIS DATABASE CONFIGURATION IF YOUR ARE RUNNING IT WITH DOCKER
# THIS WILL CONNECT TO POSTGRES CONTAINER WHEN 'docker-compose up' is used

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": 'task_scheduler',
#         "USER": 'admin',
#         "PASSWORD": 'dbpassword',
#         "HOST": 'postgres',
#         "PORT": '5432',
#         "TEST": {"NAME": "test_task_scheduler"},
#     }
# }

# Path to WSGI application
WSGI_APPLICATION = "task_scheduler.wsgi.application"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

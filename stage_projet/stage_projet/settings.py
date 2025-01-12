# Django settings for stage_projet project.

import os
from pathlib import Path
import environ
from celery.schedules import crontab # pour celery
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

env = environ.Env()
environ.Env.read_env()

LOGIN_URL = 'login'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_NAME = 'sessionid'  # Nom du cookie de session

# Configuration du modèle utilisateur personnalisé
AUTH_USER_MODEL = "listings.CustomUser"

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-4*mw^d-76p=hr633o94b02ar!&)yqik)u!ca2kp%9=ped%9+#e'
DEBUG = True  

ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS =["http://",'http://172.0.0.1:4001','127.0.0.1','http://127.0.0.1:8000']
# = ["http://",'http://127.0.0.1:4001','127.0.0.1','http://127.0.0.1:8000']
#CSRF_TRUSTED_ORIGINS =[
   # 'http://127.0.0.1:4001',  # Adjust the port if you're using a different one
   # 'http://localhost:4001',
   # 'http://127.0.0.1:8000',   # Add localhost for good measure
#]
#CRSF_COOKIE_SECURE = int(0)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'listings',
    'django_celery_beat',  # pour l'email celery
    'django_celery_results',  # pour l'email celery
    'bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'listings.middleware.DisableCacheMiddleware',
]

ROOT_URLCONF = 'stage_projet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'stage_projet.wsgi.application'

#Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test1',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',#192.168.80.27
        'PORT': '5432',
    }
}

#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.postgresql',
        #'NAME': os.getenv('DB_NAME'),
        #'USER': os.getenv('DB_USER'),
        #'PASSWORD': os.getenv('PASSWORD'),
        #'HOST': os.getenv('DB_HOST'),
        #'PORT': os.getenv('DB_PORT', '5432'),  # 5432 par défaut
   #}
#}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#Internationalization
LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'listings'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'josephinedorianekouadio@gmail.com'
EMAIL_HOST_PASSWORD = 'qxig fhjz sjiq iehj'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'celery<josephinedorianekouadio@gmail.com>'

# Celery configuration

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'  # fuseau horaire

#CELERY_BEAT_SCHEDULER ={
   #'send-email-every-day-at-17':{
       #'task':'stage_projet.tasks.relance',
       #'schedule': crontab('*/15'),
  # }
#}
#demander

#tache

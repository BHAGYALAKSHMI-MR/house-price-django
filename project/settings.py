import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'dummy-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'predictor',
]

MIDDLEWARE = []

ROOT_URLCONF = 'project.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'predictor/templates')],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': []},
}]

WSGI_APPLICATION = 'project.wsgi.application'

STATIC_URL = '/static/'
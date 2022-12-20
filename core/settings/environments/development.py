import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='envs/.env.development')

DEBUG = True

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

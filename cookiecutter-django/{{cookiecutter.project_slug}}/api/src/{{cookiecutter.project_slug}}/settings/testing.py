from {{ cookiecutter.project_slug }}.settings.base import *

SECRET_KEY = 'insecure'
CELERY_TASK_ALWAYS_EAGER = True
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
TEST_LOGIN = '{{ cookiecutter.project_slug }}.admin@amsterdam.nl'
SITE_DOMAIN = 'localhost:8000'

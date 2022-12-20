INSTALLED_APPS = [
    # third-party Apps
    'ckeditor',
    'crispy_forms',
    'rest_framework',
    'markdown',
    # core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local apps
    'apps.blog.apps.BlogConfig',
    'apps.account.apps.AccountConfig',
]

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Auth Config
AUTH_USER_MODEL = 'account.User'
LOGIN_URL = 'account:login'
LOGIN_REDIRECT_URL = 'account:profile'

# Static Config
STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'asset'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media Config
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


# Crispy Config
CRISPY_TEMPLATE_PACK = 'bootstrap4'

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

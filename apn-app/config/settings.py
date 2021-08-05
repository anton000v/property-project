import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATHLIB_BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

load_dotenv(dotenv_path=str(PATHLIB_BASE_DIR / '.env'))
env_path = PATHLIB_BASE_DIR / '.env'

# For russian language in admin interface
# LANGUAGE_CODE = 'ru'
# USE_I18N = True
# # USE_L10N = True
# LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
# LANGUAGES = [
#     ('en', _('English')),
#     ('ru', _('Russian')),
# ]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'asnovostroi.com.ua']

# Django corsheaders
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = [
#     # 'http://localhost:8080',
#     'http://localhost:8080',
# ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'api',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_filters',
    'drf_yasg'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'api.pagination.CustomPageNumber',
    # 'PAGE_SIZE': 10
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


# # All settings common to all environments
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'app_static')
#
# STATIC_DIR = os.path.join(BASE_DIR, 'api', 'static')
# STATICFILES_DIRS = [
#     STATIC_DIR,
#     os.path.join(STATIC_DIR, 'admin')
# ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'api', 'media')

# ----------- LOGGING:
APN_LOG_CONSOLE_LEVEL = os.environ.get('APN_LOG_LEVEL')
APN_LOG_FILE_LEVEL = os.environ.get('APN_LOG_FILE_LEVEL')
APN_LOG_FILE_PATH = os.environ.get('APN_LOG_FILE_PATH')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '[{asctime}] {message}',
            'style': '{',
        },
        'file': {
            'format': '{levelname} [{asctime}] {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'file': {
            'level': APN_LOG_FILE_LEVEL,
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, APN_LOG_FILE_PATH),
        },
        'console': {
            'level': APN_LOG_CONSOLE_LEVEL,
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['file', 'console'],
            'propagate': True,
            'level': 'INFO',
        },
    },
}

GOOGLE_PERSONAL_KEY = os.getenv('GOOGLE_PERSONAL_KEY')

VUE_APP_API_USERNAME = os.getenv('VUE_APP_API_USERNAME')
VUE_APP_API_PASS = os.getenv('VUE_APP_API_PASS')

SUPERUSER_USERNAME = os.getenv('SUPERUSER_USERNAME')
SUPERUSER_PASS = os.getenv('SUPERUSER_PASS')

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        # 'Basic': {
        #       'type': 'basic'
        # },
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

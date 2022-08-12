from pathlib import Path
import sys, os

import django_heroku, dj_database_url
from decouple import config

# djangorestframework
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR,'apps'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r81h8mty!p$0g2^4ephgz1(alkmnfj9*y5o91=t6#-*v4dfk$y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Local apps
    'users.apps.UsersConfig',

    # Third party apps
    'rest_framework',
    'rest_framework.authtoken',
    "rest_framework_simplejwt.token_blacklist",
    'djoser',
    'rest_framework_simplejwt',
    'drf_yasg'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djoser_user_auth.urls'

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

WSGI_APPLICATION = 'djoser_user_auth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
    ),
}

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}

DJOSER = {
    'SEND_CONFIRMATION_EMAIL': True,
    'LOGIN_FIELD': 'email',
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'api/auth/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'HIDE_USERS': False,
    'SERIALIZERS': {
        'user': 'users.serializers.ReadUserSerializer',
        # 'user': 'djoser.serializers.UserSerializer',

        # 'user_create': 'djoser.serializers.UserCreateSerializer',
        'user_create': 'users.serializers.UserRegistrationSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
        'current_user': 'djoser.serializers.UserSerializer', # Get own user data.
        'password_reset': 'djoser.serializers.SendEmailResetSerializer',
        'password_reset_confirm': 'djoser.serializers.PasswordResetConfirmSerializer',
        'password_reset_confirm_retype': 'djoser.serializers.PasswordResetConfirmRetypeSerializer',
        'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,

        
        'token': 'djoser.serializers.TokenSerializer',
        'token_create': 'djoser.serializers.TokenCreateSerializer',
    },
    'PERMISSIONS': {
        'activation': ['rest_framework.permissions.AllowAny'],
        
        # 'set_password': ['rest_framework.permissions.CurrentUserOrAdmin'],
        
        # 'set_username': ['rest_framework.permissions.CurrentUserOrAdmin'],
        # 'user_delete': ['rest_framework.permissions.CurrentUserOrAdmin'],
        # 'user': ['rest_framework.permissions.CurrentUserOrAdmin'],
        # 'user': ['rest_framework.permissions.AllowAny'],
        'user_list': ['rest_framework.permissions.IsAdminUser'],
        'token_create': ['rest_framework.permissions.AllowAny'],
        'token_destroy': ['rest_framework.permissions.IsAuthenticated'],
    }
}

LOGIN_URL = 'auth/jwt/create'
# LOGIN_URL = 'admin/login/'

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            "name": "api_key",
            "in": "header"
        }
    },
    'USE_SESSION_AUTH': True
}

django_heroku.settings(locals())


"""
Django settings for empacadoralitoral project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zae^g$kvf(%00j+hm0$40+fg!%0fk-cb@+j4=j0*th5#2(94+o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DJANGO_APPS = [
    # Servidor HTTPS para pruebas
    # "sslserver",
    #---------------------------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #generar qr con python
    'qr_code',
    #-----------------------
] 


LOCAL_APPS = [
    'django.contrib.humanize',
    'apps.compania',
    'apps.conductor',
    'apps.empleado',
    'apps.equipo',
    'apps.inicio',
    'apps.prestamos',
    'apps.remision',
    'apps.seguridad',
    'apps.vehiculo',
    'apps.hielo_proceso',
    'apps.camaron',
    # DEBUG TOOLBAR
    # 'debug_toolbar',
    #-----------------
]
# Application definition


INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # DEBUG TOOLBAR
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    #---------------
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'empacadoralitoral.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates"),], 
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

WSGI_APPLICATION = 'empacadoralitoral.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'empacadoralitoral',
        'USER': 'empacadoralitoral',
        'PASSWORD': '668246Litoral',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'empacadoralitoral',
#         'USER': 'root',
#         'PASSWORD': 'dimeobek',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# AUTH_USER_MODEL = 'users.User'

# LANGUAGE_CODE = 'es-HN'
LANGUAGE_CODE = 'es-EN'

TIME_ZONE = 'America/Tegucigalpa'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# LOGIN_URL = '/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'jorgeescoto18@gmail.com'
# EMAIL_HOST_PASSWORD = 'escoto100'


LOGIN_URL = '/'
STATIC_URL = '/static/'
# STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'global_static'),
# )
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static/'),]

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticos/')
TEMPLATE_DIRS=(BASE_DIR, 'templates')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR,'global_static'),]
# STATIC_ROOT = os.path.join(BASE_DIR,'static')



# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR,'media')


#LOGIN_URL = '/seguridad/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'control.hielo.litoral@gmail.com'
EMAIL_HOST_PASSWORD = 'Litoral100'


# DEBUG TOOLBAR
# def show_toolbar(request):
#     if not request.is_ajax() and request.user and request.user.username == 'admin':
#         return True
#     return False

# DEBUG_TOOLBAR_CONFIG = {

#     'SHOW_TOOLBAR_CALLBACK' : 'empacadoralitoral.settings.show_toolbar',

# }
#----------------------------------


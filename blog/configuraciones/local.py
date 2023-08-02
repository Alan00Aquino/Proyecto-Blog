from .settings import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Proyecto_Blog',
        'USER': 'root',
        'PASSWORD': 'F3rn3t4340.A',  #Alan #F3rn3t4340.A
        'HOST': 'localhost',  
        'PORT': '3306',  
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'proyectblog827@gmail.com'
EMAIL_HOST_PASSWORD = 'nqhqivdafeyyxizl'   #4dmin1239


DEBUG = True

ALLOWED_HOSTS = ['localshost', '127.0.0.1']
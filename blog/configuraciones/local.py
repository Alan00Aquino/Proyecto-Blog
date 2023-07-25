from .settings import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'proyecto_final',
        'USER': 'root',
        'PASSWORD': 'Z37796498',
        'HOST': 'localhost',  
        'PORT': '3306',  
    }
}

#Este es un comentario de prueba
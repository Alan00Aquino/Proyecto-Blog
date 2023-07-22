from .settings import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Proyecto_Blog',
        'USER': 'root',
        'PASSWORD': 'F3rn3t4340.A',
        'HOST': 'localhost',  
        'PORT': '3306',  
    }
}
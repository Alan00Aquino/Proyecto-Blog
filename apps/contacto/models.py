from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombre = models.CharField(max_length = 100)
    email = models.EmailField()
    mensaje = models.CharField(max_length = 255)
    numero_tel = models.CharField(max_length = 20)

    def str(self):
        return self.nombre


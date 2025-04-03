from django.db import models

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    edad = models.IntegerField(null=True, blank=True)
    ciudad_nacimiento = models.CharField(max_length=255, null=True, blank=True)
    ciudad_residencia = models.CharField(max_length=255, null=True, blank=True)
    afiliada = models.BooleanField(default=False)
    diagnostico_confirmado = models.BooleanField(default=False)

    def __str__(self):
        return self.username

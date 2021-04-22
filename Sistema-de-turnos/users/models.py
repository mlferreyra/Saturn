from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import CustomUserManager


# Create your models here.
class Registro(AbstractBaseUser):
        idUsuario = models.AutoField(primary_key=True)
        email = models.CharField(max_length=50, unique=True)
        nombre = models.CharField(max_length=50)
        apellido = models.CharField(max_length=50)
        dni = models.BigIntegerField()
        telefono = models.BigIntegerField()
        fechaDeNacimiento = models.DateField(auto_now=False, auto_now_add=False)
        date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True, null=True)
        last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

        USERNAME_FIELD = 'email'
        
        SEXO = (
            ('M', 'Masculino'),
            ('F', 'Femenino'),
            ('O', 'Otros'),
        )
        sexo = models.CharField(max_length=1, choices=SEXO)
        
        objects = CustomUserManager()

        def __str__(self):
            return self.email

from django.db import models
from django.utils import timezone
from users.models import Registro

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class Especialidad(models.Model):
    especialidadId = models.AutoField(primary_key=True)
    descripcion    = models.CharField(max_length=70) 
    
    def __str__(self):
        return self.descripcion
    
    class Meta:
        db_table = 'gestionturnos_especialidad'

class ObraSocial(models.Model):
    ObraSocialId  = models.AutoField(primary_key=True)
    descripcion   = models.CharField(max_length=50)   

    def __str__(self):
        return '{}'.format(self.descripcion)

class Medico(models.Model):
    medicoId    = models.AutoField(primary_key=True)
    matriculaId = models.IntegerField()
    nombre      = models.CharField(max_length=50)
    dni         = models.IntegerField()
    email       = models.CharField(max_length=50)
    telefono    = models.IntegerField()
    obrasocial  = models.ForeignKey(ObraSocial, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)

class Turno(models.Model):
    TurnoId          = models.AutoField(primary_key=True)
    hora_turno       = models.TimeField(null=True)
    fecha_registro   = models.DateField(default=timezone.now)
    usuario          = models.ForeignKey(Registro, on_delete=models.CASCADE, null=True)
    especialidad     = models.ForeignKey(Especialidad, on_delete=models.CASCADE)    
    medico           = models.ForeignKey(Medico, on_delete=models.CASCADE)
    obrasocial       = models.ForeignKey(ObraSocial, on_delete=models.CASCADE)
    fecha_turno      = models.DateField()
    dni              = models.IntegerField()
    nombre           = models.CharField(max_length=50)
    edad             = models.PositiveSmallIntegerField(null=True)
    telefono         = models.CharField(max_length=13)
    
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    sexo             = models.CharField(max_length=1, choices=SEXO)
    mail             = models.EmailField(max_length=50)

class EspecialidadMedico(models.Model):
    medico       = models.ForeignKey(Medico, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

class ConfiguracionHoraria(models.Model):
    medico     = models.ForeignKey(Medico, on_delete=models.CASCADE)
    nombredia  = models.CharField(max_length=70)   
    hora_desde = models.TimeField()
    hora_hasta = models.TimeField()
    duracion   = models.IntegerField()

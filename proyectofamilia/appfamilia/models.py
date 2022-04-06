from django.db import models

# Create your models here.
class Familiar(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    apodo = models.CharField(max_length=40)
    nacimiento = models.DateField()



         
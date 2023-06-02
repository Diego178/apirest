from django.db import models

class Reporte(models.Model):
    esp32=models.CharField(max_length=10)
    mensaje=models.CharField(max_length=250)
    fecha=models.CharField(max_length=15)
    hora=models.CharField(max_length=10)
    latitud=models.IntegerField()
    longitud=models.IntegerField()

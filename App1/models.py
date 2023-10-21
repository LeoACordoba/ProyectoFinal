from django.db import models
from django.conf import settings

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Edad {self.edad}"


    
class Catalogo(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    valor = models.IntegerField()
    imagen = models.ImageField(upload_to='catalogo', null=True, blank = True)
    
    def __str__(self):
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Valor: {self.valor} - Imagen : {settings.MEDIA_URL}{self.imagen} "

    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Direccion: {self.direccion} - E-Mail: {self.email} - Telefono: {self.telefono}"




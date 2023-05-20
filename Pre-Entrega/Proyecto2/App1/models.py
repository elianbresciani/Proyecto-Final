from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your models here.

class Dueño(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email}"
    nombre= models.CharField(max_length=30)

    apellido= models.CharField(max_length=30)

    email= models.EmailField()

 

class Blog(models.Model):
    def __str__(self):
        return f"Nombre: {self.titulo} - Apellido {self.subtitulo} - E-Mail {self.contenido} - Profesión {self.autor}"

    titulo = models.CharField(max_length=30)

    subtitulo= models.CharField(max_length=30)

    contenido = models.CharField(max_length=500)

    autor = models.CharField(max_length=40)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    

from django.db import models
# Create your models here.

def agent_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/section_<name>/<filename>
    return 'agente/{0}'.format(filename)

class Agente(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=500)
    transicion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to=agent_directory_path)

    def __str__(self):
        return self.nombre

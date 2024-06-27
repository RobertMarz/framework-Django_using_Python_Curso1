from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200) #tenemos que ir a mysite -settings.py para conectarlo
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE) #relacion con class Project y ondelete par aque borre los hijos
    
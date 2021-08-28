from django.db import models

# Create your models here.

class ToDo(models.Model):
  description = models.CharField(max_length=150)
  completed = models.BooleanField()
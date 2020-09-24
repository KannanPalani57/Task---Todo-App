from django.db import models

# Create your models here.

class Task(models.Model):
    taskName = models.CharField(max_length = 70)
    isCompleted = models.BooleanField(default = False)
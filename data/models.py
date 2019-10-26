from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pointer = models.IntegerField(default=0)
    task_id = models.CharField(max_length=100, null=True)

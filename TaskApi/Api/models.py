from django.db import models

# Create your models here.
from django.db import models

CHOICE = [
    ('perday', 'per day'),
    ('weekly', 'weekly'),
    ('monthly', 'monthly'),
]


class Task(models.Model):
    Task_type = models.IntegerField()
    Task_desc = models.CharField(max_length=300)


class TaskTracker(models.Model):
    Task_type = models.ForeignKey(Task, on_delete=models.CASCADE)
    Update_type = models.CharField(choices=CHOICE, max_length=10)
    Email = models.EmailField(unique=True)

from django.db import models
from datetime import datetime


class ProjectModel(models.Model):
    name = models.CharField(max_length=30)
    ProjectDescription = models.TextField()
    ProjectCreated_at = models.DateTimeField(default=datetime.now())


class TaskModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    TaskDescription = models.TextField()
    TaskCreated_at = models.DateTimeField(default=datetime.now())
    Choices = [
        ('option1', 'To_Do'),
        ('option2', 'In_Progress'),
        ('option3', 'Completed'),
    ]
    status = models.CharField(max_length=15, choices=Choices, default='option1')

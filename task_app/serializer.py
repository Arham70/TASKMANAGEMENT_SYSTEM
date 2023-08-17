from rest_framework import serializers
from .models import ProjectModel, TaskModel


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = ['id', 'name', 'ProjectDescription', 'ProjectCreated_at']


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id', 'project', 'title', 'TaskDescription', 'TaskCreated_at', 'status']

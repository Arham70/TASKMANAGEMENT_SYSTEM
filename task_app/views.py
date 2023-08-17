from rest_framework import viewsets
from .models import ProjectModel, TaskModel
from .serializer import ProjectModelSerializer, TaskModelSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializer

    @action(detail=True, methods=['GET'])
    def tasks(self, request, pk=None):
        project = self.get_object()
        tasks = TaskModel.objects.filter(project=project)
        serializer = TaskModelSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelSerializer


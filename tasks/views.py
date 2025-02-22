from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .services import TaskService

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = self.get_object()
        TaskService.mark_complete(task)
        return Response({'status': 'Task marked as complete'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def reopen(self, request, pk=None):
        task = self.get_object()
        TaskService.mark_reopen(task)
        return Response({'status': 'Task marked as not completed'}, status=status.HTTP_200_OK)

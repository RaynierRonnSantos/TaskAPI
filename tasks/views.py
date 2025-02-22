from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from tasks.models import Task
from tasks.serializers import TaskSerializer
from tasks.services import TaskService  # Import Service Layer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('due_date', 'priority')
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        """Use the service layer to create a task."""
        TaskService.create_task(
            title=serializer.validated_data['title'],
            description=serializer.validated_data['description'],
            due_date=serializer.validated_data['due_date'],
            priority=serializer.validated_data['priority']
        )

    @action(detail=True, methods=["POST"])
    def complete(self, request, pk=None):
        """Mark a task as completed using the service layer."""
        task = self.get_object()
        updated_task = TaskService.mark_task_complete(task)
        return Response(TaskSerializer(updated_task).data)

    @action(detail=True, methods=["POST"])
    def reopen(self, request, pk=None):
        """Mark a task as not completed using the service layer."""
        task = self.get_object()
        updated_task = TaskService.mark_task_reopen(task)
        return Response(TaskSerializer(updated_task).data)

from datetime import datetime
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from tasks.models import Task

class TaskService:
    @staticmethod
    def create_task(title, description, due_date, priority):
        """Creates a new task and ensures due_date is not in the past."""
        if due_date < now().date():
            raise ValidationError("Due date cannot be in the past.")
        return Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            is_completed=False
        )

    @staticmethod
    def mark_task_complete(task: Task):
        """Marks a task as completed."""
        task.is_completed = True
        task.save()
        return task

    @staticmethod
    def mark_task_reopen(task: Task):
        """Reopens a task (sets is_completed to False)."""
        task.is_completed = False
        task.save()
        return task

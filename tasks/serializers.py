from rest_framework import serializers
from .models import Task
from django.utils.timezone import now

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_due_date(self, value):
        if value < now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

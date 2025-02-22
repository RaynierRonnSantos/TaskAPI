from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    id = models.AutoField(primary_key=True)  # Explicit primary key
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')

    # Additional fields to satisfy the requirement:
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update
    assigned_to = models.CharField(max_length=255, blank=True, null=True)  # Placeholder for a user system
    category = models.CharField(max_length=100, blank=True, null=True)  # Category field

    class Meta:
        ordering = ['due_date', 'priority']  # Default ordering

    def __str__(self):
        return self.title

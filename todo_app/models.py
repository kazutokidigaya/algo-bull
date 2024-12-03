from django.db import models

class TodoTask(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING_REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-set creation time
    title = models.CharField(max_length=100)  # Task title
    description = models.TextField(max_length=1000)  # Task description
    due_date = models.DateField(null=True, blank=True)  # Optional due date
    tags = models.CharField(max_length=255, blank=True)  # Optional tags (comma-separated)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')  # Task status

    def __str__(self):
        return self.title

from django.test import TestCase
from .models import TodoTask

class TodoTaskModelTest(TestCase):
    def setUp(self):
        self.task = TodoTask.objects.create(
            title="Test Task",
            description="This is a test task",
            due_date="2024-12-05",
            tags="work,priority",
            status="OPEN",
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task")
        self.assertEqual(self.task.status, "OPEN")

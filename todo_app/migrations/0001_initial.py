# Generated by Django 4.2.7 on 2024-12-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoTask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=1000)),
                ("due_date", models.DateField(blank=True, null=True)),
                ("tags", models.CharField(blank=True, max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("OPEN", "Open"),
                            ("WORKING", "Working"),
                            ("PENDING_REVIEW", "Pending Review"),
                            ("COMPLETED", "Completed"),
                            ("OVERDUE", "Overdue"),
                            ("CANCELLED", "Cancelled"),
                        ],
                        default="OPEN",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
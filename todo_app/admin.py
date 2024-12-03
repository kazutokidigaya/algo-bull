from django.contrib import admin
from .models import TodoTask

@admin.register(TodoTask)
class TodoTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'timestamp')  # Display these fields in the admin panel
    list_filter = ('status', 'due_date')  # Add filters for easy management
    search_fields = ('title', 'description')  # Searchable fields

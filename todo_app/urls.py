from django.urls import path
from .views import TodoTaskListCreateAPIView, TodoTaskDetailAPIView

urlpatterns = [
    path('tasks/', TodoTaskListCreateAPIView.as_view(), name='tasks-list-create'),
    path('tasks/<int:pk>/', TodoTaskDetailAPIView.as_view(), name='tasks-detail'),
]

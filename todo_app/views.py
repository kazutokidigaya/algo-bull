from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TodoTask
from .serializers import TodoTaskSerializer

class TodoTaskListCreateAPIView(APIView):
    def get(self, request):
        tasks = TodoTask.objects.all()
        serializer = TodoTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoTaskDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            task = TodoTask.objects.get(pk=pk)
        except TodoTask.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoTaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            task = TodoTask.objects.get(pk=pk)
        except TodoTask.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoTaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            task = TodoTask.objects.get(pk=pk)
        except TodoTask.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

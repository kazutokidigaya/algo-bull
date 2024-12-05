from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the AlgoBulls App!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo_app.urls')),  # Ensure 'todo_app.urls' is correctly set up
    path('', home_view),  # Add this for the root path
]

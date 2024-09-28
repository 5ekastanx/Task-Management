from django.urls import path, include
from .views import TasksListAPIView, TaskAPIView, TaskCreateAPIView


urlpatterns = [
    path('tasks/',TasksListAPIView.as_view()),
    path('tasks/create/',TaskCreateAPIView.as_view()),
    path('tasks/<int:pk>/',TaskAPIView.as_view()),
]

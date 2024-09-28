from rest_framework import generics
from .models import Task
from .serializers import TaskDetailSerializer, TasksListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

class TasksListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksListSerializer

class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskDetailSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        return Response(
            {
                'Ваш пост':"создан"
            }
        )

class TaskAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsAdminUser]

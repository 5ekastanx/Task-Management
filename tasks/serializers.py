from rest_framework import serializers
from .models import Task

class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TasksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

from rest_framework import serializers
from .models import Task, TaskTracker


class Task1(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskTracker1(serializers.ModelSerializer):
    class Meta:
        model = TaskTracker
        fields = '__all__'

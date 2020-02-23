from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from .models import TaskTracker, Task
from .serializer import Task1, TaskTracker1
from rest_framework import viewsets


class TaskViews(viewsets.ModelViewSet):
    serializer_class = Task1
    queryset = Task.objects.all()


class TaskTrackerView(viewsets.ModelViewSet):
    serializer_class = TaskTracker1
    queryset = TaskTracker.objects.all()


from .tasks import sendemails


def mail(request):
    sendemails.delay(5)
    return HttpResponse('Account is verified...')

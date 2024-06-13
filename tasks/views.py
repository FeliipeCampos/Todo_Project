from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from notifications.models import Notification

class TaskList(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            if request.user.is_authenticated:
                users = User.objects.all()
                notify.send(request.user, recipient=users, verb='criou uma nova tarefa', description=task.title)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskUpdate(APIView):
    def put(self, request, pk, format=None):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            if request.user.is_authenticated:
                users = User.objects.all()
                notify.send(request.user, recipient=users, verb='atualizou uma tarefa', description=task.title)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDelete(APIView):
    def delete(self, request, pk, format=None):
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TaskComplete(APIView):
    def patch(self, request, pk, format=None):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        task.completed = True
        task.save()
        if request.user.is_authenticated:
            users = User.objects.all()
            notify.send(request.user, recipient=users, verb='completou uma tarefa', description=task.title)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

class NotificationList(APIView):
    def get(self, request, format=None):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_403_FORBIDDEN)
        notifications = request.user.notifications.all()
        return Response([{
            'actor': n.actor.username,
            'verb': n.verb,
            'target': n.target,
            'description': n.description,
            'timestamp': n.timestamp
        } for n in notifications], status=status.HTTP_200_OK)

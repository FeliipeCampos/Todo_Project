from django.urls import reverse
from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        Task.objects.create(title="Test Task", description="Test Description")

    def test_task_content(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.title}'
        self.assertEqual(expected_object_name, 'Test Task')
        self.assertEqual(task.description, 'Test Description')
        
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task

class TaskAPITest(APITestCase):

    def test_create_task(self):
        url = reverse('task-list')
        data = {"title": "Test Task", "description": "Test Description"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_get_tasks(self):
        Task.objects.create(title="Test Task", description="Test Description")
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Task')

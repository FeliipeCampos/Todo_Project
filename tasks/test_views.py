from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

class TaskTests(APITestCase):

    def setUp(self):
        self.task1 = Task.objects.create(title='Task 1', description='Description 1')
        self.task2 = Task.objects.create(title='Task 2', description='Description 2')

    def test_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'New Task', 'description': 'New Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        data = {'title': 'Updated Task', 'description': 'Updated Description', 'completed': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Updated Task')
        self.assertEqual(self.task1.completed, True)

    def test_delete_task(self):
        url = reverse('task-delete', args=[self.task1.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)

    def test_mark_task_complete(self):
        url = reverse('task-complete', args=[self.task1.id])
        data = {'completed': True}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.completed, True)
